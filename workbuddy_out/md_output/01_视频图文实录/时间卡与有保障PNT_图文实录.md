# 时间卡：一种有韧性的 R-PNT 定制方案

> OCP Global Summit 2026 · Time Appliances Project (TAP) 分会场
> 讲者：Yair Neugeboren（Oscilloquartz 产品线高级经理）、Anil Reddy（Oscilloquartz 全球业务拓展副总裁）
> 全长 16 分 46 秒　|　共 15 页幻灯片

---

## 01　开场：从时间卡到韧性

![开场标题页：A Timecard as a R-PNT custom solution，讲者为 Yair Neugeboren 与 Anil Reddy（均为 Oscilloquartz）](images/01_00m30s.jpg)

谢谢。那么，本次演讲我们来讲时间卡（time card）。我们会讲时间卡的各个不同方面；最后我会为不太熟悉的人稍微讲一下时间卡是什么、定义时间卡的不同标准组织、以及业界有哪些可以使用时间卡的用例。如果上一场讲得还不够，我也会稍微讲一下 PTM；然后我把时间交给 Anil 讲韧性。

（现场）不，不，应该能工作。不，往回翻一页。

> "Thank you. So, we'll talk in this session about the time card. We'll talk about different aspects of a time card and eventually I'll talk a little bit about what is a time card for those who are less familiar, the different standard bodies that define time card, what are the use cases to in the industry that you could use time card. I'll talk a little bit about PTM if someone didn't have enough from the previous session and then I'll hand off to Anil to talk about resiliency.  No. No, it should work. No, go one back."

<div class="takeaway"><b>小结</b>　演讲分两段：Yair 讲"是什么"——时间卡定义、标准、架构、形态与用例；Anil 讲"靠不靠得住"——GNSS 源的风险与 R-PNT 韧性等级。这一分工本身就点出了主题：卡片做得再好，源头不可信就没有意义。</div>

---

## 02　时间卡的范式转移

![The Timecard Paradigm shift：左侧 Dedicated appliance（外部 1U/2U 授时服务器，固定功能、独立机架空间与供电、额外布线、专用生命周期），右侧 Modular timecard（COTS 服务器内的 PCIe 模块，授时源贴近计算、复用服务器供电/散热/库存、随开放基础设施扩展、支持 OCP-TAP 与扩展的 P335 功能）](images/02_01m20s.jpg)

好。那么，时间卡。呃，如果我们过去习惯于用完整的设备来做授时——1U、2U，甚至更大的授时服务器，硬件固定，占用机架空间，还要布线和更多功耗。我们现在正在转向一种模式：可以利用现有硬件，只是把某些器件插进去。授时源离计算更近，好处是能为计算模型提供非常精确的时间，而且容易扩展。

> "Okay. So, a time card. So, if we were used to have full-blown devices for timing 1U, 2U, maybe even more, timing servers with a fixed hardware and space rack and cabling and more power. We're kind of shifting to a mode that we could use the existing hardware. We're just plugging some appliances into it. The timing source is closer to the compute with the advantages of providing very accurate time to the compute model. And it's easily scalable."

<div class="takeaway"><b>小结</b>　范式从"专用授时设备"转向"服务器内的模块"：省掉独立机架空间、供电与布线，复用 COTS 服务器的供电/散热/库存，同时把授时源物理上推进到计算旁边——这既降成本，也缩短了时间传递路径。</div>

---

## 03　时间卡标准：OCP TAP 与 IEEE P335

![Timecard Standards：左栏 OCP TIME APPLIANCES (TAP)——开放规范与参考设计、可互操作实现、由 OCP-TAP 驱动管理、主要作为 GNSS 输入为宿主系统授时；右栏 IEEE P335——定义时间卡系统的通用架构与接口、可选授时输入输出、可选控制接口，但不一定是开放架构](images/03_02m10s.jpg)

那么，有哪些授时标准？授时标准最初从 OCP TAP 开始，它有自己的规范，主要定义开放接口，然后是开放代码、开源，说明时间卡是什么、有哪些接口、以及如何在服务器上支持它。它主要聚焦于把 GNSS 传给 CPU，除此之外不多。我们还有 IEEE P335，它——我不想说它明显矛盾——它把时间卡的范围展开：更多的可选授时输入、授时输出、控制接口是什么，并且不绑定到某个特定驱动、特定实现。

那么，时间卡是什么？时间卡的基本架构是什么？时间卡显然有一个振荡器，可以是简单的石英振荡器……

> "So, what are the timing standards? The timing standards initially it started from OCP TAP which it has its own specification that mainly defined an open interfaces and then open code open source for what a time card is what are the interfaces and how it would be supported on on on a server. It mainly focuses on a GNSS to the CPU delivery or not much more than that. We have also the IEEE P335 which kind of wouldn't say it doesn't obviously contradict it kind of elaborate the scope of a time card to be with more optional timing inputs timing outputs what are control interfaces and not kind of tied to a specific driver specific implementation. So what is a time card and what is the basic architecture of a time card? So a time card has obviously an oscillator could be simple oscillator like quartz"

<div class="takeaway"><b>小结</b>　两个标准互补：OCP TAP 规范开放、有参考设计与开源驱动，但范围窄（主要是 GNSS→CPU）；IEEE P335 把范围扩展到可选的授时输入/输出与控制接口，且不绑定具体驱动实现。前者重"可互操作落地"，后者重"架构通用性"。</div>

---

## 04　时间卡基本架构

![Timecard Basic Architecture：模块化服务器集成的时间卡架构——外部时源（GNSS 卫星、1PPS、10MHz、IRIG 等）进入时间卡模块（GNSS 接收机、GNSS 锁定振荡器与 PLL、高稳定振荡器、时钟引擎、TAP/P335 引擎、温度补偿），经 PCIe 与 PCIe PTM 送到主机 CPU、网卡与 BMC；下方列出架构收益、授时数据流、关键标准与接口、典型应用](images/04_03m05s.jpg)

……也可以是一颗铷钟这类高端振荡器，如果需要更长的保持（holdover）时长。它还有一个 PLL，实际上锁定到时间并维持时间；而 GNSS 通常是取时的时间源，从 GPS 卫星获取。最后一段——我们上一场讲过——讲的是 PTP。那么，时间卡是什么？时间卡不一定是一块 PCIe 时间卡。

> "and a nick could be I hand oscillator like a rubidium if if hold over durations longer hold over durations are needed. And it has a PLL which actually um locks to the time and maintains the time and the GNSS was usually the source of time getting from from GPS satellites. And the last mile the last things we we talked about the the last session was talked about about PTP. So what is a time card? So a time card is not necessarily a PCIE time card."

<div class="takeaway"><b>小结</b>　时间卡的三件核心：振荡器（石英→铷钟，决定保持能力）、PLL（锁定并维持时间）、GNSS 接收（时间源）。架构上它把外部时源经 PCIe/PTM 分发给主机 CPU、网卡与 BMC——这解释了为什么"时间卡"本质是一个板级授时子系统，而不只是一块扩展卡。</div>

---

## 05　时间卡形态：PCIe / M.2 / USB

![Time Card options：标题下注明"A timecard is not necessarily a PCIe card"；左为 PCIe Timecard（GNSS、ToD/1PPS/IRIG/HQ、1PPS/CLK、ETH PTP/NTP、PCIe PHC/PTM），中为 m.2 module（GNSS、1PPS/CLK/PCIe PTM/PHC/ToD），右为 USB interface（USB PHC/PTM、1PPS/CLK、GNSS、ETH PTP/NTP）](images/05_03m50s.jpg)

时间卡也可以是 OCP 规范定义的 M.2 模块，好处是不占插槽；也可以是 USB 接口。呃，如果你去问 Ahmed，那都是他的心血——关于 USB 模块怎么能真正充当时间卡。希望很快也能支持 PTM。呃，那样你只需要一根 USB 直接连到 CPU，就有了一个非常微型的时间卡。

那么，PTM。我不会再重复 PTM 是什么。呃，那些去过我们创新实验室展台的人，我们展示了一块在系统里充当 PRTC-B 的时间卡。呃，我们用的应该是和上一场完全相同的配置，尽管我们拿到了更好的结果。呃，我同意 Kevin 的看法，很可能是我们时间卡上用的那颗振荡器把噪声都压下去了。

> "A time card could be also M.2 model also specified by OCP. Um with the advantages of not occupying slot it also could be a USB interface Um, and if you ask Ahmed, it's all his own baby. About uh how USB could um model could actually act as a time card. And hopefully soon also with PTM support. Um, and and then you kind of only need a USB connected directly to the CPU and you have your uh very miniature time card. So, PTM. So, I will not go over again what PTM is. Um, those of you who managed to go through our table in the innovation lab, we kind of showed um a time card in a system acting as a PRTCB. Um, we had a I think it the exact same setup that the previous session presented. Although we got um better results. Um, and I agree with Kevin probably the"

<div class="takeaway"><b>小结</b>　三种形态各有取舍：PCIe 卡接口最全（GNSS、ToD/1PPS/IRIG、以太网 PTP/NTP、PTM）；M.2 省插槽；USB 最微型，只需一根 USB 直连 CPU（PTM 支持在望）。形态选择由机箱空间与所需接口决定，而非功能上限。</div>

---

## 06　PRTC-B 时间卡系统与 PTM

![PRTC-B timecard system with PTM：GNSS 天线输入时间卡（OSA5400），时间卡输出 1PPS 与 PTP；右侧列出配置——Timecard: OSA5400、NIC: Intel I226、CPU/PCH: Intel Z890、时间卡与网卡均启用 PTM、1PPS 取自 OSA5400 的 PHC、PTP 为经 I226 的 ptp4l G.8275.1 master；下方为测量曲线与统计](images/06_05m00s.jpg)

……振荡器——很可能是我们时间卡上用的那颗振荡器把噪声都压下去了。所以，基本上我们有一个配置：一块时间卡，Oscilloquartz 的时间卡；我们用了支持 PTM 的 Intel I226 网卡；PCH 是 Intel Z890。呃，时间卡和网卡上都启用了 PTM。我们比较的是：从时间卡 PHC 输出的 1PPS，与经网卡送出的 PTP 相比。我们经网卡用的是 G.8275.1，把 1PPS 与 PTP 相比。如你所见——我们展台上也有——我们看到了 7 纳秒的 MTI，持续了大约 3 天。呃，所以它显然可以是 PRTC-B，甚至可能更好。

> "oscillator used um on our on the time card um managed to reduce all the noise. So, basically we had a setup. We had a time card, uh the Oscilloquartz time card. We used the NIC, the Intel I226, which supports PTM. The PCH was Intel uh Z890. Um, PTM was enabled both on the time card, the NIC, and what we compared, we compared um the output from the PHC from the time card through 1 PPS and compared it to PTP going out through the NIC. We used uh G8275.1 um through the NIC and compared the 1 PPS to the PTP. And if you can see, and we we had that also in in our table, we saw uh MTI of 7 nanoseconds for like 3 days. Um, so obviously it could be a PRTCB or maybe even better."

<div class="takeaway"><b>小结</b>　实测配置：OSA5400 时间卡 + Intel I226（支持 PTM）+ Z890 PCH，1PPS（取自卡上 PHC）与经网卡输出的 G.8275.1 PTP 比对，MTI 约 7ns、持续约 3 天——达到 PRTC-B 甚至更优。关键使能项是 PTM：它让时间卡到主机的传递不再是精度瓶颈。</div>

---

## 07　时间卡的应用场景

![Timecard solutions / TIMECARD USE CASES：AI 数据中心（同步 GPU 集群、标记任务、可观测工作负载）、开放无线接入网（5G DU 授时、LLS-C1/C2 架构）、金融交易基础设施（亚纳秒时间戳、PCIe PTM、白兔就绪）、国防传感器平台（任务关键 PNT、雷达/LiDAR/通信同步、GPS 拒止环境）](images/07_06m00s.jpg)

关于时间卡的解决方案。呃，我讲快一点。呃，时间卡虽然最初是为数据中心设计的，但很多不同的垂直行业都可以用。有数据中心、金融交易基础设施、Open RAN——显然用于 O-DU 和战术 5G 部署——还有国防传感器平台；正如 Ahmed 在圆桌里提到的，也包括 F-16 之类的东西。

> "About time card solution. So, I'll do it quickly. Uh So time card is although it was initially aimed for data centers, but many many different verticals could use time card. So there is the data centers, financial trading, uh infrastructure, uh open ran, obviously for ODUs and or tactical 5G deployments, and also for uh defense sensors platforms, and as Ahmed the round table I mentioned also F-16s or things like that."

<div class="takeaway"><b>小结</b>　四类垂直行业：AI 数据中心（GPU 集群同步、任务标记、可观测性）、Open RAN（DU 授时、LLS 架构）、金融交易（亚纳秒时间戳、PTM 到 n-slevel）、国防（雷达/LiDAR/通信同步、GPS 拒止下工作）。共同点是"计算紧邻授时"带来收益。</div>

---

## 08　电信（vRAN / 私有 5G）

![Telecom (V-RAN, private 5G)：时间卡置于 O-DU，向本地 O-RU 与远端 O-RU 提供时间；右侧三点——时间卡可对 O-DU 充当 PRTC-B 提供 ns 级精度、可充当 O-DU 的 PTP 接口（带或不带 NIC 时间戳）、提供嵌入 O-DU 软硬件的 R-PNT 授时方案](images/08_06m30s.jpg)

我讲快一点，因为我想往前推进。这些是——例如在电信里，时间卡可以放在 DU 里，同时通过（网络）给 DU 和 RU 提供时间。而对于国防系统，很多很多加固设备、加固……

> "I'll I'll I'll do it quickly because I want to move. Those are for example in the telecom, time card could be placed in uh the the DU and actually provide time both to the DU and to the RU um through uh um the internet. And for defense system, um many many um rugged devices, rugged"

<div class="takeaway"><b>小结</b>　在 vRAN 里时间卡扮演三重角色：给 O-DU 当 PRTC-B（ns 级）、给 O-DU 当 PTP 接口（可带或不带 NIC 时间戳）、以及把 R-PNT 能力嵌进 O-DU 的软硬件。一个模块同时服务本地与远端 O-RU。</div>

---

## 09　国防

![Defense：加固平台越来越需要精确且有保障的 PNT，又不愿增加笨重的独立授时硬件；PCIe 时间卡让既有加固服务器直接提供授时、定位与外部传感器同步，并可支持 STANAG、HaveQuick 等军用授时格式](images/09_06m55s.jpg)

……PC 有空闲的 PCI 插槽。你可以插一块时间卡，利用 PTM 的优势把非常精确的时间送进 CPU。而那些 CPU 可以用于导航系统、天气预报、或者雷达应用等等。

> "PCs have um PCI slots vacant. You can plug in a time card, and you can use the advantage of PTM to get very precise time into the CPU. And those CPU could be either um navigation systems, weather uh forecasts, um rather radar um applications, etc."

<div class="takeaway"><b>小结</b>　国防场景的诉求是"不加笨重授时硬件也要有保障 PNT"：利用加固机箱里空闲的 PCIe 槽位插卡，经 PTM 把精确时间送入 CPU，再分发给雷达、LiDAR、通信系统，并支持 STANAG、HaveQuick 等军用授时格式。</div>

---

## 10　R-PNT（IEEE P1952）：五级韧性

![R-PNT (IEEE P1952)：韧性等级表——RL1 检测并告警；RL2 恢复 + 检测告警；RL3 抵御 + 恢复 + 检测告警；RL4 承受（Withstand）+ 抵御 + 恢复 + 检测告警；RL5 验证（Verify）+ 承受 + 抵御 + 恢复 + 检测告警](images/10_09m00s.jpg)

那么，我转到另一个话题——交给我吧。好，谢谢。下午好。像 Yair 这样的工程师和产品经理们相信他们做出了一块能解决所有问题的出色卡片，但那只是问题的开始。相信我。为什么？因为这块卡是为向设备交付精确时间而设计的，但最大的部分是源头。那么，挑战在于：我们能否监测源头？我们能否针对源头构建韧性？

但在进入正题之前，我想问：在座有多少人认为 GNSS 已经足够好？在授时圈子里，有多少人认为 GNSS 是一个好的分发源？你们这么认为？至少世界是这么认为的。不管我们信不信，我们的世界相信 GNSS 是免费的。我可以假设 GNSS 免费，然后建一个价值 100 亿美元的授时基础设施。看到了吗？100 亿和免费，这两件事不能并存。

那么，这里的问题是：我们如何针对源头构建韧性？有没有人在研究如何为基础设施构建韧性架构？有的，就是 IEEE 这个组织在做，一个非常有意思的组织——如果你想加入，欢迎。就是 IEEE P1952。它讲的是若干韧性等级、如何保护源头基础设施，从"检测并告警"开始。这是什么意思？很简单：如果检测到任何干扰（jamming）或欺骗（spoofing），你检测到，然后你宣告出去。这是第一级。也就是说，你能够意识到自己正受到威胁。好。

然后是第二级：恢复、检测并告警/通告。也就是说，你能够检测，然后你悄悄进去看那个脆弱性是否还在。如果还在，就关掉；如果不在了，就恢复回来。这就是提供的第二级韧性。

第三级是抵御（resist）、恢复、检测。这是什么意思？"抵御"——这里振荡器就登场了：好，你发现了问题，那么你关掉端口，关掉 GNSS 端口，尽量把时钟保持住。这就是第三级韧性。

然后是第四级韧性：承受（withstand）。这一级最关键，因为这里是多源登场的地方。我的意思是，你不能指望你那 100 亿美元的基础设施，假设单一源就足以让你交付精确时间。这不该是常态。所以这里就是替代 PNT 源发挥作用的地方——比如 LEO 卫星、或者来自 NIST 或本地实验室的（时间）流。这就是你如何承受威胁或脆弱性的方式。

然后最重要的一级是第五级韧性。这里登场的是零信任架构加多源组合器（multi-source combiner）。你会尽量引入尽可能多的源：比如 GNSS 的多个星座——在轨可用的那五六个；然后是 LEO 星座；然后是来自邻近 PTP 的替代源；然后是原子钟。它是一个组合器。而零信任在于：它验证每一个源，并尽量提供满足终端应用 SLA 所需的那个相关源。这就是它现在推进到的地方。

好消息是：像他们这样聪明的工程师，正努力做出对上述脆弱性完全有韧性的卡片……

> "With that, I will move to another  I give it to me. Okay. Thank you. Good afternoon. Well, engineers and PLMs like Yair and rest of them believe that they built a fantastic card that can solve all the problems, but that's the beginning of the problem. Trust me. Why? Well, the card is designed to deliver accurate, precise time delivery to the appliances, but the biggest part is the source. Now, the challenges are we able to monitor the source? Do we Can we build resiliency to the source? But before I get in there, how many of us here believe that GNSS is good enough? How many of us here in the timing fraternity believe that GNSS is a good dissemination source? You believe so? At least the world believes. Doesn't matter whether we believe or not. Our world believes that yeah, GNSS is free. I'm able to build a a fantastic 10 billion timing infrastructure assuming that the GNSS is free. See? 10 billion and free. This doesn't go hand in hand. Now, the question here is how can we build resiliency to the source? Now, it is Is someone working on how to build resiliency architecture to the to the infrastructure? Yes, and there is this IEEE body that is working. It's a very very interesting uh body. If you want to join, feel free. It's IEEE 1952. It talks about few resiliency levels, how to protect the source infrastructure, uh starting with the detection alert. What does it mean? Very simple. If there's any jamming or spoofing is detected, you detect, and then you advertise. That's the first level. That means you are [clears throat] you are able to understand that you are under threat. Fine. And then and then comes the second level, you know, recover, detect, and uh and alert or announce. So, that means that you're able to uh you're able to detect, and then, you know, you sneak in and see if the if the vulnerability is still alive or not. And then, if it's alive, yeah, you shut down. If it's not alive, yeah, you recover back. So, that's the second level of resiliency that has been offered. And the third one is resist, recover, detect. So, what does this mean? Resist is a This is where the oscillators come into picture saying that, "Okay, you found the problem. Then, okay, you shut down the port. You shut down the GNSS port, and try to hold the clock as much as you can." That's the second that's the third level of resiliency. Then comes the fourth level of resiliency withstand. This is this is most critical because now this is where the multiple sources come into picture. I mean you cannot rely your billion dollars of infrastructure assuming that one single source is good enough for you to deliver accurate time. Which should not be the case. So this is where alternate you know PNT sources like Leo satellite or a stream line or a stream coming from a NIST or local lab could really play a role. That's where that's how you could withstand a threat or vulnerability. And then the most important one is resiliency level five. This is where the zero trust architecture with multi-source combiner comes into picture. You will try to bring as many sources as you can. For example, the GNSS versions of multiple constellations. All of those you know five or six that are available on there. And then the Leo constellations and then the alternate source coming from the neighboring PTP then atomic clock. It's a combiner. And the zero trust is where where it validates each source and tries to provide you the relevant source that is required to meet the SLA of the end application. So that's where it gets in now. The good news is you know smart engineers like them try to build a card that is fully resilient to these vulnerabilities trying to get as"

<div class="takeaway"><b>小结</b>　IEEE P1952 的五级递进：RL1 检测并告警（知道自己在受威胁）→ RL2 恢复（判断脆弱性是否仍在，决定关闭还是恢复）→ RL3 抵御（关 GNSS 端口、靠振荡器保持）→ RL4 承受（引入 LEO、NIST/本地实验室等替代 PNT 源）→ RL5 验证（零信任多源组合，逐源校验并按 SLA 择优）。核心论点：100 亿美元的基础设施不能建立在"GNSS 免费"这一假设上。</div>

---

## 11　用时间卡实现 R-PNT

![A Timecard as a R-PNT solution：左侧多源与接口（ToD、GNSS、SyncE、PTP、LEO、1PPS）汇入时间卡；右侧为等级 1–5 的阶梯；下方注明多种振荡器选项以支撑长保持，以及直连主机 CPU 带来的多源比较与校验、AI/ML 异常（如 GNSS 欺骗）检测](images/11_11m05s.jpg)

……引入尽可能多的源，然后跑一个多源组合器，再跑一个验证器，从而构建零信任架构。这是基于我们在全球运行这些一级（Tier-1）网络的数百万小时经验，愿意给出的强烈建议之一。我要给你们看一个案例研究，非常有意思的案例。我们所做的是在一个大国的 985 个站点做了 GNSS 审计。

> "many sources as possible then run a what run a multi-source combiner then run a validator. Then you know that build a zero trust architecture. So this is one of the strong recommendation that we would like to give given our millions of hours of experience running these tier one networks in the world. I'm going to show you a case study which is very interesting case study. What we did was we did a GNSS audit"

<div class="takeaway"><b>小结</b>　实现路径与 P1952 等级一一对应：多源接口（ToD/GNSS/SyncE/PTP/LEO/1PPS）进卡 → 多源组合 → 校验 → 零信任。两个工程支点：可选振荡器决定保持时长（支撑 RL3），直连主机 CPU 使多源比对与 AI/ML 异常检测（如 GNSS 欺骗）成为可能。</div>

---

## 12　案例研究：现网 GNSS 干扰

![Case Study: GNSS Interference in a LIVE MOBILE NETWORK——某匿名一级运营商 985 个站点的 GNSS 审计：46.5% 的 grandmaster 受影响，24,022 个事件、月率 1.22%，89% 集中在受扰站点，欺骗平均时长 5.5–36.9 分钟（长 6.7 倍）；右侧为可操作性风险、完整性风险与基础设施响应](images/12_12m30s.jpg)

……在一个大国的 985 个站点。结果非常有意思，也非常令人警觉。有意思是什么意思呢——顺便说，我们分两个时期做这次审计：一个 3 个月的时期，然后间隔 6 个月，再一个 2 个月的时期。结果非常令人警觉。为什么？而且有意思的是——我再强调一遍，为什么？有意思是因为我们看到了几千个非常短暂的告警，6 秒到 6 分钟。6 秒到 6 分钟。

这是一个明确的信号——也许到这个时候我们大多数人已经知道这个事实了：GPS 信号很可能是你能接触到的最弱的信号。10⁻¹³ 毫瓦。弱的 GPS，或者说 10⁻¹⁶ 瓦。你能收到的最弱的信号。当然，这很自然，它来自 22,000 公里高的天上，很自然。那么这意味着什么？一个 1 瓦的干扰器或噪声，就能真正摧毁你试图建设的关键基础设施。不幸的是，那些假设 GPS 信号很强的系统架构师，无知程度非常高。好吧，不——有时候无知是福，因为你一开始并不知道威胁。

那么问题回到这里：运营商真的意识到了。呃，好的一面是——有意思的部分是——90% 到 95% 的告警并不影响业务。我们务实一点。为什么？因为振荡器。有些优秀的振荡器设计者——2 分钟。好。有些振荡器设计者能把时间保持在相当好的水平。但也有很多告警超过几个小时，有时是几天。那么，这是一个明确的警醒：你不能信任 GNSS 这个单一源，必须构建替代方案。替代方案有很多可用。但无论如何，我们要提请你们注意的一点是：GNSS 不能再被信任了。你必须构建韧性。

而现在，当你把这种脆弱性放到数据中心环境里——你会在 GNSS 上看到脆弱性，包括干扰、欺骗。顺便说，我们在接收 GNSS 时最被低估、最被忽视的一个因素之一，是信号干扰。而这是一种小型干扰……

> "in 985 locations in in a in a large country. The results are very interesting and alarming. What does it mean by interesting is during the By the way, we did this audit in two periods, a period of 3 months, then we gave a gap of 6 months, and again a period of 2 months. The results are very alarming. Why? And interesting again, I'm reiterating, why? It's interesting because we saw few thousands of alarms that are very short-lived. 6 seconds to 6 minutes. 6 seconds to 6 minutes. This is a clear indication, probably most of us may know by this fact by this time, GPS signal is probably the weakest possible signal that you could ever feel. 10 ^ - 13 mW. The weak GPS or 10 ^ - 16 W. Weakest possible signal that you could receive. Of course, it's natural coming from 22,000 km up in the sky. It's natural. Now, what does that mean? A 1 W 1 W jammer or a noise can really destroy a critical infrastructure that you're trying to build. Unfortunately, the ignorance levels are very very high with a very high, you know, system architect who assumes that the GPS signal is strong. Well, no, it's Sometimes ignorance is blessing. Because you don't know the threat first. Now, the question here, coming back to this, uh, the operator really realized, uh, well, well, one good thing What is the interesting part is 90 to 95% of the alarms are not service impacting. Let's be practical. Why? Well, the oscillator Some of these nice oscillator designers 2 minutes. Okay. Some of these oscillator designers, they're able to hold the time to a substantial good level, but there are many alarms that are beyond few hours, sometimes few days. Now, that's a clear eye-opener that you cannot trust GNSS single source. Need to build build an alternate. Alternate could be There are many alternates that are available. But anyway, the point that we are trying to bring to your notice is GNSS cannot be trusted anymore. You have to build resiliency. And now when you bring that particular vulnerability to a data center environment, you know, where you see a vulnerability on the GNSS that includes jamming, spoofing. By the way, one of the most important factor that we are underestimating, undermining while receiving the GNSS is the signal interference. And this is sort of a mini jamming. I"

<div class="takeaway"><b>小结</b>　实测数据：985 站点、跨 11 个月三段审计，46.5% 的 grandmaster 受影响，24,022 个事件（月率 1.22%），89% 集中在受扰站点；欺骗平均持续 5.5–36.9 分钟，比干扰长 6.7 倍。告警多为 6 秒–6 分钟，90–95% 不直接影响业务（靠振荡器保持），但仍有持续数小时至数天者——这正说明"单靠振荡器"不够，必须多源。</div>

---

## 13　GNSS：数据中心里的共享授时风险

![GNSS: A Shared Timing Risk in Data Centers：GNSS 天线在楼顶，面临干扰、欺骗、信号干扰与天线/接收机故障；一旦变为"不可信或不可用时间"，风险沿 PTP 授时网络（spine/leaf 交换机、主机服务器、NIC/IPU、GPU 集群）扩散，导致事件排序错误、日志与遥测不一致、认证与证书风险、数据库复制冲突、故障隔离延迟、SLA 与取证暴露](images/13_14m10s.jpg)

我不知道这还能不能叫干扰。也许干扰仍然是一种干扰，但是一种强干扰。而轻微的信号干扰实际上在周期性地影响服务。现在的问题是，在一级（Tier-1）环境里，任何告警都会一路向下渗透。现在，有些设备会基于产生的告警触发决策。所以，即使只是 6 分钟或 6 秒的告警，渗透到网络中也会产生运营影响。所以现在很清楚：GNSS 源上的脆弱性会产生运营后果。这一点需要被指出、需要被注意。那么现在，推荐的——我是说，这就是我们试图让 TAP、让时间卡……

> "I don't know if it's called jamming. Maybe jamming is is still an interference, but a strong interference. But the minor signal interference is really impacting the service periodically. Now, the problem is in in in in a tier one environment, any alarm is percolated down all the way. Now, there are certain appliances that can trigger the decision based on the alarms that are generated. So, even a 6 minutes or 6 seconds of of alarms that are percolated down the network have an impact, uh operational impact. So, now it's very clear that a vulnerability on the GNSS source is going to impact is going to have an operational consequence. That point needs to be made, you know, needs to be noted. So, now the recommended I mean, this is where we're trying to make the TCP the time card"

<div class="takeaway"><b>小结</b>　风险传导链条：屋顶单一 GNSS 参考 → 不可信时间 → 沿 PTP 网络扩散到交换机/服务器/NIC/GPU 集群 → 六类运营后果（事件排序、遥测、认证证书、数据库复制、故障隔离、SLA 与取证）。结论一句话：一个脆弱的参考会变成整个数据中心的故障域。</div>

---

## 14　受保护的时间卡：推荐的韧性特性

![Protected Timecard: Recommended Resilience Features：四组特性——①多样化源（多频多星座 GNSS、独立 PTP/PPS 输入、高稳定振荡器或原子参考、LEO）；②检测与校验（干扰与干扰检测、欺骗与时间跳变检测、跨源比对与置信度评分）；③安全与控制（安全启动与签名固件、硬件根信任、GNSS 保障、慢速攻击限制与确定性失效）；④观测与保障（实时相位与频率遥测、PTP 质量与保持状态、远程告警与开放 API）](images/14_15m15s.jpg)

……基于这些来自现场的教训，做出非常有韧性的（时间卡）。以及我们如何在各个层级保护时间卡。其中一个层级是构建多样化源，尽可能多的源。然后最重要的是检测与校验。这是关键。检测与校验对于 5 个 9 或 7 个 9 是关键。顺便说，很多数据中心预期要达到 7 个 9 的可用性，那真是——哇，那几乎等于无故障。但实际上还没到那一步，不过我们会达到。所以在这种情况下，为了满足这样的 SLA，你需要一个检测与校验机制，并与保障（assurance）结合。是的，这非常重要。

我是说，如果有机会，我一定会想监测网络中流动的每一个时间报文。这将帮助运营商或我们的数据中心识别拥塞点、偏斜点、以及那些真正会影响性能的诸多点位。好。那么，这是让时间卡内置这些功能、使其具备韧性的建议之一。然后，是的。那么，这就是一个提议中的……

> "very resilient uh based on these learnings from the field. And how do we protect uh the time card in in various you know, levels. And one of the level is try to build diverse sources, as many sources as we can. And then most important is detect and validate. This is the key. Detection and validation is a key for a 59 or a 59 or 79. By the way, many of the data centers are expected to have a 79s availability, which is wow. She's as good as no failure. But in practicality, it is not yet there, but we will get there. So, in this case, you still need a in in in order to meet such a SLA, you need a detection validation mechanism that's combined with, you know, assurance. Yeah, this is very important. I mean, given an opportunity, I would definitely want to monitor every time packet that is going through the network. This will help the operator or our data center to identify the congestion points, the skew points, the many points that would really, you know, impact the performance. Okay. Now, this is one of the recommendation uh to have the functionalities inbuilt in the time card to make it resilient. And then, yeah. So, this is a proposed"

<div class="takeaway"><b>小结</b>　四组推荐特性构成闭环：多样化源（多频多星座、独立 PTP/PPS、原子参考、LEO）解决"没有替代"；检测与校验解决"不知道被骗"；安全与控制解决"固件与根信任"；观测与保障解决"事后说不清"。核心判据是检测+校验+保障的组合，而非单一精度指标——因为 7 个 9 的可用性要求的是"可证明的可信"。</div>

---

## 15　提议的 TAP 贡献：GNSS 保障型 OCP 时间卡

![Proposed TAP contribution: a GNSS-assured OCP TimeCard：问题（让 GNSS 信任显式化——时间卡可能接受被干扰/欺骗/故障的 GNSS 而缺乏共享信任模型，一个公共外部参考可能同时影响多台服务器与授时节点）、Oscilloquartz 贡献（保障 profile + 参考实现：多源校验、完整性控制、韧性运行、开放可观测性）、以及参与路径（在 TAP 中开启保障用例、补充运营商/超大规模/芯片/OEM 需求、共建 profile 与参考设计、通过 TAP 验证互操作性）](images/15_16m20s.jpg)

……TAP 贡献，一句话概括。我们想把 GNSS 保障（GNSS assurance）带进时间卡。我们要保障源头。呃，所以欢迎大家参与进来。我们的提议主要在多源校验与集成、完整性控制，以及开放可观测性。呃，很乐意接受任何提问。

（主持人）好，一次、两次、三次。没有问题？好。谢谢你 Anil。谢谢你 Yair。谢谢。

> "TAP contribution in a nutshell. We would like to bring the Genesis assurance into a time card. We want to assure the source. Uh so, feel free to, you know, get involved into this. And our proposal is mostly on the multi-source validation and integration integrate controls and yeah, open observability. Uh happy to take any questions. Okay, going once, twice,  [snorts]  thrice. No questions?  Yeah. Thank you, Anil. Thank you, Yair.  Thank you."

<div class="takeaway"><b>小结</b>　提案要点：把"GNSS 是否可信"从隐含假设变成显式契约——在 OCP 时间卡上定义一个保障 profile 与参考实现（多源校验、完整性控制、韧性运行、开放可观测），并给出四步参与路径。注意页脚明确：这些是推荐特性，尚未纳入任何现行 OCP 认证。</div>

---

## 附录　时间轴

| 时间 | 内容 |
| --- | --- |
| 00:06 | 开场：本次覆盖时间卡定义、标准、用例与 PTM |
| 01:00 | 范式转移：专用设备 → 服务器内模块 |
| 01:42 | 标准：OCP TAP 与 IEEE P335 |
| 02:45 | 基本架构：振荡器、PLL、GNSS |
| 03:30 | 形态：PCIe / M.2 / USB |
| 04:21 | PTM 实测：PRTC-B，MTI 约 7ns 持续 3 天 |
| 05:45 | 用例：数据中心、金融、Open RAN、国防 |
| 06:21 | 电信：时间卡置于 DU，服务 DU 与 RU |
| 06:39 | 国防：加固平台的空闲 PCIe 槽位 |
| 07:09 | R-PNT：IEEE P1952 五级韧性 |
| 10:51 | 用时间卡实现多源组合与零信任 |
| 11:21 | 案例研究：985 站点 GNSS 审计 |
| 13:39 | GNSS 脆弱性的运营后果 |
| 14:39 | 受保护时间卡的四组特性 |
| 15:54 | 提议的 TAP 贡献与参与路径 |
| 16:46 | 结束 |
