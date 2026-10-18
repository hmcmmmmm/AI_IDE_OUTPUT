# 渠道图文归档：Hot Chips 2026 非官方渠道正文与配图

> 归档时间：2026-10-18
> 归档对象：`04_非官方渠道/非官方渠道清单.md` 中 **§二「有内容但无文件附件的渠道（信息价值高）」** 所列的 5 个渠道。
> 归档方式：正文逐段抓取（保留原表述）＋配图本地化。图片分两类：① 渠道原文自带图片；② **由本库 36 份一手幻灯片 PDF 重新渲染的高清原页**（用于替代原文中低清翻拍截图，精度更高）。

## 为什么要有这个目录

Hot Chips 2026 的 51 份官方 PDF 全部位于 `hc2026.hotchips.org` 的 HTTP Basic Auth 之后（`realm="Attendees Only"`），公开渠道无法直接下载。除了百度网盘的两个参会者流转包之外，还有一批**「有实质内容、但不提供 PDF 附件」**的渠道——它们要么逐页读了幻灯片并抄下原始数字，要么从产业链视角做了系统梳理。这些渠道的信息密度往往高于二手新闻稿，是本报告「二手证据」部分的主要来源。

本目录把这些渠道的正文与配图落成本地 Markdown，目的是：
1. **可离线阅读、可引用、可核对**——原文随时可能被删改；
2. **图片可追溯**——每张图标注来源与原始出处；
3. **为 `06_深度分析报告/` 提供可点回的证据链**。

## 目录

| 文件 | 渠道 | 原始链接 | 信息类型 | 证据等级 |
| --- | --- | --- | --- | --- |
| `01_知乎_内存干货与私货.md` | 知乎 @乱序摸鱼《Hotchips 2026 干货和私货分享 — 内存》 | https://zhuanlan.zhihu.com/p/2075617575262762743 | 读稿级深度长文（内存/封装专场） | 高（大量原始幻灯片数字） |
| `02_雪球_全景梳理.md` | 雪球《Hot Chips 2026 全景梳理：当"搬数据"取代"算数据"》 | https://xueqiu.com/8353820992/406787553 | 产业链价值流向视角的全景综述 | 中（观点强、数据少） |
| `03_什么值得买_Intel三张牌.md` | 什么值得买《Hot Chips 2026 英特尔一天拍三张牌》 | https://post.smzdm.com/p/a8253mzn/ | 爆料/官宣/评论区三方交叉核对 | 中（含未证实爆料） |
| `04_NVIDIA官方_活动页与博客.md` | NVIDIA 官方 Hot Chips 活动页 + 6 篇技术博客 | https://www.nvidia.com/en-us/events/hot-chips-conference/ | 厂商官方口径（最详细的免费一手资料） | 高（官方，但为营销口径） |
| `05_百度百科_HotChips2026.md` | 百度百科《Hot Chips 2026》 | https://baike.baidu.com/item/Hot%20Chips%202026/68748688 | 参数汇编（引用多家媒体） | 中（二手汇编，个别数字需核） |
| `images/` | 配图目录 | — | 48 张原幻灯片页 + 渠道原图 | 一手（PDF 重渲染） |

## 图片说明

`images/` 下 48 张 PNG 全部由 `HotChips2026/Hotchip 2026/` 中的**原始 PDF** 用 PyMuPDF 按关键词定位页面后以 150 DPI 渲染，最大边控制在 2200 px。命名规则：`序号_主题.png`。这些图在 `06_深度分析报告/` 中被逐张引用，是报告中所有关键数字的**可视证据**。

| 图号 | 内容 | 来源幻灯片 |
| --- | --- | --- |
| 01–03 | Rubin「七芯片五机柜」全景、100 MW AI 工厂账本、NVLink 6 | NVIDIA Rubin GPU |
| 04–07 | MI455X 规格、MI455X vs MI355X、Helios 机柜、UALoE 交换 | AMD MI400 系列（芯片 + 系统两篇） |
| 08–10 | TPU8 Boardfly 拓扑、8i 规格、SRAM vs HBM 对比 | Google TPU 8t/8i |
| 11 | Maia 200 完整规格表 | Microsoft |
| 12–13 | Jalapeño 规格、2048 芯片系统 | OpenAI |
| 14–15 | Diamond Rapids SoC 组成、18A-P 工艺收益 | Intel |
| 16–17 | Vera CPU 规格、SCF 一致性互连 | NVIDIA Vera |
| 18–19 | HBM base die 三阶段路线图、zHBM 收益 | Samsung HBM Base Die |
| 20–21 | 12Hi→16Hi 封装挑战、混合键合收益 | SK hynix |
| 22–23 | 内存墙曲线、HBM 世代参数表 | Micron |
| 24–25 | AI 芯片 BOM 中内存占比、LPDDR5X-PIM 实测 | Samsung LPDDR5X-PIM |
| 26–27 | Raptor vs HBM4 面积基准对比、能量阶梯 | d-Matrix |
| 28–29 | HBF (β, α) 成本模型、72 GPU 机柜配置对比 | OXMIQ Labs |
| 30–31 | CS-4 数字表、43,200 TB/s 片上带宽 | Cerebras |
| 32–33 | MBU 随规模变化、SN50 规格 | SambaNova |
| 34–35 | MTIA 400 五芯粒封装、性能代际对比 | Meta |
| 36 | IBM Spyre 卡规格 | IBM |
| 37 | BlueField-4 7 Tb/s 数据通路 | NVIDIA |
| 38 | Spectrum-X Multiplane 512k GPU | NVIDIA |
| 39 | Thor Ultra eRoCE 特性 | Broadcom |
| 40 | Arm AGI CPU 规格 | Arm |
| 41 | MONAKA 3D 堆叠 | Fujitsu |
| 42 | Waymo 传感器融合处理器规格 | Waymo |
| 43 | XCENA MX1 架构 | XCENA × Samsung |
| 44 | Crescent Island 480 GB LPDDR5X | Intel |
| 45 | Wildcat Lake UCIe 面积代价 | Intel |
| 46 | LPU 全 SRAM 平坦内存层级 | NVIDIA LPU |
| 47 | RISC-V RVA23 Profile | SiFive |
| 48 | Versal RF 代际对比 | AMD |

## 合规与使用边界

1. 本目录正文版权属各原作者（知乎作者、雪球作者、什么值得买作者、NVIDIA、百度百科）。此处归档**仅用于个人学习与研究**，不构成转载授权。
2. `images/` 中的幻灯片页版权属各演讲单位（NVIDIA、AMD、Intel、Google、Microsoft、Meta、OpenAI、Samsung、SK hynix、Micron、Broadcom、Arm、Fujitsu、Waymo、Cerebras、SambaNova、d-Matrix、XCENA、IBM 等）。原始 PDF 由用户自行取得，此处仅做格式转换（PDF→PNG）以便阅读，未做内容修改。
3. 引用关键参数时，请优先采用本目录标注为「一手」的幻灯片页；渠道文章的转述数字可能因口语化而失真，报告中已逐条标注 `【读稿】/【报道】/【推断】`。
