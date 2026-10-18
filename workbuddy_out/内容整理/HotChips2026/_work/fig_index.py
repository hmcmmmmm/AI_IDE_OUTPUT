# -*- coding: utf-8 -*-
"""生成「附录 D：图表索引」并追加到报告末尾。"""
import os, re

MD = r"G:/AI_IDE_output/workbuddy_out/内容整理/HotChips2026/06_深度分析报告/HotChips2026_深度分析报告.md"
lines = open(MD, encoding="utf-8").read().split("\n")

fig = re.compile(r"^!\[图 (\d+)｜(.+?)\]\(images/([A-Za-z0-9_\-]+)\.jpg\)$")
chapter = ""
rows = []
for ln in lines:
    s = ln.strip()
    m = re.match(r"^# (第 \d+ 章[^：:]*)[：:](.*)$", s)
    if m:
        chapter = m.group(1).strip()
        continue
    m = fig.match(s)
    if m:
        rows.append((int(m.group(1)), m.group(2), chapter))

tbl = ["", "---", "", "# 附录 D：图表索引", "",
       f"共 {len(rows)} 张。全部由 `Hotchip 2026/` 下的原始 PDF 按关键词定位页面后重新渲染（150 DPI，长边 ≤1500 px），"
       "标注「知乎作者重绘」的 6 张来自 `05_渠道图文归档/images/zhihu_*.jpg`。", "",
       "| 图 | 内容 | 所在章节 |", "| --- | --- | --- |"]
for n, cap, ch in rows:
    tbl.append(f"| {n} | {cap} | {ch} |")

# 去掉文件末尾已有的附录 D（幂等）
txt = "\n".join(lines)
if "# 附录 D：图表索引" in txt:
    txt = txt.split("# 附录 D：图表索引")[0].rstrip()
txt = txt.rstrip() + "\n" + "\n".join(tbl) + "\n"
open(MD, "w", encoding="utf-8").write(txt)
print("appendix D rows:", len(rows))
