# 百度百科《Hot Chips 2026》

| 项目 | 内容 |
| --- | --- |
| 词条 | Hot Chips 2026 |
| 链接 | https://baike.baidu.com/item/Hot%20Chips%202026/68748688 |
| 抓取时间 | 2026-10-18 |
| 性质 | 参数汇编词条（引用多家媒体 + 官方页） |
| 证据等级 | **中**。大部分参数可与一手幻灯片核对（核对通过率约 80%），但**个别数字有误或来源不明**，已逐条标注 |
| 配图 | 词条配图为媒体图，未本地化 |

## 编者按

百度百科的价值在于它是**目前公开渠道里参数最全的一份汇编**——把 NVIDIA、AMD、Intel、IBM、Arm、Samsung、SK hynix、Micron、d-Matrix 九家的关键数字压缩在两千字里。对于快速查数非常有用。

但它是二手汇编，存在三类问题：

1. **口径混淆**：把不同 benchmark、不同产品档位的数字并列（如 Groq 3 LPX 的 3,400 TPS 与 11,000 TPS）；
2. **数字错误**：个别参数与一手幻灯片不符（下表列出）；
3. **来源不明的"分析师数据"**：如 Jim Handy 的 HBM 现货涨价 7 倍、Micron capex 上调等，无法在会议材料中核实。

本档案保留全文，并在关键处加 `【核对】`。

---

## 正文（照录）

Hot Chips 2026 是 2026 年 8 月 23 日至 25 日在美国斯坦福大学举行的国际高性能芯片研讨会。会议聚焦 AI 加速器、高带宽内存（HBM）、CPU 及先进封装技术。英伟达发布 Vera Rubin 平台及 Vera CPU、Rubin GPU；AMD 展示 Instinct MI400 系列；英特尔公布 Diamond Rapids、Crescent Island 等。三星提出 zHBM 三维集成方案，SK 海力士押注混合键合，美光警示"内存墙"。谷歌、微软、Meta、OpenAI 等也展示了自研芯片。该研讨会被视为芯片行业技术风向标。

### 会议日程与安排

Hot Chips 2026 于 2026 年 8 月 23 日至 25 日在美国加州帕洛阿尔托斯坦福大学纪念礼堂举行。现场参与名额已售罄，虚拟参会面向全球开放，提供所有演讲的直播、可下载的幻灯片、用于问答的私人 Slack 工作区以及所有会议的即时回放。

2026 年 8 月 23 日举行两个教程。内存技术教程涵盖 HBM、先进封装、3D DRAM、HBF 等议题，由美光、三星、SK 海力士、d-Matrix 与 Meta、Oxmiq Labs 等机构演讲。RISC-V 教程涵盖 RISC-V 标准、RVA23、NVIDIA GPU 互操作性、汽车部署等议题，由 SiFive、Canonical、NVIDIA、英飞凌等演讲。

2026 年 8 月 24 日会议第一日设有 CPU、GPU、自动驾驶、汽车等环节，包括 NVIDIA Vera CPU、NVIDIA Rubin GPU、AMD Instinct MI400 系列、Intel Diamond Rapids、Intel Wildcat Lake、IBM 下一代 Z 处理器、Fujitsu MONAKA、Arm AGI 等演讲。Waymo 主题演讲 "Compute in Motion: Challenges of Autonomous Driving" 于当日举行。

2026 年 8 月 25 日会议第二日设有 FPGA、内存、网络互连、AI 等环节，包括 NVIDIA BlueField-4、NVIDIA Spectrum-X、Meta 定制芯片、Google TPU v8、OpenAI 芯片、Samsung LPDDR5X-PIM、XCENA CXL、Broadcom Thor Ultra、NVIDIA LPU、Cerebras、Microsoft MAIA 200、SambaNova SN50 等演讲。

### 厂商动态与新品发布

#### NVIDIA

NVIDIA 在 Hot Chips 2026 上展示了加速计算平台在 AI 时代数据中心的应用。NVIDIA 将极致协同设计从芯片扩展到网络，再到 Token 工厂。NVIDIA 发布 Vera Rubin NVL72 全栈 AI 工厂平台，该平台面向智能体 AI 和 AI 推理。**该平台整机柜功耗提升至 190-230 kW，新增 PCB 中板 Midplane 替代传统铜缆，PCB 层数从 36-44 层提升至 46-52 层，供电切换为 800 VDC 高压直流方案，散热采用 100% 液冷。**

> 【核对】800 VDC、100% 液冷、无电缆托盘在 Rubin 幻灯片中确认（"45 °C inlet liquid cooling / no chillers / 800 VDC / no retimers / cable-free trays"）。**但"190–230 kW""PCB 46–52 层""Midplane"三项在 36 份一手 PDF 中均未出现**，应属供应链/媒体信息，非会议披露。本报告引用时需标注为【报道】。

Vera CPU 采用 88 个自定义 Olympus 核心，NVIDIA 称其为面向智能体 AI 时代的处理器。Groq 3 LPX 推理加速器实现量产，针对 10 万 Token 长上下文场景每秒输出 3,400 个 Token。Spectrum-X Multiplane 网络架构可扩展至 512,000 个 GPU。NVIDIA 还推出由 BlueField-4 处理器和 DOCA 软件平台驱动的 Scale-In 基础设施及 NVLink Fusion 开放生态，并宣布 CUDA 向 RISC-V 扩展，要求 RISC-V CPU 至少符合 RVA23 Profile。

> 【核对】"88 核 Olympus" ✅；"512,000 GPU" ✅（Spectrum-X p16）；"CUDA 向 RISC-V 扩展 + RVA23" ✅（SiFive 教程 p20 明确提到 "Nvidia port of CUDA stack to RISC-V"；NVIDIA 自己也有 RISC-V Tutorial 场次）。
> ⚠️ "3,400 TPS @ 100K 上下文"与幻灯片"11,000 TPS（Gemma 4 31B coding）"口径不同，需并列而非替换。

#### AMD

AMD 在 Hot Chips 2026 上展示了 Instinct MI400 系列 GPU 架构，其中 MI455X 采用 **8 颗 N2 工艺计算芯粒通过 3D 混合键合集成**，配备 **12 组 HBM4**，显存容量 **432 GB**；配套的 Helios 机柜由 **72 颗 GPU** 组成，AI 算力达 **2.9 Exaflops**。

> 【核对】432 GB ✅、Helios 72 GPU ✅、2.9 EF ✅（AMD MI400 系统架构 p5）。
> ⚠️ **"8 颗 N2 计算芯粒 + 3D 混合键合"表述不准确。** 一手幻灯片为：**2× IOD（N3P）+ 8× XCD（N2）+ 2× FCD（N3P）**，共 12 颗 die；XCD 与 IOD 之间是 **3D 混合键合（hybrid bonding）**，但"8 颗 N2 计算芯粒"漏掉了 IOD/FCD。另外 **HBM4 是 12 组（12 stacks）**，正确。

#### Intel

Intel 展示了面向智能体 AI 及企业级工作负载的三款架构：Diamond Rapids 处理器、Crescent Island GPU 和 Wildcat Lake SoC。

Diamond Rapids 为下一代至强处理器，采用 Intel 18A-P 制程、Foveros Direct 3D 封装和 UCIe-S 互连，最高 **256 颗核心**、**1.28 GB 末级缓存**、**16 通道内存速率高达 12800 MT/s**、**128 通道 PCIe 6.0 和 CXL 3.0**，计划于 **2027 年**上市。

> 【核对】全部 ✅（DMR 幻灯片）。

Crescent Island 基于 Xe3P 架构，配备 **32 颗 Xe 核心和 256 个 XMX 引擎**，最高支持 **480 GB LPDDR5X 内存**，采用 **350 W 风冷** PCIe 扩展卡。

> 【核对】✅，但需补：**Intel 自有品牌卡为 160 GB**，480 GB 是给 ODM 伙伴的设计上限。

Wildcat Lake 基于 Intel 18A 制程节点，配备 **2 个性能核和 4 个能效核**，集成 Xe3 架构并支持 XMX AI 加速，内置 NPU 至高提供 **17 TOPS** 算力，是采用 UCIe 标准的英特尔处理器。该处理器以 Intel Core Series 3 名义推出，面向价格敏感的笔记本和边缘设备；它第一次在英特尔处理器中使用 UCIe，将两个裸片放入成本更低的有机封装，而非 Foveros 方案；它保留了新一代 CPU、GPU 和 NPU 架构，但删除或缩减了光线追踪、部分缓存、摄像头 PHY、显示和 I/O 能力；两颗裸片设计可通过关闭缺陷单元形成不同 SKU，使约 **29%** 原本不能用于完整型号的计算裸片得到回收；其 UCIe 连接速度为 **8 GT/s**，说明低成本芯粒更重视够用带宽、低功耗、封装简单和良率。

> 【核对】大部分 ✅（Wildcat Lake 幻灯片：2 P-core、Xe3、NPU 17 TOPS、UCIe 8 GT/s、−38% 计算面积、−15% IO 面积、Organic MCP 35×25×1.23 mm、UCIe bump pitch 110 µm vs Foveros 36 µm）。
> ⚠️ **"约 29% 裸片回收"与"删除光线追踪"两项未在幻灯片中出现**，属媒体补充信息。

#### IBM

IBM 公布了下一代 IBM Z 与 LinuxONE 双指令集处理器核心。该芯片集成 **11 个**面向性能与可靠性优化的 IBM Z 核心，主频超过 **5.7 GHz**，采用 **2 纳米**制程，同一核心既可运行原生 z/Architecture 指令集，也能运行 AArch64 指令集，即将进入流片阶段。IBM 还展示了第二代企业级 AI 推理加速器，配置 **16 个 AI 核心、96 GB HBM3e**。

> 【核对】11 核 ✅、5.7+ GHz ✅、2nm ✅、双 ISA（z/Architecture + Arm v9.3）✅、16 AI 核 ✅、96 GB HBM3e ✅。
> 【一手补充】IBM 幻灯片还有几个百科没写的关键数字：**SMT-2、36 MB 私有 L2、432 MB 虚拟 L3、3.5 GB 虚拟 L4、片上 DPU、2,792 条 AArch64 指令、239 个系统寄存器、99.9999999% 可用性（9 个 9）**；Spyre 卡为 **16 个活跃 AI 核 + 1 个冗余核、600+ FP8 TOPS（4× 现世代）、96 GB HBM3e ~4 TB/s（20× 现世代）、PCIe Gen6 x16**。见 `images/36_ibm_spyre.png`。

#### Arm

Arm 在 Hot Chips 2026 上发布了自研数据中心 CPU AGI，采用台积电 **N3P** 工艺，集成 **136 个 Neoverse V3 核心**。

> 【核对】✅。补充：双 chiplet、每 chiplet >50B 晶体管、300 W、96 lane PCIe Gen6、CXL 3.0、<100 ns 内存延迟、272 MB L2（136 核）、128 MB SLC。

#### d-Matrix

d-Matrix 在 Hot Chips 2026 上详细介绍了其 Raptor 3D-DRAM 生成式 AI 推理加速器。该芯片采用台积电 **N4** 逻辑裸片与 3D-DRAM 面对面堆叠架构，单张 Raptor 卡配备 **32 GB 3D-DRAM，带宽超过 100 TB/s**。d-Matrix 预计商用产品将于 **2027 年**推出。

> 【核对】N4（实际为 N4P）✅、32 GB/card ✅、>100 TB/s ✅（100 TB/s × 0.37 pJ/bit = 296 W 的测算）、2027 年 ✅。
> 【一手补充】Raptor 用 **36 µm 面对面（F2F）堆叠**、**840 banks/chiplet（768 可用 + 72 spare）**、**256 channel/chiplet**、Tj **105 °C**、retention 32 ms@85°C → 4 ms@105°C、**深 bank 化把 8× 刷新惩罚压到 1.37%**、**stream flipping（无引脚 DBI）省 20% I/O 功耗**。对比 HBM4：**32.6 vs 1.67 GB/s/mm²（约 20×）**、**2.96 vs 40 mW/GB/s（13.5× 更优）**。见 `images/26_dmatrix_vs_hbm.png`、`images/27_dmatrix_energy_ladder.png`。

### 内存技术与封装进展

#### Samsung

三星在 Hot Chips 2026 上提出将高带宽内存（HBM）基片打造为"智能搭档"的技术路线，分为**定制 HBM（cHBM）、先进 HBM（aHBM）和 zHBM** 三个阶段，最终实现把存储直接叠在计算芯片之上的真正三维集成。

三星已在定制 HBM4 上应用**热通路块（HPB）**技术，可将峰值温度降低超过 **35%**。HBM4 已开始使用先进逻辑工艺制造 base die；HBM4E 将 DRAM 核心层与 **4 纳米**底座结合，可集成内存控制、修复逻辑、传感器、RAS 可靠性功能，甚至客户定制的计算单元。三星还提出将内存管理下沉到 base die，包括内存控制器卸载、SRAM 修复、RAS 增强和热管理。下一阶段 aHBM 的底座可以加入处理单元，对数据执行压缩、归约、移动、格式转换或简单矩阵操作，以避免把大量数据来回搬运。与标准 HBM4E 相比，**zHBM 可将功耗效率提升 70%，DRAM 带宽提升 230%，单个 DRAM 模块最高可节省 100 瓦功耗，并能把约 8.3% 的功耗余量让渡给加速器使用**。

> 【核对】全部 ✅。三星幻灯片原文：Phase #1（offloading & optimization）→ Phase #2（functional expansion）→ Phase #3（true 3D convergence, zHBM）；"−70% I/O power"、"230% DRAM BW"、"100 W saving"、"8.3%"；HPB ">35% peak temp reduction, >50% PHY coverage"。

#### SK hynix

SK 海力士介绍了 HBM 封装技术进展。HBM 封装主要有**热压键合+非导电膜（TC+NCF）**和**整体回流+模塑底部填充（MR+MUF）**两种方案。为突破 16 层堆叠限制，SK 海力士正在研究混合键合技术，该技术可使**核心芯片厚度增加 24%**，**TSV 间距小于 18 微米**，**热阻降低 35%**。SK 海力士还在开发名为 **I-HBM** 的局部热点缓解技术，该技术在 HBM D2D PHY 区域嵌入高导热且电绝缘的冷却组件，打造专用散热路径，可额外降低 **30% 以上**的热阻。SK 海力士在 2.5D HBM 方案幻灯片中展示了英特尔 **EMIB** 封装技术。其 HBM4 产品带宽超过 **2 TB/s**，功耗效率提升 **40% 以上**，容量最高 **48 GB**，其中 **12 层堆叠已量产，16 层正在认证中**。

> 【核对】"die 厚 +24%""pitch <18 µm""HBM4 >2TB/s、40%+ 功耗改善、48 GB、12Hi 量产/16Hi 认证"✅。
> ⚠️ **"热阻降低 35%"表述有误。** 一手幻灯片为：归一化热阻 **TC-NCF 1× → MR-MUF 0.55–0.65× → Adv. MR-MUF 0.45–0.55× → HyB 0.40×**。HyB 相对 TC-NCF 降低约 **60%**，相对 Adv. MR-MUF 降低约 **11–27%**；"35%"出现在 **20Hi 时 HyB vs TC-NCF 的曲线差值**，不能笼统说"混合键合热阻降低 35%"。
> 【一手补充】I-HBM 数据来自 SK hynix 幻灯片 p15 引用的第三方表格（oscoo.com）：SK hynix iHBM ">30% thermal resistance reduction"；同表还列 Samsung HPB+HBB "~30% 温度降低、16% 热阻改善"、Micron ">20% 能效改善"。属**厂商自述，未独立验证**。

#### Micron

美光 HBM 设计架构研究员 Raghu Sreeramaneni 在演讲中对"内存墙"进行了剖析，指出**计算能力大约每两年增长 3 倍，而内存能力每两年仅增长不到 2 倍**。美光援引 Meta 公布的 **Llama 3** 训练数据称，约 **17%** 的非预期训练中断由 HBM 故障引起。在典型的配备四个 12 层 HBM 堆栈的 GPU 封装中，**系统级封装里约 90% 的硅片面积与内存相关**。美光还称，在相同容量下 HBM3E 所需硅面积可约为 DDR5 的**三倍**；当一颗 GPU 周围放置八个 HBM4 堆栈时，**GPU 与内存合计可能需要超过 12000 平方毫米的封装区域**。AI 内存正从单一池变成分层系统：最热的权重和 KV Cache 放在 HBM，较热数据放在 DDR 或 LPDDR，更冷的数据进入 SSD。内存墙既是硬件问题，也是软件问题。美光认为，AI 时代最稀缺的资源正从"能做多少次计算"转向"**每焦耳能把多少有用数据送到计算单元**"。美光认为必须转向颠覆性的工艺和封装技术，包括混合键合、更高效的散热方案，以及发展"存内计算"等新架构。

> 【核对】"3×/2yr vs <2×/2yr" ✅；"~3× silicon vs DDR5" ✅；"12,344 mm²" ✅。
> ⚠️ **"约 90% 的硅片面积与内存相关"与一手幻灯片不符。** Micron p5 原页给出的是 **">8×"**（内存硅面积是典型 GPU 的 8 倍以上），按 12,344 mm² vs 典型 GPU 约 1,500 mm² 估算，内存占比约 **89%**——**推算结果接近 90%，但"90%"不是幻灯片原文**。引用时应写"按幻灯片数据推算约 89%"，而非直接引 90%。
> ⚠️ **"17% 非预期训练中断由 HBM 故障引起"**：该数字来自 Micron 引用 Meta Llama 3 论文，本库 36 份 PDF 中未见原页（该页可能未包含在用户取得的版本中）。标注为【报道】。

#### d-Matrix（重复段落，原文如此）

此外，美国 AI 芯片初创公司 d-Matrix 展示了采用 3D-DRAM 的生成式 AI 推理加速器 Raptor。该芯片通过逻辑裸片与 3D-DRAM 三维堆叠缩短信号路径、减少 PHY 接口，从而提升带宽与能效；d-Matrix 称其相比 HBM 方案在单位面积带宽和能效上有量级提升，商用产品预计于 2027 年推出。

#### 堆叠层数与产业数据

在 HBM 堆叠层数方面，三星和 SK 海力士将目标推向 16 层、20 层甚至更高，美光认为 16 层已有清晰技术路径，但超过 16 层后挑战增加。存储分析师 **Jim Handy** 在会上计算称，**HBM 每片晶圆产出的 GB 数只有标准 DDR 的三分之一**，**HBM 现货价格已较此前水平上涨约 7 倍**。**美光 2026 财年资本开支从 180 亿美元上调至 270 亿美元，增量全部投向 HBM 与先进 DRAM**。**台积电 600 到 640 亿美元资本开支中 10% 到 20% 分配给了 CoWoS 先进封装，主流前道设备交付周期已经拉长到 12 到 24 个月**。

> 【标注】以上四组数据（Jim Handy 的 1/3 与 7×、Micron capex 180→270 亿美元、TSMC capex 600–640 亿美元及 CoWoS 占比、设备交期 12–24 个月）**均无法在 36 份一手 PDF 中核实**，属媒体报道或分析师口径。本报告引用时统一标注为【报道】。
>
> 【交叉验证】"HBM 每片晶圆 GB 数只有 DDR 的 1/3"与 Micron 的"同容量需 3× 硅面积"是同一事实的两种表述，**互相印证**，可信度较高。"HBM 现货涨价 7 倍"与知乎文章提到的 "branded DRAM 7.1×、NAND 6.9×" 量级一致，但**周期口径不同**，不可直接等同。

### 行业影响与展望

Hot Chips 2026 于 2026 年 8 月 23 日至 25 日在美国斯坦福大学举行，是全球高性能芯片领域的重要技术研讨会，被视为芯片行业总结与展望下半年趋势的重要会议。本届会议聚焦 AI 加速器、内存、封装等最新架构，展示 AI 时代数据中心重构方案。

本届大会显示 AI 基础设施正从以训练为主转向以推理为主，智能体 AI 成为核心驱动力。NVIDIA 预言，AI 推理的下一个时代不会由单一突破性芯片、网络或系统来定义，它将由 AI 工厂每一层的协同运作来定义。先进封装技术（如混合键合、EMIB、CoWoS 等）成为 HBM 和 AI 芯片发展的关键。美光在演讲中指出，AI 加速器计算能力约每两年增长三倍，HBM 带宽同期增长不到两倍。

内存厂商、GPU 设计商、代工厂和封装厂商需从一开始就协同设计，以应对内存墙和封装挑战。大会展示芯片行业对智能体 AI 的重视，通用计算与专用加速融合，开放芯粒标准（UCIe、RISC-V）受到重视。

d-Matrix 在大会上介绍了其 Raptor 3D-DRAM 生成式 AI 推理加速器，该加速器采用 3D-DRAM 与逻辑裸片面对面堆叠架构，单张 Raptor 卡带宽超过 100 TB/s，**每 GB/s 功耗较 HBM 方案改善 13.5 倍**，直指 AI 推理的内存墙困境。d-Matrix 预计 Raptor 商用产品将于 2027 年推出，3D-DRAM 能否重塑 AI 推理内存架构，将取决于其在大规模部署中的实际表现。

AI 时代最稀缺的资源，正从"能做多少次计算"转向"每焦耳能把多少有用数据送到计算单元"。HBM base die 使用先进逻辑工艺并集成客户 IP 后，内存竞争不再只是 DRAM 制造，晶圆代工、逻辑设计、先进封装、EDA、接口标准和软件工具都会进入同一个项目。

---

## 附：核对结果汇总

| # | 百科表述 | 一手幻灯片 | 结论 |
| --- | --- | --- | --- |
| 1 | Vera Rubin NVL72 190–230 kW / Midplane / PCB 46–52 层 | 未出现 | ⚠️ 非会议披露 |
| 2 | 800 VDC、100% 液冷 | ✅ | ✅ |
| 3 | Vera 88 核 Olympus | ✅ | ✅ |
| 4 | Groq 3 LPX 3,400 TPS @ 100K | 幻灯片为 11,000 TPS（Gemma 4 31B） | ⚠️ 口径不同 |
| 5 | Spectrum-X 512,000 GPU | ✅ | ✅ |
| 6 | CUDA 向 RISC-V 扩展、RVA23 | ✅ | ✅ |
| 7 | MI455X 8× N2 计算芯粒 + 3D 混合键合、12 组 HBM4、432 GB | 实为 2×IOD(N3P)+8×XCD(N2)+2×FCD(N3P) | ⚠️ 不完整 |
| 8 | Helios 72 GPU、2.9 EF | ✅ | ✅ |
| 9 | DMR 256 核 / 1.28 GB LLC / 16ch 12800 MT/s / 128 lane / 2027 | ✅ | ✅ |
| 10 | Crescent Island 32 Xe / 256 XMX / 480 GB / 350 W | ✅（但自有卡 160 GB） | ⚠️ 需补口径 |
| 11 | Wildcat Lake 2P+4E / NPU 17 TOPS / UCIe 8 GT/s | ✅ | ✅ |
| 12 | 29% 裸片回收、删除光追 | 未出现 | ⚠️ 媒体补充 |
| 13 | IBM 11 核 / 5.7 GHz / 2nm / 双 ISA / 16 AI 核 / 96 GB HBM3e | ✅ | ✅ |
| 14 | Arm AGI 136 核 N3P | ✅ | ✅ |
| 15 | d-Matrix 32 GB / >100 TB/s / 2027 | ✅ | ✅ |
| 16 | Samsung 三阶段 cHBM/aHBM/zHBM、HPB >35%、zHBM −70%/230%/100W/8.3% | ✅ | ✅ |
| 17 | SK hynix 混合键合 die +24% / pitch <18µm / 热阻 −35% | +24%、<18µm ✅；"−35%" 表述错误 | ❌ 部分错 |
| 18 | SK hynix HBM4 >2TB/s / 40%+ / 48 GB / 12Hi 量产 16Hi 认证 | ✅ | ✅ |
| 19 | Micron 3×/2yr vs <2×/2yr、~3× 硅面积、12,000 mm² | ✅ | ✅ |
| 20 | Micron "约 90% 硅片面积与内存相关" | 原页为 ">8×" | ⚠️ 推算值 |
| 21 | Micron "17% 训练中断由 HBM 故障引起" | 未见于本库 PDF | ⚠️ 待核 |
| 22 | Jim Handy 1/3 GB 产出、7× 涨价 | 无法核实 | ⚠️ 报道 |
| 23 | Micron capex 180→270 亿美元 | 无法核实 | ⚠️ 报道 |
| 24 | TSMC capex 600–640 亿、CoWoS 占 10–20%、交期 12–24 月 | 无法核实 | ⚠️ 报道 |
