# Hot Chips 2026 技术综述

> 整理日期：2026-10-18　｜　依据：hotchips.org 官方完整日程 + hc2026.hotchips.org 官方文稿索引 + 公开媒体报道
> **证据分级**：`【日程】`= 官方议程原文；`【读稿】`= 第三方参会者读稿整理，数字直接取自幻灯片（来源可追溯但非官方）；`【报道】`= 媒体/百科转述的厂商口径，未与原始幻灯片逐条核对；`【推断】`= 本文分析，非事实陈述。

## 一、一句话结论

Hot Chips 2026 的叙事重心已从"训练峰值算力"整体转向**智能体推理（Agentic AI）的系统级工程**：芯片公司比拼的不再是单颗芯片的 FLOPS，而是"内存层级 + 互连拓扑 + 供电散热 + 机架整机"能否协同把每焦耳能量转化为有效 Token。NVIDIA、AMD、Intel 三家在同一天（Day 1 GPU 场）正面交锋，Google、微软、Meta、OpenAI 四家自研芯片在 Day 2 集体登场，构成本届最密集的技术信号。

## 二、会议基本盘

| 项目 | 内容 |
| --- | --- |
| 届次 | Hot Chips 38（HC38） |
| 时间 | 2026 年 8 月 23–25 日（周日教程 + 周一周二正会）【日程】 |
| 地点 | 斯坦福大学纪念礼堂（Memorial Auditorium），加州帕洛阿尔托【日程】 |
| 形式 | 现场名额售罄；虚拟参会提供直播、可下载幻灯片、Slack 问答与即时回放【报道】 |
| 议程结构 | 2 场教程（内存技术 / RISC-V）+ Day1 四场（CPU1、CPU2、Automotive、GPU）+ 1 场 Keynote + Day2 四场（FPGA、Memory、Networking、AI1、AI2）+ 11 篇海报【日程】 |
| 文稿数量 | 官方索引共 51 个 PDF（教程 10、Day1 15、Day2 15、海报 11）【官方索引实测】 |

## 三、七条技术主线

### 1. 推理成为第一性原理：芯片按"智能体"重新定义

`【日程】` 本届最直白的变化是标题措辞：NVIDIA 的 Rubin 演讲题为 *Driving the Era of Agentic AI*，Intel 的 Crescent Island 直接叫 *GPU Designed for Agentic AI Inference*，Google TPU v8 的副标题是 *Two Chips Optimized for Training and Serving in the Agentic Era*。

`【推断】` 这说明架构分工正在细化：训练仍是大芯片 + 高带宽 HBM 的战场，而推理被拆成"预填充（prefill）/ 解码（decode）"两个物理上不同的负载，分别用不同芯片承接。Google 明确用"两颗芯片"覆盖训练与服务，是这一判断最直接的证据；Intel Crescent Island 以 350W、风冷、PCIe 卡形态出现，也指向"推理是机架里可插拔的存量算力"，而非又一个液冷整机柜。

### 2. GPU 平台战：三家在同一天摊牌

**NVIDIA Rubin**`【日程】`：主讲三人覆盖架构、封装与系统；配套的 Vera CPU 单列在 CPU 场。
`【报道】` Vera Rubin NVL72 整机柜功耗升至 190–230 kW，用 PCB 中板（Midplane）替代传统铜缆，PCB 层数由 36–44 层升至 46–52 层，供电切换 800 VDC，100% 液冷；Rubin Ultra NVL576 的 Scale-up 采用 CPO。

**AMD Instinct MI400**`【日程】`：架构（Alan Smith）+ 系统架构（Steve Scott）两场连讲，是全场唯一给系统架构单独排片的 GPU 厂商。
`【报道】` MI455X 以 8 颗 N2 工艺计算芯粒 3D 混合键合集成，12 组 HBM4、432 GB 显存；Helios 机柜 72 颗 GPU、2.9 EFLOPS。

**Intel Crescent Island**`【日程】`：定位 Agentic AI 推理。
`【报道】` Xe3P 架构、32 个 Xe 核心、256 个 XMX 引擎，最高 480 GB LPDDR5X，350 W 风冷 PCIe 卡。

`【推断】` 三家的分野很清楚：NVIDIA 卖"整机柜级平台"，AMD 卖"芯片 + 系统架构的开放性"，Intel 卖"能塞进现有服务器的推理卡"。判断谁赢的关键指标不是峰值算力，而是 **每 Token 成本**与**机架级交付周期**。

### 3. CPU 被重新估值：智能体执行层的独立化

`【日程】` Day1 用两个完整场次（CPU 1、CPU 2，共 6 个演讲）讲 CPU，密度罕见。

- **NVIDIA Vera**：`【报道】` 88 个自研 Olympus 核心，被定位为"智能体 AI 时代的处理器"——即 GPU 之外单独承担编排、工具调用与长上下文管理。
- **Intel Diamond Rapids**：`【报道】` Intel 18A-P 制程、Foveros Direct 3D + UCIe-S，最高 256 核、1.28 GB LLC、16 通道 12800 MT/s、128 lane PCIe 6.0、CXL 3.0，2027 年上市。
- **Arm AGI**：`【日程】` 标题即点明"分离式（Disaggregated）、基于 Chiplet 的服务器 SoC"，解决"TB/s 时代的一致性与内存带宽"；`【报道】` 台积电 N3P、136 个 Neoverse V3 核心。
- **FUJITSU-MONAKA**：`【日程】` 主打"绿色 AI 数据中心"的能效路线。
- **IBM Z / LinuxONE**：`【日程】` 同一核心双指令集（z/Architecture + AArch64）+ AI 推理加速芯片组；`【报道】` 11 个 Z 核心、>5.7 GHz、2 nm。
- **Intel Wildcat Lake**：`【日程】` 以 Core Series 3 名义出现；`【报道】` 18A、2P+4E、NPU 17 TOPS，**首次在 Intel 处理器中使用 UCIe**（8 GT/s，有机封装替代 Foveros），并通过"关闭缺陷单元"回收约 29% 原本报废的计算裸片。

`【推断】` CPU 场次的真正主题不是性能，而是**Chiplet 的经济学**：UCIe 从"高性能互连"下沉为"降本手段"（Wildcat Lake），同时向上支撑"分离式服务器"（Arm AGI）。这是本届最被低估的一条线。

### 4. 内存墙：三条互不兼容的突围路线

这是本届信息密度最高的部分，教程 1 的六个演讲全部围绕它。

**问题量化**`【报道】`：算力约每 2 年增长 3 倍，内存能力每 2 年增长不到 2 倍；Llama 3 训练中约 17% 的非预期中断由 HBM 故障引起；典型 4 堆栈 HBM 的 GPU 封装中，约 90% 硅面积与内存相关；8 堆栈 HBM4 场景下 GPU+内存封装面积可能超过 12000 mm²。

`【读稿】` 同一组问题的更精确版本（数字直接来自幻灯片）：

| 对比项 | 数值 |
| --- | --- |
| 同容量下 HBM 与 DDR 的裸片面积比 | 约 **3×** |
| 品牌 DRAM / NAND 涨幅 | **7.1× / 6.9×** |
| 新建 DRAM 晶圆厂交付周期 | **> 2 年** |
| 8 通道 DDR5-4800 服务器 | **307 GB/s** 支撑 **~1 TB** |
| 8× HBM3 GPU | **5.3 TB/s** 支撑 **192 GB** |
| HBM3E 单堆栈内部带宽 | 256 I/O × 8 Gbps = **256 GB/s**（同工艺 DDR5 8 I/O 仅 8 GB/s） |
| 8 堆栈 × 12 层总内存硅面积 | **12,344 mm²**，超过典型 GPU 裸片面积的 8 倍 |

`【推断】` 这张表说明"内存墙"首先是"成本墙"：需求按季度重排，产能按年扩张，两者的弹性差决定了 HBM 的溢价短期不会消失。

**路线 A：把逻辑做进 HBM 底座（Samsung）**`【报道】`
分三步走：cHBM（定制）→ aHBM（底座加处理单元，可做压缩、归约、格式转换、简单矩阵运算）→ zHBM（存储直接叠在计算芯片上）。zHBM 宣称能效 +70%、DRAM 带宽 +230%、单模块省电最高 100 W，并把约 8.3% 的功耗余量让给加速器。HBM4E 已把 DRAM 核心层与 4 nm 底座结合，底座可集成内存控制器、修复逻辑、传感器、RAS，甚至客户定制计算单元。

`【读稿】` 支撑上述结论的幻灯片细节：

- **HBM4 base die 用 4 nm 逻辑工艺**（xPU 约 3 nm），意味着内存厂正式进入先进逻辑代工体系。
- 接口规格跃迁：数据 I/O **1024 → 2048**，通道 **16 → 32**，伪通道 **64**，bank 数 **128 → 256**；单 I/O **8–16 Gbps**，单堆栈 **1–5 TB/s**。
- **定制 HBM4 的 D2D PHY 从 >8 mm × 4 mm 缩到约 8.5 mm × 1.5 mm**，通道深度 5.5 mm → 2 mm——这是"底座变 SoC"的物理前提。
- 热密度反讽：HBM4E 约 14 Gbps / 0.5 W·mm⁻²，HBM5 目标 >28 Gbps / >2.0 W·mm⁻²，**速度翻倍而功率密度翻四倍**；HPB（热通路块）在 PHY 区覆盖率 >50% 时峰值温度降幅 >35%。
- zHBM 的账最直观：**1200 W GPU 配 4 颗 HBM，可省约 100 W，等于整卡 8.3% 的功耗预算**——这正好是"把功耗让给算力"的量化表达。

**路线 B：混合键合突破堆叠层数（SK hynix）**`【报道】`
现有 TC+NCF 与 MR+MUF 两种封装方案在 16 层附近遇瓶颈，混合键合可使核心芯片厚度 +24%、TSV 间距 <18 µm、热阻 −35%；另开发 I-HBM（在 D2D PHY 区嵌入高导热绝缘冷却件），额外降热阻 30%+。HBM4 已量产 12 层，16 层认证中。

`【读稿】` 12Hi → 16Hi 的几何账（这是判断"为什么必须换键合"的关键）：

| 参数 | 变化 |
| --- | --- |
| 层数 | 12 → 16（**+33%**） |
| 封装高度 | 约 **720 µm → 775 µm**（仅 **+8%**） |
| 单层 die 厚度 | 1.0× → 约 **0.9×** |
| 层间间隙 | 1.0× → **0.5×** |
| 凸点间距 | → 约 **0.9×** |

归一化热阻路线：HBM2（TC-NCF）1.0× → HBM2E/3（MR-MUF）0.55–0.65× → HBM3E/4（Advanced MR-MUF）0.45–0.55× → **HBM4E 及 ≥20Hi（混合键合）约 0.40×**。
混合键合为 SiO₂-SiO₂ 先接触、再 **>200 °C 退火**实现 Cu-Cu；在 ≥20Hi 且等高约束下，核心 die 可加厚 **24%**——`【读稿】` 该文作者认为"加厚 24%"对操作与翘曲的意义大于间距缩小。

**路线 C：换掉 HBM（d-Matrix / PIM / CXL）**`【日程】`+`【报道】`
- d-Matrix Raptor：N4 逻辑裸片与 3D-DRAM 面对面堆叠，单卡 32 GB 3D-DRAM、带宽 >100 TB/s，宣称每 GB/s 功耗较 HBM 方案改善 13.5 倍，2027 年商用。
- Samsung LPDDR5X-PIM：官方称"全球首个基于 LPDDR 的存内计算方案"，指向推理场景的低成本高能效。
- XCENA MX1：CXL 计算型内存器件（与 Samsung 联合演讲），把内存池化落到 CXL 语义层。

`【读稿】` 其中 OXMIQ 的 HBF（High Bandwidth Flash）给出了最完整的设计空间账，值得单独记：

| 维度 | HBF | HBM |
| --- | --- | --- |
| 单位容量成本系数 β | **≈1×** | **10–14×** |
| 带宽密度 α | **1–7 GB/s/GB** | **40–100 GB/s/GB** |
| 整机示例 | 全 HBF：约 **4 TB / 12.8 TB/s** | 全 HBM：约 **288 GB / 22 TB/s** |

分级带宽（单用户可用上限）：Grade 1 **0.384 TB/s**、Grade 2 **1.536 TB/s**、Grade 3 **3.072 TB/s**；访问粒度要求 **64 KB 读 / 1 MB 写 / 64 KB 对齐**；可靠性约束是 85 °C 下带电保持仅约 **24 小时**，必须由主机侧管理寿命与磨损。
`【读稿】` 该文给出的判据是成本式 `$mem = β · max(C, I·b/α)`——容量项与带宽项取大者，这解释了为什么 HBF 只适合"冷专家 / 稀疏 KV / 前缀缓存"，而不适合替代 HBM 的主力带宽。

`【推断】` 三条路线对应三种商业模式：A 是内存厂向上吃逻辑价值，B 是内存厂守住 DRAM 制造优势，C 是系统厂绕开 HBM 供应链。**它们不可能同时成立**——若 zHBM 路线走通，HBM 的独立封装产业价值会被大幅压缩；若 C 路线走通，HBM 的稀缺溢价会先崩。这是未来两年最值得跟踪的分歧点。

### 5. 互连与网络：从"配套"升级为"第一性设计"

`【日程】` Day2 的 Networking & Interconnect 场次三家连讲：Broadcom Thor Ultra（以太网 NIC）、NVIDIA BlueField-4（DPU 作为"AI 工厂操作系统"载体）、NVIDIA Spectrum-X Multiplane（多平面网络架构）。

`【报道】` Spectrum-X Multiplane 可扩展至 512,000 GPU。

`【推断】` 三个演讲的措辞值得注意：NIC 讲"为 AI 与 HPC 优化"，DPU 讲"承载 AI 工厂操作系统"，交换机讲"多平面"。这意味着网络正在从"连接 GPU 的管道"变成"调度算力与内存的资源总线"，与 OCP 侧 OSPA / UALink 的开放化方向形成呼应。

### 6. 自研 ASIC 的第二梯队：七家公司同台

`【日程】` Day2 的 AI 1 / AI 2 两个场次共 7 个演讲，全部是"非 GPU 通用路线"：

| 公司 | 芯片 | 路线特征（据日程标题） |
| --- | --- | --- |
| Meta | 定制 AI 硅 | 从推荐系统到"推荐 + GenAI 双使命" |
| NVIDIA | Groq 3 LPX（LPU） | "Think Fast"；单机柜 256 LPU / 128 GB SRAM / 40 PB/s 内存带宽 / 640 TB/s Scale-up |
| Cerebras | WSE 机架级架构 | 晶圆级引擎的机架化 |
| Microsoft | MAIA 200 | 数据中心级 AI 系统 |
| SambaNova | SN50 RDU | 数据流架构的规模化 |
| Google | TPU v8 家族 | 两颗芯片分别优化训练与服务 |
| OpenAI | 自研芯片 | 题为 *You Can Just Build Things … Chips* |

`【推断】` 这份名单的结构性意义大于单颗芯片：除 NVIDIA 外，六家全部是"自用负载驱动的定制硅"。它们的共同前提是**自家有足够大的推理负载来摊薄流片成本**——这恰好是 Hot Chips 这类会议存在的理由：把定制硅的设计经验公开交换，降低下一家的试错成本。

`【已澄清】` 上一版标注的"NVIDIA LPU 与 Groq 关系存疑"现已可确认：NVIDIA 官方 Hot Chips 2026 活动页把 **"NVIDIA Groq 3 LPX"** 直接列为在产产品（新闻稿标题为 *NVIDIA Groq 3 LPX Now in Full Production*），即 Groq 的 LPU 已并入 NVIDIA 产品线，本次演讲对应的就是该产品。官方给出的规格为：**单机柜 256 颗 LPU、128 GB SRAM、40 PB/s 内存带宽、640 TB/s Scale-up 带宽**，与 Vera Rubin 平台协同（Rubin GPU + LPU 分工）。

### 7. 边缘、汽车与学术：11 篇海报里的方向

`【日程】` 海报部分呈现三条清晰的学术主线：

1. **开放硅与教学**：ETH Zurich 的 Croc（开源 SoC 教学设计）、东京大学的 RISC-V CPU 全流程课程、PNNL 的"从 Python 到流片"开源硬件编译器 —— 开源 EDA 链条正在闭环。
2. **Chiplet 与边缘 SLM**：UC Berkeley 的 Gemmelos（Intel 16 双芯片）、Harvard/Lockheed 的 Pistil（16 nm + 20 Chiplet 2.5D SiP 跑小语言模型）。
3. **非冯·诺依曼探索**：Normal Computing 的 CN101（数字 CMOS 热力学计算）、Opticore 的相干光子张量 crossbar、KU Leuven/TU Delft 的 ETHEREAL（17 µs 事件驱动 GNN 处理器）。

`【推断】` 汽车场次（Waymo 主题演讲 + Waymo 传感器融合处理器 + BOS Semiconductors Eagle-N）说明"物理 AI"已成为独立赛道，且其芯片形态（Chiplet SoC、低延迟传感器融合）与数据中心芯片的设计约束完全不同。

## 四、关键数据点速查

| 指标 | 数值 | 主体 | 来源 |
| --- | --- | --- | --- |
| 整机柜功耗 | 190–230 kW | NVIDIA Vera Rubin NVL72 | 报道 |
| 显存容量 | 432 GB（12×HBM4） | AMD MI455X | 报道 |
| 机柜算力 | 2.9 EFLOPS（72 GPU） | AMD Helios | 报道 |
| 内存容量 | 480 GB LPDDR5X | Intel Crescent Island | 报道 |
| CPU 核心 | 256 核 / 1.28 GB LLC | Intel Diamond Rapids | 报道 |
| CPU 核心 | 136×Neoverse V3（N3P） | Arm AGI | 报道 |
| CPU 核心 | 88×Olympus | NVIDIA Vera | 报道 |
| 3D-DRAM 带宽 | >100 TB/s（32 GB/卡） | d-Matrix Raptor | 报道 |
| 能效提升 | +70%，带宽 +230% | Samsung zHBM | 报道 |
| 热阻改善 | −35%（混合键合）/ −30%（I-HBM） | SK hynix | 报道 |
| 网络规模 | 512,000 GPU | NVIDIA Spectrum-X | 报道 |
| 算力/内存增速差 | 3× vs <2×（每 2 年） | Micron 分析 | 报道 |

> 以上数值均为厂商在演讲中的自述口径，**未经第三方验证**，且本次未能取得原始幻灯片逐条核对，引用时请注明"厂商口径"。

## 五、如果你是第一次读这批文稿，建议顺序

1. `Tutorial 1` 的 Micron + Samsung + SK hynix 三篇 —— 建立内存墙的量化框架，后面所有 GPU 的参数才有参照系。
2. `Day1 GPU` 的 AMD 两篇（架构 + 系统架构）—— 唯一把"芯片→机柜"完整讲透的一组。
3. `Day1 CPU 2` 的 Intel Diamond Rapids + Arm AGI —— 看懂 Chiplet 的两种极端取舍。
4. `Day2 AI 1` 的 Google TPU v8 + Microsoft MAIA 200 —— 自研 ASIC 的两种组织方式（超大规模自用 vs 云服务对外）。
5. `Day2 Memory` 的 Samsung LPDDR5X-PIM + XCENA MX1 —— 判断"换掉 HBM"是否可行。
6. 其余按兴趣补，海报部分适合找研究方向。

## 六、文稿获取

官方 51 个 PDF 全部启用了 `Basic Auth · realm="Attendees Only"`，未持参会凭证访问返回 401；往届（HC2025 及更早）已完全公开。据参会者说法，**官方惯例是会后 3 个月解禁**，即约 2026 年 11 月下旬。

三条路径：
1. 持参会账号 → `02_文稿清单/download_slides.py` 批量下载。
2. 非官方网盘包 → 见 `04_非官方渠道/非官方渠道清单.md`（2 个已验证存活的百度网盘链接，37 份文稿，缺海报）。
3. 等官方解禁 → 跟踪 `hc2026.hotchips.org`。
