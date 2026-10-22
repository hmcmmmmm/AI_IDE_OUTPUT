# 为智能体 AI 构建开放的异构基础设施

> OCP Global Summit 2026 · 英特尔主题演讲
> 讲者：Anil Nanduri（英特尔数据中心事业部 AI 产品与 GTM 副总裁）
> 嘉宾：Pravin Patel（Astera Labs）· Neil Movva（Sail Research）
> 全长 19 分 53 秒　|　共 16 页幻灯片

```wechat-intro
英特尔这场 20 分钟的演讲，其实在回答一个问题：当推理负载本身变成异构的，基础设施该怎么办？

答案是三件套——至强当"四分卫"做编排和沙箱执行，Crescent Island（正式名 Intel GPU D 系列）做低功耗大内存的 token 生成，中间用 PCIe 而不是专用互连把 8 张卡扩成 80 张。第 03 节那三张图解释了"异构"为什么不是厂商话术；第 08、12 节是硬件参数和互连细节；第 13 节有个数字对不上，值得看一眼。
```

---

## 01　开场：异构不是选择，是负载本身的样子

![标题页：Building Open Heterogeneous Infrastructure for Agentic AI，讲者 Anil Nanduri，VP, AI Products & GTM, Data Center - Intel](images/01_00m25s.jpg)

好。下午好，各位，欢迎来到 OCP 2026。非常高兴能站在这里。今天你们从英特尔这里会听到的——以及我们请到的几位合作伙伴嘉宾会讲的——是关于 AI 推理正在发生什么，以及异构系统为什么会成为承载这些推理负载的基础；而在智能体（agentic）世界里，这些负载本身正变得越来越异构。英特尔为这种必需的能力提供了什么方案？我们又在开放生态里和合作伙伴一起做了什么，来帮助你们所有人构建面向这个令人兴奋的未来的方案？

> "Okay. Good afternoon, folks, and welcome to OCP 2026. Super excited to be here. And what you'll hear from Intel today, along with some exciting guests from our partners that we have, is around what's happening in AI inference. And how heterogeneous systems are going to be the foundation for making these inference workloads, which are becoming more and more heterogeneous in the agentic world. What is Intel delivering solutions for this capability that is required? And what are we doing with our partners in the open ecosystem in enabling you all in building solutions for this exciting future?"

<div class="takeaway"><b>小结</b>　开场就把论点摆出来了：不是"英特尔也来做 GPU"，而是"推理负载本身是异构的，所以基础设施必须是异构的"。后面十五页都在给这一句话补证据——三张经济学图表、一个四层架构、三颗 CPU、一颗 GPU、一颗交换芯片。</div>

---

## 02　116 与 33：英特尔在 OCP 里的位置

![Open Communities：intel × Open Compute Project，四个板块为 Open hardware / Open software / Open interfaces / Open infrastructure；下方两个数字牌 116 Contributions made to OCP、33 Sessions at this Global Summit，副标注 Across 13 tracks](images/02_01m00s.jpg)

大家都知道，OCP 的根基是开放——用开放标准推动整个行业往前走。英特尔从 OCP 创立之初就是这个社区的一部分，我们提交了超过 116 项贡献。今年的 OCP，我们有 33 场以上的会议、分布在 16 个 track 里。好，那我们直接开始吧。

> "As you all know, OCP is anchored on being open. Open standards to move an entire industry forward. We Intel have been part of this community since its founding days. We've had over 116 contributions. And at this year in OCP, we have over 33 sessions across 16 tracks uh being presented. Now, let's jump straight into it."

<div class="takeaway"><b>小结</b>　这两个数字是英特尔在这场演讲里的"身份证明"——它不是在推销一颗芯片，而是在说"我是这个开放社区的长期出资方"。顺带记一处现场口误：幻灯片写的是 13 个 track，讲者口述成了 16 个。</div>

---

## 03　智能体把成本曲线掰弯了

![AI is reshaping AI infrastructure economics：左图 80x growth in active agents（2030）、5x inference cost / agentic workflow（2028）；中图 前沿模型占调用 7% 却占支出 68.4%，小模型占调用 93% 只占支出 10.4%，中间模型 21.2% / 21.2%；右图 Open Weight 调用占比 7 月 31% → 9 月 78%](images/03_01m50s.jpg)

大家都知道，AI 正在爆发，这个不用我多说。但真正在发生的是：智能体的兴起给生态带来了一个不一样的问题。所需的 token 数量在爆炸式增长。与此同时，交付这些智能体的成本也在爆炸式增长。所以，如果你想把这个生态继续往前推，就必须重新审视大规模交付 AI 推理的经济性。

另一个正在发生的趋势，是前沿模型与开放权重模型之间的关系。越来越多的模型正在变成开放权重，而且随着开放权重模型的能力越来越接近前沿模型，它们被使用的比例在急剧上升。事实上，对企业来说，它们需要做的基础 AI 工作里有越来越大的一部分，其实可以用开放权重模型来处理；只有更高端的那部分才需要前沿模型。

> "As you all know, AI is booming. I don't have to say much. But what's really happening there is the rise of agents is causing a different problem into the ecosystem. The amount of tokens that are needed is exploding. While at the same time, the cost of delivering these agents is also exploding. So, the economics of delivering AI inference at scale needs to be looked at if you want to kind of feed this ecosystem forward. The other trend that is happening is the frontier models versus open weight models. More and more models are becoming open weight and the ratio of open weight models being used is increasing dramatically as the capabilities of open weight models get closer to frontier models. In fact, for enterprises, more and more significant amount of the basic AI work that they need to do can actually be handled by open weight models, whereas the higher end of the models need the frontier models."

<div class="takeaway"><b>小结</b>　三张图三句话：智能体数量到 2030 年涨 80 倍、单条智能体工作流的推理成本到 2028 年涨 5 倍；企业 93% 的调用量给了小模型，却把 68.4% 的钱花在前沿模型上；开放权重的调用占比从 7 月的 31% 涨到 9 月的 78%。这三条合起来才是"异构"的商业理由——不是技术偏好，是账单结构。</div>

<div class="insight"><b>想法</b>　中间那张图是整场演讲最有说服力的一页，也是最容易被读反的一页。93% 的调用量走小模型、只花掉 10.4% 的钱，说明企业并不是"不知道该省钱"，而是"不知道该用哪个模型"——路由决策本身成了成本中心。这也正好解释了下一节为什么要把 CPU 拉回控制面：谁来做这个路由，谁就掌握了省钱的那把钥匙。而如果哪天真有一个足够好的路由器，前沿模型的 68.4% 支出会被压掉一大块，那才是对高端 GPU 需求真正的威胁。</div>

---

## 04　三个独立的旋钮：模型大小、上下文、TPOT

![AI workloads have three independent knobs：三维坐标系中三条轴分别为 Model Size / Intelligence、Context Size / KV Cache、TPOT / Latency，中心标注 Cost per Token、Energy per Token；左侧三条要点——Tune each dimension for the workload、Managing cost and energy、Build right sized AI](images/04_02m35s.jpg)

而且，这个 AI 生态里并不是所有 token 都一样。根据模型大小、根据延迟、或者根据 KV cache 的不同，要高效交付它所需要算力是完全不同的。这三个变量都已经被纳入考量，用来解决如何在规模上获得效率。

> "Now, not all tokens in this AI ecosystem are same. Based on the model size, based on the latency, or based on the KV cache, the computational requirements to deliver that efficiently is going to be very different. And all three variables have been factored in to figure out how do you get efficiency at scale."

<div class="takeaway"><b>小结</b>　三个轴互相独立，这是"异构"的技术定义：模型大小决定算力与显存，上下文长度决定 KV cache 容量与带宽，TPOT 决定互连延迟与批处理策略。三者不能用一个硬件配置同时最优，所以只能按负载配硬件——"Build right sized AI"。</div>

---

## 05　控制面回到 CPU：从 2:8 到 1:1

![Agentic AI Inference Datacenter Architecture — Right hardware for the right workload：自上而下 Control Plane（Orchestration, CPU，含 Classify workload / Route requests / Coordinate resources）、Data Plane（Token Generation: GPU 与 RDU）、Data Plane（Execute, CPU，含 CPU-native operations / Assemble response / Return to application）、底部 Network/Fabric Plane（PCIe / Ultra Ethernet / RoCE）与 Storage & Context Plane（Vector DB/RAG / Distributed KV Cache / Session Context）；中间标注 Agent loop](images/05_03m45s.jpg)

现在，当你看智能体架构时，有一件很有意思的事情正在发生：你怎么把负载路由到正确的硬件上去跑？到目前为止，我们一直在看的是怎么把 token 跑得更快——怎么造出更快的 token，也就是延迟更低的 token，并让每个用户对这些 token 获得巨大的交互性。但在智能体架构里，CPU 在几个方面扮演着非常非常重要的角色。

第一是决策树，那个四分卫。我要怎么路由、编排、交付这个智能体工作流？上面的安全、那套 harness 要怎么搭？我又怎么处理必须发生的 token 生成和 API 调用？然后，那些 API 调用、那些 token 的结果必须被执行、被沙箱化、被验证。CPU 越来越多地处在智能体回路里，去执行这些 LLM 输出的所有结果。

所以这显著提高了对 CPU 的需求，CPU 与 GPU 的比例也在上升。事实上，过去大约是 2:8，现在走向 1:4、1:2，某些场景里甚至是 1:1。

> "Now, when you look at the agentic architecture, there's something very interesting happening. How do you write uh route the workloads to run at the right hardware? More and more, up until now, we were all looking about how to run tokens faster. How do you create faster tokens, slower to I mean lower latency tokens, and generate a huge interactivity per user for those tokens. But more and more in the agentic architecture, the CPU plays a very, very important role in couple of areas. First, the decision tree, the quarterback. How am I going to route, orchestrate, and deliver the agentic workflow? The security, the harness that needs to be built on it. How do I able to then handle the token generation and the API calls that need to be happening? And then, the outcome of those API call of the tokens have to be executed, sandboxed, verified. And CPUs are more and more in the agentic loop executing to all the outcomes that are coming from these LLMs. So, this is increasing the demand on CPU significantly that the ratio of CPU to GPU is also going up. In fact, it used to be about 2:8, now going to 1:4, 1:2, and even in 1:1 in some scenarios."

<div class="takeaway"><b>小结</b>　这张四层图是整场演讲的骨架：控制面（编排）、数据面（生成）、数据面（执行）、以及底下的网络与存储上下文层。注意中间那个环形箭头"Agent loop"——它穿过的是两次 CPU：一次在环的入口做路由，一次在环的出口做沙箱执行。CPU:GPU 从 2:8 走到 1:1，说的就是这两个位置在膨胀。</div>

---

## 06　三颗至强，三种分工

![Intel Xeon CPUs for Agentic AI：左 Xeon 6+（Dense cores for throughput & efficiency，Up to 288 E-cores）、中 Xeon 6（Routing, co-serving and guardrails，Up to 128 P-cores）、右 Next Gen Xeon codenamed Diamond Rapids（Best single-thread performance，Up to 256 P-cores）](images/06_05m00s.jpg)

我们在英特尔一直是 CPU 负载系统的大规模构建者，我们从"CPU 是智能体时代的四分卫"这个前提出发。控制面就在这里。至强具备这些负载高效运行、高效编排、高效沙箱化所需要的全部能力。对英特尔来说，我们为客户、也为生态里的你们提供了非常多的选择去构建，我们在这方面的领导级产品有很长的历史。

面向智能体时代的 CPU，我们有至强 6+，能效核最多 288 核；有至强 6，提供编排和不同类型负载所需的核；还有即将到来的 Diamond Rapids，会给你 250 核——256 核，带来市场上最好的智能体性能之一。

> "Now, we at Intel have been huge builder of systems for the CPU workloads. And we start with the CPU as being the quarterback for this agentic era. This is where the control plane is. The Xeon has all the capabilities that are needed for these workloads to be running efficiently, to be orchestrated efficiently, and sandboxed efficiently. And for from Intel, we have significant number of choices for our customers and to you in the ecosystem to build upon. We have a rich history of delivering, you know, leadership products in these aspects. For the CPUs in the agentic era, we have our Xeon 6 Plus, the E-core with up to 288 cores. We have our Xeon 6 with the the cores needed for orchestration and for different kinds of workloads, and our soon upcoming Diamond Rapids CPU, which will give you 250 core 256 cores to give you the one of the best agentic performance you can in the market."

<div class="takeaway"><b>小结</b>　三颗芯片的定位是错开的，不是代际关系：6+ 用能效核堆吞吐（288 E-core，给沙箱执行），6 用性能核做路由与护栏（128 P-core，给控制面），Diamond Rapids 拼单线程（256 P-core）。换句话说，选型依据是"这段代码是并发多还是单线程紧"，不是"哪代更新"。讲者口述"250 core 256 cores"是现场自我纠正，以幻灯片为准。</div>

---

## 07　机架已经能买了

![Intel Xeon: Agentic AI Rack Ecosystem — Faster, safer, more predictable, and ready for your workload：ASRock Rack、ASUS、GIGABYTE、MiTAC、MSI、Supermicro 六家机架，每台配二维码，标注 ORv3 OCP 与 Partners with solutions available today](images/07_05m55s.jpg)

而且，造这些东西的不只是我们。生态里的合作伙伴——我们在 Computex 上展示过——一大批合作伙伴在为这个智能体时代造至强服务器和机架。但更重要的是，今天我们真的有现成的机架，能满足这海量 token 被沙箱化、被执行所需的算力。这些至强智能体 AI 机架系统正由我们的合作伙伴部署。上面有二维码，可以带你们到产品页，你们能看到每个机架的能力——数万核，有些甚至超过 5 万核，其中很多是 ORv3 形态。

> "Now, it's not just us building these. Our partners in the ecosystem, we showed this at Computex, a wide range of partners building Xeon servers and racks for this agentic era. But more importantly, today we have actually racks available to meet the computational needs of these large volume of tokens that need to be sandboxed and executed. These Xeon agentic AI rack systems are being deployed by our partners. There are QR codes up there. They can take you to the product pages, and you can actually see the capabilities of each of these racks with tens of thousands of cores, even more than 50,000 cores, and many of them in a ORV3 form factor."

<div class="takeaway"><b>小结</b>　这是整场演讲里唯一"今天可以下单"的一页：六家 OEM，全部 ORv3 OCP 形态，都标着"Partners with solutions available today"。按 288 核/路、双路服务器算，"超过 5 万核"大约对应 90 台机器一个机架——这个密度只有在 350 W 级 CPU 和液冷/高风量机箱下才成立。</div>

---

## 08　Crescent Island 有了正式名字：Intel GPU D 系列

![INTEL GPU D-SERIES codenamed Crescent Island — Compute designed for inference：1311/2622 TFLOPS FP8/MxFP4、32 Xe-Cores（Xe3P GPU IP）、1.5TB/s Memory bandwidth、Up to 480GB LPDDR5x、256 XMX engines、16 deep systolic（XMX extensions）、350W Air-cooled PCIe、Day 0 Functionality；右侧为双槽被动散热卡渲染图，页脚注明零售 PCIe 卡为 160GB，ODM 可做到 480GB](images/08_06m40s.jpg)

现在，我们来看 token 生成这一侧。大家都知道，GPU 一直是规模化创建和运行 LLM 的基础。今天，我们很兴奋地谈一个新产品——Crescent Island，这是我们一直用的代号，正式产品名是我们的 Intel GPU D 系列。

这颗 GPU 刚从晶圆厂回来。这就是我手里的 Crescent Island，这颗 SoC。它是为智能体推理而造的：低功耗、很大的内存容量、极好的带宽。而且，我们为什么不看看它跑起来？有多少人想看它跑起来？

> "Now, let's get to the token generation side of it. As you all know, GPUs have been the foundation for creating and running LLMs at scale. Today, we are excited to talk about a new product, Crescent Island, which was the code name we've been using so far, and the product name officially is our Intel GPU D-series. Now, this GPU is come back from the fabs. This is Crescent Island in my hand, the SOC. It is built for the agentic inference with low power, significant amount of memory capacity, extremely good bandwidth, and actually, why don't we see this working? How many of you want to see it working?"

<div class="takeaway"><b>小结</b>　参数按重要程度排：1.5 TB/s 带宽、最多 480 GB LPDDR5X（带 ECC）、350 W 风冷 PCIe、FP8/MxFP4 1311/2622 TFLOPS。注意页脚那行小字——零售 PCIe 卡是 160 GB，480 GB 是留给 ODM 做定制卡的上限。整场演讲反复出现的"350 瓦"，就是靠 LPDDR5X 而不是 HBM 换来的。</div>

---

## 09　现场跑一个 270 亿参数的视频模型

![演示画面：Intel GPU D270 - Powering Generative Video，Wan2.2 T2V-A14B on a single card；界面显示 DENOISE 阶段、in progress、GENERATING 480P · 5 S ON THE CARD、1:23 Elapsed，底部档位为 480p 5s / 480p 10s / 720p 5s / 720p 10s / 1080p 5s / 1080p 10s](images/09_07m40s.jpg)

好。我们这里跑的是 VAE 模型，一个视频生成模型。它是一个 270 亿参数的模型，本质上是文生视频。它已经启动了，接下来会跑起来，并从中生成一段 5 秒的视频。

让 Crescent Island 出色的是，它支持最多 480 GB 带 ECC 的 LPDDR5X 内存。我们用来做演示的这张卡有 160 GB 内存。加上对各种数据类型的深度支持、1.5 TB/s 的内存带宽，这是一个非常灵活的、基于 PCI Express 的方案，可以支撑从小到大的各种形态，我后面会给你们看更多。

如你所见，这就是在 Crescent Island 上生成的视频。你们可以在展台看到更多，也可以在大会期间到英特尔展台试自己的提示词、生成视频。

> "Okay. So, what we are running here is the VAE model. It's a video generation model. It's a 27 billion parameter model that basically is a text-to-video. It's kicked off, and it's going to be running and creating a 5-second video out of this. Now, what makes Crescent Island great is that it has support for up to 480 GB of LPDDR5X memory with ECC. This card here that we are using for the demo has 160 GB of memory. Now, with deep amount of support for all kinds of data types, with 1.5 TB per second memory bandwidth, this is a very flexible PCI Express based solution that enables form factors from small to large, and I'll show you more about that. As you can see, that's a video generated on Crescent Island. You can see more at the booth, and you can try your own prompts and create videos at the Intel booth later during this conference."

<div class="takeaway"><b>小结</b>　演示跑的是 Wan2.2 T2V-A14B（270 亿参数），单卡、480p、5 秒、81 帧、16 fps，1 分 23 秒时还在去噪阶段。这个组合能跑起来靠的不是算力而是显存容量——160 GB 刚好装下 A14B 的权重与 KV。也正因为如此，D 系列的卖点是"每 token 成本"而不是"每 token 延迟"。</div>

---

## 10　从 SoC 到机架，还有一张 OAC 卡

![Scalable Designs：上半部分 Intel delivers（SOCs → PCIe Form Factor）与 Intel enables（Servers → Racks）；下半部分 Intel x OCP innovation — A new form factor, Open Adapter Card (OAC)，展示一块载板上并排两颗 Crescent Island](images/10_08m40s.jpg)

不只是这样。我手里举的那颗 SoC，这是 PCI Express 形态。它只有 350 W，非常灵活，可以扩展进多种 OEM 设计。但我们不止于此——这里毕竟是 OCP。OCP 正在创新一种叫 OAC 的新形态。我们这里有的是两张 Crescent Island 放在一个 OAC 形态上，这是我们和 OCP 生态一起创新的。这是我们在演示的最早的 OAC 版本之一。

> "It's not just that. That SOC that I raised in my hand, this is the PCI Express form factor. This is only 350 W. It's very flexible and scales into multiple OEM designs. But, we're not stopping there. This is OCP, after all. And OCP is innovating on this new form factor called OAC. And what we have here is two Crescent Islands on an OAC form factor that we are innovating with the OCP ecosystem. And this is one of the first OAC versions we are demonstrating."

<div class="takeaway"><b>小结</b>　形态谱系是四层：SoC → PCIe 卡 → 8 卡/16 卡服务器 → 机架。OAC（Open Adapter Card）是把两颗 GPU 做成一张"适配卡"，机架侧不必为每张卡单独走线——这是交给 OCP 的形态贡献，不是英特尔的私有设计。下一页的 Orion 就是接着这个思路做的机架。</div>

---

## 11　请上两位合作伙伴

![嘉宾介绍页：Astera Labs × Sail × intel；左侧 Pravin Patel（Vice President & General Manager, AI Platform Solutions Group, Astera Labs），右侧 Neil Movva（Chief Executive Officer and Founder, Sail Research）](images/11_09m40s.jpg)

这打开了一整个形态的谱系。我们的合作伙伴可以拿这颗 SoC 去做形态；我们的服务器伙伴可以拿 PCI Express 卡做 8 卡、16 卡的服务器设计；甚至还有伙伴要拿它做机架级方案。为了多讲讲这个，我想请几位合作伙伴上台。我想请 Astera Labs 的 Pravin Patel，和 Sail Research 的 Neil Movva——Sail Research 的 CEO。请大家给他们热烈欢迎。

> "Now, this enables a whole range of form factors. Our partners can take the SOC and build form factors. Our server partners can take the PCI Express card and build by eight, uh, you know, config or by 16 config server designs. And there are even partners who going to take this and build rack scale solutions with Crescent Island. To talk more about this, I want to introduce some partners on stage. I'd like to introduce Praveen Patel from Astera Labs and Neil Mowar from Sale Research, the the of say CEO of Sale Research. Let's please give them a broad welcome."

<div class="takeaway"><b>小结</b>　两位嘉宾的分工很清楚：Astera Labs 解决"怎么把 8 张卡扩成 80 张"，Sail Research 解决"扩出来之后怎么把推理成本打下来"。前者是互连，后者是模型映射与推理经济学。名字以幻灯片为准——录音识别成了"Praveen Patel / Neil Mowar / Sale Research"。</div>

---

## 12　Orion：一颗 320 lane 的交换芯片，把 PCIe 做成 scale-up 域

![Astera Labs 发布页：左侧 Orion Rack 机架与 Orion-CT（Accelerator & Memory Compute Tray）、Orion-FT（High Density Scale-Up Fabric Tray）；右侧 INTRODUCING AsteraLabs. Orion，下附 Production-Grade / Rack-Scale / Reference Architecture](images/12_10m40s.jpg)

嗨 Pravin，最近怎么样？

**Pravin Patel：** 很高兴又见到你。

嗨 Neil，很高兴又见到你。呃，Pravin，你今天有一些令人兴奋的消息要告诉在座各位？

**Pravin Patel：** 是的，先生。

你想多讲讲吗？

**Pravin Patel：** 好的，我的意思是，你今天看到的是英特尔新 GPU 的发布，对吧。而现在你需要一个"家"，让你能利用这颗 GPU 并建起一个大集群。所以今天 Astera Labs 发布了一款叫 Orion 的产品。Orion 是我们把 Scorpio 2 那个设计——它有业界最大的 320 lane 交换能力——做成 PCI 集群的产品。所以过去你被限制在 8 卡集群，或者最多 16 卡、再加若干交换芯片。现在，用服务器里的单颗交换芯片，你可以在 PCI 模式下以全带宽扩到 160 张 GPU。你在英特尔今天发布的 GPU 上看到的，一个机架里可以做到 80 张 GPU。而且你不用担心功耗问题，因为那张 GPU 只有 350 瓦。

> "Hi Praveen, how are you doing? >> Nice to meet you again, you know, >> Hi Neil, great to see you again. Um so Praveen, you have some exciting news for this audience today. >> Yes, sir. >> You want to tell us more? >> Yes, so I mean um what you saw today was like the new GPU introductions, right, from Intel. And now you got to have a home where you could take that advantage of the GPU and create a big cluster. So today ESTRA-LAB announced product called Orion. Orion is the product where we take our Scorpio 2 design that has a 320 lane biggest radix in the industry and create the PCI cluster. So now you used to you are limited to have eight GPU cluster or maybe 16 by putting X number of switches. Now with the single switch in the server you could scale up to 160 GPU full bandwidth in the PCI mode. What you see that Intel announced today with their GPU, you can do 80 GPU in the single rack. And still you don't have to worry about that power problem because that GPU only 350 watt."

<div class="takeaway"><b>小结</b>　几个数字串起来看：Scorpio 2 交换芯片 320 lane、单芯片 160 GPU 全带宽、单机架 80 GPU。80 × 350 W ≈ 28 kW 的加速器功耗，这就是"不用操心功耗"能成立的前提——换成 1000 W 级的卡，同一个机架光加速器就是 80 kW，风冷直接出局。</div>

---

## 13　1.16×：AlltoAll 带宽的实测

![演示画面：Low-Latency Inference Optimized Architecture（Astera Labs × intel）——左侧 8 GPUs / 4 + 4 over RoCE 拓扑，46.88 GB/s；右侧 8 GPUs / Astera Labs 320L Scorpio-X Series Smart Fabric Switch，54.31 GB/s；中间浮层 1.16X more AlltoAll bandwidth；底部柱状图为 AllReduce 35.3/34.13、AllGather 27.08/33.94、AlltoAll 46.88/54.31](images/13_12m00s.jpg)

而且 Praveen，我们一直紧密合作，有些东西已经在跑，也有我们从技术工作里得到的一些数据。要不要和大家分享一下？

**Pravin Patel：** 我觉得可以。时机正好，因为我们想确保大家理解 Astera Labs 这次发布的价值——和英特尔一起作为一个完整产品，还有我们来自 Sail Research 的客户。所以你可以看到，我们跑的这个是真实测量数据。不是那种"我们做了分析"的数据，而是用全对全通信跑出来的真实测量数据。如你所见，利用这个新架构配上英特尔 GPU，你可以获得 45% 的提升。

所以 PCI Express 给我们的可扩展性和灵活性，让它非常容易采纳，摩擦非常低。

> ">> And Praveen, we've been working closely on this and we have some things running and there's some data from the from the technical work that we've done. Do we want to share it with the team? >> I think so. This is the perfect timing because we want to make sure that team understands the value of this new announcement from ESTRA-LAB along with Intel as a complete product along with the our customer from Scale Research also. So as you can see that we ran this is the real measurement data. It's not something that hey, we did the analytics. It's the real measurement data by using all radios all all to all communications. And as you can see that you can get 45% improvement by utilizing this new architecture with Intel GPU. >> So PCI Express gives us a scalability and flexibility that's so easy to adopt that this becomes a very low friction."

<div class="takeaway"><b>小结</b>　屏幕上三组实测里，AlltoAll 从 46.88 涨到 54.31 GB/s（+15.9%），AllGather 从 27.08 涨到 33.94（+25%），AllReduce 反而从 35.3 略降到 34.13。对比基线是"8 卡 4+4 over RoCE"，也就是用两颗交换芯片拆成两个域——这正是 PCIe 方案要打的靶子。</div>

<div class="insight"><b>想法</b>　口述说"45% 提升"，屏幕上写的是 1.16×，也就是 16%。两个数字对不上，而且差了近三倍。可能性有三：45% 指的是某个未上屏的指标（比如小消息延迟或 P99），1.16× 只是 AlltoAll 这一项；或者 45% 是早期版本数据；或者纯粹是台上口误。不管哪种，公开演讲里这类"口述数字比幻灯片大"的情况值得警惕——真正做选型时，应该按 1.16× 这个保守值去算，而不是 45%。</div>

---

## 14　Neil Movva：推理要的不是峰值带宽，是小消息延迟

现在 Neil，你一直处在一些 Neo Cloud 部署的最前沿，在建一些非常非常创新的东西。我读过你的文章，你想把推理成本降 1000 倍。这些方案在你的这条路上怎么帮到你？

**Neil Movva：** 是的，这是个非常高的目标。今天我们推理的成本和"token 经济学"还有很大改进空间。当然，我们很幸运能在芯片本身和英特尔合作。Crescent Island 我们是超级粉丝，也很兴奋成为它的首批客户。但就像我们前面在这个演讲里说的，现在我们的工作已经不是一次给一颗芯片编程了。芯片架构师的工作，以及像我们这样的软件公司做模型映射的工作，是高效地扩到 8 张 GPU、64 张 GPU，甚至 80 张 GPU。这就是我们和 Astera 合作、让 PCIe 成为我们推理所需的那个 scale-up 域的原因。

这里有几点让我们、英特尔和 Astera 之间的合作效果特别好。第一，scale-up 域通常讨论的是带宽——也就是加速器之间峰值数据移动量作为主要指标。但对推理来说，情况很不一样。我们相当在意小消息的延迟。而这正是 Astera 交换设计能削掉微秒、某些情况下甚至纳秒的地方，确保我们在推理中一直在发的小消息能快速、可靠地完成，并让我们高效地扩展像 Kimi 系列那样的大型 MoE 模型——我们可以在 Astera Labs 的 fabric 上非常高效地扩展它。

除此之外，Astera 还创新得更远，带来了一些非常关键的新特性，比如在同一个域里把数据从一个加速器广播到其他加速器，而且非常高效、不会放大数据。他们叫它 HyperCast，我们很兴奋能和他们在这个新特性上合作。PCIe 会是我们所做推理的一个很好的 scale-up 域。

那么 Neil，可以说智能体推理其实是一个异构负载吗？

**Neil Movva：** 绝对是的。工作负载可以瞬间改变——从大规模 prefill，也就是用户提示或一个很大的工具调用突然送来大量 token，到智能体开始解码数千个 token、在一个难题上长时间推理。就计算密集度和内存密集度而言，这是完全相反的两端。而我们从这个像 Astera 这样大的 scale-up 域、加上定制 tile 和芯片中所获得的灵活性，让我们能在同一个平台上同时拥有好的算力和好的内存带宽，这是我们非常兴奋的。

> ">> So Neil, you've been at the spearhead of some Neo Cloud, you know, deployments and building some very very innovative stuff. I've read your article where you want to bring the cost of inferencing down by 1,000 X. Now how do these solutions help you in that journey? >> Yeah, I mean, that's a very tall order. We have a lot of room to improve on the cost and tokenomics of inference today. And of course, we've been very lucky to work with Intel on the chip itself. Crescent Island we're big fans of and we're excited to be a launch partner customer for Crescent Island. But as we've said earlier in this talk, it's no longer our job to program one chip at a time. The job of a chip architect and the job of a model mapping from a software company like ours is to scale up efficiently to use eight GPUs, 64 GPUs, even 80 GPUs. And that's where we've been working with Astera to get PCIE to be the great scale of domain we need for inference. Now there's a couple factors here that really make the partnership between us, Intel, and Astera work extraordinarily well. The first is that scale up domains often discuss bandwidth, meaning peak data movement between our accelerators as the primary metric of interest. But for inference, it's actually quite different. We care quite a bit about the latency of small messages. And this is one of the areas where Astera's switch design is able to shave off microseconds and even nanoseconds in some cases to make sure that small messages, which we send all the time in inference, can happen quickly, reliably, and allow us to scale up modern large models like Kim K3, a huge mixture of experts model. We can scale that really efficiently on the Astera Labs fabric. In addition to that, Astera has innovated even further and brought some really critical new features such as the ability to cast data from one accelerator to other accelerators in the same domain really efficiently without amplifying data. They call it HyperCast, and we're really excited to be working with them on this new feature. PCIe is going to be a great scale of domain for the inference that we do. >> So, Neil, is it fair to say that agentic inference is actually a heterogeneous workload? >> Absolutely. The work can change on a dime from massive pre-fills, meaning lots and lots of tokens being sent in by a user prompt, or maybe a large tool call, suddenly to the agent now decoding thousands of tokens to reason for a long time on a hard problem. These are entirely opposite ends of the spectrum in terms of compute and memory intensity, and it's the flexibility we get from a scale of domain that's as large as Astera's, plus the custom tile and chip that allows us to have great compute as well as great memory bandwidth on one platform that we're super excited about."

<div class="takeaway"><b>小结</b>　这一段是全场技术含量最高的部分，也是最容易被忽略的：scale-up 域的传统 KPI 是峰值带宽，但推理真正吃的是小消息延迟——因为 decode 阶段每一步都在发很小的 all-to-all（MoE 的 token 分发）。微秒级差异乘以几十万步，就是端到端延迟。HyperCast 解决的是另一件事：一份数据广播给多个加速器时不放大流量，本质上是把"复制"从带宽问题变成控制问题。</div>

---

## 15　生态清单，和一句"到此为止"

![Intel GPU D-Series — Growing Ecosystem of Customers and Partners：顶部四类分栏为 AI Natives / Appliances / ISV & Software Ecosystem / Neo Clouds / OxMs，下方为六行合作伙伴 logo 墙，右下角标注 Includes several OCP members 与 Open Compute Project 标志](images/14_16m00s.jpg)

谢谢你，Neil。我们非常兴奋能确保把这些方案交付给你们，让你们真正能部署。Pravin，非常好的合作。我们很兴奋有这个生态，它真正体现了 OCP 的意义——把这些伙伴关系带进生态、构建方案，从而降低成本、提升效率，并带来给客户选择权的方案。

**Pravin Patel：** 谢谢。谢谢你，Anil。你其实给了我们机会去在你的新设计上工作，并展示我们器件的性能。我们这里有实际的证明，可以看到 PCI 域里有增值——因为大家都知道 PCI 已经存在很多年了，对吧？所以现在你只是在 PCI 内部创建 scale-up，这完全改变了游戏规则。

谢谢。很荣幸来这里，期待我们合作伙伴带来令人兴奋的方案。

（掌声）

如你们所知，把它推向市场不只靠我们，它需要一个围绕它建立的生态。我们一直在和 AI 原生公司、Neo Cloud、生态伙伴、OEM、ODM 全面合作，帮助把 Crescent Island 推向市场。所以我非常兴奋，也等不及看到它到了开发者和真正会使用这些系统算力的客户手里。

就像我前面说的，AI 智能体和 AI 推理不是同构负载，它是异构负载，不是一招通吃。不是所有 token 都一样，不是所有 token 的需求都一样。取决于你需要多大的交互量、什么延迟、什么模型规模，会有不同种类的算力被启用。

> ">> Thank you, Neil. Uh we are super excited to making sure that we deliver the solutions to you, so you can actually deploy it. And Praveen, wonderful partnership. Uh we are excited to have this ecosystem, and truly kind of, you know, emulates what OCP is all about, uh bringing this partnerships into the ecosystem and building solutions so we can reduce costs, improve efficiency, and be able to bring solutions uh that give customers choice. >> Thank you. Thank you, Anil. I mean, you you gave us actually chance to work on your new design and how we can show the performance with our devices. And we have actually proof over here where he can see that there is a value added in the PCI domain because as we all know PCI has been there for years, right? So now you're just creating the scale up within the PCI, it just change the game completely different. >> Thank you. >> to the internet. >> Yeah. Thank you. >> coming to be here. >> Thank you. Yes. Look forward to exciting solutions from our partners. >> [applause] >> Now as you know, it doesn't take just us to bring this to market. It takes an ecosystem to build around that. We've been partnering with AI natives, Neo clouds, ecosystem partners, OEMs, ODMs, across the board helping bring Crest and Island to market. So I'm super excited and can't wait to see this in the hands of both developers and to customers who will actually use the compute from these systems. Now like I said earlier, AI agent and AI inference is not a homogeneous workload. It's a heterogeneous workload. It's not a one-size-fits-all. Not all tokens are going to be the same. Not all token requirements are going to be the same. There are going to be different kinds of compute enabled depending on what kind of volume of interactivity you need, what latencies you need, and what model sizes you need to build on."

<div class="takeaway"><b>小结</b>　这一页 57 个 logo 是整场演讲最"软"的证据，但也是最能说明问题的一页：从 ASIC 厂（Accton、Celestica 系）、OEM（Dell、HPE、Lenovo、Supermicro、Foxconn、Wistron、Pegatron、Inventec、QCT、MiTAC）、到软件栈（Canonical、Red Hat、VMware、vLLM、Hugging Face、OpenHands、Anyscale）、再到 Neo Cloud（Cirrascale、FarmGPU、VC2）。英特尔的策略不是自己卖整机，而是让这些人在自己的产品线上留一个 GPU 插槽。</div>

---

## 16　把架构图再放一遍，这次每一层都有了型号

![同一张 Agentic AI Inference Datacenter Architecture 图，但四层分别标注了具体产品：Control Plane 为 Intel Xeon 6、Execute 层为 Xeon 6+ 与 Xeon 6、Token Generation 为 Intel GPU D-Series 与 SambaNova RDU](images/15_16m35s.jpg)

我们一直在和 SambaNova 合作。SambaNova 有一个数据流架构，能为智能体时代带来低延迟、高 token 吞吐、高交互性的用例。SambaNova 的芯片可以给你最高每秒 820 个 token，在他们最近发布的 SambaNova 50 系列上是快 4 倍。我们一直和他们合作，把这种异构性带来——我们的英特尔至强、SambaNova 的 RDU，以及我们即将推出的 Crescent Island、Intel D 系列 GPU。

> "So we've been partnering with SambaNova. SambaNova has a data flow architecture that helps bring low latency, you know, high token throughput, high interactivity use cases for the agentic era. The SambaNova's um chip which is can give you up to 820 tokens per second. It's 4x faster on the SambaNova 50 series which they recently announced. We've been partnering with them to bring this heterogeneity along with our Intel Xeon, with the SambaNova RDUs, and with our upcoming s- Crescent Island Intel D-Series GPUs."

<div class="takeaway"><b>小结</b>　同一张图讲第二遍，信息量完全不同：第一次讲的是"哪一层干什么"，这一次讲的是"每一层由谁供货"。控制面是至强 6，执行面是至强 6+ 和 6，生成面同时列了 Intel GPU D 系列和 SambaNova RDU——这是全场唯一明确承认"生成层也要混着用"的一页。</div>

---

## 17　机架级交付：100 kW 的 CPU 架，60 kW 的 GPU 架

![Delivering Agentic Capability at Scale：左 Intel CPU Rack ~100kW、16,384 / 36,864 P-cores / E-cores、384TB DDR5、614GB/s / 768GB/s Mem BW per Socket；中 Intel GPU Rack ~60kW、208PF FP4 Peak、x80 GPUs、12-38TB Mem Capacity、120TB/s Mem BW；右 SambaNova SambaRack SN50 ~30kW、51PF FP8 Perf Peak、x16 RDUs、1TB HBM2e、7GB SRAM、Scale up to 256 RDUs](images/16_18m20s.jpg)

这些东西不会以单颗芯片的形式出现。随着机架级推理的增长，它们在棕地数据中心和绿地数据中心里的方案，都给你在不同算力能力之间选择的灵活性。所以，随着推理变得更分布式，你会需要从云到边缘服务器的不同算力方案。

而有了 Crescent Island、Intel D 系列上的 PCI Express，你会拥有这种灵活性，以及无摩擦扩展的能力，因为大量 OEM 和 ODM 设计会从一开始就支持 Crescent Island。在此之上，对于 Crescent Island，我们承诺对 OpenVINO 生态里的主流模型提供 Day 0 支持。我们会推动框架向上扩展，vLLM、SGLang，以及所有需要被上游支持的行业框架，这样你就不需要额外下载任何扩展。

我们正在和 SambaNova 合作建机架，他们在建机架，以便在 SambaNova 上高效地做 decode 方案，配上 Crescent Island 的能力。当然，运行这整个生态、运行编排的，是 CPU。用我们的英特尔至强产品组合，我们有广泛的能力、选择和技能供生态创新，英特尔至强家族在这里，为这个智能体时代的未来提供动力。

说到这里，我真的很想感谢大家到场，感谢给我们机会来展示我们如何为这个智能体未来铺设积木。还有更多令人兴奋的东西要来。请一定去展台看这些演示的实际运行。同时，我们明天有一场主题演讲，我的搭档 Nick Dube 会讲智能体时代未来的一些细节。那么，谢谢。谢谢你们的时间。

> "These will not just come as single chips. At rack-scale inferencing grows, their solutions in both the brownfield data centers as well as the greenfield data centers give you flexibility of choice in a range of capabilities of compute that you can deploy. So, as in inference also becomes more distributed, you're going to need different kinds of computing solutions from the cloud going towards the edge servers. And with PCI Express for Crescent Island, the Intel D-Series, you're going to have that flexibility and the capability to scale this without a friction because a broad amount of OEM and ODM designs will be supporting Crescent Island straight off the bat. On top of it, with Crescent Island, we are committing to, you know, day zero support for mainstream models in the Open VET ecosystem. We'll be working towards the frameworks to be scaling up with VLLM, SG Lang, and all the industry frameworks that need to be supported upstreamed so that you don't need any extensions to be downloaded. We're partnering with our Sambanova to build racks that they are building the racks on to work efficiently for decode solutions on Sambanova with people like, you know, capability on Crescent Island. And of course, what runs all of this ecosystem, what runs the orchestration, is going to be the CPU. With our Intel Xeon portfolio, we have wide range of capabilities and choice and skills for our ecosystem to innovate on. And the Intel Xeon family is here to actually power the future of this agentic era. With that, I really want to thank all of you to be here. Give us the opportunity to present how we are putting the building blocks towards this agentic future. Lot more exciting things coming. Please do Please do go visit the booth to see some of these demos in action. And at the same time, we have our keynote session tomorrow, where my partner, Nick Dube, will be talking about, you know, some of the future details on the agentic era. So, with that, thank you. Thank you for your time."

<div class="takeaway"><b>小结</b>　三台机架摆在一起，功率密度就说明了一切：CPU 架 ~100 kW（3.6 万个能效核、384 TB DDR5）、GPU 架 ~60 kW（80 张卡、208 PF FP4、120 TB/s）、SambaRack SN50 ~30 kW（16 颗 RDU、51 PF FP8、1 TB HBM2e）。同样一台机架，功率差三倍多——这就是"异构"在机房平面图上的样子。</div>

<div class="insight"><b>想法</b>　最后承诺的"Day 0 支持主流模型、不需要下载任何扩展"，其实比任何一颗芯片的参数都关键。过去几年英特尔 GPU 最难的不是硬件，而是"模型跑不起来要打补丁"这件事——开发者一旦踩过一次，第二次就不会再试。把 vLLM 和 SGLang 的上游支持说成"承诺"，意味着这是一条必须兑现的路线图，而不是一句营销话。真正该盯的指标是：Crescent Island 上市那天，Hugging Face 上排名前 50 的模型有几个能开箱即跑。</div>

---

## 结语

一句话：**异构不是英特尔的产品策略，而是推理负载逼出来的物理事实。**

这场演讲真正的结构是一条从账单倒推回硅片的链条：智能体让 token 量和成本同时爆炸（§03）→ token 分三类，需求互相独立（§04）→ 所以控制面回到 CPU，CPU:GPU 从 2:8 走向 1:1（§05）→ 生成层需要大内存低功耗的另一种芯片（§08）→ 而把这些芯片连起来不能靠专用互连，只能靠 PCIe（§12）。

英特尔的赌注押在最后一环：如果 PCIe 足够好，那么"异构"就不需要每一家自建 fabric，OEM 和 ODM 就能在自己的产品线上留一个插槽。这也是它必须把 OAC 交给 OCP、必须承诺 Day 0 上游支持的原因——它卖的不是一颗卡，是一个可以被别人集成的标准件。

<div class="recap"><b>数字速览</b><br>
发布产品　Intel GPU D 系列（代号 Crescent Island）<br>
算力　FP8 1311 / MxFP4 2622 TFLOPS<br>
显存　零售卡 160 GB LPDDR5X（ECC），ODM 可做到 480 GB<br>
带宽　1.5 TB/s<br>
功耗　350 W，风冷 PCIe<br>
形态　SoC → PCIe 卡 → 8/16 卡服务器 → OAC（双芯）→ 机架<br>
互连　Astera Orion / Scorpio 2，320 lane，单芯 160 GPU<br>
实测　AlltoAll 46.88 → 54.31 GB/s（1.16×）<br>
CPU:GPU　2:8 → 1:4 → 1:2 → 1:1<br>
至强　6+ 288 E-core / 6 128 P-core / Diamond Rapids 256 P-core<br>
机架　CPU 架 ~100 kW · GPU 架 ~60 kW · SambaRack SN50 ~30 kW<br>
OCP　116 项贡献、33 场会议</div>

<div class="outro">本文依据 OCP Global Summit 2026 现场录像整理，参数以幻灯片标注为准；讲者口述与幻灯片不一致处（如 track 数 16 与 13、AlltoAll 提升 45% 与 1.16×）已在对应小节注明。原片：youtube.com/watch?v=v7Sc3MK9Ezg（19 分 53 秒）。如果你正在评估推理集群的互连方案，欢迎留言聊聊：在 350 W 这个功耗档上，你会选 PCIe scale-up 还是继续用专用 fabric？</div>

---

## 附录　时间轴

| 时间 | 内容 |
| --- | --- |
| 00:05 | 开场：异构是推理负载本身的样子 |
| 00:45 | OCP 社区：116 项贡献、33 场会议 |
| 01:22 | 智能体把成本曲线掰弯了 |
| 02:24 | 三个独立的旋钮：模型大小、上下文、TPOT |
| 02:51 | 控制面回到 CPU：从 2:8 到 1:1 |
| 04:15 | 三颗至强，三种分工 |
| 05:24 | 机架已经能买了：六家 OEM |
| 06:19 | Crescent Island 正式命名 Intel GPU D 系列 |
| 07:09 | 现场演示：270 亿参数文生视频 |
| 08:18 | 从 SoC 到机架，以及 OAC 新形态 |
| 08:58 | 请上 Pravin Patel 与 Neil Movva |
| 09:47 | Orion：320 lane 交换芯片与 160 GPU scale-up 域 |
| 10:54 | 1.16× 实测与"45% 提升" |
| 12:08 | Neil Movva：推理要的是小消息延迟 |
| 15:43 | 生态清单与 SambaNova 合作 |
| 16:35 | 架构图复现：每一层都有了型号 |
| 17:28 | 机架级交付与 Day 0 承诺 |
| 19:37 | 收尾与明日 keynote |
