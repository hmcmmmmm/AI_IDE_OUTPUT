# -*- coding: utf-8 -*-
"""v2: 模糊文件名匹配 + 关键词定位 + 尺寸上限，渲染 Hot Chips 2026 关键页。"""
import os, re, json
import fitz

ROOT = r"G:\AI_IDE_output\workbuddy_out\内容整理"
SRC = os.path.join(ROOT, "HotChips2026", "Hotchip 2026")
OUT = os.path.join(ROOT, "HotChips2026", "05_渠道图文归档", "images")
os.makedirs(OUT, exist_ok=True)

def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

FILES = {norm(f): f for f in os.listdir(SRC) if f.lower().endswith(".pdf")}

JOBS = [
    ("04_mi455x_spec", "FINAL_AMD Instinct MI400 GPU Architecture_HotChips.pdf", ["40.26"]),
    ("05_mi455x_vs_mi355x", "FINAL_AMD Instinct MI400 GPU Architecture_HotChips.pdf", ["MI355X"]),
    ("06_helios_rack", "FINAL_AMD MI400_System_Arch_Hot_Chips_2026.pdf", ["2.9 Exaflops"]),
    ("07_helios_ualoe", "FINAL_AMD MI400_System_Arch_Hot_Chips_2026.pdf", ["10.8 TB/s"]),
    ("09_tpu8_spec", "HotChips2026GoogleTPU8FinalFix.pdf", ["384MB"]),
    ("24_samsung_cost_share", "HC2026.Samsung.KaramHwang.v06(final_legal disclaimer).pdf", ["63%"]),
    ("25_samsung_pim_result", "HC2026.Samsung.KaramHwang.v06(final_legal disclaimer).pdf", ["3.01x"]),
    ("39_thor_eroc", "Thor Ultra Ethernet NIC for AI and HPC final.pdf", ["eRoCE Features"]),
    ("44_crescent_island", "FINAL_Intel Crescent Island GPU Hot Chips 2026.pdf", ["480GB"]),
    ("46_lpu_sram", "NV_HC2026_LPU.pdf", ["Flat memory hierarchy"]),
]

report = []
for name, fn, kws in JOBS:
    real = FILES.get(norm(fn))
    if not real:
        report.append({"name": name, "status": "pdf-missing", "want": fn})
        continue
    doc = fitz.open(os.path.join(SRC, real))
    texts = [p.get_text("text") for p in doc]
    hit = next((i for i, t in enumerate(texts) if all(k.lower() in t.lower() for k in kws)), None)
    if hit is None:
        report.append({"name": name, "status": "kw-not-found", "real": real})
        doc.close()
        continue
    page = doc[hit]
    # 控制尺寸：最大边 <= 2200px
    r = page.rect
    dpi = 150
    if max(r.width, r.height) * dpi / 72 > 2200:
        dpi = int(2200 * 72 / max(r.width, r.height))
    pix = page.get_pixmap(dpi=dpi)
    pix.save(os.path.join(OUT, name + ".png"))
    report.append({"name": name, "page": hit + 1, "px": [pix.width, pix.height], "status": "ok"})
    doc.close()

print(json.dumps(report, ensure_ascii=False, indent=1))
print("OK:", sum(1 for r in report if r["status"] == "ok"), "/", len(JOBS))
