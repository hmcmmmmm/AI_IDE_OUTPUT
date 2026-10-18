# NVIDIA 官方 Hot Chips 2026 活动页与技术博客组

| 项目 | 内容 |
| --- | --- |
| 主页面 | https://www.nvidia.com/en-us/events/hot-chips-conference/ |
| 抓取时间 | 2026-10-18 |
| 性质 | **厂商官方口径**。无 PDF 下载，但正文比任何媒体稿都详细 |
| 证据等级 | **高（官方，但为营销口径）**。技术参数可与一手幻灯片逐条核对；性能倍数均为自测且常带 "*Unofficial Results" 免责声明 |
| 配图 | 官方页为动态渲染的产品图/架构图，未做图片本地化；对应架构图请使用 `images/01_*` ~ `03_*`、`16_*`、`17_*`、`37_*`、`38_*`、`46_*`（均来自 NVIDIA 自家幻灯片，精度更高） |

## 为什么这是"最详细的免费一手资料"

NVIDIA 在这次 Hot Chips 上讲了 6 场（1 场 Tutorial + 5 场 Talk），是全场最多的单一厂商。官方活动页把 6 场的标题、讲者、时间全部列出，并配 6 篇技术博客做参数补充。对于拿不到 PDF 的读者，这是唯一能拼出完整 NVIDIA 叙事的公开渠道。

**关键认知**：NVIDIA 在 Hot Chips 2026 讲的已经不是"一颗 GPU"，而是**"七个芯片、五个机柜"的整机柜协同设计**。这条主线贯穿全部 6 场演讲。

---

## 一、演讲清单（官方页原样）

| 时间 | 场次 | 题目 | 讲者 |
| --- | --- | --- | --- |
| 8/23 15:45 | Tutorial | RISC-V Profile and Platform for Interoperability With NVIDIA GPUs | Frans Sijstermans |
| 8/24 10:30–11:00 | Talk | NVIDIA's Vera CPU | Jonathon Evans、Polychronis Xekalakis |
| 8/24 16:45–17:15 | Talk | NVIDIA Rubin GPU: Driving the Era of Agentic AI | Manas Mandal、Rajballav Dash、Ravi Manyam |
| 8/25 11:30–12:00 | Talk | NVIDIA BlueField-4 Processor Powers the AI Factory Operating System | Idan Burstein |
| 8/25 12:00–12:30 | Talk | NVIDIA Spectrum-X Multiplane Network Architecture | Gilad Shainer |
| 8/25 14:45–15:15 | Talk | Think Fast: LPU Accelerator for Heterogeneous Compute | Igor Arsovski、Santosh Raghavan |

> 注：另有一场 Hot Interconnects 2026 主题演讲（Gilad Shainer，"Networking Innovations for Gigascale AI Systems"），不在 Hot Chips 议程内。

---

## 二、官方页给出的核心参数（原文照录）

### NVIDIA Vera CPU

> "the world's first processor purpose-built for the age of agentic AI—delivering **1.8x faster task completion** and **twice the efficiency** of traditional x86 CPUs. Powered by **88 custom Olympus cores** with the highest single-thread performance and bandwidth per core."

**【一手核对】** Vera 幻灯片确认：
- **88 个 Olympus 核 / 176 线程**（spatial multithreading，为确定性而非 SMT）
- **10-wide decode，每周期 16 条指令**
- **64 KB L1I / 96 KB L1D / 2 MiB L2**
- **164 MB L3**；**2 代 SCF，3.4 TB/s bisection 带宽**
- **1.5 TB SOCAMM LPDDR5X @ 1.2 TB/s**；**4.3 TB/s 聚合 off-die 带宽**
- **1,800 GB/s NVLink-C2C**；**x16 PCIe Gen6 = 256 GB/s**；CXL 3.1
- SPECrate2026_int：**1.2–1.8× vs AMD EPYC 9755**（agentic 1.8× / 数据处理 1.5× / EDA 1.7×）
- LPDDR5X-9600 = **5× 带宽/瓦**
- Vera 液冷机柜：**256 颗 Vera / 22,528 个 Olympus 核**
- 浏览器 Speedometer **快 24%**，去掉渲染后最高 **4.5×**；数据加工 p99 流式延迟 **6× 优于 Turin**

见 `images/16_vera_spec.png`、`images/17_vera_scf.png`。

### NVIDIA Vera Rubin

> "With **extreme co-design across seven chips**, NVIDIA Vera Rubin delivers flexible deployment options while slashing training and inference token costs."

**【一手核对】** Rubin 幻灯片的关键框架：
- **"seven chips and five racks"**：Vera Rubin NVL72（基础平台）、Vera CPU Rack（工具调用与沙箱）、Groq 3 LPX（提升交互性）、Spectrum-6 SPX（scale-out fabric）、Vera BlueField-4 STX Storage（上下文内存存储）
- 宣称 **"up to 30× greater AI factory throughput"**（TPS/MW）、**10× 交互性**、**2× vs GB300**——注意原页标注 **"\*Unofficial Results. Pending SemiAnalysis Review"**
- **NVLink 6**：**3.6 TB/s 每 GPU all-to-all**、**72-GPU 域**、**130 TFLOPS 网络内计算**、**3× 更低延迟**、**10× 包速率**
- **2:4 稀疏 NVFP4**；sparsify attention 让 SoftMax/BMM2 快 **2×**
- **45 °C 进水温度液冷、无需冷机、800 VDC、无 retimer、无电缆托盘**
- 智能功率平滑：**峰值功率降 13% → 同样 provisioned 瓦数下多装最多 40% GPU**
- 第二代 RAS 引擎：零停机健康检查
- **100 MW AI 工厂 = 2 ZFLOPS NVFP4 推理 / 1.4 ZFLOPS 训练 / 11 PB HBM4 / 800 PB/s**

见 `images/01_rubin_seven_chips_five_racks.png`、`images/02_rubin_100mw_ai_factory.png`、`images/03_rubin_nvlink6.png`。

### NVIDIA Groq 3 LPX

> "LPX features **256 LPUs** with **128 gigabytes (GB) of SRAM**, **40 petabytes per second (PB/s)** of memory bandwidth, and **640 terabytes per second (TB/s)** of scale-up bandwidth per rack."

**【一手核对】** LPU 幻灯片（Igor Arsovski）：
- **全 SRAM 平坦内存层级**，无 HBM、无外部 DRAM
- 计算通过高带宽 **"streams"** 供给；所有单元跨多颗 LPU **同步 lockstep**
- 功能单元：**MEM**（片上 SRAM）、**VXM**（向量 PE）、**MXM**（MAC 矩阵）、**SXM**（数据 reshape）
- **VLIW 架构**，指令控制面积开销小
- **软件调度到 CLK 周期粒度**，吞吐可预测；无 kernel 边界、无 MEMBAR
- 性能：**11,000 TPS**（Gemma 4 31B，coding benchmark）；**4× 更快**（100K 上下文，Artificial Analysis 第三方）

> ⚠️ **口径提醒**：NVIDIA 官方页写 256 LPU/128 GB SRAM/40 PB/s/640 TB/s；幻灯片写 11,000 TPS；百度百科引述"10 万 Token 长上下文 3,400 TPS"。三者 benchmark 不同，**不可混用**。

见 `images/46_lpu_sram.png`。

### NVIDIA BlueField-4

> "BlueField-4 is the **first AI native DPU**."

**【一手核对】** BlueField-4 幻灯片：
- **Grace CPU**：**64 核 Arm Neoverse V2 @1.7 GHz**、**SPECint 220（6× BF3）**、**LPDDR5 275 GB/s**
- **ConnectX-9**：**800G 以太网（2× BF3）**、**200G PAM4 SerDes**、**PCIe Gen6 x16**、**200 MPPS**、**25 MIOPs**、inline 加密（PSP/TLS/IPSec/AES-XTS）
- **每张 Vera Rubin 计算托盘需要 7 Tb/s 聚合网络带宽**（4×1.6 Tb/s GPU scale-out + 800 Gb/s GPU scale-in）
- 对比传统方案：**安全性更高**（scale-out 流量被隔离）、**功耗低 4×**（不必为每个 NIC 配一套 CPU/内存/连接）
- Astra 架构让 DPU **独占数据通路**，7 Tb/s 下零信任与遥测全开且不碰主机
- Storage-Scale（CMX）：**3.2 Tb/s 存储访问、10× IOPS、5× 能效**
- NVMe over Fabrics：**8 核跑满 1.6 Tb/s，16 核跑 20M IOPS**

见 `images/37_bf4_7tb.png`。

### NVIDIA Spectrum-X Ethernet Multiplane

> "Spectrum-X Ethernet Multiplane **extends AI-factory scale by 64X**."

**【一手核对】** Spectrum-X 幻灯片：
- 传统 ToR 拓扑：**2k GPU**
- Multi-Rail 拓扑：**8k Rubin GPU**（每 GPU 1.6 T scale-out，100T 交换机 64 口 × 1.6T，4 rail）
- **Multiplane 拓扑：512k Rubin GPU**（100T 交换机 512 口 × 200G，8 plane，4 rail）
- **省 1.7× scale-out 交换机**（同等规模下）
- **故障时保持 90% 带宽**（对比传统多层单 rail 拓扑直接掉到 0%）
- 检测时间 **2.68 ms（400× 更快）**，恢复时间 **100 ms（11× 更快）**
- **1.6× AI 工厂 goodput**
- 对比通用以太网：**1.3× 更低 jitter、2.2× 多租户带宽、1.6× 更高 RDMA 带宽**
- 多租户训练：**1.9× 训练性能**（DeepSeek V3，多任务环境）
- NCCL：**最高 14× 性能**（Gradient All Reduce 2× / Token Dispatch 2× / Reduce Scatter 3.5× / 并行矩阵乘 14×）
- **CPO 硅光**：微环调制器 + TSMC Coupe 3D 堆叠，量产中；**10× 更低 MTBI、5× 更低功耗、4× 更少激光器**
- **光互联耗电 ≈ 计算功耗的 10%**
- Spectrum-XGS：跨数据中心 **1.9× 多站点性能**，800 Gb/s/端口，102.4 Tb/s

见 `images/38_spx_512k.png`。

### NVLink Fusion

> "Deploy XPUs with faster time-to-market, leading NVLink scale-up performance, and unified MGX rack architecture."

**【一手核对】**
- **3.6 TB/s 每 XPU all-to-all**、**3× 更低延迟**、**72 XPU 单域**
- **18 个计算托盘 + 9 个 NVLink 交换托盘 + 1 个 NVLink spine**
- **无电缆、无软管、模块化**；**45 °C 进水**；**100% 液冷**
- 可接 **NVIDIA Vera 或自定义 CPU**，XPU 通过 **NVLink-C2C** 或 **chiplet** 接入

---

## 三、官方博客与新闻稿链接（原文照录）

| 类型 | 标题 | URL |
| --- | --- | --- |
| 新闻稿 | NVIDIA Groq 3 LPX Now in Full Production With World-Class Speed for Agentic AI | https://nvidianews.nvidia.com/news/nvidia-groq-3-lpx-now-in-full-production-with-world-class-speed-for-agentic-ai |
| 新闻稿 | SpaceXAI Adopts NVIDIA Vera CPUs for Agentic AI | https://nvidianews.nvidia.com/news/spacexai-adopts-nvidia-vera-cpu-to-accelerate-agentic-ai-at-massive-scale |
| 博客 | With Groq 3 LPX in Full Production, NVIDIA Extends Vera Rubin Inference for Agents | https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/ |
| 技术博客 | How NVIDIA Groq 3 LPX Enables Fast Interactivity | https://developer.nvidia.com/blog/how-nvidia-groq-3-lpx-unlocks-ultrafast-interactivity-at-long-context-on-nvidia-vera-rubin/ |
| 技术博客 | How NVIDIA Vera CPU Solves Agentic CPU Fleet Optimization Problem | https://developer.nvidia.com/blog/solving-agentic-ai-fleet-challenges-with-nvidia-vera-cpu/ |
| 博客 | How XPUs Meet a World-Class AI Factory | https://blogs.nvidia.com/blog/nvlink-fusion-xpu-ai-factory/ |
| 技术博客 | NVIDIA Scale-In: AI Factory Network Infrastructure | https://developer.nvidia.com/blog/nvidia-bluefield-4-powers-new-scale-in-network-infrastructure-for-agentic-ai-factories |
| 技术博客 | Gigascale AI and the Ethernet Evolution: How Spectrum-X Ethernet Rewrites the Rules | https://developer.nvidia.com/blog/giga-scale-ai-ethernet-evolution-spectrum-x-ethernet-rewrites-rules/ |

> 以上 8 条均可在官方活动页直接点开。本档案不复制其正文（属 NVIDIA 版权内容且为营销文案），仅保留链接与要点摘录。

---

## 四、从官方口径里能读出的三条真实信号

官方博客是营销文案，但**营销文案的选择本身透露战略**。三条值得注意：

1. **"七个芯片、五个机柜"是 NVIDIA 第一次在 Hot Chips 上把整机柜当作"产品"讲。** 过去 Hot Chips 是讲单芯片微架构的场合，NVIDIA 这次把 CPU、GPU、LPU、DPU、交换机、存储处理器全部打包，说明它认为竞争单位已经从芯片上移到机柜。

2. **LPX 的"全 SRAM、无 HBM"是一个明确的架构赌注。** 在一个所有人都在堆 HBM 的会议上，NVIDIA 用 256 颗 LPU + 128 GB SRAM 做纯低延迟推理，等于承认"GPU + HBM 不是所有推理负载的最优解"。这是对 d-Matrix、Cerebras、SambaNova 等"反 HBM"路线的间接认可。

3. **Spectrum-X Multiplane 的 512k GPU 是全场最大的单一规模数字。** 它比 Google TPU 的 9,600 芯片/pod、AMD Helios 的 72 GPU/柜、AWS 的任何公开数字都高一个量级以上。但要注意：512k 是**拓扑可支持的上限**（512 口 × 200G × 8 plane），不是已部署规模。

---

## 五、与一手幻灯片的口径差异汇总

| 项目 | 官方页 / 博客 | 一手幻灯片 | 差异说明 |
| --- | --- | --- | --- |
| Rubin 性能倍数 | "up to 30× AI factory throughput" | 同，但标注 "*Unofficial Results. Pending SemiAnalysis Review" | 官方页省略了免责声明 |
| Vera 效率 | "twice the efficiency of traditional x86" | SPECrate2026_int 1.2–1.8× vs EPYC 9755 | 官方页未给出对比基线 |
| LPX 吞吐 | 256 LPU / 128 GB / 40 PB/s / 640 TB/s | 11,000 TPS（Gemma 4 31B coding） | 官方页给硬件，幻灯片给 benchmark |
| BlueField-4 | "first AI native DPU" | 7 Tb/s、64 核 Grace、ConnectX-9 800G | 一致 |
| Spectrum-X | "64× scale" | 2k → 8k → 512k GPU | 64× = 512k/8k，基数需注意 |
