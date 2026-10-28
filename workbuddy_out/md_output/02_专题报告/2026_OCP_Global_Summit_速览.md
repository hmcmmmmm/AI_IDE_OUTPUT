# 2026 OCP Global Summit 会议速览

> 整理日期：2026-10-18　｜　资料来源：opencompute.org 官方会议页、2026 OCP Global Summit 官方 App 页、行业媒体综述
> 说明：本文为会议**信息整理**，非官方翻译；技术细节以 OCP 官方发布的规范与演讲稿为准。

## 一、基本信息

| 项目 | 内容 |
| --- | --- |
| 会议全称 | 2026 OCP Global Summit（开放计算项目全球峰会） |
| 时间 | 2026 年 10 月 12–15 日（主旨演讲集中在 12、13 日） |
| 地点 | 美国加州圣何塞 · San Jose McEnery Convention Center |
| 主办 | Open Compute Project Foundation（OCP） |
| 规模 | 官方售罄（SOLD OUT），现场不设报名；据行业整理，共 32 个分会场、400–500 场演讲 |
| 主题 | Building the Next Era of AI Infrastructure（构建下一代 AI 基础设施） |
| 2027 年 | 移师旧金山 Moscone Center（官方已公告） |

## 二、资料发布状态（重要）

1. 官方口径：**"所有场次均会录像；全部演讲的视频与幻灯片将在会后数日内上传至 OCP 官网"**（原文见会议页 Notes）。
2. 实际情况：截至 2026-10-18，`opencompute.org` 的 2026 Global Summit 会议页**尚未挂出任何 session 列表或幻灯片链接**（页面仅保留售票与直播说明）。
   可对照：2026 OCP EMEA Summit（4 月·都柏林）页面已完整挂出各场次的 YouTube 录像与幻灯片（Google Drive / Dropbox 双份）。
3. 网络限制：本次整理所处网络**无法访问 Google Drive / Dropbox / YouTube**（连接被阻断），即使官方链接放出也无法直接抓取 PDF；
   `opencompute.org` 自托管文档（`/wp-content/uploads/...pdf`）可正常下载。
4. 目前流传的 Global Summit 全量资料包为第三方整理的百度网盘分享（需登录 + 提取码，非官方源），本资料库未收录。

**建议跟踪入口**

- 会议页（幻灯片发布处）：https://www.opencompute.org/events/ocp-summit/2026-ocp-global-summit/
- 往届资料总入口（会后统一归档于此）：https://www.opencompute.org/events/past-events/
- OCP 文档库（规范/白皮书）：https://www.opencompute.org/documents
- OCP 官方 YouTube 频道（录像）：https://www.youtube.com/@OpenComputeProject

## 三、主旨演讲（Keynotes，15 场）

1. Welcome to the 2026 OCP Global Summit
2. Building the Next Era of AI Infrastructure
3. Concrete to Code: Engineering AI Infrastructure at Gigawatt Scale
4. The Agentic Decade Starts with Open Infrastructure
5. Scaling AI Infrastructure Through Open Innovation
6. AI Factories at Scale: Advancing Open Infrastructure for Agentic AI
7. OCP Welcome Address
8. Intelligence Infrastructure: Scaling AI for the Frontier Era
9. Scaling AI Infrastructure Responsibly Through Open Standards
10. Women in OCP (WOCP) – Community First, AI Forward
11. Secure Control and Management Plane (SCMP): From AI Racks to Autonomous Infrastructure
12. Scalable and Open AI Solutions: From Cloud to Sovereign to Edge
13. Put Every Prompt in Its Place
14. Shifting to DC Power Distribution in Data Centers: A Collaborative Journey
15. Intelligent Infrastructure for the Intelligence Era

## 四、技术主线（据行业媒体与参会者综述，供参考，未经官方逐条核实）

本届的核心叙事是 **AI 基础设施的重新分工**：内存与计算解耦、GPU 与专用加速器分工、芯片到电网的共同设计。

**1. AMD：Helion 智能体机架**
区分 Helion（CPU / CPU+GPU 混合，纯 CPU 最高 32,768 核，承担智能体执行）与 Helios（GPU 机架）；AMD 计划向 OCP 贡献相关规范，合作方配置预计 11 月起供货。

**2. NVIDIA：MGX 1.2 与 Vera Rubin 开放机架**
通过 MGX 开放架构贡献 Vera Rubin 机架与计算托盘设计，涵盖液冷盲插、可配置 I/O、无风扇托盘、液冷大电流母排，支持约 250 kW 机架；开放部分 DSX AI 工厂管理软件。Rubin Ultra NVL576 的 Scale-up 将采用 CPO。

**3. Meta：全栈开放 AI 网络**
IcePack 液冷网络机架、102.4 Tb/s 的 IceCube 交换平台、Flattened Planar Fabric 多平面网络、MetaRoCE，以及开放交换机平台架构 OSPA；交换芯片、拓扑、协议、OS、液冷一体化设计。

**4. SK hynix：MARS 内存中心型 AI 机架系统**
内存从单机解耦为共享内存池；多轮智能体推理中共享 KV Cache 相较重算带来 3–5 倍首 Token 性能改善；HBF Cube 计划 2028 年初送样。

**5. d-Matrix：Squadron 多机架推理系统**
最高 16 机架 / 1,024 颗 Corsair XPU，风冷，已向优先客户交付；主打 Attention–FFN 拆分，与 GPU 异构协同而非替换。

**6. 供电与光互连的系统工程化**
Google 提出开放数据规范 v0.7 与电网韧性规范（扰动后 2 秒内恢复近满载）；微软 Mt. Diablo 电源侧柜实现电力转换与计算机架分离（约 100 kW 至 1 MW+ 模块化）；固态变压器、储能安全与配电标准同步推进。
光互连方面，Lightmatter + Dell 讨论 CPO 的 MHS 平台接口约定，Credo + SENKO 展示微发射器与盲插光背板，Ayar Labs / Wiwynn 展示光学 Scale-up 架构。

**7. 定制推理芯片**
微软 Maia 300：推理优先架构，8 组 HBM4、18 TB/s 峰值带宽、950 W TDP；96 加速器机架提供 27.6 TB HBM、约 1.7 PB/s 聚合带宽，计划 2027 年投产。

> 来源：上海未尽信息科技咨询《2026 OCP 全球峰会划重点》（2026-10-15）。以上为二手整理，引用前请以 OCP 官方稿件为准。

## 五、可直接使用的地址清单（2026-10-18 实测）

| 用途 | 地址 | 实测状态 |
| --- | --- | --- |
| 峰会主页（幻灯片将挂在此页） | https://www.opencompute.org/events/ocp-summit/2026-ocp-global-summit/ | 可访问，**无任何 session 或文稿** |
| 峰会主题页（说明性内容） | https://www.opencompute.org/events/ocp-summit/2026-ocp-global-summit/theme/ | 可访问，无文稿 |
| 往届资料归档总入口 | https://www.opencompute.org/events/past-events/ | 可访问，2026 峰会条目下无 slides 链接 |
| 对照：2026 EMEA 峰会（已挂全量文稿） | https://www.opencompute.org/events/ocp-summit/2026-ocp-emea-summit/ | 可访问，约 120 场，含 YouTube + G-Drive + Dropbox |
| 对照：2025 Global Summit（往届完整形态） | https://www.opencompute.org/events/ocp-summit/2025-ocp-global-summit/ | 可访问，全量 session + 文稿 |
| 第三方整理包（Global Summit 2026，500+ 场） | https://pan.baidu.com/s/1jorjxNaC1Z7CkYtu6D5kXg　提取码 `vuqk` | 链接有效（需登录百度网盘） |
| 第三方整理包（APAC Summit 2026，台北） | https://pan.baidu.com/s/1T3fptI5wQ0DBBkB8MIVPng　提取码 `gidd` | 链接有效（需登录百度网盘） |
| 官方 YouTube 频道（录像，会后陆续上线） | https://www.youtube.com/@OpenComputeProject | 本机网络不可达 |

**网络实测结论**：`opencompute.org`、`ocpasia.org`、`pan.baidu.com` 可访问；`drive.google.com`、`dropbox.com`、`youtube.com` 连接被阻断。
因此 OCP 官方一旦发布（其幻灯片固定使用 Google Drive + Dropbox 双托管），**在本次整理所处网络内仍然无法直接下载**，需换网络环境或用网盘包。

## 六、本目录内容

- 本文件：会议速览与资料状态说明
- `keynotes.txt`：主旨演讲原始英文标题清单（便于检索官方录像）
- 官方幻灯片发布后，可将 PDF 直接放入本目录，并在 `../index.html` 中登记。
