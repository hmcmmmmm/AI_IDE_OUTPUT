# 构建下一代 AI 基础设施

**AMD 董事长兼 CEO 苏姿丰（Dr. Lisa Su）OCP Global Summit 2026 主题演讲 · 图文实录**

---

## 关于这份文档

这是一份**逐段实录**，不是要点综述。每一节遵循同一结构：

- **图片**：演讲当时投影的幻灯片（或现场画面），按时间顺序
- **中文译文**：苏姿丰在这一页停留期间所说的话，逐句翻译，不作删减
- **英文原句**：同段话的英文原文，供核对与引用
- **小结**：整理者对这一段的一句话归纳，与讲话内容明确区分

原文由 YouTube 自动字幕转写，已去除 um、uh 等口头填充词，并修正明显的转写错误（如 EPYC、agentic、OCP 等专有名词）。中文译文以"准确传达原意"为优先，而非追求文采。

---

## 视频信息

| 项目 | 内容 |
|---|---|
| 标题 | Building the Next Era of AI Infrastructure |
| 演讲人 | Dr. Lisa Su（苏姿丰），AMD 董事长兼首席执行官 |
| 场合 | OCP Global Summit 2026 · AMD Keynote |
| 时间地点 | 2026 年 10 月，加州圣何塞（幻灯片页脚：October 15, 2026） |
| 时长 | 27 分 37 秒 |
| 频道 | Open Compute Project（YouTube） |
| 链接 | https://www.youtube.com/watch?v=3nFDQMaoNKc |

---

# 第一部分　开场与市场判断

![OCP Global Summit 2026 开场画面：Scaling Innovation for the AI Era](images/01_00m03s.jpg)

## 01 ｜ 00:09　开场

![AMD Keynote：Dr. Lisa Su, Chair and Chief Executive Officer, AMD](images/02_00m09s.jpg)

我听说这里是必须来的地方。事实上，AMD 一直是 OCP 的长期支持者，但这确实是我第一次参加 OCP 全球峰会，我必须说，这里的规模让我震撼。所以我要祝贺 George，也祝贺整个组委会，办了一场非常出色的活动。

今天我想先谈谈我们在 AMD 看到的、市场上正在发生的事。我可以肯定地说，这是我见过变化最快的市场——如此多的变化、如此多的创新、如此多的协作。

从总体上讲，我们 AMD 所有人每天醒来想的是：我们的工作是推动高性能计算的边界，去解决世界上一些最重要的挑战和问题。而要做到这一点，实际上需要深度的协作。

> I have heard that this is the place to be. Actually, AMD has been a long-standing supporter of OCP, but this is actually my first time at the OCP Global Summit, and I have to say I'm just blown away by the scale of what we have here. So, I want to congratulate George and really the entire organizing committee for putting together just a fantastic event. So, today what I'd like to do is maybe talk a little bit about what we see at AMD in terms of what's happening in the market. I can say for sure it's the fastest-moving market that I've ever seen. So much change, so much innovation, so much collaboration. And maybe from an overarching standpoint, I would say, for all of us at AMD, we wake up every day thinking that our job is to really push the boundaries of high-performance computing so that we can solve some of the most important challenges and problems in the world. And to do this actually requires intense collaboration.

<div class="takeaway"><b>小结</b>　开场用两个判断定调：这是"变化最快的市场"，而应对方式是"必须协作"。这两句话是全场后续所有技术叙事的伏笔。</div>

## 02 ｜ 01:21　解决世界上最重要的问题

![Solving the World's Most Important Challenges：Compute is the Engine of Human Progress](images/03_01m21s.jpg)

因为我坚信，没有任何一家公司能对所有问题都有答案。坦白说，我们越能把各家最好的东西聚到一起，整个行业就会做得越好。

所以，"开放"是 AMD 原则的基础——我们在开发技术时会考虑它，在制定路线图时也会考虑它。

> Because I'm a big believer that there is no one company that has every answer to every solution. And frankly, the more we can bring the best of our companies together, the better we're going to do as an industry. And so, AMD has open as a foundation of our principles. It's one of the things that we think about when we develop technology. It's one of the things that we think about when we develop our road map.

<div class="takeaway"><b>小结</b>　把"开放"从价值观表述转化为工程约束：不是姿态，而是路线图的输入条件。</div>

## 03 ｜ 02:18　与 OCP 协作的十五年

![AMD × OCP：15 Years of Collaboration，从 Open Server Platform 到 Open AI Infrastructure](images/04_02m18s.jpg)

回看过去 15 年 OCP 真正做成的事，它其实是我们路线图中很大的一部分。

最早是开放服务器平台——2017 年我们与微软紧密合作，做出了第一代 Naples 平台，然后一起把它带进 OCP。

再看近几年，网络侧有大量工作汇聚起来：超以太网联盟（UEC），以及我们在 UALink 和 ESON 上做的事。这些对互操作性都至关重要。

我很期待谈 Helios。今天会讲讲这个机架级方案的进展。

> And when you look at the last 15 years of what OCP has really done, it's really been a huge part of our development road map going forward. First on our open server platforms, from our very first platform that we did with Naples back in 2017 — that was a very close collaboration with our partner Microsoft, but together we brought it to OCP. When you look at over the last few years, a lot of work has come together on the networking side with the Ultra Ethernet Consortium, with the work that we're doing around UALink and ESON. All of those are really important things for interoperability. I'm excited to talk about Helios. So, we're going to talk a little bit about Helios today and the progress on that rack-scale solution.

<div class="takeaway"><b>小结</b>　用一条十五年时间线证明开放不是新姿态：从 2017 年 Naples 到 UEC、UALink、ESON，AMD 的关键平台都先在 OCP 落地。</div>

## 04 ｜ 03:27　AI 正在改造每一个行业

![AI Is Transforming Every Industry：Healthcare、Manufacturing、Science、Finance、Media](images/05_03m27s.jpg)

这个机架级方案同样基于 OCP 标准。往前看，我们还有很多可以协作的机会——无论是 MRC 还是 Oak，这些都是整个生态可以一起做的巨大机会。

当我们作为一个开放生态走到一起，我们实际上会加快创新的速度，为客户交付更好的方案。

说一点市场的情况。我想你们都很清楚，AI 市场正在真正改造世界的每一个部分、每一个我们所在的行业——无论是医疗、制造还是科学。我们看到的能力提升要大得多。

我常说，我们正处在一个"计算即智能"的世界里。如果你有机会变得更智能，为什么不去争取更强的能力呢？这正是我们想把这一切带进生态所做的事。

> Solution, which is again based on OCP standards. And then looking forward, I think we have lots more opportunities to collaborate together, and these also become — whether you're talking about MRC or Oak — these are also areas where there's just a tremendous opportunity for us to come together as an ecosystem. And with the notion of when we come together as an open ecosystem, we will actually accelerate the pace of innovation and get better solutions for our joint customers. So, a little bit about the market. I think you guys know very well the AI market is truly transforming every part of the world, every industry that we're in — whether you're talking about healthcare or manufacturing or science. We're seeing much, much more capability come across. I like to say that we're in a world where computing equates to intelligence. And if you have the chance to be more intelligent, why wouldn't you try to get more capability?

<div class="takeaway"><b>小结</b>　"计算即智能"是全场的经济学前提：算力不再是成本项，而是能力的直接来源，因此需求没有天然上限。</div>

## 05 ｜ 04:06　需求持续加速：95 倍

![Demand for AI Continues to Accelerate：95x increase in tokens per month consumed over past 2 years](images/06_04m06s.jpg)

这正是我们试图把这一切带进生态所做的事。

看几个需求数字。每次我看这些图表，它们总是一路向右上方走。人们总在问：我们确定投入的这些 AI 算力是在做有效的工作吗？答案绝对是肯定的。我们在完成大量的工作，而且每一次都变得更有效率。

你看这些需求数字，过去两年每月消耗的 Token 增长了 95 倍。

> And just a few of the demand numbers that you see — every time I look at these charts, they tend to keep going up into the right. And people are always asking, well, are we sure that we're doing productive work with all of the AI compute that we're putting on board? And the answer is absolutely yes. We are doing a tremendous amount of work. We're getting more and more productive each time. You look at some of these demand numbers and you see like a 95x increase in tokens per month over the past 2 years.

<div class="takeaway"><b>小结</b>　95 倍这个数字是用来回应"算力是否过剩"的质疑：Token 消耗仍在加速，尚未见顶。</div>

## 06 ｜ 05:21　推理成为第一大工作负载

![Training Continues to Scale（训练算力每年 5 倍）；But Inference Is Now the #1 AI Workload（智能体驱动，年初至今 ≥14x）](images/07_05m21s.jpg)

我们现在的规模大约是每月 40 万亿亿（4×10¹⁶）个推理 Token。

谈到这对"有用的 AI"意味着什么，我们会看到很多不同的数据。但对我最重要的数据，是我和客户交流时、和最大的用户相处时看到的东西。

显然，训练仍然极其重要，我们仍然需要世界上最大的训练集群，仍然会继续推进能力边界——可以说自 2020 年以来每年增长 5 倍，而且这个趋势看起来不会改变，会继续下去。

但我们一直认为，AI 真正产生回报的时刻，是推理超过训练的时候。看过去几年的数字，尤其是 2026 年——今年真的是"推理之年"。我们认为从今年起，推理大约占市场的 60%。

而且不只是推理，真正起飞的是智能体工作负载。看这些数字，这是 OpenRouter 的新数据，它把请求路由到许多模型，你可以看到人类流量在稳步上升，但真正增长的是智能体流量——仅今年，经过的智能体流量就增长了 14 倍。

> We're now at some number like almost 40 quadrillion inference tokens a month. When you think about what that means in terms of useful AI, we get a lot of different data, but I think the data that's most important to me is what do I see when I talk to customers and when I spend time with the largest users. Clearly, training continues to be extremely important and we're going to continue to need the largest training clusters in the world, and we're going to continue to push the envelope on capability — let's call it 5x increase every year since 2020, and that doesn't look like that's going to change. But we've always thought that where AI really pays off is when inference overtakes training. And when you look at the numbers over the last few years, especially this year in 2026 — this year is really the year of inference. This is the year where we believe inference is now about 60% of the market going forward. And it's not just inference, it's really the agentic workloads that have really taken off. This is some new data from OpenRouter, which routes requests across many models, and what you see is that the amount of human traffic has gone up steadily, but what's really grown is the amount of agentic traffic — and we're seeing a 14x growth just this year.

<div class="takeaway"><b>小结</b>　全场最重要的结构判断：2026 年是"推理之年"，推理约占市场 60%，且增量主要来自智能体而非人类流量。</div>

## 07 ｜ 06:57　CPU 与加速器同步上修

![Demand Accelerating Across CPUs and GPUs：CPU TAM 2025 $26B → 2030 $220B；AI Accelerator TAM 2025 $200B → 2030 $1.4T](images/08_06m57s.jpg)

这就是 AI 在起作用的力量。我们在训练更好的模型，现在不仅有机会做推理，还有机会真正解决问题。因此我们看到更多的增长机会——而且是真正有产出的增长。

George 刚才展示了一些与基础设施相关的 TAM 数字。这里是与芯片和系统相关的 TAM，芯片是核心，也是我们专注的地方。

我们看到几件事。首先，数据中心 AI 加速器的 TAM 到 2030 年将增长到接近 1.5 万亿美元，这是一个极其庞大的数字，这也是为什么这个领域有如此多的热情和创新。

但我们也看到，随着智能体工作负载的出现，过去被称为"传统 CPU"的 TAM 出现了非常显著的增长。如果你看这个数字——就算是一年前——人们会说："CPU 市场大概是个 200 亿美元的市场，未来几年个位数增长。"

> And that kind of tells you the power of AI working. We're training better models. We now have the opportunity not just to do inference, but we have the opportunity to solve problems. And with that we're seeing a lot more opportunity for growth — really productive growth going forward. Now, George showed some numbers about the TAM as it relates to the infrastructure. This is some information on the TAM as it relates to the silicon and the systems — the silicon is the core, which is what we're focused on. And we're seeing a couple things. First of all, we're seeing the data center AI accelerator TAM grow to close to 1.5 trillion by the time we get to 2030, which is a fantastically large number. That's why there's so much excitement and innovation in this area. But we've also seen that with agentic workloads, we've seen a very significant increase in what was known as the traditional CPU TAM. If you were to look at this number even a year ago, people would have said, "Hey, the CPU market is probably a 20 billion-dollar market growing single digits over the next few years."

<div class="takeaway"><b>小结</b>　14 倍的智能体流量把 CPU 重新拉回牌桌——这是 AMD 敢于大幅上修 CPU TAM 的实证依据。</div>

## 08 ｜ 08:51　AMD 的三大战略支柱

![AMD Strategy：Compute Leadership + Open Platforms + Pervasive AI](images/09_08m51s.jpg)

而实际上，我们在过去九个月里把这条曲线往上调了三次，因为我们看到了 CPU 总需求的增长幅度。我们现在认为，未来四到五年它会以约 50% 的年复合增长率增长，到 2030 年 TAM 超过 2,000 亿美元。

这对你如何构建系统是有含义的。事实是，算力没有"一招通吃"。你实际上需要为合适的工作负载匹配正确的算力——这涵盖 CPU、GPU、ASIC、FPGA，以及它们之间的各种组合。这也是 AMD 专注的基础。

所以我们认为最重要的三件事：第一，也是首要的，我们是一家计算公司。计算即智能，我们必须有算力领导力——覆盖 CPU、GPU、ASIC 的每一个方面，因为每个应用都需要合适的算力。

第二，我们相信 AI 将无处不在。接下来几天大概会有很多关于云端、超大规模和企业级"大机器"的讨论。我们同样坚信，AI 会渗透到边缘和客户端的每一个角落。我们越能让这些不同形态的标准统一、让软件在所有系统上通用，就越能为最终用户带来生产力。

> And we have actually raised the TAM on this three times in the last nine months, because we've seen that much growth in the overall CPU demand, which we now believe will grow at approximately 50% CAGR over the next four or five years to over a 200 billion-dollar TAM by the time you get to 2030. And that has implications on how you want to build systems. The fact is, there's no one size fits all when it comes to compute. You actually need the right compute for the right workload, and that's across CPUs and GPUs and ASICs and FPGAs and all of the mix in between. And that's the foundation of how we have really focused at AMD. So, the three things that we think are most important: first and foremost is we're a compute company. Compute equals intelligence. We need to have compute leadership. And that compute leadership is across every aspect — CPU, GPU, ASIC — because we need the right compute for each application. We also believe that you're going to see AI everywhere. We're big believers in the fact that you're going to see AI infused through every aspect of the edge as well as the client in the ecosystem. And the more that we can get the standards across those different form factors to be the same, the more that we can get the software to work across all of those systems.

<div class="takeaway"><b>小结</b>　九个月三次上修 CPU TAM（2030 年约 2,200 亿美元、50% CAGR），并由此推出"没有一种算力能通吃"的系统设计原则。</div>

## 09 ｜ 09:45　协作的规模

![AMD × OCP：Collaboration at Scale — Rack-Scale Innovation、Agentic Infrastructure](images/10_09m45s.jpg)

而第三个点，也是今天最相关的：开放是 AMD 所做一切的基础。我们非常、非常坚信，开放平台促成协作，协作让每家公司拿出最好的东西，从而让我们有更好的整体方案。

事实是，规模化的 AI 是一项团队运动。在这个领域，我们要把整个行业聚到一起。

所以今天我会讲一点我们在机架级创新上做的工作，因为这一年对我们来说非常、非常激动人心。

> And then the middle point is the point that's most relevant for today. Open is a foundation of what we do at AMD. We are big, big believers in the idea that open platforms enable collaboration. Collaboration enables the best of each company to bring to the table so that we have better overall solutions. And the fact is, AI at scale is a team sport. It is an area where we want to bring the industry together. So, I'll talk a little bit today about the work that we're doing on rack-scale innovation, because it's been a very, very exciting year for us.

<div class="takeaway"><b>小结</b>　"开放平台 → 协作 → 更好的整体方案"被表述为因果链而非口号，并由此引出本场主线：机架级创新。</div>

## 10 ｜ 10:24　前沿 AI 需要集成式机架

![Frontier AI Requires Integrated Rack Architectures：Leadership Compute、Open Rack Architecture、Scale-Out Fabric、Efficiency & Serviceability、Turnkey Solutions](images/11_10m24s.jpg)

接下来讲一点我们对智能体基础设施的判断。

首先，我想你们都清楚这一点，这也是一个原则：前沿 AI 对我们所有人的要求越来越高。我们的工作是把方案带到市场，让最终用户尽可能快、尽可能高效、尽可能少摩擦地使用这项技术，拿到最好的"每美元 Token 数"和"每次结果 Token 数"。

要做到这一点，你需要所有这些东西：你需要领先的算力，你需要开放的机架架构，你需要一个能跨系统扩展的 fabric。

> Then a little bit about what we see going forward in terms of the agentic infrastructure. First and foremost, I think all of you guys know this, but this has been a principle — frontier AI has higher and higher demands on what all of us do. Our job is to bring a solution to the market that allows our end users to use the technology as fast as possible, as efficiently as possible, with as little friction as possible, to get the best tokens for dollar, to get the best tokens for outcome. And to do that, you need all of these pieces. You need to have leadership compute. You need to have an open rack architecture. You need to have a fabric that allows you to scale across the systems.

<div class="takeaway"><b>小结</b>　五项能力缺一不可：领先算力、开放机架、扩展 fabric、能效与可维护性、交钥匙交付。这是 Helios 的设计前提。</div>

## 11 ｜ 11:21　Helios 登场

![AMD HELIOS：The Highest Performance Rack-Scale AI Solution](images/12_11m21s.jpg)

我们还需要关心效率、可维护性，以及整体的交钥匙方案。所以这些全都需要。

我必须说，当我们决定推出 Helios 架构时，所有这些都至关重要。我们在今年 7 月发布了 Helios，就在几个月前。

我们的看法是：这是业界性能最高的 AI 机架。72 颗 GPU 作为单一加速器协同工作，超过 18,000 个 GPU 计算单元，4,600 个 Zen 6 核心。每个计算托盘有点重——160 磅。

> We also need to care about things like efficiency and serviceability, as well as overall turnkey solutions. So, you need all of these things. And I have to say, all of these things were critical when we decided to bring out the Helios architecture. We launched Helios in July of this year, just a couple of months ago. Our view is that this is the highest performance AI rack in the industry. 72 GPUs working together as a single accelerator. More than 18,000 GPU compute units. 4,600 Zen 6 cores. Each compute tray is just a little bit heavy at 160 lb.

<div class="takeaway"><b>小结</b>　Helios 于 2026 年 7 月发布，核心卖点是"72 颗 GPU 作为单一加速器"，而非单芯片性能。</div>

## 12 ｜ 12:24　与 AI 领导者联合设计

![Helios: High-Performance Rack Co-Engineered with AI Leaders — AMD + Meta + Open，Open Rack Wide / OCP Power Shelves / OCP GPU Management](images/13_12m24s.jpg)

整机架接近 7,000 磅。所以它确实是台不小的机器。George 说过类似"人随着年龄增长都会变宽一点"的话——我不想这样形容我们的机架，但我要说，我们在 Helios 上做了一个非常刻意的选择：采用 OCP Open Rack Wide 标准。

这是我有幸参与过的、最具雄心的工程之一。它是与我们的伙伴 Meta 联合设计的，稍后你们会听到 Santosh 的分享。我必须说，这是一段非常好的合作关系。

我们的出发点是：未来会有很多种加速器，没有一招通吃，也没有哪家公司拥有所有最好的部件。我们要做的是让异构数据中心环境变得非常容易——因为我们坚信，你会需要 CPU、GPU 和专用 ASIC 的混合。

> And the total rack is nearly 7,000 lb. So, it's a little bit of a machine. I think George said something like everyone gets a little wider as the years pass. I don't want to say that about our racks, but I would say we made a very deliberate choice with Helios to use the OCP Open Rack Wide standard. It is one of the most ambitious engineering feats that I've ever had a chance to be part of in my career. This was co-engineered with Meta, our partner. And we started with the notion of — look, there're going to be a lot of accelerators out there. It is not one-size-fits-all. It's not that one company has all the best parts. What we want to do is make it really easy for a heterogeneous data center environment, because there's a firm belief that you're going to need a mix of CPUs, GPUs, purpose-built ASICs.

<div class="takeaway"><b>小结</b>　整机架近 7,000 磅；关键决策是采用 OCP Open Rack Wide 而非自有机架，与 Meta 联合设计——目标是"换加速器不必换机架"。</div>

## 13 ｜ 13:54　网络：三条链路、五个伙伴

![Helios: High-Performance Networking Delivered Through An Open Ecosystem — Front-End / Scale-Up（UALoE、ESON）/ Scale-Out（UEC、MRC、MetaRoCE）](images/14_13m54s.jpg)

它们会希望处在相似的数据中心环境里。你不会希望每次更换加速器就换掉所有部件。你会尽量把能标准化的部分标准化，只在真正产生差异的地方做差异化。

这正是我们与 Meta 一起在 Helios 平台上做的事。我认为这里有一个把生态聚起来的巨大机会。要让 Helios 成为现实，需要非常多的伙伴，包括机架层面的开放架构、开放式电源架、开放网络，以及整体的管理系统。我们对 Helios 的进展非常满意。

作为其中一部分，网络是这个生态里极大的一块。我们内部花了相当多时间——负责数据中心方案的 Norrod 团队——来架构这件事。但我们的原则是：要用当时可用的最好方案。而"最好"意味着把世界上最领先的网络伙伴拉进来。我们与 Broadcom、Cisco、Arista、HPE、DriveNets 有大量合作。

> They're going to want to be in a similar data center environment. You're not going to want to switch out every component every time you change an accelerator. You're really going to try to standardize as much as you can, so that you are differentiating on the things that make the most difference. And that's exactly what we've done with the Helios platform together with Meta. I think what we see here is a tremendous opportunity to bring the ecosystem together. Lots and lots of partners are needed to make Helios happen, but it includes the open architecture on the rack standpoint, open power shelves, open networking, and the overall management system. As part of this, networking is a huge piece of this ecosystem. Our principle is we wanted to use the best solution that was available, and that would mean bringing in the leading networking partners in the world. We're doing tremendous work with Broadcom, Cisco, Arista, HPE, DriveNets.

<div class="takeaway"><b>小结</b>　网络分三层交付：前端、Scale-Up（UALoE/ESON）、Scale-Out（UEC/MRC/MetaRoCE），全部走 OCP 生态，而非 AMD 自研闭环。</div>

## 14 ｜ 14:42　ROCm 与开放软件

![ROCm: High-Performance Software Powered By An Open Ecosystem — 前 15 大开源 AI 社区原生支持 AMD](images/15_14m42s.jpg)

目标是拥有领先的前端方案、领先的 Scale-Up 方案（UALink over Ethernet 以及 ESON），以及领先于行业的 Scale-Out 方案。所有这些都通过 OCP 开放生态交付。

而这种开放性同样延伸到软件。软件层面的想法是：我们要确保客户能非常容易地把新工作负载搬到我们的加速器上。要做到这一点，你需要让最领先的开放社区原生运行。我们有排名前 15 的开放 AI 社区原生支持 AMD。

> To have leading front-end solutions, leading scale-up solutions with UALink over Ethernet as well as ESON, and then leading scale-out solutions as well that are ahead of the industry. And all of this is delivered through the OCP open ecosystem. And all of this openness extends to software as well. The idea of software is, we need to make sure that it's super easy for our customers to bring new workloads onto our accelerators. And to do that, you want to have the leading open communities running natively. We have the top 15 open AI communities that are supporting AMD natively.

<div class="takeaway"><b>小结</b>　软件层的关键指标不是自研框架数量，而是"前 15 大开源 AI 社区原生支持 AMD"——用生态覆盖度替代单点性能叙事。</div>

## 15 ｜ 15:51　交付指标：三项第一与 30%

![AMD Helios Delivers Leadership Rack-Scale AI Solution：2.9 EF FP4 / 31TB HBM4 / 260TB/s Scale-Up，Up to 30% More Tokens/$，17,000 tokens/s/GPU](images/16_15m51s.jpg)

我们看到了显著的收益。这也许是我们在 AI 上看到的最大收益之一——智能体 AI 可以持续让硬件性能变得更好。

举一个数字：Hyperloom 是我们的智能体 AI 方案，我们让它持续对 Hugging Face 上的模型运行。超过 14,000 个模型、全程无人在环，仅仅因为智能体在跑，我们就看到了接近 40% 的性能提升。

所以关键在硬件与软件的开放生态，它把显著性能提升的机会带给最终用户。那么把这一切合起来，对最终用户意味着什么？

Helios 机架带来业界最高的算力、最高的内存容量、最高的内存带宽、最高的网络能力。给一些数字上的概念：我们相信这转化为每美元 Token 数提升 30%。

> We have seen significant benefit. Perhaps this is one of the largest benefits that we've seen of AI — this is a case where agentic AI can actually continue to make the performance of the hardware better over time. Just to give you one statistic: Hyperloom is our agentic AI solution, and we've had it running continuously for the Hugging Face models. Over 14,000 models on Hugging Face with no humans in the loop, we've seen almost a 40% improvement in performance just having the agentic AI run. So, the key is open ecosystems on hardware and software, bringing the opportunity to get significant performance capability to our end users. So, if you take a look at all of those pieces, what does that mean to the end user? The Helios rack delivers the highest compute in the industry, the highest memory capacity, the highest memory bandwidth, and the highest networking capability across the industry. And to give you some idea of the numbers, we believe that we're translating into 30% more tokens per dollar.

<div class="takeaway"><b>小结</b>　自证式案例：Hyperloom 对 14,000+ 个模型无人值守调优，带来约 40% 性能提升；对客户则表述为 30% 的每美元 Token 数提升。</div>

## 16 ｜ 16:39　从幻灯片转向实拍

![Helios Deployments Underway at Leading AI Customers（现场团队与部署实景）](images/17_16m39s.jpg)

所有这些 PPT 听起来都不错。不过看几张照片可能更好。让我给你们看一点东西。

> Now, all the PowerPoint sounds great. It's probably better to see a few pictures. So, let me show you a little bit here.

<div class="takeaway"><b>小结</b>　从参数叙事切到现场实拍，是这类发布演讲中建立可信度的常见手法——"PPT 说得再好，不如看照片"。</div>

## 17 ｜ 16:57　量产与首批客户

![Helios Deployments Underway at Leading AI Customers：OpenAI、Meta、Anthropic、Microsoft、Oracle](images/18_16m57s.jpg)

有人告诉我，机架级方案会是我们做过最难的事。我想他们完全说对了。Helios 绝对是我们在 AMD 与伙伴一起构建过的、最复杂精密的系统。

但我很高兴地说，Helios 今天已经在量产。我们在 9 月开始出货。第一批系统已经安装在我们的领先客户那里：OpenAI、Meta、微软、Oracle、Anthropic。

当我们把这些拼在一起时，我们持续看到大量的经验积累。

> People told me that rack-scale solutions would be the hardest thing that we've ever done. I think they were absolutely right. Helios is absolutely the most sophisticated and complex system that we have built at AMD together with our partners. But I'm very happy to say that Helios is in production today. We started shipping production in September. The first systems are installed at our leading customers — OpenAI, Meta, Microsoft, Oracle, Anthropic — and we continue to see just tremendous learnings when we bring all of these pieces together.

<div class="takeaway"><b>小结</b>　7 月发布、9 月量产，首批落地五家头部客户——从发布到出货仅两个月，这是本场最硬的时间线。</div>

## 18 ｜ 17:54　采用面正在扩大

![AMD Helios: Growing Adoption By AI Leaders（OpenAI、Meta、Anthropic、Microsoft、Oracle、xAI、Dell、HPE、Lenovo、Supermicro 等）](images/19_17m54s.jpg)

我们的量产会在第四季度持续爬坡，并延续到明年上半年。我们与伙伴在 OCP 标准上所做的，整体上是非常出色的工程。

我很高兴地说，Helios 的采用正在显著扩大——不只是最大的模型公司，还包括一批 AI 原生公司，以及整个生态里的 ODM、OEM。我知道你们中有不少今天就在台下。还有 Neocloud 的朋友们，谢谢你们，谢谢你们在 Helios 上的所有协作。

未来几个季度我们会继续扩展这件事。

> So, our production will continue to ramp through the fourth quarter into the first half of next year, but what we did with the OCP standard, working together with our partners, was just fantastic engineering overall. I'm happy to say there's significant growing adoption of Helios — not only the largest model companies, but in addition a number of AI native companies, a number of the overall ecosystem ODMs, OEMs. I know a bunch of you are in the audience today. Neoclouds, thank you for all of the collaboration on Helios. We're going to continue to broaden this going forward as we think about the next few quarters.

<div class="takeaway"><b>小结</b>　采用面从五家头部客户扩散到 AI 原生公司、ODM/OEM 与 Neocloud，说明 Helios 已进入生态供给阶段，而不只是样板工程。</div>

## 19 ｜ 18:24　转入智能体基础设施

![AMD × OCP：Collaboration at Scale（过渡页）](images/20_18m24s.jpg)

接下来，我想转到智能体基础设施。

我要说，这大概是过去——我们称之为——六个月里活动最密集的地方。关于智能体有很多讨论，我认为这种兴奋是真实的。

> So, with that, maybe I'll transition a little bit to agentic infrastructure. And I would say that this is probably the place where there has been the most activity over the last, let's call it 6 months or so. There's been a lot of talk about agents. I would say the excitement is real.

<div class="takeaway"><b>小结</b>　下半场主题切换：过去半年变化最快的不是芯片，而是智能体带来的负载形态。</div>

# 第二部分　智能体基础设施

## 20 ｜ 19:12　高并发智能体时代

![Entering an Era of High-Volume Agentic Usage：Meta Muse 5 Million Downloads、OpenAI 10,000 Agents（Navier-Stokes）、Anthropic 30,000 R&D Agents](images/21_19m12s.jpg)

我想我们都看到了巨大的生产力提升，无论是个人场景还是企业场景，而且它推进的速度比我们想象的快得多。

有几个例子挺有意思。Muse 重新点燃了人们对"AI 能为消费者做什么"的想象。Meta Muse 的 500 万次下载是截至 9 月底的数字，也就是头几周。今天早上我在《华尔街日报》读到，首月左右已经达到 900 万次下载。

OpenAI 谈到用 10,000 个智能体去攻克历史上一些最难的数学问题，那些问题此前并没有真正看到完整解。Anthropic 则谈到用研发智能体去……

> I think we've all seen just tremendous productivity, whether in personal use cases or in enterprise use cases, and it's moving much faster than we thought. Some of the examples out there are pretty interesting. Muse has kind of recaptured the imagination as to what AI can do for the consumer. This number of 5 million downloads of Meta Muse was as of the end of September — that was like the first couple of weeks. I think I read this morning in the Wall Street Journal that they're up to 9 million downloads of Meta Muse in just the first month or so. OpenAI has talked about using 10,000 agents to solve some of the most difficult math problems in history that haven't really seen the full solution. Anthropic talks about using R&D agents to...

<div class="takeaway"><b>小结</b>　三个案例共同证明"智能体已是产能而非演示"：消费端 900 万下载、科研端 10,000 个智能体攻关千禧年难题、研发端 30,000 个智能体构建下一代模型。</div>

## 21 ｜ 20:15　智能体需要匹配的算力

![Agents Need the Right Compute：Personal Agents / Enterprise Agents / Technical Compute Agents](images/22_20m15s.jpg)

……真正把四元数跑起来。所有这些都说明，智能体使用是真实的。

我可以告诉你们，AMD 内部正在积极使用智能体，既用在芯片开发，也用在软件开发上。我刚才举了 Hyperloom 的例子。

那么你会问："好吧，人人都在谈智能体，但智能体到底需要什么？"我认为最重要的一点是：智能体其实不是一种东西。智能体就像人一样，有很多不同类型。你需要为合适的应用配上合适的智能体，而为此，你实际上需要合适的算力。

所以谈到个人智能体，你大概想要尽可能高的密度。这些是更简单的任务，你希望它们非常高效，希望每瓦能跑最多的智能体，这样你的电力才用得对。

再谈企业智能体，你要做很多不同类型的活动，所以你希望它们比较均衡。

> All of these say that agentic usage is real. I can tell you, within AMD we're actively using agents both on our silicon development as well as on our software development. I gave you the example of Hyperloom. So, you say, "Okay, everyone talks about agents, but what do you actually need for agents?" And I think the most important thing to realize is that agents actually are not one thing. Agents, like people, there are lots of different types of agents. You need the right agents for the right application. And for that, you actually need the right compute. So, when you're talking about personal agents, you probably want the densest agents possible. These are simpler tasks, and you want them to be very efficient. You want them to be maximum number of agents per watt, so you are saving your power correctly. You talk about enterprise agents, where you're doing a lot of different types of activities, so you want them to be pretty balanced.

<div class="takeaway"><b>小结</b>　三类智能体对应三种算力取向：个人智能体要密度与每瓦数量，企业智能体要均衡，技术计算智能体要极致性能。</div>

## 22 ｜ 20:54　智能体也需要匹配的机架

![And Agents Also Need the Right Rack：HYPERSCALE Disaggregated Agentic Rack / ENTERPRISE All-In-One Agentic Rack](images/23_20m54s.jpg)

或者你谈的是最难的算力问题，也就是技术计算智能体。你会希望它们有最前沿的性能，最好的那一档。

所以每一种智能体都需要不同类型的算力。而且我们认为，每一种智能体也需要合适类型的机架。这意味着在超大规模环境里你会看到一种机架形态——CPU 与 GPU 机架解耦部署；而在企业场景，未来你可能更希望看到一体式机架。

所以我很高兴地说，今天上午我们发布了 AMD Helion 智能体 AI 机架。

> Or you're talking about some of the hardest compute problems out there — these technical compute agents. You're going to want them to have bleeding-edge performance, the best of the best. So, each of these agents needs a different type of compute. And what we believe is each of these agents also needs the right type of rack. And that means you're going to see a certain type of rack in hyperscale environments, where you might have disaggregated CPU and GPU racks, whereas in enterprise you might want to see more all-in-one racks going forward. So, I'm happy to say this morning, we announced the AMD Helion Agentic AI Rack.

<div class="takeaway"><b>小结</b>　机架形态随负载分叉：超大规模用 CPU/GPU 解耦机架，企业用 CPU+GPU 一体机架。</div>

## 23 ｜ 21:39　Helion：Helios 的"表亲"

![TODAY: AMD Helion Agentic AI Rack — Match your CPU compute to your agentic workloads / Choose any combination of CPU & GPU nodes / Integrated token router / Open hardware & open software](images/24_21m39s.jpg)

Helion 是 Helios 的表亲，它真正聚焦在智能体 AI 算力这一面。

我们想做的，坦白说，是把 Open Compute 基础设施的所有部件用最简单的方式拼起来，从而得到最高效的 CPU 机架。所以你可以用 CPU 和 GPU 的组合。我们还把它与 token router 集成在一起。我想大家都在讨论，怎样才能最有效率地路由你的 AI 用量。

> Helion is the cousin to Helios. And it's really focused on the agentic AI compute aspect of it. What we're trying to do here is frankly do what is easiest in terms of bringing all of the pieces of the Open Compute infrastructure together, so that we can get the most efficient CPU racks. So, you can use a combination of CPUs and GPUs. We're also integrating it with a token router. I think everyone is talking about how can you most efficiently route your...

<div class="takeaway"><b>小结</b>　Helion 与 Helios 的分工清晰：Helios 是 GPU 主导的机架，Helion 是 CPU 主导的机架；后者首次把 Token Router 做进机架设计。</div>

## 24 ｜ 22:36　Helion 的规格

![AMD Helion Agentic AI Rack：Up to 32,768 Zen 6、Up to 16 MI350P、Up to 102 Tbps Networking、ORv3 440U](images/25_22m36s.jpg)

……整体 AI 用量。我知道在我们自己的 IT 基础设施里，思路就是：你不需要对每个问题都用同一个模型，也不需要为每个问题用同样的算力。你希望能够为合适的应用路由合适的模型和合适的算力。这是这套方案的关键一环，也是整体开放环境的关键。

关于我们的 Helion 智能体 AI 机架，有几件事。Helion 的好处是，我们尽可能把能用的 OCP 规范全都用上了：它是标准的 21 英寸机架，可以液冷也可以风冷，最高支持 32,000 多个 Zen 6 核心，比同类竞争机架多 40%。

> I know that within our own IT infrastructure, the idea is you don't need the same model for every question. You don't need the same compute for every question. You want to be able to route the right model and the right compute for the right application. And that's a key piece of this, as well as the overall open environment. A few of the things about our Helion Agentic AI Rack — the nice thing about Helion is we've used practically everything that we could through OCP specs, with the idea of it's a standard 21-inch rack. It can be liquid or air cooled. It is up to 32,000 plus Zen 6 cores, which is 40% more than the other competitive racks.

<div class="takeaway"><b>小结</b>　幻灯片标注 32,768 个 Zen 6 核心、最多 16 颗 MI350P、102 Tbps 网络；口播说"32,000 多个"和"32 颗 MI350P"，两者在加速器数量上有出入，以幻灯片为准。</div>

## 25 ｜ 23:27　超大规模配置

![AMD Helion Agentic AI Rack – Hyperscale Config：Personal / Enterprise / Technical Agents，Mix and Match CPU Nodes](images/26_23m27s.jpg)

它是业界最高的计算密度。它还能容纳最多 32 颗 Instinct MI350P GPU，以及非常强的网络能力。所以这一切都汇聚到一个开放的算力标准里。

看我们预期它们如何被使用：在超大规模配置下，考虑到超大规模的算力密度，你会想象数据中心的一部分部署大量 GPU 机架，但你的智能体 CPU 机架可以就摆在旁边，而且可以在其中混插不同类型的 CPU 节点。所以无论你看的是个人智能体、企业智能体还是技术计算智能体，你都能为合适的工作负载挑到合适的算力。

> It's the highest compute density in the industry. It also can hold up to 32 Instinct MI350P GPUs, as well as a tremendous amount of networking capability. So, it's all coming together in an open compute standard. When you look at how we expect these to be used — when you start in a hyperscale configuration, given the density of compute in hyperscale, you would imagine that you would have significant GPU racks in one portion of the data center, but you can have your agentic CPU racks really sitting side by side, and you can mix and match the type of CPU nodes in it. So, whether you're looking at personal agents or enterprise agents or technical agents, you can pick the right compute for the right workload.

<div class="takeaway"><b>小结</b>　超大规模场景下 Helion 是纯 CPU 的智能体机架，与 GPU 机架并排部署，按智能体类型混插节点——这是"解耦"的具体形态。</div>

## 26 ｜ 24:06　企业配置

![AMD Helion Agentic AI Rack – Enterprise Config：Agentic Node（CPU "Sandbox"）、Inference Node、General Purpose Node](images/27_24m06s.jpg)

而在企业配置下，你实际上可以再加上一块：很多企业大概并不运行最先进的基础模型——至少在他们本地部署时是这样。他们可能更希望有能力把 CPU 和 GPU 放进同一个机架，针对自己的特定工作负载做优化。这就是 Helion 机架能做的事。

> And in the enterprise configuration, you can actually add another piece of this — a lot of enterprises are probably not running the most advanced foundational model, at least when they're running them on prem. They could be actually wanting to have the ability to have both CPUs and GPUs in the same rack, optimized for their particular workload. And so, that is what we can do with the Helion rack.

<div class="takeaway"><b>小结</b>　企业配置把 CPU 与 GPU 收进同一机架，前提判断是"企业本地往往不跑最前沿模型"，因此更看重按自身负载配比而非峰值性能。</div>

## 27 ｜ 24:24　供货与生态

![AVAILABLE NOVEMBER '26：AMD Helion Agentic AI Rack，Contributing to OCP，Dell / HPE / Lenovo / Supermicro / Asus / Gigabyte 等伙伴](images/28_24m24s.jpg)

我很高兴地说，我们的智能体机架得到了非常积极的回应。所以有两点：一是我们有一个丰富的生态，从 11 月 26 日起提供 Helion 机架；二是所有这些都会贡献给 OCP。非常期待。

好，在最后几分钟，我想给大家更新一下我们的芯片进展。

> I'm happy to say that there's been tremendously positive response to our agentic rack. So, two pieces: one is we have a rich ecosystem that are offering the Helion rack starting November 26th, and all of this is going to be contributed to OCP. So, very excited for that. Okay, so in the final few minutes, I thought I would just give you an update on our silicon.

<div class="takeaway"><b>小结</b>　"11 月供货 + 贡献给 OCP"是同一句话的两半：既给出商业化时间点，又把规格交出去，换取生态供给。</div>

# 第三部分　CPU 路线图与收尾

## 28 ｜ 25:06　EPYC "Venice" 家族

![EPYC "Venice"：The Best Server CPU Portfolio for Agentic Racks — Host Node / Agent CPU Servers / General Purpose](images/29_25m06s.jpg)

我们始终在推动芯片的最前沿，就像我说的。7 月我们谈过 Venice 产品组合，我们认为这是智能体机架最好的服务器 CPU 组合，因为我们有能力真正按工作负载混搭。

我们谈过 Venice 的各种形态：用于智能体 CPU 服务器的"主力"——Venice 256 核；用于通用 CPU 服务器的型号；以及用于主机节点的 Venice 高频版。

这些都很好。但 7 月见到你们时，我展示了四块芯片，今天我们有一些新芯片要给你们看。让我展示一下。

> We are always pushing the bleeding edge of silicon, as I said. In July, we talked about our Venice portfolio, and we believe these are the best server portfolio for agentic racks because we have the ability to really mix and match for the right workload. We talked about the various flavors of Venice, including our workhorse for agentic CPU servers, the Venice 256 core, our general purpose CPU servers, as well as our CPUs for host nodes, the Venice high frequency. And all of that is great, but when I saw you in July, I showed you four pieces of silicon, and we have some new silicon to show you today. So, let me show you.

<div class="takeaway"><b>小结</b>　Venice 家族按"位置"分工：主机节点用高频版（及 Verona），智能体沙箱用 256 核，通用服务器用 SP7/SP8/Venice-X。</div>

## 29 ｜ 25:45　首次展示 EPYC "Verona"

![苏姿丰在台上举起 EPYC "Verona" 芯片](images/32_25m45s_verona_live.jpg)

来了。这是我们的新芯片 EPYC Verona。

Verona 基于 Venice 家族的 CPU 核心。这一款实际上是为最低系统功耗优化的，所以它有六个 CCD，也就是六个 CPU 核心 die，每个 32 核，最高 192 核。同时我们也更新了 CPU 到 GPU 的带宽，这让它特别适合主机节点方案。

所以 Verona 看起来非常出色。围绕 Verona 以及 Venice 家族其余型号，大家都很兴奋，我们将在 2027 年上半年量产。

> Here we go. This is our new EPYC Verona. Verona is based on the Venice family of CPU cores. This guy is actually optimized for the lowest system power, so it actually has six CCDs, or six CPU core dies, that have 32 cores each — up to 192 cores. And with that, we've also updated the CPU to GPU bandwidth, which makes it exceptionally good for head node solutions as well. So, Verona looks fantastic. There's a lot of excitement about Verona as well as the rest of the Venice family, and we will be in production in the first half of 2027.

<div class="takeaway"><b>小结</b>　Verona 是 Venice 家族中面向最低系统功耗与主机节点的型号：6 CCD × 32 核 = 最高 192 核，2027 年上半年量产。</div>

## 30 ｜ 27:06　开放是每一个层面的

![Open Ecosystem Drives Innovation：Open Hardware + Open Software + Open Ecosystem](images/30_27m06s.jpg)

那么，让我做个总结。我想说：我们热爱 OCP，我们热爱开放生态。开放是 AMD 所关心之事的基础。

它在每一个层面都是开放的：硬件层面开放，规格开放，与伙伴协作开放，软件层面也开放——与所有软件厂商合作，确保我们把这一切整合起来；生态层面同样开放。

> So, with that, let me conclude and say: look, we love OCP. We love the open ecosystem. Open is a foundation for what we care about at AMD. It is open on every level. It's open on the hardware level. It's open with specs. It's working with our partners. It's open on the software level, working with all of the software vendors to ensure that we are bringing that together. And it's open on the ecosystem side as well.

<div class="takeaway"><b>小结</b>　"开放"在这里被拆成四个可检验的层面（硬件、规格、软件、生态），而不是一句态度表述。</div>

## 31 ｜ 27:18　收尾

![Collaboration at Scale: Delivering the Next Era of AI Infrastructure — Leadership Components / Flexible, Open Platforms / Integrated Rack Solutions](images/31_27m18s.jpg)

我很高兴地说，我们的很多伙伴本周都在 OCP 现场。看到这些工作汇聚起来，看到把团队聚到一起所带来的收获，我觉得非常棒。

所以我要再次感谢 OCP，真正促成了这件事——我称之为"规模化的协作"。它让我们每个人都能在自己最擅长的地方创新，也让我们每个人都能把行业里的所有部件聚到一起，从而更快地把方案推向市场。

那么，谢谢大家。祝 OCP 愉快。

> So, I'm very happy to say a lot of our partners are here at OCP this week. I think it's fantastic — all of the work that's coming together and all of the learnings that we will get from bringing the teams together. So, again, I want to say a big thank you to OCP for really bringing together this, what I would call collaboration at scale. It's an opportunity for each of us to innovate on the things that we're best at, and also for each of us to bring together all of the components across the industry so that we can get solutions to the market faster. So, with that, thank you very much. Have a great OCP.

<div class="takeaway"><b>小结</b>　收尾把全场落成三句话：领先的部件、灵活开放的平台、集成式机架方案；而"规模化的协作"是它们能同时成立的前提。</div>

---

# 附录 A　关键数据速查

以下数字均取自幻灯片标注；仅存在于口播的数字已单独标注。

| 指标 | 数值 | 来源 |
|---|---|---|
| 月度 Token 消耗增长（近两年） | 95 倍 | 幻灯片 |
| 月推理 Token 规模 | 约 40 万亿亿（4×10¹⁶） | 口播 |
| 训练算力增速 | 每年 5 倍（自 2020 年） | 幻灯片 |
| 推理占 AI 市场比重（2026） | 约 60% | 口播 |
| 智能体流量增长（2026 年初至 8 月） | ≥14 倍 | 幻灯片（OpenRouter） |
| 数据中心 CPU TAM（2025 → 2030） | 260 亿 → 约 2,200 亿美元 | 幻灯片 |
| CPU TAM 年复合增速 | >50% | 幻灯片 |
| AI 加速器 TAM（2025 → 2030） | 2,000 亿 → 约 1.4 万亿美元 | 幻灯片 |
| AI 加速器 TAM 年复合增速 | >45% | 幻灯片 |
| Helios GPU 数量 | 72（作为单一加速器） | 口播 |
| Helios 算力 | 2.9 EF FP4 / 1.48 EF FP8 | 幻灯片 |
| Helios 内存 | 31 TB HBM4，1.7 PB/s | 幻灯片 |
| Helios 网络 | 260 TB/s Scale-Up，43 TB/s Scale-Out | 幻灯片 |
| Helios 每美元 Token 提升 | 最高 30% | 幻灯片 |
| DeepSeek R1 推理性能 | 17,000 tokens/s/GPU | 幻灯片（AMD 实测 MLPerf） |
| Helios 计算托盘 / 整机架重量 | 160 磅 / 约 7,000 磅 | 口播 |
| Hyperloom 自动调优提升 | 约 40%（14,000+ 模型，无人在环） | 口播 |
| Helion CPU 核心 | 最高 32,768 个 Zen 6 | 幻灯片 |
| Helion GPU | 最高 16 颗 MI350P（74 PF FP4） | 幻灯片 |
| Helion 网络 | 最高 102 Tbps | 幻灯片 |
| Helion 机架 | ORv3 440U | 幻灯片 |
| Verona 核心 | 6 CCD × 32 核 = 最高 192 核 | 口播 |
| Verona 量产 | 2027 年上半年 | 口播 |

# 附录 B　时间轴

| 时间 | 内容 |
|---|---|
| 00:09 | 开场，首次参加 OCP 全球峰会 |
| 01:21 | 没有一家公司能回答所有问题 |
| 02:18 | 与 OCP 协作的十五年 |
| 03:27 | AI 正在改造每一个行业 |
| 04:06 | 需求加速：95 倍 |
| 05:21 | 推理成为第一大工作负载 |
| 06:57 | CPU 与加速器 TAM 同步上修 |
| 08:51 | 三大战略支柱 |
| 09:45 | 协作的规模 |
| 10:24 | 前沿 AI 需要集成式机架 |
| 11:21 | Helios 登场 |
| 12:24 | 与 AI 领导者联合设计 |
| 13:54 | 网络：三条链路、五个伙伴 |
| 14:42 | ROCm 与开放软件 |
| 15:51 | 交付指标：三项第一与 30% |
| 16:39 | 从幻灯片转向实拍 |
| 16:57 | 量产与首批客户 |
| 17:54 | 采用面正在扩大 |
| 18:24 | 转入智能体基础设施 |
| 19:12 | 高并发智能体时代 |
| 20:15 | 智能体需要匹配的算力 |
| 20:54 | 智能体也需要匹配的机架 |
| 21:39 | Helion：Helios 的"表亲" |
| 22:36 | Helion 的规格 |
| 23:27 | 超大规模配置 |
| 24:06 | 企业配置 |
| 24:24 | 供货与生态 |
| 25:06 | EPYC "Venice" 家族 |
| 25:45 | 首次展示 EPYC "Verona" |
| 27:06 | 开放是每一个层面的 |
| 27:18 | 收尾 |

# 附录 C　资料来源与处理说明

- 视频：https://www.youtube.com/watch?v=3nFDQMaoNKc（Open Compute Project 频道）
- 字幕：YouTube 自动生成英文字幕，经去重、按语义分段后与幻灯片时间窗对齐
- 图片：从 1080p 原片按幻灯片切换点抽取，共 31 张幻灯片 + 1 张现场画面
- 英文原文已去除 um、uh 等填充词，并修正 ASR 明显错误（EPYC、agentic、OCP、Norrod 等）
- 中文译文以传达原意为准，未作压缩；括号内为译者补充的上下文
- 数字口径：幻灯片标注值优先，口播数字单独标注

---

*本文档为视频内容实录整理，用于信息参考。技术参数与商业表述以 AMD 官方发布为准。*
