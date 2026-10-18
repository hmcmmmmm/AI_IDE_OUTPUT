# -*- coding: utf-8 -*-
"""把报告里的 `见 images/xxx` 文字引用升级为真正的图文嵌入，并补齐缺失图片。"""
import os, re, shutil, glob
from PIL import Image

ROOT = r"G:/AI_IDE_output/workbuddy_out/内容整理/HotChips2026"
MD = os.path.join(ROOT, "06_深度分析报告", "HotChips2026_深度分析报告.md")
DST = os.path.join(ROOT, "06_深度分析报告", "images")
SRC_PNG = os.path.join(ROOT, "05_渠道图文归档", "images")

CAP = {
    "22_micron_memory_wall": "Micron：TFLOPS ≈3×/2 年，而 HBM 带宽 <2×/2 年 —— 内存墙的两条斜率",
    "24_samsung_cost_share": "Samsung：内存在 AI 芯片 BOM 中的占比从 52% 升到 63%",
    "23_micron_hbm_table": "Micron：HBM 世代参数表（容量、IO、功耗与 3× 硅面积的计算底座）",
    "20_skhynix_16hi": "SK hynix：12Hi → 16Hi 的封装挑战（总高 720 → 775 µm）",
    "21_skhynix_hybridbond": "SK hynix：混合键合（HyB）相对 TC-NCF 的热阻与厚度收益",
    "18_hbm_basedie_roadmap": "Samsung：HBM base die 的三阶段路线（sHBM4 → cHBM4 / aHBM4 → zHBM4）",
    "19_zhbm_benefit": "Samsung：zHBM 的收益拆解（−70% 搬运功耗 / +8.3% 性能 / +230% 容量）",
    "27_dmatrix_energy_ladder": "d-Matrix：能量阶梯 —— 每一层数据搬运的 pJ/bit 定价",
    "26_dmatrix_vs_hbm": "d-Matrix：以硅面积归一化的 Raptor 3D-DRAM vs HBM4 对比",
    "28_hbf_cost_model": "OXMIQ：HBF 的 (β, α) 成本模型 —— $mem = β·max(C, I·b/α)",
    "25_samsung_pim_result": "Samsung：LPDDR5X-PIM 实测（带宽 8×，端到端 3.01×）",
    "37_bf4_7tb": "NVIDIA：BlueField-4 的 7 Tb/s 数据通路",
    "38_spx_512k": "NVIDIA：Spectrum-X Multiplane 扩展到 512k GPU",
    "07_helios_ualoe": "AMD：Helios 机柜的 UALoE Scale-Up 交换结构",
    "39_thor_eroc": "Broadcom：Thor Ultra 的 eRoCE（MRC++）特性",
    "04_mi455x_spec": "AMD：MI455X 规格表",
    "05_mi455x_vs_mi355x": "AMD：MI455X vs MI355X 的代际对比",
    "41_monaka_3d": "Fujitsu：MONAKA 的 3D 堆叠（core N2P + SRAM N5 混合键合 + IO N5）",
    "14_dmr_soc": "Intel：Diamond Rapids 的 SoC 组成（16 core chiplet + 2 fabric hub + 4 base tile + 2 IMH）",
    "15_dmr_18ap": "Intel：18A-P 相对 18A 的工艺收益",
    "45_wildcat_ucie": "Intel：Wildcat Lake 改用 UCIe-S 后的 D2D 面积代价（+70%）",
    "46_lpu_sram": "NVIDIA：LPU 的全 SRAM 平坦内存层级",
    "02_rubin_100mw_ai_factory": "NVIDIA：100 MW AI 工厂的功耗账本",
    "32_sambanova_mbu": "SambaNova：MBU（Model Bandwidth Utilization）随部署规模的变化",
    "06_helios_rack": "AMD：Helios 机柜解剖",
    "30_cerebras_numbers": "Cerebras：CS-4 的关键数字",
    "09_tpu8_spec": "Google：TPU8i 规格表",
    "11_maia200_spec": "Microsoft：Maia 200 完整规格表",
    "12_jalapeno_spec": "OpenAI：Jalapeño 规格表",
    "16_vera_spec": "NVIDIA：Vera CPU 规格表",
    "17_vera_scf": "NVIDIA：Vera 的 SCF 一致性互连（3.4 TB/s bisection）",
    "40_arm_agi_spec": "Arm：AGI CPU 规格表",
    "43_xcena_mx1": "XCENA：MX1 的 CXL 近存架构（3,072 RISC-V 核 + SSD-backed memory）",
    "03_rubin_nvlink6": "NVIDIA：NVLink 6 的 3.6 TB/s/GPU 与 72-GPU 域",
    "34_meta_mtia400_pkg": "Meta：MTIA 400 的五芯粒 2.5D 封装",
    "zhihu_07": "知乎作者重绘：PHY 面积跨代演进 —— sHBM4 起改用紧凑 D2D 后急剧收缩",
    "zhihu_08": "知乎作者重绘：标准 HBM vs 定制 HBM 的 base die floorplan",
    "zhihu_10": "知乎作者重绘：用 B-die 富余面积做 cell 级 repair resource",
    "zhihu_11": "知乎作者重绘：2.5D HBM vs zHBM，横向毫米级路径折成垂直几十微米",
    "zhihu_13": "知乎作者重绘：SK hynix 封装路线图（容量路径 + 热阻归一化曲线）",
    "zhihu_14": "知乎作者重绘：Hybrid Bonding 三项收益（厚度 / TSV pitch / 热阻）",
}

# 1) 补齐缺失图片：PNG 转 JPG，知乎图直接拷
def to_jpg(name):
    p = os.path.join(SRC_PNG, name + ".png")
    out = os.path.join(DST, name + ".jpg")
    if not os.path.exists(p) or os.path.exists(out):
        return
    im = Image.open(p)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA"); bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1]); im = bg
    else:
        im = im.convert("RGB")
    w, h = im.size
    if max(w, h) > 1500:
        r = 1500 / max(w, h); im = im.resize((int(w * r), int(h * r)), Image.LANCZOS)
    im.save(out, "JPEG", quality=88, optimize=True, progressive=True)

for n in ("23_micron_hbm_table", "30_cerebras_numbers", "45_wildcat_ucie", "46_lpu_sram"):
    to_jpg(n)
for n in ("zhihu_07", "zhihu_08", "zhihu_10", "zhihu_11", "zhihu_13", "zhihu_14"):
    s = os.path.join(SRC_PNG, n + ".jpg"); d = os.path.join(DST, n + ".jpg")
    if os.path.exists(s) and not os.path.exists(d):
        shutil.copy2(s, d)

# 2) 改写正文
lines = open(MD, encoding="utf-8").read().split("\n")
counter = {"n": 0}
used = set()

def block(name, once=False):
    if once and name in used:
        return []
    if name not in CAP:
        raise KeyError("no caption: " + name)
    if not os.path.exists(os.path.join(DST, name + ".jpg")):
        raise FileNotFoundError(name)
    used.add(name)
    counter["n"] += 1
    cap = CAP[name]
    return [f"![图 {counter['n']}｜{cap}](images/{name}.jpg)", "", f"*图 {counter['n']}｜{cap}*", ""]

out = []
pending = {}   # 在某个锚点行之前插入
ANCHORS = {
    "## 2.2 三条读表结论": ["09_tpu8_spec", "11_maia200_spec", "12_jalapeno_spec"],
    "## 3.4 一个被忽略的细节：Arm 的份额数字": ["16_vera_spec", "17_vera_scf"],
    "# 第 4 章 内存墙的量化：从技术曲线到成本结构": ["40_arm_agi_spec"],
    "## 6.5 本章结论": ["43_xcena_mx1"],
    "## 7.3 Scale-Out：Spectrum-X Multiplane 的“降一层”策略": ["03_rubin_nvlink6"],
    "## 8.2 案例一：AMD MI455X —— 12 颗 die 的分工": ["34_meta_mtia400_pkg"],
}
# 兜底：锚点文本可能用了直引号
ANCHORS_ALT = {k.replace("“", '"').replace("”", '"'): v for k, v in ANCHORS.items()}

pat = re.compile(r"images/([A-Za-z0-9_\-]+)\.(?:png|jpg)")
ALL_ANCHORS = {}
ALL_ANCHORS.update(ANCHORS)
ALL_ANCHORS.update(ANCHORS_ALT)
for ln in lines:
    key = ln.strip()
    if key in ALL_ANCHORS:
        for nm in ALL_ANCHORS[key]:
            out.extend(block(nm, once=True))
    if ln.startswith("见 `images/"):
        names = pat.findall(ln)
        fresh = [n for n in names if n not in used]
        if fresh:
            for nm in fresh:
                out.extend(block(nm))
        else:
            out.append(ln.replace(".png", ".jpg"))
        continue
    out.append(ln)

open(MD, "w", encoding="utf-8").write("\n".join(out))
print("figures inserted:", counter["n"])
print("files used:", len(used))
missing = set(os.path.splitext(f)[0] for f in os.listdir(DST)) - used
print("unused files in images/:", sorted(missing))
