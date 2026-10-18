# -*- coding: utf-8 -*-
"""从原始 Hot Chips 2026 PDF 中按关键词定位并渲染关键页为 PNG。"""
import os, re, sys, json
import fitz

ROOT = r"G:\AI_IDE_output\workbuddy_out\内容整理"
SRC = os.path.join(ROOT, "HotChips2026", "Hotchip 2026")
OUT = os.path.join(ROOT, "HotChips2026", "05_渠道图文归档", "images")
os.makedirs(OUT, exist_ok=True)

# (输出名, PDF 文件名, [关键词...], 是否取最后匹配页)
JOBS = [
    ("01_rubin_seven_chips_five_racks", "FINAL_NV_HC2026_Rubin.pdf", ["seven chips", "five racks"], False),
    ("02_rubin_100mw_ai_factory", "FINAL_NV_HC2026_Rubin.pdf", ["100 MW", "ZFLOP"], False),
    ("03_rubin_nvlink6", "FINAL_NV_HC2026_Rubin.pdf", ["NVLink 6"], False),
    ("04_mi455x_spec", "FINAL_AMD_Instinct_MI400_GPU_Architecture_HotChips.pdf", ["40.26", "MXFP4"], False),
    ("05_mi455x_vs_mi355x", "FINAL_AMD_Instinct_MI400_GPU_Architecture_HotChips.pdf", ["3.3", "MI355X"], False),
    ("06_helios_rack", "FINAL_AMD_MI400_System_Arch_Hot_Chips_2026.pdf", ["1.7 PB/s", "2.9 Exaflops"], False),
    ("07_helios_ualoe", "FINAL_AMD_MI400_System_Arch_Hot_Chips_2026.pdf", ["UALoE"], False),
    ("08_tpu8_boardfly", "HotChips2026GoogleTPU8FinalFix.pdf", ["Boardfly"], False),
    ("09_tpu8_spec", "HotChips2026GoogleTPU8FinalFix.pdf", ["384 MB", "288 GB"], False),
    ("10_tpu8_sram_vs_hbm", "HotChips2026GoogleTPU8FinalFix.pdf", ["SRAM", "HBM"], False),
    ("11_maia200_spec", "HC2026.Microsoft.PrashantRanjan.v04.pdf", ["10,145"], False),
    ("12_jalapeno_spec", "OpenAI Jalapeno - V2 Final - HotChips _26.pdf", ["13.4"], False),
    ("13_jalapeno_2048", "OpenAI Jalapeno - V2 Final - HotChips _26.pdf", ["2048"], False),
    ("14_dmr_soc", "DMR at Hot Chips 2026_FINAL.pdf", ["1.28 GB"], False),
    ("15_dmr_18ap", "DMR at Hot Chips 2026_FINAL.pdf", ["18A-P"], False),
    ("16_vera_spec", "HC2026.NVIDIA Vera.JonathonEvans.PolychronisXekalakis_v06.pdf", ["88", "164"], False),
    ("17_vera_scf", "HC2026.NVIDIA Vera.JonathonEvans.PolychronisXekalakis_v06.pdf", ["3.4 TB/s"], False),
    ("18_hbm_basedie_roadmap", "HC2026.HBMBaseDie.SangwookHan.v20.pdf", ["Phase #3"], False),
    ("19_zhbm_benefit", "HC2026.HBMBaseDie.SangwookHan.v20.pdf", ["zHBM", "230%"], False),
    ("20_skhynix_16hi", "HC2026.SK hynix.Jaesik_FINAL1.pdf", ["720", "775"], False),
    ("21_skhynix_hybridbond", "HC2026.SK hynix.Jaesik_FINAL1.pdf", ["18um", "24%"], False),
    ("22_micron_memory_wall", "HC2026.MicronTechnology.RaghuSreeramaneni.v03.pdf", ["3x/2yr"], False),
    ("23_micron_hbm_table", "HC2026.MicronTechnology.RaghuSreeramaneni.v03.pdf", ["2048", "11"], False),
    ("24_samsung_cost_share", "HC2026.Samsung.KaramHwang.v06_final_legal_disclaimer_.pdf", ["63%"], False),
    ("25_samsung_pim_result", "HC2026.Samsung.KaramHwang.v06_final_legal_disclaimer_.pdf", ["3.01x", "2.28x"], False),
    ("26_dmatrix_vs_hbm", "hc2026.dmatrix.SudeepBhoja.v3.0.pdf", ["13.5", "32.6"], False),
    ("27_dmatrix_energy_ladder", "hc2026.dmatrix.SudeepBhoja.v3.0.pdf", ["energy ladder"], False),
    ("28_hbf_cost_model", "HC2026.OXMIQ.AnuragAgrawal.v03.pdf", ["\u03b2", "\u03b1"], False),
    ("29_hbf_rack", "HC2026.OXMIQ.AnuragAgrawal.v03.pdf", ["294.9"], False),
    ("30_cerebras_numbers", "HC2026.Cerebras.JPFricker.v02.pdf", ["BY THE NUMBERS"], False),
    ("31_cerebras_bw", "HC2026.Cerebras.JPFricker.v02.pdf", ["43,200"], False),
    ("32_sambanova_mbu", "HotChips2026_SambaNova_SN50.pdf", ["MBU"], False),
    ("33_sambanova_spec", "HotChips2026_SambaNova_SN50.pdf", ["432 MB"], False),
    ("34_meta_mtia400_pkg", "HC2026.Meta.LokeChenSingh.V05.pdf", ["5-chiplet"], False),
    ("35_meta_mtia_perf", "HC2026.Meta.LokeChenSingh.V05.pdf", ["12 PFLOPS"], False),
    ("36_ibm_spyre", "HotChips2026.IBM.ChristianZoellen.finaluncompressed.pdf", ["600+"], False),
    ("37_bf4_7tb", "NV_HC2026_BlueField-4_For_Presenting.pdf", ["7Tb/s"], False),
    ("38_spx_512k", "NV_HC2026_SpectrumX_Shainer.pdf", ["512k"], False),
    ("39_thor_eroc", "Thor_Ultra_Ethernet_NIC_for_AI_and_HPC_final.pdf", ["eRoCE"], False),
    ("40_arm_agi_spec", "HC2026.Arm.DeepakGoel.v1.pdf", ["136"], False),
    ("41_monaka_3d", "HC2026.FUJITSU.RYOHEI_OKAZAKI.v7.pdf", ["Hybrid Bonding", "SRAM die"], False),
    ("42_waymo_spec", "HC2026.Waymo.SabareeshRavikumar.v02.pdf", ["208"], False),
    ("43_xcena_mx1", "HC2026.XCENA-Samsung.Kim.v02.pdf", ["3072"], False),
    ("44_crescent_island", "FINAL_Intel_Crescent Island GPU Hot Chips 2026.pdf", ["480"], False),
    ("45_wildcat_ucie", "HC2026.Intel.LanceHacking.v07.submit2.pdf", ["UCIe", "110"], False),
    ("46_lpu_sram", "NV_HC2026_LPU.pdf", ["SRAM"], False),
    ("47_sifive_rva23", "RISCV-20260823-HotChips_SiFive.pdf", ["RVA23"], False),
    ("48_versal_rf", "FINAL for Distribution_HC AMD Versal RF Series.pdf", ["32 GSPS"], False),
]

def pages_text(doc):
    out = []
    for p in doc:
        out.append(p.get_text("text"))
    return out

report = []
for name, fn, kws, _ in JOBS:
    path = os.path.join(SRC, fn)
    if not os.path.exists(path):
        report.append({"name": name, "file": fn, "status": "pdf-missing"})
        continue
    doc = fitz.open(path)
    texts = pages_text(doc)
    hit = None
    for i, t in enumerate(texts):
        if all(k.lower() in t.lower() for k in kws):
            hit = i
            break
    if hit is None:
        # 退化为任一关键词命中
        for i, t in enumerate(texts):
            if any(k.lower() in t.lower() for k in kws):
                hit = i
                break
    if hit is None:
        report.append({"name": name, "file": fn, "status": "kw-not-found"})
        doc.close()
        continue
    page = doc[hit]
    pix = page.get_pixmap(dpi=150)
    outp = os.path.join(OUT, name + ".png")
    pix.save(outp)
    report.append({"name": name, "file": fn, "page": hit + 1, "px": [pix.width, pix.height], "status": "ok"})
    doc.close()

print(json.dumps(report, ensure_ascii=False, indent=1))
ok = sum(1 for r in report if r["status"] == "ok")
print(f"\nRENDERED {ok}/{len(JOBS)}")
