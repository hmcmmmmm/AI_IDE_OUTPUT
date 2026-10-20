#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
md2wechat.py — 把 Typora 的 Markdown 转成"可直接粘贴进微信公众号"的 HTML

核心作用：
  1. 把本地图片文件读成 base64 内嵌到 HTML 里（不再依赖磁盘路径）
  2. 把 CSS 全部写成 inline style（公众号编辑器会丢弃 <style> 和 class）
  3. 输出单文件 HTML，浏览器打开后 Ctrl+A / Ctrl+C，粘贴进公众号编辑器即可

用法：
  python md2wechat.py 文章.md                  # 生成 文章.wechat.html
  python md2wechat.py 文章.md -o out.html
  python md2wechat.py 文章.md --check          # 只诊断图片，不转换
  python md2wechat.py 文章.md --download       # 网络图片也下载并内嵌
  python md2wechat.py 文章.md --open           # 生成后自动用浏览器打开
  python md2wechat.py 文章.md --width 750      # 自定义正文宽度(px)
"""

import argparse
import base64
import io
import mimetypes
import os
import re
import sys
import urllib.parse
import urllib.request

try:
    import markdown
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("缺少依赖，请先执行：pip install markdown beautifulsoup4")

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


# ---------------------------------------------------------------- 图片解析

MAGIC = [
    (b"\x89PNG\r\n\x1a\n", "image/png"),
    (b"\xff\xd8\xff", "image/jpeg"),
    (b"GIF87a", "image/gif"),
    (b"GIF89a", "image/gif"),
    (b"BM", "image/bmp"),
    (b"RIFF", "image/webp"),
]


def sniff_mime(data: bytes, fallback: str = "image/png") -> str:
    for magic, mime in MAGIC:
        if data.startswith(magic):
            if mime == "image/webp" and data[8:12] != b"WEBP":
                continue
            return mime
    head = data[:512].lstrip()
    if head.startswith(b"<svg") or head.startswith(b"<?xml"):
        return "image/svg+xml"
    return fallback


def to_data_uri(data: bytes, mime: str) -> str:
    return "data:%s;base64,%s" % (mime, base64.b64encode(data).decode("ascii"))


def optimize_image(data: bytes, mime: str, max_width: int, quality: int):
    """等比缩放到 max_width 以内并重编码，返回 (data, mime)。失败则原样返回。"""
    if not HAS_PIL or max_width <= 0:
        return data, mime
    if mime == "image/svg+xml" or mime == "image/gif":
        return data, mime  # 矢量/动图不处理
    try:
        im = Image.open(io.BytesIO(data))
        im.load()
    except Exception:
        return data, mime

    has_alpha = im.mode in ("RGBA", "LA") or (
        im.mode == "P" and "transparency" in im.info
    )
    changed = False
    if im.width > max_width:
        h = max(1, round(im.height * max_width / im.width))
        im = im.resize((max_width, h), Image.LANCZOS)
        changed = True

    buf = io.BytesIO()
    try:
        if has_alpha:
            im.save(buf, "PNG", optimize=True)
            new_mime = "image/png"
        else:
            if im.mode not in ("RGB", "L"):
                im = im.convert("RGB")
            im.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
            new_mime = "image/jpeg"
    except Exception:
        return data, mime

    out = buf.getvalue()
    if not changed and len(out) >= len(data):
        return data, mime
    return out, new_mime


def candidate_paths(src: str, md_dir: str, md_stem: str):
    """给出一个 src 可能的本地路径候选，按优先级排列。"""
    raw = src.split("?")[0].split("#")[0]
    if raw.lower().startswith("file:///"):
        raw = raw[8:]
    elif raw.lower().startswith("file://"):
        raw = raw[7:]
    raw = urllib.parse.unquote(raw).replace("/", os.sep)

    out = []
    if os.path.isabs(raw) or re.match(r"^[A-Za-z]:", raw):
        out.append(raw)
    else:
        out.append(os.path.join(md_dir, raw))
        # Typora 常见资源目录
        out.append(os.path.join(md_dir, "assets", os.path.basename(raw)))
        out.append(os.path.join(md_dir, md_stem + ".assets", os.path.basename(raw)))
        out.append(os.path.join(md_dir, "images", os.path.basename(raw)))
        out.append(os.path.join(md_dir, "img", os.path.basename(raw)))
    seen, uniq = set(), []
    for p in out:
        k = os.path.normcase(os.path.abspath(p))
        if k not in seen:
            seen.add(k)
            uniq.append(p)
    return uniq


def load_remote(url: str, timeout=15):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
            "Referer": url,
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def kb(n: int) -> str:
    return "%.0fKB" % (n / 1024) if n < 1024 * 1024 else "%.1fMB" % (n / 1024 / 1024)


def resolve_image(src: str, md_dir: str, md_stem: str, download: bool,
                  max_width: int, quality: int, stats: dict):
    """返回 (新src, 状态, 说明)。状态: base64 / remote / missing / skipped"""
    if not src:
        return src, "skipped", "空 src"

    if src.startswith("data:"):
        stats["after"] += len(src) * 3 // 4
        stats["before"] += len(src) * 3 // 4
        return src, "base64", "已是内嵌 base64"

    if re.match(r"^https?://", src, re.I):
        if not download:
            return src, "remote", "网络图片（保留 URL，公众号会尝试自动抓取）"
        try:
            data = load_remote(src)
        except Exception as e:
            return src, "remote", "下载失败，保留 URL：%s" % e
        mime = sniff_mime(data)
        new_data, new_mime = optimize_image(data, mime, max_width, quality)
        stats["before"] += len(data)
        stats["after"] += len(new_data)
        return to_data_uri(new_data, new_mime), "base64", "已下载并内嵌（%s → %s）" % (
            kb(len(data)), kb(len(new_data)))

    for p in candidate_paths(src, md_dir, md_stem):
        if os.path.isfile(p):
            try:
                with open(p, "rb") as f:
                    data = f.read()
            except OSError as e:
                return src, "missing", "读取失败：%s" % e
            if not data:
                return src, "missing", "文件为空：%s" % p
            mime = mimetypes.guess_type(p)[0] or sniff_mime(data)
            if not mime.startswith("image/"):
                mime = sniff_mime(data)
            new_data, new_mime = optimize_image(data, mime, max_width, quality)
            stats["before"] += len(data)
            stats["after"] += len(new_data)
            tag = "%s → %s" % (kb(len(data)), kb(len(new_data))) if len(new_data) != len(data) else kb(len(data))
            return to_data_uri(new_data, new_mime), "base64", "已内嵌 %s（%s）" % (os.path.basename(p), tag)
    return src, "missing", "找不到文件（尝试过 %d 个路径）" % len(candidate_paths(src, md_dir, md_stem))


# ---------------------------------------------------------------- 样式内联

FONT = ('-apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC",'
        '"Hiragino Sans GB","Microsoft YaHei",sans-serif')
MONO = 'Menlo,Consolas,"Courier New",monospace'

STYLES = {
    "p": "margin:16px 0;line-height:1.8;font-size:16px;color:#3f3f3f;letter-spacing:.5px;",
    "h1": "margin:34px 0 18px;font-size:23px;font-weight:bold;line-height:1.4;color:#1a1a1a;letter-spacing:.5px;",
    "h2": "margin:30px 0 16px;font-size:20px;font-weight:bold;line-height:1.45;color:#1a1a1a;padding-left:10px;border-left:4px solid #07c160;",
    "h3": "margin:24px 0 12px;font-size:18px;font-weight:bold;line-height:1.5;color:#1a1a1a;",
    "h4": "margin:20px 0 10px;font-size:16px;font-weight:bold;color:#1a1a1a;",
    "h5": "margin:18px 0 8px;font-size:15px;font-weight:bold;color:#1a1a1a;",
    "h6": "margin:16px 0 8px;font-size:15px;font-weight:bold;color:#888;",
    "img": "max-width:100%;height:auto;display:block;margin:18px auto;border-radius:4px;",
    "blockquote": "margin:18px 0;padding:10px 16px;border-left:4px solid #d0d7de;"
                  "background:#f6f8fa;color:#57606a;font-size:15px;line-height:1.75;",
    "pre": "margin:18px 0;padding:14px 16px;background:#f6f8fa;border-radius:6px;"
           "overflow-x:auto;font-size:13px;line-height:1.6;font-family:%s;" % MONO,
    "code": "background:#f2f3f5;color:#c7254e;padding:2px 5px;border-radius:3px;"
            "font-size:14px;font-family:%s;" % MONO,
    "table": "margin:18px 0;border-collapse:collapse;width:100%;font-size:14px;",
    "th": "border:1px solid #dfe2e5;padding:8px 12px;background:#f6f8fa;"
          "font-weight:bold;color:#1a1a1a;text-align:left;",
    "td": "border:1px solid #dfe2e5;padding:8px 12px;color:#3f3f3f;",
    "ul": "margin:16px 0;padding-left:26px;",
    "ol": "margin:16px 0;padding-left:26px;",
    "li": "margin:7px 0;line-height:1.8;font-size:16px;color:#3f3f3f;",
    "a": "color:#576b95;text-decoration:none;border-bottom:1px solid #576b95;",
    "hr": "margin:26px 0;border:none;border-top:1px solid #e5e5e5;",
    "strong": "font-weight:bold;color:#1a1a1a;",
    "em": "font-style:italic;",
    "del": "text-decoration:line-through;color:#999;",
}


def inline_styles(soup):
    for tag, css in STYLES.items():
        for el in soup.find_all(tag):
            el.attrs.pop("class", None)
            # pre 内的 code 不套行内代码样式
            if tag == "code" and el.find_parent("pre"):
                el["style"] = "background:none;color:inherit;padding:0;font-size:13px;font-family:%s;" % MONO
                continue
            el["style"] = css
    # 去掉无用的 id / class
    for el in soup.find_all(True):
        el.attrs.pop("id", None)
        if el.name not in ("code",):
            el.attrs.pop("class", None)
    return soup


# ---------------------------------------------------------------- 主流程

def build(md_text: str, md_path: str, download: bool, width: int,
          max_width: int = 1200, quality: int = 85):
    md_dir = os.path.dirname(os.path.abspath(md_path))
    md_stem = os.path.splitext(os.path.basename(md_path))[0]

    html = markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists", "admonition"],
        output_format="html5",
    )
    soup = BeautifulSoup(html, "html.parser")

    report = []
    stats = {"before": 0, "after": 0}
    for i, img in enumerate(soup.find_all("img"), 1):
        src = img.get("src", "")
        new_src, status, note = resolve_image(
            src, md_dir, md_stem, download, max_width, quality, stats)
        img["src"] = new_src
        alt = img.get("alt", "")
        report.append((i, status, note, alt, src[:70]))
        # 公众号对 <img> 的 title/alt 无要求，清理冗余属性
        for k in ("title", "width", "height", "loading"):
            img.attrs.pop(k, None)

    inline_styles(soup)

    body = soup.decode()
    container = (
        '<div style="max-width:%dpx;margin:0 auto;padding:0 10px;'
        'font-family:%s;font-size:16px;line-height:1.8;color:#3f3f3f;'
        'letter-spacing:.5px;word-break:break-word;text-align:left;">%s</div>'
        % (width, FONT, body)
    )

    page = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<style>
  body{margin:0;padding:24px 12px;background:#fff;}
  ::selection{background:#b3e5c8;}
</style>
</head>
<body>
%s
</body>
</html>
""" % (os.path.basename(md_path), container)
    return page, report, stats


def main():
    ap = argparse.ArgumentParser(description="Markdown 转微信公众号可用 HTML（图片内嵌）")
    ap.add_argument("md", help="Markdown 文件路径")
    ap.add_argument("-o", "--out", help="输出 HTML 路径")
    ap.add_argument("--check", action="store_true", help="只诊断图片，不生成 HTML")
    ap.add_argument("--download", action="store_true", help="网络图片也下载并内嵌")
    ap.add_argument("--open", action="store_true", help="生成后用默认浏览器打开")
    ap.add_argument("--width", type=int, default=677, help="正文宽度 px，默认 677")
    ap.add_argument("--max-width", type=int, default=1200,
                    help="图片最大宽度 px，超出则等比缩小；0 表示不缩放，默认 1200")
    ap.add_argument("--quality", type=int, default=85,
                    help="JPEG 重编码质量 1-95，默认 85")
    args = ap.parse_args()

    if not os.path.isfile(args.md):
        sys.exit("文件不存在：%s" % args.md)

    for enc in ("utf-8-sig", "utf-8", "gbk"):
        try:
            with open(args.md, "r", encoding=enc) as f:
                text = f.read()
            break
        except UnicodeDecodeError:
            continue
    else:
        sys.exit("无法识别文件编码：%s" % args.md)

    page, report, stats = build(text, args.md, args.download, args.width,
                                args.max_width, args.quality)

    print("=" * 62)
    print("图片处理报告：共 %d 张" % len(report))
    print("=" * 62)
    if not report:
        print("（文档中没有图片）")
    for idx, status, note, alt, src in report:
        flag = {"base64": "OK  ", "remote": "URL ", "missing": "LOST", "skipped": "----"}[status]
        print("[%s] #%-2d %s" % (flag, idx, note))
        if alt:
            print("        alt: %s" % alt)
    lost = sum(1 for r in report if r[1] == "missing")
    if lost:
        print("\n⚠ 有 %d 张图片无法定位源文件，粘贴后会显示为裂图。" % lost)
        print("  若原文图片是通过『复制粘贴截图』插入的，可能本就未落盘，需重新截图插入。")

    if stats["before"]:
        saved = 100.0 * (1 - stats["after"] / stats["before"])
        print("\n图片体积：%s → %s（压缩 %.0f%%）" % (
            kb(stats["before"]), kb(stats["after"]), saved))
        est = stats["after"] * 4 / 3
        print("预计 HTML 大小：约 %s（base64 膨胀 33%%）" % kb(int(est)))

    if args.check:
        return

    out = args.out or os.path.splitext(args.md)[0] + ".wechat.html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    size_mb = os.path.getsize(out) / 1024 / 1024
    print("\n已生成：%s  (%.2f MB)" % (out, size_mb))
    print("下一步：用浏览器打开该文件 → Ctrl+A 全选 → Ctrl+C → 粘贴到公众号编辑器")


if __name__ == "__main__":
    main()
