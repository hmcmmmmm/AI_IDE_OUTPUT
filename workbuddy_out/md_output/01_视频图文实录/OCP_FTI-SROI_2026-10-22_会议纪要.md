# OCP「短距光互连」工作流会议纪要

**FTI → OCP 官方工作组的毕业提案，与《Optical Connectivity Options》命名表评审**

| 项目 | 内容 |
| --- | --- |
| 会议 | FTI – SROI（Short Reach Optical Interconnect）workstream 例会 |
| 时间 | 2026 年 10 月 22 日（周四），21 分 07 秒 |
| 发布 | Open Compute Project 官方频道，2026-10-23 上传 |
| 形式 | 线上例会（屏幕共享 + 口播），无正式议程文档 |
| 主持 | Bobby Lu（SROI 白皮书编者） |
| 主讲 | Ron Swartzentruber（提案部分）、Bobby Lu（命名表部分） |
| 原片 | https://www.youtube.com/watch?v=Tug9Ax_VtBM |
| 材料 | 9 页提案幻灯片（草稿，2026-10）+《Optical Connectivity Options》v0.5.5（2026-10-22，7 页） |

> **本文的证据规则**：正文中的数字与结论一律以**幻灯片/文档原文**为准；口播与幻灯片冲突处单列于第五节。字幕为 YouTube 自动生成，专有名词错误率较高（如把 NPO 听成 MPO、pJ/b 听成 pJ/s），已逐条校正。附录 A 保留完整英文原话与时间戳，供回溯。

---

## 摘要：五条要点

**1. SROI 正式"毕业"。** 运行在 FTI（Future Technologies Initiative）下的 SROI 工作流，将升级为 OCP 官方工作组，挂靠 OCP Networking 项目，成立 **Optical Connectivity / CPO / xPO 子项目**，下设 6 个工作流。SROI 保留原名，作为 WS1 内的 scale-up 剖面。

**2. 组织设计的关键是"一个家"。** 提案把 SROI、OCI、CPX 与 optical engine 四摊事收到同一个 OCP 屋檐下，理由是它们共享同一批公司、同一条技术栈、同一组接口。子项目要招 **2 名以上 co-lead，优先来自 operator（超大规模云厂）**。

**3. SROI 的量化目标已经写完，不需要重新讨论。** ≤10 pJ/b（目标 ≤7）、≤2 FIT、≤30 m、1 Tbps/mm（目标 2）——全部来自 2026 年 8 月 5 日发布的白皮书 1.0.0 附录 A。

**4. 技术核心是一张命名表。** 《Optical Connectivity Options》0.5.5 把光引擎的六种摆放位置按"信号损耗距离"从长到短排序，并用**同一条判据**划开 NPO 与 CPO：光引擎模块是否可插拔、是否被同一个 lid 覆盖。

**5. 会上出现了实质性的保留意见。** 一位与会者指出：SROI 的覆盖面已经超出"网络"范畴（部分工作落在 server 侧），把它整体塞进 Networking 项目是否合适，尚未定论；提案本身"还很湿"（still pretty wet）。

---

## 一、会议定位与背景

### 1.1 这场会是什么

![提案封面：Optical Connectivity / CPO / xPO Subproject（OCP Networking Project · Proposal · 2026-10）](images/01_title.jpg)

这不是一场对外演讲，而是一次**内部工作流例会**，只有 21 分钟，前 5 分钟在解决日历邀请的技术问题，中段 9 分钟过提案，后段 5 分钟评审命名表，最后提前散会。它的信息价值不在"发布了什么"，而在**一个开放标准组织如何把一个自下而上的工作流，转成有章程、有工作流划分、有交付物的正式项目**——这个过程通常不会公开留档。

会议标题里的 `85206871737` 是 OCP 日历的事件编号，不是文档号。

### 1.2 为什么现在做这件事

提案第 2 页给出三条硬约束，构成整个工作的动机：

![Why now：铜缆在 AI scale-up 场景已经到达物理极限](images/02_why_now.jpg)

- **1–1.5 m**：200G/lane 下无源铜缆的极限距离，即使用 fly-over cable 也只能到此；
- **500–1,000+**：下一代多机架 pod 里的加速器数量；
- **≤30 m**：SROI 设定目标的短距光域。

三条放在一起就是一句话：**单个 pod 内的互连距离需求（米级）已经超过铜的物理上限（1.5 m），而光器件又要在这个距离上做到可批量部署的成本与可维护性。** 这正是 OCP 相对 OIF/IEEE 的定位——不重复做 PHY 标准，而是定义"让 operator 能从多家供应商规模部署"所需的开放接口、形态、可靠性与可维护性要求。

> **【判断】** 这个定位是清醒的：OIF 管电口/光口参数，IEEE 管以太网 MAC/PHY，OCP 管"机柜里怎么装、坏了怎么换、谁来认证"。三者不冲突，但**只有 OCP 这一层是 operator 直接说了算的**，这也是它要求 co-lead 必须来自 operator 的原因。

---

## 二、提案：从 FTI 工作流毕业为 OCP 官方工作组

### 2.1 五个 effort、五个层级

![五个 effort 对应五个层级，彼此重叠很小](images/03_five_efforts.jpg)

这张表是整份提案的骨架。它按"光在系统里的位置"把五件事分层，每层标注了现状与下一步：

| 层级 | 项目 | 归属/现状 | 关键内容 |
| --- | --- | --- | --- |
| **REQUIREMENTS** | **SROI** | 白皮书 1.0.0（2026-08），正从 FTI 毕业 | scale-up 光互连的系统级目标（≤30 m）：pJ/b、FIT、密度、时延 |
| **OPTICAL PHY** | **OCI MSA** | v1.0 已发布；v2.0 在 OCP SPW 中，v1.0 贡献可选 | 200G/lane NRZ + WDM 链路，面向 AI scale-up；成员含 AMD、Broadcom、Meta、Microsoft、NVIDIA、OpenAI |
| **MODULE + SOCKET** | **CPX MSA** | 规范 2026-09 出；是否向 OCP 贡献 TBD；WS4 潜在 lead：Edi Roitman（Marvell） | 可插拔 CPO/NPO 模块，每 socket 6.4T / 7.2T，外置或集成激光 |
| **OPTICAL CHIPLET** | **Chiplet group** | 拟建半公开工作流 | 与代工厂无关（foundry-neutral）的光引擎 chiplet；GUC、GlobalFoundries 等参与，Arista 有兴趣 |
| **SERVER TRAY** | **MHS-HSIO** | 章程草案 v0.2，与本案为 liaison 关系 | MHS 托盘内的光面板、光纤走线、OE 等级 |

**读表要点**：五层不是流水线，而是**五个已经各自在跑的社群**。提案的价值在于承认它们"little overlap"（重叠很小），因此不需要合并，只需要一个共同的屋檐和一套共享的接口定义。口播里说的是 "five layers with overlap"，与幻灯片标题 "little overlap" 相反——以幻灯片为准。

### 2.2 组织架构：一个子项目、六个工作流

![一个子项目挂在 OCP Networking 之下，六个工作流横向切分](images/04_architecture.jpg)

架构图的左半是层级，右半是四条设计原则：

1. **One home, operator-led** —— 招 2 名以上 co-lead，理想情况来自 operator；
2. **SROI sets the envelope** —— 功率、FIT、距离目标约束每一个引擎、链路与模块；
3. **Specify the joins first** —— OE-to-host、OE-to-module、OE-to-laser 这三个接缝最值得先定；
4. **Server trays stay in MHS** —— 托盘级集成留在 MHS-HSIO，通过 liaison 对接。

图中有两处值得单独指出：**CPX 可插拔模块（WS4）与 on-substrate CPO 是并列的两条路径**，前者经 socket、后者直接焊在 switch/XPU 封装上；而**激光源（laser source）是跨层资源**，可以是外置激光模块（ELS），也可以集成进引擎。

六个工作流的正式定义在下一页：

![六个工作流及其开放度与首个交付物](images/05_workstreams.jpg)

| 编号 | 名称 | 开放度 | 范围 | 首个交付物 |
| --- | --- | --- | --- | --- |
| **WS1** | Operator reqs and SROI | Open | 距离分级、pJ/b、FIT、时延；scale-up 与 scale-out 两套剖面 | SROI baseline；reqs v0.5 |
| **WS2** | Optical chiplet | Semi-private | 与代工无关的 chiplet 接口；host I/F、footprint、fiber attach、管理 | Chiplet 接口参考规范 |
| **WS3** | OCI v2.0 | Semi-private | 光 PHY 已在 SPW 中起草；v1.0 贡献可选 | OCI v2.0 作为 OCP 贡献 |
| **WS4** | CPX module | MSA-led, TBD | 取决于 CPX 是否加入；天然 lead 为 Edi Roitman（Marvell） | OCP 部署剖面 |
| **WS5** | Lasers, fiber and system | Open | ELS 模块、面板光纤、shuffle、冷板 | ELS 调研；光纤指南 |
| **WS6** | Test, reliability, management | Open | 分级可靠性认证、CMIS 式管理、安全 | 测试与认证方法 |

### 2.3 WS2 与 WS4 是否合并

![合并与分立的取舍，以及 Open NPO 的参考数据](images/06_ws2_ws4.jpg)

这是全场唯一一处给出**双向论证**的地方，值得完整保留：

**合并（Option B）的理由**

- chiplet-to-socket-to-host 是同一条边界，只需要定义一次；
- 做引擎和做 CPX 模块的是同一批公司；
- 不止一种 socket 在路上（CPX 与 Open NPO）；
- Edi Roitman（Marvell）是天然 lead，可配一位代工厂 co-lead。

**分立（Option A）的理由**

- CPX 是否参与仍 TBD；
- on-substrate CPO 根本不用 socket，chiplet 接口应保持中立；
- CPX MSA 自己拥有自己的规范，WS2 则应是 OCP 规范。

底部蓝框是参考数据：**Open NPO 的模块-主机连接器为 72 对差分 + 9G 电源/低速引脚，插损 ≤1.5 dB 到 56 GHz，样品在测，并打算向 OCP 贡献。** 这条数字很关键——它说明"可插拔"这条路在 56 GHz 上还有 1.5 dB 的预算空间，不是纯理论。

> **【判断】** 提案倾向于 Option B（合并），理由是组织效率；但反对理由更硬：**on-substrate CPO 没有 socket，把它和一个以 socket 为中心的工作流绑在一起，会让 chiplet 接口规范带上 socket 假设。** 会上没有形成决议，只决定"继续在邮件列表里发酵"。

### 2.4 SROI 的四个量化目标与毕业步骤

![SROI 带着已写好的目标毕业](images/07_sroi_targets.jpg)

四个目标来自白皮书 1.0.0 附录 A（OCP，2026-08-05）：

| 指标 | 目标 | 口径 |
| --- | --- | --- |
| 能效 | **≤10 pJ/b**（目标 ≤7） | SerDes + 光器件，**一个链路端** |
| 可靠性 | **≤2 FIT** | 每个光链路端，光学件近 40 °C |
| 距离 | **≤30 m** | SROI 覆盖域，SMF 或 MMF |
| 密度 | **1 Tbps/mm**（目标 2） | ASIC 边缘的 CPO 密度 |

右侧是四步毕业流程：① 与团队确认（编者 Bobby Lu 与 Ron Swartzentruber 同意，FTI co-lead 可留在 WS1）；② 提交 FTI 领导层（白皮书已发布、多公司署名、规范工作在前）；③ **把附录 A 变成 WS1 的基线**（白皮书维持 CC BY-SA，新的规范性工作放在 OWF 之下）；④ 可选保留 SROI 这个名字，作为 WS1 内的 scale-up 剖面。

> **【判断】** 第 3 步是整个毕业动作里最实质的一步：**它把"白皮书里的目标值"从建议变成了规范基线。** 一旦附录 A 成为 WS1 baseline，后续任何引擎/模块/链路提案都要拿这四个数当验收线。这也是为什么会上没有人讨论"目标值该定多少"——那场仗在 8 月白皮书发布时已经打完了。

### 2.5 会上的保留意见

第 11 分 30 秒，一位与会者（口播中称 "James proposed…"，应为另一位成员转述 James 的意见）提出了三点保留：

1. **提案"还很湿"**（still pretty wet），现在只是讨论稿；
2. **SROI 的覆盖面超出"网络"** —— 有些工作（例如 "B John 领导的那个工作组"）落在 **server** 侧，把它们整体挂到 Networking 项目下是否合适，尚待确定；
3. 因此**哪些内容最终成为 SROI 之下的工作流，仍未定**，欢迎各方反馈。

Bobby 的回应是"对任何想法都开放，只要能把人聚在一起"，并强调今年 workshop 的质量很好、要"保持势头、建立粘性"。Ron 补充说这仍是提案，需要继续 socialize。

> **【判断】** 这段是整场会最有信息量的 90 秒。它暴露了开放标准组织的经典张力：**技术分类（网络 vs 服务器）与社群归属（谁的人、谁的例会）不是一回事。** 把 SROI 放进 Networking 是为了借现成的项目框架快速立项，但代价是 server 侧的工作要么被切走、要么被"越界"管理。这个矛盾不会因为一次会议解决，它会一路带到章程里。

---

## 三、技术核心：《Optical Connectivity Options》命名表

### 3.1 文档状态

![文档第 4 页：2 Optical Connectivity Options 与 Table 1](images/10_table_page.jpg)

会议后半段评审的是一份独立文档，不是提案的一部分：

| 项目 | 内容 |
| --- | --- |
| 标题 | Optical Connectivity Options |
| 版本 | **0.5.5** |
| 日期 | 2026-10-22 |
| 作者 | Jeff Hutchins（Ranovus） |
| 篇幅 | 7 页（1 Introduction / 2 Optical Connectivity Options / 3 Illustrations / 4 License / 5 About OCP Foundation） |
| 许可 | CC BY-SA 4.0 |
| 状态 | 拟公开发布于 OCP 网站，供社区引用与下载；评审通过后提交 |

分工值得记一笔：**Jeff 提供 Excel 与侧视图，Bobby 重绘了俯视图并重排了顺序**，两人的图合起来构成第 3 页的 Figure 1。Bobby 在会上的原话是"Jeff creates the side view and I create the top view, so it's a co-working"。

### 3.2 三类位置、六种布置

![Figure 1：六种 O/E 布置方式的侧视图与俯视图](images/09_illustrations.jpg)

这张图按**信号损耗距离从长到短**排列，是命名体系的可视化定义：

| 序 | 命名 | 位置 | 关键特征 |
| --- | --- | --- | --- |
| 1 | **Pluggable-PCB** | 面板 | 模块插在 PCB 的 cage 里，经 near-package copper 连到 MCM |
| 2 | **Pluggable-NPC** | 面板（近封装铜） | 同为可插拔，但模块更靠近封装，铜路径更短（NPC = Near Package Copper） |
| 3 | **NPO-PCB** | 封装外 | 光引擎在 PCB 上，仍有 near-package copper |
| 4 | **NPO-HDI** | 封装外 | 光引擎在 HDI 基板上，无 near-package copper |
| 5 | **CPO-SP** | 封装内（标准封装） | 光引擎在封装基板上，光纤从封装边缘引出 |
| 6 | **CPO-AP** | 封装内（先进封装） | 光引擎进入 MCM 本体（"Optical MCM"），可含 optical interposer |

图例区分了 11 种元素：Die、Interposer、Package substrate、Module PCB、PCB、Optical engine (OE)、Pluggable module、Cage、Socket/connector、Near package copper、Fiber、MCM lid。**俯视图的作用就是让"芯片边界"和"lid 边界"可见**——这是 NPO 与 CPO 的分界线，侧视图看不出来。

### 3.3 Table 1 完整还原

![Table 1：Connectivity Options and Characteristics](images/08_table1.jpg)

原表是横向 5 列（图 1 有 6 行，因为 FPO 一列覆盖了 Pluggable-PCB 与 Pluggable-NPC 两种变体）、纵向 8 行。完整还原如下：

| 属性 | FPO（面板可插拔） | NPO-PCB¹（或 OBO） | NPO-HDI² | CPO（标准封装） | CPO-AP³（先进封装） |
| --- | --- | --- | --- | --- | --- |
| **位置** | 面板前 | 封装外 | 封装外 | 封装内 | 封装内 |
| **名称** | FPO — Optics Plugged at front Panel | NPO-PCB (or OBO) — Optics on PCB | NPO-HDI — Optics on HDI | CPO — Optics with Standard Packaging | CPO-AP — Optics with Advanced Packaging |
| **连接方式** | 面板上的 receptacle | 焊在或插在 PCB 上 | 焊在或插在 HDI 上 | 焊接（标准封装） | 焊接（先进封装） |
| **高速间距** | ~0.5–1.0 mm | PCB：0.6–1.0 mm | HDI：0.3–0.5 mm | C4 bump / ~110 µm | µbump / ~30–50 µm |
| **高速电接口** | 高速，>22 dB/2000 | Flex/Cable：13–18 dB/2000；PCB：16–22 dB/2000 | HDI：13–18 dB/2000 | 高速 & D2D（如 UCIe-S、BoW） | 高速 & D2D（如 UCIe-A、BoW） |
| **特征** | 可用集成铜连接、copper flex 或 PCB 走线 | 同上 | HDI 走线 | 最低损耗；高带宽边缘密度；SoC 集成 | 最低损耗；最高带宽边缘密度；高度集成 SoC |
| **互操作性与绑定** | 全生命周期内可与可互操作光件替换，一般支持热插拔 | 焊接：可互操作但不可替换；插接：拆刀片时可替换 | 同左 | chiplet 级可互操作，但不可替换 | chiplet 级可互操作，但不可替换 |
| **标准** | 已标准化 | 标准正在制定 | 标准正在制定 | 部分标准已有，其余待制定 | 部分标准已有，其余待制定 |

**脚注（原文）**

1. NPO-PCB 的实现有时被称为 On-Board Optics（OBO）。
2. NPO-HDI 的部分"板上封装"实现有时被称为 "CPO"（CPO-HDI）。
3. CPO-AP 中用 interposer + µbump 实现光学的一种具体方案，被称为 Co-Integrated Optics（CIO）。

> 上表共 6 列，窄屏下可横向滚动查看 CPO 与 CPO-AP 两列。

### 3.4 判据：NPO 还是 CPO

口播里花了最长的一段解释这张表最容易被误用的地方，值得完整还原：

> 我们讨论的关键之一是"模块"这一层。比如 CPX 那种可插拔 socket——无论它是否在同一基板上，只要它**没有被同一个 lid 覆盖**，就应该叫 **NPO**；只有当它**完全被同一个 lid 覆盖**时，才叫 **CPO**。

也就是说，**判据不是"在不在封装里"，而是"在不在同一个 lid 下、能不能拔"。** 这条判据解释了两件容易混淆的事：

- **CPX 可插拔模块属于 NPO 家族**，哪怕它已经贴在封装基板上——因为它有 socket、能拔、有自己的盖子；
- **on-substrate CPO 才属于 CPO 家族**——焊死、不可替换。

脚注 2 进一步承认了历史的混乱：**某些被厂商称为 "CPO" 的方案，按这套定义其实是 NPO-HDI（CPO-HDI）。** 这句话是整份文档最锋利的一处，因为它等于在说"过去几年市面上有一部分 CPO 宣传，命名是错的"。

> **【判断】** 命名表真正的价值不在分类，而在**给采购与验收提供了一套不可含糊的坐标系**。运营商招标时最怕的不是技术不好，而是"你说 CPO 我说 CPO，其实不是一回事"。把 lid 边界写成判据，就把这件事变成了可验收的物理事实。

### 3.5 一条贯穿全表的规律：pitch 与损耗的反向关系

把表 1 的四行数字纵向读，会看到一条非常干净的单调关系：

| 方案 | 高速间距 | 高速电接口损耗 | 可替换性 | 标准成熟度 |
| --- | --- | --- | --- | --- |
| FPO | 0.5–1.0 mm | >22 dB/2000 | 热插拔 | 已标准化 |
| NPO-PCB | 0.6–1.0 mm | 16–22 dB/2000（PCB） | 插接可换 / 焊接不可换 | 制定中 |
| NPO-HDI | 0.3–0.5 mm | 13–18 dB/2000 | 同上 | 制定中 |
| CPO | ~110 µm | D2D 级 | 不可替换 | 部分已有 |
| CPO-AP | ~30–50 µm | D2D 级 | 不可替换 | 部分已有 |

**间距缩小约 20 倍（1.0 mm → 50 µm），损耗从 >22 dB 降到 D2D 量级，代价是可替换性从"热插拔"一路退到"不可替换"，标准成熟度从"已标准化"退到"部分已有"。**

这正是文档引言里的那句话的量化版本：*"moving optics closer to the ASIC shortens the electrical path, reducing loss and increasing bandwidth density, but at the cost of replaceability and with less mature standards."*

> **【判断】** 这张表实际上是一张**权衡曲线**，而不是分类表。它说明产业没有"更好的方案"，只有"在某个位置上的最优解"。CPO 之所以在 2026 年成为焦点，不是因为它在曲线上更靠右就更好，而是因为 **200G/lane 之后，曲线左端的 >22 dB 已经用完了预算**——铜的物理极限（1–1.5 m）把所有人都往右推，而右边的代价（不可替换、标准不全）还没有被工程化解决。这与 Hot Chips 2026 上"封装从单极走向多极"的判断是同一件事的两个侧面。

---

## 四、行动项

| # | 责任人 | 事项 | 时点 |
| --- | --- | --- | --- |
| 1 | Bobby | 取消原会议 series 的 extension，重建 Outlook 邀请并设置会前一天提醒 | 会后立即 |
| 2 | Bobby | 把子项目提案发到 reflector（邮件列表）征集意见 | 本周内 |
| 3 | Bobby | 把命名表文件放到 Google Drive，并把链接与说明发到邮件列表 | 本周内 |
| 4 | 全体 | 评审命名表并留言——**同意也请留言**，无异议后提交白皮书发布 | 待定 |
| 5 | Ron / Bobby | 按四步流程推进 SROI 毕业（团队确认 → FTI 领导层 → 附录 A 作为 WS1 基线 → 保留名称） | 持续 |
| 6 | 有意者 | 应征子项目 co-lead（2 名以上，优先 operator） | 待定 |
| 7 | — | 为命名表配套建一个网页/博客，方便社区访问 | 提议中 |

第 1 项是会上唯一有明确截止时间的动作。背景是：原会议邀请在 Global Summit 前到期，Bobby 做了 extension，但部分成员的 Google Calendar 收不到——有人需要手动导入 .ics，有人只收到 Gmail 通知。Bobby 的解决方案是"干脆重建"，而不是继续打补丁。

---

## 五、口径与转录更正

自动字幕在这场会里错得比较多，且错误集中在**最关键的数字与缩写**上。以下逐条校正，正文一律采用右列：

| 字幕/口播 | 实际（幻灯片/文档原文） | 性质 |
| --- | --- | --- |
| "MPO"、"MPO HTI"、"MPO-PCB" | **NPO**、**NPO-HDI**、**NPO-PCB** | 听音错误；NPO = Near Package Optics |
| "10 pJ/s" | **≤10 pJ/b** | 单位错误（每比特，非每秒） |
| "2 pJ" | **≤2 FIT** | 数量级错误（FIT 是失效率） |
| "3 Tbps/mm" | **1 Tbps/mm**（目标 2） | 数值错误 |
| "5 m" | **≤30 m** | 数值错误 |
| "five layers with overlap" | **"Five efforts, five layers, little overlap"** | 语义反转 |
| "cooling face plate" | **cold plate**（WS5 范围） | 术语错误 |
| "chaffis" | **shuffles**（光纤 shuffle） | 听音错误 |
| "XCPo"、"xCPO" | **xPO** | 缩写错误 |
| "optical phi" / "optical five" | **optical PHY** | 听音错误 |

**另有两条需要标注为"待澄清"，不属于字幕问题，而是材料本身的不一致：**

1. **WS5 的范围在两张幻灯片上不一致。** 第 4 页架构图把 WS5 标为 "Switch / XPU system integration"（面板光纤、shuffle、线缆路径、机架适配），激光源单列为 WS6 的框；而第 5 页工作流表把 WS5 定义为 "Lasers, fiber and system"（ELS 模块、面板光纤、shuffle、冷板）。同一份草稿里 WS5 有两种定义，说明编号仍在调整中。
2. **图 1 与表 1 的粒度不一致。** 图 1 列 6 种布置，表 1 只有 5 列——FPO 在图中拆成 Pluggable-PCB 与 Pluggable-NPC 两种，在表中合并为一列。这不是错误，但读者容易误以为图里有 6 个正式名称。

---

## 六、与本资料库其他材料的关系

这场会的内容，正好落在既有两份材料之间：

**与 `OCP2026会议资料/`** —— 这条线是 OCP 2026 全年议程里"Global Summit 之后"的部分。Global Summit（10/12–15）期间 SROI 的提案在早餐会上做了宣讲（Kevin 主讲），10/22 这场例会是把同一份材料带回工作流内部征求意见。也就是说，**本文记录的是 Global Summit 成果向正式项目转化的第一步**，而这一步的文档通常不会进入峰会资料包。

**与 `HotChips2026/06_深度分析报告/`** —— 三处直接对应：

1. **第 7 章（互连五层网络）**：报告把网络分成 Scale-Up / Scale-Out / Scale-In / Scale-Across / Context Scale 五层。SROI 定义的是 **Scale-Up 的物理层**，≤30 m 这个数字恰好落在"机架内到相邻机架"的区间，与报告里 NVLink 6（铜）与 UALoE（以太网）之间的空档位置吻合。
2. **第 9 章（能效经济学）**：报告引用了 d-Matrix 的能量阶梯（SRAM 50 fJ、片上走线 35 fJ/mm、2.5D HBM4 2.5+3 pJ/bit）。SROI 的 ≤10 pJ/b 是**一个链路端（SerDes + 光器件）的端到端口径**，不能与阶梯里的单层数字直接相减——两者分母不同。若要对比，应把 SerDes 的 pJ/b 单独拆出来。
3. **第 8 章（封装多极化）**：CPO-AP 与 optical interposer、CIO 的关系，正是报告里"封装边界从 die 扩展到 package"那条线在光互连上的体现。

---

## 附录 A：完整转录（英文原文，带时间戳）

> 自动字幕原文，仅去掉说话人切换标记 `>>` 并合并为段落；未做任何改写。数字错误见第五节。

```
[00:27] Hey Bobby. Hey um have you rece- have you received the Outlook meeting reservation? Or Outlook
meeting reservation? Yeah, or anything can pop up on the calendar. That's fine. I get a I get a Gmail
notice for this meeting or if that's what you're asking. I think that should -- It's just only the Gmail,
right? But you didn't receive any meeting uh or an- anything to block the meet- the time for for the
meeting on on the calendar?

[01:17] Not not in Outlook, but I mean all of my OCP correspondence is is Gmail. So it's it's a Google
Google calendar or Gmail. Calendar. Do do you have do do you have the meet- the the schedule? The um Well,
that's on our on our Groups.io page. There's a calendar there. I have that. Yeah, yes. And every every
week it's there on the Groups.io calendar. I can see it. Bobby, do you receive anything Are there Do Do
you of you receive meeting invite or something that can that can block your calendar? It doesn't
automatically block the calendar but I do get meeting notification. I need to pull the the the dot ICS
file and then open it then it will add to my calendar. If you do that that's exactly right. Yep. Okay. So
I just have I just have I just have my Outlook blocked but you know I

[02:43] cuz I found I found the meeting disappear from my calendar cuz I know that our regular meeting was
set up ended by

[02:59] the global summit and that was a previous meetings and I did the extension before. So the in the
the meeting aisle it it shows up but I'm wondering

[03:24] but I did it didn't appear on my Google calendar so that's why I was asking the questions.

[03:33] I want to make sure that everybody will be able to easily see the calendar.

[03:45] Everyone has to get on mute. You may just have questions for are you hearing my neighbor? Sorry.
[laughter] I know I can. No, but I'm I'm calendar challenge, so I depend on your email. I'll read out the
-- And it comes in it used to come in the day of right at the same time of the meeting, which is a little
bit challenging. But now it came in the day before, which I like a lot because I I know, you know. But my
calendar is stinks. I I haven't figured it out. Oh, I mean, it's not just this group, it's all my
meetings, so -- Oh, okay. Um all right. So so it seems like I should uh probably cancel the cancel my
extensions right now, just end that original meeting uh and then reset up another meeting, so it will send
out the um the Outlook invite and then um then that that everybody will be able to put that into the
calendar. Uh and I will be able to set up the reminder uh on the day before. So, I'll I'll do that after
the meeting.

[05:05] Um so -- Hey Bobby, for this for this meeting, I was hoping to maybe review some of the uh the
proposal for our group going forward. Oh, yeah. That is one of the important stuff that we should uh talk
about. And um and uh Ron, do you want to drive that things or -- don't why don't I why don't I go ahead.
So, let me let me share my screen. So, we had some [clears throat]

[05:45] we had a a good discussion um at the uh breakfast. If those of you were there, let me try to go.
Here we go, full screen. You You may have closed the door and not the button. There. Uh, at our at our
breakfast and so, uh, Kevin, uh, presented this and I just want to share it with the team. So, the the
good news is that our future technologies initiative workstream, uh, is now going to be graduating from
FTI to an official OCP, uh, work group. And, uh, some of these slides here are introduction. I don't need
to repeat this slide because it's all part of our white paper, uh, which you're all very familiar with.
Um, Right. And so, here's what they're thinking is five efforts, five layers with overlap. So, first off
is the short-reach optical interconnect, which we now have. I think with the, uh, publish of our white
paper and specifically the information that's listed in the spec- in the appendix can be easily, uh, used
to draft a specification. So, the

[07:16] the charter of our OCP work group going forward will then be to author an actual OCP, uh,
specification. Okay. And then, what they're showing here is some other overlap, where there's the OCI MSA
for the optical five. There's the CPX MSA defining module socket. And then, there's a chiplet group uh,
which they talked about uh much interest from Arista and others to to create an an actual standard uh or
specification I should say for defining an optical chiplet.

[08:06] Um okay and then this slide shows a little bit more about the how the hierarchy would work. I guess
there would be we would fall under the OCP networking project. So that would be our parent that is is
under networking. And then they would create a uh a subproject for optical connectivity. Okay and what
they're looking for is two plus co-leads. Uh it says here ideally operators. I think ideally they're
looking for hyperscalers. So someone to represent the the end customer. So um they want to be they want to
be fairly selective in who would lead the subproject. Okay and then uh they've listed the various five
different or sorry or six different workstreams that would fall under that subproject. So you can see
first the SROI. Uh so this this group uh we could logically continue our Thursday meetings. We could
logically continue uh the membership of this group and then just advance uh to the uh OCP workstream.
Then they have as you can see here, the

[09:38] switch um cooling face plate the pluggables

[09:47] optical engine optical phi laser source and test reliability management. So, we'd be looking for
comments on this proposal. I think uh OCP leadership is definitely interested in comments from this group.
So, I wanted to just socialize it a little bit here. Um I can you know post this and see if we have any
further comments. This uh describes a little bit more about the six work streams.

[10:29] Okay. Um And he has some several options for work stream two and work stream four. And then here's
more a slide specifically for us. So, we will quote graduate with targets already written. As I
mentioned, the appendix has uh clearly listed specifications. Um and then we would we would you know, move
this forward to create a a specification. And we could I actually keep They said we could keep our keep
the same name. So, um thoughts, questions comments anyone? Yeah. Uh and then on the next slide a little
bit.

[11:30] So, I'd like to chime in a little bit. Um this is still the proposal right now. Um, still pretty
wet at the moment. Um, James proposed that we are on under the uh the OCP network uh workgroup uh but our
SOI has covered, you know, all the things is not just covered on the under the network but um, so that
could be some change, uh in in between because for example, some of the things would uh like the the
workgroup that B John's leading, uh they're under the server part. Uh so uh so will that be part of the uh
uh workstream under SOI uh still not determined yet. Um, so this we're we're welcomes all the uh
feedbacks, ideas from the group.

[12:41] I hope and I didn't check with you, Bobby, but I'm okay to continue with the with the group. Uh
hope you are as well. Um, yeah, I'm I'm I'm pretty open to any uh any ideas in in here um as long as we
can bring everybody together cuz I I feel um we should keep we had a very good uh workshop this year and
we should keep the momentum um in uh in create the stickiness for everyone.

[13:26] Yeah, great job, by by way, coordinating all of those speakers. I think we had a we had a very good
workshop this year. I was able to uh sit back and enjoy. Um so thank you very much for organizing that.
And I think I also thank all of the speakers. I think they did a did a very good job um as well as the
panel. The panel was it was was very informative.

[14:03] Okay, I guess if there's there's no comments on that proposal, maybe what we can do is uh socialize
it a little bit more. Maybe I'll send out uh some information to the reflector. And uh we can take it from
there. Were there any other topics you had wanted to discuss today? Um so uh let me share a little bit in
here. Uh I have

[15:02] So this is the uh connectivity options, which is a naming table. Uh we decided to uh publish that
um so to make it available uh on the website. And so um not just us, but for the greater community,
they'll be able to referencing and uh and download. Uh so I put down together in here. Um, not much change
compared with last time. Um, the the table in here now has a higher quality uh,

[15:44] clips in here because the um, the Jeff was able to provide the Excel file uh, that he created for
the table to me. Uh, so I I I uh, uh, used updated version instead of the one that he put down into the
original PowerPoint file. Um, and I redid the illustration for different uh, options uh, and the naming
conventions. Um, so uh, and um, and reordered into the from the from the longest uh, signal loss distance
uh, all the way down to the shortest signal path uh, which is from the front pluggable uh, to the uh,
copper direct uh, connect pluggable all the way to the the PCB level uh, and the uh, the HDI levels um,
or to and in the standard XCPo uh, all the way to the advanced packaging CPO which is uh, potentially
including the interpole optical interposer or any other options. Um, and I also created the top view uh,
on the side cuz I I I think um, it would be more intuitive with a top view uh not just a side view but
also including the

[17:22] top view so it will be able to easily see where the uh the chip boundary is and uh where where the
cover is because when one of the key uh things that we discuss about is the MPO part right? There's many
uh for example the CPX open the CPX uh that you were able to you'll be able to uh socket uh removable
socket for the uh optical engine module uh no matter it's on the same uh substrate or not uh it should be
calling as an MPO uh because it it's not like covered it under the same package so uh so we we define that
as an MPO HTI uh it's clearly uh illustrated in here um and then when when it's fully covered by the uh
the same under the same lid then it becomes a a CPO uh so I put this files on the on the Google Drive and
I will send out uh the notes um but everyone please review it and if uh and comment it um if you find
anything one I like to update uh please comment it we will update that uh and after uh if everyone is a
success uh

[19:02] not success so everyone okay with it uh you can also leave a comment which okay and then we will um
submit this white paper and let it go out quickly.

[19:21] Hey thanks Bobby. Is that Is that on our Google Drive? Just checking. Uh yes, it's on the Google
Drive naming. So, I'll share the link uh with the email list.

[19:37] Um -- Yeah, very nice. I really like uh the figures that goes with the table. So, very well done.
Thank you, Daryl. Uh Jeff creates uh the the side view and I I create the top view. So, it's a
co-working. Um hopefully we'll besides this, we'll be able to create a a blog with a webpage for people
easily to access this one um cuz I I think we want to pushing the naming uh to for people can uh access it
easily.

[20:28] All right. Uh this is from my side. Um any other topics for today?

[20:39] Uh nothing nothing for here. Mhm.

[20:48] So, if uh but we don't have any other topic, I think we can conclude a meeting earlier today. All
right. Sounds good. Thanks, everyone. Thank you, everyone. Thanks. Thanks, Bobby. Thank you. Bye-bye.
Bye. Bye-bye.
```

## 附录 B：文件清单

```
yt_Tug9Ax_VtBM_FTI_SROI___Short_Reach_Optical_Interconnect_85206871737/
├── OCP_FTI-SROI_2026-10-22_会议纪要.md   本文件
├── OCP_FTI-SROI_2026-10-22_会议纪要.html 图文版
├── OCP_FTI-SROI_2026-10-22_Tug9Ax_VtBM.mp4  原片（1080p H.264 + AAC，38 MB，21:07）
├── Tug9Ax_VtBM.en.vtt                    英文字幕（原始）
├── transcript_plain.txt                  清洗后转录（带时间戳）
├── Tug9Ax_VtBM.info.json                 视频元数据
├── images/                               10 张图（幻灯片 7 + 文档 3）
├── slides/                               候选画面全分辨率帧
├── slides.json                           画面切换索引
└── scan/                                 扫描缩略帧（可删）
```

**说明**：视频保留在交付目录内，可直接回看核对。所有图片由原片按时间点精确抽帧，PPT 页已裁掉底部字幕带；文档页因屏幕共享缩放，已按原始像素放大 4 倍，文字可读但非矢量。
