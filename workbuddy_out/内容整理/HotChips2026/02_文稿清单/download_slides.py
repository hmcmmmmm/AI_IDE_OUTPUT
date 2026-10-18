# -*- coding: utf-8 -*-
"""Hot Chips 2026 幻灯片批量下载器。

官方文稿位于 hc2026.hotchips.org，启用 HTTP Basic Auth（realm="Attendees Only"）。
持参会凭证（注册邮箱收到的账号）时可直接批量拉取。

用法：
    python download_slides.py <用户名> <密码>
    python download_slides.py            # 凭证走环境变量 HC_USER / HC_PASS
"""
import base64
import csv
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "slides")
CSV_PATH = os.path.join(HERE, "HC2026_幻灯片直链.csv")


def safe(name, maxlen=120):
    for c in '<>:"/\\|?*':
        name = name.replace(c, "-")
    name = " ".join(name.split()).strip().rstrip(". ")
    if len(name) > maxlen:
        stem, ext = os.path.splitext(name)
        name = stem[: maxlen - len(ext)] + ext
    return name


def main():
    user = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("HC_USER", "")
    pwd = sys.argv[2] if len(sys.argv) > 2 else os.environ.get("HC_PASS", "")
    if not user or not pwd:
        print("缺少凭证。用法: python download_slides.py <用户名> <密码>")
        return 1

    token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8-sig")))
    os.makedirs(OUT, exist_ok=True)
    ok = 0
    for i, r in enumerate(rows, 1):
        sub = safe(r["分类"]).replace(" · ", "_")
        d = os.path.join(OUT, sub)
        os.makedirs(d, exist_ok=True)
        fn = f'{int(r["序号"]):02d}_{safe(r["单位"])}_{safe(r["题目"])}.pdf'
        path = os.path.join(d, fn)
        if os.path.exists(path) and os.path.getsize(path) > 10000:
            ok += 1
            continue
        req = urllib.request.Request(
            r["官方直链"],
            headers={"Authorization": f"Basic {token}", "User-Agent": "Mozilla/5.0",
                     "Referer": "https://hc2026.hotchips.org/"},
        )
        try:
            data = urllib.request.urlopen(req, timeout=180).read()
            if data[:4] != b"%PDF":
                print(f'[{i}/{len(rows)}] 非 PDF 响应（凭证失效或未授权）: {r["题目"][:40]}')
                continue
            open(path, "wb").write(data)
            ok += 1
            print(f'[{i}/{len(rows)}] OK {len(data)/1048576:5.1f}MB {fn[:60]}')
        except Exception as e:  # noqa: BLE001
            print(f'[{i}/{len(rows)}] 失败: {e} :: {r["题目"][:40]}')
        time.sleep(0.3)
    print(f"完成 {ok}/{len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
