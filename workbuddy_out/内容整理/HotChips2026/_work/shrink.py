# -*- coding: utf-8 -*-
"""把报告用图压缩为 web 尺寸 JPEG（长边 <=1500，白底）。"""
import os, glob
from PIL import Image

D = r"G:/AI_IDE_output/workbuddy_out/内容整理/HotChips2026/06_深度分析报告/images"
MAX = 1500
total = 0
for p in sorted(glob.glob(os.path.join(D, "*.png"))):
    im = Image.open(p)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    w, h = im.size
    if max(w, h) > MAX:
        r = MAX / max(w, h)
        im = im.resize((int(w * r), int(h * r)), Image.LANCZOS)
    out = p[:-4] + ".jpg"
    im.save(out, "JPEG", quality=88, optimize=True, progressive=True)
    total += os.path.getsize(out)
    print(os.path.basename(out), im.size, f"{os.path.getsize(out)/1024:.0f} KB")
print(f"TOTAL {total/1024/1024:.1f} MB")
