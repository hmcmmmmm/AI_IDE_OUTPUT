# -*- coding: utf-8 -*-
"""把 Markdown 报告渲染为单文件 HTML（含侧边目录、图片、表格美化）。"""
import os, re, html
import markdown

BASE = r"G:/AI_IDE_output/workbuddy_out/内容整理/HotChips2026/06_深度分析报告"
SRC = os.path.join(BASE, "HotChips2026_深度分析报告.md")
OUT = os.path.join(BASE, "HotChips2026_深度分析报告.html")

md_text = open(SRC, encoding="utf-8").read()

md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists", "md_in_html"],
                       extension_configs={"toc": {"toc_depth": "1-2", "permalink": False}})
body = md.convert(md_text)
toc_html = md.toc

# 证据标记 → 彩色 chip
TAGS = {
    "【一手】": "t1", "【一手·推算】": "t2", "【官方】": "t3",
    "【读稿】": "t4", "【报道】": "t5", "【推断】": "t6",
}
for k, cls in TAGS.items():
    body = body.replace(k, f'<span class="tag {cls}">{k[1:-1]}</span>')

# 图片 + 图注：把 <p><img ...></p> 后紧跟的 <p><em>图 N｜...</em></p> 合成 figure
fig_re = re.compile(
    r'<p><img alt="(图 (\d+)｜[^"]*)" src="(images/[^"]+)"\s*/?></p>\s*<p><em>\1</em></p>',
    re.S)
def figsub(m):
    alt, num, src = m.group(1), m.group(2), m.group(3)
    cap = alt.split("｜", 1)[1] if "｜" in alt else alt
    return (f'<figure id="fig{num}"><img src="{src}" alt="{html.escape(cap)}" loading="lazy">'
            f'<figcaption><b>图 {num}</b>　{html.escape(cap)}</figcaption></figure>')
body, n = fig_re.subn(figsub, body)

# 表格包一层可滚动容器
body = body.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")

# 一级标题加编号胶囊
body = re.sub(r'<h1>(第 \d+ 章)', r'<h1><span class="chno">\1</span>', body)

CSS = """
:root{
  --bg:#fbfbfa; --fg:#1d2129; --muted:#6b7280; --line:#e5e7eb; --card:#ffffff;
  --accent:#1a4fd6; --accent-soft:#eef3ff;
  --t1:#0f7b4f; --t1bg:#e7f6ee; --t2:#0b6b8a; --t2bg:#e5f4f9;
  --t3:#7a4a00; --t3bg:#fdf3e2; --t4:#5b3fa8; --t4bg:#f1ecfd;
  --t5:#8a2b2b; --t5bg:#fbeaea; --t6:#4b5563; --t6bg:#eef0f3;
}
@media (prefers-color-scheme: dark){
  :root{
    --bg:#15171a; --fg:#e6e8eb; --muted:#9aa3ad; --line:#2c3037; --card:#1b1e22;
    --accent:#7aa2ff; --accent-soft:#1c2536;
    --t1:#5fd3a0; --t1bg:#123227; --t2:#63c6e6; --t2bg:#102b34;
    --t3:#e0b062; --t3bg:#33280f; --t4:#b49bff; --t4bg:#241d3d;
    --t5:#f08a8a; --t5bg:#3a1d1d; --t6:#b6bcc4; --t6bg:#23262b;
  }
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);
  font:16px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
  -webkit-font-smoothing:antialiased}
#bar{position:fixed;top:0;left:0;height:3px;width:0;background:var(--accent);z-index:99;transition:width .1s}
nav{position:fixed;top:0;left:0;bottom:0;width:288px;overflow-y:auto;padding:22px 16px 60px;
  border-right:1px solid var(--line);background:var(--card);font-size:13.5px}
nav .brand{font-weight:700;font-size:15px;line-height:1.4;margin-bottom:4px}
nav .sub{color:var(--muted);font-size:12px;margin-bottom:16px}
nav ul{list-style:none;margin:0;padding:0}
nav>ul>li{margin:2px 0}
nav a{display:block;padding:4px 8px;border-radius:6px;color:var(--fg);text-decoration:none;
  line-height:1.4;word-break:break-word}
nav a:hover{background:var(--accent-soft);color:var(--accent)}
nav>ul>li>a{font-weight:600;margin-top:8px}
nav ul ul a{padding-left:20px;color:var(--muted);font-size:12.5px;font-weight:400}
main{margin-left:288px;padding:56px 48px 120px;max-width:1080px}
h1{font-size:26px;line-height:1.35;margin:56px 0 18px;padding-top:14px;border-top:1px solid var(--line)}
h1:first-of-type{border-top:0;margin-top:0;padding-top:0}
h1 .chno{color:var(--accent)}
h2{font-size:19px;margin:34px 0 12px;color:var(--fg)}
h3{font-size:16.5px;margin:26px 0 10px}
p{margin:12px 0}
a{color:var(--accent)}
strong{font-weight:650}
hr{border:0;border-top:1px solid var(--line);margin:40px 0}
blockquote{margin:18px 0;padding:12px 18px;background:var(--card);border-left:3px solid var(--accent);
  border-radius:0 8px 8px 0;color:var(--fg)}
blockquote p{margin:6px 0}
code{font:13px/1.5 ui-monospace,SFMono-Regular,Consolas,monospace;background:var(--accent-soft);
  padding:1px 5px;border-radius:4px}
pre{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;overflow:auto}
pre code{background:none;padding:0;font-size:12.5px}
.tw{overflow-x:auto;margin:18px 0;border:1px solid var(--line);border-radius:10px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th,td{padding:8px 12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
td:first-child{min-width:6em;white-space:nowrap}
li{margin:7px 0}
ol,ul{padding-left:1.6em}
th{background:var(--accent-soft);font-weight:650;white-space:nowrap}
tr:last-child td{border-bottom:0}
tbody tr:hover{background:var(--accent-soft)}
figure{margin:26px 0;padding:0;text-align:center}
figure img{max-width:100%;border:1px solid var(--line);border-radius:10px;background:#fff}
figcaption{margin-top:8px;font-size:12.5px;color:var(--muted)}
figcaption b{color:var(--accent)}
.tag{display:inline-block;padding:0 6px;margin-right:2px;border-radius:4px;font-size:12px;
  font-weight:600;line-height:19px;vertical-align:1px}
.t1{color:var(--t1);background:var(--t1bg)} .t2{color:var(--t2);background:var(--t2bg)}
.t3{color:var(--t3);background:var(--t3bg)} .t4{color:var(--t4);background:var(--t4bg)}
.t5{color:var(--t5);background:var(--t5bg)} .t6{color:var(--t6);background:var(--t6bg)}
.top{position:fixed;right:22px;bottom:22px;width:38px;height:38px;border-radius:50%;border:1px solid var(--line);
  background:var(--card);color:var(--fg);cursor:pointer;display:none;font-size:15px}
@media (max-width:960px){
  nav{position:static;width:auto;border-right:0;border-bottom:1px solid var(--line);max-height:40vh}
  main{margin-left:0;padding:24px 18px 80px}
}
@media print{
  nav,#bar,.top{display:none} main{margin:0;max-width:none;padding:0}
  h1{page-break-before:always} figure{page-break-inside:avoid}
}
"""

JS = """
var bar=document.getElementById('bar'),top=document.querySelector('.top');
addEventListener('scroll',function(){
  var h=document.documentElement, s=h.scrollTop||document.body.scrollTop,
      m=(h.scrollHeight-h.clientHeight)||1;
  bar.style.width=(s/m*100)+'%';
  top.style.display=s>600?'block':'none';
},{passive:true});
top.onclick=function(){scrollTo({top:0,behavior:'smooth'})};
document.querySelectorAll('nav a').forEach(function(a){
  a.addEventListener('click',function(){
    document.querySelectorAll('nav a').forEach(function(x){x.style.background=''});
    a.style.background='var(--accent-soft)';
  });
});
"""

HTML = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hot Chips 2026 深度分析报告</title>
<style>{CSS}</style>
</head>
<body>
<div id="bar"></div>
<nav>
  <div class="brand">Hot Chips 2026 深度分析报告</div>
  <div class="sub">HC38 · 2026-08-23/25 · Stanford<br>基于 36 份一手 PDF · 41 图</div>
  {toc_html}
</nav>
<main>{body}</main>
<button class="top" title="回到顶部">↑</button>
<script>{JS}</script>
</body>
</html>
"""
open(OUT, "w", encoding="utf-8").write(HTML)
print("figures:", n, "html bytes:", len(HTML.encode("utf-8")))
