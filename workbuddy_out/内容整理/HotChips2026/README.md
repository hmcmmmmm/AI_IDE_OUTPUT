# Hot Chips 2026（HC38）资料库

> 整理日期：2026-10-18　｜　入口：`index.html`（可筛选/搜索的 51 条文稿目录）

## 一、一句话说清这批资料的状态

**官方已公布全部 51 个演讲文稿的文件路径，但服务器对所有 PDF 启用了 `Basic Auth · realm="Attendees Only"`，无参会凭证一律返回 HTTP 401。** 因此本次交付的是"**完整索引 + 深度综述 + 一键下载工具**"，而不是 PDF 本体；同时把**完全公开的 2025 届全套 54 份文稿**下载下来作为可立即阅读的参照。

| 年份 | 文稿数量 | 可下载性 | 本库处理 |
| --- | --- | --- | --- |
| HC2026（8/23–25，斯坦福） | 51 份（教程 10 / Day1 15 / Day2 15 / 海报 11） | **需参会凭证**（实测 401） | 全量索引 + 直链 + 综述 + 下载脚本 |
| HC2025 | 54 份 | 完全公开（实测 200） | **已全量下载**（`_参考_HotChips2025/`） |
| HC2024 | 55 份 | 完全公开 | 未下载，可按需补 |

## 二、目录结构

```
HotChips2026/
├── index.html                              ← 51 条文稿目录（按分类筛选 + 关键词搜索）
├── 01_会议日程/
│   ├── HC2026_完整日程.md                  ← 官方日程中文结构化版（含讲者、单位、时间）
│   └── HC2026_日程.csv
├── 02_文稿清单/
│   ├── HC2026_幻灯片直链.csv               ← 51 行：题目 / 单位 / 讲者 / 分类 / 官方直链
│   └── download_slides.py                  ← 带 Basic Auth 的批量下载器
├── 03_技术综述/
│   └── HotChips2026_技术综述.md            ← 七条主线 + 关键数据表 + 阅读顺序建议
├── 04_非官方渠道/
│   └── 非官方渠道清单.md                   ← 2 个已验证的百度网盘包 + 8 个信息渠道 + 已排除渠道
└── _参考_HotChips2025/                     ← 2025 届 54 份公开文稿（tutorials/conference/posters）
    └── 文件清单.csv                        ← 54 份文件的目录/文件名/体积索引
```

## 三、如何拿到 2026 官方文稿（三条路径）

**路径 0：非官方网盘包（无需参会凭证，需百度账号）**

| 来源 | 链接 | 提取码 | 内容 |
| --- | --- | --- | --- |
| 知乎《Hot Chips 2026 所有的PPT》 | `https://pan.baidu.com/s/1N0P9DTRCS3ODpdSjczQZEg` | `s4z0` | 37 份（Day1 13 / Day2 14 / Tutorials 10），**缺 11 篇海报** |
| 微信公众号《HotChips2026全景总结》 | `https://pan.baidu.com/s/1gCKT8zHHMNd_2kBrHq8mTg` | `9znj` | 未披露清单，可与上者互补 |

两个链接均已实测存活（HTTP 200，正常弹出提取码）。完整核查记录见 `04_非官方渠道/非官方渠道清单.md`。

**路径 1：你有参会账号（最快）**
```bash
cd 02_文稿清单
python download_slides.py <注册邮箱> <密码>
# 或 set HC_USER=... / set HC_PASS=... 后直接 python download_slides.py
```
脚本会按分类建子目录、自动重命名（序号_单位_题目.pdf）、跳过已下载文件。

**路径 2：购买官方"幻灯片 + 视频"访问权**
https://hotchipssymposium.regfox.com/hot-chips-2026-video-and-presentation-access
（官网首页 "Register Slide and Video Access" 即指向此页）

**路径 3：等归档期开放（免费）**
往届规律是当年文稿先对参会者开放，之后整体转为公开（HC2025 现已全公开）。归档入口：
https://hc2026.hotchips.org/ （当年）/ https://www.hotchips.org/archives/ （历届总入口）

## 四、会议看点（详见 `03_技术综述/`）

- **议程结构**：2 场教程（内存技术 / RISC-V）+ Day1 四场（CPU1、CPU2、Automotive、GPU）+ Waymo 主题演讲 + Day2 五场（FPGA、Memory、Networking、AI1、AI2）+ 11 篇海报。
- **Day1 GPU 场是全场焦点**：NVIDIA Rubin、AMD MI400（架构 + 系统架构两讲）、Intel Crescent Island 同日登场。
- **内存墙是信息密度最高的部分**：Samsung 走"底座逻辑化 → zHBM 三维集成"，SK hynix 走"混合键合突破 16 层"，d-Matrix / XCENA 走"绕开 HBM"。
- **CPU 被重新估值**：Vera、Diamond Rapids、Arm AGI、MONAKA、IBM Z 双指令集、Wildcat Lake（Intel 首次用 UCIe 降本）。
- **自研 ASIC 第二梯队集体亮相**：Google TPU v8、Microsoft MAIA 200、Meta、OpenAI、Cerebras、SambaNova、NVIDIA LPU。

## 五、已知限制

1. **未能取得 2026 原始 PDF**，故综述中的参数分三级标注：`【读稿】`（第三方参会者读稿整理，数字直接取自幻灯片）、`【报道】`（媒体/百科转述）、`【推断】`（本文分析）。拿到网盘包后可逐条核对。网盘包本身未经我验证，可能存在缺页或非最终稿。
2. **NVIDIA LPU 与 Groq 的关系已澄清**：NVIDIA 官方活动页把 "NVIDIA Groq 3 LPX" 列为在产产品（单机柜 256 LPU / 128 GB SRAM / 40 PB/s / 640 TB/s），即 LPU 已并入 NVIDIA 产品线。上一版的"存疑"标注已更正。
3. **Waymo 主题演讲无对应文稿文件**：51 个文件中只有 Waymo 的"传感器融合处理器"演讲，Keynote 本身未列入索引。
4. **2025 参考集为英文原稿**，文件名保留官方命名（含厂商与项目代号），未做重命名。

## 六、来源与版权

- 日程与文稿索引：`hotchips.org/advance-program/`、`hc2026.hotchips.org`（2026-10-18 抓取）
- 往届文稿：`hc2025.hotchips.org`（公开）
- 参数与厂商动态：百度百科词条（引用多家媒体报道）及公开新闻，仅作二手参考
- 所有文稿版权归各演讲单位（NVIDIA、AMD、Intel、Google、Microsoft、Meta、Samsung、SK hynix 等）所有，仅供个人学习研究，请勿商业传播
