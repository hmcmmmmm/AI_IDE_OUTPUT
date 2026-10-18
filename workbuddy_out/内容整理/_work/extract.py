# -*- coding: utf-8 -*-
"""Extract text from the Hot Chips 2026 decks using PyMuPDF."""
import os
import re
import sys

import fitz

ROOT = r"G:\AI_IDE_output\workbuddy_out\内容整理"
SRC = os.path.join(ROOT, "HotChips2026", "Hotchip 2026")
OUT = os.path.join(ROOT, "_work", "txt")
os.makedirs(OUT, exist_ok=True)

index = []
for fn in sorted(os.listdir(SRC)):
    if not fn.lower().endswith(".pdf"):
        continue
    path = os.path.join(SRC, fn)
    try:
        doc = fitz.open(path)
    except Exception as e:  # noqa: BLE001
        print("OPEN FAIL", fn, e)
        continue
    parts = []
    for i, page in enumerate(doc, 1):
        t = page.get_text("text")
        t = re.sub(r"\n{2,}", "\n", t).strip()
        parts.append(f"\n--- p{i} ---\n{t}")
    doc.close()
    stem = re.sub(r"[^\w\u4e00-\u9fff.-]+", "_", os.path.splitext(fn)[0])[:80]
    with open(os.path.join(OUT, stem + ".txt"), "w", encoding="utf-8") as f:
        f.write("".join(parts))
    index.append((fn, doc.page_count if False else len(parts), len("".join(parts))))
    print(f"{len(parts):3d}p {len(''.join(parts)):7d}ch  {fn[:70]}")

with open(os.path.join(OUT, "_index.txt"), "w", encoding="utf-8") as f:
    for fn, pages, chars in index:
        f.write(f"{pages}\t{chars}\t{fn}\n")
print("TOTAL", len(index), "files")
