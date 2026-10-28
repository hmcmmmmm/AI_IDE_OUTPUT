# STORY.md

## ① 意图对齐

**目标受众**：研发管理层（芯片 / 节点 / 机柜级系统）与质量、制造测试负责人。场合为会后技术复盘与决策评审，页面以「发给领导自己看」为主，需脱离讲解仍能读懂完整论证。

**核心目标**：让管理层接受三个判断——(1) L10–L12 是三份互不替代的证明，不是三级测试；(2) 覆盖率必须分层度量，单一百分比不可采信；(3) 「样机可运行即视为可量产」应作为否定式判据直接拒绝。并同意三项 30/60/90 天动作。

**PPT 长度**：16 页。Hero 页 4 页（封面 / 逃逸成本 / 液路时间轴 / 结束），占 25%。

**视觉调性**：深空克制 / 工程权威 / 数据密度高 / 金属质感 / 无装饰噪声。

**内容边界**：
- 必讲：L10/L11/L12 的证明边界与「不证明」清单；四层覆盖率与 WCI；线缆与液路两个物理面的验证缺口；样机→DVT→PVT→MP 的证据跃迁；MRS 评分卡与三项动作。
- 不讲：具体厂商性能数字、CPO/800VDC 等其他技术主线、OCP 议程排期细节。
- 禁碰：把任何厂商声明当作已验证事实；把示意性数值当作实测结论（所有推算须显式标注「分析模型」）。

---

## ② 页面布局骨架

**页面总数 16，分 4 章：**

| 章 | 标题 | 页码 | 章节扉页 |
| :- | :--- | :--- | :--- |
| — | 封面 / 目录 | P1–P2 | — |
| 01 | 起点：一行十九个字 | P3–P4 | P3 |
| 02 | 三级验收与覆盖率 | P5–P9 | P5 |
| 03 | 两个物理面：线缆与液路 | P10–P12 | P10 |
| 04 | 从误区到工具 | P13–P16 | P13 |

**目录↔章节扉页契约**：目录声明 4 章 → 全篇有且仅有 4 个 `type: section` 扉页（P3 / P5 / P10 / P13），编号 01–04 连续，标题与目录逐字一致。

**Hero 页定位**：P1（封面）、P7（逃逸成本，200× 锚点）、P12（液路 3–12 个月锚点）、P16（结束）。任意两个 Hero 之间至少间隔 3 个 Supporting 页。

**rhythm 曲线**：
P1 peak → P2 valley → P3 transition → P4 valley → P5 transition → P6 valley → P7 peak → P8 valley → P9 valley → P10 transition → P11 valley → P12 peak → P13 transition → P14 valley → P15 valley → P16 peak。
无连续 ≥3 页 valley（P8–P9 两页后接 transition）。

**非对称版式预算**：P1 / P2 / P4 / P6 / P7 / P8 / P11 / P12 / P14 / P15 = 10 页，占 62%（≥40%）。
**对称版式预算**：仅 P9（图表+洞察）与 P16（全屏视觉+大标题）2 页。
`左大图+右侧文字` 与 `非对称双栏` 合计 5 页（P4/P6/P11/P14/P15），占 31%（≤40%）。
`N卡片横排`：0 页（上限 2）。

---

## ③ 页面大纲

### P1 封面
- type: cover / role: hero / rhythm: peak / layout: 全幅图+骑线文字
- visual: L1 深空底纹 + 左侧竖金线（占全幅） / visual_role: atmosphere
- density: 字数约 45 / 图片 0 张 / 留白约 45%
- anti_pattern: 禁止居中排版；禁止在封面放目录式条目；禁止使用彩色渐变铺底
- description: 标题「可制造性」评估维度解析，副标 L10–L12 测试覆盖 · 线缆与液路验证，落款 2026 OCP Global Summit 技术分析。右侧留大片深空，用超大级数序号「L10–L12」做暗纹。

### P2 目录
- type: catalog / role: supporting / rhythm: valley / layout: 左标题+右内容
- visual: L3 细金线 / visual_role: atmosphere
- density: 字数约 150 / 图片 0 张 / 留白约 25%
- anti_pattern: 禁止四卡片横排；禁止每条只写两个字的章名
- description: 四章条目，每条带一句「这章回答什么问题」的副述，让目录本身承担导航判断。

### P3 章节扉页 01
- type: section / role: transition / rhythm: transition / layout: 全屏视觉+大标题
- visual: L1 巨型数字 01 / visual_role: anchor
- density: 字数约 40 / 图片 0 张 / 留白约 55%
- anti_pattern: 禁止四卡片预览；禁止铺满正文段落
- description: 章节大字「起点」+ 一句小标：这一行十九个字，是整份报告唯一把「做出来了」和「能重复做出来」切开的地方。

### P4 六维评估矩阵
- type: content / role: supporting / rhythm: valley / layout: 非对称双栏 62:38
- visual: 6×4 矩阵点阵（占左 62%） / visual_role: anchor
- density: 字数约 230 / 图 1 / 留白约 18%
- anti_pattern: 禁止等宽卡片横排；禁止把矩阵做成纯表格文字
- description: 性能/功耗/可靠性/可制造性/可维护性/生态成熟度 × 概念设计/样机DVT/制造PVT·MP/部署运营。可制造性一行高亮：它是唯一横跨样机与量产、且在两端证据最弱的维度 → 所以在评审中最容易被「样机跑通了」顶替。

### P5 章节扉页 02
- type: section / role: transition / rhythm: transition / layout: 全屏视觉+大标题
- visual: L1 巨型数字 02 / visual_role: anchor
- density: 字数约 40 / 图片 0 张 / 留白约 55%
- anti_pattern: 禁止四卡片预览；禁止铺满正文段落
- description: 章节大字「三级验收」+ 小标：L10 证明托盘，L11 证明机柜，L12 证明集群——三者不是更严格，而是回答不同问题。

### P6 三级验收的证明边界
- type: content / role: supporting / rhythm: valley / layout: 左大图+右侧文字 65:35
- visual: 三栏证明卡（L10/L11/L12，占左 65%） / visual_role: anchor
- density: 字数约 320 / 图 1 / 留白约 15%
- anti_pattern: 禁止把「不证明」写成小字脚注；禁止三栏等高无差异
- description: 每栏含「证明 / 测试域 / 输出物 / 不证明」。L10 不证明卡匣就位与 72 卡 NVLink 域；L11 不证明跨柜传输与 JCT；L12 不证明长期可用性 → 任何一级缺失都会形成无法补偿的证据空洞。

### P7 缺陷越晚发现越贵
- type: content / role: hero / rhythm: peak / layout: 巨型数字+洞察
- visual: 200× 巨型锚点数字 + 五级成本阶梯 / visual_role: anchor
- density: 字数约 180 / 图 1 / 留白约 30%
- anti_pattern: 禁止等宽卡片横排；禁止把 200× 塞进图表角落；禁止不标注「分析模型」
- description: L10=1× → L11=4× → L12=15× → 现场=60× → 运行期=200×。结论：L11 是线缆与液路缺陷的最后一道低成本拦截点，而这两类缺陷恰好「样机阶段不暴露」。

### P8 覆盖率必须分四层
- type: content / role: supporting / rhythm: valley / layout: 左标题+右内容 30:70
- visual: 四层结构条 + WCI 公式 / visual_role: anchor
- density: 字数约 300 / 图 1 / 留白约 15%
- anti_pattern: 禁止只给一个百分比；禁止四层等权重
- description: 需求 20% / 拓扑 25% / 工况 25% / 故障模式 30%。每层写清「分母是什么、这个数字如何骗人」→ 单一百分比掩盖结构性缺口，红线机制防止平均分掩盖缺失。

### P9 覆盖率的经济学
- type: content / role: supporting / rhythm: valley / layout: 图表+洞察
- visual: Chart(折线：逃逸成本 vs 验证成本) + 洞察框 / visual_role: evidence
- density: 字数约 160 / 图 1 / 留白约 20%
- anti_pattern: 禁止把交叉点标成「最优解」却不说明这是示意模型；禁止双轴堆叠
- description: 逃逸成本随覆盖上升快速下降，验证成本越靠后越陡，交叉点约在 81%（示意）。判断：不必追 100%，但量产爬坡期曲线右移，应主动抬高覆盖目标。

### P10 章节扉页 03
- type: section / role: transition / rhythm: transition / layout: 全屏视觉+大标题
- visual: L1 巨型数字 03 / visual_role: anchor
- density: 字数约 40 / 图片 0 张 / 留白约 55%
- anti_pattern: 禁止四卡片预览；禁止铺满正文段落
- description: 章节大字「两个物理面」+ 小标：原文把线缆与液路单独点名，因为它们是样机阶段最不暴露、量产阶段最高频的两类失效。

### P11 线缆：失效模式 × 检测手段
- type: content / role: supporting / rhythm: valley / layout: 非对称双栏 70:30
- visual: 7×6 矩阵点阵（占左 70%） / visual_role: anchor
- density: 字数约 240 / 图 1 / 留白约 12%
- anti_pattern: 禁止用表格代替矩阵；禁止只写「已做 TDR」不给覆盖关系
- description: 前两列（来料 IQC、组件 TDR）对「未就位」与「错插漏插」几乎无效，而这两类正是 L11 最高频逃逸源 → 装配态必须靠互锁信号 + 误码计数 + NCCL 交叉验证。

### P12 液路：时间延迟暴露
- type: content / role: hero / rhythm: peak / layout: 上大图+下方卡片
- visual: 六阶段风险柱 + 3–12 个月巨型锚点 / visual_role: anchor
- density: 字数约 200 / 图 1 / 留白约 28%
- anti_pattern: 禁止六张等宽卡片横排；禁止把「当前没漏」当结论
- description: 风险峰值在运输、灌注、长期运行三段，而「样机可运行」的取样窗口只覆盖出厂保压一段 → 用样机状态推断液路可量产性，取样点根本不在风险区。

### P13 章节扉页 04
- type: section / role: transition / rhythm: transition / layout: 全屏视觉+大标题
- visual: L1 巨型数字 04 / visual_role: anchor
- density: 字数约 40 / 图片 0 张 / 留白约 55%
- anti_pattern: 禁止四卡片预览；禁止铺满正文段落
- description: 章节大字「拆掉那个逻辑」+ 小标：样机证明存在性，量产要求分布性——中间隔着 DVT 与 PVT 两道完整台阶。

### P14 证据阶梯
- type: content / role: supporting / rhythm: valley / layout: 左大图+右侧文字 60:40
- visual: 四级阶梯 + ORW 时间线 / visual_role: anchor
- density: 字数约 280 / 图 1 / 留白约 18%
- anti_pattern: 禁止把样机与 DVT 画成同一级；禁止不给出时间尺度
- description: 样机（n=1）/ DVT（设计达标）/ PVT（产线稳定）/ MP（分布可控）。ORW 实例：2025.10 规范初稿 → 2026.11 量产爬坡，约 13 个月 → 这段时间不是在改设计，是在做公差、工装与产能。

### P15 量产就绪度评分卡
- type: content / role: supporting / rhythm: valley / layout: 非对称双栏 55:45
- visual: 8 维打分条 + 总分仪表 / visual_role: anchor
- density: 字数约 240 / 图 1 / 留白约 15%
- anti_pattern: 禁止只给总分不给红线；禁止把示例分数当实测
- description: 测试覆盖 20% / 线缆 15% / 液路 15% / 工装 10% / 良率 15% / 二供 10% / 可服务 10% / 变更 5%。红线：测试覆盖与液路低于 50 分一票否决 → 防止平均分掩盖结构性缺失。

### P16 三项立即动作
- type: ending / role: hero / rhythm: peak / layout: 全屏视觉+大标题
- visual: 巨型数字 30/60/90 / visual_role: anchor
- density: 字数约 150 / 图 0 张 / 留白约 40%
- anti_pattern: 禁止四条以上动作；禁止写成口号不写交付物
- description: 30 天拆覆盖率、60 天线缆与液路专项 DVP、90 天把「样机可运行」移出证据清单。收束句：把判断依据从「谁说得更有信心」换成「谁能拿出可复现的数据」。
