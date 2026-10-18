# AI 工厂的规模化

**Ian Buck（NVIDIA 超大规模与 HPC 计算副总裁）OCP Global Summit 2026 演讲 · 图文实录**

---

## 关于这份文档

这是一份**逐段实录**，不是要点综述。每一节遵循同一结构：

- **图片**：演讲当时投影的幻灯片，按时间顺序
- **中文译文**：Ian Buck 在这一页停留期间所说的话，逐句翻译，不作删减
- **英文原句**：同段话的英文原文，供核对与引用
- **小结**：整理者对这一段的一句话归纳，与讲话内容明确区分

原文由 YouTube 自动字幕转写，已去除 um、uh 等口头填充词，并修正明显的转写错误（如 Rubin、RoCE、KV cache、Feynman、DSX、MaxLPS、NVL72 等专有名词）。凡口播数字与幻灯片标注不一致处，正文采用幻灯片值，并在当节注明差异；仅存在于口播、幻灯片上无对应的数字，标注为「口头表述」。

中文译文以"准确传达原意"为优先，而非追求文采。

---

## 视频信息

| 项目 | 内容 |
|---|---|
| 标题 | AI Factories at Scale: Advancing Open Infrastructure for Agentic AI |
| 演讲人 | Ian Buck，NVIDIA 超大规模与 HPC 计算副总裁 |
| 场合 | OCP Global Summit 2026 · 主会场演讲（当日收尾场） |
| 时间地点 | 2026 年 10 月 13 日，加州圣何塞（幻灯片页脚：October 12–15, 2026） |
| 时长 | 24 分 09 秒 |
| 频道 | Open Compute Project（YouTube） |
| 链接 | https://www.youtube.com/watch?v=UR7kJy7X_nQ |

---

# 第一部分　开场：一套用了十三年的基础设施

## 01　开场：为什么要在 OCP 讲硬件

![OCP Global Summit 2026 主题页：Scaling Innovation for the AI Era，October 12-15, 2026，San Jose](images/01_00m03s.jpg)

谢谢。今天由我来收尾，所以我不会占用大家太多晚餐时间。当然，这里是 OCP，所以我正好可以借这个机会，好好聊一聊硬件，聊一聊我们在 NVIDIA 做的这些事，以及我们回馈给 OCP 的东西。

我们的贡献史可以一路追溯到 2013 年——最早是 Mellanox 时代；然后是 GPU 还只是 PCIe 插卡的时候；再到我们第一块 GPU 主板 HGX；一直到 Blackwell，也就是我去年讲过的部分。

今年我会讲一点 Rubin。但从 2015 年那批最早的 GPU，到 2013 年的网络，再到现在——这中间我们建起来的东西，跨度非常大。

> Thank you. Well, I wrap up today, so I won't keep you too long from dinner, but of course, this is OCP. So, I'm here to have a chance to really geek out on the hardware and all the things that we've been doing at NVIDIA and contributing back to OCP. Our history of contributions dates all the way back to 2013, the original Mellanox days into today the GPUs when they were still PCIe cards to our first GPU motherboards with HGX all the way up to Blackwell, what I talked about last year. This year, I'm going to talk a little bit about Rubin, but the span of what we built all the way back to those contributions from those first GPUs in 2015, the networking in 2013 to today

<div class="takeaway"><b>小结</b>　他先给这场演讲定了坐标：不是发布一款产品，而是交代十三年积累下来的同一条技术脉络。</div>

## 02　它像桥梁、像电缆一样持久

![History of OCP Contributions：2013 SwitchX-2 起，经 ConnectX-3、Tesla M40、P100、V100 OAM、A100、HGX-H100、ConnectX-7、MGX 1.0 Blackwell 机架，到 2025 MGX 1.1 Blackwell Ultra](images/02_01m00s.jpg)

我们已经建成了一整套开放计算的生态与基础设施，全世界都在从中受益。

而且它确实是"基础设施"——它是长期存在的、持久的，就像桥梁、像电缆、像管道。这是向全世界开放可用的算力。

> has built an entire ecosystem and infrastructure of open computing that the world is benefiting on. And it's infrastructure and in that it's infrastructure. It is existing, it's lasting like bridges, like cables, like pipes. This is computing that is available to the world

<div class="takeaway"><b>小结</b>　他用桥梁、电缆、管道作比，回答的是一个采购问题——这套东西能用多久；而屏幕上那张十二年不断代的时间线，就是答案本身。</div>

## 03　基础设施的三个属性：持久、多用途、越来越便宜

![NVIDIA AI Factories Are Productive, Durable, and Fungible：10M 开发者、CSP/NCP/OEM/ODM 与 300+ 供应链伙伴；预训练、后训练、推理、智能体、加速计算五类负载；V100/DGX-1 已服役 10 年、A100 已 6 年、NVL72 才 1 年](images/03_01m39s.jpg)

在 AI 之前就是如此，今天更是如此。我们现在有超过 1000 万名开发者在加速计算基础设施上开发。每一家 CSP、每一家 NCP、每一家 OEM、每一家 ODM——当然，你们今天都在场。仅供应链上就有超过 300 家主要公司在用 OCP 的东西做产品、做部件、做零件，共同把这个生态建起来。我当然要感谢你们所有人，感谢这个丰富的生态，感谢你们对所有开发者的支持。

这使这套基础设施既持久，又"多用途"（fungible）。它能做预训练，能做后训练，能做推理，能做智能体负载，当然也能做加速计算。这些基础设施——每一个模型、每一种负载，不管是闭源的还是前沿的——都是建立在 OCP 之上、建立在十余年的开放贡献之上的。

而且每一次发布，我们都让它更快。我最近和一位客户聊过。他们在 2019 年买了一批 Volta，当时出租价格大约是每小时两毛五。今天，他们能以每小时大约一美元的价格租出去。这就是基础设施：它越来越快、越来越便宜，而且几乎可以永久使用下去，能赚钱，也能支撑我们共同在做的事情不断增长。

当然，最新一代是 Vera Rubin。每一代我们坐下来时，想的不只是怎么让它更快、更强——为智能体、为用户、为 AI 模型、为仿真提供更高性能——同时还要更便宜。Vera Rubin 通过端到端的方式，做分离式服务（disaggregated serving），研究速率……

> even before AI and AI today. We now have over 10 million developers developing on accelerated computing infrastructure. And every CSP, NCP, every OEM, every ODM, they're of course you're all here. There's over 300 major companies in the supply chain alone building products, components, pieces from OCP in building this ecosystem. I certainly have to thank all of you for that rich ecosystem and the support for all those developers. That makes that infrastructure and lasting fungible. It can do pre-training, it can do post-training, it can do inference, it can do agentic workloads, and of course, it can do accelerated computing. These that infrastructure, that that every model, every workload, whether it be closed or frontier, is available built on OCP for well over a decade worth of open contributions. And with every release, we make it faster. I talked to one customer recently. They they bought some Voltas back in 2019. They they rented them out for about a quarter an hour. Today, they're now renting them out for about a dollar an hour. That's infrastructure. That makes it gets faster, affordable, it lasts for uh literally almost forever now, and makes um help build money and help builds the growth of what we're all doing together. The latest generation, of course, Vera Rubin it is with every generation, we sit down and we're trying to figure out not just how to make something faster, more capable uh with more performance for the the agent or the user or the AI model or the simulation, but also more affordable. Vera Rubin, by going end-to-end, working on disaggregated serving, studying rate

<div class="takeaway"><b>小结</b>　"每小时两毛五涨到一美元"是全场最有力的一句论证：旧硬件不但没贬值，反而涨价——这正是"开放基础设施"与"专用设备"的分野。</div>

---

# 第二部分　Vera Rubin 与第三代 MGX

## 04　全栈协同设计：30 倍吞吐与 45 倍成本下降

![Full-Stack Co-Design Delivers up to 30x Better AI Factory Throughput on Agentic Workloads：DeepSeek-V4-Pro / SemiAnalysis AgentX；左图每兆瓦 token 吞吐 2x/10x/30x，右图每百万 token 成本低 45x](images/04_02m57s.jpg)

……匹配（rate matching）、所有软件、集成最新的 KV cache 实现，并把那个 MGX 机架搭起来——它现在就是 OCP 的——你能得到 2 倍、10 倍，极端情况下 30 倍于用户实际体验的 token 性能。

而在右边，我们同时还在降低这些 token 的成本。因为机架里可用的算力多得多，我们能服务更多请求，实际上把 token 成本降低了 45 倍。

这是在真实基准上测出来的，具体说是 SemiAnalysis 做的 AgentX 基准。所以，我们此刻在 OCP。Vera Rubin 已经全面量产，你们大概已经看到了。它正在进入全世界的数据中心、全世界每一家 CSP，我们已经从客户那里看到一些非常惊人的结果，到处都在部署。而 NVIDIA，就像去年对 Blackwell 做的那样，我们正在贡献……

> matching, all the software, all integrating all the latest KV cache implementations, and building up that MGX rack, which now is OCP, you get 2x, 10x, at the extreme 30x more token performance experienced by the user. But on the right-hand side, we're actually redu- at same time reducing the cost of those tokens. Because there's that much more computing available in the rack, we can serve more and actually reduce the cost of those tokens by 45x. This is measured on actual benchmarks, in this case the AgentX benchmark done by SemiAnalysis. So, we're here at OCP. Vera Rubin is in full production, as you've probably seen. It's it's showing up in all of the world's data centers, at all the world's CSPs, and we're already seeing some amazing results from it from our customers, being deployed everywhere. And NVIDIA, just like we did with Blackwell last year, we are contributing

<div class="takeaway"><b>小结</b>　两张图必须一起看：吞吐提升 30 倍与成本下降 45 倍不是同一个数字的两种说法，而是"每兆瓦吞吐"和"每百万 token 成本"两个不同坐标上的结果。</div>

## 05　第三代 MGX：把工厂级液冷架构交给 OCP

![NVIDIA Contributes Third-Gen MGX Specification to OCP：MGX 1.2 的十项规格——无线缆无软管计算托盘、5,000 A 液冷母排、托盘内 MQD/MQDB、铜脊、盲插歧管、锁扣顶杆、浮动盲插、盲插滑轨、更大机架走线槽、机架加强件、后部延长件、计算托盘底座系统、交换机托盘形态、DC-SCM、UQD08 流量规格](images/05_04m03s.jpg)

……我们的第三代 MGX 机架架构，也就是 Rubin 所基于的、基于 OCP 的那一套。这是我们的 MGX 1.2：工厂级规模、高密度、液冷架构。

从计算托盘本身的设计，到液冷母排（bus bar），到托盘内的 MQD、MQDB 快速接头——我在水流、以及怎么让这些东西顺畅运行上学到了非常多。还有盲插歧管（blind mate manifold）、机架后部延长件、整个底座系统；以及把流量规格标准化，帮全世界在流量规格上达成一致，这样我们做的部件、零件、组件不仅能和 NVIDIA 的产品兼容，OCP 的每一个成员都能受益，我们也能一起为今天的数据中心和下一代数据中心做设计。

这是我们对 OCP 的承诺，也是对你们所有人的承诺：继续让 MGX 保持 OCP 兼容，并且每一代、每一年都贡献出来。

今年不只是这些组件，我们还把重点放在了可制造性上。左边是计算托盘，GB200 NVL72。你可以看到走向 Vera Rubin 时的变化——我们把所有线缆都去掉了。

> our third generation MGX rack architecture, which is what with Rubin's based on OCP. This is our MGX 1.2 factory scale high-density liquid-cooled architecture. And everything from the design of the compute tray itself to the liquid-cooled bus bar the way to the in-tray MQDs and MQDBs quick disconnects. I have learned enormous things about water flow and how to make things run run smoothly. Um the blind mate manifold, the rear rack extenders, the the whole base system, and also standardizing helping the world standardize on flow rates so we can all be building components and pieces and parts that are compatible not just with NVIDIA's product but every member of OCP can get the benefit and we can all be designing for today's data centers and for the next generation. This is our commitment to OCP and and commitment to all of you to continue to make MGX OCP compatible and contribute it every year with every generation. And this year not just all those components, but we also focused on manufacturability. On the left is the compute tray, the GB200 and NVL72. And you can see going to Vera Rubin the changes. We eliminated every cable.

<div class="takeaway"><b>小结</b>　这一页真正的贡献不是硬件，而是"流量规格"——把水的流速写进公开规范，零组件才可能在 NVIDIA 之外被独立制造。</div>

## 06　从 90 分钟到 1 分钟

![Third-Gen MGX Improves Manufacturability and Maintenance：GB200 NVL72（第一代 OCP MGX 1.0）与 Vera Rubin NVL72（第三代 OCP MGX 1.2）的计算托盘、交换机托盘对比，副标题"90 minutes to 1 minute build time: no cables, fans, or hoses"](images/06_05m09s.jpg)

用 Grace Blackwell 的时候，做那个计算托盘要花 90 分钟。我们学到了很多，也做了优化。很大一部分工作在于液冷和快插接头，以及怎么让所有环节都可靠、稳定、完全自动化。

今天，无论是在美国，还是在台湾、亚洲以及世界各地，工厂都在制造 Vera Rubin 的托盘。组装和制造那个计算托盘只需要 1 分钟。而我们现在每周生产数千个机架。

这项贡献当然对 OCP 很有价值——我们把所有的经验都分享给在座各位，这样我们能继续走这条路、继续扩大规模。

另外，我们也在为未来做规划。这是第一座 800 伏直流（800 VDC）AI 工厂……

> It actually took 90 minutes to make that compute tray with Grace Blackwell. We learned a lot. We optimized. A lot of it was liquid cooling and QD connectors and how to make everything reliably and stable and fully automated. Factories today both here in the US and of course in Taiwan and Asia and around the world are now manufacturing the Vera Rubin tray. It takes 1 minute to assemble and manufacture that compute tray. And we're literally producing thousands of racks a week at this point. This contribution of course is great for OCP. All of we're sharing all of our learnings with the rest of you so that we can continue on this journey and scale up. In addition, we're planning for the future. This is the first 800-V DC AI factory

<div class="takeaway"><b>小结</b>　90 分钟到 1 分钟，是从"能装出来"到"能按周产数千台"的门槛线；他把这条经验也一并交出去了，等于把竞争对手的爬坡时间也压缩了。</div>

---

# 第三部分　供电：800 伏直流

## 07　首座 800 VDC AI 工厂

![First 800 VDC AI Factory Engineered for the Next Decade of Accelerated Computing：Visionbay.ai 的 16 MW 部署单元，四个供电单元 SU 1–SU 4，上游交流基础设施、冗余列末电源中心集中变换、800 VDC 125 A 机架级分接、800 VDC 母排把电力架空分配到 4 MW 可扩展单元](images/07_06m18s.jpg)

……它现在正在被设计和建造，为下一个十年的加速计算而工程化。

它实际上是由 Visionbay.ai 建造的，采用了目前正在制定中的 OCP 800 VDC 标准，并在这座数据中心里实现了它的第一个版本。

800 伏的好处当然是：我们做的变换和升压级数更少。这意味着可能出故障的部件更少，同时我们也提高了那座数据中心的效率。更不用说铜的用量——少得多。相比其他方案，800 伏需要的铜要少 45%（口头表述）。而且它还是可扩展的：它能支持我们今天 100 kW 的机架，但通过把 800 伏电力直接送到数据中心、送到每一排，实际上可以一路扩展到 1 MW 的机架。

我们对此非常兴奋。我们实际上是在和合作伙伴一起贡献这件事。我们官网上有一篇博客，用来验证和证实一套 800 VDC 的基础设施系统——它会帮助今天的数据中心用 Rubin 和 Ultra 扩展，一直走到 Feynman 及以后，既为我们的产品，也为整个生态。

好，现在人人都在谈 CPU。当然，NVIDIA 也一直……

> that's being designed and built now, engineered for the next decade of accelerated computing. It's actually being built by Visionbay.ai, and it is actually taking the OCP 800-V DC standard that's being developed now and implementing the the first version of it in this data center. The benefit of 800-V of course is we're doing fewer transitions and stepping. That means less components that could potentially fail, and we're increasing the efficiency of that data center. Not to mention, we're using copper, a lot less copper. 45% less copper is required with 800-V than alternatives. And it's also scalable. This can support the 100-kW racks that we have today, but can actually scale all the way up to 1-MW racks by delivering 800-V power direct to the data center and across all those rows. We're super excited about this. We've actually contributing this along with our partners. We have a blog on our website, and to prove out and to validate an 800-V DC infrastructure system that's going to help scale data centers today with Rubin and Ultra out to Feynman and beyond for both our products and both for the entire ecosystem. Okay, well, everyone's talking about CPUs. Of course, Nvidia also has been

<div class="takeaway"><b>小结</b>　800 VDC 的收益被拆成三件可量化的事：少一级变换、少 45% 铜、从 100 kW 一路撑到 1 MW——这是为"机架功率还会再涨十倍"提前买好的保险。</div>

---

# 第四部分　CPU：为智能体重做一颗核

## 08　为智能体而生的 Vera CPU

![NVIDIA Vera CPU for Agents：单线程性能 × 吞吐的四象限中，"Max Single-Threaded CPU at Scale"是此前空白的象限；2x 性能（Olympus 核）、3.4 TB/s 核间带宽（零 chiplet 税、可扩展一致性 fabric）、每核 1.2 TB/s 内存带宽（LPDDR5X）](images/08_07m42s.jpg)

……做 CPU 已经有一段时间了。我们做了 Grace，并把它和 Blackwell、Hopper 系统配对，如果大家还记得的话。到了 Rubin，我们做了一颗新的 CPU——Vera CPU。我们把它用在 Vera Rubin GPU 上。但我们也和这里所有人一样，看到了为智能体计算（agentic computing）打造一种新型 CPU 的机会。

在前云时代——也就是 PC 和游戏领域——我们有很快的 CPU。它们跑在 GHz 级别的频率上，可能只有几个核，8 个、10 个、12 个或 16 个，但它们很快，在客户端负载上有着极好的单线程性能。但它们不具备云的规模。

到了云时代，所有人都在按"每核多少钱"采购、都在为成本做优化，机会就变成了：堆很多吞吐、很多核，但不一定需要最高的频率。

Vera 其实是一种不同类型的 CPU。它的设计目标是——我们在意单线程性能。如果你在跑 GPU、在跑一座 AI 工厂，规模是吉瓦级、造价几十亿美元，你绝不想让任何 CPU 执行成为等待。你要让那些 GPU 一直忙。但你也需要吞吐。我们有那么多任务、有那么多不同的操作必须发生，才能让那些 GPU 保持忙碌。所以我们既需要快的单线程性能，又需要所有核一直跑着。而这正是 Vera 被设计来做的事。

当然，它被设计成我们 GPU 的好搭档，但它同样也是做所有智能体工具调用（tool calling）的好搭档。相比对位的 Grace，它的单核性能实际是两倍。它是 NVIDIA 自研的核设计。它有 3.4 TB/s 的核间带宽。我们的核数可能不如那些按"每核多少钱"卖的云 CPU 多，但我们把资源花在了所有核彼此之间、以及核与内存之间的通信上。这里没有妥协，没有 chiplet 税（chiplet tax），是完全的、可扩展的一致性 fabric。所以当每个核都想做数据库操作时，它不会撞上内存墙，不会撞上传输瓶颈，它可以充分访问自己需要的所有资源。

因此，我们还把它和 LPDDR 内存结合起来。这是原本为手机设计的内存，我们把它加固到了数据中心级别。我们在 Grace CPU 上做了这个创新，而且我们已经在嵌入式领域用了相当一段时间。加 ECC、和内存厂商合作、为低功耗、高带宽、低延迟的 LPDDR 内存制定新标准。这颗 CPU 实际有每核 1.2 TB/s 的内存带宽，它所有的工作都通过那套 fabric 完成。你在结果和基准里能看到这一点。我们跑了 Meta 的 DC……

> building CPUs for quite some time. We built Grace and paired it with our Blackwell and Hopper systems, if you remember. And with Rubin, we built a new CPU, the Vera CPU. We've used it with our Vera Rubin GPUs. But we also, like everyone else here, see the opportunity for building a new kind of CPU for agentic computing. In the pre-cloud space, this is in PCs and in gaming, we had fast CPUs. They were clocked at gigahertz of performance. Maybe only had a few cores, eight or 10 or 12 or 16, but they were fast, and they got excellent single-threaded performance for doing client-based workloads, but they weren't at the cloud scale. Come the cloud where everyone's buying dollar per core and optimizing for cost, the opportunity was to build lots of throughput, lots of cores, but not necessarily have the highest of clocks. Vera is actually a different kind of CPU. It was designed to take — we care about single-threaded performance. If you're running a GPU, running an AI factory, you for gigawatts, costing billions of dollars, you do not want to wait on any CPU execution. You want to keep those GPUs busy. But you also need throughput. We have all those tasks, we have lots of different operations that have to happen to keep those GPUs busy. So we need both fast single-threaded performance, but with all the cores running all the time. And that's actually what Vera was designed to do. It was designed, of course, to be a great partner for our GPUs, but it's also a great partner for doing all the agent tool calling. It actually is double the per core performance compared to comparative Grace. It's an NVIDIA core design. It is 3.4 terabytes a second of core-to-core bandwidth. We may not have as many cores as the cloud dollar per core CPUs, but what we did spend it on is the communication of all those cores to each other and to the memory. There's no compromises, no chiplet tax, fully scalable coherent fabric. So if every core wants to do database operations, it's not going to hit a memory wall, it's not going to hit a transition, and it can fully access all the resources it needs. As a result, we also combine it with LPDDR memory. This is memory that was designed for cell phones that we've hardened for the data center. We innovated this with our Grace CPUs, and we've been using it in an embedded space for quite some time. Adding ECC, working with the memory vendors, working on new standards for low energy, high bandwidth, low latency LPDDR memory. This CPU actually has 1.2 terabytes a second per core and it get all of its work done that comes through that fabric. You see that in the results and benchmarks. We ran Meta's DC

<div class="takeaway"><b>小结</b>　四象限图里那个空格是关键论点：单线程强与规模吞吐此前互斥，Vera 声称能同时占据——理由不是核更多，而是把预算全花在 fabric 上。</div>

## 09　Vera 的 2 倍：从 Meta DCPERF 到 Redpanda

![NVIDIA Vera Delivers 2x Performance for Agentic AI：2x Hyperscale Cloud（Meta DCPERF）、2x HPC Golden Suite（TACC）、3.5x Apache Kafka（Redpanda）；单项基准 1.3x–2.2x](images/09_10m12s.jpg)

……perf 基准，这是一个开源基准，在 GitHub 上。它代表了他们数据中心节点的典型负载。结果是 Vera 相比 Grace 有 2 倍的性能提升。而且 Meta 最近刚刚宣布，他们会在明年初建起第一个 Vera 集群——就像他们当初对 Grace 做的那样。

在仿真、HPC，以及为行业用例跑智能体代码方面，HPC Golden Suite 上是 2 倍——这个套件在超算和 HPC 社区里已经被测量了很长时间。甚至对于 Apache Kafka、以及用 Redpanda 的数据库这类操作，是 3.5 倍。

这些你们都可以去读，但它现在已经出货了。我们实际上已经在向客户交付，并真正在云里把它们搭起来。而我们今天在 OCP 还要宣布的是，新的 NVIDIA Vera CPU……

> perf benchmark, which is an open source benchmark. It's on GitHub. It was representative of their data center nodes. Saw 2x better performance with Vera compared to Grace and actually Meta just recently announced that they'll be building their first Vera cluster, like they did with Grace, early next year. On simulation and HPC and running agentic codes for industry use cases, 2x on the HPC golden suite that's been measured in supercomputing and HPC community for some time. And even for operations like Apache Kafka, databases with Redpanda, 3.5x. You can read about all this, but it's shipping now. We have actually been delivering them to our customers and actually building them out inside the clouds. And what we're also announcing here at OCP is that the new Nvidia Vera CPU

<div class="takeaway"><b>小结</b>　三个数字分别对应三类买家：超大规模云（Meta DCPERF）、超算中心（HPC Golden Suite）、企业中间件（Kafka/Redpanda）——这是在用同一颗芯片同时说服三种采购逻辑。</div>

## 10　Vera CPU MGX 机架：256 颗 CPU，已出货

![Announcing NVIDIA Vera CPU MGX Rack Now Available：单机架 256 颗 1U CPU、全液冷、无线缆模块化；早期采用者 Anthropic、ClickHouse、DeepInfra、OpenAI、Perplexity、SpaceX；超算中心 Los Alamos、NERSC、TACC；云 CoreWeave、Crusoe、Firmus、Nebius、Nscale、Oracle、Lambda、Together AI；以及 Bull、Dell、HPE、Lenovo、Supermicro 等二十余家生态伙伴](images/10_11m06s.jpg)

……MGX 机架现在已可用、已在出货。这是 OCP 兼容的设计。

我们的合作伙伴——它沿用了我们讲 Vera Rubin 时提到的同一套生态，只不过这里是 Vera CPU。这个机架里实际有 256 颗 CPU（口头表述），全部液冷、全部 1U、配置密度极高。

它支持所有智能体工具调用，也支持所有可以用我们 BlueField 前端网卡实现的 AI 安全能力——用来保护这些智能体，确保它们待在自己的沙箱里，不做运营商不希望它们做的事。

早期采用者你们可以在这里看到，但真正让我兴奋的是生态伙伴——这里的每一家都在造这个机架，而它现在已经在出货了。

再强调一次：它无线缆、模块化、液冷，而且因为它是 OCP，所以它是开放的。它完全可定制。你可以在里面放 GPU 托盘，也可以只放 CPU；我们可以做 2U，可以改变密度，包括两者都提供；你可以配各种 CPU 加标准 PCIe 加速器，随意混搭；或者就用标准 2U 风冷。所有这些现在都可获得、都在出货。

> MGX rack is now available and shipping. This is OCP compatible design. Our partner, the same leverages all of the same ecosystems that we talked about with Vera Rubin as Vera CPU. This rack actually has 256 CPUs in it, all liquid cooled, all 1U, highly dense configuration. It supports all of the agentic tool calling and all of the AI safety that can be implemented with our BlueField front end NICs to secure those agents and make sure they stay within their sandbox and don't do anything that operators don't want them to do. The early adopters you can see here, but the ecosystem partners — what I'm really excited about is everybody here building this rack and it's now shipping. Again, it's cableless, it's modular, it's liquid cooled and it's because it's OCP, it's open. It's fully customizable. You can take and design it with a GPU tray in there, a CPU only, we can do a 2U, vary the density including offer both, standard PCIe accelerators with various CPUs and mix and match, or just go with standard 2U air cooled. All of this is available and shipping now.

<div class="takeaway"><b>小结</b>　Vera 单独成架、可纯 CPU、可混插 PCIe——这说明 NVIDIA 卖的不再只是 GPU 的附属 CPU，而是要让 Vera 单独进入通用服务器市场。</div>

---

# 第五部分　把整座工厂写成规范

## 11　DSX：把整座 AI 工厂写成开放规范

![NVIDIA DSX Advances OCP-Compatible AI Factories：新的 DSX 兼容规范贡献（开放数据中心与电网韧性）、MaxLPS 同样电力下多 40% GPU（把搁浅电力变成 GPU 容量）、新的 DSX AI 工厂开放软件（Rack Management Service、Cluster Readiness Engine、Config Manager）](images/11_12m54s.jpg)

最后，OCP 不只是关于铁皮和硬件——我们所有人都在建数据中心。你们已经听了 Santosh 和其他人的精彩演讲，他们在建一些最了不起的数据中心，在训练一些最了不起的模型。能和他们所有人合作是一种殊荣——一起去推动性能、推动 MTBI（平均无故障间隔），最终推动 token 效率，去生成我们所有人都在用、我们的智能体都在用的 AI 和 token，把这场革命往前推。

我们有一个平台叫 DSX。它是我们面向现代加速 AI 工厂的软件、生态和参考架构。我们现在实际已经贡献出去的，是我们的参考实现——也就是我们建议你如何用 NVIDIA 技术建一座完整的、模块化、规模化的 AI 工厂——把它开放出来，贡献给 OCP。

这实际上是为了能够做到最先进的每平方英尺 350 kW（口头表述）、100% 液冷，以及所有相关的技术、设计、扩展方式，还有流量等方面的规范——这是和 AMD、和 Google、和 Meta，当然还有 NVIDIA 一起，去建一个开放的数据中心规范。我们加入其中，并把我们的参考架构贡献给 OCP。

我们也正在研究这些数据中心该如何与电网对话。你知道，AI 工厂需要成为电网的一部分——不只是消费者，还要是贡献者。以及我们要如何管理这些相当强大的资产、能力和工厂，同时又不影响电费缴纳者、不成为电网的负担，而是成为资产。所以我们必须管理、必须分配、必须承担责任。如果电网需要更多电力，这些工厂要能响应，要能把功率调上去；也许要调下来，或者改变它们的负载，或者把负载推到明天而不是今天——因为外面太热了。

这实际上是与 Google、Meta、Microsoft 和 NVIDIA 的合作，去设计一份真正能用的电网韧性（grid resiliency）规范。这也是我们在 OCP 所做事情的重要部分——保持开放。公用事业是我们这个世界上最开放的东西，它必须建立在开放标准之上，这样我们才能都成为电网的一部分，而不是负担。

最后是软件，也就是数据中心里真正的操作系统。DSX 有很多不同的组件，用来管理和部署整个机群的一部分。我最自豪的其中一个叫 MaxLPS。MaxLPS 本质上是在说："让我们聪明地使用电力。"

我们通常听到的是"一座 100 MW 的数据中心"，但我们并不是时时刻刻都在用满那 100 MW。公用事业可能按 100 MW 给我们批了容量，但实际用量——每一种负载，不管是跑 GPT 还是做数据库操作——这个机架消耗的功率是不一样的。我们并不是一直在 100% 运行。这就是机会。

今天的世界是受电力约束的。我们没法把数据中心都建起来，但如果我们去研究、去看我们已经有的数据中心，我们其实并没有用完批给我们的全部电力。MaxLPS 就是抓住这个机会的办法。它是集成在我们机架与电源管理系统里的软件，是开源软件，实际帮助协调和调度各种不同的负载，并与调度器集成，告诉它："嘿，这里其实有富余的电力，你可以往这块 GPU 上多放一些负载。"

或者更好的是：你其实有可能在数据中心里多放一些 GPU——因为你不需要担心那个机架的峰值性能和 TDP，你真正要关心的是那个机架的"工作功率"。只要那里的软件在持续做功率封顶（power capping）和管理，保证没有线路过载、我们能待在规格之内，我们实际上就能增加 GPU 数量、增加我们产出的 token 数量。

这是一个正在和 Nscale 一起做的项目，数据中心我记得是在冰岛。通过在同一个数据中心里部署 MaxLPS 软件——再次强调，是开源软件——他们实际上在那个数据中心里多放了 37% 的 GPU（口播为"多 37 块 GPU"，幻灯片标注为"多 37%"，即 140 → 192 块）。

> Finally, OCP is not just about the brass iron and the hardware, but we all are building data centers. And you heard some great talks from Santosh and others here that are building some of the most amazing data centers and training some of these amazing models. It's a great privilege to work with all of them to drive performance, MTBI, and in the end token efficiency to generate the AI and the tokens that we're all using, our agents are using, to bring forward this revolution. We have a platform called DSX. It is our software and ecosystem and a reference architecture for a modern accelerated AI factories. We have actually now contributed our reference implementation, how we recommend how you build a full modular at scale complete AI factory with NVIDIA technology and made it open and contributing it to OCP. This is actually to build out to be able to do the state of the art 350 kW per square foot, 100% liquid cooling, all of the techniques and designs and scaling and specifications for flow and other things in collaboration with AMD, with Google, with Meta, and of course with NVIDIA to build an open data center spec. We're joining that and contributing our reference architecture to OCP. We're also working on how these data centers want to talk to the grid. You know, AI factories need to be part of the grid, not just consumers, but contributors. And how do we want to manage these quite powerful assets and capabilities and factories but not affect ratepayers and be a burden on the grid but an asset. So, we've got to manage and distribute and take responsibility. If the grid needs more power, these factories need to respond and be able to dial in the power, maybe dial it down or change their workloads or push workloads to tomorrow instead of today because it's hot outside. This is actually a collaboration with Google, again Meta, Microsoft, and NVIDIA to design a grid resiliency specification that actually works. And that's a big part of what we're doing here at OCP to be open. Utilities are the most open thing we have out there. Has to work with open standards so that we can all be part of the grid and not a burden. And finally, the software, the actual operating system in the data center. DSX has lots of different components for managing and deploying parts of the fleet. One of the ones I'm most proud of is actually called MaxLPS. MaxLPS basically says, "Let's be smart about the power we use." We typically hear about a 100 MW data center, but we don't actually use all 100 MW all the time. We may be provisioned that by the utility, but the actual usage — every workload, whether it be running GPT or doing a database operation — is going to consume a different amount of power for the rack. We're not running 100% all the time. That's an opportunity. The world is power constrained right now. We can't get data centers being stood up, but if we go and study and look at the data centers we already have, we're actually not using all the power that we have provisioned to us. MaxLPS is a way to actually take advantage of that opportunity. It's software that's integrated into our rack and power management system and open source software that actually helps coordinate and pull all the different workloads and integrating with the schedulers to say, "Hey, there's actually strained [stranded] power here. You can put some more workload on this GPU." Or even better, you can actually potentially put more GPUs in your data center because you don't need to worry about the max performance and the TDP of the actual rack, but actually what's the working power of that rack? And as long as the software there is constantly power capping and managing so that no circuit blows, and we can stay within spec, we can actually increase the number of GPUs and number of tokens we're building. This is a project being done with Nscale right now with a data center in I believe it's Iceland. They've actually been able to put 37 more GPUs in the data center by deploying the MaxLPS software, again open source software, into that same data center.

<div class="takeaway"><b>小结</b>　这一节把"开放"从机架推进到了电网：当 AI 工厂开始向电力公司承诺可调功率时，OCP 讨论的对象已经不是服务器，而是基础设施政策。</div>

## 12　Nscale：同样的电，多 37% 的 GPU，多 50% 的吞吐

![Nscale Increases Throughput 50% With MaxLPS：同样 264 kW 电力下，GPU 从 140 增至 192（+37%），吞吐从 1.1M 增至 1.6M tok/s（+50%）；脚注为冰岛 GB300 集群上 Kimi-K2.5 8K/1K 的实测聚合吞吐，静态 MaxP 为 1.083M，MaxLPS 为 1.618M，提升 49%](images/12_16m24s.jpg)

他们把资源对准了数据中心里收益最高的那些机会，以最大化收入，结果他们的收入和 token 吞吐实际增长了 50%。

我认为我们所有人都要重新看一个问题：不是"你能不能在最大功率下交付算力"，而是"你能不能高效地管理你的电力"。你的管理控制器是怎么工作的？你能不能快速响应？我们有没有为这些负载的灵活性做设计？

不会只有一个 AI 模型统治世界，也不会只有一种工具调用统治世界，它一定是动态的。我们的系统——如果我们能抓住这一点——就能更高效地使用现有的数据中心和现有的电力，并且在今天就实实在在把 GPU 数量再提高 40%。

去看看 MaxLPS，理解你的软件、你的控制逻辑如何管理并运行一个动态的功率环境，从而最大化你的 token 吞吐和收入，就像 Nscale 在那座数据中心里做到的那样。

> And they target toward the highest revenue opportunities they had inside of their data center to maximize the revenue and actually grew their revenue and their token throughput by 50%. I think all of us need to look at what is your — not the ability to deliver compute at a maximum power, but how can you manage your power efficiently? How is your management controller working? Can you respond quickly? And are we designing for the flexibility of these workloads? There isn't just one AI model that's going to rule the world. There isn't just one tool call that's going to rule the world. It's going to be dynamic. Our systems, if we can take advantage of this, we can actually more efficiently use the data centers and the power that we have now and quite literally increase the number of GPUs by another 40% today. Check out MaxLPS, understand how your software, how your control logic can manage and operate a dynamic power environment and to maximize your token throughput, your revenue just like Nscale did in this data center.

<div class="takeaway"><b>小结</b>　这是全场唯一一个有第三方实测的案例：不改电网、不加变压器，仅靠功率调度软件，同一度电多出 37% 的 GPU 和 50% 的 token——"电力约束"因此被重新定义成"调度问题"。</div>

---

# 第六部分　网络：从铜到光

## 13　Spectrum-X 光子多平面：2.6 毫秒的故障检测

![NVIDIA Spectrum-X Photonics Multiplane Ethernet Uninterrupted AI Connectivity：Spectrum-X 多平面光子使 AI 工厂以扁平两层网络扩展到 512K GPU；2.6 ms 故障检测、少 40% 交换机、5x 能效、10x MTBI；配 ConnectX-9 SuperNIC 与 BlueField-4 DPU](images/13_18m12s.jpg)

好，网络。我们显然一直在开创世界上最好的、面向 AI 的网络和以太网。随 Vera Rubin 一起推出的最新网络，是新的 Spectrum-X 光子多平面以太网（Photonic Multiplane Ethernet）。这实际上是我们的第一款 CPO（共封装光学）以太网交换机，Spectrum 建立在 Spectrum-X 之上。

它与 ConnectX-9 SuperNIC（就是我在图上指的那个）以及 BlueField-4 DPU 协同工作，去管理和连接——就像我们刚才听到的——横向扩展（scale-out），当然还有纵向扩展（scale-up），覆盖所有地方，用于运行智能体、训练模型和做推理。

最新 Spectrum-X 有意思、令人兴奋的地方在于它的多平面（multiplane）支持。多平面让它具备硬件管理的故障检测能力，可以在 2.6 毫秒内发现一条链路 down 或者链路抖动（link flap）。此前世界上其他网络交换机必须用软件来检测和响应链路 down。如果你有 2.6 毫秒，你就能在百分之一秒内做出响应，非常快地识别出链路抖动，并把那条链路从链条里摘出去，这样你就不会丢数据，也不会拖慢整个计算。你会立刻响应。

另外，使用多平面、以及带故障检测的硬件多平面系统，你实际上可以用更少的交换机——少 40%。更酷的是，这是一台共封装光学（co-packaged optics）交换机。也就是说，我们把收发器和光引擎直接放到封装上，与交换芯片共封装。你在图上能看到。这实际上带来 5 倍更高的能效；而且因为我们做了共封装和设计，信号只需要从交换芯片走到同一封装上的光引擎。

那个交换机中间其实是 NVIDIA 的硅片——这里有一张它的照片。这就是 CPO 的 Spectrum-X 封装，它实际上是 Spectrum-X 光子多平面交换机的一部分。在这个配置里，我们只有一颗交换机芯片。在更大的 Spectrum-X 里，我们实际会用四颗这样的芯片，组成一个 400 Tbps 的 Spectrum 交换方案。

最令人兴奋的是什么？它今年就会出货。所以非常激动地宣布这件事。它将彻底改变我们做大规模训练的可靠性和规模，真正把全世界的 AI 数据中心连在一起。非常期待。谢谢。

> Okay, networking. We have obviously been pioneering in the world's best networking and ethernet for AI. Our latest networking that comes with Vera Rubin is the new Spectrum-X photonic multi-plane ethernet. This actually is our first CPO based ethernet switch, Spectrum built on Spectrum-X. It works in sync with the ConnectX-9 SuperNICs, which I see there, and the BlueField-4 DPUs to manage and connect, as we just heard, the scale out and of course the scale up of all and across and everywhere for running agents, training models, and doing inference. What's interesting and exciting about the new latest Spectrum-X is actually it's multi-plane support. Multi-plane has hardware managed capabilities to detect faults, so it can find a link down or a link flap actually within 2.6 milliseconds. Prior network switches in the rest of the world has to use software to detect it and respond to link downs. If you have 2.6 milliseconds, you can respond in like a hundredth of a second, very quickly identify a link flap, and take that link out of the chain so that you're not losing data or slowing down the entire computation. You will respond immediately. Also using multi-plane and hardware system multi-plane with the fault detection, you can actually use 40% fewer switches. What's even cooler is that this is a co-packaged optical switch. That means we put the transceivers and the optical engines directly on the package, co-package it with the switch. You can see it there. That actually delivers you 5x higher power efficiency, and because we've co-packaged it and designed it, the signals only need to travel from the switch chip right to the optical engine, which is on the same package. In the middle of that switch actually is NVIDIA's silicon. There's a shot of it here. This is the CPO Spectrum-X package that actually is part of the Spectrum-X Photonic multi-plane switch. In this configuration, we have a single switch. In the larger Spectrum-X, we actually have four of these chips to build up a 400 terabit Spectrum switch solution. What's super exciting about this? This is actually shipping this year. So, super excited to be announcing this. It's going to totally change the reliability and the scale of which we can do training at scale and actually connect the world's AI data centers together. Very excited about it. Thank you.

<div class="takeaway"><b>小结</b>　把故障检测从软件挪进硬件，换来的不只是 2.6 毫秒，而是"少 40% 交换机"——多平面让容错不再需要用冗余端口去买。</div>

## 14　为 Meta 造的 Spectrum-6

![Announcing Spectrum-6 Ethernet Switch for Meta's AI Factory：Meta 102.4T FBOSS 交换机（N-IceCube），基于 NVIDIA Spectrum-6；多平面协作提升韧性、全球最快故障检测（比传统软件方案快 30 倍）、NVIDIA 开放以太网硅片配 OCP 软件栈](images/14_20m21s.jpg)

最后，我们当然把这一切开放出来。Spectrum 对 OCP 开放，也对与我们所有 CSP 伙伴的集成开放。

很高兴宣布我们与 Meta、与 Santosh 和他的团队的合作，为 Meta 的 AI 工厂交付 Spectrum-6 以太网交换机。这就是 Meta 那颗 102.4T 的 FBOSS 交换机，叫 IceCube（N-IceCube）。它基于 NVIDIA Spectrum-X，实际实现了 Meta 自己的网络协议，用来把这些交换机大规模连起来，并且与他们合作实现了 Spectrum-X 的多平面，以获得更好的韧性和更平滑的部署。

另外，我们一直在和 Google 合作。去年，Google 把 Google Falcon 这个传输引擎贡献给了 OCP——一个非常重要的贡献，让 Google 得以分享他们实际上是怎么把所有数据中心连起来、怎么在所有那些交换机之间做传输的。Google Falcon。我们一直在和他们合作，并且……

> Finally, we of course make this open. Spectrum is open to OCP and open to integrations with all of our CSP partners. Happy to be announcing our work with Meta and Santosh and his team to actually deliver the Spectrum-6 Ethernet switch for Meta's AI factory. This is the Meta 102.4T FBOSS switch called the IceCube. It's based on NVIDIA Spectrum-X, actually implements Meta's own networking protocol to connect these at scale, and actually implements the Spectrum-X multi-plane in collaboration with them for better resiliency and smooth deployment. In addition, we've been working with Google. Last year, Google contributed Google Falcon, the transport engine, to OCP. A really important contribution that lets Google share how they actually connect all of their data centers and how they do the transport across all those switches. Google Falcon. We've been working with them and

<div class="takeaway"><b>小结</b>　"用 NVIDIA 的硅片跑 Meta 自己的协议"是这一页的分量所在：开放交换芯片第一次让超大规模厂商保留协议自主权。</div>

## 15　把 Google Falcon 移植到 NVIDIA 网络

![Announcing Google Falcon Transport on NVIDIA Networking：多路径负载均衡、可编程拥塞控制、硬件丢包恢复、逐连接安全；支持 Spectrum-X SuperNIC 与 BlueField DPU；Google Cloud + NVIDIA + OCP 三方标识](images/15_21m06s.jpg)

……与他们合作，把 Google Falcon 移植并实现在 NVIDIA 的平台上。所以我们现在也贡献出来、并且宣布我们已经做到了。

我们把 Google Falcon 具备的多路径负载均衡（multipath load balancing）、可编程拥塞控制（programmable congestion control）、硬件丢包恢复（hardware loss recovery），以及逐连接安全（per-connection security）全部做了进去，让它在 Spectrum-X SuperNIC 上可用，并在 BlueField DPU 上实现，然后同样回馈给 OCP。

> partnering with them actually to port and implement Google Falcon on NVIDIA. So, we're now we're also contributing and announcing that we've done that. We put all the multi-path load balancing, the programmable congestion control, all the hardware loss recovery, and the per connection security that Google Falcon has, and made it available on the Spectrum-X SuperNIC, and implemented on the BlueField DPUs, and contributed that as well back to OCP.

<div class="takeaway"><b>小结</b>　这件事的方向值得注意：不是让 Google 采用 NVIDIA 的传输协议，而是把 Google 的协议实现在 NVIDIA 的硅片上——贡献是双向的，才叫开放。</div>

## 16　一个平台，四种传输

![Spectrum-X Ethernet Extends Open Networking Leadership：Google Cloud 的 Falcon、Meta 的 Meta RoCE、OpenAI 的 MRC、NVIDIA 的 Spectrum-X Adaptive RDMA，四种 AI 传输跑在同一个加速以太网平台上](images/16_21m51s.jpg)

Spectrum-X 是我们面向开放网络的平台。不管是 Google Cloud 的 Falcon、Meta 的 RoCE、OpenAI 的 MRC，还是 NVIDIA 自己的 Spectrum-X Adaptive RDMA。

这里有非常多很棒的想法和方式，去扩展并连接所有这些数据中心，不管它们跑的是 AI 还是加速计算。它是一个创新的平台。而且它完全是开放的——这正是 OCP 最了不起的地方，也是我们在这里的原因。

最后，还有一件事。当全世界正在收到他们的 Rubin 系统、正在建设的时候——你们已经看到了一些了不起的成果，比如 Astra 现在跑在 Vera Rubin 上，而且跑得更快——我们并没有停下。我们已经在做下一代了。这是 Vera Rubin Ultra 的一个抢先预览。它实际上不是单机架 72 块 GPU……

> Spectrum-X is our platform for open networking. Whether it be Google Cloud Falcon, Meta RoCE, OpenAI's MRC, or NVIDIA's own Spectrum-X Adaptive RDMA. There's lots of amazing ideas and ways to actually scale and connect all of these data centers, whether they'll be running AI or accelerated computing. It's a platform for innovation. And it's all open, which is what's so great about OCP and what we're here for. And finally, one more thing. While the world is actually now receiving all of their Rubin systems and building out, and you've already seen some of the amazing work of — you know, Astra is now running on Vera Rubin, and running faster. We're not sitting still. We're already working on the next generation. Here's a sneak peek of Vera Rubin Ultra. This actually is not 72 GPUs in a single

<div class="takeaway"><b>小结</b>　四家超大规模厂商各用各的传输协议却共用同一块硅片，这是"开放"最实用的一种形态：接口标准化，协议不强制统一。</div>

---

# 第七部分　下一代与收尾

## 17　Vera Rubin Ultra：单机架 576 块 GPU

![Vera Rubin Ultra NVL576 Is Built for Breakthrough Scale and Efficiency：Vera Rubin Ultra 计算托盘、NVLink 7 CPO 交换托盘，以及由八组机架连成的 NVL576 CPO 系统，为 10T+ 参数模型设计](images/17_22m45s.jpg)

……而是实际上 576 块 GPU，全部用 NVLink 连接。它用的是我们下一代的 NVLink CPO 交换托盘——我这里有它的照片——以及我们下一代的 Vera Rubin 托盘。你可能会注意到这里有一些相似之处。这一切都基于 OCP 标准。

它实际上会把这些 GPU、以及所有独立的机架，通过 CPO 网络连在一起，组成一个巨大的、576 块 GPU 全部用 NVLink 相连的系统——就是那里那些细细的黄色光纤，连接着那些光引擎。

这将是地球上每瓦性能最高的、扁平的 NVLink 巨型 GPU，它的设计目标是把我们带到 10 万亿参数模型——明年我们到那里时就能享受它。

我就讲到这里，谢谢大家到场。我希望你们来参加 OCP 的活动。我们有很多精彩的演讲。这里有几个和 AI tokenomics 相关的。我们可以详细解释 NVIDIA 与伙伴们一起做的工作，以及电网如何运作，还有我们下一代的 DC 架构，以及它如何……

> rack, but actually 576 GPUs that are all NVLink connected. This is using our next generation NVLink CPO switch tray, and I have a picture of it here, along with our next generation Vera Rubin tray. You may notice some similarities here. This is all based on the OCP standards. And it's actually going to be connecting all of those GPUs and all of those individual racks together with CPO networking to build one giant 576 GPUs all connected with NVLink, with the little yellow fibers there connecting those optical engines. This will be the highest performance per watt flat NVLink giant GPU on the planet and is designed to take us to 10 trillion parameter models to enjoy when we get there next year. That's it for me and thank you for coming. I want you to join us at OCP. We have lots of great talks. There's a couple here with AI tokenomics. We can explain in detail the work that's being done with NVIDIA in partnership with others, and how the grid works, and also our next generation DC architecture and how it's

<div class="takeaway"><b>小结</b>　72 → 576 不是简单堆数量：跨机架靠 CPO 光纤把 NVLink 延伸到整个集群，等于把"一台 GPU"的边界从机架推到了机房。</div>

## 18　来 OCP 听我们讲

![Join Us at OCP：OCP Talks 共 33 场，列出的六场包括 AI Tokenomics Explained、800 VDC AI Factories、Flexibility the Grid Can Count On、Revolutionizing Networking for Gigawatt AI Factories、Next-Gen ML Infrastructure、The AI Factory Digital Twin](images/18_23m30s.jpg)

……从今天扩展到明天、再往后。那里还有一个非常酷的技术展示。如果你想看连接器如何与母排配合工作、我们回馈给 OCP 的所有东西，以及我们是怎么造出 Blackwell 和 Vera Rubin 的，还有……

> going to scale from today to tomorrow and beyond. And there are really cool displays of all of the technology. If you want to see how the connectors work with bus bars, all the things that we're contributing back to OCP and how we built Blackwell and Vera Rubin and

<div class="takeaway"><b>小结</b>　33 场 NVIDIA 相关议程里，"tokenomics""电网""数字孪生"占了多数——这家公司对外讲述的重点，已经从芯片转向了工厂的经济性。</div>

## 19　MGX 生态展区

![MGX Ecosystem 展区：NVIDIA AI Factory MGX Ecosystem，近 100 家伙伴参展，展出 800 VDC 供电技术与下一代创新](images/19_23m51s.jpg)

……以及往前走，Vera Rubin Ultra 的一些组件。你能看到我们实际上是如何贡献、如何帮助世界建起这些工厂的——这些我们今天共同在生产的工厂。

谢谢大家到场。希望你们享受 OCP 剩下的议程，谢谢。（掌声）

> moving forward some of the components of Vera Rubin Ultra there. You can see how we're actually contributing and helping the world build the factories that we're all producing together today. Thank you for coming. I hope you have enjoyed the rest of OCP and thank you. [applause]

<div class="takeaway"><b>小结</b>　收尾没有回到产品，而是回到展区里那近 100 家伙伴——这场演讲真正想证明的，是这条供应链已经能独立运转。</div>

---

# 附录

## A. 关键数据核对表

| 数据项 | 幻灯片值 | 口播值 | 本文采用 |
|---|---|---|---|
| Agentic 负载吞吐提升 | 最高 30x（每兆瓦 token） | 2x / 10x / 极端 30x | 幻灯片值 |
| 每百万 token 成本 | 低 45x | 低 45x | 一致 |
| 计算托盘装配时间 | 90 分钟 → 1 分钟 | 同 | 一致 |
| 800 VDC 省铜 | 未标注 | 少 45% | 口播值（已标注） |
| 800 VDC 机架功率范围 | 未标注 | 100 kW → 1 MW | 口播值（已标注） |
| Vera 单核性能 | 2x（对比 Grace） | 2x | 一致 |
| Vera 核间带宽 | 3.4 TB/s | 3.4 TB/s | 一致 |
| Vera 内存带宽 | 1.2 TB/s（每核） | 1.2 TB/s（每核） | 一致 |
| Meta DCPERF | 2x | 2x | 一致 |
| HPC Golden Suite（TACC） | 2x | 2x | 一致 |
| Apache Kafka（Redpanda） | 3.5x | 3.5x | 一致 |
| Vera 机架 CPU 数量 | 未标注 | 256 颗 | 口播值（已标注） |
| MaxLPS 增益 | 同电力下多 40% GPU | 多 40% | 一致 |
| Nscale GPU 数量 | 140 → 192（+37%） | "多 37 块 GPU" | **幻灯片值**（口播有误） |
| Nscale 吞吐 | 1.1M → 1.6M tok/s（+50%） | +50% | 一致 |
| Nscale 实测脚注 | 1.083M → 1.618M tok/s（+49%） | — | 幻灯片值 |
| 故障检测时延 | 2.6 ms | 2.6 ms | 一致 |
| 交换机数量 | 少 40% | 少 40% | 一致 |
| CPO 能效 | 5x | 5x | 一致 |
| MTBI 提升 | 10x | — | 幻灯片值 |
| 网络扩展规模 | 512K GPU，扁平两层 | — | 幻灯片值 |
| Spectrum-X 交换容量 | 单芯片 → 4 芯片 400 Tbps | 400 Tbps | 一致 |
| Meta 交换机 | 102.4T FBOSS（N-IceCube） | "1.2T F" | **幻灯片值**（口播含糊） |
| 故障检测对比传统软件 | 快 30x | — | 幻灯片值 |
| Vera Rubin Ultra | 单机架 576 GPU | 576 GPU | 一致 |
| 目标模型规模 | 10T+ 参数 | 10 万亿参数 | 一致 |
| 开发者规模 | 10M | 1000 万 | 一致 |
| 供应链伙伴 | 300+ | 300+ | 一致 |
| 生态伙伴参展 | 近 100 家 | — | 幻灯片值 |

## B. 时间轴

| 时间 | 内容 |
|---|---|
| 00:00 | 开场：十三年贡献史 |
| 00:48 | 基础设施的三个属性 |
| 01:12 | 1000 万开发者与 300+ 供应链 |
| 02:36 | 全栈协同设计：30x 吞吐、45x 成本 |
| 03:33 | 第三代 MGX（MGX 1.2）规范 |
| 04:51 | 可制造性：90 分钟 → 1 分钟 |
| 05:45 | 首座 800 VDC AI 工厂（Visionbay.ai） |
| 07:06 | Vera CPU 的设计取舍 |
| 09:48 | Vera 基准：DCPERF / HPC / Kafka |
| 10:39 | Vera CPU MGX 机架发布 |
| 12:00 | DSX：开放规范、电网韧性、MaxLPS |
| 15:51 | Nscale 案例：同样的电，多 50% 吞吐 |
| 17:12 | Spectrum-X 光子多平面以太网 |
| 20:03 | 为 Meta 造的 Spectrum-6 |
| 20:42 | Google Falcon 移植到 NVIDIA |
| 21:30 | 一个平台，四种传输 |
| 22:24 | Vera Rubin Ultra NVL576 预览 |
| 23:21 | OCP 议程导览 |
| 23:39 | 收尾与致谢 |

## C. 术语对照

| 缩写 | 全称 | 说明 |
|---|---|---|
| MGX | Modular GPU Accelerator | NVIDIA 的机架级模块化架构规范，已贡献给 OCP |
| CPO | Co-Packaged Optics | 共封装光学：把光引擎与交换芯片封在同一基板上 |
| DSX | — | NVIDIA 面向 AI 工厂的软件、生态与参考架构平台 |
| MaxLPS | Max Liquid-cooled Power Smoothing | 机架级动态功率调度软件，开源 |
| MTBI | Mean Time Between Interruptions | 平均无故障间隔，衡量集群稳定性的指标 |
| FBOSS | Facebook Open Switching System | Meta 的开放交换机软件栈 |
| MQD / MQDB | Modular Quick Disconnect | 托盘内液冷快速接头 |
| UQD | Universal Quick Disconnect | OCP 标准的液冷快接头规格 |
| RoCE | RDMA over Converged Ethernet | 融合以太网上的远程直接内存访问 |
| DCPERF | Data Center Performance | Meta 开源的服务器性能基准，托管于 GitHub |
