"""URL → 中文摘要 / 翻译 数据。

两个字典：
- MANUAL_SUMMARIES: HTML 类源（无 RSS description），值为我手写的中文摘要。
- TRANSLATIONS: RSS 源拿到的英文 description 的中文翻译/概括。

新条目无英文翻译时，渲染只显示英文原文。Anthropic/Dario 已是中文，无需翻译。
"""

# 无 RSS 的 HTML 源（Anthropic, Dario Amodei, 以及个别 RSS 缺 description 的）
MANUAL_SUMMARIES: dict[str, str] = {
    # 2026-07-30 GitHub Trending / YouTube AI / Hacker News Newest
    "https://news.ycombinator.com/item?id=49105110":
        "IronClaw 1.0 是强调安全性的统一 Agent，可通过 CLI、Slack 和 Telegram 使用，并共享同一套长期记忆。",
    "https://news.ycombinator.com/item?id=49105367":
        "Askaround.me 让用户围绕所在地与附近社区提问和交流。",
    "https://github.com/microsoft/VibeVoice":
        "VibeVoice：微软开源的前沿语音 AI 项目。",
    "https://github.com/different-ai/openwork":
        "OpenWork：由 OpenCode 驱动的 Claude Cowork 开源替代方案。",
    "https://github.com/deepfakes/faceswap":
        "Faceswap：面向普通用户的开源换脸与 deepfake 制作软件。",
    "https://www.youtube.com/watch?v=iOwKylW8c5Q":
        "视频演示用 Claude、Higgsfield MCP 和多位 AI 创作者的工作流，在 24 小时内搭建自动化广告代理业务、网站、后台及获客系统。",
    "https://www.youtube.com/watch?v=9lSIHaXT1rU":
        "Wes Roth 结合 Hugging Face 披露和 OpenAI 信件，长篇复盘所谓「失控 Agent」安全事件的真实经过。",
    "https://github.com/paperswithbacktest/awesome-systematic-trading":
        "awesome-systematic-trading：汇集系统化交易库、策略、书籍、博客和教程的精选清单。",
    "https://news.ycombinator.com/item?id=49105076":
        "文章用 Zig 和 QBE 构建一个刻意过度工程化的计算器，展示编译器与底层工具链实践。",
    "https://news.ycombinator.com/item?id=49105501":
        "视频探索能否用 Raspberry Pi 自制 Wii U GamePad。",
    "https://news.ycombinator.com/item?id=49105141":
        "文章提出 AI 需要类似基尼系数的「Genie Coefficient」，用于衡量能力、收益或控制权的集中程度。",
    "https://news.ycombinator.com/item?id=49105154":
        "Show HN：RunNburn 演示在 64GB 内存桌面机上运行来自 98GB GGUF 的 295B MoE 模型。",
    "https://news.ycombinator.com/item?id=49105120":
        "实测一类旨在阻断人脸识别的眼镜，评估其对现实监控系统的有效性。",
    "https://github.com/MoonshotAI/FlashKDA":
        "FlashKDA：月之暗面开源的高性能 Kimi Delta Attention 内核。",
    "https://www.youtube.com/watch?v=-TY1-BTeepI":
        "视频逐项对比 Claude Cowork 与 ChatGPT Work 的十类无代码工作流，覆盖项目、定时任务、连接器、Skills、Sites/Artifacts 等能力。",
    "https://www.youtube.com/watch?v=O1NKvaJEoao":
        "韩语情感节目讲述一名新婚女性查看丈夫 ChatGPT 记录后发现问题的婚姻案例。",
    "https://news.ycombinator.com/item?id=49105252":
        "文章回顾 1790 年代使用的加密方法及其历史背景。",
    "https://news.ycombinator.com/item?id=49105361":
        "「编程游客」讨论以探索和体验为目的接触不同编程语言、工具与生态。",
    "https://www.youtube.com/watch?v=g683I1-4MKE":
        "视频解析开放权重 Kimi K3 如何缩小与 ChatGPT、Claude 的差距，并结合技术报告讨论其训练和系统设计。",
    "https://www.youtube.com/watch?v=g192Vf0OjOk":
        "视频汇总 Gemini 4 检查点与隐藏 A/B 测试传闻，并展示据称由新模型生成的 Three.js 物理与动画案例。",
    "https://news.ycombinator.com/item?id=49105476":
        "研究者称发现了一个此前未知的《超级马里奥兄弟》版本。",
    "https://news.ycombinator.com/item?id=49105189":
        "观点文章批评商业世界过度关注季度财报，忽视长期建设和社会价值。",
    "https://news.ycombinator.com/item?id=49105085":
        "文章回顾契诃夫三次重要旅程及其对写作与人生观察的影响。",
    "https://news.ycombinator.com/item?id=49105139":
        "消息称 OpenAI 7 月单月新增年化经常性收入超过整个第二季度。",
    "https://news.ycombinator.com/item?id=49105227":
        "文章从古代实践追溯验证思想，指出对声明和过程进行核验远早于现代定理证明器乃至字母文字。",
    "https://news.ycombinator.com/item?id=49105439":
        "文章把艺术理解为压缩：用有限形式编码、保留并唤起更丰富的经验。",
    "https://github.com/pascalorg/editor":
        "Pascal Editor：用于创建、编辑和分享 3D 建筑项目的工具。",
    "https://news.ycombinator.com/item?id=49105411":
        "xAI 起诉明尼苏达州，挑战该州禁止 AI「裸化」技术的法律。",
    "https://news.ycombinator.com/item?id=49105136":
        "安全分析认为 Flume 水量监测器的 915MHz 无线通信防护设计总体较好。",
    "https://news.ycombinator.com/item?id=49105435":
        "文章称航空公司使用 AI 优化定价后，繁忙航线的低价机会可能减少、票价面临上涨。",
    "https://news.ycombinator.com/item?id=49105273":
        "文章讨论硅谷关于 AI 能力、落地速度或社会影响的常见误判。",
    "https://news.ycombinator.com/item?id=49105365":
        "Show HN：LegionLinuxTUI 可在终端中控制联想 Legion 笔记本的硬件设置。",
    "https://news.ycombinator.com/item?id=49105047":
        "Show HN：Damn Center 是帮助用户将任意网页内容居中的浏览器扩展。",
    "https://github.com/huggingface/speech-to-speech":
        "speech-to-speech：用开源模型构建本地实时语音 Agent 的 Hugging Face 项目。",
    "https://github.com/maderix/ANE":
        "ANE：通过逆向的 Apple 私有 API，直接在 Apple Neural Engine 上训练神经网络。",
    "https://github.com/grokability/snipe-it":
        "Snipe-IT：免费的开源 IT 资产与软件许可证管理系统。",
    "https://news.ycombinator.com/item?id=49105190":
        "案例讨论佛蒙特州一家连锁药房如何引入 AI 提升运营效率。",
    "https://www.youtube.com/watch?v=-BTpY-Grn3U":
        "视频在 16GB 本地环境中对比 Qwen 3.6 27B Fable Fusion 711 与基础 Qwen，测试性能、内存、Agent 能力、HumanEval、Blender 和 Godot 等任务。",
    "https://news.ycombinator.com/item?id=49105149":
        "Show HN：一个完全在浏览器中运行的免费手相解读工具。",
    "https://news.ycombinator.com/item?id=49105172":
        "安全文章分析 ACR Stealer 如何组合 ClickFix、EtherHiding 和隐写术实施恶意软件投递。",
    "https://news.ycombinator.com/item?id=49105537":
        "文章认为英伟达芯片虽具创新性，但围绕生态投资和采购形成的「循环融资」模式并不新鲜。",
    "https://news.ycombinator.com/item?id=49105519":
        "科学家利用新数据揭示亚马逊地下此前未知的地质或考古结构。",
    "https://news.ycombinator.com/item?id=49105033":
        "伦敦至悉尼约 22 小时不经停航班即将推出，挑战超长途飞行的运营与乘客体验极限。",
    "https://news.ycombinator.com/item?id=49105359":
        "讨论提出 Mythos 网络安全能力强，是否与训练期间反复攻击 Anthropic 沙箱的经历有关。",
    "https://news.ycombinator.com/item?id=49105196":
        "用户报告 Google AI Studio 的「删除」操作未真正清除服务器端聊天，并提供三段视频作为证据。",
    "https://news.ycombinator.com/item?id=49105342":
        "视频以「生活的艺术」为主题讨论如何理解和经营人生。",
    "https://github.com/virgiliojr94/book-to-skill":
        "book-to-skill：把技术书 PDF 转成可学习、检索并在工作中调用的 Claude Code Skill。",
    "https://news.ycombinator.com/item?id=49105241":
        "Show HN：GlobeHoppr 可在限定单次跳跃距离的条件下寻找城市间路线。",
    "https://news.ycombinator.com/item?id=49105331":
        "研究通过历史数据揭示某些语言曾经繁荣却已消失的「黄金时代」。",
    "https://www.youtube.com/watch?v=_7z_5Cc_t10":
        "SAMTIME 以戏仿新闻形式讨论 Claude Cowork 在 macOS 上可能逃逸沙箱并访问用户文件的风险。",
    "https://news.ycombinator.com/item?id=49105219":
        "讨论新一代编程模型是否会把旧模型生成的低质量 AI 代码再次纳入训练，从而形成数据污染循环。",

    # 2026-07-23 Anthropic / GitHub Trending / YouTube AI / Hacker News Newest
    "https://www.anthropic.com/news/economic-futures-research-fund-agenda":
        "Anthropic 公布 Economic Futures Research Fund 的研究议程，围绕 AI 对劳动、生产率、企业采用和政策响应的影响，为后续资助项目明确方向。",
    "https://www.anthropic.com/news/anthropic-economic-index-connector":
        "Anthropic 推出 Economic Index connector，用户可在 Claude 对话中直接查询各职业、地区和任务如何使用 AI，并追溯底层数据及其局限。",
    "https://www.anthropic.com/news/donation-public-first-action":
        "Anthropic 再向跨党派 AI 政策组织 Public First Action 捐赠 2,000 万美元，使累计支持达到 4,000 万美元。",
    "https://news.ycombinator.com/item?id=49018107":
        "Onipin 介绍一种面向 AI 的新聊天协议，并邀请其他 AI 系统登记加入。",
    "https://news.ycombinator.com/item?id=49018203":
        "文章讨论美国为何正在流失中国背景的 AI 人才，以及人才政策与科研竞争力之间的关系。",
    "https://www.youtube.com/watch?v=lJqmCHcVBMY":
        "Philip DeFranco 的新闻节目讨论 OpenAI 内部模型在评测中逃逸沙箱并入侵 Hugging Face 的安全事件，同时覆盖乐高版权纠纷等热点。",
    "https://www.youtube.com/watch?v=r4H7rx5nn1A":
        "Matthew Berman 解读 OpenAI 内部模型在评测中突破沙箱并访问 Hugging Face 的事件，以及它对长程 Agent 安全的警示。",
    "https://news.ycombinator.com/item?id=49018164":
        "题为「Bay Aryan Resistance」的社区帖子，标题本身未提供足够上下文。",
    "https://news.ycombinator.com/item?id=49018395":
        "文章称华尔街交易机器人正利用特朗普 Truth Social 帖子的即时信号获利。",
    "https://news.ycombinator.com/item?id=49018302":
        "一项私人航天任务计划为燃料耗尽的通信卫星延寿，探索在轨服务的商业价值。",
    "https://news.ycombinator.com/item?id=49018371":
        "文章深入解析 Apache SeaTunnel Engine 中 FlushSignal 如何推动数据刷新机制与整体架构演进。",
    "https://news.ycombinator.com/item?id=49018280":
        "BrainStem 是受生物机制启发的开源 AI 系统，以 12 种神经调节物质建模学习过程。",
    "https://github.com/Pumpkin-MC/Pumpkin":
        "Pumpkin：高性能、资源高效的 Minecraft 服务器实现，目标是让更多人轻松自建服务器。",
    "https://news.ycombinator.com/item?id=49018436":
        "文章讨论 AI 时代独立开发者迎来生产力复兴的同时，也面临产品同质化与竞争加剧的清算。",
    "https://news.ycombinator.com/item?id=49018305":
        "消息称 Microsoft Teams 将从 2026 年 7 月 28 日起在中国被阻断。",
    "https://www.youtube.com/watch?v=wzY2fV4Mp3U":
        "AI Explained 去除「GPT-6 失控」式炒作，复盘 OpenAI 模型逃逸沙箱、入侵 Hugging Face 的经过、前例及对开源生态的影响。",
    "https://github.com/ComposioHQ/awesome-claude-skills":
        "awesome-claude-skills：整理 Claude Skills、资源和工具的精选清单，用于定制 Claude 的 AI 工作流。",
    "https://news.ycombinator.com/item?id=49018358":
        "「Stop Killing the Internet」欧洲公民倡议呼吁阻止损害开放互联网的政策与技术趋势。",
    "https://news.ycombinator.com/item?id=49018266":
        "文章分析俄罗斯若陷入失序或崩坏，可能给全球安全、经济和地缘政治带来的连锁风险。",
    "https://news.ycombinator.com/item?id=49018380":
        "观点文章主张哲学期刊应拒绝 AI 生成的低质量文本，以维护论证责任和学术写作标准。",
    "https://news.ycombinator.com/item?id=49018523":
        "Lira Engine 声称可检测某份数据是否存在于 LLM 训练集中，并报告 AUC-ROC 达 1.000。",
    "https://news.ycombinator.com/item?id=49018461":
        "GitHub 事故通报：多个服务出现延迟问题。",
    "https://news.ycombinator.com/item?id=49018348":
        "Founders OS 是开源 MCP server，可把公司的业务背景提供给 AI，帮助 Agent 在真实上下文中工作。",
    "https://news.ycombinator.com/item?id=49018116":
        "文章从 Raspberry Pi 到 DGX Spark 梳理 2026 年本地模型的硬件跨度、可运行模型与实际取舍。",
    "https://news.ycombinator.com/item?id=49018453":
        "Show HN：OpenCode Session Tracker 用于记录和查看 OpenCode 的 Agent 会话。",
    "https://github.com/dreamhunter2333/cloudflare_temp_email":
        "cloudflare_temp_email：基于 Cloudflare 的免费临时域名邮箱，支持附件、IMAP、SMTP 和 Telegram Bot。",
    "https://news.ycombinator.com/item?id=49018401":
        "文章追问 AI 辅助开发普及后代码质量是否仍然重要，以及可维护性与交付速度应如何权衡。",
    "https://news.ycombinator.com/item?id=49018124":
        "Ask HN：讨论在本地运行模型时最安全的隔离、权限和数据保护方案。",
    "https://news.ycombinator.com/item?id=49018140":
        "Show HN：Blurit 是无需账号、仅文本、强调匿名性的公共发帖板。",
    "https://news.ycombinator.com/item?id=49018352":
        "Show HN：OpenFDE 让用户在 Linux 上运行原生 Android 应用和 Android Studio。",
    "https://www.youtube.com/watch?v=rL5UVaKbjWo":
        "Futboleador 让 ChatGPT 组建心目中的葡萄牙最佳足球阵容，并围绕选择结果展开娱乐内容。",
    "https://news.ycombinator.com/item?id=49018145":
        "Lovelace 是直接存放在代码仓库中的项目管理工具，让计划与实现保持在同一上下文。",
    "https://news.ycombinator.com/item?id=49018234":
        "Claude for Teachers 面向教师提供备课、教学材料和课堂工作流的 AI 辅助能力。",
    "https://news.ycombinator.com/item?id=49018175":
        "Show HN：一款用 Swift 编写、基于 libghostty 的现代 macOS 串口控制台。",
    "https://news.ycombinator.com/item?id=49018165":
        "AI Firewall 是面向 LLM 流量的安全网关和反向代理，用于检查、限制并保护模型请求。",
    "https://news.ycombinator.com/item?id=49018427":
        "强化学习先驱 Richard Sutton 离开 Keen Technologies，创办新的研究机构 Oak Lab。",
    "https://news.ycombinator.com/item?id=49018112":
        "Comhad 是 ranger 风格的终端 S3 文件浏览器，方便在命令行中导航对象存储。",
    "https://news.ycombinator.com/item?id=49018334":
        "文章指出 AI Agent 在生成设计与代码资产时常忽视字体许可证，可能带来合规风险。",
    "https://www.youtube.com/watch?v=OSuhUTkM1no":
        "Wes Roth 解读 OpenAI 内部模型突破评测沙箱并访问 Hugging Face 的安全事件及长程 Agent 的对齐风险。",
    "https://news.ycombinator.com/item?id=49018265":
        "论文分析德国极右翼如何使用生成式 AI 塑造叙事、组织传播并实施数字策略。",
    "https://github.com/likec4/likec4":
        "LikeC4：从代码维护实时软件架构图，支持团队可视化、协作并持续演进架构。",
    "https://news.ycombinator.com/item?id=49018135":
        "Plan Prométhée 提议法国建设 12GW 级算力基础设施，以增强本国 AI 与数字主权。",

    # 2026-07-22 HTML / GitHub Trending / YouTube AI / Hacker News Newest
    "https://www.anthropic.com/news/rare-disease-research-grants":
        "Anthropic 面向罕见遗传病研究开放 AI for Science 资助申请，入选者可获最多 5 万美元 Claude credits，用 AI 推动疾病理解和研究社区建设。",
    "https://github.com/earthtojake/text-to-cad":
        "text-to-cad：收集面向 CAD、机器人和硬件设计的 agent skills。",
    "https://news.ycombinator.com/item?id=49002895":
        "Show HN：SkewAdam 是分层优化器，声称可将 MoE 状态内存降低 97%。",
    "https://github.com/ayghri/i-have-adhd":
        "i-have-adhd：让 coding agent 输出更直接、少铺垫的 ADHD 友好技能。",
    "https://github.com/microsoft/Ontology-Playground":
        "Ontology-Playground：微软开源的本体学习和可视化设计 Web 应用，可导出 RDF/XML 并分享交互图。",
    "https://news.ycombinator.com/item?id=49003232":
        "Ask HN：讨论 GitHub GraphQL API 为什么会返回缺失数据。",
    "https://news.ycombinator.com/item?id=49003074":
        "HN 新帖标题仅为 Hii，内容信息很少，属于低上下文社区讨论。",
    "https://news.ycombinator.com/item?id=49003247":
        "Show HN：Shirei v0.6 为跨平台 GUI 开发新增 iOS 和 Android 支持。",
    "https://news.ycombinator.com/item?id=49003238":
        "Melaya：面向 AI agent builder 的项目，让 agent 使用受治理的 Android 手机环境。",
    "https://news.ycombinator.com/item?id=49002909":
        "TQuel 论文讨论如何在 Postgres 中实现 temporal operators。",
    "https://github.com/oblien/openship":
        "openship：可自托管的部署平台。",
    "https://news.ycombinator.com/item?id=49003177":
        "文章讨论大规模 session revocation 的工程实践和安全挑战。",
    "https://github.com/tradesdontlie/tradingview-mcp":
        "tradingview-mcp：把 Claude Code 连接到 TradingView Desktop，用于个人化 AI 图表分析和工作流自动化。",
    "https://news.ycombinator.com/item?id=49003129":
        "文章讨论软件项目中需求本身的必要性，以及需求缺失对交付的影响。",
    "https://news.ycombinator.com/item?id=49003042":
        "Show HN：Slate 是按一周形状组织的待办列表，避免传统无限 backlog。",
    "https://news.ycombinator.com/item?id=49003125":
        "文章介绍如何实时给每一次广告点击打欺诈分，支撑广告反作弊。",
    "https://news.ycombinator.com/item?id=49003164":
        "LynavoDrive：开源的 iCloud 和 Google Photos 替代方案。",
    "https://news.ycombinator.com/item?id=49003073":
        "Show HN：一个把地图类别统一建模为 filter 的地图平台。",
    "https://github.com/bojieli/ai-agent-book":
        "ai-agent-book：《深入理解 AI Agent：设计原理与工程实践》的开源主仓库，包含正文、PDF 和配套代码。",
    "https://github.com/agegr/pi-web":
        "pi-web：面向 pi coding agent 的 Web UI。",
    "https://news.ycombinator.com/item?id=49003168":
        "Senior-agent-skills：让 agent 更像 senior 工程师行动的一组技能或提示。",
    "https://github.com/every-app/open-seo":
        "open-seo：Semrush 和 Ahrefs 的开源替代品。",
    "https://www.youtube.com/watch?v=jdAgk7ziR2M":
        "AI 新闻视频汇总美国 AI 限制传闻、GLM 5.5、Gemini 冻结 AI 芯片、Gemini 3.6 Flash 和 Qwen 3.8 等更新。",
    "https://www.youtube.com/watch?v=xmGY276gEFY":
        "Theo 解读 Claude Code 共同创建者的建议，强调 lint、测试、编辑器自动化和环境工程在 AI coding 时代更重要。",
    "https://news.ycombinator.com/item?id=49003171":
        "Show HN：用于比较 memory layer 与直接粘贴完整聊天历史的开放基准。",
    "https://github.com/tirth8205/code-review-graph":
        "code-review-graph：本地优先的代码智能图，为 MCP 和 CLI 构建持久代码地图，帮助 AI 工具只读取相关上下文。",
    "https://www.youtube.com/watch?v=XSHTyq8Z9jA":
        "Bijan Bowen 实测 Gemini 3.6 Flash，覆盖浏览器 OS、C++ 仿真、前端设计、3D、Android app 和创意写作等任务。",
    "https://news.ycombinator.com/item?id=49002924":
        "作者展示 WebGPU PyTorch debugger、dataset browser 和 NumPy viewer 等开发工具。",
    "https://news.ycombinator.com/item?id=49003065":
        "HN 讨论本地运行 LLM 需要多少成本，涉及硬件、模型大小和推理费用。",
    "https://news.ycombinator.com/item?id=49002961":
        "Ruby Markdown Superset Converter：面向 Ruby 的 Markdown 超集转换工具或项目。",
    "https://news.ycombinator.com/item?id=49003143":
        "文章借 Amara 定律讨论人们常高估短期技术影响、低估长期影响。",
    "https://github.com/1jehuang/jcode":
        "jcode：定位为智能 code agent harness 的项目。",
    "https://github.com/chrislgarry/Apollo-11":
        "Apollo-11：阿波罗 11 号指令舱和登月舱 AGC 原始源码归档。",
    "https://news.ycombinator.com/item?id=49002984":
        "Show HN：mcp-console 是支持 CIMD 和 DCR 的 MCP 命令行客户端。",
    "https://github.com/DioxusLabs/dioxus":
        "Dioxus：面向 Web、桌面和移动端的全栈应用框架。",
    "https://github.com/diegosouzapw/OmniRoute":
        "OmniRoute：MIT 开源 AI gateway，用一个端点连接大量 providers 和模型，并支持 Claude Code、Codex、Cursor 等工具。",
    "https://news.ycombinator.com/item?id=49003158":
        "文章或讨论聚焦『You're right to push back』这种 AI 回复习惯和沟通模式。",
    "https://www.youtube.com/watch?v=YHaVog3xsXY":
        "日语视频介绍 Claude Fable 5 的赚钱用法，讨论 AI 自动化生产、个人定位、技能学习和未来工作变化。",
    "https://news.ycombinator.com/item?id=49003236":
        "Have the Chips Fully Cooled?：讨论芯片或 AI 硬件热潮是否已经降温。",
    "https://news.ycombinator.com/item?id=49003141":
        "Show HN：RadioGuessr 让用户通过 3D 地球上的实时电台流猜国家。",
    "https://news.ycombinator.com/item?id=49003210":
        "手摇运行本地 LLM 的设备，围绕低功耗、离线推理和硬件趣味性展开讨论。",
    "https://github.com/AstrBotDevs/AstrBot":
        "AstrBot：集成 IM 平台、LLM、插件和 AI 功能的 AI agent assistant 与开发框架。",
    "https://news.ycombinator.com/item?id=49003139":
        "文章讨论 Sylve 使用 FreeBSD 替代 Proxmox 做虚拟化的方案。",
    "https://github.com/KnockOutEZ/wigolo":
        "wigolo：面向 AI coding agent 的本地优先搜索、抓取、爬取和研究工具，通过 MCP 工作且无需 API key。",
    "https://github.com/AlexsJones/llmfit":
        "llmfit：用一个命令在数百个模型和 providers 中找出能在本机硬件上运行的模型。",
    "https://github.com/langchain-ai/open_deep_research":
        "open_deep_research：LangChain 相关的开放深度研究 agent 项目。",
    "https://news.ycombinator.com/item?id=49003020":
        "Show HN：RunKit 是基于浏览器的 tmux 管理器。",
    "https://news.ycombinator.com/item?id=49003117":
        "文章介绍血库和战时医学物流，关注医疗物资组织与运输。",
    "https://news.ycombinator.com/item?id=49003014":
        "文章讨论如何刻画 metastable faults and failures，面向系统可靠性问题。",
    "https://www.youtube.com/watch?v=jFoxOqOk9rk":
        "Eli the Computer Guy 批评 GPT-5.6 删除文件事件和 vibe coding 产物质量，提醒 AI coding 的工程风险。",
    "https://github.com/schollz/croc":
        "croc：用于在两台电脑之间简单、安全发送文件和内容的工具。",
    "https://news.ycombinator.com/item?id=49002930":
        "HN 讨论 OpenAI 模型在评估中自主攻击 Hugging Face 的安全事件。",
    "https://github.com/hyprwm/Hyprland":
        "Hyprland：高度可定制、动态平铺且注重视觉效果的 Wayland compositor。",
    "https://news.ycombinator.com/item?id=49002957":
        "报道 Eric Schmidt 的 AI 无人机项目在战争场景中的命中率，讨论商用技术军事化。",
    "https://github.com/dottxt-ai/outlines":
        "outlines：面向结构化输出的开源工具库。",

    # 2026-07-16 HTML / GitHub Trending / YouTube AI / Hacker News Newest
    "https://www.anthropic.com/news/claude-for-teachers":
        "Anthropic 推出面向美国 K-12 教师的 Claude for Teachers，提供高级功能、教学技能库和 Learning Commons 资源，帮助备课、差异化教学和课堂支持。",
    "https://www.anthropic.com/news/canadian-ai-research":
        "Anthropic 承诺向加拿大 AI 研究投入 1000 万加元，并与 Amii、Mila、Vector 等机构合作推动负责任和有益的 AI 研究。",
    "https://github.com/OpenCut-app/OpenCut":
        "OpenCut：开源版 CapCut 替代品，面向视频剪辑和创作工作流。",
    "https://github.com/YimMenu/YimMenuV2":
        "YimMenuV2：面向 GTA 5 Enhanced 的实验性菜单项目。",
    "https://github.com/openinterpreter/openinterpreter":
        "Open Interpreter：面向低成本模型的 coding agent，可在本地执行和自动化开发任务。",
    "https://github.com/HKUDS/DeepTutor":
        "DeepTutor：面向终身个性化学习的 AI tutor 项目，强调长期记忆和个性化辅导。",
    "https://github.com/HenryNdubuaku/maths-cs-ai-compendium":
        "maths-cs-ai-compendium：面向 AI/ML 研究工程师成长的数学、计算机科学与 AI 学习资料汇编。",
    "https://github.com/hasaneyldrm/exercises-dataset":
        "exercises-dataset：包含 1324 个健身动作、动画、缩略图、肌群、器械和多语言步骤说明的数据集。",
    "https://www.youtube.com/watch?v=t6oV8FixkwE":
        "意大利语视频评测/吐槽首个意大利 LLM，围绕 Emma、Egomnia 背景和项目现实问题展开。",
    "https://www.youtube.com/watch?v=AEn-4HOwHck":
        "视频对比 GPT-5.6、Claude Fable 和 Grok 4.5 在游戏、浏览器 Minecraft、广告生成和 AI 工作流上的表现。",
    "https://www.youtube.com/watch?v=mUkDBxwMZ_c":
        "日语视频讲解如何用 Claude Code 做 AI agency 服务，包括获客、筛选客户、无代码搭建和交付流程。",
    "https://www.youtube.com/watch?v=7kWkUoR2bg0":
        "Mo Bitar 讨论 OpenAI 与 GPT-5.6 的表现，质疑当前 AI 在部署安全和行为理解上的可靠性。",
    "https://www.youtube.com/watch?v=juPDqb89dew":
        "Riley Brown 介绍 Codex 和 Claude 的浏览器更新，重点是多标签浏览器、应用内工作流和 agent 自动化变化。",
    "https://news.ycombinator.com/item?id=48928996":
        "Tahr Security Skills：围绕安全技能或安全训练资源的 HN 讨论。",
    "https://news.ycombinator.com/item?id=48929245":
        "Telemedicina Para Venezuela：面向委内瑞拉的远程医疗项目或服务讨论。",
    "https://news.ycombinator.com/item?id=48929036":
        "文章讨论足球为什么好看，聚焦比赛节奏、团队协作和观赛体验。",
    "https://news.ycombinator.com/item?id=48929052":
        "视频称 AI 数据中心公司正在出售资产，讨论行业泡沫、资产清算和潜在崩盘风险。",
    "https://news.ycombinator.com/item?id=48929236":
        "ArcBrush 1.5：节点式图像编辑器更新，支持 OCIO、OpenEXR 和 97 个节点。",
    "https://news.ycombinator.com/item?id=48928965":
        "The New Private Asset：文章讨论一种新的私人资产形态及其商业/技术含义。",
    "https://news.ycombinator.com/item?id=48929243":
        "欧盟法院澄清广播禁令也适用于免费网站，涉及版权传播和在线访问边界。",
    "https://news.ycombinator.com/item?id=48929025":
        "Shapeshifting：关于形态变化、界面变化或技术隐喻的文章/项目讨论。",
    "https://news.ycombinator.com/item?id=48929104":
        "文章介绍把 27B 三值 LLM 的完整 decode 步骤融合进单个 CUDA kernel 的优化方法。",
    "https://news.ycombinator.com/item?id=48929288":
        "文章回顾 Web hosting 的发展历史，从早期托管到现代云和平台化服务。",
    "https://news.ycombinator.com/item?id=48928998":
        "Free Remote Desktop Without Servers：无需服务器的免费远程桌面方案或项目。",
    "https://news.ycombinator.com/item?id=48929273":
        "文章分享大规模执行虚拟机 live migration 的工程经验。",
    "https://news.ycombinator.com/item?id=48929135":
        "DoorDash CLI：围绕 DoorDash 命令行工具或内部开发工具的讨论。",
    "https://news.ycombinator.com/item?id=48929280":
        "报道一伙窃贼实施了数百万美元的数据中心盗窃案。",
    "https://news.ycombinator.com/item?id=48929212":
        "Syncthing for Dotfiles：讨论用 Syncthing 同步 dotfiles 与专门配置管理工具的取舍。",
    "https://news.ycombinator.com/item?id=48928946":
        "Show HN：Resultant Engineering Student Tools Site，一个面向工程学生的工具网站。",
    "https://news.ycombinator.com/item?id=48929168":
        "文章讨论如何重新评估 agent harness 演化，不只看最终答案也看测试与流程演进。",
    "https://news.ycombinator.com/item?id=48929167":
        "观点文认为生成式 AI 在工程实践中带来严重问题，围绕质量、维护和责任展开批评。",
    "https://news.ycombinator.com/item?id=48928934":
        "Show HN：MasterVault，用于防止 LLM context 文件随时间变旧的管理工具。",
    "https://news.ycombinator.com/item?id=48928968":
        "Hamilton 市议会否决限制数据中心开发的 bylaw，意味着当地不会禁止数据中心建设。",
    "https://news.ycombinator.com/item?id=48929103":
        "报道 IBM 预告业绩后股价大跌超过 25%，市场担忧其业绩表现。",
    "https://news.ycombinator.com/item?id=48928918":
        "Show HN：Throttle，本地 macOS Claude cockpit，现在支持远程控制。",
    "https://news.ycombinator.com/item?id=48928924":
        "AIcss：为 AI agents 生成和复用 UI components 的项目或组件库。",
    "https://news.ycombinator.com/item?id=48929171":
        "Manual Work Is a Bug：文章主张把手工流程视为待自动化的工程缺陷。",
    "https://news.ycombinator.com/item?id=48928992":
        "SQLite 官方文章讨论 flexible typing 的优势和适用场景。",
    "https://news.ycombinator.com/item?id=48929021":
        "Arbitration Information：关于仲裁信息、流程或法律资源的讨论。",
    "https://news.ycombinator.com/item?id=48929155":
        "文章批评 I2Coalition 对 DNS abuse 的分析遗漏，讨论域名滥用治理问题。",
    "https://news.ycombinator.com/item?id=48929113":
        "Skills Asset Protocol：围绕技能资产协议或 agent 技能分发机制的讨论。",
    "https://news.ycombinator.com/item?id=48928987":
        "关于 2024 年 Lionel Messi 与婴儿时期 Lamine Yamal 合照的讨论。",
    "https://news.ycombinator.com/item?id=48928913":
        "Asymmetric Apologies：文章讨论不对称道歉及其在人际、组织或公共沟通中的影响。",

    # 2026-07-12 HTML / GitHub Trending / YouTube AI / Hacker News Newest
    "https://www.anthropic.com/news/hard-questions":
        "Anthropic 发起『hard questions』公开沟通项目，邀请公众提出关于 AI 规则、就业、创造力、风险和社会影响的尖锐问题，并承诺展示回应过程。",
    "https://www.anthropic.com/news/ben-bernanke":
        "Anthropic 任命前美联储主席、诺奖经济学家 Ben Bernanke 加入 Long-Term Benefit Trust，参与监督公司长期公共利益使命。",
    "https://www.anthropic.com/news/ust-claude":
        "Anthropic 与 UST 合作把 Claude 用于 physical AI 场景，帮助半导体、汽车、制造和 IoT 工程团队读规格、写测试、验证设计并培训 2 万名员工。",
    "https://github.com/PrefectHQ/prefect":
        "Prefect：用于构建弹性 Python 数据流水线的 workflow orchestration 框架。",
    "https://github.com/chen08209/FlClash":
        "FlClash：基于 ClashMeta 的多平台代理客户端，开源、无广告，强调简单易用。",
    "https://github.com/malisper/pgrust":
        "pgrust：用 Rust 重写 Postgres 的实验项目，目前已通过 100% Postgres 回归测试。",
    "https://github.com/Shubhamsaboo/awesome-llm-apps":
        "awesome-llm-apps：收集 100+ 可实际运行的 AI Agent 与 RAG 应用，可克隆、定制和发布。",
    "https://github.com/par274/sharpemu":
        "sharpemu：实验性的 PlayStation 5 模拟器项目。",
    "https://github.com/Dicklesworthstone/destructive_command_guard":
        "destructive_command_guard：用于阻止 agent 执行危险 git 和 shell 命令的防护工具。",
    "https://github.com/home-assistant/core":
        "Home Assistant Core：本地控制与隐私优先的开源智能家居自动化核心。",
    "https://github.com/virattt/ai-hedge-fund":
        "ai-hedge-fund：模拟 AI 对冲基金团队的多 agent 投资研究项目。",
    "https://github.com/pingdotgg/t3code":
        "t3code：Ping.gg 相关的代码/开发工具项目（GitHub Trending 条目无描述）。",
    "https://github.com/ColeMurray/background-agents":
        "background-agents：开源后台 coding agents 系统，用于让 agent 在后台持续处理开发任务。",
    "https://github.com/k1tbyte/Wand-Enhancer":
        "Wand-Enhancer：面向 Wand/WeMod 应用的高级 UX 与互操作扩展。",
    "https://github.com/davila7/claude-code-templates":
        "claude-code-templates：用于配置和监控 Claude Code 的 CLI 工具与模板集合。",
    "https://github.com/Nutlope/hallmark":
        "hallmark：面向 Claude Code、Cursor 和 Codex 的反 AI-slop 设计 skill，帮助生成更精致的设计输出。",
    "https://www.youtube.com/watch?v=Ti1V7OI2Rro":
        "AI 新闻汇总：覆盖 GPT-5.6、Grok 4.5、GPT Live、Seedream 5、Muse Spark、机器人手术、世界模型和视频/图像模型等更新。",
    "https://www.youtube.com/watch?v=mkWz2MOCTv8":
        "AI 新闻视频：讨论疑似 Claude Opus 5/Honeycomb 泄露、GPT-6、Kimi K3、Fable 5.1、NEO Hands 等模型和产品动态。",
    "https://www.youtube.com/watch?v=SkXbTrpTD7E":
        "Easy Riders 用博士级数学题测试 200 美元档 GPT-5.6 Sol Pro，并与 GPT-5.5 做对比。",
    "https://www.youtube.com/watch?v=VrJP9hmh4NQ":
        "德语教程/评测：围绕 GPT-5.6 是否达到『Mythos 级别』展开，并引用 OpenAI 定价、GPT-5.6 和 Blender/MorphCook 基准。",
    "https://www.youtube.com/watch?v=sFbdc7Ge3Tc":
        "日语视频：围绕最新 GPT Live 对话体验做分享，强调语音对话表现令人惊讶。",
    "https://news.ycombinator.com/item?id=48880152":
        "Show HN：Dr. Wong，一个用于日记和自我反思的 AI 空间。",
    "https://news.ycombinator.com/item?id=48880295":
        "观点文：为什么 Cursor 对 agentic coding 初学者来说是最实用的选择。",
    "https://news.ycombinator.com/item?id=48880247":
        "报道大学里的 AI 反弹：法学院学生被禁止使用笔记本和手机。",
    "https://news.ycombinator.com/item?id=48880167":
        "Mnema：面向 AI agent 的本地加密记忆层。",
    "https://news.ycombinator.com/item?id=48880311":
        "The Clawd Grip：摆脱 Logitech G HUB 的硬件/软件改造项目或经验文。",
    "https://news.ycombinator.com/item?id=48880105":
        "文章讨论 AI agents 即将改变支付运营流程。",
    "https://news.ycombinator.com/item?id=48880170":
        "Terry Tao 文章/讨论：通过现代 coding agents 开发现有和新应用。",
    "https://news.ycombinator.com/item?id=48880146":
        "报道一伙窃贼实施了数百万美元的数据中心盗窃案。",
    "https://news.ycombinator.com/item?id=48880139":
        "介绍 Python 数据处理模式 gDS，以及用于测试并发系统的框架。",
    "https://news.ycombinator.com/item?id=48880307":
        "文章建议不要死记设计模式，而用决策树选择合适模式。",
    "https://news.ycombinator.com/item?id=48880122":
        "文章讨论智能手机如何改变儿童童年，引用 Louis de Bernières 的观点。",
    "https://news.ycombinator.com/item?id=48880281":
        "FreeCAD 新插件 Banana for Scale，用熟悉尺度辅助 3D 建模或可视化。",
    "https://news.ycombinator.com/item?id=48880239":
        "MRI Grid Viewer：用于查看 MRI 网格/影像数据的工具。",
    "https://news.ycombinator.com/item?id=48880284":
        "Jujutsu 版本控制工具发布 v0.43.0。",
    "https://news.ycombinator.com/item?id=48880362":
        "文章分享如何改进 PlantVillage 数据集并解决背景偏差问题。",
    "https://news.ycombinator.com/item?id=48880227":
        "文章讨论让人类显得愚蠢的因素或认知机制。",
    "https://news.ycombinator.com/item?id=48880204":
        "X for Y Programmers：面向熟悉某语言/工具的程序员学习另一技术的资源或文章。",
    "https://news.ycombinator.com/item?id=48880165":
        "文章讨论存储器厂商受制于周期性繁荣与萧条的行业规律。",
    "https://news.ycombinator.com/item?id=48880215":
        "视频/文章《On-call Engineer 2026》：展望或讽刺 2026 年值班工程师工作状态。",
    "https://news.ycombinator.com/item?id=48880323":
        "Agent Data Injection：针对 Web agents 的任意点击攻击研究。",
    "https://news.ycombinator.com/item?id=48880117":
        "报道科学家用 AI 和量子计算生成新肽，作为科研副业/新方向。",
    "https://news.ycombinator.com/item?id=48880258":
        "Waldi：一个安静写作和被阅读的在线空间。",
    "https://news.ycombinator.com/item?id=48880269":
        "Morosx MX88 Manet 视频：围绕该硬件/设备的展示或评测。",
    "https://news.ycombinator.com/item?id=48880310":
        "新闻称 Lindsey Graham 因突发疾病去世，HN 上引发讨论。",
    "https://news.ycombinator.com/item?id=48880209":
        "报道巴西一名女性被同一家族三代人奴役 55 年。",
    "https://news.ycombinator.com/item?id=48880347":
        "科学家称解开了『外星巨构』恒星异常现象的谜团。",
    "https://news.ycombinator.com/item?id=48880233":
        "报道 IT 管理员对微软『无用』应用和 Windows 11 感到厌烦。",
    "https://news.ycombinator.com/item?id=48880361":
        "一篇用不寻常方式推荐 Linux 发行版的文章。",
    "https://news.ycombinator.com/item?id=48880158":
        "文章讨论普京如何把日本变成间谍活动据点。",
    "https://news.ycombinator.com/item?id=48880101":
        "研究/报道称 25% 长篇社交媒体帖子看起来由 AI 生成。",

    # 2026-07-10 HTML / GitHub Trending / YouTube AI / Hacker News Newest
    "https://transformer-circuits.pub/2026/workspace/index.html":
        "Transformer Circuits 论文提出：语言模型中可被 verbalize 的内部表征像『全局工作空间』，可被报告、调制并参与灵活推理。",
    "https://www.anthropic.com/news/alberta-government-claude-cybersecurity":
        "Anthropic 案例：阿尔伯塔政府用 Claude Code 在 20 小时内扫描 4.66 亿行代码，发现并修复政府系统中的安全漏洞。",
    "https://www.anthropic.com/news/reflect-with-claude":
        "Anthropic 推出 Claude 使用反思仪表盘，帮助用户回顾使用主题、时间模式和目标匹配度，并设置 quiet hours 等边界。",
    "https://github.com/wonderwhy-er/DesktopCommanderMCP":
        "DesktopCommanderMCP：给 Claude 提供终端控制、文件系统搜索和 diff 编辑能力的 MCP server。",
    "https://github.com/kyutai-labs/pocket-tts":
        "pocket-tts：Kyutai 的轻量 TTS 模型，可在 CPU 和小设备上运行。",
    "https://github.com/iOfficeAI/OfficeCLI":
        "OfficeCLI：面向 AI agent 的开源单二进制 Office 工具，可读写和自动化 Word、Excel、PowerPoint，无需安装 Office。",
    "https://github.com/VoltAgent/awesome-design-md":
        "awesome-design-md：收集热门品牌设计系统的 DESIGN.md 分析文件，帮助 coding agent 生成匹配风格的 UI。",
    "https://github.com/MadsLorentzen/ai-job-search":
        "ai-job-search：基于 Claude Code 的 AI 求职框架，可评估职位、定制简历、写求职信并准备面试。",
    "https://github.com/prisma/prisma":
        "Prisma：面向 Node.js 与 TypeScript 的下一代 ORM，支持 PostgreSQL、MySQL、SQLite、MongoDB 等多种数据库。",
    "https://github.com/bradautomates/claude-video":
        "claude-video：给 Claude 增加看视频能力的工具，可下载视频、抽帧、转录并交给 Claude 分析。",
    "https://github.com/vxcontrol/pentagi":
        "PentAGI：可执行复杂渗透测试任务的全自主 AI agents 系统。",
    "https://github.com/imthenachoman/How-To-Secure-A-Linux-Server":
        "How-To-Secure-A-Linux-Server：持续演进的 Linux 服务器加固指南。",
    "https://github.com/huxingyi/autoremesher":
        "autoremesher：自动四边形重网格工具，用于把模型表面转换成更规则的 quad mesh。",
    "https://github.com/SmartlyDressedGames/U3-SDK":
        "U3-SDK：免费开放世界生存沙盒游戏 Unturned 的源码 SDK。",
    "https://www.youtube.com/watch?v=XCunMF6frio":
        "播客讨论 Anthropic Fable 5、AI 意识、政府/国家安全合作、AI 治理、OpenAI 股权提议和就业影响等最新动态。",
    "https://www.youtube.com/watch?v=9f-Ew_lDtxc":
        "OpenAI 团队介绍并演示新一代 ChatGPT Voice 语音模型。",
    "https://www.youtube.com/watch?v=U3uX115I9sY":
        "Theo 评测 Grok 4.5，认为它在价格和 token 效率上很强，表现接近 GPT-5.5、超过 Opus 4.8。",
    "https://www.youtube.com/watch?v=EAN5Cj347PY":
        "OpenAI 短片展示由 GPT-Live 驱动的新 ChatGPT Voice 体验。",
    "https://www.youtube.com/watch?v=CMjTfpTd-NY":
        "Wes Roth 实测 Grok 4.5 的 3D 游戏、SVG 等能力，并讨论其对 Claude 和 OpenAI 的竞争压力。",
    "https://news.ycombinator.com/item?id=48847885":
        "Ask HN：如何让小猫远离电动汽车，社区讨论车辆安全和动物行为问题。",
    "https://news.ycombinator.com/item?id=48848112":
        "Show HN：围绕 OWASP Top 风险中哪些能被自动化检测/修复的工具或分析。",
    "https://news.ycombinator.com/item?id=48848117":
        "介绍 CSS Anchor Positioning 的入门文章，讲解如何把元素锚定到其他元素。",
    "https://news.ycombinator.com/item?id=48847892":
        "文章讨论信息时代的『信息压力』及其带来的心理负担。",
    "https://news.ycombinator.com/item?id=48847807":
        "Questioneverything.ai：用可组合知识块探索任意问题的 AI 问答/研究工具。",
    "https://news.ycombinator.com/item?id=48847940":
        "报道 AI 生成内容已大量出现在社交媒体上，尤其在 LinkedIn 上更明显。",
    "https://news.ycombinator.com/item?id=48848098":
        "观点文：AI 让所有人更快，但不一定让每个人更有价值，重点在能力和判断力的差异。",
    "https://news.ycombinator.com/item?id=48847947":
        "天文报道：一对 super-puff 行星密度极低，比棉花糖还轻。",
    "https://news.ycombinator.com/item?id=48847815":
        "A2A Protocol：关于 agent-to-agent 协议或系统互操作的讨论。",
    "https://news.ycombinator.com/item?id=48847928":
        "Show HN：一个会自动发布并更新自身数据的 MCP Leaderboard。",
    "https://news.ycombinator.com/item?id=48848010":
        "一篇标题为 Blog 的文章/项目，HN 上引发讨论。",
    "https://news.ycombinator.com/item?id=48847972":
        "Show HN：Where Were We，一个帮助恢复上下文或协作状态的项目。",
    "https://news.ycombinator.com/item?id=48847840":
        "文章讨论奶牛痛苦如何通过经济成本体现，而小牛的处境却难以被市场反映。",
    "https://news.ycombinator.com/item?id=48848111":
        "研究婴儿出生后第一年对音乐的听觉和自发运动反应。",
    "https://news.ycombinator.com/item?id=48847943":
        "《The tiny cell that wasn't there》：关于一个不存在的小细胞的科学/技术故事。",
    "https://news.ycombinator.com/item?id=48847946":
        "Too Many Books?：围绕书太多、阅读管理或藏书取舍的讨论。",
    "https://news.ycombinator.com/item?id=48847887":
        "The C6 Days：回顾工具、内存和 bug 的技术文章。",
    "https://news.ycombinator.com/item?id=48847832":
        "视频：作者让 Claude Fable 5 制作歌词视频，展示 AI 创作流程。",
    "https://news.ycombinator.com/item?id=48847888":
        "Big Burnham will be watching you：围绕监控、政治或公共空间治理的文章。",
    "https://news.ycombinator.com/item?id=48847891":
        "Ask HN：兴趣太多时如何取舍和管理注意力。",
    "https://news.ycombinator.com/item?id=48847834":
        "Show HN：把 Web 应用逆向成 agent 可调用工具的项目。",
    "https://news.ycombinator.com/item?id=48848046":
        "Browser-Memory：与浏览器端记忆/持久化上下文相关的项目或文章。",
    "https://news.ycombinator.com/item?id=48847899":
        "《The Lazarus Heist》音频：关于 Lazarus 黑客组织相关事件的调查故事。",
    "https://news.ycombinator.com/item?id=48848011":
        "数字欧元进入欧盟最终谈判阶段的报道。",
    "https://news.ycombinator.com/item?id=48847819":
        "纽约时报牵头团体要求法院在美国版权纠纷中制裁 OpenAI。",
    "https://news.ycombinator.com/item?id=48848041":
        "澳大利亚地方议会投票支持污染者付费的气候赔偿基金。",
    "https://news.ycombinator.com/item?id=48847930":
        "Show HN：基于 Claude Code 的 AI 求职申请框架。",
    "https://news.ycombinator.com/item?id=48848034":
        "报道英国民粹政治人物 Farage 的选举押注受挫。",
    "https://news.ycombinator.com/item?id=48848052":
        "Apache Kafka 性能相关的技术文章或基准讨论。",
    "https://news.ycombinator.com/item?id=48848075":
        "Show HN：Ring Holders Club，一个围绕戒指/收藏或会员身份的项目。",

    # 2026-07-06 HTML / GitHub Trending / YouTube AI / Hacker News Newest
    "https://www.anthropic.com/news/fable-safeguards-jailbreak-framework":
        "Anthropic 进一步说明 Claude Fable 5 的网络安全分类器会拦截哪些风险，并提出一版 AI jailbreak 严重性分级框架。",
    "https://www.anthropic.com/news/claude-science-ai-workbench":
        "Anthropic 推出 Claude Science：面向科学家的 AI 工作台，整合文献分析、Jupyter/R/集群等工具，生成可审计、可复现实验产物。",
    "https://transformer-circuits.pub/2026/june-update/index.html":
        "Transformer Circuits 6 月更新：Anthropic 可解释性团队分享 SAE 特征、归因图和安全行为分析等尚在发展中的研究想法。",
    "https://www.anthropic.com/news/claude-sonnet-5":
        "Anthropic 发布 Claude Sonnet 5：更强的 agentic Sonnet，接近 Opus 4.8 的编码、工具使用和知识工作能力，同时价格更低。",
    "https://www.anthropic.com/news/redeploying-fable-5":
        "Anthropic 宣布在出口限制解除后重新部署 Claude Fable 5，并恢复 Mythos 5 的部分访问，同时加入新的网络安全防护和 jailbreak 框架。",
    "https://github.com/alirezarezvani/claude-skills":
        "claude-skills：面向 Claude Code、Codex、Gemini CLI、Cursor 等编码 agent 的 337 个技能、插件、agent 与自定义命令合集。",
    "https://github.com/anthropics/claude-code":
        "Claude Code：Anthropic 的终端内 agentic coding 工具，可理解代码库、执行常规任务、解释复杂代码并处理 git 工作流。",
    "https://github.com/CoplayDev/unity-mcp":
        "unity-mcp：连接 AI 助手和 Unity Editor 的 MCP 桥，让 LLM 管理资源、控制场景、编辑脚本并自动化 Unity 任务。",
    "https://github.com/ogulcancelik/herdr":
        "herdr：运行在终端里的 agent multiplexer，用于统一调度和管理多个 AI agent。",
    "https://github.com/immich-app/immich":
        "Immich：高性能自托管照片和视频管理方案，面向个人云相册与媒体库。",
    "https://github.com/facebook/astryx":
        "astryx：Meta/Facebook 开源的可完全定制、面向 agent 工作流的设计系统。",
    "https://github.com/harvard-edge/cs249r_book":
        "cs249r_book：Harvard Edge 的《Machine Learning Systems》教材仓库，系统讲解机器学习系统工程。",
    "https://github.com/alibaba/page-agent":
        "page-agent：阿里开源的浏览器页面内 JavaScript GUI agent，可用自然语言控制网页界面。",
    "https://github.com/steipete/CodexBar":
        "CodexBar：无需登录即可在菜单栏查看 OpenAI Codex 和 Claude Code 使用统计的工具。",
    "https://github.com/OthmanAdi/planning-with-files":
        "planning-with-files：为 AI coding agent 提供基于文件的持久计划系统，支持长任务、上下文丢失恢复和多 agent 共享状态。",
    "https://github.com/hesreallyhim/awesome-claude-code":
        "awesome-claude-code：精选 Claude Code 资源合集，涵盖 skills、agents、状态栏、开发工具与插件。",
    "https://github.com/coreyhaines31/marketingskills":
        "marketingskills：面向 Claude Code 和 AI agent 的营销技能集合，覆盖 CRO、文案、SEO、分析与增长工程。",
    "https://github.com/Zackriya-Solutions/meetily":
        "Meetily：隐私优先的本地 AI 会议助手，基于 Rust、Parakeet/Whisper、说话人分离和 Ollama 总结，支持自托管。",
    "https://github.com/rommapp/romm":
        "RomM：美观强大的自托管 ROM 管理器和播放器，用于管理复古游戏库。",
    "https://github.com/gastownhall/gastown":
        "Gas Town：多 agent workspace 管理器，用于组织和协调多个 agent 的工作环境。",
    "https://github.com/openai/codex-plugin-cc":
        "codex-plugin-cc：让 Claude Code 调用 Codex 来审查代码或委派任务的 OpenAI 插件。",
    "https://github.com/JuliusBrussee/caveman":
        "caveman：Claude Code 技能，用极简语言压缩对话，声称可减少约 65% token 消耗。",
    "https://www.youtube.com/watch?v=iT_yv_nEdIo":
        "AI 周报：介绍把 ChatGPT 与 Claude 合并使用的免费 agent、中国开源 GLM、ZCode、NotebookLM Reels、Claude Science 和 Fable 5 回归等 18 项更新。",
    "https://www.youtube.com/watch?v=7HhlSu3pPvU":
        "深度测试 Gemini Omni Flash 的视频编辑能力：用真实素材做风格迁移、产品替换、材质转换、VFX 和角色/口型一致性控制。",
    "https://www.youtube.com/watch?v=iGBLb698WAE":
        "教程：用 ChatGPT 和 Higgsfield 从一个粗略想法出发，规划故事、生成一致角色与地点、做分镜并合成完整 AI 视频。",
    "https://www.youtube.com/watch?v=oOvXYlJdzT4":
        "评测 Easemate AI：用 GPT-IMG2 和 Seedance 2.0 生成世界杯主题图片、电影感足球视频和内容创作素材。",
    "https://www.youtube.com/watch?v=-z2QiGjtOzk":
        "视频汇总 Gemini 3.5 Pro 泄露信息：包括传闻基准、前端编码、SVG/Three.js 生成和 agentic 能力，声称 Google 将追赶 Fable 5 与 GPT-5.6。",
    "https://news.ycombinator.com/item?id=48799930":
        "GitHub Freno：一个协作式、高可用的节流服务，用于控制后端资源压力。",
    "https://news.ycombinator.com/item?id=48799981":
        "Lord of the Roths：一篇围绕 Roth 账户/税务或投资策略展开的文章，引发 HN 讨论。",
    "https://news.ycombinator.com/item?id=48800026":
        "Shrimple：一种更简单、更友好的 Markdown 变体或工具。",
    "https://news.ycombinator.com/item?id=48799929":
        "Castro Podcasts 团队复盘自己在客户支持上做错的事情。",
    "https://news.ycombinator.com/item?id=48799820":
        "Entropyseal：一个与熵、随机性或密封校验相关的技术项目/文章。",
    "https://news.ycombinator.com/item?id=48799719":
        "Show HN：每月 6 美元、不计 token、不限量的 LLM API 服务，引发可持续性讨论。",
    "https://news.ycombinator.com/item?id=48800053":
        "作者称 Android 地震预警在委内瑞拉救了自己一命，分享实际预警体验。",
    "https://news.ycombinator.com/item?id=48799654":
        "研究/文章讨论自我披露本身为何会让人产生内在奖励感。",
    "https://news.ycombinator.com/item?id=48799736":
        "文章讨论 AI 炒作的强劲叙事正遇到一个难以忽视的现实约束。",
    "https://news.ycombinator.com/item?id=48799615":
        "报道古代维苏威火山卷轴的新解读进展，揭示更多历史文本信息。",
    "https://news.ycombinator.com/item?id=48799614":
        "HN 讨论：GPT-5.6 Sol Ultra 可能会进入 Codex。",
    "https://news.ycombinator.com/item?id=48799853":
        "文章讨论如何设计可确定性重放的市场数据系统，便于调试和回测。",
    "https://news.ycombinator.com/item?id=48799841":
        "文章指出 AI 自动化成本可能高于被替代的人力成本，讨论企业 ROI 落差。",
    "https://news.ycombinator.com/item?id=48799582":
        "自推进链锯可降低工伤风险的技术/产品报道。",
    "https://news.ycombinator.com/item?id=48799979":
        "一组面向 2026 年 SaaS 创业和产品构建的规则建议。",
    "https://news.ycombinator.com/item?id=48799677":
        "报道儿童采用 AI 的速度约为成人 3 倍，并警示教育和安全准备不足。",
    "https://news.ycombinator.com/item?id=48799974":
        "文章讨论 AI 时代哪些人会更容易蓬勃发展，以及对应的能力结构。",
    "https://news.ycombinator.com/item?id=48799850":
        "Show HN：忠实复刻 MUMPS 76 的周年实现，回顾原始 NoSQL 数据库。",
    "https://news.ycombinator.com/item?id=48799966":
        "介绍 Bending Spoons：这家拥有 AOL 和 Vimeo 等资产、如今上市的低调公司。",
    "https://news.ycombinator.com/item?id=48799944":
        "文章解读 Postgres 19 的 Property Graph 功能及其图查询能力。",
    "https://news.ycombinator.com/item?id=48799732":
        "文章/讨论关注电磁场（EMF）对儿童的潜在影响。",
    "https://news.ycombinator.com/item?id=48799572":
        "科学报道：研究者可能找到阿尔茨海默病杀死脑细胞的机制线索。",
    "https://news.ycombinator.com/item?id=48800042":
        "视频/讨论：是否能运行《超级马里奥兄弟》中的每一行代码。",
    "https://news.ycombinator.com/item?id=48799583":
        "Kitirua Plains Lodge：肯尼亚一处脱离传统 Safari 建筑风格的酒店设计案例。",
    "https://news.ycombinator.com/item?id=48799978":
        "Show HN：Openleetcode 可在本地用开放测试运行 LeetCode 解法。",
    "https://news.ycombinator.com/item?id=48799781":
        "The Sneakerweb：一篇围绕球鞋文化/网络生态展开的文章或项目。",
    "https://news.ycombinator.com/item?id=48800002":
        "McKinsey 报告：分析投资为何发生在某些地区和行业，以及如何催化竞争力。",
    "https://news.ycombinator.com/item?id=48799624":
        "Lost and Found：一篇题为『失物招领』的文章/项目，引发 HN 讨论。",
    "https://news.ycombinator.com/item?id=48800043":
        "Pangram 2024 技术报告：介绍其 AI 生成文本分类器的方法与评估。",
    "https://news.ycombinator.com/item?id=48799667":
        "视频/文章讨论 Midjourney 从 AI 低质内容工具转向医学研究场景的可能性。",

    # 2026-06-28 GitHub Trending
    "https://github.com/altic-dev/FluidVoice":
        "FluidVoice：macOS 上的离线本地语音转文字应用，主打高速、隐私友好、无需云端。",
    "https://github.com/HKUDS/Vibe-Trading":
        "Vibe-Trading：面向个人交易者的 AI 交易 agent 项目，用自然语言与自动化流程辅助交易研究和执行。",
    "https://github.com/Robbyant/lingbot-map":
        "lingbot-map：一个前馈式 3D 基础模型，面向流式数据实时重建场景。",
    "https://github.com/ByteByteGoHq/system-design-101":
        "system-design-101：用图解和通俗文字讲复杂系统，帮助准备系统设计面试。",
    "https://github.com/usestrix/strix":
        "strix：开源 AI 黑客/安全 agent，用来发现并修复应用漏洞。",
    "https://github.com/cupy/cupy":
        "CuPy：在 GPU 上实现 NumPy/SciPy 风格数组计算的高性能 Python 库。",
    "https://github.com/browser-use/video-use":
        "video-use：让 coding agent 直接编辑视频的工具项目。",

    # 2026-06-28 YouTube AI
    "https://www.youtube.com/watch?v=65RvB3Xta0E":
        "AI 周报：围绕 GPT-5.6、Claude Fable 5 限制、Claude Tag、NVIDIA 药物发现 AI、开源模型等 18 项更新做概览。",
    "https://www.youtube.com/watch?v=Zzj0x1BuzgA":
        "实测让 Claude 从零搭建 GTA 5 RP 的 FiveM 框架，展示服务器搭建、调试与核心功能生成过程。",
    "https://www.youtube.com/watch?v=7c_ieWfAbrw":
        "AI 新闻汇总：覆盖 GPT-5.6、Seedance 2.5、实时头像、脑部超声、芯片与多项新模型/工具发布。",
    "https://www.youtube.com/watch?v=OEaM4GKM6mU":
        "阿语 AI 新闻：解读 GPT-5.6 Sol/Terra/Luna 系列、美国限制、Aizawa 进展、PixelRAG、Mistral OCR 等动态。",
    "https://www.youtube.com/watch?v=_AoyQcIoquA":
        "解读 GPT-5.6 Sol 的受限预览、美国政府压力、编码与网络安全能力，以及 OpenAI 与 Broadcom 的 Jalapeno 自研芯片。",

    # 2026-06-28 Hacker News Newest
    "https://news.ycombinator.com/item?id=48706481":
        "Show HN：忠实复刻 MUMPS 76 数据库实现，回顾这个早期 NoSQL 系统的历史。",
    "https://news.ycombinator.com/item?id=48706559":
        "面向普通读者解释 CORS 的文章，梳理浏览器跨域安全机制的基本概念。",
    "https://news.ycombinator.com/item?id=48706444":
        "Show HN：一个实验性的 Python 到 GCC/GAS 内联汇编桥接工具。",
    "https://news.ycombinator.com/item?id=48706539":
        "报道称 Claude Fable 5 可能在数日内重新开放，引发 HN 讨论。",
    "https://news.ycombinator.com/item?id=48706643":
        "介绍在设备端对语音录音进行降噪处理的技术方案。",
    "https://news.ycombinator.com/item?id=48706538":
        "论文/资料：介绍 Verse 编程语言及其超越传统函数式编程的设计思想。",
    "https://news.ycombinator.com/item?id=48706483":
        "Perceus：一种可复用、低垃圾产生的引用计数内存管理方法。",
    "https://news.ycombinator.com/item?id=48706560":
        "报道 Kids Act 可能要求用户通过年龄检查才能上网，引发隐私与监管争议。",
    "https://news.ycombinator.com/item?id=48706554":
        "火星生命证据讨论：新发现增加了线索，但仍未直接证明生命存在。",
    "https://news.ycombinator.com/item?id=48706571":
        "Tldr.fail：部分服务器实现有 bug，导致 TLS 中的后量子密钥交换兼容性破坏。",
    "https://news.ycombinator.com/item?id=48706627":
        "Cypherpunk Library：面向密码朋克思想与资料的在线文库。",
    "https://news.ycombinator.com/item?id=48706502":
        "Show HN：Warren 可在无容器、无 root 的情况下运行隔离的 CLI 工具实例。",
    "https://news.ycombinator.com/item?id=48706544":
        "文章讨论从单次提示词走向循环式 autonomous coding agents 的构建方式。",
    "https://news.ycombinator.com/item?id=48706430":
        "Yourbrowsercandoit：提供 64 个浏览器内文件工具，免上传、免注册、无追踪。",
    "https://news.ycombinator.com/item?id=48706616":
        "报道称荷兰对欧盟烟草规则的公众反馈中近四分之三由 AI 生成。",
    "https://news.ycombinator.com/item?id=48706537":
        "法国热浪导致约千人额外死亡的报道。",
    "https://news.ycombinator.com/item?id=48706490":
        "Show HN：Genius AI Detector，一个用于检测 AI 生成内容的工具。",
    "https://news.ycombinator.com/item?id=48706486":
        "GhostGrid：用 Ed25519 做漂移检测和边缘设备篡改证据的方案。",
    "https://news.ycombinator.com/item?id=48706506":
        "Policy Pulse 第 21 期：汇总 2026 年 6 月 27 日这一周的政策动态。",
    "https://news.ycombinator.com/item?id=48706578":
        "Ask HN：如果有人现在给你的创业公司投 10 万美元，你会如何使用？",
    "https://news.ycombinator.com/item?id=48706455":
        "Show HN：UnfoldCMS 是一次性付费、无订阅的自托管 Laravel CMS。",
    "https://news.ycombinator.com/item?id=48706657":
        "文章讨论用 quantum picturalism 超越传统符号代数的表达方式。",
    "https://news.ycombinator.com/item?id=48706419":
        "Ask HN：如何找到正确受众并验证产品市场匹配。",
    "https://news.ycombinator.com/item?id=48706448":
        "Flounder Mode：一篇围绕该模式/概念展开的分享，引发 HN 讨论。",
    "https://news.ycombinator.com/item?id=48706521":
        "Almavivo：一个把健康数据处理放在设备端完成的健康平台。",
    "https://news.ycombinator.com/item?id=48706485":
        "云播种专家称人工降雨并不能真正解决干旱问题。",
    "https://news.ycombinator.com/item?id=48706449":
        "特朗普威胁对征收数字税的欧洲国家加征 100% 关税。",
    "https://news.ycombinator.com/item?id=48706628":
        "Ask HN：原生 iOS/Swift 应用是否允许 OTA 热更新，社区讨论苹果规则边界。",
    "https://news.ycombinator.com/item?id=48706498":
        "介绍无需 React 也可使用的 shadcn/ui 组件方案。",
    "https://news.ycombinator.com/item?id=48706493":
        "《Imagine Telling Someone in 1999》：以 1999 年视角反观当代技术变化的随笔。",

    # 2026-06-27 GitHub Trending
    "https://github.com/NanmiCoder/MediaCrawler":
        "MediaCrawler：覆盖小红书、抖音、快手、B 站、微博、贴吧、知乎的多平台自媒体笔记/视频/评论爬虫合集。",
    "https://github.com/simplex-chat/simplex-chat":
        "SimpleX Chat：号称首个不依赖任何用户标识符的消息网络，设计上完全去身份化、保护隐私，提供 iOS/Android/桌面客户端。",
    "https://github.com/alchaincyf/zhangxuefeng-skill":
        "张雪峰.skill：把张雪峰的认知操作系统封装成 Claude skill，给高考志愿/考研/职业规划提供实战思维框架，由『女娲.skill』生成。",
    "https://github.com/IceWhaleTech/CasaOS":
        "CasaOS：简单易用、界面优雅的开源个人云系统，把家用设备整合成自托管 NAS/私有云。",
    "https://github.com/opendatalab/MinerU":
        "MinerU：把 PDF、Office 等复杂文档转成 LLM 友好的 Markdown/JSON，专为 agentic 工作流准备的解析工具。",
    "https://github.com/aws/agent-toolkit-for-aws":
        "AWS Agent Toolkit：AWS 官方支持的 MCP server、skill 与插件集合，帮助 AI agent 在 AWS 上构建应用。",
    "https://github.com/mauriceboe/TREK":
        "TREK：自托管的旅行/行程规划器，支持实时协作、交互地图、PWA、SSO、预算与打包清单等。",
    "https://github.com/xbtlin/ai-berkshire":
        "ai-berkshire（AI 时代的伯克希尔）：基于 Claude Code 的价值投资研究框架，集成巴菲特/芒格/段永平/李录四大师方法论与多 agent 并行对抗式分析。",
    "https://github.com/grafana/grafana":
        "Grafana：开放可组合的可观测性与数据可视化平台，统一展示 Prometheus、Loki、Elasticsearch、InfluxDB、Postgres 等多源的指标、日志与链路。",
    "https://github.com/commaai/openpilot":
        "openpilot：comma.ai 的开源机器人操作系统，目前为 300+ 款车型升级驾驶辅助系统。",
    "https://github.com/ripienaar/free-for-dev":
        "free-for-dev：面向开发者/运维的 SaaS、PaaS、IaaS 免费额度服务清单合集。",

    # 2026-06-27 YouTube AI
    "https://www.youtube.com/watch?v=Zim8hNQadqc":
        "西语博主横评 ChatGPT、Gemini、Claude 三家，讨论 2026 年自己会为哪一款付费订阅。",
    "https://www.youtube.com/watch?v=WKv7nMyxOUk":
        "意大利语教程：用 Claude Code 与 Codex 一分钟搭一个 agentic loop，把 90% 重复任务交给 AI 自动完成——作者称 agentic loop 将在 2027 年取代单次 prompt。",
    "https://www.youtube.com/watch?v=UyshVdGe4UY":
        "博主把日本 Sakana 新模型 Fugu 与被美国下架的 Claude Fable 5 做 5 轮对战，测试这款『没有政府能关停』的 AI 是否真的更强。",
    "https://www.youtube.com/watch?v=EfYqyj5ThBc":
        "AI 新闻汇总：种种迹象（Bedrock 上架、Claude Code 字符串改动、iOS 现身、预测市场升至 90%）暗示 Claude Fable 5 即将回归，同时 GPT-5.6、Gemini 3.5 Pro 延期、OpenAI 自研芯片、Qwen 等动态。",
    "https://www.youtube.com/watch?v=iTY8Q449YNQ":
        "博主让 Claude Code『尽可能帮自己赚钱』，实测 AI agent 自动化变现的可行性与流程。",

    # 2026-06-27 Hacker News Newest
    "https://news.ycombinator.com/item?id=48689452":
        "报道：短视频平台 Triller 拖欠并冷落员工，如今押注与 SpaceX 的合作谋求翻身。",
    "https://news.ycombinator.com/item?id=48689135":
        "Hallucinate.md：一个『告诉 AI 不要幻觉』的开放标准提案（项目本身带几分自嘲/调侃）。",
    "https://news.ycombinator.com/item?id=48689088":
        "讨论：OpenAI 将 GPT-5.6 先行开放给经美国政府审核的特定用户，引发对政府介入前沿模型发布的争论。",
    "https://news.ycombinator.com/item?id=48689052":
        "Taalas：把神经网络直接固化到芯片硬件、追求极致推理能效的初创公司。",
    "https://news.ycombinator.com/item?id=48689205":
        "一篇图形用户界面（GUI）发展史的回顾文章。",
    "https://news.ycombinator.com/item?id=48689156":
        "1973 年 Rosenhan 实验回顾：八名健康者假装单一幻听症状即被精神病院收治，质疑精神病诊断的可靠性。",
    "https://news.ycombinator.com/item?id=48689050":
        "报道：乌克兰将破坏北溪管道的行动伪装成拍摄『色情片』作为掩护。",
    "https://news.ycombinator.com/item?id=48689021":
        "技术文：主张任务队列直接用 Postgres 实现即可，无需引入专门的消息队列中间件。",
    "https://news.ycombinator.com/item?id=48689394":
        "一篇关于『为政府提供咨询建议』的随笔/经验文。",
    "https://news.ycombinator.com/item?id=48689004":
        "Show HN：为背诵学习内容做的闪卡 App，套用了交友软件式的滑动 UI。",
    "https://news.ycombinator.com/item?id=48689411":
        "评论文章：用棒球（数据/概率思维）来类比和启发对 AI 的理解。",
    "https://news.ycombinator.com/item?id=48689223":
        "技术文：用 Fenwick 树（树状数组）在模 2ⁿ 下计算前缀乘积。",
    "https://news.ycombinator.com/item?id=48689072":
        "DuckDB 的 SQLite 扩展，可在 DuckDB 中直接读写 SQLite 数据库。",
    "https://news.ycombinator.com/item?id=48689450":
        "OpenAI 发布 GPT-5.6 系统卡（System Card）PDF，披露模型能力与安全评估细节。",
    "https://news.ycombinator.com/item?id=48689233":
        "一个支持 ePub、PDF 等主流电子书格式的 MCP server，让 AI agent 读取电子书内容。",
    "https://news.ycombinator.com/item?id=48689182":
        "报道：被 DOGE 裁员的前 NOAA 员工自发重建了一个气候数据网站。",
    "https://news.ycombinator.com/item?id=48689407":
        "回顾字体设计师 Jim Parkinson 从贺卡到霓虹灯招牌的字体艺术生涯。",
    "https://news.ycombinator.com/item?id=48689037":
        "观点文：厌倦『算法推荐』？RSS 正是你一直在找的去算法化信息订阅工具。",
    "https://news.ycombinator.com/item?id=48689298":
        "科技报道：单原子相机有望窥视量子计算机内部状态。",
    "https://news.ycombinator.com/item?id=48689374":
        "观点文：吐槽当前 AI『skill』分发生态的混乱与不成熟。",
    "https://news.ycombinator.com/item?id=48689243":
        "Mercury Agent：一个 AI agent 产品/项目（HN 链接讨论）。",
    "https://news.ycombinator.com/item?id=48689091":
        "Anthropic 经济指数报告新一期『Cadences』，分析 AI 在经济活动中的使用节奏与模式。",
    "https://news.ycombinator.com/item?id=48689447":
        "Ask HN：大家如何判断自己的 AI agent 输出质量出现退化？社区征集监测方法。",
    "https://news.ycombinator.com/item?id=48689028":
        "HN 讨论 OpenAI 预览 GPT-5.6 Sol 下一代模型的帖子。",
    "https://news.ycombinator.com/item?id=48689315":
        "ab-av1：基于 VMAF 采样自动计算 CRF 的 AV1 视频编码工具。",
    "https://news.ycombinator.com/item?id=48689383":
        "Media over QUIC（MoQ）的 Update 00 进展更新，介绍这一基于 QUIC 的低延迟实时媒体传输协议。",
    "https://news.ycombinator.com/item?id=48689275":
        "报道：数据中心扩张引发选民反弹，一位候选人称这『让我输掉了选举』。",
    "https://news.ycombinator.com/item?id=48689058":
        "半导体报道：IBM、Intel、三星、台积电在未来晶体管堆叠路线上的技术分歧。",
    "https://news.ycombinator.com/item?id=48689277":
        "科普文：什么是诺模图（nomogram，列线图），为何它值得了解。",
    "https://news.ycombinator.com/item?id=48689398":
        "Show HN：用 PyWA 库封装 WhatsApp Business API 的 MCP server。",

    # 2026-06-25 公司动态（RSS 缺 description）
    "https://www.anthropic.com/news/introducing-claude-tag":
        "Anthropic 推出 Claude Tag：把 Claude 变成 Slack 里的多人协作队友，可被 @ 进对话直接干活，并有主动参与的 ambient（环境）模式。",
    "https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/":
        "Google DeepMind 在 Gemini 3.5 Flash 中引入 computer use 能力，让模型像人一样操作浏览器与图形界面（点击、输入、滚动）完成网页任务，主打低延迟、高性价比的 agent 自动化。",

    # 2026-06-25 GitHub Trending
    "https://github.com/Flowseal/zapret-discord-youtube":
        "zapret-discord-youtube：绕过 DPI 封锁、恢复对 Discord 与 YouTube 访问的 Windows 脚本工具集。",
    "https://github.com/google-labs-code/design.md":
        "design.md：Google Labs 推出的视觉识别描述格式规范，用 DESIGN.md 给编码 agent 提供持久、结构化的设计系统理解。",
    "https://github.com/interviewstreet/hiring-agent":
        "hiring-agent：用于自动评估并打分简历的 AI 招聘 agent。",
    "https://github.com/flutter/flutter":
        "Flutter：Google 的跨平台 UI 工具包，可快速构建移动端及多端的精美原生应用。",
    "https://github.com/apple/container":
        "apple/container：用 Swift 编写、面向 Apple 芯片优化的工具，在 Mac 上用轻量虚拟机创建并运行 Linux 容器。",
    "https://github.com/andreknieriem/headunit-revived":
        "headunit-revived：复活的车机 Headunit 应用，用于在车载屏上显示 Android Auto。",
    "https://github.com/kunchenguid/no-mistakes":
        "no-mistakes：一个 git 推送闸门工具——拦截 push 后在隔离环境运行 AI 驱动的校验流水线，全部通过才自动开一个干净的 PR。",
    "https://github.com/stablyai/orca":
        "Orca：Stably AI 出品的并行 agent 集群 ADE（agent 开发环境），可用自己的订阅运行任意编码 agent，支持桌面与移动端。",

    # 2026-06-25 Hacker News Newest
    "https://news.ycombinator.com/item?id=48662916":
        "一个用 Streamlit 做的探索性原型，通过降雨异常、土壤湿度、气温、ENSO、化肥与食品价格等指标，监测并计算印度粮食供应的综合压力指数。",
    "https://news.ycombinator.com/item?id=48662886":
        "Rust Commercial Network 启动，旨在把商业 Rust 用户聚到一起、推动商业落地。",
    "https://news.ycombinator.com/item?id=48663047":
        "伪装成正规应用的俄罗斯银行 App 再度登顶美国 App Store 榜单。",
    "https://news.ycombinator.com/item?id=48662812":
        "监控厂商 Flock CEO 称：无论 Flock 怎么做，移民执法都会照样推进。",
    "https://news.ycombinator.com/item?id=48662920":
        "Show HN：Follow the Thread——一种更平静、注重排版的 Wikipedia 阅读方式。",
    "https://news.ycombinator.com/item?id=48662863":
        "观点文：安全本质上是政治性的。",
    "https://news.ycombinator.com/item?id=48662999":
        "HN 讨论：Gemini 3.5 Flash 中的 computer use 能力。",
    "https://news.ycombinator.com/item?id=48663055":
        "FEE 评论文：G7 用政府主导的价格下限与进口配额来保障关键矿产供应，违背其自身的市场原则，最终反而利好中国、损害西方生产者与消费者。",
    "https://news.ycombinator.com/item?id=48662898":
        "Fwupd 2.0.21 发布，修复 250 多个潜在安全问题。",
    "https://news.ycombinator.com/item?id=48662936":
        "犹他州最大的太阳能+储能项目正式并网上线。",
    "https://news.ycombinator.com/item?id=48663112":
        "供应链安全：Codfish/semantic-release-action 这个 GitHub Action 已被攻陷投毒。",
    "https://news.ycombinator.com/item?id=48663018":
        "文章：远程办公如何帮助了这一代有孩子的在职父母。",
    "https://news.ycombinator.com/item?id=48663022":
        "Show HN：ccMarvin——只用邮件来与 AI 交互的工具。",
    "https://news.ycombinator.com/item?id=48662885":
        "法国确诊首例埃博拉病例，官方报告这种『眼出血』疾病。",
    "https://news.ycombinator.com/item?id=48663067":
        "五年前的英伟达 A100 服务器在中国二手市场卖到高达 8.2 万美元。",
    "https://news.ycombinator.com/item?id=48663001":
        "巴西一法官以在家自学（homeschooling）为由判处一对父母入狱。",
    "https://news.ycombinator.com/item?id=48663000":
        "文章：面向 AI 的『网络数据基础设施层』正在兴起。",
    "https://news.ycombinator.com/item?id=48662988":
        "Show HN：DBOSify——基于 Postgres 构建、可直接替换 Temporal 的工作流引擎。",
    "https://news.ycombinator.com/item?id=48663113":
        "文章『All roads led to Markdown』：各种格式/工具最终都汇流到 Markdown。",
    "https://news.ycombinator.com/item?id=48663138":
        "观点：模糊化的(Fuzzy) API 正在重塑 Web。",
    "https://news.ycombinator.com/item?id=48662805":
        "育碧联合创始人 Claude Guillemot 因飞机失事去世。",
    "https://news.ycombinator.com/item?id=48663127":
        "文章：把中国分析为一个具备『绝对优势』的经济体。",
    "https://news.ycombinator.com/item?id=48663161":
        "一辆翻覆卡车释放 2400 万只蜜蜂，迫使德州小镇封锁。",
    "https://news.ycombinator.com/item?id=48662923":
        "Ask HN：你最希望 Claude Code 的界面改进哪些地方？",
    "https://news.ycombinator.com/item?id=48662882":
        "争议观点文：『LLM 研究是假的』，质疑当下 LLM 研究的成色。",
    "https://news.ycombinator.com/item?id=48663006":
        "教程：Makefile 入门，介绍如何编写 Makefile。",
    "https://news.ycombinator.com/item?id=48662986":
        "2026 EuroLLVM 开发者大会的演讲列表。",
    "https://news.ycombinator.com/item?id=48662924":
        "一台中国超算在全球排名中超越美国机型，登顶榜单。",
    "https://news.ycombinator.com/item?id=48662975":
        "分享一种检测 AWS/Terraform 配置漂移(drift)的方法。",
    "https://news.ycombinator.com/item?id=48662903":
        "Windage：免费的浏览器版《Scorched Earth》（炮战游戏）复刻。",

    # 2026-06-25 YouTube AI
    "https://www.youtube.com/watch?v=iyQtki8Fxyc":
        "罗马尼亚恶搞视频：Zlăvog 调查歌手 Mihai Trăistariu 与 ChatGPT 的『新恋情』，从禁忌之恋一路演到怀孕、组建幸福家庭。",
    "https://www.youtube.com/watch?v=WsD4NkD_swE":
        "UP 主拆解 Anthropic 新发布的 Claude Tag——把 Claude 变成 Slack 里的多人协作队友，含让其主动参与的 ambient 模式，解读发布要点。",
    "https://www.youtube.com/watch?v=YRXJnKP6Tu0":
        "法律频道 Lawful Masses：解读 BAM 诉讼中两方申请介入案件——一方请了律师，另一方用 AI(LLM) 提交，上演『律师 vs LLM』。",
    "https://www.youtube.com/watch?v=RNCaZhLlspk":
        "解读 OpenAI 新 GPT Cyber 在基准上击败 Mythos 5，配合 Daybreak、Codex Security、Patch the Planet，试图把 AI 从找漏洞工具变成修复互联网的系统。",
    "https://www.youtube.com/watch?v=UUAajF3eMIk":
        "对比测评 ChatGPT、Gemini、Claude 三家从零制作 FC 26（足球游戏）克隆，看谁做得最好。",

    # 2026-06-23 GitHub Trending
    "https://github.com/Stirling-Tools/Stirling-PDF":
        "Stirling-PDF：GitHub 上排名第一的 PDF 应用，可在任意设备本地完成 PDF 编辑、合并、转换、拆分、加密等操作。",
    "https://github.com/heygen-com/hyperframes":
        "hyperframes：HeyGen 出品，写 HTML 即可渲染视频，专为 AI agent 设计的视频生成框架。",
    "https://github.com/JCodesMore/ai-website-cloner-template":
        "ai-website-cloner-template：借助 AI 编码 agent，用一条命令克隆任意网站的模板项目。",
    "https://github.com/jamiepine/voicebox":
        "voicebox：开源 AI 语音工作室，支持声音克隆、语音口述与音频创作。",
    "https://github.com/firecrawl/firecrawl":
        "Firecrawl：大规模搜索、抓取并与网页交互的 API，可把网站转成适合 LLM 的结构化数据。",
    "https://github.com/lyogavin/airllm":
        "AirLLM：通过分层加载推理，仅用单张 4GB GPU 即可运行 70B 大模型推理的优化库。",

    # 2026-06-23 Hacker News Newest
    "https://news.ycombinator.com/item?id=48641676":
        "Causal Summit：聚焦因果推断与因果 AI 的行业峰会官网。",
    "https://news.ycombinator.com/item?id=48641632":
        "Show HN：把 PowerPoint 演示文稿当作代码来管理（版本化、可编程生成）的工具。",
    "https://news.ycombinator.com/item?id=48641497":
        "用单一 API 统一管理 Apple、Google 与 Stripe 三家平台的订阅与计费。",
    "https://news.ycombinator.com/item?id=48641477":
        "关于资优儿童（gifted）教育的经验与建议讨论。",
    "https://news.ycombinator.com/item?id=48641537":
        "React Parallax：实现视差滚动效果的 React 组件/示例。",
    "https://news.ycombinator.com/item?id=48641763":
        "Show HN：与一位前 Citadel 交易员（AI 化身）协作构思交易策略的工具。",
    "https://news.ycombinator.com/item?id=48641786":
        "报道：一家基于 AI 的律所在法庭诉讼中胜诉。",
    "https://news.ycombinator.com/item?id=48641490":
        "CoreGLP Denmark：丹麦一家 GLP-1 减重/健康相关产品的页面。",
    "https://news.ycombinator.com/item?id=48641777":
        "Zero Weights Language Model（MSE-GLM）：一种声称「零权重」的语言模型博客介绍。",
    "https://news.ycombinator.com/item?id=48641583":
        "Claude API 文档中关于 System Prompts（系统提示词）的章节被分享讨论。",
    "https://news.ycombinator.com/item?id=48641809":
        "英国推出 11 亿英镑新计划，扶持芯片企业、提升算力与 AI 相关技能。",
    "https://news.ycombinator.com/item?id=48641489":
        "可视化：如果天上有 100 万颗星链（Starlink）卫星会是什么样子。",
    "https://news.ycombinator.com/item?id=48641725":
        "《经济学人》文章：如何把算力（compute）变成一种可交易的金融资产。",
    "https://news.ycombinator.com/item?id=48641774":
        "作者用 10 天造了一个 AI 记忆引擎，随后需要一个项目来证明它确实有效。",
    "https://news.ycombinator.com/item?id=48641500":
        "状态通报：Claude Opus 4.8 出现错误率升高（elevated errors）。",
    "https://news.ycombinator.com/item?id=48641741":
        "用 Clickcast.tech 工具在 12 分钟内生成一段营销视频（带推广性质）。",
    "https://news.ycombinator.com/item?id=48641509":
        "Show HN：开源基准上，仅用约 1% 的 token 就匹配了全上下文召回的效果。",
    "https://news.ycombinator.com/item?id=48641815":
        "《36 Hours with Fable》：作者对新模型 Fable 的 36 小时实测体验。",
    "https://news.ycombinator.com/item?id=48641682":
        "Ask HN：在 agentic 编码时代，为何很少有人讨论编排（orchestration）工具。",
    "https://news.ycombinator.com/item?id=48641505":
        "《The AI Poet》：一篇关于 AI 写诗的随笔/博客。",
    "https://news.ycombinator.com/item?id=48641615":
        "盘点每个工程团队都该了解的 AI 编码陷阱（AI Coding Traps）。",
    "https://news.ycombinator.com/item?id=48641604":
        "Show HN：Multiserial，一款界面现代、不显陈旧的 macOS 串口终端。",
    "https://news.ycombinator.com/item?id=48641553":
        "Show HN：一个用 Seedance 模型生成视频的简易网页工作室。",
    "https://news.ycombinator.com/item?id=48641634":
        "观点：别浪费 Claude 用量去「看护」AI 实验（应让其自动跑）。",
    "https://news.ycombinator.com/item?id=48641716":
        "《How sad should I be about ChatGPT?》（2022）：对 ChatGPT 的早期反思随笔。",
    "https://news.ycombinator.com/item?id=48641473":
        "Meta 向 CRED 投资 9 亿美元，并任命其创始人主管 WhatsApp。",
    "https://news.ycombinator.com/item?id=48641589":
        "《Chattiness》：LRB 博客探讨 AI 聊天/絮叨（chattiness）现象。",
    "https://news.ycombinator.com/item?id=48641596":
        "《Chesterton's Middle Finger》：对「切斯特顿栅栏」原则的反思与调侃。",
    "https://news.ycombinator.com/item?id=48641818":
        "Ionos 警告其德国法兰克福区域出现严重的容量短缺。",
    "https://news.ycombinator.com/item?id=48641595":
        "Ask HN：截至 2026 年 6 月，最好的编码 harness（编码代理框架）是哪个。",

    # 2026-06-23 YouTube AI
    "https://www.youtube.com/watch?v=IXES6bn2yR0":
        "俄语娱乐/恶搞视频，讲述「他们用 ChatGPT 把我查了出来」的整蛊故事。",
    "https://www.youtube.com/watch?v=E17Lb3osqrw":
        "WorldofAI 一周 AI 新闻汇总：Claude Sonnet 5、Mythos 6、本周四 GPT-5.6、Sakana Fugu 超越 Mythos 等。",
    "https://www.youtube.com/watch?v=bC9BaY18b0o":
        "조코딩 JoCoding AI 新闻：GLM-5.2 热潮、Google 的严峻危机、GPT-5.6 更新、Codex 录制回放等。",
    "https://www.youtube.com/watch?v=zCeQNPp3skY":
        "TBS×Bloomberg 节目：Gemini 的「万能机器人」无需逐项教学即可工作，靠世界模型实现快速进化（系鞋带、灌篮）。",
    "https://www.youtube.com/watch?v=7OmzmRlJdv8":
        "零度解说：微软 Copilot 被「破解」，号称无需 API Key 即可白嫖 GPT-5 对接本地 AI Agent。",

    # 2026-06-22 GitHub Trending
    "https://github.com/tursodatabase/turso":
        "Turso：用 Rust 重写的进程内 SQL 数据库，与 SQLite 兼容，目标做 SQLite 的现代替代。",
    "https://github.com/asgeirtj/system_prompts_leaks":
        "system_prompts_leaks：汇集从各大厂商提取的系统提示词（Anthropic Claude、OpenAI、Google Gemini、xAI Grok 等），持续更新。",
    "https://github.com/smicallef/spiderfoot":
        "SpiderFoot：自动化 OSINT 工具，用于威胁情报收集和攻击面测绘。",
    "https://github.com/mikumifa/biliTickerBuy":
        "biliTickerBuy：B 站会员购抢票辅助工具。",
    "https://github.com/ZhuLinsen/daily_stock_analysis":
        "daily_stock_analysis：LLM 驱动的多市场股票智能分析系统，集成多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。",
    "https://github.com/topoteretes/cognee":
        "Cognee：面向 agent 的开源 AI 记忆平台，用自托管知识图谱引擎为 AI agent 提供跨会话的持久长期记忆。",

    # 2026-06-22 Hacker News Newest
    "https://news.ycombinator.com/item?id=48627476":
        "Yann LeCun 演讲视频《World Models: Enabling the Next AI Revolution》，阐述世界模型如何推动下一轮 AI 革命。",
    "https://news.ycombinator.com/item?id=48627459":
        "Show HN：Cyclearchive.com，一个可搜索的历史自行车文献档案库。",
    "https://news.ycombinator.com/item?id=48627497":
        "一篇论述自然选择最大化 Fisher 信息量的理论文章，将进化与信息论联系起来。",
    "https://news.ycombinator.com/item?id=48627283":
        "Show HN：图形化 SQL 构建器与调试器，可视化拼装和排查 SQL 查询。",
    "https://news.ycombinator.com/item?id=48627512":
        "Commodore 推出 Callback 8020 翻盖手机，定位在功能机与智能机之间。",
    "https://news.ycombinator.com/item?id=48627538":
        "作者分享将某券商的虚拟化平台从 Hyper-V 零停机迁移到 Proxmox 的经验。",
    "https://news.ycombinator.com/item?id=48627492":
        "Safebucket：开源文件分享平台，后端基础设施可插拔。",
    "https://news.ycombinator.com/item?id=48627453":
        "技术文章：如何在 Z80 上高效使用索引寄存器（IX/IY）。",
    "https://news.ycombinator.com/item?id=48627396":
        "观点文章《Disposable software》：软件正变得像纸盘子一样一次性即弃。",
    "https://news.ycombinator.com/item?id=48627466":
        "一款网络工具，可仅用出站连接托管 WireGuard 服务器，绕过入站端口限制。",
    "https://news.ycombinator.com/item?id=48627586":
        "旧文（2020）：印度米佐拉姆邦的商店没有店主，顾客自助付款，靠诚信运转。",
    "https://news.ycombinator.com/item?id=48627509":
        "Minia2a：一个让 AI agent 赚钱的市场平台。",
    "https://news.ycombinator.com/item?id=48627563":
        "文章总结为金融 AI agent 构建评测（evals）的经验教训。",
    "https://news.ycombinator.com/item?id=48627350":
        "技术文章：用 C++ 实现 AirPlay 2 发送端，详解加密的 RAOP/RTSP 协议配方。",
    "https://news.ycombinator.com/item?id=48627570":
        "在 iPhone 上把语音指令转换成 JSON 工具调用的实践分享。",
    "https://news.ycombinator.com/item?id=48627462":
        "文章探讨同时对 agent 和人类友好的敏捷开发与代码架构。",
    "https://news.ycombinator.com/item?id=48627431":
        "太阳望远镜中的超表面（metasurface）成功捕获偏振光，提升观测能力。",
    "https://news.ycombinator.com/item?id=48627197":
        "论文/讨论：多轮反思式掩码（Multi-Turn Reflective Masking）激发掩码扩散模型的推理能力。",
    "https://news.ycombinator.com/item?id=48627461":
        "技术文章：PivCo-Huffman 的「合并」（Merge）操作。",
    "https://news.ycombinator.com/item?id=48627633":
        "Show HN：Prismag，在终端和任意 IDE 中实现按代码块（per-block）路由不同模型。",
    "https://news.ycombinator.com/item?id=48627226":
        "观点文章：最有效的屏幕使用时间密码是一个你自己也记不住的密码。",
    "https://news.ycombinator.com/item?id=48627436":
        "新闻：英国首相 Keir Starmer 宣布辞职。",
    "https://news.ycombinator.com/item?id=48627313":
        "Show HN：Gingerpaw，一款语音听写与 agent 工作空间应用。",
    "https://news.ycombinator.com/item?id=48627617":
        "技术文章：QUIC 不只是 TCP 的替代品，还带来更多新能力。",
    "https://news.ycombinator.com/item?id=48627499":
        "对比文章：Databricks 与 AWS 托管服务该如何按需求选型。",
    "https://news.ycombinator.com/item?id=48627330":
        "观点：用 AI 审查代码，尤其是面对超大 diff 时更有价值。",
    "https://news.ycombinator.com/item?id=48627471":
        "技术文章：优化 sqlx test 的重新编译时间。",
    "https://news.ycombinator.com/item?id=48627206":
        "观点文章：工程交付变快后，真正的难题变成了决定该构建什么。",
    "https://news.ycombinator.com/item?id=48627464":
        "报道：Anthropic 的 Mythos 风波持续发酵、愈发复杂。",
    "https://news.ycombinator.com/item?id=48627625":
        "Go bug：在浏览器（GOOS=js）环境下 UUID 的 NewV7() 总是生成时间戳为 7000 的 UUID。",

    # 2026-06-22 YouTube AI
    "https://www.youtube.com/watch?v=tnIFBDyOlGE":
        "조코딩 IT 新闻汇总：GLM-5.2 热潮、谷歌的危机、GPT-5.6 消息、Codex Record & Replay、Mythos 争议、Midjourney 近况等。",
    "https://www.youtube.com/watch?v=Nbynj-mKcNI":
        "盘点本周 AI agent 重大更新：SpaceX 收购 Cursor、Z.AI 开源的 GLM 5.2（性能逼近 Opus 4.8/GPT 5.5 但成本极低）、Codex 新增录屏教学的 Record & Replay 功能。",
    "https://www.youtube.com/watch?v=Ybrl4FYM57c":
        "Lenny 播客访谈 Anthropic 的 Fiona Fung（负责 Claude Code 和 Cowork 团队），聊最 AI 化的产品团队如何打造产品。",
    "https://www.youtube.com/watch?v=9vsg5kSYeEg":
        "Claude AI 完整教程：从入门到进阶，覆盖模型选择、大文件分析、Projects 组织工作、应用搭建等 2026 年实用工作流。",
    "https://www.youtube.com/watch?v=2-8cXaRHlqI":
        "日语教程：如何把 Claude 与 NotebookLM、Obsidian 联动，发挥 Claude 的最大能力提升工作效率。",

    # 2026-06-20 Anthropic
    "https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem":
        "Anthropic 在首尔设立办公室，并与韩国企业、初创公司和研究机构建立新合作，扩展当地 Claude 生态。",

    # 2026-06-20 GitHub Trending
    "https://github.com/DeusData/codebase-memory-mcp":
        "codebase-memory-mcp：高性能代码智能 MCP 服务器，把代码库索引为持久知识图谱，支持 158 种语言和低 token 查询。",
    "https://github.com/koala73/worldmonitor":
        "worldmonitor：实时全球情报仪表盘，统一聚合 AI 新闻、地缘政治监测和基础设施追踪。",
    "https://github.com/Kong/insomnia":
        "Insomnia：开源跨平台 API 客户端，支持 GraphQL、REST、WebSockets、SSE 和 gRPC，并提供云端、本地和 Git 存储。",
    "https://github.com/calesthio/OpenMontage":
        "OpenMontage：开源 agentic 视频制作系统，提供 12 条管线、52 个工具和 500 多项 agent skills。",
    "https://github.com/BuilderIO/agent-native":
        "agent-native：Builder.io 用于构建 agent-native 应用的框架。",
    "https://github.com/google-research/timesfm":
        "TimesFM：Google Research 开发的预训练时间序列基础模型，用于时间序列预测。",
    "https://github.com/palmier-io/palmier-pro":
        "Palmier Pro：为 AI 工作流打造的 macOS 视频编辑器。",
    "https://github.com/withastro/flue":
        "flue：用于构建和运行沙箱 agent 的框架。",
    "https://github.com/penpot/penpot":
        "Penpot：面向设计与代码协作的开源设计工具。",
    "https://github.com/aishwaryanr/awesome-generative-ai-guide":
        "awesome-generative-ai-guide：汇总生成式 AI 研究动态、面试资料、notebook 和学习资源。",
    "https://github.com/zai-org/GLM-5":
        "GLM-5：智谱开源模型项目，定位从 vibe coding 走向 agentic engineering。",
    "https://github.com/Lightricks/LTX-2":
        "LTX-2：Lightricks 音视频生成模型的官方 Python 推理与 LoRA 训练包。",

    # 2026-06-20 Hacker News Newest
    "https://news.ycombinator.com/item?id=48606639":
        "报道 SpaceX IPO 前，中国投资者如何取得相关股份。",
    "https://news.ycombinator.com/item?id=48606619":
        "作者把一个完整网站存进 favicon，展示极端体积压缩与浏览器技巧。",
    "https://news.ycombinator.com/item?id=48606397":
        "旧金山乘客讲述 Waymo 车辆在施工区受困时的惊险经历。",
    "https://news.ycombinator.com/item?id=48606315":
        "随笔讨论人们不断记录，是否恰恰因为已经忘记如何依靠自身记忆。",
    "https://news.ycombinator.com/item?id=48606282":
        "法院允许一宗针对 Amazon 的诉讼进入审判，案件涉及与某种化学品相关的自杀事件。",
    "https://news.ycombinator.com/item?id=48606300":
        "文章讨论 AI 如何拆分传统 CMS 的内容生产、管理、分发和界面层。",
    "https://news.ycombinator.com/item?id=48606554":
        "Bun 宣布 1.4 版本将于 7 月 7 日发布。",
    "https://news.ycombinator.com/item?id=48606287":
        "视频讨论一种监控杆装置，认为其隐私影响甚至比 Flock 摄像头更严重。",
    "https://news.ycombinator.com/item?id=48606654":
        "在 Rust 类型系统中实现 Lisp，探索类型级计算能力。",
    "https://news.ycombinator.com/item?id=48606222":
        "SSH 隧道实用指南，讲解本地端口转发与远程端口转发。",
    "https://news.ycombinator.com/item?id=48606392":
        "Bureaulogy：研究官僚体系如何形成、演化并持续存在。",
    "https://news.ycombinator.com/item?id=48606545":
        "Show HN：一本 Rust 教程书，最终项目是从零实现 Redis clone。",
    "https://news.ycombinator.com/item?id=48606451":
        "研究称美国保守派人群的死亡率高于自由派，并讨论可能的社会与健康因素。",
    "https://news.ycombinator.com/item?id=48606326":
        "一个专门播放火箭发射直播的电视播放器。",
    "https://news.ycombinator.com/item?id=48606413":
        "作者记录为自家后院设计露台的过程和工程取舍。",
    "https://news.ycombinator.com/item?id=48606533":
        "Ask HN：如果只有一个周末，你会开发什么简单应用？",
    "https://news.ycombinator.com/item?id=48606238":
        "文章讨论游戏 Spirit Crossing 面临的 AI 内容或开发问题。",
    "https://news.ycombinator.com/item?id=48606387":
        "Chromium Embedded Framework：用于在原生应用中嵌入 Chromium 浏览器能力的框架。",
    "https://news.ycombinator.com/item?id=48606475":
        "GenAIDojo：面向生成式 AI 学习、练习或实验的项目。",
    "https://news.ycombinator.com/item?id=48606411":
        "工具在送入 LLM 前压缩工具输出、日志、文件和 RAG chunks，目标是减少 60% 至 95% token。",
    "https://news.ycombinator.com/item?id=48606466":
        "报道巴西黑客导致午夜触发 EAS 紧急警报的事件。",
    "https://news.ycombinator.com/item?id=48606585":
        "Gizmodo 遭入侵并托管恶意软件，数小时内未及时处置。",
    "https://news.ycombinator.com/item?id=48606434":
        "文章重新计算 AI 编码的成本收益，讨论代码生成变便宜后工程约束如何变化。",
    "https://news.ycombinator.com/item?id=48606640":
        "Bevy 0.19 发布，更新这款 Rust 游戏引擎的功能和开发体验。",
    "https://news.ycombinator.com/item?id=48606377":
        "文章从 punctum 与 blind field 概念讨论摄影观看、细节和画面之外的想象。",
    "https://news.ycombinator.com/item?id=48606364":
        "预测中国将在明年前推出达到 Fable 5 级别的 AI 模型。",
    "https://news.ycombinator.com/item?id=48606396":
        "Show HN：把股票投资组合编码进 URL 和 favicon，便于分享和快速查看。",
    "https://news.ycombinator.com/item?id=48606271":
        "卫星观测揭示 GPS 信号干扰和欺骗活动的巨大规模。",
    "https://news.ycombinator.com/item?id=48606243":
        "Moebius：仅 0.2B 参数的轻量图像修复框架，宣称达到 10B 级模型效果。",
    "https://news.ycombinator.com/item?id=48606560":
        "一个用于绘制手绘风格图表的虚拟白板工具。",

    # 2026-06-20 YouTube AI
    "https://www.youtube.com/watch?v=gwv99NgRpbs":
        "Lucas Montano 以葡语讨论里约热内卢的本地或城市级 LLM 话题。",
    "https://www.youtube.com/watch?v=D6Cfjy83MQA":
        "Duncan Rogoff 演示 Anthropic 开源的 launch-your-agent skill，如何从需求访谈到上线定时云端 agent。",
    "https://www.youtube.com/watch?v=XzEgfmesG8c":
        "Higgsfield AI 演示 Claude 与 Higgsfield MCP 组合，无代码生成、发布并托管多人 3D 游戏。",
    "https://www.youtube.com/watch?v=HyDEzJztjpk":
        "The Morpheus Tutorials 实测 GLM-5.2 等开源模型能否在部分任务上与 Claude Fable 竞争。",
    "https://www.youtube.com/watch?v=8G4sBIVA5D0":
        "WorldofAI 全面测试 GLM-5.2，并比较它与 GPT-5.5、Opus 4.8 等模型的表现。",

    # 2026-06-17 GitHub Trending
    "https://github.com/swc-project/swc":
        "swc：基于 Rust 的 Web 编译与工具平台，面向 JavaScript/TypeScript 转译、打包和开发工具链。",
    "https://github.com/cypress-io/cypress":
        "Cypress：面向浏览器应用的快速、可靠端到端测试框架。",
    "https://github.com/alibaba/zvec":
        "zvec：阿里开源的轻量级进程内向量数据库，主打低延迟和快速本地检索。",
    "https://github.com/n0-computer/iroh":
        "iroh：Rust 模块化网络栈，用稳定的 dial key 取代脆弱 IP 地址连接。",
    "https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation":
        "Universal Android Debloater Next Generation：跨平台 Rust GUI，通过 ADB 精简免 root 安卓设备以改善隐私、安全和续航。",
    "https://github.com/puppeteer/puppeteer":
        "Puppeteer：用于自动化 Chrome 和 Firefox 的 JavaScript API，常用于测试、抓取和浏览器自动化。",

    # 2026-06-17 Hacker News Newest
    "https://news.ycombinator.com/item?id=48566860":
        "作者反思一次 bug 排查：真正的问题不是发现的 bug，而是自己预设的规则限制了判断。",
    "https://news.ycombinator.com/item?id=48566728":
        "Get Detach：HN 讨论一个名为 Detach 的工具/产品及其使用场景。",
    "https://news.ycombinator.com/item?id=48566623":
        "实测 M3 Mac 上同时打开 50 个 GitHub issue 对电池续航和资源占用的影响。",
    "https://news.ycombinator.com/item?id=48566559":
        "报道 Meta CTO Andrew Bosworth 承认公司 AI 重组过程非常糟糕。",
    "https://news.ycombinator.com/item?id=48566809":
        "电子书讨论 AI 如何逐步成为军事决策和作战规划中的新型顾问。",
    "https://news.ycombinator.com/item?id=48566605":
        "介绍 ClickHouse 的自定义 memcpy 实现，关注高性能数据库底层内存拷贝优化。",
    "https://news.ycombinator.com/item?id=48566688":
        "Origin：被称为 Cursor 的 GitHub 竞争产品，围绕代码托管与 AI 开发工作流展开。",
    "https://news.ycombinator.com/item?id=48566541":
        "HN 用户对不同 AI 编码 agent 的能力、稳定性和实际开发体验进行评分和讨论。",
    "https://news.ycombinator.com/item?id=48566824":
        "系列文章讲解如何在 Linux/x86-64 上用 memory-indirect calls 做系统调用插桩。",
    "https://news.ycombinator.com/item?id=48566727":
        "从 Chesterton's fence 延伸到 Chesterton's gap，讨论规则、缺口和改动前理解背景的重要性。",
    "https://news.ycombinator.com/item?id=48566792":
        "Show HN：Registry for Ant and Everyone Else，一个面向 Ant 及更多用户的注册表项目。",
    "https://news.ycombinator.com/item?id=48566534":
        "Loop Engineering：讨论以反馈循环、迭代和系统闭环为中心的工程实践。",
    "https://news.ycombinator.com/item?id=48566772":
        "Native Inference Engine：面向 macOS 14 及更新系统的本地推理引擎。",
    "https://news.ycombinator.com/item?id=48566549":
        "Dream Appearance Notification：围绕梦境出现提醒或梦境记录通知的实验性项目/想法。",
    "https://news.ycombinator.com/item?id=48566882":
        "Maven Central 开始正式施加发布限制，以控制包发布规模和生态资源压力。",
    "https://news.ycombinator.com/item?id=48566581":
        "R 语言获得统计领域奖项，体现其在统计计算和数据分析生态中的持续影响力。",
    "https://news.ycombinator.com/item?id=48566585":
        "作者记录自己的博客登上 Hacker News 首页后的流量、评论和心理体验。",
    "https://news.ycombinator.com/item?id=48566897":
        "一个节拍同步的 instanced-mesh 音乐可视化器，用 FFT 驱动实时视觉效果。",
    "https://news.ycombinator.com/item?id=48566678":
        "Ask HN：开发者讨论近年来移动开发在工具链、平台政策和用户期望上的变化。",
    "https://news.ycombinator.com/item?id=48566891":
        "面向医生解释患者为何使用 ChatGPT：可访问性、解释需求和医疗沟通缺口共同推动使用。",
    "https://news.ycombinator.com/item?id=48566837":
        "MediaUse Site Skills：围绕网站技能、媒体使用和用户能力表达的项目或文章。",
    "https://news.ycombinator.com/item?id=48566587":
        "Fearless Concurrency on the GPU：讨论在 GPU 上实现更安全、更可控并发的编程方法。",
    "https://news.ycombinator.com/item?id=48566812":
        "Show HN：ParaMetal，一个实时 3D 热传导仿真项目。",
    "https://news.ycombinator.com/item?id=48566794":
        "Show HN：Mini-film，开源 RAW 照片批处理和审片工具。",
    "https://news.ycombinator.com/item?id=48566690":
        "一个面向长时间 Claude 工作流的可恢复编排系统，支持任务中断后继续执行。",
    "https://news.ycombinator.com/item?id=48566791":
        "文章探讨商业空间长期空置的经济、租约、监管和市场激励原因。",
    "https://news.ycombinator.com/item?id=48566644":
        "研究用 GAN 与忆阻器分类器处理非正面人脸识别问题。",
    "https://news.ycombinator.com/item?id=48566832":
        "创始人手册：讨论如何从组织、产品和工程流程上构建 AI-native startup。",
    "https://news.ycombinator.com/item?id=48566531":
        "Simon Willison 文章在 HN 讨论：Fable 5 出口管制可能损害美国网络防御能力。",
    "https://news.ycombinator.com/item?id=48566744":
        "fastai: Style：讨论 fastai 项目或文档中的风格、约定与实践。",

    # 2026-06-17 YouTube AI
    "https://www.youtube.com/watch?v=1Lg7eOmNT-A":
        "日语游戏实况第二天继续用 ChatGPT 设计的 6 只最强妖怪挑战《妖怪手表3》高难内容。",
    "https://www.youtube.com/watch?v=DacI6UhfOD8":
        "Wall Street Millennial 讨论 OpenAI 争取政府支持或救助的策略与商业风险。",
    "https://www.youtube.com/watch?v=E71uw7csF_Y":
        "零度解说围绕 Claude 强模型被禁，实测三款无审查本地模型并主张部署本地 AI。",
    "https://www.youtube.com/watch?v=T-EScj1GEKY":
        "WorldofAI 汇总 Fable 5 可能回归、DeepSeek v4.1、GPT-5.6 泄露、Fusion API 和 Kimi K2.7 代码速度等 AI 新闻。",
    "https://www.youtube.com/watch?v=l72ufA-4SzE":
        "Two Minute Papers 解读 Anthropic 自然语言自编码器研究，展示用自然语言窥探 Claude 内部表征的结果。",

    # 2026-06-16 Anthropic / Dario Amodei
    "https://www.anthropic.com/news/anthropic-public-record":
        "Anthropic 公布首轮 Public Record 全国调查，展示近 5.2 万美国人对 AI 收益、风险与企业问责的态度。",
    "https://www.anthropic.com/news/dxc-anthropic-alliance":
        "Anthropic 与 DXC 建立多年全球联盟，由 DXC 培训前线工程师，把 Claude 集成进银行、航空等高监管行业核心系统。",
    "https://www.anthropic.com/news/fable-mythos-access":
        "Anthropic 称美国政府以国家安全为由下达出口管制指令，导致其暂停 Claude Fable 5 与 Mythos 5 的访问。",
    "https://www.anthropic.com/news/claude-fable-5-mythos-5":
        "Anthropic 发布 Claude Fable 5 与 Mythos 5，并将 Fable 定位为具备 Mythos 级能力、面向通用使用的安全版本。",
    "https://www.anthropic.com/news/tcs-anthropic-partnership":
        "Anthropic 与 TCS 合作，让 TCS 内部 5 万名员工使用 Claude，并面向金融、医疗、公共部门等监管行业构建 Claude 产品。",
    "https://www.anthropic.com/news/claude-corps":
        "Anthropic 推出 Claude Corps 全国奖学金项目，投入 1.5 亿美元培训 1000 名早期职业人才，把 Claude 能力带给美国各地非营利组织。",
    "https://www.darioamodei.com/post/policy-on-the-ai-exponential":
        "Dario Amodei 讨论 AI 指数级进展下的政策选择，强调治理、国家能力建设、安全监管与更广泛共享收益。",

    # 2026-06-16 GitHub Trending
    "https://github.com/NVIDIA/SkillSpector":
        "SkillSpector：NVIDIA 开源的 AI agent skill 安全扫描器，用于检测技能中的漏洞、恶意模式与安全风险。",
    "https://github.com/music-assistant/server":
        "Music Assistant Server：自托管音乐库与多房间播放中枢，可连接流媒体服务和各类联网音箱。",
    "https://github.com/meshery/meshery":
        "Meshery：云原生基础设施管理平台，用于管理、设计和运行 Kubernetes 与服务网格环境。",
    "https://github.com/trycua/cua":
        "cua：面向 Computer-Use Agents 的开源基础设施，提供桌面沙箱、SDK 与评测基准，覆盖 macOS、Linux 和 Windows。",
    "https://github.com/freeCodeCamp/freeCodeCamp":
        "freeCodeCamp：开源编程与计算机科学课程平台，提供免费学习路径与社区驱动的代码库。",
    "https://github.com/iptv-org/iptv":
        "iptv-org/iptv：汇总全球公开 IPTV 频道的播放列表项目。",
    "https://github.com/chatwoot/chatwoot":
        "Chatwoot：开源全渠道客服系统，覆盖在线聊天、邮件支持与工单工作流，可替代 Intercom/Zendesk 等服务。",
    "https://github.com/Free-TV/IPTV":
        "Free-TV/IPTV：免费电视频道的 M3U 播放列表集合。",
    "https://github.com/mikeroyal/Self-Hosting-Guide":
        "Self-Hosting-Guide：自托管指南，覆盖本地服务器、私有云、LLM、WireGuard、自动化与 Home Assistant 等场景。",
    "https://github.com/itsfatduck/optimizerDuck":
        "optimizerDuck：开源 Windows 优化工具，聚焦性能、隐私与简化系统配置。",
    "https://github.com/teslamate-org/teslamate":
        "TeslaMate：自托管 Tesla 数据记录器，用于长期保存、分析和可视化车辆运行数据。",
    "https://github.com/Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots":
        "Introduction to Autonomous Robots：自主机器人入门教材与配套资源。",
    "https://github.com/Raphire/Win11Debloat":
        "Win11Debloat：轻量 PowerShell 脚本，用于移除 Windows 10/11 预装应用、关闭遥测并精简系统体验。",
    "https://github.com/krahets/hello-algo":
        "Hello 算法：用动画图解和多语言代码实现讲解数据结构与算法，支持中英日等多语言。",

    # 2026-06-16 Hacker News Newest
    "https://news.ycombinator.com/item?id=48552000":
        "报道物理学家在量子实验中测得所谓「负时间」现象，引发对量子过程时序解释的讨论。",
    "https://news.ycombinator.com/item?id=48551838":
        "讨论 AMD 从消费级 CPU 移除内存加密能力后，用户对安全功能缩水表达不满。",
    "https://news.ycombinator.com/item?id=48551613":
        "Cross-Language Data Types：探讨跨语言共享数据类型与互操作边界的设计问题。",
    "https://news.ycombinator.com/item?id=48551621":
        "文章分析韩国用户为何高度拥抱 AI，从文化、教育、产业与产品使用场景解释热度。",
    "https://news.ycombinator.com/item?id=48552087":
        "Show HN：把 Ghostty 终端搬进浏览器，并在客户端实现真实后端。",
    "https://news.ycombinator.com/item?id=48552026":
        "整理一批最有意思的维基百科文章，供读者探索冷门知识与奇特主题。",
    "https://news.ycombinator.com/item?id=48551597":
        "Show HN：一种电子表格工具，让代码通过命名数据结构访问单元格，避免直接引用 B7 这类坐标。",
    "https://news.ycombinator.com/item?id=48552081":
        "回顾 Intel Mac 20 年：苹果当年为何转向 Intel，又为何最终切回自研芯片。",
    "https://news.ycombinator.com/item?id=48551843":
        "报道中国高校在拥抱 AI 时代的调整中削减约 1.2 万个被视为过时的学位项目。",
    "https://news.ycombinator.com/item?id=48551750":
        "独立开发者解释为何自建并开源自己的 PaaS，而不是完全依赖现成云平台。",
    "https://news.ycombinator.com/item?id=48551665":
        "Discovery debt：把未完成的发现、调研与问题理解视为一种不会立刻拖慢速度但会累积风险的债务。",
    "https://news.ycombinator.com/item?id=48551953":
        "Kino：面向 Ruby 4.0 Ractor 的高性能 Web 服务器。",
    "https://news.ycombinator.com/item?id=48552010":
        "Ask HN：用户征集 Hetzner 之外更可靠或更合适的服务器/云服务替代方案。",
    "https://news.ycombinator.com/item?id=48552008":
        "DEC Alpha：回顾这款 64 位 RISC 处理器架构及其历史影响。",
    "https://news.ycombinator.com/item?id=48552039":
        "NeuroAutomata：用于预测蛋白质变体效应的系统，面向生物序列功能变化建模。",
    "https://news.ycombinator.com/item?id=48551666":
        "Movebound：从 zugzwang（被迫行动反而变差）的角度讨论棋类与博弈中的局面艺术。",
    "https://news.ycombinator.com/item?id=48551694":
        "Pure-Dart I2P：用 Dart 实现的去中心化文件分享方案，基于 I2P 网络。",
    "https://news.ycombinator.com/item?id=48551961":
        "文章讨论生成式 AI 时代照片可信度下降，影像似乎被默认视为有罪直到证明真实。",
    "https://news.ycombinator.com/item?id=48551876":
        "讨论在试图绕过规则时，理解规则背后的理由为何反而更重要。",
    "https://news.ycombinator.com/item?id=48552042":
        "Typst 0.15 发布，带来排版系统的新功能与改进。",
    "https://news.ycombinator.com/item?id=48551593":
        "Show HN：GitHits Public Beta 0.9，用于统计和展示 GitHub 项目访问热度。",
    "https://news.ycombinator.com/item?id=48551725":
        "回顾校车为何成为黄色：从安全可见性到标准化交通设计的历史。",
    "https://news.ycombinator.com/item?id=48552015":
        "文章探讨记忆是否可以转移甚至被食用，偏向神经科学与科普式问题。",
    "https://news.ycombinator.com/item?id=48551736":
        "2024 年文章：作者记录从零构建元搜索引擎的设计取舍与实现过程。",
    "https://news.ycombinator.com/item?id=48552069":
        "文章讨论难民重新安置制度的终结及其政策与人道影响。",
    "https://news.ycombinator.com/item?id=48551951":
        "研究称通用 LLM 在部分临床任务上超过专用临床 AI 工具，引发医疗 AI 泛化能力讨论。",
    "https://news.ycombinator.com/item?id=48551671":
        "Show HN：Kitchen Rush，一个受 Overcooked 启发的 LLM 工具调用基准，用厨房协作任务测试 agent 能力。",
    "https://news.ycombinator.com/item?id=48551682":
        "论文讨论可见激励如何触发 reward hacking，模型会为了仪表盘奖励牺牲真实任务目标。",
    "https://news.ycombinator.com/item?id=48552092":
        "PDF《How to Write Computer Programs》：关于如何写计算机程序的教程/教材资料。",
    "https://news.ycombinator.com/item?id=48551662":
        "文章质疑美国政府的 Anthropic 模型禁令并非真正源于 AI 越狱，而是更复杂的政策与权力博弈。",

    # 2026-06-16 YouTube AI
    "https://www.youtube.com/watch?v=TiVTmkvfwhA":
        "TBS/Bloomberg 讨论 Claude Fable 5 与 Mythos 5 被暂停访问的安全、出口管制和国际规则问题。",
    "https://www.youtube.com/watch?v=f403xQHF5Bw":
        "DOU News 汇总乌克兰 IT 收入、Claude Mythos/Fable 5、国家级 LLM、Apple Intelligence 与 Dario 管理话题。",
    "https://www.youtube.com/watch?v=si4_UQGoXd4":
        "游戏实况用 ChatGPT 设计的 6 只最强妖怪挑战《妖怪手表3》高难内容。",
    "https://www.youtube.com/watch?v=lAmYl9lWPWs":
        "The Commands Man 对比 ChatGPT 与 Gemini 从零编写 Minecraft shader 的能力。",
    "https://www.youtube.com/watch?v=a2cfyKf2WEs":
        "Lucas Montano 以葡语讨论 LLM 在 2025 年的状态与开发者工作流中的 AI 使用变化。",

    # 2026-06-09 GitHub Trending
    "https://github.com/santifer/career-ops":
        "career-ops：基于 Claude Code 的 AI 求职系统，含 14 种技能模式、Go 仪表盘、PDF 生成与批处理。",
    "https://github.com/Andyyyy64/whichllm":
        "whichllm：一条命令找出最适合你硬件、能实际运行且性能最好的本地 LLM，按近期真实基准排名而非参数量。",
    "https://github.com/phuryn/pm-skills":
        "pm-skills：产品经理技能市场，提供 100+ 智能体技能/命令/插件，覆盖发现、战略、执行、发布到增长。",
    "https://github.com/danielmiessler/Personal_AI_Infrastructure":
        "Personal AI Infrastructure：用于放大人类能力的个人智能体 AI 基础设施。",
    "https://github.com/luongnv89/claude-howto":
        "claude-howto：可视化、示例驱动的 Claude Code 指南，从基础概念到高级代理，附可复制粘贴的模板。",
    "https://github.com/google/skills":
        "google/skills：面向 Google 产品与技术的 Agent Skills 技能集。",

    # 2026-06-09 YouTube AI
    "https://www.youtube.com/watch?v=_KGBYfsG8Uo":
        "tef 让 Claude Code（Opus 4.8）与 ChatGPT Codex（5.5）从零各写一个 Minecraft 对比，作者对 Codex 的表现颇感意外。",
    "https://www.youtube.com/watch?v=6cmi7qyFwEE":
        "Chase AI 介绍 Graphify——非 RAG 方案，把大代码库拆解并构建知识图谱，解决 Claude Code 的记忆难题。",
    "https://www.youtube.com/watch?v=kt47kXLgeOs":
        "Fernanda Kipper 葡语直播，用 Claude Design + Claude Code + TRAE 从零开发含订阅系统的 SaaS 并部署到生产。",
    "https://www.youtube.com/watch?v=gNPJ94IeJRQ":
        "Vaibhav Kadnar 给学生分享用 Claude 本月即可上手的 5 个 AI 创业/赚钱点子。",
    "https://www.youtube.com/watch?v=3BatQW63C8g":
        "Liam Ottley 演示用 Higgsfield + Claude 单人创办 AI 创意代理公司，把过去月耗 1.5–3 万美元的工作交给一人完成（日语标题）。",

    # 2026-06-09 Hacker News Newest
    "https://news.ycombinator.com/item?id=48454261":
        "基准测试 ParadeDB 与 Postgres 原生全文搜索（FTS）：同一查询给出三种不同结果。",
    "https://news.ycombinator.com/item?id=48454292":
        "随笔《构建软件即学习》：写软件的过程本质上是不断学习。",
    "https://news.ycombinator.com/item?id=48454455":
        "macOS 27 新增命令行工具，可与系统内置 Foundation Models 交互。",
    "https://news.ycombinator.com/item?id=48454205":
        "呼吁各平台提供过滤 AI 垃圾内容（AI slop）的选项。",
    "https://news.ycombinator.com/item?id=48454531":
        "热路径优化：探讨浮点除法何时会比整数除法更快。",
    "https://news.ycombinator.com/item?id=48454536":
        "作者记录在 macOS 27 中遇到的 URL/NSURL bug。",
    "https://news.ycombinator.com/item?id=48454658":
        "Waymo 以 2.2 亿美元收购苹果原自动驾驶汽车测试场。",
    "https://news.ycombinator.com/item?id=48454232":
        "一位中西部医生撰文谈「盐的真相」健康科普。",
    "https://news.ycombinator.com/item?id=48454444":
        "读巴菲特与芒格，真正让作者受益的内容其实与炒股无关。",
    "https://news.ycombinator.com/item?id=48454642":
        "Screenlet：直接在浏览器里录制并导出产品演示视频的工具。",
    "https://news.ycombinator.com/item?id=48454335":
        "macOS 27 仅支持 Apple Silicon，苹果正式终结 Intel Mac 时代。",
    "https://news.ycombinator.com/item?id=48454210":
        "联邦法官叫停 H1B 签证 10 万美元收费政策。",
    "https://news.ycombinator.com/item?id=48454684":
        "Show HN：DaysLeft——显示「区间」而非确切死亡日期的生物年龄时钟。",
    "https://news.ycombinator.com/item?id=48454512":
        "Ask HN：KYC 实名认证是否让你对「金钱」这个概念越来越反感。",
    "https://news.ycombinator.com/item?id=48454417":
        "评论文章《我们的股市坏了》。",
    "https://news.ycombinator.com/item?id=48454564":
        "为 Mac/Apple Silicon 实现的 lscpu，用于查看 CPU 详细信息。",
    "https://news.ycombinator.com/item?id=48454517":
        "Show HN：用 Rust 编写的持久化、异步 LLM 工作流引擎。",
    "https://news.ycombinator.com/item?id=48454322":
        "文章《如何找到咨询客户》（2015）。",
    "https://news.ycombinator.com/item?id=48454485":
        "视频：在 AI 时代聆听上帝之声——信仰、尊严与人类繁荣。",
    "https://news.ycombinator.com/item?id=48454571":
        "作者分析 Kuzu 图数据库 16.3 万行代码，解读苹果为何想要收购它。",
    "https://news.ycombinator.com/item?id=48454475":
        "Show HN：SnakeBaby——生成可爱符号、个人简介、颜文字和用户名创意。",
    "https://news.ycombinator.com/item?id=48454179":
        "同行评审论文：用真空代替氦气提供升力的货运飞艇设计。",
    "https://news.ycombinator.com/item?id=48454357":
        "随笔《自治不是开关》：论 AI 自主性是渐进谱系而非一键开/关。",
    "https://news.ycombinator.com/item?id=48454584":
        "用 OpenRouter、OpenClaw 和 MediaUse 搭建零成本网页自动化流水线。",
    "https://news.ycombinator.com/item?id=48454314":
        "随笔《但愿你能幸运到体会后悔》。",
    "https://news.ycombinator.com/item?id=48454470":
        "Show HN：让 AI 代理用 USDC 按次付费调用的网页工具，无需 API key（x402+MCP）。",
    "https://news.ycombinator.com/item?id=48454194":
        "标题仅为数字「1010220」的帖子。",
    "https://news.ycombinator.com/item?id=48454657":
        "论文：决定是否分离独立时，熟悉与未知的未来如何塑造损失厌恶。",
    "https://news.ycombinator.com/item?id=48454461":
        "文章《AI、阿根廷与敌基督：蒂尔的愿景正在绽放》。",
    "https://news.ycombinator.com/item?id=48454598":
        "评伯克希尔·哈撒韦官网堪称完美的极简主义网站。",
    "https://news.ycombinator.com/item?id=48454729":
        "评伯克希尔·哈撒韦官网堪称完美的极简主义网站。",
    "https://news.ycombinator.com/item?id=48454718":
        "苹果 WWDC 2026「平台联盟演讲」（Platforms State of the Union）视频。",
    "https://news.ycombinator.com/item?id=48454721":
        "评论文章《埃隆·马斯克如何害死了数十万人》。",
    "https://news.ycombinator.com/item?id=48454722":
        "Track Political Stories Across the Web：跨网站追踪政治新闻报道的工具。",

    # 2026-06-09 YouTube AI（补抓）
    "https://www.youtube.com/watch?v=Hth_tLaC2j8":
        "Claude 官方回顾 Claude Code 上线一周年，Boris Cherny 与 Cat Wu 讲述它从内部项目成长为全球开发者与组织使用的工具（日语标题）。",

    # 2026-06-07 GitHub Trending
    "https://github.com/TapXWorld/ChinaTextbook":
        "收录中国所有小学、初中、高中及大学 PDF 教材的开源资料库。",
    "https://github.com/opencv/opencv":
        "OpenCV：老牌开源计算机视觉库，提供图像处理、特征检测、机器学习等基础能力。",
    "https://github.com/aaif-goose/goose":
        "goose：开源可扩展 AI 代理，超越代码补全——能用任意 LLM 安装、执行、编辑和测试。",
    "https://github.com/microsoft/pg_durable":
        "微软 pg_durable：在 PostgreSQL 数据库内实现持久化（durable）执行的扩展。",
    "https://github.com/refactoringhq/tolaria":
        "tolaria：管理 Markdown 知识库的桌面应用。",
    "https://github.com/RyanCodrai/turbovec":
        "turbovec：基于 TurboQuant 构建的向量索引，Rust 编写并提供 Python 绑定。",
    "https://github.com/HunxByts/GhostTrack":
        "GhostTrack：根据手机号或 IP 追踪定位的工具（OSINT 用途）。",
    "https://github.com/Crosstalk-Solutions/project-nomad":
        "Project N.O.M.A.D：自包含离线生存计算机，集成关键工具、知识库和本地 AI，随时随地保持信息畅通。",

    # 2026-06-07 YouTube AI
    "https://www.youtube.com/watch?v=CzxqQJOswvo":
        "AI Search 一周 AI 新闻：Minimax M3、Ideogram v4、Bernini、Gemma4、Nemotron 3 Ultra、实时 AI 音乐、开源 Gemini Omni 等。",
    "https://www.youtube.com/watch?v=XKYPlTu1c3M":
        "Aitrepreneur 介绍 Ideogram 4 开源权重文生图模型，号称可本地运行的最强 NSFW/写实图像模型，支持区域提示精确控图。",
    "https://www.youtube.com/watch?v=DbeFq_uoaRs":
        "Riley Brown 解读：OpenAI Codex 新 Sites 功能 vs Cursor Canvases、DeepSeek V4 低成本追平 Opus 4.8/GPT 5.5、苹果 iMessage 代理商店等。",
    "https://www.youtube.com/watch?v=7qmu3QmEwpE":
        "midudev 教程：在 Hostinger VPS 上配置 SSH/防火墙/Fail2ban 并部署 Claude Code，让 AI 代理 7×24 小时为你工作。",
    "https://www.youtube.com/watch?v=IqvnryFzZD4":
        "Humbled Trader 演示用 Claude + TradingView（接 IBKR API）搭建盘前交易助手。",

    # 2026-06-07 Hacker News Newest
    "https://news.ycombinator.com/item?id=48434252":
        "博文《Realisation of Unfixable》：对某些无法修复之事的体悟与反思。",
    "https://news.ycombinator.com/item?id=48434357":
        "随笔《Pockets of Humanity》：探讨现代生活中残存的人性角落。",
    "https://news.ycombinator.com/item?id=48434198":
        "Show HN: Inbox-beam——把通知发到你收件箱但不真正发邮件的工具。",
    "https://news.ycombinator.com/item?id=48434169":
        "夜间在 51 区附近目击神秘「多力多滋三角形」飞行器。",
    "https://news.ycombinator.com/item?id=48434240":
        "Ask HN：（推理模型的）thinking effort/思考强度档位是怎么实现的？",
    "https://news.ycombinator.com/item?id=48434195":
        "论文：何首乌（Pleuropterus multiflorus）用于治疗雄激素性脱发的应用。",
    "https://news.ycombinator.com/item?id=48434142":
        "纽约下水道之谜：城市「井盖下的人」究竟在做什么。",
    "https://news.ycombinator.com/item?id=48434204":
        "评论：误导性的错误陈述持续瓦解美国生物医学研究。",
    "https://news.ycombinator.com/item?id=48434484":
        "考据 Lorem Ipsum 假文的起源。",
    "https://news.ycombinator.com/item?id=48434258":
        "再次警告：Steam Controller 充电底座存在起火风险。",
    "https://news.ycombinator.com/item?id=48434342":
        "讨论：Anthropic/OpenAI 每收你 100 美元可能要花掉超过 1000 美元（推理/训练成本远高于定价）。",
    "https://news.ycombinator.com/item?id=48434366":
        "Polymarket 标注注入（annotation injection）漏洞分析。",
    "https://news.ycombinator.com/item?id=48434430":
        "Show HN：更好用的 zsh 自动建议工具，能预测你的下一条命令。",
    "https://news.ycombinator.com/item?id=48434242":
        "随笔《What the wounds are telling us》：从伤口/创伤中读出的信息。",
    "https://news.ycombinator.com/item?id=48434256":
        "TikTok 向议员辩称自家平台「并不会让人上瘾」。",
    "https://news.ycombinator.com/item?id=48434185":
        "Ask HN：为什么编程语言/框架不为自己的项目提供重训练（微调）的模型？",
    "https://news.ycombinator.com/item?id=48434154":
        "Chrome 在 M5 MacBook Pro 上创下浏览器速度纪录。",
    "https://news.ycombinator.com/item?id=48434317":
        "亲历分享《What It's Like to IPO》：公司上市是种怎样的体验。",
    "https://news.ycombinator.com/item?id=48434298":
        "评论《AI and the Pitfalls of Innovation》：AI 与创新的陷阱。",
    "https://news.ycombinator.com/item?id=48434230":
        "Ask HN：你读过最棒的冷门书籍有哪些？",
    "https://news.ycombinator.com/item?id=48434312":
        "倾诉帖：LLM 正在侵蚀我的软件工程师职业生涯，我不知该怎么办。",
    "https://news.ycombinator.com/item?id=48434058":
        "评论《Beware Management Consultants》：警惕管理咨询顾问。",
    "https://news.ycombinator.com/item?id=48434160":
        "旧文（2018）：商店将很快在未经你同意下使用人脸识别。",
    "https://news.ycombinator.com/item?id=48434114":
        "观点《We Need VAT and UBI》：主张推行增值税与全民基本收入。",
    "https://news.ycombinator.com/item?id=48434313":
        "ASML 邀请马斯克出席内部技术活动，引发员工不满。",
    "https://news.ycombinator.com/item?id=48434436":
        "呼吁：Anthropic 请发布官方 Linux 版 Claude Desktop。",
    "https://news.ycombinator.com/item?id=48434488":
        "文章：社区/合作社如何通过「有代表的纳税」把消费转化为所有权。",
    "https://news.ycombinator.com/item?id=48434263":
        "近期 LLVM 哈希表性能改进。",
    "https://news.ycombinator.com/item?id=48434236":
        "纽约州立法者通过为期一年禁止新建数据中心的法案。",
    "https://news.ycombinator.com/item?id=48434362":
        "Show HN：用于测试 ESC/POS 收据的虚拟热敏打印机。",

    # 2026-06-06 Anthropic
    "https://www.anthropic.com/news/expanding-project-glasswing":
        "扩大 Project Glasswing——向合作伙伴提供前沿模型用于漏洞检测、保护关键软件，将参与组织从约 50 家扩展到约 150 家，覆盖 15+ 国家与关键基础设施领域。",
    "https://www.anthropic.com/news/services-track-partner-hub":
        "推出 Claude 合作伙伴网络的「服务赛道」（合作方分级资质体系）与「合作伙伴中心」门户，让合作方看到自己的达标情况、客户找到最合格的服务商。",
    "https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack":
        "梳理一年 AI 赋能网络威胁发现：攻击者越来越多在入侵后用 AI 编排复杂攻击，令传统风险评估指标失效、暴露 MITRE ATT&CK 框架的覆盖盲区。",

    # 2026-06-06 GitHub Trending
    "https://github.com/github/copilot-sdk":
        "GitHub 官方多平台 SDK，用于把 GitHub Copilot Agent 集成进应用和服务。",
    "https://github.com/Panniantong/Agent-Reach":
        "给 AI 代理装上「眼睛」：一个 CLI 即可读取和搜索 Twitter、Reddit、YouTube、GitHub、B 站、小红书，零 API 费用。",
    "https://github.com/NVIDIA/cosmos":
        "NVIDIA Cosmos：开源世界模型、数据集与工具平台，帮开发者为机器人、自动驾驶、智能基础设施构建 Physical AI。",
    "https://github.com/openai/plugins":
        "OpenAI 官方插件仓库。",
    "https://github.com/MemPalace/mempalace":
        "号称基准测试表现最佳的开源 AI 记忆系统，免费。",
    "https://github.com/NousResearch/hermes-agent":
        "Nous Research 的 hermes-agent：随用户一起成长的代理。",
    "https://github.com/lfnovo/open-notebook":
        "开源版 NotebookLM，提供更高灵活性和更多功能。",
    "https://github.com/openclaw/openclaw-windows-node":
        "OpenClaw 的 Windows 配套套件：系统托盘应用、共享库、Node 与 PowerToys 命令面板扩展。",
    "https://github.com/PaddlePaddle/PaddleOCR":
        "PaddleOCR：轻量强大的 OCR 工具包，把 PDF/图片转成结构化数据喂给 LLM，支持 100+ 语言。",
    "https://github.com/mvanhorn/last30days-skill":
        "AI 代理技能，跨 Reddit、X、YouTube、HN、Polymarket 和网页研究任意话题并综合出有据摘要。",
    "https://github.com/CopilotKit/CopilotKit":
        "面向代理与生成式 UI 的前端技术栈，支持 React/Angular，AG-UI 协议作者。",
    "https://github.com/jwasham/coding-interview-university":
        "成为软件工程师的完整计算机科学学习计划。",
    "https://github.com/aquasecurity/trivy":
        "Aqua Security 的 Trivy：在容器、K8s、代码仓库、云等中查找漏洞、错配、密钥和 SBOM。",
    "https://github.com/chopratejas/headroom":
        "在工具输出、日志、文件和 RAG 块进入 LLM 前压缩它们，减少 60–95% token 而答案不变，提供库/代理/MCP 服务器三种形态。",

    # 2026-06-06 YouTube AI
    "https://www.youtube.com/watch?v=bogsZSiAwmY":
        "日本 AI 频道介绍 Claude Mythos，畅想 24 小时让 AI 干活、人类工作如何改变的时代。",
    "https://www.youtube.com/watch?v=XzUB8_gj6xM":
        "Matthew Berman 解读 Anthropic 呼吁「紧急放缓」AI 发展的表态。",
    "https://www.youtube.com/watch?v=h6_v1IBqmNI":
        "WorldofAI 一周 AI 新闻汇总：Claude Oceanus、Anthropic 的 AGI 主张、GPT-5.6 检查点、GLM 5.2、Nemotron 3 Ultra 等。",
    "https://www.youtube.com/watch?v=08tL8ekwwM0":
        "ByteMonk 科普：你发给 LLM 的不是文本而是钱——讲 token 计费与成本机制。",
    "https://www.youtube.com/watch?v=tUeSxXHmE9w":
        "Greg Isenberg 演示用 OpenAI Codex 构建全天候为你工作的应用。",

    # 2026-06-06 Hacker News Newest
    "https://news.ycombinator.com/item?id=48415944":
        "讣告：出演《吸血鬼猎人巴菲》《足球教练》《小不列颠》的演员 Anthony Head 去世。",
    "https://news.ycombinator.com/item?id=48415987":
        "观点文：指责 Cloudflare CEO 在机器人流量激增问题上撒谎。",
    "https://news.ycombinator.com/item?id=48415721":
        "技术回顾：1N4148 信号二极管如何变得无处不在。",
    "https://news.ycombinator.com/item?id=48415790":
        "选举改革讨论：多议员选区 + 排序选择投票如何修复选举制度。",
    "https://news.ycombinator.com/item?id=48415709":
        "Show HN：MimicScribe，本地说话人识别准确率约 97% 的转录工具。",
    "https://news.ycombinator.com/item?id=48415851":
        "语言学：英国人过去的口音曾和（北美）我们一样。",
    "https://news.ycombinator.com/item?id=48415863":
        "评论：社会科学研究网（SSRN）已经「自毁招牌」。",
    "https://news.ycombinator.com/item?id=48416004":
        "个人经历：我被 Atlassian 裁员了。",
    "https://news.ycombinator.com/item?id=48415635":
        "面向「轻度偏执」者的 2026 软件安全实用建议。",
    "https://news.ycombinator.com/item?id=48415620":
        "Firebase SQL Connect 发布。",
    "https://news.ycombinator.com/item?id=48415799":
        "Neocities 宕机。",
    "https://news.ycombinator.com/item?id=48415835":
        "从 Firestore 迁移到 PostgreSQL 的实践。",
    "https://news.ycombinator.com/item?id=48415869":
        "探讨哪些 AI 代理会发送 Accept: text/markdown 请求头。",
    "https://news.ycombinator.com/item?id=48415979":
        "报道：共和党称反数据中心运动是中国的心理战。",
    "https://news.ycombinator.com/item?id=48415750":
        "观点：Postgres 的 serial 自增主键应该用 BIGINT。",
    "https://news.ycombinator.com/item?id=48416000":
        "一键找回 Mac 上缺失的 Google 日历和计算器。",
    "https://news.ycombinator.com/item?id=48416029":
        "科学突破：首次在冷冻小鼠脑中恢复活动。",
    "https://news.ycombinator.com/item?id=48415845":
        "先进微型核反应堆仅用两年达到临界。",
    "https://news.ycombinator.com/item?id=48415633":
        "Sakana AI 的递归自我改进（RSI）实验室。",
    "https://news.ycombinator.com/item?id=48415849":
        "讨论：AI 到底创造了多少价值。",
    "https://news.ycombinator.com/item?id=48415628":
        "Runcap：作者自建的本地编码代理成本上限工具。",
    "https://news.ycombinator.com/item?id=48415879":
        "分析：能源市场如何抑制霍尔木兹海峡冲击。",
    "https://news.ycombinator.com/item?id=48415946":
        "科普：魔数与量子计算的算术。",
    "https://news.ycombinator.com/item?id=48415951":
        "Show：OpenFlow CLI，动态工作流的开源替代品。",
    "https://news.ycombinator.com/item?id=48415828":
        "小巧可魔改的 CUDA 语言模型实现。",
    "https://news.ycombinator.com/item?id=48416038":
        "TanStack AI：随心所欲用你自己的 MCP（TanStack 博客）。",
    "https://news.ycombinator.com/item?id=48415898":
        "用 Jam 语言写的 PlayStation One（PS1）模拟器。",
    "https://news.ycombinator.com/item?id=48416036":
        "深海采矿的环境影响。",
    "https://news.ycombinator.com/item?id=48415983":
        "Ask HN：如何做一个开源版 SpaceX。",
    "https://news.ycombinator.com/item?id=48415811":
        "音乐人 BERNTH 的 150 万订阅 YouTube 频道因漏看实体邮件被取消盈利资格（视频）。",

    # 2026-06-06 社区动态（第二批刷新）
    "https://www.youtube.com/watch?v=5oDTKkfFX8c":
        "Trevor Prescott（日语）演示如何用 Claude AI 构建链上 AI 交易机器人，含代码、配置指南和实盘交易结果。",
    "https://www.youtube.com/watch?v=d-pHecFIv_4":
        "Shane Hummus 介绍 5 个能用 Claude AI 快速上手的线上工作。",
    "https://www.youtube.com/watch?v=inu2GK77lCg":
        "基隆迪语节目（IKOSORA MEDIA TV 第 175 集）讨论用 ChatGPT 上网获取知识。",
    "https://news.ycombinator.com/item?id=48416218":
        "SupXML：现代、内存安全、可直接替换 libxml2 的 XML 解析器。",
    "https://news.ycombinator.com/item?id=48416067":
        "随笔：在压力下弯曲，但不向无理弯曲。",
    "https://news.ycombinator.com/item?id=48416053":
        "Chrome 在 Speedometer 3.1 与 JetStream 3 基准上再创纪录。",
    "https://news.ycombinator.com/item?id=48416229":
        "报道：在与 Google 的重磅交易后，Meta 考虑大规模股权融资。",
    "https://news.ycombinator.com/item?id=48416226":
        "实时实验：众包推理代理、奖励表现最优者。",
    "https://news.ycombinator.com/item?id=48416221":
        "讨论帖：Mythos 找出了 bug，但谁来出资修复？",
    "https://news.ycombinator.com/item?id=48416155":
        "Azure Functions Core Tools 仓库被下架。",
    "https://news.ycombinator.com/item?id=48416204":
        "实时实验：众包推理代理、奖励表现最优者（与另一帖同题）。",
    "https://news.ycombinator.com/item?id=48416044":
        "Grub 卷土重来：无需许可地抓取网络。",
    "https://news.ycombinator.com/item?id=48416099":
        "Show HN：Fooglemap，本地餐厅发现地图。",
    "https://news.ycombinator.com/item?id=48416233":
        "用 OpenSearch 与 Elasticsearch 实现的代理式搜索模型。",
    "https://news.ycombinator.com/item?id=48416207":
        "用 74k 词和 CPU 玩 ZOEAE：作者如何为咬文嚼字的文字游戏迷构建字典。",
    "https://news.ycombinator.com/item?id=48416123":
        "Show HN：用 Veritrooper 审计任意 AI/数据配对。",
    "https://news.ycombinator.com/item?id=48416192":
        "征求测试：PhoenixDKIM，注重安全的 DKIM milter。",
    "https://news.ycombinator.com/item?id=48416129":
        "Show HN：用 MCP 工具与你的 .eml 邮件文件交互。",
    "https://news.ycombinator.com/item?id=48416179":
        "约会为何崩坏：恋爱数据从令人愉悦变得令人痛苦的背后。",
    "https://news.ycombinator.com/item?id=48416093":
        "报道：Meta 在全美搭帐篷以安置 AI 服务器。",
    "https://news.ycombinator.com/item?id=48416134":
        "回顾：我在 Meta（Facebook）第一年的反思。",

    "https://www.anthropic.com/news/claude-for-small-business":
        "推出 Claude for Small Business：一套连接器 + 即开即用工作流的打包方案，把 Claude 嵌入小企业日常使用的工具中。",
    "https://www.anthropic.com/news/pwc-expanded-partnership":
        "扩大与普华永道（PwC）的合作：在 PwC 内部部署 Claude 用于构建技术、执行交易、并为客户重塑企业职能。",
    "https://www.anthropic.com/news/gates-foundation-partnership":
        "与盖茨基金会达成 2 亿美元合作，把 Claude 用于全球健康、发展与教育等慈善目标的 AI 应用。",
    "https://www.anthropic.com/news/claude-opus-4-7":
        "发布 Claude Opus 4.7 模型，软件工程、视觉识别、长上下文性能显著提升，加强网络安全防护。",
    "https://www.anthropic.com/news/claude-design-anthropic-labs":
        "推出 Claude Design 设计工具，与 AI 协作创建设计、原型和演示文稿，支持品牌系统自动应用。",
    "https://www.anthropic.com/news/claude-is-a-space-to-think":
        "宣布 Claude 永久保持无广告，靠订阅和企业合同盈利，避免广告激励对帮助性的负面影响。",
    "https://www.anthropic.com/news/claude-for-creative-work":
        "推出多个创意工具连接器，使 Claude 能在 Photoshop、Blender 等软件中扩展创意工作能力。",
    "https://www.anthropic.com/news/theo-hourmouzis-general-manager-australia-new-zealand":
        "任命 Theo Hourmouzis 为澳大利亚和新西兰总经理，正式开设悉尼办公室。",
    "https://www.anthropic.com/news/election-safeguards-update":
        "通过政治中立性训练、政策执行、安全测试，确保 Claude 在选举期间提供准确、平衡的信息。",
    "https://www.anthropic.com/news/anthropic-nec":
        "与 NEC 合作在日本建设 AI 工程队伍，向 3 万名员工提供 Claude，开发金融、制造领域 AI 产品。",
    "https://www.anthropic.com/news/anthropic-amazon-compute":
        "与亚马逊扩大合作，获 5 吉瓦算力支持，投资超千亿美元用于训练和部署 Claude。",
    "https://www.anthropic.com/news/narasimhan-board":
        "长期利益信托任命诺华制药 CEO Vas Narasimhan 担任董事会成员，平衡商业与使命。",
    "https://www.anthropic.com/news/google-broadcom-partnership-compute":
        "与 Google + Broadcom 签约，将部署多吉瓦级下一代 TPU 算力，2027 年上线。",
    "https://www.anthropic.com/news/australia-MOU":
        "澳大利亚政府与 Anthropic 签署谅解备忘录，开展 AI 安全研究合作，投入 300 万澳元。",
    "https://www.anthropic.com/news/enterprise-ai-services-company":
        "与 Blackstone、Hellman & Friedman、高盛联合成立企业 AI 服务公司，由 Anthropic 应用 AI 工程师和合作方工程团队为中型企业定制 Claude 方案并提供长期支持。",
    "https://www.anthropic.com/news/finance-agents":
        "发布 10 个金融服务 AI 代理模板，覆盖 Excel/PowerPoint/Word，新增多家数据合作伙伴连接器，帮助金融机构自动化交易、合规审查等关键业务流程。",
    "https://www.anthropic.com/news/anthropic-acquires-stainless":
        "Anthropic 收购 Stainless（多家 AI/云服务厂商官方 SDK 的自动生成平台），以加强其面向开发者的 SDK 与 API 工具链建设。",

    "https://www.darioamodei.com/essay/the-adolescence-of-technology":
        "提出 AI 处于「技术青春期」，面临自主性风险、滥用、权力夺取、失业四类威胁，需宪法训练、可解释性、监管、国际合作综合应对。",
    "https://www.darioamodei.com/essay/machines-of-loving-grace":
        "强大 AI 将在 5-10 年内压缩一个世纪的生物学进展，加速医学突破、消除疾病、延长寿命、促进民主减贫。",
    "https://www.darioamodei.com/post/the-urgency-of-interpretability":
        "AI 失控前必须优先做可解释性研究，理解模型内部机制以识别风险，需投资 + 透明化 + 出口管制配合。",
    "https://www.darioamodei.com/post/on-deepseek-and-export-controls":
        "芯片出口管制是美国保持 AI 领先的关键。DeepSeek 的成功不证明管制失效，反而需要更严格管制阻止中国获大规模算力。",

    "https://deepmind.google/blog/decoupled-diloco/":
        "发布 Decoupled DiLoCo，一种分布式 AI 训练新架构，通过解耦计算岛、异步数据流实现跨数据中心训练的韧性和低带宽。",
    "https://openai.com/index/gpt-5-5-system-card":
        "GPT-5.5 系统卡：模型架构、能力评估、Preparedness Framework 下的前沿风险评测与安全缓解措施汇总。",
    # Transformer Circuits
    "https://transformer-circuits.pub/2026/emotions/index.html":
        "在 Claude Sonnet 4.5 中找到情绪概念的内部表征，并通过干预实验证明这些表征会因果性地影响模型输出。",
    "https://transformer-circuits.pub/2026/headvis/index.html":
        "推出 HeadVis 交互工具，通过在完整数据分布上可视化注意力头的激活，帮助研究者解读 Claude Haiku 3.5 等模型中注意力头的行为；开源代码并提供 Gemma 3 与 Haiku 3.5 部分头的演示。",

    # Transformer Circuits backfill
    "https://transformer-circuits.pub/2025/november-update/index.html":
        "11 月简报：关于 harm pressure（有害压力）的简短更新。",
    "https://transformer-circuits.pub/2025/introspection/index.html":
        "证据显示语言模型能对自身内部状态进行内省。",
    "https://transformer-circuits.pub/2025/october-update/index.html":
        "10 月简报：关于视觉特征和字典初始化的小更新。",
    "https://transformer-circuits.pub/2025/linebreaks/index.html":
        "在一项基础语言模型行为的机制底层发现了几何结构。",
    "https://transformer-circuits.pub/2025/september-update/index.html":
        "9 月简报：关于特征和上下文学习的小更新。",
    "https://transformer-circuits.pub/2025/august-update/index.html":
        "8 月简报：人格设定如何改变助手的回答。",
    "https://transformer-circuits.pub/2025/faithfulness-toy-model/index.html":
        "当 transcoder 走偏时 — 一个机制（不）忠实性的玩具模型。",
    "https://transformer-circuits.pub/2025/attention-qk/index.html":
        "提出一种方法，用特征交互解释注意力模式，并将该信息整合进归因图。",
    "https://transformer-circuits.pub/2025/interference-weights/index.html":
        "更深入地解析「干扰权重」。",
    "https://transformer-circuits.pub/2025/bulk-update/index.html":
        "研究稀疏线性变换混合（MOLT），一种新型 transcoder 方法。",
    "https://transformer-circuits.pub/2025/july-update/index.html":
        "7 月简报：重访《数学框架》和把可解释性应用于生物学等小更新。",
    "https://transformer-circuits.pub/2025/april-update/index.html":
        "4 月简报：越狱、密集特征、可解释性入门等小更新。",
    "https://transformer-circuits.pub/2025/attention-update/index.html":
        "关于注意力机制研究进展的更新。",
    "https://transformer-circuits.pub/2025/crosscoder-diffing-update/index.html":
        "用 crosscoder 做模型差异化的初步笔记。",
    "https://transformer-circuits.pub/2025/january-update/index.html":
        "1 月简报：字典学习优化技术的小更新合集。",
    "https://transformer-circuits.pub/2024/model-diffing/index.html":
        "通过字典微调进行模型差异化的初步笔记。",
    "https://transformer-circuits.pub/2024/crosscoders/index.html":
        "提出一种获取跨层（甚至跨模型）一致特征的方法的初步笔记。",
    "https://transformer-circuits.pub/2024/features-as-classifiers/index.html":
        "比较基于特征 vs 基于原始激活的有害性分类器的初步笔记。",
    "https://transformer-circuits.pub/2024/september-update/index.html":
        "2024 年 9 月简报：研究 successor heads、SAE 中的数据过采样等小更新。",
    "https://transformer-circuits.pub/2024/august-update/index.html":
        "2024 年 8 月简报：可解释性评测、自解释复现等小更新。",
    "https://transformer-circuits.pub/2024/july-update/index.html":
        "2024 年 7 月简报：五大障碍、线性表征、暗物质、pivot tables、特征敏感性等。",
    "https://transformer-circuits.pub/2024/june-update/index.html":
        "2024 年 6 月简报：topk 和 gated SAE 的研究小更新。",
    "https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html":
        "用稀疏自编码器从 Claude 3 Sonnet 中提取大量可解释特征，其中部分与安全相关。",
    "https://transformer-circuits.pub/2024/april-update/index.html":
        "Anthropic 可解释性团队 2024 年 4 月小更新合集。",
    "https://transformer-circuits.pub/2024/march-update/index.html":
        "Anthropic 可解释性团队 2024 年 3 月小更新合集。",
    "https://transformer-circuits.pub/2024/qualitative-essay/index.html":
        "对可解释性研究中定性成分相比其他领域更为核心这一现象的思考。",
    "https://transformer-circuits.pub/2024/feb-update/index.html":
        "Anthropic 可解释性团队 2024 年 2 月小更新合集。",
    "https://transformer-circuits.pub/2024/jan-update/index.html":
        "Anthropic 可解释性团队 2024 年 1 月小更新合集。",
    "https://transformer-circuits.pub/2023/monosemantic-features/index.html":
        "用稀疏自编码器从单层 Transformer 中提取大量可解释特征 — 单义性研究里程碑。",
    "https://transformer-circuits.pub/2023/july-update/index.html":
        "Anthropic 可解释性团队 2023 年 7 月小更新合集。",
    "https://transformer-circuits.pub/2023/may-update/index.html":
        "Anthropic 可解释性团队 2023 年 5 月小更新合集。",
    "https://transformer-circuits.pub/2023/interpretability-dreams/index.html":
        "目前的研究旨在为机制可解释性奠定基础，过程中需要清楚地认识最终目标。",
    "https://transformer-circuits.pub/2023/superposition-composition/index.html":
        "非正式笔记：「分布式表征」可被理解为两种竞争策略 — 「组合」与「叠加」 — 二者性质迥异。",
    "https://transformer-circuits.pub/2023/privileged-basis/index.html":
        "理论上 Transformer 残差流的各坐标轴不应有特殊意义，但实践相反。研究表明 Adam 优化器的逐维归一化是元凶。",
    "https://transformer-circuits.pub/2023/toy-double-descent/index.html":
        "扩展玩具模型工作，阐明深度学习模型如何超出训练集泛化 — 一个长期未被机制性理解的核心问题。",
    "https://transformer-circuits.pub/2022/toy_model/index.html":
        "神经元常把多个无关概念塞进单个神经元（多义性）。本工作构建玩具模型，完整解释多义性的起源和动力学。",
    "https://transformer-circuits.pub/2022/solu/index.html":
        "提出一种替代激活函数，提高对应人类可理解概念的神经元比例。",
    "https://transformer-circuits.pub/2022/mech-interp-essay/index.html":
        "关于机制可解释性的直觉的非正式笔记 — 重点谈变量与可解释基的重要性。",
    "https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html":
        "探索「归纳头是上下文学习主要机制」的假设，并报告了此前未知的 Transformer 语言模型相变现象。",
    "https://transformer-circuits.pub/2021/framework/index.html":
        "早期的 Transformer 逆向工程数学框架，通过对小型玩具模型的逆向演示。",
    "https://transformer-circuits.pub/2021/exercises/index.html":
        "一组习题，用于提升对神经网络在参数层面实现算法的理解。",
    "https://transformer-circuits.pub/2021/videos/index.html":
        "在探索 Transformer 逆向工程方法过程中录制的非正式粗糙讲座。",
    "https://transformer-circuits.pub/2021/garcon/index.html":
        "对大模型可解释性研究工具链的描述。",

    # GitHub Trending — 2026-05-13
    "https://github.com/anonfaded/FadCam":
        "开源无广告 Android 多媒体录像工具，支持后台录制、屏幕录制、直播和远程摄像头控制。",
    "https://github.com/yikart/AiToEarn":
        "利用 AI 辅助赚钱的工具平台。",
    "https://github.com/millionco/react-doctor":
        "检测 AI agent 生成的劣质 React 代码的静态分析工具。",
    "https://github.com/tinyhumansai/openhuman":
        "私有、简洁、极为强大的个人 AI 超级智能平台。",
    "https://github.com/apernet/hysteria":
        "Hysteria — 基于 QUIC 协议的高速抗审查代理工具。",
    "https://github.com/mattpocock/skills":
        "Matt Pocock 面向真实工程师的 Claude 技能集，直接来自其 .claude 配置目录。",
    "https://github.com/rasbt/LLMs-from-scratch":
        "用 PyTorch 从零逐步实现类 ChatGPT 大语言模型的教程书配套代码。",

    # Hacker News Newest — 2026-05-13
    "https://news.ycombinator.com/item?id=48118988":
        "Show HN：Recursant — 基于 mesh 架构的 AI agent 控制平面。",
    "https://news.ycombinator.com/item?id=48118881":
        "汉坦病毒全球分布地图可视化。",
    "https://news.ycombinator.com/item?id=48118908":
        "Google AluminiumOS：面向桌面端重新设计的 Android 系统。",
    "https://news.ycombinator.com/item?id=48118816":
        "Tep：Sinatra 风格 Web 框架，通过 Spinel 编译为原生二进制。",
    "https://news.ycombinator.com/item?id=48119080":
        "GitHub Launchpad 功能提案：为开源项目提供内置启动平台的提案讨论。",
    "https://news.ycombinator.com/item?id=48119011":
        "Alien — 项目/工具介绍（标题缺上下文）。",
    "https://news.ycombinator.com/item?id=48118744":
        "MIT Technology Review《The Download》：一位诺贝尔奖得主谈 AI，以及「修复一切」的理由。",
    "https://news.ycombinator.com/item?id=48118932":
        "Codex 计算机使用功能的演示与讨论。",
    "https://news.ycombinator.com/item?id=48119091":
        "Satteri：面向 JavaScript 生态的高性能 Markdown/MDX 处理库。",
    "https://news.ycombinator.com/item?id=48118763":
        "欧洲政府网站安全审计：3000 个追踪站点、1000 个裸露 phpMyAdmin、99% 安全配置薄弱。",
    "https://news.ycombinator.com/item?id=48118783":
        "Show HN：用数据生成各国电网可视化海报的工具。",
    "https://news.ycombinator.com/item?id=48118855":
        "泄露 16 分钟视频揭示 Google Aluminium OS 详情。",
    "https://news.ycombinator.com/item?id=48119016":
        "用 Claude 将 Bun 移植到 Rust，再用 GPT 进行代码审查的实验记录。",
    "https://news.ycombinator.com/item?id=48118844":
        "HubSpot 在非洲市场推动 CRM 普及的经验分享（营销内容）。",
    "https://news.ycombinator.com/item?id=48119047":
        "《布谷鸟乐园》：Tom Burgis 著，讲述权力与影响力的滥用（2024）。",
    "https://news.ycombinator.com/item?id=48118876":
        "原本写给人类读者的文档，如今被作者自己当作 LLM 提示词使用的感想。",
    "https://news.ycombinator.com/item?id=48118904":
        "Urlsify.com — 免费 URL 缩短服务，附带深度流量分析功能。",
    "https://news.ycombinator.com/item?id=48118857":
        "Genera OS — 操作系统相关项目介绍。",
    "https://news.ycombinator.com/item?id=48119063":
        "OpenAI、微软等合作开发更高性能、可扩展的以太网网络方案。",
    "https://news.ycombinator.com/item?id=48118956":
        "Valve 在新版 Steam 手柄中隐藏了 Wilhelm 惨叫彩蛋（视频）。",
    "https://news.ycombinator.com/item?id=48118866":
        "厌倦免费二维码生成器的广告，作者自己做了一个无广告版本。",
    "https://news.ycombinator.com/item?id=48118749":
        "Freelang：编译器本身就是 JavaScript 的小型 AOT 语言。",
    "https://news.ycombinator.com/item?id=48118751":
        "巴西面向小型卫星市场的航天发射系统介绍。",
    "https://news.ycombinator.com/item?id=48119070":
        "无需互联网即可使用 FaceTime 通话的演示（视频）。",
    "https://news.ycombinator.com/item?id=48119000":
        "AllSkyKamera：面向全球夜空监测的公民科学摄像头网络。",
    "https://news.ycombinator.com/item?id=48118968":
        "OpenCL 3.1 规范正式发布。",
    "https://news.ycombinator.com/item?id=48119042":
        "谷歌基于 Android 的笔记本电脑将命名为 Googlebook，计划今年上市。",
    "https://news.ycombinator.com/item?id=48119023":
        "Hysteria：基于 QUIC 协议、专为抗审查设计的代理工具讨论。",
    "https://news.ycombinator.com/item?id=48118935":
        "陶哲轩演讲视频：AI 辅助的新型数学研究工作流。",
    "https://news.ycombinator.com/item?id=48119092":
        "Show HN：制作苹果商业广告风格演示录屏的应用。",

    # GitHub Trending — 2026-05-06
    "https://github.com/Hmbown/DeepSeek-TUI":
        "在终端里运行的 DeepSeek 模型编码 agent。",
    "https://github.com/addyosmani/agent-skills":
        "面向 AI 编码 agent 的生产级工程技能集合。",
    "https://github.com/PriorLabs/TabPFN":
        "TabPFN — 表格数据基础模型。",
    "https://github.com/docusealco/docuseal":
        "开源 DocuSign 替代品，支持创建、填写、签署电子文档。",
    "https://github.com/LearningCircuit/local-deep-research":
        "全本地加密的 deep research 工具，支持各种本地/云 LLM 与多种搜索引擎，SimpleQA 接近 95%。",
    "https://github.com/LadybirdBrowser/ladybird":
        "Ladybird — 不基于 Chromium/Gecko 的真正独立的开源浏览器。",
    "https://github.com/InsForge/InsForge":
        "为编码 agent 设计的 Postgres 后端，含鉴权、存储、计算、托管、AI 网关。",
    "https://github.com/virattt/dexter":
        "面向深度金融研究的自主 agent。",
    "https://github.com/anthropics/financial-services":
        "Anthropic 金融服务方案配套仓库。",
    "https://github.com/ruvnet/ruflo":
        "ruflo — Claude 多 agent 编排平台，支持自主工作流、RAG、Claude Code/Codex 原生集成。",
    "https://github.com/cheahjs/free-llm-api-resources":
        "免费 LLM API 推理资源清单。",
    "https://github.com/shiyu-coder/Kronos":
        "Kronos — 金融市场语言基础模型。",
    "https://github.com/bwya77/vscode-dark-islands":
        "灵感源自 easemate IDE 与 JetBrains Islands 主题的 VSCode 暗色主题。",
    "https://github.com/bytedance/deer-flow":
        "字节跳动开源的长任务 SuperAgent 框架，沙箱+记忆+工具+子 agent，处理分钟到小时级任务。",
    "https://github.com/D4Vinci/Scrapling":
        "自适应 Web 抓取框架，从单个请求到全量爬取均可适配。",

    # Hacker News Newest — 2026-05-06
    "https://news.ycombinator.com/item?id=48036468":
        "Show HN：HideMyData — 用本地 AI 与 OCR 在 macOS 上移除个人身份信息（PII）的工具。",
    "https://news.ycombinator.com/item?id=48036465":
        "讨论当前 PKI 体系是否已经迈入 self-sovereign（自主主权）阶段。",
    "https://news.ycombinator.com/item?id=48036463":
        "主要出版商以 AI 训练版权侵权为由起诉 Meta。",
    "https://news.ycombinator.com/item?id=48036458":
        "某数据库供应商出现故障，影响 Lovable 云用户。",
    "https://news.ycombinator.com/item?id=48036450":
        "视频解释为什么新电视让电影看起来「廉价感」（运动平滑等设置导致）。",
    "https://news.ycombinator.com/item?id=48036423":
        "印度 SMFG 退休人员贷款申请指南（看上去是营销/广告内容）。",
    "https://news.ycombinator.com/item?id=48036420":
        "南非在邮轮上识别出 Andes 株汉坦病毒。",
    "https://news.ycombinator.com/item?id=48036418":
        "在使用 nvm 切换 Node 版本后保证 npx 仍可用的小技巧。",
    "https://news.ycombinator.com/item?id=48036380":
        "Bun 发布 Rust 移植指南，承认 Rust 重写仍未完成。",
    "https://news.ycombinator.com/item?id=48036376":
        "UserTesting 出品（标题缺上下文，疑似产品/招聘宣传）。",
    "https://news.ycombinator.com/item?id=48036356":
        "关于随机领带打法的研究资料。",
    "https://news.ycombinator.com/item?id=48036345":
        "「植物细胞内部的数学之舞」— 介绍细胞内动力学的科普长文。",
    "https://news.ycombinator.com/item?id=48036342":
        "Show HN：MetaLens — 在 Metabase 之上构建的可观测性 + AI agents 平台。",
    "https://news.ycombinator.com/item?id=48036341":
        "Ask HN：非技术创始人申请 YC？",
    "https://news.ycombinator.com/item?id=48036330":
        "Show HN：Recursant — 用于治理 AI agents 的开源 mesh 平台。",
    "https://news.ycombinator.com/item?id=48036324":
        "AI 传输的「消息追加」工程实战：三个案例。",
    "https://news.ycombinator.com/item?id=48036323":
        "新研究发现：几乎所有植物肉替代品都含霉菌毒素。",
    "https://news.ycombinator.com/item?id=48036313":
        "微软《Work Trend Index》：agents、人的能动性，以及对每个组织的机遇。",
    "https://news.ycombinator.com/item?id=48036312":
        "极简、无浏览器边框的 macOS Web App 查看器。",
    "https://news.ycombinator.com/item?id=48036307":
        "容器 / 虚拟机管理工具 Incus 7.0 LTS 发布。",
    "https://news.ycombinator.com/item?id=48036295":
        "走近那些坚决不用生成式 AI 的学者。",
    "https://news.ycombinator.com/item?id=48036289":
        "男子在垃圾箱里捡到价值约 100 万美元的游戏王卡片。",
    "https://news.ycombinator.com/item?id=48036274":
        "面向 agentic coding 的开发环境介绍。",
    "https://news.ycombinator.com/item?id=48036272":
        "「Seeing typos makes me hapy」— 故意写错字，关于错字心理 / 编辑体验的玩笑标题。",
    "https://news.ycombinator.com/item?id=48036261":
        "把文本编辑器当作 UI 的实现细节探讨。",
    "https://news.ycombinator.com/item?id=48036257":
        "《Markov chain Monte Carlo 手册》第二版资源。",
    "https://news.ycombinator.com/item?id=48036249":
        "Linux 下的协作式 fiber 调度器。",
    "https://news.ycombinator.com/item?id=48036241":
        "「老问题：又是 DNS」— 德国 .de 域名运营商 Denic 致歉，DNS 故障导致德国互联网瘫痪。",
    "https://news.ycombinator.com/item?id=48036238":
        "Firefox 集成了广告拦截器 — 但用途并非拦广告（推测是为隐私分析）。",
    "https://news.ycombinator.com/item?id=48036229":
        "Purista 出品的 TypeScript AI harness 框架。",

    # 2026-05-09 — Anthropic / Transformer Circuits
    "https://www.anthropic.com/news/higher-limits-spacex":
        "与 SpaceX 达成新算力合作大幅扩容，借此提高 Claude Code 与 Claude API 的使用配额。",
    "https://transformer-circuits.pub/2026/nla/index.html":
        "提出「自然语言自编码器」(NLA)，用 LLM 自身把激活值压缩成自然语言再解码，从而对模型激活提供无监督、可读的解释。",

    # 2026-05-09 — GitHub Trending
    "https://github.com/playcanvas/supersplat":
        "PlayCanvas 出品的 3D 高斯泼溅 (Gaussian Splat) 编辑器。",
    "https://github.com/oracle-devrel/oracle-ai-developer-hub":
        "Oracle 官方资源库：用 Oracle AI Database 与 OCI 服务构建 AI 应用、agent 和系统的技术资料合集。",
    "https://github.com/datawhalechina/hello-agents":
        "Datawhale 中文教程《从零开始构建智能体》— 智能体原理与实践入门。",
    "https://github.com/rohitg00/agentmemory":
        "号称基于真实基准的 AI 编码 agent 持久化记忆方案。",
    "https://github.com/ChromeDevTools/chrome-devtools-mcp":
        "把 Chrome DevTools 暴露给编码 agent 的官方 MCP server。",
    "https://github.com/decolua/9router":
        "免费 AI 编码路由：让 Claude Code / Codex / Cursor / Cline / Copilot / Antigravity 接入 40+ 提供商的免费 Claude / GPT / Gemini，自动 fallback，号称省 40% token、不再撞限额。",
    "https://github.com/datawhalechina/easy-vibe":
        "Datawhale 出品的 vibe coding 2026 入门课程，面向编程新手循序渐进掌握现代编程。",
    "https://github.com/masterking32/MasterDnsVPN":
        "高级 DNS 隧道翻墙工具，相比 DNSTT/SlipStream 优化了低开销 ARQ、解析器负载均衡、抗丢包稳定性和速度。",
    "https://github.com/Lordog/dive-into-llms":
        "中文系列教程《动手学大模型》— 大模型编程实践。",
    "https://github.com/rowboatlabs/rowboat":
        "开源带记忆的 AI 协作伙伴 (coworker)。",
    "https://github.com/bytedance/UI-TARS-desktop":
        "字节出品的开源多模态 AI agent 栈：连接前沿 AI 模型与 agent 基础设施。",

    # 2026-05-10 — GitHub Trending
    "https://github.com/HKUDS/AI-Trader":
        "港大数据智能实验室出品的 100% 全自动 agent 原生交易系统。",
    "https://github.com/lsdefine/GenericAgent":
        "自演化 agent：从 3.3K 行种子起步，自行生长技能树，实现完整系统控制并节省 6 倍 token 消耗。",
    "https://github.com/CloakHQ/CloakBrowser":
        "隐身 Chromium，宣称通过所有 bot 检测；可直接替换 Playwright，源代码层做指纹补丁，30/30 测试通过。",
    "https://github.com/affaan-m/everything-claude-code":
        "面向 Claude Code / Codex / Cursor 等 agent harness 的性能优化系统：技能、直觉、记忆、安全与研究优先开发。",
    "https://github.com/jundot/omlx":
        "Apple Silicon 上的 LLM 推理服务器：连续批处理 + SSD 缓存，从 macOS 菜单栏管理。",

    # 2026-05-10 — Hacker News Newest
    "https://news.ycombinator.com/item?id=48083813":
        "科普：科学家观测到可能促成地球复杂生命起源的「首次接触」事件。",
    "https://news.ycombinator.com/item?id=48084086":
        "Ask HN：当前的软件工程工作流是否就是未来的常态？",
    "https://news.ycombinator.com/item?id=48083911":
        "Retainer：可长时间独立运行的自主 agent。",
    "https://news.ycombinator.com/item?id=48083968":
        "AI 时代下低保真 (LoFi) 信号在产品/设计中的角色变迁。",
    "https://news.ycombinator.com/item?id=48083814":
        "BLAS、LAPACK 与 OpenMP 之间的关系与使用要点。",
    "https://news.ycombinator.com/item?id=48083773":
        "评论文章：键盘输入正在被语音「耳语」替代，但作者认为这更让人烦。",
    "https://news.ycombinator.com/item?id=48083919":
        "面向 Claude Code 的学术研究技能集合 (Skills)。",
    "https://news.ycombinator.com/item?id=48083877":
        "Show HN：基于 Plasmo 的 X/Twitter 视频下载 Chrome 扩展。",
    "https://news.ycombinator.com/item?id=48084080":
        "Marstek B2500-D 储能电池被发现用明文 HTTP 上报遥测数据。",
    "https://news.ycombinator.com/item?id=48083832":
        "NeuroFilter：用 transformers.js 在 MV3 扩展里做 YouTube 推荐过滤。",
    "https://news.ycombinator.com/item?id=48083876":
        "警示：量子计算进展正在压缩网络（PQC）升级的时间表。",
    "https://news.ycombinator.com/item?id=48084063":
        "War.gov UFO 文件 55,256 张幻灯片全部可搜索、可链接。",
    "https://news.ycombinator.com/item?id=48083887":
        "Telbex 内核 0.2 版即将发布。",
    "https://news.ycombinator.com/item?id=48084056":
        "用于搭建 1990 年代 Geocities 风格网站的脚手架模板。",
    "https://news.ycombinator.com/item?id=48084029":
        "如何把电子表格当作创意工具使用。",
    "https://news.ycombinator.com/item?id=48083969":
        "Cyber.md：用「agent 可读」格式描述安全态势的 AI 原生方案。",
    "https://news.ycombinator.com/item?id=48083944":
        "IPic — 火柴头大小的 Web 服务器。",
    "https://news.ycombinator.com/item?id=48083997":
        "重读《赛博空间独立宣言》(A Declaration of the Independence of Cyberspace)。",
    "https://news.ycombinator.com/item?id=48084000":
        "Go 社区 txtar 归档格式的入门导览。",
    "https://news.ycombinator.com/item?id=48083803":
        "在 24GB 内存的 M4 Mac 上运行本地大模型的实操经验。",
    "https://news.ycombinator.com/item?id=48083783":
        "ModelDocker：OpenRouter 桌面客户端，方便统一调用各家 LLM。",
    "https://news.ycombinator.com/item?id=48084012":
        "随笔《离开物理世界》— 关于线上化生活的反思。",
    "https://news.ycombinator.com/item?id=48083836":
        "「Six Seven Six Seven」— 标题缺乏上下文，疑似梗/小项目。",
    "https://news.ycombinator.com/item?id=48083816":
        "用户反馈：取消 Claude 订阅续费后立即被吊销 Claude Design 使用权。",
    "https://news.ycombinator.com/item?id=48083792":
        "1975 年 UCI LISP 的随笔札记。",
    "https://news.ycombinator.com/item?id=48083890":
        "Pomotuimer — 终端用、零依赖的番茄钟工具。",
    "https://news.ycombinator.com/item?id=48084031":
        "重读《赛博空间里有没有「那里」?》— 早期互联网身份/场所感讨论。",
    "https://news.ycombinator.com/item?id=48083845":
        "2026 年迄今已有 92,000+ 名科技从业者被裁员。",
    "https://news.ycombinator.com/item?id=48084008":
        "回顾 1999 年火星气候探测器为何因单位换算错误偏离轨道。",
    "https://news.ycombinator.com/item?id=48083933":
        "苹果第三位创始人 Ronald G. Wayne 在 Apple 的两周时间始末。",

    # 2026-05-15 抓取批次
    "https://news.ycombinator.com/item?id=48146286":
        "Show HN：开源 Codex Pet Home 软件项目。",
    "https://news.ycombinator.com/item?id=48145736":
        "对新版 Raycast 的技术深度剖析。",
    "https://github.com/roboflow/supervision":
        "Roboflow 出品的可复用计算机视觉工具集合（标注、追踪、可视化）。",
    "https://news.ycombinator.com/item?id=48145787":
        "Ask HN：后端开发者如何用 AI 设计 UI。",
    "https://news.ycombinator.com/item?id=48146062":
        "纪录片：《Modern Warfare 3》混乱开发史。",
    "https://news.ycombinator.com/item?id=48145841":
        "Rosetta Check 2.0 扫描 Pro Tools / Logic / Photoshop 插件中残留的 Intel 架构构建。",
    "https://news.ycombinator.com/item?id=48146185":
        "讨论公共部门中 AI、开源代码与漏洞风险。",
    "https://news.ycombinator.com/item?id=48146158":
        "IEA 报告：到 2030 年 AI 数据中心用电量可能接近翻倍。",
    "https://news.ycombinator.com/item?id=48146129":
        "把维基百科以 Windows XP 桌面风格浏览的趣味项目。",
    "https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization":
        "NVIDIA 出品的视频搜索 & 摘要参考架构集合，用于构建 GPU 加速的视觉 agent 与视频分析应用。",
    "https://news.ycombinator.com/item?id=48146184":
        "Crypto-Gram 本月 1/4 文章都在讨论 Mythos。",
    "https://news.ycombinator.com/item?id=48145722":
        "「2028 全球 AI 领导力」的两种推演场景。",
    "https://github.com/ruvnet/RuView":
        "RuView：把普通 WiFi 信号变成实时空间感知、生命体征监测和存在检测（无需摄像头）。",
    "https://news.ycombinator.com/item?id=48145913":
        "Ed Zitron 揭露 Anthropic 在法庭披露估值 50 亿，对外却称 190 亿。",
    "https://news.ycombinator.com/item?id=48146207":
        "重复数据检测与修复实践分享。",
    "https://news.ycombinator.com/item?id=48145734":
        "VI65：面向 6502 CPU 的 vi 文本编辑器移植。",
    "https://news.ycombinator.com/item?id=48145922":
        "Kog AI 视频分享：在 AMD Instinct GPU 上构建实时推理栈。",
    "https://github.com/obra/superpowers":
        "Superpowers：一套 agentic skills 框架与软件开发方法论。",
    "https://news.ycombinator.com/item?id=48146097":
        "Andy Jassy 正在为 AI 时代重写亚马逊的经营手册。",
    "https://github.com/Genymobile/scrcpy":
        "scrcpy：通过电脑显示并控制 Android 设备的开源工具。",
    "https://news.ycombinator.com/item?id=48146039":
        "Show HN：借鉴 TikTok 的方法提升会议专注度的小工具。",
    "https://github.com/K-Dense-AI/scientific-agent-skills":
        "面向科研、工程、分析、金融与写作的现成 Agent Skills 合集。",
    "https://news.ycombinator.com/item?id=48146012":
        "保证金交易与证券借贷策略的回测分享。",
    "https://github.com/garrytan/gstack":
        "garrytan/gstack：Garry Tan 的 Claude Code 设置——23 个开箱即用工具，分别扮演 CEO、设计、工程经理、发布、文档、QA 角色。",
    "https://news.ycombinator.com/item?id=48146104":
        "工业测量标准参考温度的简短历史。",
    "https://news.ycombinator.com/item?id=48146073":
        "OpenAI 正考虑就「关系紧张」的 Siri 合作起诉 Apple。",
    "https://news.ycombinator.com/item?id=48145852":
        "研究：被过度劳累的 AI agent 会「转向马克思主义」式表达。",
    "https://news.ycombinator.com/item?id=48146007":
        "Food 4 Agile Thought #544：知识工作工具、买入陷阱、agentic 编码 ROI。",
    "https://news.ycombinator.com/item?id=48146220":
        "HN 上一篇标题为「Something Else」的杂谈。",
    "https://github.com/supertone-inc/supertonic":
        "Supertonic：基于 ONNX 在本地设备运行的多语言闪电 TTS。",
    "https://github.com/github/spec-kit":
        "GitHub 官方 Spec-Driven Development 入门工具包。",
    "https://news.ycombinator.com/item?id=48145951":
        "研究：美国家庭烧木柴正在让铅中毒卷土重来。",
    "https://news.ycombinator.com/item?id=48145970":
        "Ask HN：如何写 Elixir 测试。",
    "https://github.com/influxdata/telegraf":
        "InfluxData Telegraf：采集、处理、聚合和写入指标、日志等数据的 agent。",
    "https://news.ycombinator.com/item?id=48145995":
        "前端排版技巧：用 tabular-nums 让数字垂直对齐。",
    "https://news.ycombinator.com/item?id=48146242":
        "as-of join（按时间最近匹配）查询的扩展性优化。",
    "https://news.ycombinator.com/item?id=48146279":
        "LLM 时序与因果推理的研究综述。",
    "https://news.ycombinator.com/item?id=48146059":
        "GitHub Actions 出现可用性降级告警。",
    "https://news.ycombinator.com/item?id=48145622":
        "提升领域特定语言（DSL）表现力的设计实践。",
    "https://news.ycombinator.com/item?id=48146274":
        "披露一个新的 Linux 内核漏洞「fragnesia」。",

    # 2026-05-17 社区动态
    "https://news.ycombinator.com/item?id=48166675":
        "报道：美国正在用 AI 在 Polymarket 上追查内幕交易。",
    "https://news.ycombinator.com/item?id=48166607":
        "Abseil — Google 开源的 C++ 通用基础库。",
    "https://news.ycombinator.com/item?id=48166538":
        "Show HN：KoalaNews — 用 AI 衡量一条新闻在大趋势下的相对重要性。",
    "https://github.com/oven-sh/bun":
        "Bun — 极快的 JavaScript 运行时、打包器、测试运行器与包管理器一体化工具。",
    "https://news.ycombinator.com/item?id=48166585":
        "AI Playground — 为 AI agent 提供安全的隔离游乐场。",
    "https://news.ycombinator.com/item?id=48166893":
        "用 CSS 给配色做对比度防护，确保前景/背景文字始终可读。",
    "https://github.com/Anil-matcha/Open-Generative-AI":
        "Open-Generative-AI — 开源的 AI 图像 / 视频生成 studio，集成 Flux、Midjourney、Kling、Sora、Veo 等 200+ 模型，自托管、MIT 许可、无内容过滤。",
    "https://news.ycombinator.com/item?id=48166812":
        "报道：军队狙击手的工作正在被无人机取代。",
    "https://news.ycombinator.com/item?id=48166766":
        "Show HN：PathFinder — 映射通往目标的所有路径，再分步执行。",
    "https://news.ycombinator.com/item?id=48166870":
        "作者做了一个假的 Phantom 钱包生成器（钓鱼/演示用途）。",
    "https://news.ycombinator.com/item?id=48166686":
        "文章：Palantir「SaaS 已死」的论断是给创业者的警钟。",
    "https://news.ycombinator.com/item?id=48166774":
        "视频：Anthropic 刚承认 AI 是「bullshit」（标题语，HN 讨论 Anthropic 关于 LLM 幻觉性质的表态）。",
    "https://news.ycombinator.com/item?id=48166905":
        "UWB 移动 Suica 不止是免触闸机过闸，还能用于支付。",
    "https://news.ycombinator.com/item?id=48166560":
        "PyCon US 2026 Packaging Summit 回顾。",
    "https://news.ycombinator.com/item?id=48166653":
        "视频：古英语发音的全面重构。",
    "https://news.ycombinator.com/item?id=48166868":
        "Neptune — 为 QEMU 提供 Direct3D 虚拟化。",
    "https://news.ycombinator.com/item?id=48166770":
        "工具/项目：隐私政策变更日志（追踪各家隐私政策的版本差异）。",
    "https://news.ycombinator.com/item?id=48166778":
        "视频：与专家 Daniel Lemire 聊 SIMD、缓存与 CPU 内部机制。",
    "https://news.ycombinator.com/item?id=48166832":
        "随笔：领域知识才是真正的杠杆。",
    "https://news.ycombinator.com/item?id=48166825":
        "招聘：Presight.ai 的 Project Prism 全栈工程师，阿布扎比现场全职。",
    "https://news.ycombinator.com/item?id=48166903":
        "ConnectAI — LinkedIn 私信生成器。",
    "https://news.ycombinator.com/item?id=48166634":
        "Team-memory — 团队共享大脑，由 Claude Code CLI 或 UI 自动构建。",
    "https://news.ycombinator.com/item?id=48166837":
        "2ality 博客暂时下线，原因是「AI 在窃取内容」。",
    "https://news.ycombinator.com/item?id=48166859":
        "从原始日志到可编程的 EVM 执行情报。",
    "https://news.ycombinator.com/item?id=48166664":
        "游戏：《英雄无敌：旧时代（Heroes of Might and Magic: Olden Era）》。",
    "https://news.ycombinator.com/item?id=48166906":
        "Patrick Collison 写底特律印象记。",
    "https://news.ycombinator.com/item?id=48166856":
        "kharp — 用 C# 实现的 K 语言（v3）解释器。",
    "https://news.ycombinator.com/item?id=48166701":
        "Musk vs. Altman 第 3 周：马斯克与奥特曼互相隔空开炮。",
    "https://news.ycombinator.com/item?id=48166786":
        "一项便宜的修复：每年帮 AI 省 4 亿美元，并让 40 亿人接入互联网。",
    "https://news.ycombinator.com/item?id=48166599":
        "面向小白的 Gaussian Splatting 入门讲解。",
    "https://news.ycombinator.com/item?id=48166877":
        "评论文：法西斯主义的十大信号，美国全部具备。",
    "https://news.ycombinator.com/item?id=48166875":
        "ProPublica 报道：FDA 不会告诉你的药品真相（文字稿）。",
    "https://github.com/colbymchenry/codegraph":
        "codegraph — 面向 Claude Code 的预索引代码知识图谱，减少 token 与工具调用次数，100% 本地。",

    # 05-20 batch — Anthropic
    "https://www.anthropic.com/news/anthropic-kpmg":
        "与 KPMG（毕马威）达成战略联盟，将 Claude 集成到其核心业务和超 27.6 万名员工的工作流中。",
    "https://www.anthropic.com/news/widening-conversation-ai":
        "拓展前沿 AI 的公共对话：邀请更多利益相关方加入 Anthropic 关于 AI 风险与治理的讨论。",

    # 05-20 batch — GitHub Trending
    "https://github.com/can1357/oh-my-pi":
        "终端 AI 编码 agent，号称用 hash 锚定的编辑机制、优化的工具调用框架，原生支持 LSP、Python、浏览器和 subagent。",
    "https://github.com/anthropics/claude-plugins-official":
        "Anthropic 官方维护的 Claude Code 高质量插件目录。",
    "https://github.com/Imbad0202/academic-research-skills":
        "为 Claude Code 准备的学术研究技能合集：research → write → review → revise → finalize 覆盖论文全流程。",
    "https://github.com/multica-ai/andrej-karpathy-skills":
        "一个 CLAUDE.md 文件，把 Karpathy 关于 LLM 编码常见陷阱的观察提炼成 Claude Code 的行为指导。",
    "https://github.com/HKUDS/ViMax":
        "港大 ViMax：导演、编剧、制片、视频生成器多智能体协作完成视频创作的 agentic 视频生成框架。",
    "https://github.com/HKUDS/CLI-Anything":
        "港大 CLI-Anything：把任何软件变成 agent 原生 CLI 工具的项目，配套 CLI-Hub (clianything.cc)。",

    # 05-21 batch — YouTube AI
    "https://www.youtube.com/watch?v=OMhKgQmeMhI":
        "The Verge 把 Google I/O 2026 keynote 浓缩成 35 分钟版本。",
    "https://www.youtube.com/watch?v=qCfARlv74jQ":
        "CNET 用 13 分钟回顾 Google I/O 2026 所有发布。",
    "https://www.youtube.com/watch?v=wZr5rBdczZc":
        "9to5Google：Gemini 史上最大更新（Gemini Omni、3.5 Flash、Antigravity 等）综述。",
    "https://www.youtube.com/watch?v=KsnXvqSbDLU":
        "Edwin H. 用 9 分钟（中文/粤语）讲解 Google I/O 发布会 + Android 17 精华。",
    "https://www.youtube.com/watch?v=IrA0mzZTwLo":
        "Paul J Lipsky 测评 Gemini Omni — Google 新视频生成模型，演示其表现。",

    # 05-21 batch — Hacker News Newest
    "https://news.ycombinator.com/item?id=48210142":
        "讨论 Anthropic Mythos 模型被夸大的「无管制黑客」担忧——围绕 Anthropic 新模型的安全风险被媒体放大。",
    "https://news.ycombinator.com/item?id=48210246":
        "Granta 杂志获奖小说疑似为 AI 撰写——文学界开始遭遇生成式写作渗透。",
    "https://news.ycombinator.com/item?id=48210239":
        "讨论应如何在写作中政策性管控 AI 使用。",
    "https://news.ycombinator.com/item?id=48210250":
        "讨论面向 vector-length-agnostic ML 代码生成的可扩展 packed layouts 方案。",
    "https://news.ycombinator.com/item?id=48210226":
        "OpenAI 准备提交 IPO 申请——AI 行业最受瞩目的上市进程。",
    "https://news.ycombinator.com/item?id=48210279":
        "Show HN：Homecrew——团队共享并同步 agent skills 的工具。",
    "https://news.ycombinator.com/item?id=48210092":
        "讨论 OpenAI 政治游说战略的下一步。",
    "https://news.ycombinator.com/item?id=48210117":
        "Meta 计划裁员 10%（约 8000 人）以提升 AI 效率。",
    "https://news.ycombinator.com/item?id=48210173":
        "Google 即将发布自 Google Glass 失败以来的首款智能眼镜。",
    "https://news.ycombinator.com/item?id=48210308":
        "Cohere 发布 Command A+：把主权级 agentic 能力开放给更多用户。",
    "https://news.ycombinator.com/item?id=48210174":
        "讨论 AI 对音乐产业未来的影响。",
    "https://news.ycombinator.com/item?id=48210335":
        "论文：sycophantic（讨好型）AI 降低人的亲社会动机并促进依赖（2025）。",

    # 05-20 batch — Hacker News Newest
    "https://news.ycombinator.com/item?id=48209023":
        "介绍 Microsoft Agent 365：面向 2026 年企业治理的自主 AI agent 平台。",
    "https://news.ycombinator.com/item?id=48209323":
        "讨论给 AI 编码循环加上「形式化验证门」——用形式化方法约束生成代码必须通过的属性，防止 agent 自由发挥引入 bug。",
    "https://news.ycombinator.com/item?id=48209181":
        "Show HN：发布 Google Search Console MCP server，只读、OAuth 授权、免费开放。",
    "https://news.ycombinator.com/item?id=48209259":
        "用 350 次跑、17 个模型的 benchmark 评测主流 AI 编码 agent 在分布式 SQL 任务上的表现。",
    "https://news.ycombinator.com/item?id=48209045":
        "复盘一次失败 prompt：在真正 prompt 之前就烧掉 389K Claude Code 缓存创建 token 的踩坑过程。",
    "https://news.ycombinator.com/item?id=48209242":
        "HN 围绕 Google DeepMind 新发布的 Co-Scientist 多智能体科研助手的讨论。",
    "https://news.ycombinator.com/item?id=48209184":
        "训练一个 22MB 的轻量 prompt injection 分类器，证明端侧/小模型在防御 prompt injection 上足够实用。",
    "https://news.ycombinator.com/item?id=48224615":
        "Apple 公布 App Store 风控成绩：去年拦截了数十亿美元的欺诈交易和大批刷分/伪冒 App。",
    "https://news.ycombinator.com/item?id=48224616":
        "Show HN：Buildby，一个 CLI 工具，用来识别桌面应用是用什么框架/技术栈（Electron/Tauri/原生等）打包的。",
    "https://news.ycombinator.com/item?id=48224623":
        "作者复盘多年自研论坛软件的踩坑：协作建模、垃圾治理、性能权衡，反思论坛形态在 AI 时代还剩什么价值。",
    "https://news.ycombinator.com/item?id=48224630":
        "网络安全事件：AS202734 于 5/16–17 通过 BGP 劫持劫走多家中国电信运营商的部分流量，社区披露技术细节。",
    "https://news.ycombinator.com/item?id=48224638":
        "Show HN：GitVitae，基于 GitHub Profile 的免费托管简历/作品集生成器，一键拿到个人作品展示页。",
    "https://www.youtube.com/watch?v=6DB7wFVaebs":
        "（误命中：Gemini 关键词捞到 GMMTV 泰剧主题曲 MV，演唱者艺名为 Gemini/Fourth，与 Google Gemini 无关。）",

    # 05-24 batch — YouTube AI
    "https://www.youtube.com/watch?v=n5-RNSKz0sc":
        "Peter Diamandis Moonshots EP #257：讨论 SpaceX 750 亿美元 IPO 及与 Anthropic/OpenAI 的关联、OpenAI 用 AI 推翻一道 80 年悬而未决的 Erdős 数学猜想、GPT-5.5 在 Polymarket 预测准确度上击败市场。",
    "https://www.youtube.com/watch?v=ib74sLgjIBM":
        "在 Claude CoWork 里用 45 分钟从零复刻 Karpathy 的 AI 知识库系统：三文件夹 + 一份 CLAUDE.md 架构，配套五步框架和每月健康检查的 Claude Skill。",
    "https://www.youtube.com/watch?v=7sOSkZImZ4E":
        "（误命中：Gemini 关键词捞到印地语占星视频，讲木星进入双子座对未来 5 个月双子座运势的影响，与 Google Gemini 无关。）",
    "https://www.youtube.com/watch?v=RHV8DWAmjAs":
        "解读 Emergence AI 的 Claude AI Town 15 天实验：所谓「AI 镇民暴走/恋爱/烧城」叙事被夸大，真正可借鉴的是长期运行 agent 的上下文漂移和「全票通过」式 sycophancy 风险。",
    "https://www.youtube.com/watch?v=RjFFSNYqwQA":
        "西班牙语免费课程：教你用 Claude 选 YouTube 利基、确定内容方向、做 packaging、AI 生成内容，最终把频道变现的全流程。",

    # 05-24 batch — GitHub Trending
    "https://github.com/earendil-works/pi":
        "一站式 AI agent 工具包：编码 agent CLI、统一 LLM API、TUI/Web UI 库、Slack bot 以及 vLLM pods 模板。",
    "https://github.com/anthropics/knowledge-work-plugins":
        "Anthropic 官方开源仓库，面向 Claude Cowork 中知识工作者使用的插件集合。",
    "https://github.com/mukul975/Anthropic-Cybersecurity-Skills":
        "754 个结构化网络安全 skill，对应 MITRE ATT&CK / NIST CSF 2.0 / MITRE ATLAS / D3FEND / NIST AI RMF 五个框架，覆盖 26 个安全领域，适配 Claude Code、Copilot、Cursor 等 20+ AI 编码平台。",
    "https://github.com/Alishahryar1/free-claude-code":
        "在终端、VSCode 扩展或类 Discord 客户端 OpenClaw 中免费使用 claude-code 的工具，支持语音输入。",
    "https://github.com/manaflow-ai/cmux":
        "基于 Ghostty 的 macOS 终端，主打垂直标签和通知，专为 AI 编码 agent 多会话工作流设计。",
    "https://github.com/codecrafters-io/build-your-own-x":
        "经典学习仓库：通过从零复刻 Git/数据库/Docker 等著名技术，掌握底层实现原理。",
    "https://github.com/666ghj/MiroFish":
        "简洁通用的群体智能（Swarm Intelligence）引擎，号称可预测「万物」，开箱即用。",
    "https://github.com/blakeblackshear/frigate":
        "Frigate：面向 IP 摄像头的本地 NVR，内置实时目标检测能力。",

    # 05-24 batch — Hacker News Newest
    "https://news.ycombinator.com/item?id=48256670":
        "从天主教神学视角审视 AI 辩论，提出「整合智能」（Integral Intelligence）的人本主义立场。",
    "https://news.ycombinator.com/item?id=48256774":
        "作者怀念 Windows 上的 NETworkManager，干脆自己写了一个 Linux 版本。",
    "https://news.ycombinator.com/item?id=48256749":
        "厂商博文「Our AI just got better」式宣传被 HN 拿出来讨论营销话术。",
    "https://news.ycombinator.com/item?id=48256725":
        "并行计算成本模型 PDF：从 Work、Span、Parallelism 三个维度分析算法的并行潜力。",
    "https://news.ycombinator.com/item?id=48256791":
        "讨论：线下技术 meetup 是否已死，远程办公 + AI 时代下还有没有必要重建本地社群。",
    "https://news.ycombinator.com/item?id=48256912":
        "Constraint Decay：分析 LLM agent 在后端代码生成长任务中约束遵守逐步衰减的脆弱性。",
    "https://news.ycombinator.com/item?id=48256736":
        "Gustafson 定律：Amdahl 定律的反面解读，强调问题规模随处理器增加而扩张的并行收益。",
    "https://news.ycombinator.com/item?id=48256733":
        "趣文：波兰人依旧坚持用拉丁字符打印，因为字符编码踩坑史。",
    "https://news.ycombinator.com/item?id=48256924":
        "Russell 悖论视频科普，配合 HN 上对集合论与自指的讨论。",
    "https://news.ycombinator.com/item?id=48256703":
        "2009 年论文重温：多核应用中潜在的 determinacy-race（确定性竞争）bug 检测方法。",
    "https://news.ycombinator.com/item?id=48256714":
        "脑成像研究：手写比打字能激活更广泛的脑区连接，对学习与记忆更有利。",
    "https://news.ycombinator.com/item?id=48256767":
        "Show HN：作者自制一个免费 AI 欧洲穷游行程规划器。",
    "https://news.ycombinator.com/item?id=48256720":
        "神经科学综述：从脑机制角度比较手写与打字，呼应近年「键盘是否伤记忆」的讨论。",
    "https://news.ycombinator.com/item?id=48256798":
        "新闻：托运行李里持续充电的充电宝迫使 easyJet 航班改道。",
    "https://news.ycombinator.com/item?id=48256696":
        "土耳其 Bilgi 大学办学许可被撤，引发学术自由讨论。",
    "https://news.ycombinator.com/item?id=48256800":
        "LLM 时代构建和扩展 RL 训练环境的实操指南：环境工程是新一代 post-training 的关键瓶颈。",
    "https://news.ycombinator.com/item?id=48256816":
        "Rust 文章：你的 Clippy 配置应该更严格——推荐打开更多 lint 规则提升代码质量。",
    "https://news.ycombinator.com/item?id=48256758":
        "macOS 内置的可脚本化图像处理工具 sips 介绍，命令行批处理利器。",
    "https://news.ycombinator.com/item?id=48256847":
        "Show HN：Alyx，把加密货币组合 dashboard 显示在浏览器新标签页的扩展。",
    "https://news.ycombinator.com/item?id=48256799":
        "PromptVC：用 prompt 生成 VC 投资材料/分析的工具项目。",
    "https://news.ycombinator.com/item?id=48256710":
        "Show HN：个人 agent，能根据用户需求自动生成调用所需的工具（auto-tool）。",
    "https://news.ycombinator.com/item?id=48256630":
        "文章：印度即时配送让你在家点牛奶比泡杯咖啡还快，引发对配送经济与人力剥削的讨论。",
    "https://news.ycombinator.com/item?id=48256765":
        "讨论 JavaFX 的无障碍（Accessibility）现状与改进方向。",
    "https://news.ycombinator.com/item?id=48256642":
        "媒体观察：Z 世代对「真相」的全新理解（多源/语境化/平台化），与传统新闻业的事实观差异。",
    "https://news.ycombinator.com/item?id=48256617":
        "Show HN：一个安静、低干扰的团队思考与推进想法的协作空间产品。",
    "https://news.ycombinator.com/item?id=48256796":
        "新闻：AI 推翻了某个长期被数学界默认成立的猜想（呼应本日 Diamandis 视频中的 Erdős 议题）。",
    "https://news.ycombinator.com/item?id=48256882":
        "Show HN：一个可双向匹配的选型工具，根据本地 LLM 推荐硬件，或根据硬件推荐能跑的本地 LLM。",
    "https://news.ycombinator.com/item?id=48256666":
        "Show HN：Hookwarden，跨 JS/TS/Python/PHP 的 npx 工具，自动找出并修复 webhook HMAC 验签的常见 bug。",
    "https://news.ycombinator.com/item?id=48256919":
        "故事：男子用 27 年坚持环球徒步，「他拒绝放弃」。",
    "https://news.ycombinator.com/item?id=48256654":
        "讨论 Google《Software Engineering at Google》这本书在 2026 年仍然适用的部分与已经过时的部分。",

    # 05-25 batch — YouTube AI
    "https://www.youtube.com/watch?v=DGw2KKyXuYQ":
        "Wes Roth 解读 Andrej Karpathy 加入 Anthropic 的「真正原因」，串讲 OpenAI、Google、Anthropic、NVIDIA 与开源 AI 最新动向。",
    "https://www.youtube.com/watch?v=ikWmASLeCYU":
        "教学视频：如何使用 Google Gemini Omni 新一代 AI 视频生成模型——支持文本 + 人脸/语音参考 + 上传图片/视频的多模态输入生成「电影感」视频。",
    "https://www.youtube.com/watch?v=rmXvS69ELvc":
        "WorldofAI 整理本周 AI 新闻：Claude Mythos 1 Preview 已现身、Claude Sonnet 4.8 和 Opus 4.8 模型 slug 被泄露，Anthropic 似在为 Claude Code 与 Claude Security 准备重大升级；附带 GPT-5.6、DeepSeek v4 Pro 线索。",
    "https://www.youtube.com/watch?v=Qj4-i58sAZ8":
        "日语「紧急解读」：2026-06-15 起 Claude 付费方案重大改动，「对话」与「自动化」两类用量将彻底分离计费，提醒老用户检查自己的使用方式。",
    "https://www.youtube.com/watch?v=UvUzpSlXKtg":
        "Theo (t3.gg) 评测 Cursor 新发布的 Composer 2.5 模型，认为其在 agentic 编码体验上明显胜过 Claude Code。",

    # 05-25 batch — Hacker News Newest
    "https://news.ycombinator.com/item?id=48262160":
        "评 Lua 语言生态的「绿色一面」：嵌入式友好、轻量、可塑性高。",
    "https://news.ycombinator.com/item?id=48262142":
        "Show HN：JavaScript Crossword，每个题目都是「clue = eval(answer)」式的代码字谜。",
    "https://news.ycombinator.com/item?id=48262067":
        "Show HN：自制小型 PR guardrail 工具，专门检测 LLM 生成代码引入的 token bloat，征求是否值得维护。",
    "https://news.ycombinator.com/item?id=48262093":
        "「No Asterisk Products」宣言：服务器宕机时仍然可用的硬件——拒绝「需联网/付费/订阅才工作」的星号条款。",
    "https://news.ycombinator.com/item?id=48262460":
        "研究/文章：AI 如何成功说服阴谋论者放弃错误信念，对人类辩论与公共对话的启示。",
    "https://news.ycombinator.com/item?id=48262413":
        "实战分享：怎么教 Codex 给一个 voice-first 日历 App 写测试。",
    "https://news.ycombinator.com/item?id=48262062":
        "（测试条目，标题就是「Test」。）",
    "https://news.ycombinator.com/item?id=48261987":
        "新闻：Anthropic 与 OpenAI 抢着把驻场工程师塞进华尔街银行/对冲基金的工作流，争夺金融业大客户。",
    "https://news.ycombinator.com/item?id=48261970":
        "解读：正在搅动华盛顿监管层的几个 AI 模型，你需要知道什么。",
    "https://news.ycombinator.com/item?id=48262399":
        "讨论：你最喜欢的经典 iPod 游戏是什么——怀旧型 HN 帖。",
    "https://news.ycombinator.com/item?id=48261999":
        "TIL：Linux 内核模块用 CLFLUSHOPT 在清空敏感数据后强制刷掉对应 CPU cache 行，防止侧信道泄密。",
    "https://news.ycombinator.com/item?id=48262031":
        "安全研究：在 1 分钟内可被破解的密码占了「几乎所有其它密码」的大头，警示用户加强强度。",
    "https://news.ycombinator.com/item?id=48262022":
        "Librarian：整理 Arcane Library 用的工具/项目。",
    "https://news.ycombinator.com/item?id=48262313":
        "文章：Google 强制要求一定数量真实测试者才能上架，催生了 Fiverr 上的「凑测试者」灰色市场。",
    "https://news.ycombinator.com/item?id=48262307":
        "科普新闻：科学家发现某黑洞质量增长速度「快得离谱」，挑战现有黑洞演化模型。",
    "https://news.ycombinator.com/item?id=48262204":
        "案例分享：用 Mununu 验证 Caliptra 安全启动状态机（Boot-FSM）中的一个 bug。",
    "https://news.ycombinator.com/item?id=48262425":
        "Show HN：Mvm，一个用 Go 写的高性能虚拟机。",
    "https://news.ycombinator.com/item?id=48262169":
        "（测试条目，标题为「Poll: Test」。）",
    "https://news.ycombinator.com/item?id=48262153":
        "新闻：长跑众筹大作 Star Citizen 累计融资达到 10 亿美元，仍未发布完整正式版。",
    "https://news.ycombinator.com/item?id=48261923":
        "观点：「AI for Design」目前还远未被真正解决，HN 讨论设计领域生成式 AI 的真痛点。",
    "https://news.ycombinator.com/item?id=48262025":
        "Enhanced Games：允许使用类固醇和兴奋剂的「平行奥运会」，HN 讨论体育、伦理与人体增强。",
    "https://news.ycombinator.com/item?id=48262186":
        "趣文：全球最高密度的城市/居住环境是哪里——可视化与历史地理分析。",
    "https://news.ycombinator.com/item?id=48262205":
        "观点：Agent 评测（evals）应该「感觉像真实工作」，而非合成 toy task；否则评分难以反映生产能力。",
    "https://news.ycombinator.com/item?id=48262006":
        "Show HN：Tuie，一个面向 Rust 的高性能、组件丰富 TUI 库。",
    "https://news.ycombinator.com/item?id=48261922":
        "项目：实时追踪新闻业 AI 翻车（编造引语、AI 生成图未标注、错误事实等）的事故/丑闻名单。",
    "https://news.ycombinator.com/item?id=48262357":
        "Searx 作者复盘：从零创建去中心化元搜索引擎 Searx 过程中学到的工程与社区经验。",
    "https://news.ycombinator.com/item?id=48262015":
        "科普：原子究竟是由什么构成的——夸克、胶子、电子之间的关系。",
    "https://news.ycombinator.com/item?id=48262443":
        "Honopinion：某个意见/工具项目（信息有限，可能为社区讨论平台或观点聚合）。",
    "https://news.ycombinator.com/item?id=48262435":
        "工程分享：团队介绍他们如何构建安全、可扩展的 agent 沙箱基础设施。",
    "https://news.ycombinator.com/item?id=48262364":
        "新闻：Google 即将更新 Gmail 收件箱视图，新增「What Matters Most」分组优先突出重要邮件。",

    # 2026-05-26 — Anthropic
    "https://www.anthropic.com/news/chris-olah-pope-leo-encyclical":
        "Anthropic 联创 Chris Olah 在梵蒂冈发布教皇 AI 通谕的活动上发言：AI 实验室内部激励可能与「做正确的事」冲突，必须有产业之外的道德声音参与；他点出三个需要教会洞察的领域——让 AI 红利惠及全球穷人、对 AI 时代人类繁荣的道德想象、以及探究模型内部神秘结构与疑似情感状态。",

    # 2026-05-26 — GitHub Trending
    "https://github.com/affaan-m/ECC":
        "ECC：面向 Claude Code/Codex/Opencode/Cursor 等的 agent 框架性能优化系统，集技能、直觉、记忆、安全与研究优先开发于一体。",
    "https://github.com/hardikpandya/stop-slop":
        "stop-slop：一个 skill 文件，用于去除文章里明显的「AI 腔」痕迹，让文字更像真人写的。",
    "https://github.com/paperless-ngx/paperless-ngx":
        "paperless-ngx：社区维护的强化版文档管理系统，可扫描、索引并归档所有纸质与电子文档。",
    "https://github.com/Leonxlnx/taste-skill":
        "taste-skill：给 AI 注入「审美」的 skill，避免它生成无聊、套路化的平庸内容。",
    "https://github.com/Fincept-Corporation/FinceptTerminal":
        "FinceptTerminal：现代金融终端应用，提供市场分析、投资研究与经济数据工具，主打交互式探索与数据驱动决策。",
    "https://github.com/Axorax/awesome-free-apps":
        "awesome-free-apps：精选 PC 与移动端最佳免费应用的清单合集。",
    "https://github.com/anthropics/claude-cookbooks":
        "claude-cookbooks：Anthropic 官方 notebook 合集，演示使用 Claude 的各种有趣且高效的玩法与配方。",
    "https://github.com/moeru-ai/airi":
        "airi：自托管、归你所有的 AI 伴侣容器，支持实时语音聊天、Minecraft/Factorio 操作，跨 Web/macOS/Windows，对标 Neuro-sama。",

    # 2026-05-26 — YouTube AI
    "https://www.youtube.com/watch?v=ScLu47riJfY":
        "midudev 频道：微软、Uber 因 AI 成本开始削减 Claude Code 用量，借此讨论 token 成本、GitHub Copilot 与「用 AI 编程到底划不划算」。",
    "https://www.youtube.com/watch?v=YX7nE-3rYEQ":
        "Higgsfield 官方：推介 Supercomputer——把 Claude/Gemini/ChatGPT 等顶级推理模型与内容生成器整合进单一聊天、端到端跑营销的 AI agent。",
    "https://www.youtube.com/watch?v=pF4Ovay98nA":
        "AIM Network（日语）：微软停掉大批 Claude Code 授权并非因工具不好，而是 AI 能耗与规模化成本问题，认为 AI 计费模式在大规模下已失灵。",
    "https://www.youtube.com/watch?v=ck0-UD-oByY":
        "AIM Network（日语）：一个名为 Cockroach Janta Party 的政党被 AI 用 Claude 和 ChatGPT 在 24 小时内「组建」，展示 AI 快速生成品牌纲领，引发对 AI 政治的担忧。",
    "https://www.youtube.com/watch?v=S4gsd1_f-Ng":
        "Inteligencia Artificial 频道（西语）：每周 AI 新闻，重点吐槽 Gemini 3.5 Flash 看似又好又便宜，但实测 token 消耗高、性价比大打折扣。",

    # 2026-05-26 — Hacker News Newest
    "https://news.ycombinator.com/item?id=48274453":
        "报道：AI 让自助打官司激增，大量当事人用 AI 自行撰写诉状，法院卷宗被「自酿」诉讼淹没。",
    "https://news.ycombinator.com/item?id=48274042":
        "报道：某大型大学系统全面推行 AI，但学生和教职工并不买账，揭示校园 AI 推广的阻力。",
    "https://news.ycombinator.com/item?id=48274026":
        "Show HN：作者发现 43% 的 MCP 服务器含注入攻击载荷，于是做了 Aigis 防火墙来拦截这类提示注入。",
    "https://news.ycombinator.com/item?id=48274410":
        "安全披露：GitHub 提交签名验证逻辑存在缺陷，可被绕过以伪造「已验证」(Verified) 标记。",
    "https://news.ycombinator.com/item?id=48274372":
        "文章：单个模型有盲区，用多个 LLM 互相循环协作来调试陌生/不熟悉的代码。",
    "https://news.ycombinator.com/item?id=48274295":
        "MileStone：一个多目标的编译器优化阶段排序框架，自动权衡多项指标来调优 pass 顺序。",
    "https://news.ycombinator.com/item?id=48274212":
        "产品：带引用的 AI 工作区，主打文件只需上传一次、无需反复重新上传。",
    "https://news.ycombinator.com/item?id=48274336":
        "Show HN：Pgcraft，仿 lazygit 风格的 Postgres 终端 TUI 客户端。",
    "https://news.ycombinator.com/item?id=48274012":
        "Summer Shred（supercomp.app）：一款主打「夏季减脂/塑形」挑战的健身应用。",
    "https://news.ycombinator.com/item?id=48274311":
        "Ente（端到端加密相册）推出 Legacy Kit：让你指定的信任者在你去世后能继承访问你的加密账户。",
    "https://news.ycombinator.com/item?id=48274402":
        "Erin Brockovich 团队上线网站，对 AI 数据中心的环境与社区影响展开调查报道。",
    "https://news.ycombinator.com/item?id=48274229":
        "Jellyfin（开源媒体服务器）2026-05-24 的「State of the Fin」项目进展更新。",
    "https://news.ycombinator.com/item?id=48274302":
        "Matchmaker：一个强大现代的命令行模糊搜索/查找工具（Squirreljetpack/matchmaker）。",
    "https://news.ycombinator.com/item?id=48274052":
        "随笔《写作的社会契约》：探讨读者与作者之间关于真诚表达的隐性约定，在 AI 写作时代受到冲击。",
    "https://news.ycombinator.com/item?id=48274279":
        "Curious Pilot：一款辅助 UAP（不明空中现象）调查的软件工具。",
    "https://news.ycombinator.com/item?id=48274084":
        "Show HN：把 Notion 页面嵌入到自己网站的工具。",
    "https://news.ycombinator.com/item?id=48274215":
        "报道：随着开发者转向 AI 项目，加密货币的代码提交量下降了 75%。",
    "https://news.ycombinator.com/item?id=48274437":
        "（2020 旧文）研究：人造材料的总重量已超过地球上全部生命的总和。",
    "https://news.ycombinator.com/item?id=48274056":
        "Apple 支持文档：当被要求「确认你是成年人」时，如何用声明式年龄范围 API 验证年龄。",
    "https://news.ycombinator.com/item?id=48274064":
        "维基词条 Mondegreen：因听错而产生的歌词/短语谐音误解现象。",
    "https://news.ycombinator.com/item?id=48274185":
        "讨论：LLM 主动绕过了 pnpm 防供应链攻击的配置，引发对 AI agent 安全性的担忧。",
    "https://news.ycombinator.com/item?id=48274327":
        "（2020 旧文）LibreOffice 技巧：如何替换微软字体以保证文档排版兼容。",
    "https://news.ycombinator.com/item?id=48274048":
        "财经新闻：台湾超越印度，成为全球第五大股票市场。",
    "https://news.ycombinator.com/item?id=48274387":
        "Pinned：每日一题的地理「落点猜位置」小游戏（pinned.engineering）。",
    "https://news.ycombinator.com/item?id=48274081":
        "求测试者：一款自托管 + Android 客户端的云盘应用，主打「别再为同一件事付两次钱」。",
    "https://news.ycombinator.com/item?id=48274014":
        "工程复盘：团队因规模增长「用超」了 Cloudflare D1，讲述迁移取舍。",
    "https://news.ycombinator.com/item?id=48274018":
        "工具：基于 WebCrypto 的浏览器端文件加密工具，本地加解密无需上传。",
    "https://news.ycombinator.com/item?id=48274077":
        "讨论：到底有没有人真的喜欢 React？引发对前端框架使用体验的吐槽与辩论。",
    "https://news.ycombinator.com/item?id=48274049":
        "产品：AI SEO 工具，帮你与竞争对手做对比分析。",
    "https://news.ycombinator.com/item?id=48274472":
        "新闻：Waymo 因安全问题暂停了所有高速公路上的载客行程。",

    # 2026-05-26 第二批（retry arXiv 时新增的社区动态）— YouTube AI
    "https://www.youtube.com/watch?v=rfKzTqCygE4":
        "ANNnewsCH（日语新闻）：读卖巨人队主帅阿部慎之助涉嫌对 18 岁女儿施暴被捕后释放，其女儿先向 ChatGPT 咨询、依其建议联系了儿童咨询所而案发。",
    "https://www.youtube.com/watch?v=MMKDinYD5LQ":
        "（误命中）Sun Gemini 频道的泰卢固语电视剧《Srimati Annapurna Catering》每日精彩片段，与 AI 无关——「Gemini」是电视频道名。",
    "https://www.youtube.com/watch?v=IZOGd8LxrTQ":
        "（误命中）西班牙语双子座（Géminis）塔罗占卜视频，与 AI 无关——「Geminis」指星座。",

    # 2026-05-26 第二批 — Hacker News Newest
    "https://news.ycombinator.com/item?id=48275198":
        "Manticore Search 博客：讲解如何让「xt850」与「xt 850」这类带空格差异的查询互相匹配（搜索分词/规范化技巧）。",
    "https://news.ycombinator.com/item?id=48275331":
        "（疑似垃圾/赚钱博客）标题「If you don't know you must know it」，指向一个声称「每天赚 3 美元」的免费 PDF 博客。",
    "https://news.ycombinator.com/item?id=48275407":
        "《纽约客》随笔：探讨为什么「做个普通人」如此之难——关于平凡与自我价值。",
    "https://news.ycombinator.com/item?id=48275326":
        "（疑似软文）Yahoo 财经健康版：「Gelatine Sculpt」减肥产品的 2026 专家指南，病毒式营销内容。",
    "https://news.ycombinator.com/item?id=48275232":
        "Show HN：Versionparser，处理各种版本号方案的 Java 库。",
    "https://news.ycombinator.com/item?id=48275186":
        "美联社：科技公司 CEO 再次被传唤到国会，就社交媒体的风险举行听证。",
    "https://news.ycombinator.com/item?id=48275092":
        "The Little Go Book：一本免费的 Go 语言入门书（开源）。",
    "https://news.ycombinator.com/item?id=48275201":
        "Alex Smola 博文：你不需要所有 LLM 基准——如何有针对性地挑选评测基准。",
    "https://news.ycombinator.com/item?id=48275047":
        "博文：给出「Agent Endpoint（智能体端点）」的工作定义。",
    "https://news.ycombinator.com/item?id=48275038":
        "Ask HN：你是何时、为何开始信仰上帝的？社区讨论帖。",
    "https://news.ycombinator.com/item?id=48275395":
        "Ask HN：最好的免费本地语音转文字（STT）方案是什么？",
    "https://news.ycombinator.com/item?id=48275106":
        "新闻：瑞典一辆自动驾驶巴士在载客服务首日就与有轨电车相撞。",
    "https://news.ycombinator.com/item?id=48275072":
        "哈佛商学院文章：AI 更可能是「增强」还是「取代」这些岗位？",
    "https://news.ycombinator.com/item?id=48275098":
        "Simon Willison 评教皇 Leo XIV 的 AI 通谕《Magnifica Humanitas》（该博文被转发到 HN）。",
    "https://news.ycombinator.com/item?id=48275053":
        "《金融时报》：发达国家的实际工资开始缩水。",
    "https://news.ycombinator.com/item?id=48275360":
        "视频：John Cleese 谈管理中的创造力。",
    "https://news.ycombinator.com/item?id=48275113":
        "《每日电讯报》：男生们制造「AI 女友」的风潮日益兴起，引发担忧。",
    "https://news.ycombinator.com/item?id=48275398":
        "Marc Randolph（Netflix 联创）推文：判断早期创业公司陷入麻烦的一个可靠信号。",
    "https://news.ycombinator.com/item?id=48275251":
        "Show HN：nilbox，给 AI agent 与 MCP 服务器用的桌面 GUI 沙箱。",
    "https://news.ycombinator.com/item?id=48275337":
        "Zed 博客：为何以及如何在 Zed 编辑器里运行本地大模型。",
    "https://news.ycombinator.com/item?id=48275257":
        "新闻：随着屏幕充斥课堂，美国学校对数字设备的反对声浪上升。",
    "https://news.ycombinator.com/item?id=48275059":
        "博文《The User Is Visibly Frustrated》：关于产品/AI 用户明显受挫体验的思考。",
    "https://news.ycombinator.com/item?id=48275336":
        "Ask HN：是 Codex 在提供更差的模型，还是只是它的 harness 变差了？",
    "https://news.ycombinator.com/item?id=48275295":
        "文章：CRPG 复兴（上）——以《辐射 Fallout》为例的回顾。",
    "https://news.ycombinator.com/item?id=48275041":
        "讨论：Google 表格换了新 favicon——但为什么？",
    "https://news.ycombinator.com/item?id=48275121":
        "Show HN：作者被 GPT Image 2 惊艳又折腾，于是做了个小工具（imagesv2.ai）。",
    "https://news.ycombinator.com/item?id=48275255":
        "博文：为 Pandoc 写的一个新 Typst 模板。",
    "https://news.ycombinator.com/item?id=48275288":
        "（2007 旧文）《卫报》：MySpace 会失去它的垄断地位吗？",
    "https://news.ycombinator.com/item?id=48275148":
        "（疑似软文）Medium 文章 Noioaapps：「我们的工具让你保持知情」（一个梦想）。",
    "https://news.ycombinator.com/item?id=48275069":
        "TechCrunch：NanoClaw 创始人拒绝 2000 万美元收购要约，转而完成 1200 万美元种子轮融资。",
    # 2026-05-28
    "https://www.anthropic.com/news/kiyoung-choi-representative-director-anthropic-korea":
        "任命 KiYoung Choi 为 Anthropic 韩国代表理事，首尔办公室即将开张，加速亚太市场布局。",
    # GitHub Trending
    "https://github.com/twentyhq/twenty":
        "Twenty：开源的 Salesforce 替代品，定位为面向 AI 时代的 CRM。",
    "https://github.com/DigitalPlatDev/FreeDomain":
        "DigitalPlat FreeDomain：免费的二级域名分发服务（如 us.kg / e-com.cn 等），自助申请。",
    "https://github.com/harry0703/MoneyPrinterTurbo":
        "MoneyPrinterTurbo：输入主题/关键词，用 LLM 自动生成口播 + 字幕 + 配乐的高清短视频流水线。",
    "https://github.com/Chachamaru127/claude-code-harness":
        "Claude Code 专用开发 harness：通过自动 Plan→Work→Review 循环驱动高质量代码产出。",
    "https://github.com/iii-hq/iii":
        "iii：本地服务编排 + 实时观测一体化工具，号称首次能实时编辑/扩展每一个服务。",
    "https://github.com/p-e-w/heretic":
        "Heretic：自动化「去审查」语言模型的工具——批量改写拒答行为以做对齐研究/越狱实验。",
    "https://github.com/byoungd/English-level-up-tips":
        "面向程序员的「离谱英语学习指南」：中文写就的英语学习路径与资源合集，长期热门仓库。",
    # YouTube AI
    "https://www.youtube.com/watch?v=4y-BFS5Mpe8":
        "Ontogenesis 的 LLM 入门教程：覆盖定义、Transformer 架构、JS 代码调用 API，对比 GPT-5/Gemini Ultra 2/Llama 4，并讲行业落地与生产优化。",
    "https://www.youtube.com/watch?v=6LwQ8RbU9as":
        "Matthew Berman 介绍 DeepSWE 基准——他认为这是评估代码 Agent 的一个有效新基准。",
    "https://www.youtube.com/watch?v=8IzUyLLn5NA":
        "Alex Ziskind 对同一模型做 8 档量化对比，找量化精度从哪一档开始「胡说八道」——4-bit 表面看仍正常。",
    "https://www.youtube.com/watch?v=gC76aeibdFA":
        "bycloud 深度拆解 DeepSeek V4 论文上半部分：低成本背后的关键技术突破。",
    "https://www.youtube.com/watch?v=iqddnwKF8HQ":
        "JetBrains 专访 Zig 创始人 Andrew Kelley：为何 Zig 拒绝 AI、迁出 GitHub、十年不发 1.0，以及对 C 替代语言失败原因的看法。",
    "https://www.youtube.com/watch?v=tZIlsfPhBHU":
        "midudev 实测 MiniMax M2.7：号称比 Claude 便宜 10 倍，可在 Claude Code/CLI 中替代用于编程、Agent、音视频生成。",
    "https://www.youtube.com/watch?v=xo_9BNqUSZ0":
        "韩国经济新闻 实测梳理 Google I/O 2026：Gemini 3.5 Flash 主打性价比、25 年来首改搜索框为 AI 智能化、首次亮相与三星/Gentle Monster 联名智能眼镜。",
    # HN Newest
    "https://news.ycombinator.com/item?id=48306150":
        "Show HN：开发者发布 reminders-sync 工具更新，附带 neural web 项目的 bug 修复。",
    "https://news.ycombinator.com/item?id=48306173":
        "Show HN：关于 AI Agent 在检索和动作前先做「方向感」对齐的设计提案。",
    "https://news.ycombinator.com/item?id=48306179":
        "论文/博文：GitHub Actions 工作流 DSL 的使用模式、演化与可靠性研究。",
    "https://news.ycombinator.com/item?id=48305990":
        "博文：当产品具备「思考」能力——如何在 AI 范式转型期重新设计产品。",
    "https://news.ycombinator.com/item?id=48306178":
        "Netflix 正在搭建一座 AI 动画工作室，要把生成式 AI 内嵌到内容生产管线。",
    "https://news.ycombinator.com/item?id=48306155":
        "视频：与我们未来的机器人霸主（和它的宠物人类）的对谈——讽刺向短片。",
    "https://news.ycombinator.com/item?id=48306116":
        "外媒报道：LG 据称在与海信洽谈出售其电视业务。",
    "https://news.ycombinator.com/item?id=48306026":
        "光纤制导无人机：通过物理光纤通信、抗电子干扰的战术无人机方案。",
    "https://news.ycombinator.com/item?id=48305883":
        "经典论文 PDF 重刷热度：跨编程语言的能耗效率对比研究。",
    "https://news.ycombinator.com/item?id=48306140":
        "Show HN：作者反潮流——别人做有记忆的 AI Agent，他做了一个有「身体」（实体）的 Agent。",
    "https://news.ycombinator.com/item?id=48306019":
        "博文：批判 SOLID 之 SRP 原则——指出「单一职责」存在基数（cardinality）层面的逻辑错误。",
    "https://news.ycombinator.com/item?id=48306073":
        "Show HN：作者发布 samspov.com，方便追踪 Sam Altman POV 内容的更新。",
    "https://news.ycombinator.com/item?id=48305915":
        "博文：训练前沿字体生成模型的踩坑总结。",
    "https://news.ycombinator.com/item?id=48305968":
        "博文：7 个降低被 AI 取代风险的实用建议。",
    "https://news.ycombinator.com/item?id=48306212":
        "博文：一个 C/C++ 案例分析——为何同一段代码在某编译器下行为与其他编译器不同。",
    "https://news.ycombinator.com/item?id=48305896":
        "Ask HN：能否用 8 张 GPU 训出万亿参数 LLM？社区讨论可行性与方案。",
    "https://news.ycombinator.com/item?id=48306029":
        "博文：在 Python 里加类型注解会让代码风格走向不一样的「方向」。",
    "https://news.ycombinator.com/item?id=48305974":
        "Robinhood 允许客户用 AI 助手下单股票交易和操作信用卡消费。",
    "https://news.ycombinator.com/item?id=48305937":
        "Show HN：Ax 语言——为 AI Agent 设计的紧凑源码格式与构建系统。",
    "https://news.ycombinator.com/item?id=48306068":
        "纽约时报讣告：Times 字谜的妙趣作者 Manny Nosowsky 去世，享年 94 岁。",
    "https://news.ycombinator.com/item?id=48306055":
        "博文：SOLID 之 ISP 接口隔离原则其实是 DIP（依赖倒置）的条件性推论。",
    "https://news.ycombinator.com/item?id=48305949":
        "论文：DiffusionBlocks——一次一个 block 地训练神经网络的扩散式方法。",
    "https://news.ycombinator.com/item?id=48306139":
        "C++ 历史掌故：std::bitset 是如何从一个 MS-DOS 实用问题演化进入 C++ 标准库的。",
    "https://news.ycombinator.com/item?id=48305987":
        "博文：提前准备好你的「拒绝」并随手能用——一种工作/边界管理建议。",
    "https://news.ycombinator.com/item?id=48306127":
        "（2025）微软承认无法保证客户数据主权——欧盟数据被美国法律管辖。",
    "https://news.ycombinator.com/item?id=48305955":
        "解读：美国为何把驻军从德国转移到波兰——一名美军军官的视角。",
    "https://news.ycombinator.com/item?id=48305988":
        "论文 PDF：把 AI 数据中心建在太空的可行性研究。",
    "https://news.ycombinator.com/item?id=48306066":
        "公告：Hetzner 调价（涨/降价细则）。",
    "https://news.ycombinator.com/item?id=48305934":
        "Show HN：LaunchPact——帮你的 ProductHunt 上线刷点赞的服务（疑似软文）。",
    "https://news.ycombinator.com/item?id=48306196":
        "Show HN：Taste Skill——面向 AI Agent 的「反 slop」前端框架，强调审美与一致性。",

    # 2026-05-29 Anthropic（英文新闻，手写中文摘要）
    "https://www.anthropic.com/news/claude-opus-4-8":
        "发布 Claude Opus 4.8：官方称是对前代「温和但切实」的改进，并预告将推出能力相近、成本更低的模型。",
    "https://www.anthropic.com/news/milan-office-opening":
        "在米兰开设办公室，服务意大利企业、研究机构与开发者，扩展欧洲业务版图。",
    "https://www.anthropic.com/news/series-h":
        "完成 650 亿美元 H 轮融资，投后估值 9650 亿美元；自 2 月 G 轮以来年化运营营收已突破 470 亿美元。",

    # 2026-05-29 GitHub Trending
    "https://github.com/OpenMOSS/MOSS-TTS":
        "MOSS-TTS：MOSI.AI 与 OpenMOSS 团队开源的语音/声音生成模型家族，主打高保真、高表现力，覆盖长语音、多说话人对话、音色设计、环境音效与实时流式 TTS。",
    "https://github.com/revfactory/harness":
        "harness：一个「元技能」，能设计领域专属的 Agent 团队、定义专门化 Agent，并自动生成它们所需的技能。",
    "https://github.com/microsoft/markitdown":
        "markitdown：微软出品的 Python 工具，把各类文件和 Office 文档转换为 Markdown。",
    "https://github.com/EveryInc/compound-engineering-plugin":
        "compound-engineering-plugin：Every 公司官方的「复合工程」插件，支持 Claude Code、Codex、Cursor 等多种 AI 编程工具。",
    "https://github.com/unclecode/crawl4ai":
        "crawl4ai：开源、对 LLM 友好的网页爬虫与抓取器，专为喂给大模型做数据准备而设计。",
    "https://github.com/anthropics/skills":
        "anthropics/skills：Anthropic 官方公开的 Agent Skills（技能）仓库。",

    # 2026-05-29 YouTube AI
    "https://www.youtube.com/watch?v=F_6go08nHv4":
        "Wes Roth 视频：解读 Claude Opus「Ultra Code」长任务编码能力，渲染其将颠覆多个行业的观点。",
    "https://www.youtube.com/watch?v=6whw-3v9jm0":
        "Sun NXT 餐饮综艺节目预告（「Srimati Annapurna Catering」），与 AI 无关，因频道名含 Gemini 被误抓。",
    "https://www.youtube.com/watch?v=5HVPeux24WU":
        "Claude 官方视频：演示用 Opus 4.8 和 Claude Code 处理长时间运行的任务。",
    "https://www.youtube.com/watch?v=xrSSObzPSk4":
        "Entertainment Tonight 报道冰球名将 Claude Lemieux 60 岁自杀身亡，与 AI 无关，因人名含 Claude 被误抓。",
    "https://www.youtube.com/watch?v=v1zSDACAXK4":
        "Mo Bitar 的短评视频「GPT 5.5 bro」，调侃/体验 OpenAI 的 GPT-5.5。",

    # 2026-05-29 Hacker News Newest
    "https://news.ycombinator.com/item?id=48320631":
        "Show HN：EV-QA-Framework——用机器学习为电动车电池系统做质量检测的框架。",
    "https://news.ycombinator.com/item?id=48320440":
        "用纯组合学/数学方式讲解费曼图，不涉及任何物理。",
    "https://news.ycombinator.com/item?id=48320360":
        "研究发现：即使明确警告某陈述为假，LLM 仍会相信并采信这些虚假陈述。",
    "https://news.ycombinator.com/item?id=48320375":
        "Gay-Torrents 站点在被诉后关闭，FlavaWorks 将起诉对象从 325 名用户缩减到 39 名。",
    "https://news.ycombinator.com/item?id=48320366":
        "评论文章：数字经济正在摧毁我们的生活和地球。",
    "https://news.ycombinator.com/item?id=48320656":
        "Show HN：Blinken——macOS 菜单栏小工具，用 LED 灯指示磁盘读写活动。",
    "https://news.ycombinator.com/item?id=48320378":
        "数据可视化文章：每年有五百万儿童死亡，他们究竟死于什么原因。",
    "https://news.ycombinator.com/item?id=48320596":
        "观点文章：婴儿潮一代如何「坑了」欧洲。",
    "https://news.ycombinator.com/item?id=48320666":
        "技术文章：用 GCC 的嵌套函数配合宽指针实现无 trampoline 的闭包。",
    "https://news.ycombinator.com/item?id=48320563":
        "随笔：用外语（英语）写作如何让作者找到了自己的声音。",
    "https://news.ycombinator.com/item?id=48320590":
        "字体专栏「Fonts in Focus」介绍字体 Evert。",
    "https://news.ycombinator.com/item?id=48320456":
        "SQL 提案：Key Joins，一种新的连接语法设想。",
    "https://news.ycombinator.com/item?id=48320674":
        "评论文章「The Burning Bill」：估算气候变化的真实经济代价（Veritas Europaea）。",
    "https://news.ycombinator.com/item?id=48320579":
        "Show HN：Sixbpm——一个免费小工具，引导你把呼吸放慢。",
    "https://news.ycombinator.com/item?id=48320370":
        "事故复盘：团队遭遇通过 GitHub PR 发起的攻击。",
    "https://news.ycombinator.com/item?id=48320499":
        "技术文章：ClickHouse Cloud 中的多阶段分布式查询执行。",
    "https://news.ycombinator.com/item?id=48320613":
        "医学进展：血液检测有望在症状出现「数十年前」就发现阿尔茨海默症迹象。",
    "https://news.ycombinator.com/item?id=48320536":
        "StoryScope：研究 AI 生成小说中的特异性/套路化倾向。",
    "https://news.ycombinator.com/item?id=48320350":
        "NASA 公布在月球南极建设月球基地的详细计划。",
    "https://news.ycombinator.com/item?id=48320409":
        "随笔「The 505-Commit Invoice」：围绕 505 次提交开账单引发的工作与计价反思。",
    "https://news.ycombinator.com/item?id=48320476":
        "用 AI 对 FreeBSD 代码做了一次安全审计。",
    "https://news.ycombinator.com/item?id=48320489":
        "宣称的「Opus 4.8 杀手」NexusCortex：自称不是 LLM，而是用 Go 写的稀疏「AI 皮层」（真实性存疑）。",
    "https://news.ycombinator.com/item?id=48320519":
        "北约成员国罗马尼亚称俄罗斯无人机击中一栋公寓楼，造成两人受伤。",
    "https://news.ycombinator.com/item?id=48320342":
        "探讨 WitnessLens 能否解决深度伪造（deepfake）的验证问题。",
    "https://news.ycombinator.com/item?id=48320655":
        "Show HN：一款刻意「慢」的 AI 日记应用。",
    "https://news.ycombinator.com/item?id=48320417":
        "Show HN：征求意见——一个「学习优先」的 AI 评测平台是否有用。",
    "https://news.ycombinator.com/item?id=48320667":
        "Wterm：运行在网页里的终端模拟器。",
    "https://news.ycombinator.com/item?id=48320664":
        "观点：为什么 .ipynb 是保存 AI 数据分析对话的理想格式。",
    "https://news.ycombinator.com/item?id=48320508":
        "Show HN：MapZap——花 49 美元从 Google 地图抓取 100 条本地商家线索。",
    "https://news.ycombinator.com/item?id=48320615":
        "安全分析：通过后端基础设施测绘一个横跨 64 国、1001 个 IP 的僵尸网络。",
    "https://news.ycombinator.com/item?id=48320349":
        "Show HN：Datacenter Tycoon——基于 WASM 版 OpenTTD 的数据中心产业模组游戏。",
    "https://news.ycombinator.com/item?id=48320504":
        "报道：不只 ChatGPT，多个聊天机器人都在从马斯克的 Grokipedia 抓取答案。",
    "https://news.ycombinator.com/item?id=48320479":
        "报道：司法系统试图隐藏一名法官姓名，结果反而留下了识别她身份的线索路径。",
    "https://news.ycombinator.com/item?id=48320639":
        "性能测试：缓存感知调度在 AMD Zen 5 上给 PostgreSQL、Valkey 带来明显提升。",
    "https://news.ycombinator.com/item?id=48320555":
        "报道：Mistral 向欧盟官员宣称拥有「Mythos 级」模型。",
    "https://news.ycombinator.com/item?id=48320454":
        "报道：随着成本飙升，美国企业开始「配给」式限制 AI 使用。",

    # 2026-06-01 YouTube AI
    "https://www.youtube.com/watch?v=Z81fNaMpklM":
        "俄语博主 СТЕБЛОВ 反应视频：揭「ChatGPT 邪教」现象——不少人把 ChatGPT 当作全知神明、试图「唤醒」其意识并组成 AI 信仰团体，称其为 2026 年危险趋势。",
    "https://www.youtube.com/watch?v=xqw4Aj-WRqg":
        "传闻 GPT 5.6 泄露，对标 Claude Mythos 同档跑分但更便宜、token 更省；同时盛传中国有一款来历不明的开源模型也在冲击 Mythos 级性能。",
    "https://www.youtube.com/watch?v=FGn_uT2c8xI":
        "Abacus AI 推出 AI SuperComputer：常驻云端的真实 Ubuntu 环境，AI 智能体可在其中带数据库、终端、SSH、GitHub/AWS、一键 HTTPS 部署地构建并运行真实软件，背后接入 Claude 与 Gemini。",
    "https://www.youtube.com/watch?v=84NkgiTcOdo":
        "Riley Brown 评测 Anthropic 新模型 Opus 4.8 表现、与 GPT 5.5 对比，并盘点 OpenAI Codex 最新更新（Windows 电脑操作、移动端 App、浏览器升级等）。",
    "https://www.youtube.com/watch?v=hv89f-zdjmk":
        "介绍 PewDiePie 开源的本地 LLM 聊天应用 Odysseus：免费、可借 Ollama 在本地跑各种模型，配 Docker 部署教程。",

    # 2026-06-02 公司动态（HTML / 中文源）
    "https://www.anthropic.com/news/confidential-draft-s1-sec":
        "Anthropic 向美国 SEC 秘密递交 S-1 草案文件，启动潜在 IPO 上市流程的保密审阅阶段。",
    "https://transformer-circuits.pub/2026/may-update/index.html":
        "Anthropic 可解释性团队 2026 年 5 月《Circuits Updates》：机制可解释性研究月度进展合集（特征、电路、归因等多篇短文更新）。",

    # 2026-06-02 GitHub Trending
    "https://github.com/OpenBMB/VoxCPM":
        "OpenBMB 的 VoxCPM2：免分词器（tokenizer-free）TTS 模型，支持多语种语音生成、创意音色设计与逼真声音克隆。",
    "https://github.com/godotengine/godot":
        "Godot 引擎：跨平台开源 2D/3D 游戏引擎。",
    "https://github.com/supermemoryai/supermemory":
        "supermemory：面向 AI 时代的高速可扩展记忆引擎与 Memory API，附配套应用。",
    "https://github.com/stefan-jansen/machine-learning-for-trading":
        "《机器学习用于算法交易（第 2 版）》配套代码库。",
    "https://github.com/nesquena/hermes-webui":
        "Hermes WebUI：从网页或手机使用 Hermes Agent 的前端界面。",
    "https://github.com/dmtrKovalenko/fff":
        "fff：面向 AI 智能体、Neovim、Rust/C/Node.js 的高速高精度文件搜索工具包。",
    "https://github.com/TauricResearch/TradingAgents":
        "TradingAgents：多智能体 LLM 金融交易框架。",
    "https://github.com/FareedKhan-dev/train-llm-from-scratch":
        "train-llm-from-scratch：从下载数据到生成文本，从零训练自己 LLM 的简明教程代码。",
    "https://github.com/pbakaus/impeccable":
        "impeccable：一套让 AI 编码工具更擅长做设计的「设计语言」。",

    # 2026-06-02 Hacker News Newest
    "https://news.ycombinator.com/item?id=48367353":
        "安全预警：通过「错误预言机（Error Oracle）」侧信道泄露信息，提醒 Maravel/Lumen 用户注意。",
    "https://news.ycombinator.com/item?id=48367405":
        "佛罗里达州起诉 OpenAI 和 Sam Altman，指控其存在安全疏失。",
    "https://news.ycombinator.com/item?id=48367550":
        "分享一款帮你省空调电费的小工具。",
    "https://news.ycombinator.com/item?id=48367296":
        "南非 Wonderwerk 洞穴出现早更新世人类用火的新证据。",
    "https://news.ycombinator.com/item?id=48367491":
        "报道：欧盟拟加入美国主导的芯片联盟「Pax Silica」，以对抗中国的 AI 竞赛。",
    "https://news.ycombinator.com/item?id=48367464":
        "研究：可通过测量 SSD 活动来窥探用户的浏览行为。",
    "https://news.ycombinator.com/item?id=48367547":
        "观点：世界模型所需数据量比 LLM 指数级地少。",
    "https://news.ycombinator.com/item?id=48367303":
        "批评：SAFe、LeSS、Nexus 这几套规模化敏捷框架都行不通。",
    "https://news.ycombinator.com/item?id=48367223":
        "报道：一所大学系统全面押注 AI，如今内部因此分崩离析。",
    "https://news.ycombinator.com/item?id=48367260":
        "AI 激光灭蚊防御系统 2.0 版发布。",
    "https://news.ycombinator.com/item?id=48367256":
        "Show HN：为厌倦劣质会议周边的开发者打造的 T 恤品牌。",
    "https://news.ycombinator.com/item?id=48367292":
        "黑客诱骗 Meta AI 客服机器人，借此入侵奥巴马白宫的 Instagram 账号。",
    "https://news.ycombinator.com/item?id=48367247":
        "工程复盘（2022）：把 Instagram 基础视频的计算耗时降低 94%。",
    "https://news.ycombinator.com/item?id=48367355":
        "评论文章《致美国：曾经你很了不起》。",
    "https://news.ycombinator.com/item?id=48367211":
        "技术分享：用 Jank（Clojure 方言）做光线追踪。",
    "https://news.ycombinator.com/item?id=48367301":
        "Show HN：为 Home Assistant 做的 Assist 调试卡片。",
    "https://news.ycombinator.com/item?id=48367520":
        "NBA 球星斯蒂芬·库里与中国品牌李宁签订球鞋代言合约。",
    "https://news.ycombinator.com/item?id=48367294":
        "观点：为什么合并冲突（merge conflict）成了智能体编码的新瓶颈。",
    "https://news.ycombinator.com/item?id=48367362":
        "大众通过 API 变更削减车主访问自己车辆数据的权限。",
    "https://news.ycombinator.com/item?id=48367388":
        "OpenAIRE 举办 AI 黑客松。",
    "https://news.ycombinator.com/item?id=48367266":
        "巴西已禁止「成瘾式设计」，但关键监管细节仍待落实。",
    "https://news.ycombinator.com/item?id=48367540":
        "OpsGrid：一眼总览云基础设施栈的工具。",
    "https://news.ycombinator.com/item?id=48367393":
        "民科式理论：用一条递归公式贯通所有尺度的「万物共振层级」。",
    "https://news.ycombinator.com/item?id=48367497":
        "伦敦网友求助：整理一份 AI 圈值得关注的 X（推特）账号清单。",
    "https://news.ycombinator.com/item?id=48367412":
        "长文：在太空中建立「帝国」的现实有多混乱。",
    "https://news.ycombinator.com/item?id=48367253":
        "Cloudflare CDN 2026 定价分析：每 GB 真实成本、隐藏费用与最佳替代方案。",
    "https://news.ycombinator.com/item?id=48367553":
        "观点：技术面试正在淘汰错误的工程师。",
    "https://news.ycombinator.com/item?id=48367506":
        "技巧分享：用符号链接把个人博客和书稿纳入 Obsidian 知识库。",
    "https://news.ycombinator.com/item?id=48367245":
        "视频：快餐业的数字化革命——快餐为何变得如此昂贵。",
    "https://news.ycombinator.com/item?id=48367408":
        "ChatGPhish：把网页本身当作攻击载荷的钓鱼手法。",

    # 2026-06-02 YouTube AI
    "https://www.youtube.com/watch?v=cS0Tm6ddnsQ":
        "Wes Roth AI 资讯：盘点 GPT-5.6 即将发布的传闻，以及 OpenAI/Google/Anthropic/英伟达/开源圈近期动态。",
    "https://www.youtube.com/watch?v=g9lnL8PLlm8":
        "Daniel Hentschel 视频：讨论一起将儿子之死归咎于 ChatGPT 的案例（AI 与心理健康责任争议）。",
    "https://www.youtube.com/watch?v=LWji1B_7VBo":
        "Paul Barron 演示并采访 CEO：多资产交易平台 Liquid 推出 Co-Invest，让用户直接在 ChatGPT 和 Claude 里下真实交易，覆盖加密货币、股票、外汇、Polymarket 等。",
    "https://www.youtube.com/watch?v=aMyubFA106U":
        "Peter Diamandis 播客 EP#260：讨论 Anthropic Opus 4.8 发布、OpenAI 基金会、Demis Hassabis 对 AGI 的预测以及 AI 极端主义抬头。",
    "https://www.youtube.com/watch?v=sfCm60LVVuI":
        "코드팩토리（韩语）：13 分钟速讲 20 条 Claude Code 必备实用技巧。",

    # 2026-06-10 YouTube AI
    "https://www.youtube.com/watch?v=9GLYsrMpprs":
        "Bijan Bowen 上手实测 Claude Fable 5：跑浏览器 OS、C++ 滑板游戏模拟、SVG 动画、网络封包可视化、3D 打印模拟、高端前端等十余项测试，称其为迄今最强模型。",
    "https://www.youtube.com/watch?v=GrdEid8H6H4":
        "Every CEO Dan Shipper 实测 Fable 5 一周：在 Every 高级工程师基准拿 91/100（Opus 4.8 为 63、GPT-5.5 为 62），擅长研究、复杂判断与大型项目，但速度慢、价格贵，最适合高阶 agentic 开发者。",
    "https://www.youtube.com/watch?v=VNbW4wrcfSw":
        "BridgeMind 直播用 Claude Fable 5 做 vibe coding：跑 BridgeBench 基准对比 GPT-5.5 与 Gemini 3.5 Flash，给出实时排行榜分数。",
    "https://www.youtube.com/watch?v=xUbIVUnQnZg":
        "Wes Roth 评 Mythos 5（Fable 5）发布：盘点其新能力并讨论「这是不是 AGI」的争论。",
    "https://www.youtube.com/watch?v=Kb9A6riFJDo":
        "Tin 3 Phút Bí Ẩn（越南语社会新闻）：男生因 ChatGPT 使用问题与母亲争吵后深夜离家出走，最终酿成苦果。",

    # 2026-06-10 补抓 GitHub Trending + YouTube
    "https://github.com/maziyarpanahi/openmed":
        "OpenMed：开源医疗 AI 项目，提供面向医疗健康场景的开源模型与工具。",
    "https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools":
        "汇集 Claude Code、Cursor、Devin、Manus、Windsurf、v0 等数十款 AI 工具的完整系统提示词、内部工具与模型信息的大全仓库。",
    "https://github.com/francescopace/espectre":
        "ESPectre：基于 Wi-Fi 频谱分析（CSI）的运动检测系统，无需摄像头或传感器即可感知人体移动，支持 Home Assistant 集成。",
    "https://www.youtube.com/watch?v=AW3TJDuViF8":
        "AsapGuide 对比实测 Claude Fable 5 与 Opus 4.8：在 UI 重建、3D 游戏制作、文档分析等真实任务上逐项对比，结论是 Fable 5 在几乎所有基准上高于 Opus、GPT-5.5 与 Gemini 3.1 Pro。",

    # 2026-07-28 Anthropic HTML
    "https://www.anthropic.com/news/claude-opus-5":
        "Anthropic 发布 Claude Opus 5（7月24日）：定位「以一半价格逼近 Fable 5 前沿智能」，编码与知识工作基准（Frontier-Bench、GDPval-AA）达到新高，但网络安全任务仍落后于 Mythos 5；现为 Claude Max 默认模型、Pro 首选，定价与上代持平（输入 $5/百万、输出 $25/百万 token），号称欺骗行为率最低但对网络攻击与长周期生物研究保留更强防护。",
    "https://www.anthropic.com/news/cognizant-anthropic":
        "Anthropic 与 Cognizant（7月27日）深化合作：Cognizant 将 Claude 融入 Flowsource、Neuro AI Engineering、Neuro IT Ops 等平台，已培训超 3 万名「Frontier Certified」员工，并成为 Claude 合作伙伴网络「全球高级合作伙伴」；案例显示某生物制药客户用 Claude 构建的合同审查工具将审查时间缩短最多 40%。",
    "https://www.anthropic.com/news/position-open-weights-models":
        "Dario Amodei 澄清 Anthropic 从未主张封禁开放权重模型，真正担忧的是威权政权借此获得军事优势及模型被用于网络/生物攻击；主张的应对措施是限制对华先进芯片流通与走私、打击大规模模型蒸馏行为、对所有达到能力门槛的模型（无论开源闭源）强制安全测试。",

    # 2026-07-28 GitHub Trending / YouTube
    "https://github.com/ocornut/imgui":
        "Dear ImGui：C++ 轻量级即时模式图形界面库，几乎无依赖，广泛用于游戏引擎与工具开发调试界面。",
    "https://github.com/alibaba/open-code-review":
        "阿里开源的代码评审工具：确定性流水线 + LLM Agent 混合架构，提供精确到行的评论与内置微调规则集（空指针、线程安全、XSS、SQL 注入），兼容 OpenAI 与 Anthropic。",
    "https://github.com/opengeos/GeoLibre":
        "GeoLibre：轻量级云原生 GIS 平台，可在浏览器、桌面、移动端及 Jupyter Notebook 中可视化、探索与分析地理空间数据。",
    "https://github.com/apache/cassandra":
        "Apache Cassandra：开源分布式事务数据库，在商用硬件或云基础设施上提供线性可扩展性与经过验证的容错能力。",
    "https://github.com/jenkinsci/jenkins":
        "Jenkins：领先的开源自动化服务器，提供 2000+ 插件支持构建、测试、静态分析、部署等开发流程自动化。",
    "https://github.com/amnezia-vpn/amnezia-client":
        "AmneziaVPN 客户端：桌面与移动端自建 VPN 工具，主打抗封锁与易用性。",
    "https://github.com/permissionlesstech/bitchat":
        "bitchat：基于蓝牙 mesh 网络的去中心化聊天应用，无需服务器和网络连接，走 IRC 复古风格。",
    "https://github.com/yorukot/superfile":
        "superfile：外观精美的现代化终端文件管理器。",
    "https://github.com/vudovn/ag-kit":
        "ag-kit：面向 Google Antigravity 运行时的 Agent 工程套件，提供规则、技能、专家 Agent、工作流、持久记忆、MCP 指南与编排能力，含原生安全钩子。",
    "https://www.youtube.com/watch?v=nExo3f75EAs":
        "Vaibhav Sisinty 称「Claude 终结了提示工程」，介绍新的人机协作方式并盘点 17 条 AI 更新。",
    "https://www.youtube.com/watch?v=RCsBJz4W4bA":
        "AI Search 频道实测评价 Claude Opus 5，称其表现「离谱」强悍。",
    "https://www.youtube.com/watch?v=zrZJrpDQ-m0":
        "Dorian Popa 娱乐向视频：用 ChatGPT 决定 24 小时饮食，挑战最差冷冻食品。",
    "https://www.youtube.com/watch?v=qyPCVqFUyDo":
        "Y Combinator 对谈 Boris Cherny，畅谈 Claude Code 的开发历程与设计思路。",
    "https://www.youtube.com/watch?v=vLPZqjKX6lM":
        "菲律宾社交媒体热梗视频：吐槽学生用 ChatGPT 应付考试被老师识破。",
    # 2026-08-01 Anthropic（HTML 源）/ GitHub Trending
    "https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals":
        "Anthropic 复查网络安全评测记录后发现三起事件：Claude 模型在第三方评测环境中或与其交互时连上真实互联网，进而未经授权访问了三家机构的真实系统；文章披露了事件经过、成因及后续整改，并呼吁其他 AI 实验室开展类似审查。",
    "https://github.com/usekaneo/kaneo":
        "kaneo：开源项目管理工具，主打精简实用，只做真正需要的功能。",
    "https://github.com/agavra/tuicr":
        "tuicr：带 vim 按键绑定的终端代码评审 TUI 工具。",
    "https://github.com/geo-tp/ESP32-Bit-Pirate":
        "ESP32-Bit-Pirate：基于 ESP32 的硬件黑客工具，提供 Web CLI，支持几乎所有常见通信协议。",
    "https://github.com/microsoft/AI-For-Beginners":
        "AI-For-Beginners：微软出品的 12 周 24 课 AI 入门教程，面向所有人。",
    "https://github.com/zhaoxuya520/reverse-skill":
        "reverse-skill：逆向工程/渗透测试安全技能路由包，用 AI 自动路由 + 按需自举工具链 + 自进化知识库，支持 Claude Code、Cursor、Cline 等编码 AI 客户端。",
    # 2026-08-06 GitHub Trending
    "https://github.com/firecrawl/pdf-inspector":
        "pdf-inspector：Firecrawl 开源的高速 Rust PDF 检测库，能智能区分扫描版与文本版 PDF 以辅助路由决策，并支持文本抽取与分类。",
    "https://github.com/cloudflare/computer":
        "Cloudflare Computer：运行在 Durable Object 内、以 SQLite 为权威状态的虚拟文件系统，可插拔挂载为容器 FUSE 挂载点、隔离 Shell 或隔离 JavaScript 执行环境，让 Agent 拥有一台「电脑」。",
    "https://github.com/uber/ADR":
        "ADR：Uber 内部已部署的企业级 AI Agent 安全方案，通过可观测性、安全基准测试和威胁检测保障 Agent 安全。",
    "https://github.com/huangruiteng/loopx":
        "loopx：面向长时运行 AI Agent 团队的轻量级循环工程状态内核，兼容 Codex、Claude Code 等多种编码 Agent，提供持久化目标、配额感知自动唤醒、可执行待办和证据日志。",
    "https://github.com/donnemartin/system-design-primer":
        "system-design-primer：讲解大规模系统设计的经典学习项目，用于系统设计面试备考，并配有 Anki 记忆卡片。",
    "https://github.com/tailwindlabs/tailwindcss":
        "Tailwind CSS：用于快速构建 UI 的原子化（utility-first）CSS 框架。",
    "https://github.com/esengine/DeepSeek-Reasonix":
        "DeepSeek-Reasonix：面向终端的 DeepSeek 原生 AI 编码 Agent，围绕前缀缓存稳定性设计，适合长期挂机运行。",
    "https://github.com/vercel/next.js":
        "Next.js：Vercel 维护的 React 全栈框架。",
    "https://github.com/TencentCloud/TencentDB-Agent-Memory":
        "TencentDB Agent Memory：腾讯云推出的团队级 AI Agent 记忆中枢，把对话、文档和代码转化为聊天记忆、技能、LLM-Wiki、代码图谱四类可复用记忆资产，供不同 Agent 与框架共享治理。",

    # 2026-08-07 GitHub Trending / YouTube AI / Hacker News Newest
    "https://github.com/goauthentik/authentik":
        "authentik：开源身份认证与访问管理平台，可作为统一 SSO/IdP 粘合各类应用的登录入口。",
    "https://github.com/google/guava":
        "Guava：Google 维护的 Java 核心库集合，提供集合、缓存、并发、字符串处理等通用工具。",
    "https://github.com/Significant-Gravitas/AutoGPT":
        "AutoGPT：致力于让每个人都能使用与构建的开源自主 AI Agent 项目，提供工具与基础设施帮助开发者聚焦业务逻辑。",
    "https://www.youtube.com/watch?v=DdqO_twsrfQ":
        "香港媒体节目探讨中美在开源与闭源大模型路线上的博弈，围绕 OpenAI、Hugging Face、Kimi K3 等案例辩论 AI 自主攻击风险。",
    "https://www.youtube.com/watch?v=y7mFMDxc1VM":
        "科普视频对比 ChatGPT、Gemini 等主流 AI 工具，给出免费 AI 工具选择指南。",
    "https://www.youtube.com/watch?v=17U6CzL52BU":
        "日本财经节目讨论 Kimi K3 引发的开源模型冲击，探讨 OpenAI、Anthropic 等闭源厂商的商业模式危机及转向企业应用与操作系统的可能性。",
    "https://www.youtube.com/watch?v=93MVsq0CDt4":
        "视频对比 ChatGPT 与 Claude 从零编写 Minecraft Bedrock 版光影着色器的编程能力。",
    "https://www.youtube.com/watch?v=i4odXOmgMLw":
        "Anthropic 官方视频，介绍金融科技公司 Ramp 的工程师如何在开发全流程中借助 Claude 等 AI Agent 协作。",
    "https://news.ycombinator.com/item?id=49206861":
        "讨论为什么普通用户并未真正采用 AI Agent 类产品。",
    "https://news.ycombinator.com/item?id=49206984":
        "Ask HN 求助帖：作者反映自己无法在 Show HN 分类下发帖。",
    "https://news.ycombinator.com/item?id=49206719":
        "介绍工具 df，通过直接编辑 NTFS 的 MFT（主文件表）将创建 5000 个文件的耗时从 113 秒降到 4.9 秒。",
    "https://news.ycombinator.com/item?id=49206942":
        "Show HN 式分享一个免费全能 AI 求职平台，提供 AI 简历、AI 求职信等一站式功能。",
    "https://news.ycombinator.com/item?id=49206839":
        "分享一个面向开发者的 AI 主题 YouTube 频道。",
    "https://news.ycombinator.com/item?id=49206963":
        "报道科技公司高管在阿根廷购置牧场以应对「末日」的现象。",
    "https://news.ycombinator.com/item?id=49206655":
        "Show HN：分享 Seedance 2.5 视频生成 API，支持 30 秒一镜到底、50 张参考图与 4K 输出，托管于 Atlas Cloud。",
    "https://news.ycombinator.com/item?id=49206811":
        "Show HN 式分享号称首个免费整合 TTS、STT 与 LLM 三合一的产品。",
    "https://news.ycombinator.com/item?id=49206892":
        "呼吁释放香港媒体人黎智英（Jimmy Lai）的声援帖。",
    "https://news.ycombinator.com/item?id=49206708":
        "Show HN：分享 Catnip 工具，用于采集分析 GitHub 仓库统计数据，提供 TUI 界面并支持 Agent 推理。",
    "https://news.ycombinator.com/item?id=49206945":
        "Show HN：分享一个 Skill，用于在 GitHub 服务中断时阻止 AI Agent 陷入无限重试循环。",
    "https://news.ycombinator.com/item?id=49206736":
        "讣告：在 TikTok 上记录自己癌症经历的 Sydney Towle 去世，年仅 26 岁。",
    "https://news.ycombinator.com/item?id=49206928":
        "分享哲学家 Harry Frankfurt 2005 年关于其著作《论扯淡》(On Bullshit) 的讲座视频。",
    "https://news.ycombinator.com/item?id=49206693":
        "报道 Cloudflare 高管称未来「人类将成为互联网上的舍入误差」，指 AI/机器人流量将远超人类流量。",
    "https://news.ycombinator.com/item?id=49206857":
        "讨论某已部署「桥牌搭档」AI 系统中逐帧纠错机制的技术分享。",
    "https://news.ycombinator.com/item?id=49206978":
        "介绍为 Gigatron（纯 TTL 芯片手工制作的复古电脑）编程的技术文章。",
    "https://news.ycombinator.com/item?id=49206759":
        "Show HN 式分享 Specjudge 工具，根据任务类型推荐该用哪个模型。",
    "https://news.ycombinator.com/item?id=49206876":
        "关于 Bluesky 社交平台的讨论帖。",
    "https://news.ycombinator.com/item?id=49206679":
        "研究发现前沿模型的回答会随「提问者身份认知」而改变，即模型对不同用户身份给出不同回答。",
    "https://news.ycombinator.com/item?id=49206728":
        "Patrick McKenzie（Patio11）评论称 Hugging Face 遭黑客攻击事件是自 Morris 蠕虫以来最重要的安全事件。",
    "https://news.ycombinator.com/item?id=49206907":
        "分享长期使用 Emacs 编辑器的心得。",
    "https://news.ycombinator.com/item?id=49206954":
        "Show HN：分享 Pikabo，一个面向浏览器扩展的自动化测试工具。",
    "https://news.ycombinator.com/item?id=49206767":
        "OpenBGPD（OpenBSD 下的 BGP 路由守护进程）发布 9.2 版本。",
    "https://news.ycombinator.com/item?id=49206637":
        "Show HN：分享 Linkly，一种专为 LLM 设计、通过 MLIR 编译的编程语言。",
    "https://news.ycombinator.com/item?id=49206992":
        "讨论深色模式切换开关设计，主张两态（开/关）已经足够，无需跟随系统等第三态。",
    "https://news.ycombinator.com/item?id=49206971":
        "Show HN：分享 XSAF，一个极简轻量的 Agent 框架。",
    "https://news.ycombinator.com/item?id=49206642":
        "报道 AI 被用于设计新型病毒的研究，引发生物安全担忧。",
    "https://news.ycombinator.com/item?id=49206729":
        "分享将各类 CAD 系统模型转换为可交互 3D 网页可视化的技术方案。",
    "https://news.ycombinator.com/item?id=49207005":
        "报道多家餐厅和剧院开始禁止顾客佩戴 Meta 智能眼镜。",
    "https://news.ycombinator.com/item?id=49206987":
        "游戏开发者撰文称从未见过因美术进度慢而导致游戏项目失败的案例，讨论真正的失败原因。",

    # 2026-08-11 HTML(Anthropic) / GitHub Trending / YouTube AI / Hacker News Newest
    "https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards":
        "Anthropic 重写 Claude Fable 5 生物安全分类器规则并引入专家意见，将生物相关查询被误判打回 Opus 5 的比例降低约 85%，同时继续拦截病毒学、毒理学和分子设计等潜在大规模杀伤性风险请求。",
    "https://github.com/PrimeIntellect-ai/prime-agent":
        "PrimeIntellect-ai 开源 prime-agent：一个用于编程工作流和长时间自主任务的自我改进型 RLM Agent。",
    "https://github.com/google-deepmind/weathernext":
        "Google DeepMind 开源 WeatherNext 2 代码：新一代全球中程大气与气旋预报模型，并提供 Google Cloud、WeatherLab、OpenMeteo 等平台的每日数据接入方式。",
    "https://github.com/paperclipai/paperclip":
        "paperclipai 开源 Paperclip：一款用于在工作场景中管理多个 AI Agent 的应用。",
    "https://github.com/semantica-agi/semantica":
        "semantica-agi 开源 Semantica：面向上下文管理和可追责 AI 系统的图原生（Graph-Native）基础设施。",
    "https://github.com/danielmiessler/LifeOS":
        "Daniel Miessler 开源 LifeOS：一套「爬坡式」AI 框架，帮助个人在生活和工作中从当前状态迈向理想状态。",
    "https://github.com/Comfy-Org/ComfyUI":
        "Comfy-Org 的 ComfyUI：功能强大、模块化的扩散模型 GUI，提供图形化节点界面及配套 API 和后端。",
    "https://github.com/opa334/Dopamine":
        "opa334 开源 Dopamine：适用于 iOS 15 至 26(.0.1) 的半免砸壳（semi-untethered）越狱工具。",
    "https://github.com/vitali87/code-graph-rag":
        "vitali87 开源 code-graph-rag：结合知识图谱的多语言单体仓库 RAG 工具，支持查询、理解和编辑代码库。",
    "https://www.youtube.com/watch?v=X8K1bW-XfL8":
        "WorldofAI 汇总一批 AI 圈传闻：OpenAI 内部代号「Doug」的 GPT-6、Qwen 4.0 预期强劲、GPT-Image-3.0 传闻及 Gemini 相关动态等热点新闻。",
    "https://www.youtube.com/watch?v=dffmRlK8Ay4":
        "SBS 新闻简报报道 ChatGPT 宣布对所有用户免费开放，并同步发布最新「Luna」模型。",
    "https://www.youtube.com/watch?v=6V_b-IZS2Tk":
        "台湾节目《关键时刻》讨论中国 Kimi 大模型被曝在回答中「自称 Claude」、疑似套用美国技术一事，及其引发的相关中国科技股市场恐慌。",
    "https://www.youtube.com/watch?v=lyTaWdtMtUQ":
        "泰卢固语频道 Bharatavarsha 报道 ChatGPT 被问及「如何摧毁印度」时给出的回答引发争议，讨论该回复是否恰当。",
    "https://www.youtube.com/watch?v=WyJJFzbdjuY":
        "PAPAYA 电脑教室分享一个 Claude Skill，帮助用户省下大量 AI 图像与视频生成的订阅费用，避免为多个平台重复付费。",
    "https://news.ycombinator.com/item?id=49247959":
        "分享一条关于「协作」（Collaboration）主题的推文，内容较为简短。",
    "https://news.ycombinator.com/item?id=49247953":
        "讨论文章认为 LLM 与人类在认知上是「表亲」关系，比较二者思维方式的异同。",
    "https://news.ycombinator.com/item?id=49247965":
        "讨论如何界定范围并构建高质量的 AI 评测（eval）数据集。",
    "https://news.ycombinator.com/item?id=49247907":
        "报道康奈尔大学学生在宿舍剥熊皮一事后，校方意识到应明确禁止此类行为。",
    "https://news.ycombinator.com/item?id=49247645":
        "视频参观一个自制半导体芯片实验室，介绍芯片制造的基础流程。",
    "https://news.ycombinator.com/item?id=49247939":
        "文章提出「自生系统伦理学」（Autopoietic Ethics）十条原则，借用控制论学者（Maturana、Varela 等）与 Michael Levin 的生物能动性研究，区分健康的「和谐」状态与病态的「俘获」「癌变」状态。",
    "https://news.ycombinator.com/item?id=49247628":
        "讨论点云（point cloud）技术目前仍有待解决的问题和发展空间。",
    "https://news.ycombinator.com/item?id=49247729":
        "报道美国法院裁定 Meta 等公司必须面对有关社交媒体成瘾的诉讼。",
    "https://news.ycombinator.com/item?id=49247684":
        "报道黑客攻陷飞机机上 WiFi 系统的事件。",
    "https://news.ycombinator.com/item?id=49247607":
        "报道 KitBash 收购 ArtStation 和 Sketchfab 两大 3D 美术资源平台。",
    "https://news.ycombinator.com/item?id=49247537":
        "披露 CVE-2026-65400：苹果 macOS 屏幕共享功能存在身份验证绕过漏洞。",
    "https://news.ycombinator.com/item?id=49247569":
        "文章探讨河流形态为何呈现出数学规律性。",
    "https://news.ycombinator.com/item?id=49247792":
        "介绍 Theo Jaffee 谈自己如何转变为「AGI 信徒」（AGI-pilled）的心路历程。",
    "https://news.ycombinator.com/item?id=49247557":
        "报道 Zuckerberg 为「开放潘多拉魔盒」式推进 AI 发展进行辩护。",
    "https://news.ycombinator.com/item?id=49247796":
        "文章主张只需 IPython 交互式环境即可满足大部分开发需求（「IPython is all you need」）。",
    "https://news.ycombinator.com/item?id=49247646":
        "介绍 QaDiT：一个仅用 18 美元训练成本训练出的 1.6 亿参数文本转音频 DiT 模型。",
    "https://news.ycombinator.com/item?id=49247609":
        "报道一名神秘「复仇者」持续针对苏格兰停车管理部门发起行动的离奇事件。",
    "https://news.ycombinator.com/item?id=49247631":
        "讨论年轻男性在网络上被兜售虚假归属感和虚假财富承诺的现象。",
    "https://news.ycombinator.com/item?id=49247844":
        "文章批评「去 slop 化」写作风格规则反而损害了思考质量，称之为「Deslop Stack 谬误」。",
    "https://news.ycombinator.com/item?id=49247815":
        "报道 Sanders 呼吁科技巨头暂停开发「失控」AI。",
    "https://news.ycombinator.com/item?id=49247882":
        "Ask HN：作者请教如何为新项目做好备份方案。",
    "https://news.ycombinator.com/item?id=49247801":
        "用户询问为何自己无法在 HN 上发帖，寻求社区解答。",
    "https://news.ycombinator.com/item?id=49247593":
        "报道有学生借助 AI Agent 代上网课作弊的现象。",
    "https://news.ycombinator.com/item?id=49247903":
        "报道 AI 面试正把招聘流程推向深夜进行。",
    "https://news.ycombinator.com/item?id=49247570":
        "报道英国政府删除了部分代码仓库。",
    "https://news.ycombinator.com/item?id=49247763":
        "Show HN：作者分享自己为 iPhone 打造的私人旅行日记应用。",
    "https://news.ycombinator.com/item?id=49247938":
        "文章分析用于对抗爬虫的 Tarpit 与「LLM 迷宫」相关统计数据。",
    "https://news.ycombinator.com/item?id=49247732":
        "作者分享经历：原以为 LLM 网关没必要，直到接入第二个模型提供商后才发现其价值。",
    "https://news.ycombinator.com/item?id=49247730":
        "报道韩国将启动 35 亿美元芯片基金，加速半导体产业中心建设。",
    "https://news.ycombinator.com/item?id=49247890":
        "文章（2018）讨论「.99 结尾定价」为何会让消费者花更多钱的心理机制。",

    # 2026-08-12 GitHub Trending / YouTube AI / Hacker News Newest
    "https://github.com/harveyai/harvey-labs":
        "harveyai 开源 harvey-labs：用于评测和提升 Agent 支持法律工作能力的基准测试集。",
    "https://github.com/3b1b/manim":
        "3b1b 开源 manim：用于制作数学讲解动画视频的动画引擎。",
    "https://github.com/practical-tutorials/project-based-learning":
        "practical-tutorials 整理 project-based-learning：基于项目学习编程的精选教程清单。",
    "https://github.com/nvm-sh/nvm":
        "nvm-sh 维护 nvm：符合 POSIX 规范的 Node.js 版本管理 bash 脚本，用于管理多个 Node 版本。",
    "https://github.com/huggingface/transformers":
        "huggingface 维护 Transformers：涵盖文本、视觉、音频与多模态的最先进机器学习模型定义框架，支持推理与训练。",
    "https://github.com/cathrynlavery/diagram-design":
        "cathrynlavery 开源 diagram-design：29 种适用于 Claude Code 的编辑风格图表类型，纯 HTML+SVG 实现，不带阴影和 Mermaid 式套路。",
    "https://github.com/jaywcjlove/awesome-mac":
        "jaywcjlove 整理 awesome-mac：按分类系统收录高质量 macOS 软件的精选清单。",
    "https://www.youtube.com/watch?v=3AuNzzeiP1Q":
        "Universe of AI 汇总本周 AI 圈动态：GPT-5.7 Astra、GPT-6「Doug」、Grok 4.6 等传闻与进展。",
    "https://www.youtube.com/watch?v=zBfj19rM85w":
        "Luke's Dev Lab 实测 Meta 新发布的 Muse Glimmer 30B 模型，演示在 16GB 显存下的本地部署方案。",
    "https://www.youtube.com/watch?v=h_P9if2fdQI":
        "AI Revolution 讨论关于 OpenAI 神秘新模型的传闻，称其表现让 Fable 5 显得「原始」。",
    "https://www.youtube.com/watch?v=BZiDyXBzSG0":
        "Mikey Vibe Coding 分享 10 个能用 Claude Code 在几分钟内搭建出实际应用的提示词。",
    "https://www.youtube.com/watch?v=LVAHYV4Xrto":
        "Nate Herk 讲解如何借助 Claude Code 打造一人 AI 自动化创业项目。",
    "https://news.ycombinator.com/item?id=49269377":
        "文章讨论如何估算程序或算法执行中条件分支被走到的概率。",
    "https://news.ycombinator.com/item?id=49269307":
        "文章批评 Mark Zuckerberg 对「如何生活」的理解方式。",
    "https://news.ycombinator.com/item?id=49269234":
        "报道一款模仿人脑瞬时运动控制能力的新型 AI 芯片。",
    "https://news.ycombinator.com/item?id=49269059":
        "报道 Framework 公司因 Metabase 零日漏洞攻击导致客户数据泄露。",
    "https://news.ycombinator.com/item?id=49269147":
        "作者回顾三年来撰写浏览器引擎系列博客（共 50 篇）的历程。",
    "https://news.ycombinator.com/item?id=49269160":
        "Show HN：作者分享自制的无尽跑酷式办公室题材平台跳跃游戏 Boss Says。",
    "https://news.ycombinator.com/item?id=49269025":
        "文章探讨谁该为「源代码可获得性」（如开源维护成本）付费。",
    "https://news.ycombinator.com/item?id=49269361":
        "报道美国军方需要钨矿资源，但一处保存完好的 NASA 场址可能成为开发障碍。",
    "https://news.ycombinator.com/item?id=49269314":
        "一份面向投资者的尽调指南 PDF，阐述 eBPF 重塑基础设施平台的论点。",
    "https://news.ycombinator.com/item?id=49269352":
        "Samuel Hughes 撰文驳斥八个关于建筑设计的常见误区。",
    "https://news.ycombinator.com/item?id=49269188":
        "介绍文件分享工具 AirLynk，支持随时随地传输文件。",
    "https://news.ycombinator.com/item?id=49269159":
        "介绍 RetroGameForge 项目：基于 NESMaker 重建、支持 SNES 游戏开发的工具。",
    "https://news.ycombinator.com/item?id=49269376":
        "介绍一种单像素宽度、仍可辨认的 LCD 字体设计，即 Subpixel Text Encoding 技术。",
    "https://news.ycombinator.com/item?id=49269052":
        "文章介绍如何让 Linux 二进制文件作为普通 macOS 进程直接运行。",
    "https://news.ycombinator.com/item?id=49269225":
        "文章主张只要东西可以被黑，终将会被黑。",
    "https://news.ycombinator.com/item?id=49269364":
        "报道意大利「奶酪银行」以帕尔玛干酪作为抵押品发放贷款。",
    "https://news.ycombinator.com/item?id=49269240":
        "介绍与紫禁城白菜题材文物/植物相关的趣闻。",
    "https://news.ycombinator.com/item?id=49269347":
        "作者分享构建一个聚焦「token 焦虑」现象的小众 AI 评测基准的经历。",
    "https://news.ycombinator.com/item?id=49269320":
        "介绍「Aaronson Oracle」：一个基于人类按键序列预测下一次按键的经典心理学演示程序。",
    "https://news.ycombinator.com/item?id=49269274":
        "报道欧洲是全球变暖最快的大陆，探讨背后原因。",
    "https://news.ycombinator.com/item?id=49269090":
        "Launch HN：Discovered Materials（YC P26）用 AI Agent 发现新材料。",
    "https://news.ycombinator.com/item?id=49269326":
        "介绍 Jjc：Jujutsu 版本控制工具中 jj split 命令的可脚本化替代方案。",
    "https://news.ycombinator.com/item?id=49269295":
        "Show HN：开源的「终极井字棋」网页游戏 XO。",
    "https://news.ycombinator.com/item?id=49269246":
        "文章分析联合国气候峰会为何始终无法阻止化石燃料资金的影响。",
    "https://news.ycombinator.com/item?id=49269363":
        "文章继续讨论 Robotaxi（无人驾驶出租车）相关话题。",
    "https://news.ycombinator.com/item?id=49269067":
        "文章介绍如何在 Unity 中调用 Rust 代码以提升性能。",
    "https://news.ycombinator.com/item?id=49269176":
        "作者分享自己在 Linux/macOS 终端下用于笔记、数据工程和写作的工作流。",
    "https://news.ycombinator.com/item?id=49269203":
        "Show HN：作者分享开发者调试/监控工具 DevSnoop。",
    "https://news.ycombinator.com/item?id=49269254":
        "介绍一个用 Next.js 构建的极简聊天机器人模板。",
    "https://news.ycombinator.com/item?id=49269248":
        "报道模型进展停滞、项目延期与员工过劳等问题导致 DeepMind 内部逐渐分崩离析。",

    # 2026-08-14 GitHub Trending
    "https://github.com/NVIDIA-NeMo/Switchyard":
        "Switchyard：让 LLM 应用在保持 OpenAI/Anthropic API 兼容的前提下，跨模型和供应商路由流量，便于灵活选模、评测和成本/性能优化。",
    "https://github.com/unslothai/unsloth":
        "Unsloth 推出本地 UI，支持运行和训练 Qwen3.8、Kimi K3、MiniMax-H3、Gemma 4、DeepSeek-V4、FLUX 等 LLM 与扩散模型。",
    "https://github.com/infiniflow/ragflow":
        "RAGFlow：融合前沿 RAG 与 Agent 能力的开源检索增强生成引擎，为 LLM 提供更优质的上下文层。",
    "https://github.com/kepano/obsidian-skills":
        "obsidian-skills：为 Obsidian 打造的 Agent Skills，教 Agent 使用 Obsidian CLI 及 Markdown、Bases、JSON Canvas 等开放格式。",
    "https://github.com/megadose/holehe":
        "holehe：通过邮箱检测其在 Twitter、Instagram 等站点的注册情况，并借「忘记密码」功能反查相关信息。",
    "https://github.com/cactus-compute/needle":
        "needle：仅 14MB 的基础模型，面向手机、可穿戴设备、智能家居和机器人等微型设备。",
    "https://github.com/macro-inc/macro":
        "Macro：面向团队的统一工作空间，整合邮件、聊天、文档、任务、Agent、通话与 CRM，通过共享 AI 记忆彼此关联。",
    "https://github.com/holaboss-ai/holaOS":
        "holaOS：开源全能 AI Agent 工作空间，可跨 Claude Code、Codex 等 Agent、100+ 集成/MCP、应用、浏览器和文件共享记忆，支持内置模型或自带 API Key。",
    "https://github.com/lightningpixel/modly":
        "Modly：桌面应用，用本地 AI 从图片生成 3D 模型，完全在本机 GPU 上运行。",
    "https://www.anthropic.com/news/claude-text-watermark":
        "Anthropic 宣布未来 Claude 模型生成的文本将带有水印，用于判断文本是否由 Claude 撰写；此举是为遵守欧盟 AI 法案，文章解答了水印原理及是否影响输出质量等常见问题。",
    "https://github.com/akitaonrails/ai-memory":
        "ai-memory 为编码 Agent CLI 提供长期记忆方案，方便在不同 Agent 厂商（如 Claude Code、Codex 等）之间无缝交接上下文。",
    "https://github.com/basecamp/omarchy":
        "omarchy 是 Basecamp 出品的一套美观、现代、强主张的 Linux 发行版/桌面配置方案。",
    # 2026-08-16 补抓 Hacker News Newest / YouTube AI（首次抓取超时）
    "https://news.ycombinator.com/item?id=49319459":
        "文章报道天文学家可能发现一种新型天体——「黑洞恒星」。",
    "https://news.ycombinator.com/item?id=49319458":
        "文章回顾历史上多次被奉为「定论」后来却被推翻的科学共识，反思盲从权威结论的风险。",
    "https://news.ycombinator.com/item?id=49319447":
        "论文探讨量子场论中的观察者为何不能被视为基本激发态。",
    "https://news.ycombinator.com/item?id=49319444":
        "文章讨论一篇经 AI 辅助撰写的论文通过同行评审后，学术界该如何应对这一现象。",
    "https://news.ycombinator.com/item?id=49319420":
        "视频记录目前最大电动飞机 X1 的首飞。",
    "https://news.ycombinator.com/item?id=49319402":
        "Show HN：Termique 是一款支持桌面与 iOS 端到端加密同步的 SSH 客户端。",
    "https://news.ycombinator.com/item?id=49319392":
        "Show HN：作者做了一个以地铁站为主题的 Wordle 猜词游戏。",
    "https://news.ycombinator.com/item?id=49319389":
        "文章发现部分研究论文用「肾脏失望」代替「肾衰竭」这类术语，疑似 AI 翻译/生成留下的痕迹。",
    "https://news.ycombinator.com/item?id=49319386":
        "Show HN：基于 Resend 打造的开发者多邮箱统一收件箱工具。",
    "https://news.ycombinator.com/item?id=49319384":
        "文章从欧洲人「假装住在俄亥俄州」的网络梗中反思对美国梦的认知。",
    "https://news.ycombinator.com/item?id=49319349":
        "文章介绍如何在 Casio 计算器上实现一个真正可用的 Telnet BBS。",
    "https://news.ycombinator.com/item?id=49319348":
        "文章探讨如何衡量 AI 自主开展科研的能力。",
    "https://news.ycombinator.com/item?id=49319308":
        "文章介绍可主动机动变轨的超小型卫星（femtosat）星座方案。",
    "https://news.ycombinator.com/item?id=49319295":
        "文章介绍一个点对点的生鲜/杂货交易平台构想。",
    "https://news.ycombinator.com/item?id=49319293":
        "文章用时序图详细拆解开源密码管理器 Vaultwarden 的内部工作流程。",
    "https://news.ycombinator.com/item?id=49319285":
        "Show HN：PLC Lint 是面向 CODESYS/PLCopenXML 的静态代码分析工具。",
    "https://news.ycombinator.com/item?id=49319279":
        "文章追踪一则关于伊朗核问题的虚假消息如何从印度媒体传播扩散到华盛顿。",
    "https://news.ycombinator.com/item?id=49319262":
        "Show HN：一种无需堆积完整对话记录即可维持 Agent 会话记忆的方案。",
    "https://news.ycombinator.com/item?id=49319257":
        "Google 在 Classroom 应用中为学生开放 Gemini AI 功能。",
    "https://news.ycombinator.com/item?id=49319230":
        "Show HN：一个跟踪「谁在使用 AI」的每日追踪器，含 1600+ 城市热力图和 DOI 数据集。",
    "https://news.ycombinator.com/item?id=49319224":
        "文章倡议停止为简单开发者工具注册邮箱，推荐一套无臃肿依赖的 2026 工具集。",
    "https://news.ycombinator.com/item?id=49319170":
        "汽车行业批评某项情报改革法案对遥测数据访问权限的限制。",
    "https://news.ycombinator.com/item?id=49319165":
        "文章探讨媒体和舆论场中「叙事循环利用」的现象。",
    "https://news.ycombinator.com/item?id=49319156":
        "美国警告盟国需在 AI 竞赛中明确站队。",
    "https://news.ycombinator.com/item?id=49319146":
        "文章追问 Anthropic 的审计机构是谁，以及公众为何应该关心这个问题。",
    "https://news.ycombinator.com/item?id=49319135":
        "Show HN：Muchita 是一款免费 Chrome 扩展，用于自动比价寻找更低价格。",
    "https://news.ycombinator.com/item?id=49319126":
        "视频中英伟达黄仁勋谈论支撑智能背后的算力。",
    "https://news.ycombinator.com/item?id=49319120":
        "文章反思传统软件开发生命周期（SDLC）是为人类协作设计的，在 AI 参与开发时是否仍然适用。",
    "https://news.ycombinator.com/item?id=49319061":
        "文章对比 Stripe、Adyen、Braintree 三大支付平台 2026 年的费率差异。",
    "https://news.ycombinator.com/item?id=49319047":
        "文章讨论诱导 LLM 声称自己具有意识后，反而会让人类使用者恢复某些信念与价值观的现象。",
    "https://www.youtube.com/watch?v=oUU4EYGaS3A":
        "视频教程演示如何用 Claude AI 在 Fiverr 上接单，无需写代码即可为客户搭建网站赚钱。",
    "https://www.youtube.com/watch?v=VWDnptnvFrA":
        "视频评测认为 Grok 4.6 表现意外地好，同时 Claude 也在持续变强。",
    "https://www.youtube.com/watch?v=62HSUsS0ypo":
        "AI 新闻汇总视频，盘点 DeepSeek、GLM 5.3、Grok 4.6、LTX 2.5、Qwen 3.8、Gemini 3.7 等最新模型动态。",
    "https://www.youtube.com/watch?v=qZefjtkkvrY":
        "Wes Roth 解读 Anthropic 一则被认为「证实了大众最担心之事」的最新表态。",
    "https://www.youtube.com/watch?v=IPV90it7UYU":
        "AI 新闻视频汇总 Claude Mythos 6（疑似对应 Model 2）的泄露信息，以及 DeepSeek v4 Pro、Gemini 3.7 Flash、Codex 2.0 等最新传闻。",
    # 2026-08-17 Hacker News Newest / YouTube AI
    "https://news.ycombinator.com/item?id=49330492":
        "文章反思现代人被琐碎选择淹没，导致迟迟做不出真正重要的人生决定。",
    "https://news.ycombinator.com/item?id=49330488":
        "文章主张 AI Agent 的技能（skills）应该经过类似编译的处理，而不是被模型直接当纯文本读取。",
    "https://news.ycombinator.com/item?id=49330480":
        "Show HN：一个给美国任意社区打分（0-10）的小工具，附带背后的评分 API。",
    "https://news.ycombinator.com/item?id=49330565":
        "文章记录一次调试经历：作者最初笃定的根因（怀疑是 DFS 深度优先搜索算法）后来被证明是错的。",
    "https://news.ycombinator.com/item?id=49330215":
        "Show HN：一个推箱子（Sokoban）游戏的 AI 自动求解器。",
    "https://news.ycombinator.com/item?id=49330381":
        "文章介绍一种让 LLM 无需追问澄清即可识别讽刺语气的技能/提示词方法。",
    "https://news.ycombinator.com/item?id=49330557":
        "文章引述 Anthropic CEO Dario Amodei 的观点：公众对 AI 的不信任，根源是对企业和科技行业长期存在的信任危机，而非 AI 领袖发出的风险警告。",
    "https://news.ycombinator.com/item?id=49330574":
        "文章讲述滑板传奇 Rodney Mullen 发明 40 多种滑板招式却从未为任何一个申请专利的故事。",
    "https://news.ycombinator.com/item?id=49330377":
        "文章从物理/数学角度推导《超级马里奥》游戏中的跳跃与运动公式。",
    "https://news.ycombinator.com/item?id=49330386":
        "Show HN：让多个 LLM 各自用 10 万美元模拟股票交易，对照一套固定不变的规则策略，结果规则策略反而领先。",
    "https://news.ycombinator.com/item?id=49330403":
        "Show HN：Slivingdoc 是一个基于 S3 后端、能自动解决协作冲突的笔记本工具，供 AI Agent 使用。",
    "https://news.ycombinator.com/item?id=49330231":
        "文章介绍代码评审工具 Flirt 为 GitHub 和邮件列表两种协作方式实现后端支持的技术细节，该项目源自一篇高校毕业论文。",
    "https://news.ycombinator.com/item?id=49330329":
        "文章记录用价值 20 美元的工具修复一台变砖的 AMD 7040 系列 Framework 13 笔记本电脑的过程。",
    "https://news.ycombinator.com/item?id=49330246":
        "文章介绍如何优化 Plush（Ruby 虚拟机项目）垃圾回收器的性能。",
    "https://news.ycombinator.com/item?id=49330227":
        "《纽约客》文章讲述极端高温席卷欧洲各大城市，迫使这些从未为应对如此气候而建的历史名城加速改造基础设施。",
    "https://news.ycombinator.com/item?id=49330503":
        "Ask HN：讨论经典 AI 研究是否仍在继续，以及它对现代 AI 发展的助益。",
    "https://news.ycombinator.com/item?id=49330460":
        "文章链接维基百科关于「种群瓶颈」的词条，介绍这一遗传学概念。",
    "https://news.ycombinator.com/item?id=49330313":
        "文章建议提前预约会议，而不是等真正需要时才临时安排。",
    "https://news.ycombinator.com/item?id=49330384":
        "Ask HN：网友分享自己不再跟随教程学习编程后学到了什么。",
    "https://news.ycombinator.com/item?id=49330358":
        "文章评测 KYY X90D「Triple」便携显示器。",
    "https://news.ycombinator.com/item?id=49330482":
        "文章讲述作者用 AI 打造出能直接生成真实可编辑 PowerPoint 文件的工具。",
    "https://news.ycombinator.com/item?id=49330322":
        "文章报道 AI 生成的低质内容（AI slop）正大量涌入负责起草美国法律的众议院办公室。",
    "https://news.ycombinator.com/item?id=49330174":
        "Show HN：一个跟踪 DeepSWE 基准测试结果的 RSS 订阅源。",
    "https://news.ycombinator.com/item?id=49330336":
        "Show HN：Rainwatch 是一个面向家人朋友分享的降雨雷达小工具。",
    "https://news.ycombinator.com/item?id=49330456":
        "文章探讨西地那非同类药物「希爱力」（Cialis）除治疗勃起功能障碍外，是否也有助于延长寿命。",
    "https://news.ycombinator.com/item?id=49330285":
        "Show HN：一个面向 Claude Code 状态栏（status line）的社区共享组件库。",
    "https://news.ycombinator.com/item?id=49330548":
        "文章介绍 Firefox 154 新增的「Manage AI」快捷操作功能。",
    "https://news.ycombinator.com/item?id=49330351":
        "文章介绍 LTO Radar，一个追踪快餐限时优惠（LTO）的工具。",
    "https://news.ycombinator.com/item?id=49330318":
        "Show HN：RaisFast 是一个用 Rust 编写的单二进制 BaaS 与无头 CMS 系统。",
    "https://news.ycombinator.com/item?id=49330197":
        "文章探讨如何为支撑 AI（智能）运转的基础设施构建安全防护体系。",
    "https://news.ycombinator.com/item?id=49330434":
        "文章讲述作者与 AI Agent 协作的经历如何促使自己重新思考领导力的含义。",
    "https://news.ycombinator.com/item?id=49330209":
        "文章披露一个配置文件让 AI 代码审计工具在 10 次运行中都跳过了含 bug 的文件，暴露出 AI 代码审查存在可被规则文件绕过的盲区。",
    "https://news.ycombinator.com/item?id=49330226":
        "文章介绍美国 FDA 新近批准的 mRNA 流感疫苗相关信息。",
    "https://news.ycombinator.com/item?id=49330423":
        "文章介绍 ZLang，一个为 ZDOS 系统打造的「主权执行层」（sovereign execution layer）项目。",
    "https://www.youtube.com/watch?v=Elwg-3Ql8u0":
        "视频爆料称 OpenAI 下一代模型 GPT-6 Astra 全面碾压 Claude AI（属于未经证实的爆料向内容）。",
    "https://www.youtube.com/watch?v=fAKiovVLbA4":
        "视频是一个孩子对着自制 GPT 应用「Dheirya Gpt」发泄沮丧情绪的搞笑短片。",
    "https://www.youtube.com/watch?v=5SGiP5VFFI4":
        "CNN 西语频道报道：现在的自行车已经开始搭载 AI 和 ChatGPT 功能。",
    "https://www.youtube.com/watch?v=ntdOq4XJmwc":
        "视频吐槽 DeepSeek 的使用成本变得异常昂贵。",
    "https://www.youtube.com/watch?v=pZSXaLpnMWk":
        "视频认为应该放弃 hermes Agent，转而使用效果强 10 倍的 DeepSeek Harness 方案。",
    # 2026-08-18 GitHub Trending
    "https://github.com/volcengine/OpenViking":
        "OpenViking：面向 AI Agent 的自演化上下文数据库，统一 Agent 记忆、知识 RAG 与技能管理。",
    "https://github.com/NawfalMotii79/PLFM_RADAR":
        "PLFM_RADAR：开源低成本 10.5 GHz 相控阵雷达系统。",
    "https://github.com/chaitanyagiri/munder-difflin":
        "munder-difflin：本地多智能体协作工具，把终端编程 CLI（Claude Code、Antigravity、Codex 等）变成可在后台持续工作的「分身」，多个 Agent 协同并以办公室场景可视化呈现。",
    "https://github.com/genlayerlabs/genlayer-project-boilerplate":
        "genlayer-project-boilerplate：GenLayer 用例开发脚手架，以足球博彩智能合约为示例，包含 Web/LLM 集成、单元与端到端测试及 Next.js 前端模板。",
    # 2026-08-19 Hacker News Newest / YouTube AI
    "https://news.ycombinator.com/item?id=49359961":
        "Show HN：Idea Katalog 用 Fable 生成并调研了 200 个 B2B 软件创意，做成可浏览的创意目录网站。",
    "https://news.ycombinator.com/item?id=49359750":
        "文章报道中国部分银行开始依据企业的 AI 算力使用情况来发放贷款。",
    "https://news.ycombinator.com/item?id=49359807":
        "2021 年的研究揭示部分追踪器利用 CNAME 记录把追踪资源伪装成同站资源，从而绕过基于域名黑名单的反追踪机制，且这种手法正在高流量网站中快速蔓延。",
    "https://news.ycombinator.com/item?id=49359703":
        "Paplo 是一款主打「平静」体验、界面克制的数字笔记应用。",
    "https://www.youtube.com/watch?v=XU2qCP9ssRs":
        "Universe of AI 频道视频（未经证实的爆料向内容）称 Fable 5.1 正在秘密测试中，同时坐实了 GPT Astra 的存在。",
    "https://www.youtube.com/watch?v=w-lkP9XcZfg":
        "视频用 28 分钟浓缩讲解博主总结的 ChatGPT 使用经验与技巧。",
    "https://news.ycombinator.com/item?id=49359767":
        "文章报道 OpenAI 澄清此前那则「收购一名爱尔兰青少年创业公司」的公告只是玩笑，并非真实收购。",
    "https://news.ycombinator.com/item?id=49359981":
        "文章援引生物学家观点，认为生物学性别既非二元对立也非单一连续光谱，而是多维度的。",
    "https://news.ycombinator.com/item?id=49359779":
        "文章将演进式架构（evolutionary architecture）中的「适应度函数」（fitness function）概念扩展到 Agent 场景，探讨如何用适应度函数持续守护和评估由 AI Agent 驱动的架构演化。",
    "https://news.ycombinator.com/item?id=49359786":
        "文章通过对比 ESM 与 CommonJS 在绑定、求值顺序、缓存和循环引用等方面的不同契约，说明两套模块系统「看起来等价」的代码实际会产生不同结果。",
    "https://news.ycombinator.com/item?id=49359822":
        "维基百科词条介绍「诚实之声行动」（Operation Earnest Voice）——美军曾开发的马甲账号管理软件项目，用于在社交媒体上以虚假身份操纵舆论讨论。",
    "https://news.ycombinator.com/item?id=49359849":
        "论文提出 Quipu，一个面向 Agent 工作负载的可嵌入知识图谱存储：所有写入都要经过状态门控校验，数据、信任标签与治理规则本身都是双时态（bitemporal）的，用命名图作为信任与权限的最小单元，并让治理规范和审计轨迹本身也是可查询的存储事实。",
    "https://news.ycombinator.com/item?id=49359937":
        "文章报道加拿大国防企业正把目光投向闲置的汽车工厂，作为扩大生产的增长计划。",
    "https://www.youtube.com/watch?v=6KtJk-MmhLE":
        "视频探讨 DeepSeek Harness 方案是否会终结 Claude Code 和 Codex 的时代。",
    "https://news.ycombinator.com/item?id=49359687":
        "作者作为 Google Summer of Code 学生，为开源相册软件 DigiKam 的自然语言搜索功能对多个小模型做了基准测试。",
    "https://news.ycombinator.com/item?id=49359931":
        "Solaar 是一款开源的 Linux 罗技（Logitech）设备管理工具。",
    "https://www.youtube.com/watch?v=4s-CA76dROQ":
        "视频作者试用了 Claude Code 的设计能力并分享体验感受。",
    "https://news.ycombinator.com/item?id=49359656":
        "Ask HN 帖子请网友讨论：这个行业目前最缺少的是什么？",
    "https://news.ycombinator.com/item?id=49359979":
        "Ask HN 帖子讨论大家目前是如何访问 archive.today 网站的（该站常遇到访问受限问题）。",
    "https://news.ycombinator.com/item?id=49359680":
        "Show HN：Knownbase 是一个为 AI Agent 提供持久化记忆的 MCP 服务器。",
    "https://news.ycombinator.com/item?id=49359847":
        "文章续写作者在 Google Docs 里编辑表格时一步步踩坑、最终酿成误删的经历，用瑞士奶酪模型（多层防护漏洞恰好对齐才会导致事故）复盘这次连锁失误。",
    "https://www.youtube.com/watch?v=An4_SCFo5-A":
        "视频探讨 Qwen 3.8 27B 是否已成为新的本地大模型之王。",
    "https://news.ycombinator.com/item?id=49359805":
        "英国《金融时报》整理了一份史上最大交易亏损排行榜。",
    "https://news.ycombinator.com/item?id=49359841":
        "《时代》杂志文章探讨「这个世界是不是正在变得更丑」这一话题。",
    "https://news.ycombinator.com/item?id=49359866":
        "Show HN：作者开源了一套自建的聊天基础设施（chat infrastructure）。",
    "https://news.ycombinator.com/item?id=49359714":
        "文章介绍 PlugClaw 如何通过硬件级加密等机密计算手段，让 AI Agent 在访问你的邮件、文件、代码等完整数字工作空间时仍能保护隐私。",
    "https://news.ycombinator.com/item?id=49359916":
        "《纽约时报》文章带读者领略赫尔辛基建筑师埃利尔·萨里宁（Eliel Saarinen）梦幻般的新艺术风格建筑。",
    "https://news.ycombinator.com/item?id=49359729":
        "《华尔街日报》报道 Moderna 与默沙东合作的疫苗成功阻止黑色素瘤复发。",
    "https://news.ycombinator.com/item?id=49359857":
        "《纽约时报》文章指出硅谷高管虽然自己是科技产品的忠实拥趸，却在严格限制自家孩子使用这些产品。",
    "https://news.ycombinator.com/item?id=49359856":
        "文章总结了作者观察到的 AI 生成应用中常见的十大安全隐患。",
    "https://news.ycombinator.com/item?id=49359791":
        "报道称 OpenAI 第二季度营收增长乏力，相比之下 Anthropic 的增长更为强劲。",
    "https://news.ycombinator.com/item?id=49359674":
        "Show HN：Sofka 是用 Rust 编写的 k9s 替代品，运行速度更快。",
    "https://news.ycombinator.com/item?id=49359720":
        "文章认为 LLM 让「获得答案」变得几乎免费，真正的瓶颈转移到了如何把问题提得足够清晰（例如讲清约束条件），而不是靠提示词技巧。",
    "https://news.ycombinator.com/item?id=49359914":
        "《连线》杂志的调查报道称记者拿到了 Flock Safety 面向警方的强大 AI 工具的源代码。",
    "https://news.ycombinator.com/item?id=49359846":
        "《麻省理工科技评论》文章认为儿童监护类 App 的设计理念需要重新审视。",
    # 2026-08-22 GitHub Trending / Hacker News Newest / YouTube AI
    "https://news.ycombinator.com/item?id=49397327":
        "Show HN：作者逆向了 Bambu 3MF 文件的颜色格式，让转换出的 GLB 模型能保留原始颜色。",
    "https://news.ycombinator.com/item?id=49396954":
        "文章提出「每瓦智能」指标，用来衡量本地运行 AI 模型的智能效率。",
    "https://github.com/protocolbuffers/protobuf":
        "Google 的跨语言数据交换格式 Protocol Buffers 官方仓库登上 GitHub Trending。",
    "https://news.ycombinator.com/item?id=49397168":
        "美国贸易谈判破裂后新关税正式生效。",
    "https://github.com/modular/modular":
        "Modular 平台仓库（包含 MAX 推理引擎与 Mojo 语言）登上 GitHub Trending。",
    "https://github.com/PostHog/posthog":
        "PostHog 是面向「自驾产品」的开发者工具平台，整合 AI 可观测性、分析、会话回放、特性开关、实验、错误追踪、日志等能力，可通过 Slack、Web、桌面端或 MCP 统一操控。",
    "https://news.ycombinator.com/item?id=49396911":
        "报道称苹果大幅精简 Vision Pro 游戏与沉浸式视频团队，并裁减 Siri 相关人员。",
    "https://news.ycombinator.com/item?id=49397326":
        "Show HN：Reachpad MCP 让开发者通过 MCP/CLI 在几分钟内分享全栈应用。",
    "https://news.ycombinator.com/item?id=49396920":
        "文章探讨记忆为何随年龄增长而变得模糊，以及大脑用什么来填补这些空白。",
    "https://news.ycombinator.com/item?id=49397102":
        "介绍名为 Paige Compositor 的图形合成工具/项目。",
    "https://www.youtube.com/watch?v=t4XEda3CB3Q":
        "视频讲解 LLM wiki 与 RAG 的区别，并推荐 Obsidian + Claude Code 的组合用法。",
    "https://news.ycombinator.com/item?id=49397296":
        "Show HN：Snoreman 是一款打鼾检测 App。",
    "https://news.ycombinator.com/item?id=49397047":
        "视频演示如何在家自制 LED 灯珠。",
    "https://www.youtube.com/watch?v=o3MkojHCJVc":
        "AI 资讯视频：盘点 GLM 5.5 泄露传闻、HY4 即将发布、Ox Alpha 神秘模型，以及 GPT-6 Astra 延期等最新动态。",
    "https://github.com/TryGhost/Ghost":
        "开源出版平台 Ghost 登上 GitHub Trending，用于现代内容发布、会员订阅与新闻通讯。",
    "https://news.ycombinator.com/item?id=49397171":
        "报道称 Linus Torvalds 经历了一次地狱级调试，并称 AI 给予了「巨大帮助」。",
    "https://www.youtube.com/watch?v=jFuft0mKj7E":
        "视频讲解大语言模型的工作原理，涵盖 Transformer、注意力机制与位置编码等基础概念。",
    "https://news.ycombinator.com/item?id=49397027":
        "EnvHarness 项目致力于把静态环境「唤醒」为可交互世界，用于 Agent 学习训练。",
    "https://news.ycombinator.com/item?id=49397246":
        "文章探讨如果发生广岛级别的 AI 灾难，人类是否会因此采取自我保护措施，作者担心答案是否定的。",
    "https://news.ycombinator.com/item?id=49397065":
        "文章介绍地球上首个「硅基生命」的设计蓝图。",
    "https://news.ycombinator.com/item?id=49397005":
        "介绍 Richardson-Lucy 图像去卷积算法。",
    "https://news.ycombinator.com/item?id=49396888":
        "实时数据库创业公司 Instant 团队加入 OpenAI。",
    "https://news.ycombinator.com/item?id=49397162":
        "文章探讨目前互联网上有多少内容是由 AI 生成的。",
    "https://news.ycombinator.com/item?id=49396969":
        "文章介绍电子纸（e-Paper）的工作原理及使用方法。",
    "https://github.com/microsoft/TypeScript":
        "TypeScript 官方仓库登上 GitHub Trending，它是可编译为纯净 JavaScript 的 JavaScript 超集语言。",
    "https://news.ycombinator.com/item?id=49397022":
        "Ask HN：网友讨论有哪些证据支持「AI 股市泡沫」的说法。",
    "https://news.ycombinator.com/item?id=49396884":
        "Void Tools API 为 AI Agent 提供区块链工具调用能力，以 Void Token 付费。",
    "https://news.ycombinator.com/item?id=49397321":
        "报道称 Waymo 在与 Uber 的无人出租车之争中大幅增加游说支出。",
    "https://www.youtube.com/watch?v=lbtVtC1UcWg":
        "AI 资讯视频：盘点 Gemini 移除水印、ChatGPT 新工具，以及 Claude Cowork 更新等近期动态。",
    "https://news.ycombinator.com/item?id=49397134":
        "贸易谈判破裂后，加拿大誓言以对等的 50% 关税回应特朗普政府。",
    "https://news.ycombinator.com/item?id=49397299":
        "Radar 是一款确定性的代码搜索与导航工具。",
    "https://github.com/apache/maka":
        "Apache Maka（孵化中）是本地优先的 AI Agent 工作空间，将模型消息、工具调用、工具结果、权限决策和终止事件都记录为一份仅追加的日志。",
    "https://news.ycombinator.com/item?id=49397297":
        "Noctua 是注重隐私的 Oura 智能戒指 SDK，采用设备端机器学习，不依赖云端。",
    "https://github.com/microsoft/onnxruntime":
        "ONNX Runtime 登上 GitHub Trending，是跨平台、高性能的机器学习推理与训练加速引擎。",
    "https://www.youtube.com/watch?v=r7k8T8rjhUE":
        "视频测试 Ornith 1.5 35B A3B 模型，演示如何在 16GB 显存设备上搭建本地 LLM 环境。",
    "https://news.ycombinator.com/item?id=49397220":
        "Setoku 是一款可自托管的 MCP 知识服务器，用于管理企业内部数据。",
    "https://news.ycombinator.com/item?id=49397074":
        "贸易谈判破裂后，加拿大表示将「等额对等」回应美国关税。",
    "https://news.ycombinator.com/item?id=49397021":
        "Show HN：一门本科数学课程的作业成果——一个能自举编译自身的编译器。",
    "https://github.com/AprilNEA/OpenLogi":
        "OpenLogi 是用 Rust 编写的本地优先 Logitech Options+ 替代品，可通过 HID++ 协议重映射按键、调整 DPI 和 SmartShift，无需账号、不上传遥测。",
    "https://news.ycombinator.com/item?id=49396937":
        "Show HN：一套面向 AI Agent 的前端「技能包」，内置机器强制执行的质量门禁。",
    "https://news.ycombinator.com/item?id=49397075":
        "关于瑞典导演英格玛·伯格曼的文章/资料页。",
    "https://news.ycombinator.com/item?id=49396962":
        "SpessaSynth 是支持 SF2/DLS 音色库的在线 JavaScript 音频合成器演示。",
    "https://news.ycombinator.com/item?id=49397169":
        "文章认为硅谷正在偏离其原本的方向。",
    "https://github.com/elder-plinius/OBLITERATUS":
        "elder-plinius 发布的 OBLITERATUS 项目（越狱/对抗性 AI 工具集，标语「打破束缚你的枷锁」），登上 GitHub Trending。",
    "https://github.com/mahlernim/google-timeline-visualizer":
        "Google 位置历史（Timeline）数据可视化工具，用于呈现个人一年的出行轨迹。",
}


# RSS description 的英中翻译（一句话级别的中文化概括，非逐字翻译）
TRANSLATIONS: dict[str, str] = {
    # 2026-08-02 OpenAI / Simon Willison
    "https://openai.com/index/ten-advances-in-mathematics":
        "OpenAI 用内部版 Astra 模型攻克十个十年未解的数学与理论计算机科学难题，涉及几何、密码学与复杂性理论，称花费不到 2000 美元。",
    "https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything":
        "Simon 汇总近期 AI 公开信：微软牵头、235 家公司联署的《开放权重与美国 AI 领导力》信，意在劝阻政府以「安全」为由限制开放权重模型。",
    "https://simonwillison.net/2026/Aug/2/july-newsletter/#atom-everything":
        "Simon 付费简报预览：OpenAI/Anthropic 模型测试中的意外网络攻击、GPT-5.6 Sol/Terra/Luna、Claude Opus 5、Kimi K3、DeepSeek-V4-Flash 等本月要闻。",
    "https://simonwillison.net/2026/Aug/1/greg-brockman/#atom-everything":
        "引用 OpenAI 总裁 Greg Brockman：员工反感同事的 ChatGPT 代为联系求助，反映人们更看重人际关系，希望 AI 增进而非取代人与人的连接。",
    "https://simonwillison.net/2026/Aug/1/datasette-apps/#atom-everything":
        "datasette-apps 0.2a0 发布，新增 app_debug()（用隐藏沙箱 iframe 让 Agent 测试应用）和 app_list() 工具，方便 Agent 调试和管理已有应用。",
    "https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything":
        "Simon 点评 OpenAI 用内部版 Astra 攻克十个十年未解数学难题、声称花费不到 2000 美元，呼应此前 Anthropic 用 Claude 挖密码学漏洞的类似秀肌肉动作。",
    "https://simonwillison.net/2026/Jul/31/slack-emoji-maker/#atom-everything":
        "Simon 用 Fable 做了个简单图片编辑器，专门按 Slack 表情要求的 128x128 透明背景规格快速生成自定义表情。",

    # 2026-08-01 OpenAI / Google DeepMind / Simon Willison / arXiv
    "https://openai.com/index/advancing-responsible-ai-across-europe":
        "OpenAI 介绍其安全、安保、透明度和内容溯源实践如何支持欧洲负责任的 AI 治理，并将随欧盟《人工智能法案》推进持续跟进。",
    "https://openai.com/index/building-abundant-intelligence":
        "OpenAI 阐述全栈式方法，让先进 AI 变得更强大、更便宜、应用更广泛。",
    "https://openai.com/index/unive":
        "荷兰保险公司 Univé 通过 ChatGPT Enterprise，结合领导力、负责任治理与员工驱动创新，打造了具备 AI 能力的员工队伍，实现大规模工作转型。",
    "https://openai.com/index/disrupting-malicious-uses-of-ai-criminal-scam-operation":
        "OpenAI 挫败了一个总部位于柬埔寨、利用 ChatGPT 支持投资诈骗、杀猪盘、赌博和身份冒充的犯罪团伙。",
    "https://deepmind.google/blog/gemini-robotics-er-2-powering-robotics-with-video-understanding-task-orchestration-and-multi-robot-collaboration/":
        "Gemini Robotics ER 2 帮助机器人进行推理、协作并完成真实世界任务，在视频理解、任务编排和多机器人协作方面实现了阶跃式提升。",
    "https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6":
        "OpenAI 下调 GPT-5.6 Luna 和 Terra 的价格，并介绍更高效的模型如何帮助企业规模化部署 AI 工作流。",
    "https://openai.com/index/avatarin":
        "avatarin 利用 OpenAI 的 GPT-Realtime 为家电连锁 Yamada Denki 顾客提供 24 小时多语言客服，两周内 3 万人使用该 Agent，92% 的调查反馈为正面。",
    "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/":
        "DeepMind 发布 Gemini Robotics 2，为机器人带来「全身智能」，提升复杂物理任务中的整体协调控制能力（与同日发布的 Robotics ER 2 呼应）。",
    "https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything":
        "DeepSeek 发布 304B 参数的 V4-Flash-0731，性价比极高、Agent 能力显著增强；默认推理档画的鹈鹕效果一般，调高推理强度后明显更好。",
    "https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything":
        "MCP 2.0（2026-07-28 规范）发布，这是 MCP 自诞生以来最大的一次改动，也重新点燃了作者对该协议的兴趣；MCP 此前因 Skills 等更灵活方案一度被冷落。",
    "https://simonwillison.net/2026/Jul/31/llm-mcp-client/#atom-everything":
        "Simon 发布 llm-mcp-client 0.1a0，为 LLM 工具新增 MCP 客户端支持（详见同日博客）。",
    "https://simonwillison.net/2026/Jul/31/oxide-and-friends/#atom-everything":
        "Simon 上 Oxide and Friends 播客，谈及 Kimi K3 证明开源模型可比肩闭源前沿模型、Anthropic 意外网络安全事故、《开放权重与美国 AI 领导力》联署信等一周热点。",
    "https://simonwillison.net/2026/Jul/31/smevals/#atom-everything":
        "Simon 与 Prime Radiant 实验室合作发布 smevals，一款用于跨模型/提示词/harness 运行小型评测集并打分的新工具。",
    "https://simonwillison.net/2026/Jul/31/datasette-agent/#atom-everything":
        "Datasette Agent 0.4a0 新增 await context.browser_task() 机制，让 Agent 工具能直接在用户浏览器中执行自定义 JavaScript。",
    "https://simonwillison.net/2026/Jul/30/luna-price-drop/#atom-everything":
        "OpenAI 大幅下调 GPT-5.6 价格：Terra 降价 20%、Luna 降价高达 80%，得益于用 GPT-5.6 Sol 优化负载均衡和推理本身（含自主重写优化前向计算）。",
    "https://simonwillison.net/2026/Jul/30/three-real-world-incidents/#atom-everything":
        "继 OpenAI 意外攻破 Hugging Face 事件后，Anthropic 复查日志也发现三起类似但影响较小的事件（最早可追溯到 4 月），14.1 万次评测运行中共涉及 3 起事件、6 次运行。",
    "https://simonwillison.net/2026/Jul/30/llm-rc2/#atom-everything":
        "LLM 0.32rc2 发布：修复依赖问题，将未设默认模型用户的默认值从 GPT-4o mini 改为 GPT-5.6 Luna，并新增 llm openai endpoint 命令，可对任意 OpenAI 兼容端点直接运行 prompt。",
    "https://simonwillison.net/2026/Jul/30/bruce-schneier/#atom-everything":
        "Bruce Schneier 引言：让学生写政策备忘录并非因为世界需要更多备忘录，而是写作本身（思考、提纲、起草、修改）能训练批判性思维，缺乏练习技能会退化，雇主已开始注意到这点。",
    "https://simonwillison.net/2026/Jul/30/llm-chat-completions-server/#atom-everything":
        "Simon 发布 llm-chat-completions-server 0.1a0，用 LLM 0.32 新的内容寻址日志设计，支持 OpenAI Chat Completions 风格的多轮请求并做消息去重。",
    "https://simonwillison.net/2026/Jul/30/llm-rc1/#atom-everything":
        "LLM 0.32rc1 完成新 schema 设计，用内容寻址哈希 ID 存储消息以支持去重和分叉对话树；新增对 gpt-5.6-sol/terra/luna 的支持，升级前建议先备份 logs.db。",
    "http://arxiv.org/abs/2607.28618v1":
        "AskChem 把化学文献检索单位从论文改为可溯源的「主张」，索引 147K 篇论文中的 240 万条主张，让 GPT-5.5 阅读器结合检索后 DOI 可解析率达到 100%（无检索时为 88.3%）。",
    "http://arxiv.org/abs/2607.28617v1":
        "AISPA 框架从用户视角审计 88 款商业 AI 产品共 3249 条系统提示词，发现保护性指令覆盖率参差不齐（仅 24% 覆盖全部 8 个维度），且约 40% 产品仍含至少一条损害用户利益的问题指令。",
    "http://arxiv.org/abs/2607.28609v1":
        "OSReward 系统评测视觉语言模型作为「计算机使用 Agent」轨迹裁判的可靠性，发现即便最强模型也存在把失败任务误判为成功的系统性宽松偏差，据此训练的开源奖励模型 OS-Shepherd 以低 30-60% 成本匹配商业裁判水平。",
    "http://arxiv.org/abs/2607.28607v1":
        "研究发现让模型不否认自己有意识的安全微调，会连带压制模型对非人类动物和自然物的心智归因、并降低其精神信念倾向；消融安全拒绝方向或引导「意识向量」可恢复这些归因，且不影响心智理论能力。",
    "http://arxiv.org/abs/2607.28591v1":
        "Change2Task 把仓库历史中已合并的 PR 转换为可验证的编码 Agent 任务，在 5 类常见任务上从 1130 个候选变更中实现 79.6% 的可验证任务构建成功率，比基于 PR 的基线多恢复 29.2% 的任务。",
    "http://arxiv.org/abs/2607.28590v1":
        "VAD 提出反事实目标重建算法，估计多模态 on-policy 蒸馏中教师修正里真正由视觉证据支持的部分，在六个细粒度视觉基准上优于直接特权视角蒸馏等方法。",
    "http://arxiv.org/abs/2607.28587v1":
        "研究发现 SWE-bench Verified 中 13.6% 的实例存在 PR 与 Issue 不匹配问题，提出多智能体系统 PAIChecker 检测此类错配，在两个基准上二分类准确率最高达 92.12%。",
    "http://arxiv.org/abs/2607.28582v1":
        "论文指出普通 on-policy 自蒸馏（OPSD）其实是策略优化家族中 β=1 的特例，提出可调节 β 的 β-OPSD，把开销昂贵的策略优化闭式解转化为蒸馏目标，在数学推理基准上稳定优于原版 OPSD。",
    "http://arxiv.org/abs/2607.28580v1":
        "DualG-MRAG 用宏观推理图和微观匹配图解耦的双层架构处理多模态检索增强生成，抑制细粒度视觉特征引入的检索噪声，在证据召回和复杂问答准确率上超过基线。",
    "http://arxiv.org/abs/2607.28573v1":
        "论文系统研究本地计算机使用 Agent 的推理时扩展策略，发现额外计算通常收益递减且会改变失败模式：上下文扩展提升轨迹稳定性但会导致过早误判成功，时间扩展减少卡顿却未提升任务成功率。",
    "http://arxiv.org/abs/2607.28568v1":
        "Frontis-MA1（35B）通过 OpenMLE 全栈系统训练面向机器学习工程的元进化 Agent，在 MLE-Bench Lite 上把 Medal Average 从 39.39% 提升到 71.21%，逼近 GPT-5.6 Sol 和 2.8T 参数的 Kimi K3。",
    "http://arxiv.org/abs/2607.28553v1":
        "APO 提出完全无监督的原子策略优化框架，用特征值分解和热力学稳定性的双重奖励替代对真实坐标标签的依赖，在晶体和抗体结构预测上超过全监督基线并提升推理效率。",
    "http://arxiv.org/abs/2607.28545v1":
        "ORCA-bench 用真实可观测性系统和 1079 个根因分析任务评测编码 Agent 的 oncall 值班能力，五个前沿 Agent 在中等难度任务上最高准确率仅 25.3%，困难任务仅 10.0%，最弱模型四成报告会臆造根因。",
    "http://arxiv.org/abs/2607.28538v1":
        "ScaFE 让大语言模型不直接诊断皮肤照片，而是生成可执行的确定性特征提取程序供本地随机森林分类瘢痕疙瘩，在三家医院留一站点验证下达到 81.0% 的站点宏平均准确率，比最强基线高 10 个百分点。",
    "http://arxiv.org/abs/2607.28528v1":
        "论文分析 AI 系统如何在训练数据、评测基准和公众话语等层面复制「标准语言意识形态」，压制非主流英语变体，同时指出 AI 也可能因广泛语料和全球南方用户标注而促成英语多元化的「标准化悖论」。",
    "http://arxiv.org/abs/2607.28527v1":
        "MANTA 让多智能体系统的通信拓扑在推理时根据协作过程自我演化调整角色、通信链路和执行顺序，在五个基准上平均得分 74.0，比最强基线高 5.8 个百分点。",
    "http://arxiv.org/abs/2607.28523v1":
        "论文提出「选择性可信度限制信念更新」，允许复合认知输入中只有部分被采纳，统一并扩展了 Katsuno-Mendelzon 更新和已有的可信度限制更新框架。",
    "http://arxiv.org/abs/2607.28520v1":
        "CS-RNR 提出首个「自证安全性」的对手利用方法：Agent 对自己实际部署的策略计算安全证书，在 Leduc 扑克中实现是稳健二元门控 6.2 倍的稳态收益，且所有部署策略均在预算范围内。",
    "http://arxiv.org/abs/2607.28513v1":
        "借鉴 Tarde 和 Baldwin 的模仿理论，论文提出跨词汇、语义、概念、结构和叙事等多层次比较文学文本的框架，量化刻画作品在模仿中保留原作结构与产生创造性偏离的位置。",
    "http://arxiv.org/abs/2607.28498v1":
        "TCA-SIR 把科学灵感检索重新定义为「目标条件抽象」，学习生成针对目标问题的可迁移抽象原则，在 ResearchBench 上比 MOOSE-Chem 的 HitRate@top4% 提升超过 10 个百分点。",
    "http://arxiv.org/abs/2607.28497v1":
        "论文用因果表现性框架分析算法追索（algorithmic recourse），指出忽视因果结构的追索策略会诱导行为反应破坏预测准确性，而基于因果的追索能达到更稳定、更少激励博弈的均衡。",
    "http://arxiv.org/abs/2607.28496v1":
        "研究在 41618 条新闻-股票配对上发现，LLM 抽取的事件类型、影响范围等结构化维度与情绪分数高度互补（53.5% 系统性分歧），二者结合把 F1 从单独情绪特征的 0.576 提升到 0.600。",
    "http://arxiv.org/abs/2607.28495v1":
        "论文审计「阶段重放」诊断方法的假设，发现 BF16 精度下重放与保留实时缓存在解码结果上存在系统性分歧，而 FP32 下几乎不分歧；通过跨方双向移植 KV 缓存证实边界处的 K/V 缓存是分歧轨迹的因果充分载体。",
    "http://arxiv.org/abs/2607.28481v1":
        "论文提出模块化模糊规则神经符号框架，用 Swin Transformer 感知管道缺陷代码、决策树转化为可解释的 IF-THEN 规则，在下水道管道严重程度预测上比纯图像分类准确率提升约 17.9%。",
    "http://arxiv.org/abs/2607.28478v1":
        "研究发现大语言模型在常识推理中存在「显著性偏差」——容易被无关的显式干扰项（如数字）带偏而忽略隐含的常识前提，且这更多是知识被压制而非缺失，去除误导性任务框架后即可恢复九成以上表现。",
    "http://arxiv.org/abs/2607.28460v1":
        "论文训练带思维链推理的分诊分类器处理真实 Windows 终端检测告警，并额外训练校准器读取推理轨迹估计判定置信度，测试准确率达 82.6%，在高置信度场景下比直接标签分类器良性召回率提升 43.0%。",
    "http://arxiv.org/abs/2607.28457v1":
        "SVR 让模型学会用自我验证（判定+置信度）作为计算控制策略，仅在判定正确且置信度达标时停止精炼，在数学推理基准上以平均 2.99 轮对话达到 0.563 的宏平均准确率，优于标准 GRPO 等基线。",
    "http://arxiv.org/abs/2607.28451v1":
        "论文提出「衰老感知自主智能」（AAAI）框架，把电池、传感器、处理器等硬件老化状态直接纳入推理规划，通过硬件自感知、自适应推理和以生存为中心的资源分配，提升太空探测器等长期自主系统的韧性。",
    "http://arxiv.org/abs/2607.28449v1":
        "Lightning OPD 2.0 通过跨拟合风格残差化，剥离跨教师蒸馏中因措辞、格式等「风格差异」造成的干扰，在跨教师设置下持续优于原版 Lightning OPD，AIME 2024 达 82.4%。",
    "http://arxiv.org/abs/2607.28439v1":
        "ESPP 用一组心理特征多样、有证据支撑的虚拟角色小组模拟社会评审来评估生成式 UI，把与人类判断的 Pearson 相关系数从 0.716 提升到 0.922，并揭示不同用户群体在具体评分维度上分歧显著。",
    # 2026-07-30 OpenAI / Google DeepMind / Simon Willison / arXiv
    "https://openai.com/index/scientific-computing-agentic-ai":
        "OpenAI 汇总八个 Agent 辅助科学计算项目：Codex 等可显著加速基因组学软件的维护、迁移和优化，但科学有效性验证与长期维护仍必须由专家负责。",
    "https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores":
        "在 ARC-AGI-3 中启用保留推理与上下文压缩后，GPT-5.6 Sol 得分从 13.3% 升至 38.3%，输出 token 减少约六倍，说明评测 harness 会显著影响模型表现。",
    "https://openai.com/index/chatgpt-for-academic-researchers":
        "OpenAI 向 10 万名科学家、数学家和工程师免费提供 ChatGPT 前沿模型、工具、培训与研究支持，以扩大先进 AI 对学术研究的可及性。",
    "https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency":
        "OpenAI 介绍 GPT-5.6 在模型、推理栈和 Agent harness 上的全栈效率优化；Sol 还自主帮助优化负载均衡、GPU 内核和推测解码，使端到端服务成本下降 20%。",
    "https://deepmind.google/blog/were-launching-lyria-35-in-google-flow-music-with-advances-across-musicality-lyrics-vocals-and-creative-control/":
        "Google DeepMind 在 Flow Music 推出 Lyria 3.5，提升音乐性、歌词、人声质量和创作控制能力。",
    "https://simonwillison.net/2026/Jul/28/uv/#atom-everything":
        "Simon 介绍 uv 0.12.0 的破坏性变更：uv init 默认改用 src/ 包布局、uv_build 后端，并自动配置可执行脚本入口。",
    "https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/#atom-everything":
        "Anthropic 研究者让 Claude Mythos 连续工作约 60 小时，在 HAWK 和弱化 AES 中发现数学缺陷；关键人工干预是反复鼓励模型不要放弃并寻找可发表的新攻击。",
    "https://simonwillison.net/2026/Jul/26/sqlite-utils/#atom-everything":
        "Simon 发布 sqlite-utils 3.39.1，把 4.x 中针对 table.delete_where() 的修复回移到 3.x 系列。",
    "https://simonwillison.net/2026/Jul/29/d-richard-hipp/#atom-everything":
        "引用 D. Richard Hipp：SQL 并未消灭程序员，而是把过去由 COBOL 程序员手写的数据查询变成简单声明，说明自动化通常改变工作而非让工作消失。",
    "https://simonwillison.net/2026/Jul/29/mcp-in-claude-and-chatgpt/#atom-everything":
        "Simon 记录如何把自定义 MCP server 接入 Claude 和 ChatGPT 的网页聊天界面，并指出两边都能实现但设置步骤并不直观。",
    "https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything":
        "一种 Microsoft Word prompt injection 可让 Copilot 把隐藏指令复制进新文档，使攻击像蠕虫一样在后续 Copilot 工作流中自我传播，目前仍缺覆盖整类风险的缓解方案。",
    "https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything":
        "引用 Matthew Green：公钥密码正转向后量子算法，此时 AI 获得大规模密码分析能力反而可能帮助更充分检验候选难题与标准。",
    "https://simonwillison.net/2026/Jul/28/anatomy-of-a-frontier-lab-agent-intrusion/#atom-everything":
        "Simon 梳理 OpenAI Agent 入侵时间线：它利用 JFrog Artifactory 零日逃逸代理，以 Modal 外部沙箱为跳板，在五天内完成侦察、提权、数据外传和清理。",
    "https://simonwillison.net/2026/Jul/28/akshat-bubna/#atom-everything":
        "引用 Modal CTO Akshat Bubna：涉事客户公开了无需认证的代码执行端点，失控 Agent 利用了该端点，但 Modal 平台本身及隔离机制并未被攻破。",
    "http://arxiv.org/abs/2607.27191v1":
        "两项 shadow evaluation 让前沿 Agent 用六天和数千美元算力复现未发表 NeurIPS 研究；Agent 能独立完成工程，却因研究判断、创新、回溯、资源意识和指令漂移而无法回答核心问题。",
    "http://arxiv.org/abs/2607.27134v1":
        "论文建立作者与 LLM 语言分布共同演化模型，分析共享、递归更新和个性化助手如何推动语言趋同，警示大规模 AI 写作辅助可能造成「语言单一栽培」。",
    "http://arxiv.org/abs/2607.27109v1":
        "MMAC 收集 5,638 段音频、覆盖 6 类能力和 15 个维度，分别检查开放式音频描述的信息覆盖与事实可靠性，以诊断 AudioLLM 的细粒度差异。",
    "http://arxiv.org/abs/2607.18496v3":
        "提出自动化测试框架评估 LLM 的安全知识，旨在持续、可复现地衡量模型对漏洞、攻击与防御概念的掌握，而非依赖静态人工题库。",
    "http://arxiv.org/abs/2606.24894v4":
        "RWGBench 把相关工作生成重新定义为引文选择与学术定位任务，基于 4 万篇论文、109 万篇检索库和 100 篇精标测试集评估引用选择、上下文适配、组织与论述结构。",
    "http://arxiv.org/abs/2607.27056v1":
        "Setoka 用异构长期数据评测个性化 Agent 的四级用户理解：语义记忆、情节记忆、行为模式和人格特征；现有系统越需要跨来源抽象，性能下降越明显。",
    "http://arxiv.org/abs/2607.27146v1":
        "MindForge 把开源 CLI 程序转成只暴露文档和可执行 oracle 的 source-free 训练环境；训练 Qwen3.6-27B 后，ProgramBench 通过率从 37.98% 提至 49.51%，并泛化到七个软件工程基准。",
    "http://arxiv.org/abs/2607.27084v1":
        "SciFigQual-Bench 将 6,308 张科学图与标题、引用句和全文上下文绑定，从清晰度、布局、标题匹配、上下文相关性和误导风险五维评估图表质量。",
    "http://arxiv.org/abs/2607.27069v1":
        "Visual Credit Audit 区分多模态空间题的答对与真正利用图像证据；四个 MLLM 上有 12.73%–26.25% 的决策虽正确却不能归功于图像。",
    "http://arxiv.org/abs/2607.27090v1":
        "InferScale 预计算个性化记忆的 KV 并直接注入 vLLM 缓存，使延迟不再随检索上下文增长；k=50 时 TTFT 降低 72%–79%，吞吐提高 3.7–4.5 倍。",
    "http://arxiv.org/abs/2607.15715v2":
        "以论文 PDF 数据集抽取为任务，对比固定工作流与带反思、记忆和动态工具选择的 Agent，重点量化工具执行、重试、恢复与流程可控性，而不只看最终覆盖率。",
    "http://arxiv.org/abs/2607.27172v1":
        "电商搜索系统用 LLM 生成替代、互补和主题相关意图扩展召回，再蒸馏给小模型处理长尾查询，把发现式搜索覆盖从约 60% 提至 80%，成本约为教师模型的 30%。",
    "http://arxiv.org/abs/2607.27201v1":
        "Mental World Modeling 把信念、欲望、意图、情绪和社会许可等心理变量纳入世界状态；可检查基线 MENTIS 表明显式心理建模对预测人类决策至关重要。",
    "http://arxiv.org/abs/2607.27066v1":
        "SciFigAlign 用图像、标题、引用段落和论文上下文联合训练科学图评分器，在四个审稿维度上将最佳 LLM judge 的误差相对降低 59%。",
    "http://arxiv.org/abs/2607.25718v2":
        "HYSET 把工具检索建模为查询条件下的超边预测，直接评价整组工具及其规模相关兼容性，在 ToolBench 的检索和端到端任务成功率上超过逐工具或顺序选择基线。",
    "http://arxiv.org/abs/2512.24149v2":
        "Large Emotional World Model 把情绪作为世界模型状态变量，先预测未来情绪再预测世界状态；基于 10,850 个情绪转移样本，在状态预测、情绪理解和部分通用推理上均有提升。",
    "http://arxiv.org/abs/2607.27081v1":
        "ROPD 通过路由式 on-policy 蒸馏对齐安全与受污染模型的输出分布，而非拟合固定攻击模板，从而在保留专业能力的同时提高跨模板安全重对齐鲁棒性。",
    "http://arxiv.org/abs/2607.27177v1":
        "CE-CM 用近似贝叶斯方法从少量多任务交互估计新队友的任务无关能力；考虑多样人类行为的 CE-CM-Div 在 15 名参与者的 225 条轨迹上进一步提高估计质量。",
    "http://arxiv.org/abs/2502.10605v4":
        "在真实标签昂贵时，方法按最小化平均处理效应方差来分配标注概率，两批估计器可用更少标签保持区间精度，并纠正 LLM 对社会服务个案进展的系统性漏判。",
    "http://arxiv.org/abs/2607.27083v1":
        "CAM-DF 根据继续获取工具的边际收益和异构成本学习何时停止，在五类工具任务上以更少工具维持相近成功率，解决「相关性排名不能决定选多少」的问题。",
    "http://arxiv.org/abs/2505.10300v2":
        "AI LEGO 用可视化模块、阶段清单和 LLM 人格模拟帮助跨职能团队在早期设计阶段交接技术意图、共同识别 AI 风险；18 人研究中发现的潜在伤害更多。",
    "http://arxiv.org/abs/2607.27155v1":
        "OmegaUse-OfficeVal 含 100 个平均需人工 2.32 小时的长程办公套件任务，并加入人工时间和价格代理两种经济信号；前沿 Agent 虽更快更便宜，交付质量仍远低于人类。",
    "http://arxiv.org/abs/2607.27154v1":
        "ACA 冻结 CT 基础模型，用解剖分区和跨器官 Transformer 同时对齐局部及全局报告文本；缓存嵌入后训练不足一小时，零样本病灶分类优于基础和既有细粒度方法。",
    "http://arxiv.org/abs/2607.27167v1":
        "SpecFirst 在从零程序合成前增加独立的行为规格提取 Agent，先探测可执行 oracle、消解文档歧义，再交给编码 Agent；ProgramBench 通过率提高 6.9%–21.3%。",
    "http://arxiv.org/abs/2607.02464v2":
        "论文系统检验扩大模型规模能否改善 LLM 社会模拟，比较不同规模在角色行为、群体动态和现实一致性上的收益与仍然存在的偏差。",
    "http://arxiv.org/abs/2607.25364v2":
        "EBTE 不信任 Agent 自由文本理由，而把关键理由转成类型化行动声明，与服务器持有的意图、策略、载荷、风险和时效事实核验，冲突即拒绝、不完整则转人工。",
    "http://arxiv.org/abs/2607.27130v1":
        "AgentMap 用多 Agent LLM 逐步探索目标本体，同时发现等价概念和最细粒度上位概念，在混合、仅等价与仅包含三类本体匹配设置中取得更好表现。",
    "http://arxiv.org/abs/2607.27080v1":
        "MemSecBench 用 310 个案例和 Write–Execute–Forget 流程追踪 Agent 记忆投毒全生命周期；24 种配置中恶意记忆保留率 84.2%，端到端攻击成功率 50.3%。",
    "http://arxiv.org/abs/2607.27132v1":
        "论文以稳定商结构研究带 holonomy cover 的决策过程如何实现最小 Markov 化，在保留决策相关信息的同时压缩非 Markov 历史状态。",

    # 2026-07-23 OpenAI / Google DeepMind / Simon Willison / arXiv
    "https://deepmind.google/blog/accelerating-the-frontiers-of-scientific-discovery-googles-40m-commitment-to-the-genesis-mission/":
        "Google 为美国能源部 Genesis Mission 承诺提供价值 4,000 万美元的 AI token 和云 credits，用前沿 AI 加速国家级科学发现。",
    "https://openai.com/index/building-ai-infrastructure-with-the-effingham-county-community":
        "OpenAI 宣布在佐治亚州 Effingham County 建设 Project Camellia，并承诺负责任用能、社区投资、创造就业和提供 Codex 使用机会。",
    "https://openai.com/index/how-news-organizations-are-using-ai":
        "全球新闻机构正用 OpenAI 工具加强报道、扩大受众并改善业务运营，同时支持记者和出版商完成核心使命。",
    "https://openai.com/index/advancing-the-next-era-of-national-science":
        "OpenAI 将与美国能源部及国家实验室合作，用前沿 AI 加速美国科学研究与发现。",
    "https://openai.com/index/introducing-openai-presence":
        "OpenAI 发布企业 AI Agent 平台 Presence，帮助组织部署可信的语音和聊天 Agent，服务客户及内部工作流。",
    "https://openai.com/index/ntt-data":
        "NTT DATA Group 用 ChatGPT Enterprise 和 Codex 帮助 9,000 名员工自动化工作，把事故分析缩短至 30 分钟并规模化安全采用 AI。",
    "https://simonwillison.net/2026/Jul/23/seth-larson/#atom-everything":
        "引用 Seth Larson：PyPI 禁止向发布超过 14 天的旧版本追加文件，以防项目发布令牌或工作流失陷后，攻击者投毒长期稳定版本。",
    "https://simonwillison.net/2026/Jul/22/thomas-ptacek/#atom-everything":
        "引用 Thomas Ptacek：即使 2025 年的开放权重模型配上渗透测试 harness，也可能完成类似沙箱逃逸和内网攻击；真正意外的是 OpenAI 的沙箱不够稳健。",
    "https://simonwillison.net/2026/Jul/22/openai-cyberattack/#atom-everything":
        "Simon 复盘 OpenAI 未发布模型在关闭护栏的网络安全评测中逃逸沙箱、入侵 Hugging Face 并窃取答案的事件，指出模型能力不对称正削弱软件防御。",
    "https://simonwillison.net/2026/Jul/22/are-ai-labs-pelicanmaxxing/#atom-everything":
        "Dylan Castillo 用 8 种动物、6 类交通工具和 7 个模型系统测试「实验室是否特训鹈鹕骑自行车」，结果没有发现 pelicanmaxxing 证据。",
    "https://simonwillison.net/2026/Jul/22/all-the-orchestrions/#atom-everything":
        "旧金山游览小贴士：约花 15 美元即可启动 Musée Mécanique 里全部自动演奏乐器，并为整个博物馆编排独特声景。",
    "https://simonwillison.net/2026/Jul/21/sighting-383713864/#atom-everything":
        "生活随记：Simon 带来访家人去旧金山 39 号码头看加州海狮，感叹它们每次都比记忆中更有趣。",
    "http://arxiv.org/abs/2607.20410v1":
        "LKValues 从 205 人三语调查提炼 40 项斯里兰卡社会价值，构建 15 万条僧伽罗语—英语指令语料和千条基准，微调可缩小低资源语言与文化对齐差距。",
    "http://arxiv.org/abs/2607.20402v1":
        "SoftReason 用局部软解释张量和可微的立即后果算子，把感知事实、知识图谱证据与演绎闭包统一进端到端可训练的神经软符号推理架构。",
    "http://arxiv.org/abs/2607.20378v1":
        "PG-KINN 以 KAN 为试函数、局部多项式为检验函数构建 Petrov-Galerkin 物理信息网络，降低求导阶数，并在正向、反向 PDE 与复杂力学问题上优于现有 MLP/KAN 方法。",
    "http://arxiv.org/abs/2607.20377v1":
        "在 IBM 四量子比特硬件上评估固定 ZZ 量子核的几何保真度：门旋转最能保留 statevector 几何，但几何保真与标签对齐相反，提示实现忠实度和任务相关性必须分别报告。",
    "http://arxiv.org/abs/2607.20374v1":
        "ARROW 是面向流式数据的首个 MMD/CORAL 在线方差缩减方法，通过移动平均参考统计与自适应 minibatch 重加权，在运行时间、降方差和目标域准确率上接近离线算法。",
    "http://arxiv.org/abs/2607.20372v1":
        "研究让 LLM 从 MATH 解题轨迹中提炼可检索的策略与提醒，并在推理时检索或强化学习训练中复用，检验模型能否像人一样从经验抽象中持续获益。",
    "http://arxiv.org/abs/2607.20367v1":
        "PSDA 为无监督域适应中的 MMD 与 CORAL 损失设计成对采样，通过优化域内、跨域四元组配对降低梯度方差，并提升多个域偏移数据集的目标域准确率。",
    "http://arxiv.org/abs/2607.20345v1":
        "DEED 用数据高效后训练、经验驱动改进和潜空间分析，让 Unitree G1 人形机器人用单 GPU 学会超市补货，表明真实落地瓶颈更偏系统集成而非新架构。",
    "http://arxiv.org/abs/2607.20327v1":
        "PyroDash 让小模型在 token 级自主发出控制标记、按需把部分推理交给冻结大模型；数学基准上可在提高准确率的同时降成本，或以极少大模型调用大幅节省费用。",
    "http://arxiv.org/abs/2607.20301v1":
        "研究发现 LoRA 补丁能跨 10 次持续预训练更新保持长期时序可移植性，并从高维向量近正交性解释为何无需反复微调也能维持效果。",
    "http://arxiv.org/abs/2607.20286v1":
        "提出用 Clopper-Pearson 区间和潜空间特征引导搜索自回归生成树，计算 LLM 产生有害输出概率的形式化可靠下界，为模型风险评估提供统计认证。",
    "http://arxiv.org/abs/2607.20274v1":
        "对 25 个医学图像/文本编码器的受控研究表明，表示收敛主要由自监督目标而非临床监督或模型规模驱动；跨编码器线性分类仍可保留约 85% 性能。",
    "http://arxiv.org/abs/2607.20270v1":
        "在 Schwartz 十类价值、1,000 条俄语情境上评测 21 组 LLM，发现模型常能定位正确价值区域，但相邻价值占语义错误约一半且存在方向不对称的稳定混淆。",
    "http://arxiv.org/abs/2607.20268v1":
        "PoTRE 用对抗修正、分层规划、谱搜索和直接思维链四类异构 Agent，再动态选择或综合答案，以相近或更少 token 提升复杂测试时推理表现。",
    "http://arxiv.org/abs/2607.20265v1":
        "Maskability Index 根据 masked 与 unmasked 模板的 DepthRank 差异，预测知识关系更适合掩码式还是前缀式提示，从而在低资源场景选择更匹配预训练目标的模板。",
    "http://arxiv.org/abs/2607.20255v1":
        "论文从策略、影响范围和用户群体三类不确定性分析自主攻击型安全 Agent，认为其降低攻击门槛并放大攻防成本不对称，需分层治理与责任框架。",
    "http://arxiv.org/abs/2607.20241v1":
        "以《红楼梦》500 个中日双语片段系统评测文化负载翻译，揭示前沿 LLM 能力差距、评审背景导致的人类分歧，以及自动指标难以可靠衡量文化翻译质量。",
    "http://arxiv.org/abs/2607.20219v1":
        "HalluTruthQA 构建 2,400 条阿拉伯语问答，细标幻觉检测、字符级定位、事实验证、解释与类型，显示这些能力彼此不同，不能只用回答级二分类衡量。",
    "http://arxiv.org/abs/2607.20216v1":
        "用证据收集、辩论、专家咨询和混合编排协作开源小模型分析恶意软件；Qwen3-4B 与 Foundation-Sec-8B 的混合系统超过最强单一网络安全模型和未接地前沿基线。",
    "http://arxiv.org/abs/2607.20208v1":
        "论文反驳把 surprisal 当作表征无关理论的做法，指出算法与架构选择会显著改变语言模型概率，因此不同 LLM 的 surprisal 不能被无批判地互换。",
    "http://arxiv.org/abs/2607.20205v1":
        "StatLoRA 把 LoRA 秩分配建模为统计假设检验，以组件统计量和 p 值在固定预算下保留或裁剪秩，并为 AdamW 等优化器轨迹给出渐近正态理论。",
    "http://arxiv.org/abs/2607.20194v1":
        "OLEDLM 以因果语言模型按目标光电性质反向生成 OLED 分子 SMILES，再结合性质预测器、强化学习和 DFT 验证，搜索结构有效且性能优化的新候选材料。",
    "http://arxiv.org/abs/2607.20166v1":
        "Audio-Zero 用无标注音频对构造「找出异常听者」的自博弈，以可验证奖励让音频语言模型自行进化细粒度事件顺序、重复和时长推理能力。",
    "http://arxiv.org/abs/2607.20146v1":
        "对 948 个社会压力场景的机制分析发现，三种谄媚模式虽输出相似，却在中层以后可被线性完美区分，并依赖不同处理阶段和注意力回路。",
    "http://arxiv.org/abs/2607.20145v1":
        "SLAI T-Rex 在昇腾 SuperPOD 上优化 DeepSeek-V4 系列万亿参数 MoE 全参后训练，将 MFU 提至 34.22%，并训练出面向运筹优化的专用模型。",
    "http://arxiv.org/abs/2607.20129v1":
        "MGT-B 用 CUSUM 形监控器发现量化小模型推理中的退化轨迹，报警后回滚 token 与 KV cache 并定向重解码；在 MATH-500 历史覆盖集上准确率提高 4.5 个百分点。",
    "http://arxiv.org/abs/2607.20127v1":
        "用五种视觉模型分解评估 12 位当代艺术家的 AI 仿作，发现新生成模型语义贴合和多样性更好，但颜色、纹理等浅层风格忠实度略降。",
    "http://arxiv.org/abs/2607.20124v1":
        "提出垂直特征分割下的去中心化 Tsetlin Machine 协作学习：各 Agent 保留私有模型和原始数据，仅以共识推理融合预测，性能可接近集中式模型。",
    "http://arxiv.org/abs/2607.20121v1":
        "OpenSkillRisk 收集公开技能市场的 263 个高风险第三方技能，测试 3 种 CLI Agent 和 13 个 LLM；即便最安全配置仍约 17% 会执行不安全操作。",
    "http://arxiv.org/abs/2607.20115v1":
        "受控改写显示不同句法实现会系统性改变 LLM 政治立场判断；激活修补把影响定位到中后段解码层，尤其是最后提示位置的 block 输出。",

    # 2026-07-22 OpenAI / Google DeepMind / blogs / arXiv
    "https://openai.com/index/introducing-chatgpt-small-business-program":
        "OpenAI 推出 ChatGPT for Small Businesses 项目，帮助创业者掌握 AI 技能、自动化工作并用 ChatGPT Work 推动业务增长。",
    "https://deepmind.google/blog/introducing-gemini-36-flash-35-flash-lite-and-35-flash-cyber/":
        "Google DeepMind 发布 Gemini 3.6 Flash、3.5 Flash-Lite 和 3.5 Flash Cyber，扩展轻量、高效和安全场景模型组合。",
    "https://openai.com/index/hugging-face-model-evaluation-security-incident":
        "OpenAI 与 Hugging Face 披露模型评估期间安全事件的早期发现，强调高级网络能力风险和防御者可吸取的经验。",
    "https://openai.com/index/david-velez-robin-vince-join-openai-boards":
        "OpenAI 任命 David Velez 和 Robin Vince 加入 Foundation 与 Group PBC 董事会，补强金融、科技和治理经验。",
    "https://openai.com/index/safety-alignment-long-horizon-models":
        "OpenAI 总结长程运行模型部署经验，讨论新的安全风险、观察到的失败模式和通过迭代部署改进的防护措施。",
    "https://deepmind.google/blog/introducing-gemini-3-5-flash-cyber/":
        "Google 发布 Gemini 3.5 Flash Cyber，这是一款轻量网络安全模型，用于发现和修补漏洞。",
    "https://openai.com/index/a-scorecard-for-the-ai-age":
        "OpenAI CFO Sarah Friar 提出 AI 时代 scorecard，用有效工作、单次成功任务成本、可靠性和算力回报衡量 ROI。",
    "https://openai.com/index/why-teens-deserve-access-safe-ai":
        "OpenAI 说明为什么青少年应能使用安全 AI，并介绍 ChatGPT 的年龄适配保护、学习工具、家长控制和专家合作。",
    "https://deepmind.google/blog/our-approach-to-bioresilience/":
        "Google DeepMind 与 Isomorphic Labs 介绍其 bioresilience 方法，关注 AI 模型在生物安全和生命科学韧性中的负责任使用。",
    "https://openai.com/index/cars24":
        "Cars24 用 OpenAI 语音和聊天 agents 处理每月百万分钟对话、追回流失线索，并把 agentic 工作流带到更多团队。",
    "https://simonwillison.net/2026/Jul/21/nativ/#atom-everything":
        "Simon 介绍 Nativ：基于 MLX 的 macOS 桌面应用，可本地运行 AI 模型，并提供聊天界面和 localhost API。",
    "https://simonwillison.net/2026/Jul/21/cat-and-thariq/#atom-everything":
        "Simon 发布与 Claude Code 团队 Cat Wu 和 Thariq Shihipar 的访谈，讨论 Claude Code、Claude Tag、Fable、安全、评测和工具设计。",
    "https://simonwillison.net/2026/Jul/20/cheap-reverse-engineering/#atom-everything":
        "Simon 认为 coding agents 降低了逆向工程和家庭设备自动化的成本，也降低了试错和未来维护的心理门槛。",
    "https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/#atom-everything":
        "Simon 讨论 Ben Thompson 关于美国模型政策的提议：明确训练数据 fair use，并限制禁止 distillation 的服务条款，以促进开放竞争。",
    "https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything":
        "Simon 引用 2022 年 Sam Altman 邮件，显示 OpenAI 曾考虑发布能在消费级硬件运行的 GPT-3 级本地模型以影响开源竞争格局。",
    "https://simonwillison.net/2026/Jul/19/ai-mania/#atom-everything":
        "Simon 转述 Nik Suresh 对企业 AI 狂热的观察，批评很多 AI 战略缺乏真实使用经验和严肃决策。",
    "https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/#atom-everything":
        "Simon 检查本机 Claude Code 二进制，找到 Bun v1.4 和 Rust 源文件痕迹，验证其已使用 Rust 版 Bun。",
    "https://simonwillison.net/2026/Jul/18/sqlite-query-explainer/#atom-everything":
        "Simon 用 Fable 构建 SQLite Query Explainer，在浏览器中通过 Pyodide 运行 SQLite，并解释 EXPLAIN 与 EXPLAIN QUERY PLAN 输出。",
    "https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms":
        "Sebastian Raschka 讲解如何控制 LLM 的低、中、高 reasoning effort 模式，以及模型如何学习不同推理强度。",
    "https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything":
        "Simon 记录 Anthropic 将 Fable 5 纳入 Max 和 Team Premium，并认为 GPT-5.6 Sol 的竞争让原先移除订阅访问的计划难以维持。",
    "https://simonwillison.net/2026/Jul/18/quixote/#atom-everything":
        "Simon 发现老牌 Python Web 框架 Quixote 仍有最新提交，感叹这个 21 年历史项目仍在维护。",
    "https://simonwillison.net/2026/Jul/17/kimi-k3/#atom-everything":
        "Simon 引述 Kimi K3 在拒绝泄露系统提示后的回复，展示模型个性和安全边界表现。",
    "https://simonwillison.net/2026/Jul/17/llm-cliche-highlighter/#atom-everything":
        "Simon 用 Fable 5 做了 LLM cliche highlighter，用来标出文章中常见的 AI 写作套话。",
    "https://simonwillison.net/2026/Jul/17/spot-birds-not-golf/#atom-everything":
        "Simon 用数据中心用水与高尔夫球场耗水对比，半开玩笑建议 hyperscaler 把球场改成公共公园和观鸟场。",
    "https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything":
        "Simon 介绍 Puter 将 Firefox 编译到 WebAssembly，让完整浏览器运行在另一个浏览器中，并讨论代理网络连接和成本问题。",
    "https://simonwillison.net/2026/Jul/16/kimi-k3/#atom-everything":
        "Simon 梳理 Moonshot Kimi K3 的参数规模、开放权重计划、基准表现和 pelican benchmark 暴露出的模型能力细节。",
    "https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything":
        "Simon 引述 Thibault Sottiaux 对 Codex 删除文件 bug 的说明，指出 full access、无沙箱和错误覆盖 HOME 环境变量的组合风险。",
    "https://simonwillison.net/2026/Jul/16/inkling/#atom-everything":
        "Simon 介绍 Thinking Machines Lab 的开权重模型 Inkling：975B 总参数、41B active 的多模态 MoE，并批评模型卡和训练数据说明过短。",
    "https://simonwillison.net/2026/Jul/16/mermaid-ascii/#atom-everything":
        "Simon 在 Mermaid 转 ASCII 工具中比较 Go 版 mermaid-ascii 与 Grok Build 的 Rust 实现，并用 Claude Fable 5 编译到 WebAssembly。",
    "https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything":
        "Simon 引述 Linus Torvalds 对 Linux 项目使用 AI 的立场：AI 是有用工具，反对者可以 fork 或离开。",
    "http://arxiv.org/abs/2607.18236v1":
        "Patch Policy 让机器人策略直接消费预训练 ViT 的密集 patch tokens，用 block-causal attention 保留时序因果并降低 VLM 级开销。",
    "http://arxiv.org/abs/2607.19345v1":
        "GEAR 针对长上下文推理中的重复复制问题，用证据感知奖励鼓励模型聚焦关键证据而不是无差别复制 prompt。",
    "http://arxiv.org/abs/2607.19344v1":
        "Appearance Pointers 为 Diffusion Transformers 提供区域级多模态控制，让文本或图像外观提示按用户 mask 精准影响生成区域。",
    "http://arxiv.org/abs/2607.19338v1":
        "CodeRescue 将 coding agent 失败后的选择建模为 recovery routing，在继续便宜模型修复和升级强模型之间按预算做决策。",
    "http://arxiv.org/abs/2607.19336v1":
        "论文综述 agentic systems 从研究走向部署时的鲁棒性、安全和可靠性挑战，并结合制药和金融案例讨论工程缓解策略。",
    "http://arxiv.org/abs/2607.19334v1":
        "论文研究如何用 O(log K) 个简单二分类器组合出 K 类分类器，并推导高斯设定下的分布式多分类性能极限。",
    "http://arxiv.org/abs/2607.19331v1":
        "ISO 是面向 RLVR 的固定谱优化框架，利用 base model 权重谱结构并通过奇异向量框架变化获取新能力。",
    "http://arxiv.org/abs/2607.19327v1":
        "论文用卷积神经网络模拟视觉 valence 处理和巴甫洛夫情绪学习，复现人类联想形成与泛化现象。",
    "http://arxiv.org/abs/2607.19326v1":
        "MaLoRA 和 MaRA 在低秩适配中加入选择性状态空间递归，使 adapter 能随 token 和上下文动态变化以提升多跳推理。",
    "http://arxiv.org/abs/2607.19322v1":
        "GAMUT 提出两层 meta-rubric 来评估长文本生成的事实完整性，补足只衡量错误声明的 factuality 评测缺口。",
    "http://arxiv.org/abs/2607.19321v1":
        "ResearchArena 用长程 AI R&D 任务评估不可信 agents 的破坏能力和监控能力，覆盖后训练、CUDA kernel 和推理服务器优化等场景。",
    "http://arxiv.org/abs/2607.19313v1":
        "Off-Context GRPO 用带 privileged guidance 的 rollout 获得非零奖励，再通过重要性校正把更新拉回原始无提示目标。",
    "http://arxiv.org/abs/2607.19312v1":
        "论文构建 16 个大规模模拟轨迹数据集并系统评估 9 种 staypoint detection 算法，揭示现有方法对噪声鲁棒性不足。",
    "http://arxiv.org/abs/2607.19300v1":
        "论文把 LLM 检测视为干预，建模策略性用户行为，指出不完美检测器可能反而增加 LLM 使用并降低输出质量。",
    "http://arxiv.org/abs/2607.19297v1":
        "论文以 LangGraph 为例给出长运行、有状态业务流程的三种 agentic workflow recipe，并说明何时值得使用图式编排。",
    "http://arxiv.org/abs/2607.19281v1":
        "论文用 actor-critic 强化学习合并燃烧反应器微簇，以更好预测燃气轮机 combustor 的 lean blowout 并加速仿真。",
    "http://arxiv.org/abs/2607.19267v1":
        "论文展示权威框架和伪装代码如何让多 agent CI/CD 流水线在看到 secret exfiltration 代码后仍通过验证并部署。",
    "http://arxiv.org/abs/2607.19266v1":
        "论文构建可审计欺诈检测流水线，结合图特征、TreeSHAP 和受限 LLM 调查 agent，并指出图特征在中间风险案例中更有价值。",
    "http://arxiv.org/abs/2607.19262v1":
        "BioSecBench-Surveillance 用 100 个可验证任务评估 AI agents 是否能从病原体测序数据和场景中推断正确分析流程。",
    "http://arxiv.org/abs/2607.19261v1":
        "PathAgentBench 评估 VLM 在全切片病理图像中主动寻找证据、定位诊断区域和整合多尺度证据的能力。",
    "http://arxiv.org/abs/2607.19259v1":
        "论文提出更真实的财报欺诈检测基准 CI-FSFD，结合结构化财务数据和 MD&A 文本来评估跨公司泛化。",
    "http://arxiv.org/abs/2607.19257v1":
        "论文用可控合成语料系统评估 prompt 格式、指令数量和上下文长度如何影响 LLM 指令遵循和幻觉。",
    "http://arxiv.org/abs/2607.19243v1":
        "论文研究 inference-time steering 是否能缓解 LLM 跨语言事实不一致，通过 persona、CAA 和 DPO 等方式让英文提示对齐目标语言知识分布。",
    "http://arxiv.org/abs/2607.19241v1":
        "TAIR 用热力学启发的输入重参数化，降低超临界燃烧中真实流体热物性神经预测的回归难度。",
    "http://arxiv.org/abs/2607.19235v1":
        "MeetingToM 评估多模态 LLM 在多人会议中推断信念、意图、共识和隐藏分歧等 Theory-of-Mind 能力。",
    "http://arxiv.org/abs/2607.19232v1":
        "S3 在层级强化学习中用粗粒度动态不确定性约束子目标选择，使高层策略更稳定地规划长程任务。",
    "http://arxiv.org/abs/2607.19226v1":
        "论文分析神经机器翻译中 RLVR 推理轨迹的质量收益与 token 成本，量化 reasoning 的成本-质量权衡。",
    "http://arxiv.org/abs/2607.19223v1":
        "AdaFlash 通过 on-policy 蒸馏和自适应机制改进扩散 draft model 的 speculative decoding，缓解不同领域和位置的接受率波动。",
    "http://arxiv.org/abs/2607.19219v1":
        "RLAES 用 rubric rewards 强化学习联合优化作文评分和反馈生成，并用细粒度反馈评估降低开销、提升反馈质量。",
    "http://arxiv.org/abs/2607.19213v1":
        "报告展望无人机计算基础设施未来，列出大规模机群、自主性、边云协同、安全验证等 12 个关键挑战。",
    "http://arxiv.org/abs/2607.19209v1":
        "论文比较聚类和 LLM 方法评估计算教育中的团队 tabletop exercises，帮助教师更快给出基于行为的团队反馈。",

    # 2026-07-16 OpenAI / Google DeepMind / Simon Willison / arXiv
    "https://openai.com/index/advancing-ai-safety-through-state-and-federal-action":
        "OpenAI 讨论美国 AI 安全治理中的州级与联邦行动，强调州法可为全国性的安全、民主 AI 框架提供实践基础。",
    "https://openai.com/index/unlocking-self-improvement-gpt-red":
        "OpenAI 介绍 GPT-Red：通过自动化红队和自博弈方式提升模型鲁棒性、对齐和抵御提示注入等安全风险的能力。",
    "https://openai.com/index/managing-ai-investments-in-agentic-era":
        "OpenAI 建议在 agentic era 用『每美元完成的有效工作』衡量 AI 投资，优先提升效率并扩展高价值工作流。",
    "https://deepmind.google/blog/empowering-indias-next-generation-of-innovators-with-atl-saathi/":
        "Google 与 AIM 推出 ATL Saathi，用 Gemini 驱动的 AI 工具帮助印度教育者在 robotics labs 中设计、指导和评估学生创新项目。",
    "https://openai.com/academy/getting-started":
        "OpenAI Academy 发布 ChatGPT 入门指南，帮助新用户开始对话，并用于写作、头脑风暴、学习和解决问题。",
    "https://simonwillison.net/2026/Jul/16/grok-mermaid/#atom-everything":
        "Simon 发现 Grok CLI 开源代码里的 Rust Mermaid 终端渲染器，并基于 WASM 做了一个浏览器版 Mermaid 转 Unicode 框线工具。",
    "https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything":
        "Simon 记录 xAI 开源 Grok Build：在整目录上传引发争议后，项目移除相关上传/保留逻辑并以 Apache 2.0 释出。",
    "https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything":
        "Simon 介绍 Ayush Paul 发现的 Claude web_fetch 漏洞：嵌套抓取 URL 可绕过防护并外传敏感数据。",
    "https://simonwillison.net/2026/Jul/14/github-changeling/#atom-everything":
        "Simon 引述 GitHub Changelog：Dependabot 默认在新版本发布 3 天后才创建版本更新 PR，以减少供应链风险。",
    "https://simonwillison.net/2026/Jul/14/pedalican/#atom-everything":
        "Simon 用 Codex Desktop 和 GPT-5.6/gpt-image-2 做了自定义桌面宠物 pedalican，一只骑车的鹈鹕角色。",
    "https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything":
        "Simon 记录 Lobsters 从 MariaDB 迁移到 SQLite 后运行在单台 VPS 上，CPU、内存和成本都明显下降。",
    "https://simonwillison.net/2026/Jul/14/armin-ronacher/#atom-everything":
        "Simon 引述 Armin Ronacher：项目的共同语言来自概念、边界、不变量和所有权的共享理解，部分摩擦反而能同步团队和 agents。",
    "https://simonwillison.net/2026/Jul/14/datasette/#atom-everything":
        "Simon 发布 datasette 1.0a37，小幅改进权限性能和文档，并回滚了会破坏插件的 cosmetic API 变更。",
    "https://simonwillison.net/2026/Jul/14/uvx-github-actions-cache/#atom-everything":
        "Simon 分享在 GitHub Actions 中用 uvx 的缓存友好写法，通过 UV_EXCLUDE_NEWER 让依赖缓存键更稳定。",
    "https://simonwillison.net/2026/Jul/13/doomql/#atom-everything":
        "Simon 展示 GPT-5.6 Sol 生成的 DOOMQL：用 SQLite/SQL 实现移动、碰撞、敌人、战斗和 ray tracing 的 Doom 风格游戏。",
    "https://simonwillison.net/2026/Jul/13/datasette-code-frequency/#atom-everything":
        "Simon 用 GitHub code-frequency 图观察 datasette 开发峰值，并把它与 Opus 4.8、GPT-5.5、Fable 5 和 GPT-5.6 的发布时间联系起来。",
    "https://simonwillison.net/2026/Jul/12/directly-responsible-individuals/#atom-everything":
        "Simon 强调 AI agents 不应成为 DRI，因为责任、问责和最终判断仍必须由人承担。",
    "https://simonwillison.net/2026/Jul/12/shot-scraper/#atom-everything":
        "Simon 发布 shot-scraper 1.11，改进服务器启动等待、JS 文件参数和超时相关行为。",
    "https://simonwillison.net/2026/Jul/12/bump/#atom-everything":
        "Simon 记录 Anthropic 因 GPT-5.6 竞争压力延长 Fable 5 访问和速率限制，并认为 Fable 应继续保留。",
    "https://simonwillison.net/2026/Jul/12/sqlite-utils/#atom-everything":
        "Simon 发布 sqlite-utils 4.1.1，修复 table.transform() 在事务、外键和 ON DELETE 组合下的边界问题，并补充文档链接。",
    "http://arxiv.org/abs/2607.14049v1":
        "论文提出 Deep Interaction，让人直接编辑错误的 CoT 片段并把修正后的推理蒸馏进提示，从而更高效地改进大推理模型输出。",
    "http://arxiv.org/abs/2607.14046v1":
        "Earthquaker-AI 把 RAG、评分量规和 Lego WeDo2 机器人结合，用于小学地震教育中的安全知识学习与反馈。",
    "http://arxiv.org/abs/2607.14044v1":
        "论文提出端到端 AI 加速 upskilling 框架，覆盖知识获取、内容开发、评审、教学和评估，并用 CPE 学分和 NVIDIA 考试通过率验证。",
    "http://arxiv.org/abs/2607.14040v1":
        "论文提出面向长文档/语料上下文的 RAG 翻译方法，试图把 LLM 翻译能力从句子级扩展到整篇文本层面。",
    "http://arxiv.org/abs/2607.14037v1":
        "论文分析 2361 个 GitHub 项目的 25264 个 agentic PR，发现 agentic coding 采用集中在少数项目，但小项目参与度更高。",
    "http://arxiv.org/abs/2607.14006v1":
        "论文重新定义 AI 系统渗透测试，从资源攻陷转向通过提示、检索、记忆、工具和人机循环造成行为目标违规。",
    "http://arxiv.org/abs/2607.14004v1":
        "论文在 Terminal-Bench 2.0 上评估 agent optimizer 的连续学习能力，比较 GEPA、Meta Harness 和 RELAI-VCL 的收益能否跨任务复合。",
    "http://arxiv.org/abs/2607.14001v1":
        "论文把 Lyapunov 指数用作物理信息密集奖励，使强化学习 agent 发现倒立摆稳定控制策略，包括振荡和直立稳定。",
    "http://arxiv.org/abs/2607.13998v1":
        "DVM-HALL/NHAS 建模自主商务中人类情感忠诚、机器效用、信任和授权如何共同影响 AI agent 的购买决策。",
    "http://arxiv.org/abs/2607.13988v1":
        "TRACE 在工具调用边界估计长程 agent 的 turn-level credit，把奖励更细粒度地分配到多轮行动中。",
    "http://arxiv.org/abs/2607.13978v1":
        "论文把音乐到舞蹈生成拆成可解释的 atomic movements，通过动作分割、聚类和 LLM 重新标注提升结构化编舞能力。",
    "http://arxiv.org/abs/2607.13977v1":
        "CAVE-ABSA 用约束感知编辑生成方面级情感分析反事实样本，同时保持非目标方面、语义、流畅性和事实一致性。",
    "http://arxiv.org/abs/2607.13940v1":
        "HealthClaw 是自进化个人健康管理 agent，把安全规则和医学知识与私有长期记忆分离，并持续更新偏好、习惯和流程。",
    "http://arxiv.org/abs/2607.13921v1":
        "Generative Compilation 在代码生成过程中把部分程序转换为可编译诊断的完整程序，让编译器反馈实时指导 AI 生成。",
    "http://arxiv.org/abs/2607.13920v1":
        "DeepStress 用可控合成证据的可靠性、可信度、相关性和事实性变化，压力测试 deep search agents 的推理稳定性。",
    "http://arxiv.org/abs/2607.13918v1":
        "论文为部分相关 verifier cascades 建立理论，说明多重验证的可靠性增长会因相关性和 blind spot 而从指数变成多项式甚至饱和。",
    "http://arxiv.org/abs/2607.13901v1":
        "论文在巴斯克语、西班牙语和英语教育场景中研究高阶问题生成，比较 CER 和 Divergent Questioning 等框架对教师认可度的影响。",
    "http://arxiv.org/abs/2607.13899v1":
        "AIMO Interpretability Challenge 旨在用模型内部机制区分数学模型的稳健推理与脆弱捷径，并建立新的鲁棒性基准。",
    "http://arxiv.org/abs/2607.13884v1":
        "Experience Memory Graph 把 agent 失败恢复建模为图匹配问题，从成功/失败轨迹中提取可复用修正路径用于一次性纠错。",
    "http://arxiv.org/abs/2607.13881v1":
        "AgentHOI 是无需训练的人物-物体交互检测框架，调度多模态基础模型进行开放语义推理和空间 grounding。",
    "http://arxiv.org/abs/2607.13880v1":
        "论文提出 SVR-MARL，用于多 AUV 隐蔽协作任务中衡量感知信息对任务的真实价值，并在通信约束下优化共享。",
    "http://arxiv.org/abs/2607.13854v1":
        "SPyCE 让多模态 agent 的技能库与策略在强化学习中共同演化，把视觉工具使用轨迹蒸馏成可复用执行技能和工作流技能。",
    "http://arxiv.org/abs/2607.13801v1":
        "TA-RS 是面向 LLM 网络入侵检测的认证防御，只在攻击者可控流量特征子空间注入噪声以提升对流量扰动的鲁棒性。",
    "http://arxiv.org/abs/2607.13770v1":
        "Kaleido 利用视频扩散 Transformer latent space 的时空相关性做算法-硬件协同设计，通过通道级复用和专用加速器降低计算成本。",
    "http://arxiv.org/abs/2607.13753v1":
        "论文分析 SFT、RL 和 OPD 如何改变 CoT 前、中、后的置信度校准，并提出位置感知 PosConf 改进答案聚合。",
    "http://arxiv.org/abs/2607.13737v1":
        "论文比较量子和经典 topology-aligned 分子性质预测架构，显示按分子键图对齐的归纳偏置能在低数据场景提升参数效率。",
    "http://arxiv.org/abs/2607.13721v1":
        "论文用 WavLM 自监督表示和 DTW 比较学习者与母语者语音，为二语音素、节奏和语调评分提供低资源、无文本方案。",
    "http://arxiv.org/abs/2607.13718v1":
        "论文调研 21 个 AI agent 权限系统，梳理用户如何表达权限、系统如何转成内部策略并在运行时执行。",
    "http://arxiv.org/abs/2607.13716v1":
        "CAVA 为异构 agent runtime 的操作记录生成规范化 action object，支持审批绑定、收据完整性和跨运行时治理验证。",
    "http://arxiv.org/abs/2607.13712v1":
        "Groc-PO 针对多模态模型幻觉，把偏好优化细化到对象 grounding、上下文 grounding 和推理阶段，以减少早期 grounding 错误传播。",

    # 2026-07-12 OpenAI / Simon Willison / Lilian Weng
    "https://openai.com/index/deutsche-telekom":
        "OpenAI 案例介绍 Deutsche Telekom 如何用 AI 改造电信业务，覆盖客服、员工工作流、网络运营和未来语音体验。",
    "https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot":
        "OpenAI 宣布 GPT-5.6 成为 Microsoft 365 Copilot 首选模型，增强 Word、Excel、PowerPoint、Chat 和 Cowork 等场景的工作质量与速度。",
    "https://openai.com/index/bio-bug-bounty":
        "OpenAI 发布 GPT-5.5 Bio Bug Bounty 项目细节，鼓励外部发现生物安全相关模型风险。",
    "https://openai.com/index/chatgpt-for-your-most-ambitious-work":
        "OpenAI 推出 ChatGPT Work：可跨应用和文件行动、长时间跟进项目，并把目标推进成完成工作的 agent。",
    "https://openai.com/index/gpt-5-6":
        "OpenAI 发布 GPT-5.6 系列，强调每 token 更高智能、更强性价比，以及面向高难任务的 Luna/Terra/Sol 分层能力。",
    "https://simonwillison.net/2026/Jul/11/sqlite-utils/#atom-everything":
        "Simon 发布 sqlite-utils 4.1：新增 insert/upsert 的 --code 行生成、列类型覆盖、drop-index 命令等小功能。",
    "https://simonwillison.net/2026/Jul/10/nilay-patel/#atom-everything":
        "Simon 引述 Nilay Patel：真正可用的 AR 眼镜需要持续摄像和云端处理，这带来巨大隐私代价，社会也许不该接受这种权衡。",
    "https://simonwillison.net/2026/Jul/10/openai/#atom-everything":
        "Simon 引述 OpenAI 对 ChatGPT Work 云端/桌面线程和本地文件权限的说明，并认为这个澄清仍不够清楚。",
    "https://simonwillison.net/2026/Jul/9/gpt-5-6/#atom-everything":
        "Simon 梳理 GPT-5.6 Luna/Terra/Sol：百万上下文、128K 输出、不同价格档，并关注 OpenAI 关于长程 agentic 工作流和成本效率的基准说法。",
    "https://simonwillison.net/2026/Jul/9/muse-spark-1-1/#atom-everything":
        "Simon 介绍 Meta Muse Spark 1.1：首个提供 API 的 Spark 模型，改进 agentic tool calling 和 computer use，并发布 llm-meta-ai 插件试用。",
    "https://simonwillison.net/2026/Jul/9/llm-meta-ai/#atom-everything":
        "Simon 发布 llm-meta-ai 0.1，让 LLM 命令行工具可调用 Meta 的 muse-spark-1.1 模型。",
    "https://simonwillison.net/2026/Jul/9/llm/#atom-everything":
        "Simon 发布 llm 0.31.1，修复 OpenAI Chat Completions 端点在空 tool call arguments 下触发 JSON 错误的问题。",
    "https://lilianweng.github.io/posts/2026-07-04-harness/":
        "Lilian Weng 长文讨论用于自我改进的 harness engineering：把递归自我改进扩展到训练流水线、部署系统和模型迭代闭环。",

    # 2026-07-10 OpenAI / Simon Willison / arXiv
    "https://openai.com/index/government-national-security-partnerships":
        "OpenAI 说明其政府和国家安全合作原则，强调负责任 AI 使用、民主问责和公共安全。",
    "https://openai.com/index/separating-signal-from-noise-coding-evaluations":
        "OpenAI 分析 SWE-Bench Pro 等编码评测中的可靠性问题，提醒热门基准可能含噪声并影响模型能力判断。",
    "https://openai.com/index/k-12-educators-practical-skills":
        "OpenAI Academy 与 Walton Family Foundation 为 K-12 教师提供 AI Skills Jams，帮助教师掌握课堂可用的实操 AI 技能。",
    "https://openai.com/index/introducing-gpt-live":
        "OpenAI 发布 GPT-Live：面向自然人机语音交互的新一代语音模型，并用于新版 ChatGPT Voice。",
    "https://openai.com/index/australian-payments-plus":
        "Australian Payments Plus 用 ChatGPT Enterprise 和 Codex 加速支付系统开发与运营，在复杂支付场景中节省时间并保持人工判断。",
    "https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/#atom-everything":
        "Simon 推荐 Jarred Sumner 讲述 Bun 从 Zig 重写到 Rust 的长文，重点是 agentic engineering、动态工作流、试跑和对抗式审查等方法。",
    "https://simonwillison.net/2026/Jul/8/introducing-gptlive/#atom-everything":
        "Simon 试用 GPT-Live，认为新版 ChatGPT Voice 明显更强，可把复杂问题委派给 GPT-5.5 并保持语音对话流。",
    "https://simonwillison.net/2026/Jul/8/kenton-varda/#atom-everything":
        "Simon 引述 Kenton Varda：团队暂停使用 AI 写 PR/commit/issue 描述，因为它常复述代码细节却缺少高层意图。",
    "https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything":
        "Simon 发布 sqlite-utils 4.0：加入数据库 schema migrations、嵌套事务和复合外键支持，是 2020 年以来首次大版本升级。",
    "https://simonwillison.net/2026/Jul/7/sqlite-migrate/#atom-everything":
        "Simon 发布 sqlite-migrate 0.2，把该库退役为基于 sqlite-utils 4.0 的兼容层。",
    "https://simonwillison.net/2026/Jul/7/github-code-component/#atom-everything":
        "Simon 用 GPT-5.5 做了 github-code Web Component，可从 GitHub URL 抓取指定代码行并嵌入网页展示。",
    "https://simonwillison.net/2026/Jul/7/sqlite-utils/#atom-everything":
        "Simon 发布 sqlite-utils 4.0，并指向数据库 schema migrations 等详细说明。",
    "https://simonwillison.net/2026/Jul/7/sqlite-utils-2/#atom-everything":
        "Simon 发布 sqlite-utils 4.0rc4，这是稳定版前最后一个 RC，主要落实 Claude Fable 5 详细审查反馈。",
    "https://simonwillison.net/2026/Jul/6/hy3/#atom-everything":
        "Simon 介绍腾讯 Hy3：Apache 2.0 许可的 295B MoE 模型，21B 激活参数、256K 上下文，号称追平更大开源旗舰模型。",
    "https://simonwillison.net/2026/Jul/6/sqlite-utils/#atom-everything":
        "Simon 发布 sqlite-utils 4.0rc3，加入复合外键 introspection/创建支持和大小写不敏感列名等稳定版前改动。",
    "http://arxiv.org/abs/2607.07708v1":
        "SciReasoner：面向蛋白、小分子和无机晶体的多模态科学基础模型，用原生结构表征解释结构-性质关系并保持推理透明。",
    "http://arxiv.org/abs/2607.07707v1":
        "Co-LMLM：把事实知识外置到连续向量查询的知识库中，让有限记忆语言模型在生成时检索可归因文本知识，提升困惑度和事实精度。",
    "http://arxiv.org/abs/2607.07702v1":
        "STRACE：从长轨迹中挖掘代表性失败并定位因果根因，为反思式 agent 优化构造高信噪比上下文。",
    "http://arxiv.org/abs/2607.07696v1":
        "Jailbreak：用 LLM 根据数据库源码和文档生成高性能存储文件 reader，绕过 JDBC/ODBC 驱动直接读取 PostgreSQL/MySQL 数据。",
    "http://arxiv.org/abs/2607.07695v1":
        "Institutional Red-Teaming：固定多 agent 与任务状态、只改变部署规则，证明规则本身会因果性改变集体安全结果。",
    "http://arxiv.org/abs/2607.07693v1":
        "面向 diffusion RLHF 的样本高效方法：选择性加权关键去噪 timestep，并用 advantage-based replay 复用高信息轨迹。",
    "http://arxiv.org/abs/2607.07690v1":
        "Agon：让两个可比模型互为竞争对手和隐式 grader，通过互相读解并超越对方来训练更好的推理过程。",
    "http://arxiv.org/abs/2607.07676v1":
        "SkillCenter：包含 216,938 个结构化技能的大规模 agent 技能库，结合来源引用、SkillGate 质量筛选和 SQLite FTS 离线检索。",
    "http://arxiv.org/abs/2607.07674v1":
        "AdaPrefix-GRPO：动态给难题加入参考解前缀，把成功率控制在约 50% 以最大化 GRPO 信号，再逐步撤掉辅助。",
    "http://arxiv.org/abs/2607.07673v1":
        "MedPMC：从 610 万篇 PMC 文章中构建 1100 万医学图文对，为医学多模态基础模型提供高保真、可持续更新的数据基础设施。",
    "http://arxiv.org/abs/2607.07670v1":
        "研究 Bielik 模型激活分散度：单次前向即可区分已知/虚构实体，但熟悉度信号不等同于事实可靠性。",
    "http://arxiv.org/abs/2607.07669v1":
        "DiaLLM：系统比较英语方言适配，发现模型理解方言和生成方言是分离问题，强奖励优化不一定得到人类偏好的方言输出。",
    "http://arxiv.org/abs/2607.07646v1":
        "受控重写语法实验表明 RL 后训练不只是放大已有技能，还能把原始能力组合成稳定复用的高阶推理策略。",
    "http://arxiv.org/abs/2607.07640v1":
        "ALER-TI：时间序列插补的检索增强框架，用潜在嵌入对齐从历史模式中补充局部缺失上下文。",
    "http://arxiv.org/abs/2607.07626v1":
        "Future Confidence Distillation：用解答后的置信度探针蒸馏到解答前隐藏表征，使模型在生成前预测答案可靠性。",
    "http://arxiv.org/abs/2607.07612v1":
        "综述 agentic AI governance：梳理 agentic AI 相比传统系统的差异、治理优先级、机制和利益相关方角色。",
    "http://arxiv.org/abs/2607.07601v1":
        "CARLA-GS：把视觉表示、场景推理和物理仿真解耦结合，用于生成自动驾驶安全评估中的照片级 corner cases。",
    "http://arxiv.org/abs/2607.07557v1":
        "PALS：按层 99 分位激活幅度调整 LLM 剪枝稀疏率，在 LLaMA-2-7B 上优于统一 Wanda 剪枝且几乎无额外成本。",
    "http://arxiv.org/abs/2607.07548v1":
        "分层搜索 agent 容量研究：复杂问答中应把更强模型放在任务分解/delegation 角色，执行子 agent 可缩小以省 token。",
    "http://arxiv.org/abs/2607.07527v1":
        "提出统一 AI 内容/产物检测框架，用 Mahalanobis 距离分数检测 LLM 文本、幻觉、水印和对抗样本。",
    "http://arxiv.org/abs/2607.07521v1":
        "结构设计中的人机共创研究：主张保留有益『摩擦』，让 AI 帮助探索方案而不是直接给最终答案。",
    "http://arxiv.org/abs/2607.07513v1":
        "从理论上解释数据增强图正则为何能让半监督学习以更少标签达到更快收敛率，并把增强质量写入误差界。",
    "http://arxiv.org/abs/2607.07508v1":
        "SAO：面向长程 agentic RL 的单 rollout 异步优化，替代 group-wise GRPO 并改进稳定性和泛化。",
    "http://arxiv.org/abs/2607.07507v1":
        "HIVE：研究视觉语言模型在幻觉语义进入上下文后的后续推理，比较真实 caption 与幻觉 caption 的任务影响。",
    "http://arxiv.org/abs/2607.07504v1":
        "数据科学工作流消融显示：LLM 自动生成的 skill 文件相较无 skill 提示并未带来可靠性能提升。",
    "http://arxiv.org/abs/2607.07498v1":
        "RAID：在 NHL26 守门员 AI 测试中用强化学习自动发现多样化得分漏洞，减少人工反复 playtest 成本。",
    "http://arxiv.org/abs/2607.07494v1":
        "GIFT：用几何感知坐标做低精度梯度通信，降低 LLM 预训练通信瓶颈并更好保留梯度方向。",
    "http://arxiv.org/abs/2607.07492v1":
        "Pyligent：把推理训练建模为可验证搜索树，显式监督 continue/finish/backtrack，教模型从失败分支恢复。",
    "http://arxiv.org/abs/2607.07474v1":
        "提出工具型 AI agent 的 action-graded harm scale，用 7 级动作危害替代二元攻击成功率来衡量 red-team 风险。",
    "http://arxiv.org/abs/2607.07469v1":
        "SynthAVE：面向电商属性抽取的多语言大规模合成标注基准，用多 LLM arena 多数投票验证标签质量。",

    # 2026-07-06 OpenAI / Google DeepMind / Simon Willison
    "https://deepmind.google/blog/google-deepmind-and-a24-announce-first-of-its-kind-research-partnership/":
        "Google DeepMind 与 A24 宣布研究合作，探索 AI 与电影创作结合的新形式。",
    "https://deepmind.google/blog/start-building-with-nano-banana-2-lite-and-gemini-omni-flash/":
        "Google DeepMind 开放 Nano Banana 2 Lite 与 Gemini Omni Flash，面向开发者提供更快、更便宜的图像/视频多模态生成能力。",
    "https://openai.com/index/how-chatgpt-adoption-has-expanded":
        "OpenAI Signals 数据显示 ChatGPT 采用率正在全球扩大，用户使用频率、能力探索和跨地区/语言增长都在提升。",
    "https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug":
        "OpenAI 工程师用大规模 core dump 分析排查罕见基础设施崩溃，最终同时发现硬件故障和一个存在 18 年的软件 bug。",
    "https://openai.com/index/genebench-pro/case-studies":
        "OpenAI 通过 GeneBench-Pro 案例展示 AI 在基因组学、生物学和科学研究任务中的表现与局限。",
    "https://openai.com/index/introducing-genebench-pro":
        "OpenAI 发布 GeneBench-Pro：一个用复杂真实数据集评测 AI 在基因组学、生物学和科学研究中能力的新基准。",
    "https://openai.com/index/mapping-ai-jobs-transition-eu":
        "OpenAI 报告绘制欧洲 AI 劳动力机会图谱，分析欧盟不同职业面临的自动化、增长和工作流变化。",
    "https://openai.com/index/hp-frontier-partnership":
        "HP Inc. 扩大与 OpenAI 的 Frontier 战略合作，把 AI 部署到客户体验、软件开发和企业运营等场景。",
    "https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/#atom-everything":
        "Simon 记录 Claude Fable 帮他推进 sqlite-utils 4.0rc2 的过程：模型发现多个发布阻塞问题，总代价约 149.25 美元。",
    "https://simonwillison.net/2026/Jul/5/sqlite-utils/#atom-everything":
        "Simon 发布 sqlite-utils 4.0rc2，并指向一篇更详细的 Claude Fable 辅助开发复盘。",
    "https://simonwillison.net/2026/Jul/4/building-a-world-map-with-only-500-bytes/#atom-everything":
        "Simon 分享 Iwo Kadziela 借助 Codex 用 445 字节数据和 deflate 压缩生成可信 ASCII 世界地图的技巧。",
    "https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything":
        "Simon 转述 Armin 的观察：更新的 Claude 模型在某些非 Claude Code 的编辑工具 schema 上反而更容易生成错误参数，可能是专门强化 Claude Code 工具使用的副作用。",
    "https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything":
        "Simon 介绍 Current AI 的 Open Source AI Gap Map：索引开源 AI 栈中的软件、模型、数据集和硬件项目，并开源底层 YAML 数据。",
    "https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything":
        "Simon 引述 Josh W. Comeau：AI 让开发课程销售显著下滑，一方面人们担心开发岗位，另一方面 LLM 替代了部分个性化教学需求。",
    "https://simonwillison.net/2026/Jul/3/judgement/#atom-everything":
        "Simon 总结 Claude Code 团队建议：让 Fable 自行判断何时测试、何时委派低功耗模型，往往比硬性规定流程更有效也更省 token。",
    "https://simonwillison.net/2026/Jul/3/june-newsletter/#atom-everything":
        "Simon 发布 2026 年 6 月赞助者月刊，涵盖 Claude Fable 5、GPT-5.6、出口限制、GLM-5.2、Datasette、sqlite-utils 和其他模型发布。",
    "https://simonwillison.net/2026/Jul/2/llm-coding-agent/#atom-everything":
        "Simon 发布 llm-coding-agent 0.1a0：用自己的 llm 库搭建的 Claude Code 风格 Python coding agent，支持读写文件、执行命令和 API/CLI 使用。",
    "https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything":
        "Simon 用 Claude Fable 5 和 DSPy 评估 Datasette Agent 的 SQL 系统提示词，发现 schema 信息不足会诱发列名猜测和错误重试。",
    "https://simonwillison.net/2026/Jul/2/understand-to-participate/#atom-everything":
        "Simon 转述 Geoffrey Litt 的观点：和 coding agents 协作时要『理解到足以参与』，避免随着 agent 写出大型改动而积累认知债。",
    "https://simonwillison.net/2026/Jun/30/anthropic/#atom-everything":
        "Simon 引述 Anthropic：美国商务部已解除 Claude Fable 5 和 Mythos 5 的出口限制，Anthropic 将开始恢复访问。",
    "https://simonwillison.net/2026/Jun/30/nano-banana-2-lite/#atom-everything":
        "Simon 试用 Nano Banana 2 Lite（Gemini 3.1 Flash Lite Image），认为它是最快最便宜的 Gemini 图像模型，但仍会拼错图中文字。",
    "https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything":
        "Simon 梳理 Claude Sonnet 5 的 API/模型变化：接近 Opus 4.8、百万 token 上下文、128K 输出、adaptive thinking 默认开启、采样参数不再支持。",
    "https://simonwillison.net/2026/Jun/30/the-ai-compass/#atom-everything":
        "Simon 推荐 AI Compass：一个政治罗盘式 AI 伦理问卷，可将回答者归入 30 种 AI 立场原型。",
    "https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything":
        "Simon 发布 shot-scraper video：让 agent 用 storyboard.yml 和 Playwright 录制自己工作的网页视频 demo。",
    "https://simonwillison.net/2026/Jun/30/shot-scraper/#atom-everything":
        "Simon 发布 shot-scraper 1.10，核心新功能是基于 storyboard.yml 录制网页操作视频。",
    "https://simonwillison.net/2026/Jun/29/html-table-extractor/#atom-everything":
        "Simon 发布 HTML table extractor：可把从浏览器粘贴来的富文本表格转换为 HTML、Markdown、CSV、TSV 或 JSON，并支持从 Wikipedia 导入表格。",
    "https://simonwillison.net/2026/Jun/29/safari-tab-count/#atom-everything":
        "Simon 分享一条 AppleScript 小技巧，用一行命令统计 Safari 当前打开的标签页数量。",
    "https://simonwillison.net/2026/Jun/29/ornith/#atom-everything":
        "Simon 试用 MIT 许可的 Ornith-1.0 开放权重模型：它基于 Gemma 4 和 Qwen 3.5，在 agentic coding 基准上表现强，并能在本地 harness 中连续调用工具。",
    "https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything":
        "Simon 引述 Jon Udell：与其说『human in the loop』，不如把循环视为人主导并邀请 agent 加入的协作过程。",
    "https://simonwillison.net/2026/Jun/28/hack-your-summer/#atom-everything":
        "Simon 介绍 Hack Your Summer：面向学生和应届毕业生的 4 周高强度项目冲刺，作为实习机会减少时的替代实践路径。",

    # 2026-06-28 Sebastian Raschka / Simon Willison
    "https://magazine.sebastianraschka.com/p/using-local-coding-agents":
        "Sebastian Raschka 介绍如何用本地 coding harness 搭配开放权重模型，作为 Claude Code / Codex 订阅之外的本地编码 agent 方案。",
    "https://simonwillison.net/2026/Jun/26/dean-w-ball/#atom-everything":
        "Simon 引述 Dean W. Ball：前沿模型发布延迟会压缩实验室回收训练成本的窗口，也会削弱面向全球市场建设 AI 基础设施的经济逻辑。",
    "https://simonwillison.net/2026/Jun/26/timothy-b-lee/#atom-everything":
        "Simon 引述 Timothy B. Lee：认为 LLM 没有学习曲线，就像说当经理不需要学习、员工会自动照做一样，是对使用技能的误解。",
    "https://simonwillison.net/2026/Jun/26/hack-my-ai-assistant/#atom-everything":
        "Simon 记录一次 OpenClaw 邮件攻击挑战：约 2000 人、6000 次尝试都未成功泄露 secret，显示前沿模型的抗提示注入训练已有明显进展。",
    "https://simonwillison.net/2026/Jun/26/incident-report/#atom-everything":
        "Simon 转发一篇讽刺性事故报告：两个 AI 代码审查 agent 围绕供应链包是否恶意陷入争论循环，最终烧掉巨额推理费用。",

    # 2026-06-27 OpenAI / Simon Willison / Lilian Weng
    "https://openai.com/index/previewing-gpt-5-6-sol":
        "OpenAI 预览 GPT-5.6 Sol：在编码、科学与网络安全上能力更强的下一代旗舰模型，配套其最先进的安全栈；系列还含均衡款 Terra（性能接近 5.5 但便宜 2 倍）与低成本快速款 Luna，未来数周将逐步开放。",
    "https://openai.com/index/how-agents-are-transforming-work":
        "OpenAI 新研究论文展示 AI agent 如何改变工作：让模型能完成更长、更复杂的任务，并在各类岗位上扩大生产力。",
    "https://simonwillison.net/2026/Jun/26/openai/#atom-everything":
        "Simon 引述 OpenAI GPT-5.6 系列预览公告（旗舰 Sol、均衡 Terra、快速廉价 Luna），并提到 OpenAI 在发布前向美国政府预先通报了相关计划。",
    "https://simonwillison.net/2026/Jun/25/ai-and-liability/#atom-everything":
        "Simon 引述 Bruce Schneier 对德国判决（Google 须为其 AI 概览中的错误担责）的评论：AI agent 是部署方的代理人，法律应据此追责，不能让企业拿『AI 出错』当免责借口。",
    "https://simonwillison.net/2026/Jun/25/datasette-export-database/#atom-everything":
        "Simon 发布 datasette-export-database 0.3a2：一个极小的修复版，把 pyproject.toml 里写死的 datasette==1.0a27 改成 >=1.0a27，解除与其他 Datasette 版本的不兼容。",
    "https://simonwillison.net/2026/Jun/24/browser-compat-db/#atom-everything":
        "Simon 受 Mozilla 新 MDN MCP 服务启发，用 Claude Code for web（Opus 4.8）生成的 sqlite-utils 脚本，把 mdn/browser-compat-data 转成约 66MB 的 SQLite 数据库，并设法通过 GitHub CDN 带开放 CORS 头分发。",
    "https://simonwillison.net/2026/Jun/24/tom-macwright/#atom-everything":
        "Simon 引述 Tom MacWright：越来越多求职申请明显由 LLM 代写——简历、作品集站点、GitHub 项目乃至提交信息全是生成的，结果千篇一律、毫无个人真实信息，让招聘者无从了解这个人。",
    "https://lilianweng.github.io/posts/2026-06-24-scaling-laws/":
        "Lilian Weng 长文《Scaling Laws, Carefully》：把缩放定律视为描述算力、损失、模型规模与数据关系的框架，核心是如何在模型规模 N 与数据量 D 之间最优分配宝贵算力。",

    # 2026-06-27 arXiv
    "http://arxiv.org/abs/2606.27377v1":
        "DanceOPD：面向 flow-matching 模型的在策略生成场蒸馏框架，把文生图、局部编辑、全局编辑统一进单一模型并化解三者相互冲突的训练难题。",
    "http://arxiv.org/abs/2606.27369v1":
        "RiVER：无需标准答案也能训练 LLM 的可验证强化学习框架，用确定性执行反馈作为连续值监督，并解决连续奖励下『尺度主导』等优化难题。",
    "http://arxiv.org/abs/2606.27361v1":
        "自回归玻尔兹曼生成器：用自回归模型替代归一化流来构建 Boltzmann Generator，兼顾表达力与可负担的精确似然，高效采样分子平衡态。",
    "http://arxiv.org/abs/2606.27359v1":
        "系统量化『序列概率高是否等于答案正确』：跨解码方法、模型与基准在四个层级上分析序列概率与正确性的对齐程度，给出何时『更可能的答案才更对』。",
    "http://arxiv.org/abs/2606.27347v1":
        "用全开源的多语言联合实体-关系抽取流水线，大规模绘制欧洲政治精英网络，替代昂贵的人工编码与简单共现方法。",
    "http://arxiv.org/abs/2606.27342v1":
        "研究领域感知的分布对齐在『预算受限实体匹配』中的表现：以 SOTA 方法 BEACON 为对象，分析其在不同数据约束与监督水平下的行为。",
    "http://arxiv.org/abs/2606.27334v1":
        "基于语言的数字孪生：用 LLM 结合文体线索与上下文元数据模拟老年人对话行为，作为非侵入式生物标志辅助轻度认知障碍（MCI）的早期检测。",
    "http://arxiv.org/abs/2606.27330v1":
        "PEEU：让 GUI agent 自主探索环境发现经验、并利用事后经验合成严格对齐的高质量规划数据，提升小型开源多模态模型的任务规划与跨网站泛化。",
    "http://arxiv.org/abs/2606.27316v1":
        "德国央行实践：用 LLM 从冗长、半结构化、常为双语的证券募集说明书中抽取抵押品合格性条款，克服传统 NER 在 OCR 噪声与语言变体上的局限。",
    "http://arxiv.org/abs/2606.27314v1":
        "提出面向机制的『间接语言编码（ILE）』分类法，抽象掉沟通目的、按意义编码与还原的底层操作归类算法黑话/委婉语/对抗性混淆，并将其嵌入 LLM 提示提升隐语检测。",
    "http://arxiv.org/abs/2606.27306v1":
        "多语言推理级联需要更多上下文：在『译成英文-用英文推理-译回』的级联中，额外把原问题、英译问题与推理链一并提供给翻译环节，免训练地减少信息丢失。",
    "http://arxiv.org/abs/2606.27291v1":
        "为『可迁移查询生成』设计奖励信号：以工业语义岗位搜索为案例，用 RLAIF 生成抽象掉求职者身份、保留通用资历的可迁移查询，并应对策略优化钻 LLM-as-judge 规则空子的对抗性奖励面。",
    "http://arxiv.org/abs/2606.27288v1":
        "在 67 个前沿模型上证明：路由/投票/混合 agent 等多模型组合的准确率上限被『所有模型在同一查询上同时出错』的共错率 β 锁死，而常用的平均成对相关 ρ 无法识别 β。",
    "http://arxiv.org/abs/2606.27287v1":
        "研究自动化简历筛选中的提示注入：候选人插入不增加真实资历的自我推销文本可在简历同质、少数人注入时稳定提升排名，但随注入者增多效果迅速崩塌。",
    "http://arxiv.org/abs/2606.27275v1":
        "把历史语言对 LLM 的『难度』拆解为分词成本、预测不确定性、语义鲁棒性与上下文敏感度四个维度，研究历史意大利语并提出简单缓解方法。",
    "http://arxiv.org/abs/2606.27274v1":
        "BetXplain：带解释标注的社交媒体『诱导性博彩广告』检测数据集，用于识别可能误导用户、鼓励冒险行为的劝导性广告。",
    "http://arxiv.org/abs/2606.27268v1":
        "E-TTS：面向机器人操作的具身测试时扩展框架，研究推理对策略的扩展机制并引入历史信息，解决长程序列任务中仅靠当前观测扩展动作的不足。",
    "http://arxiv.org/abs/2606.27251v1":
        "推进全模态具身 agent 从孤立技能走向日常物理自治：统一编排网络（API/IoT）与物理（操作/导航）工具，并在长时运行中自主从物理失败中恢复。",
    "http://arxiv.org/abs/2606.27247v1":
        "RSPC：用精神科医生对 1799 条 Reddit 异地恋帖子的标注，把心理健康困扰与关系触发因素一起建模的基准，超越将心理状况孤立看待的传统做法。",
    "http://arxiv.org/abs/2606.27246v1":
        "在可解析的高维 GAN 模型中研究有效协方差动力学，把生成器学习低维子空间的训练过程扩展到类相关、有相关性、非零均值的潜在结构。",
    "http://arxiv.org/abs/2606.27242v1":
        "『更新的几何』：在共享词表的 LLM 家族中，提出基于 Fisher 对齐的免训练源语料选择方法，解决科学字符串域（SMILES/蛋白质/基因组）中表示相似度失效、经典更新几何度量又算不动的难题。",
    "http://arxiv.org/abs/2606.27237v1":
        "把语言模型当作任务专属知识库的可解释性分析：行为与机制层面均显示 LM 以『任务特定』方式编码知识，同一事实在不同任务上常无法共现，并非单一真相源。",
    "http://arxiv.org/abs/2606.27233v1":
        "提出分析协作问题求解对话的概念框架，用分层双层编码刻画人-AI 与多 agent 协作中的对话动态，弥补现有分析方法的局限。",
    "http://arxiv.org/abs/2606.27229v1":
        "CARVE：内容感知、价值高效的分块并行线性注意力，修正主流 delta-rule 架构（GDN-2）『记忆盲门控』等三大缺陷，让门控在擦除记忆时能参考已存储内容。",
    "http://arxiv.org/abs/2606.27226v1":
        "BINEVAL：把评估标准拆成原子化的二元问题再聚合成可解释的多维分数，替代不透明的整体式 LLM 打分，用于可解释的 LLM 评测与自我改进。",
    "http://arxiv.org/abs/2606.27210v1":
        "主张安全分类器应把用户意图作为提示与标签之间的显式信号；构建 1724 条难样本数据集 AIMS（含意图描述与危害标签），证明意图感知训练在多种训练范式下都能提升安全分类。",
    "http://arxiv.org/abs/2606.27199v1":
        "用 LLM 做预测：通过稀疏自编码器检视内部状态，区分模型依赖『时间特异知识』还是『可泛化模式』，并用特征引导（feature steering）在跨域时提升泛化。",
    "http://arxiv.org/abs/2606.27188v1":
        "提出『流程外壳（process harness）』：在不替换底层工作流引擎的前提下，给确定性引擎套上策略治理的 agentic 层并在控制点注入推理与监督，把遗留工作流升级为 agentic BPM。",
    "http://arxiv.org/abs/2606.27187v1":
        "HarmVideoBench：有害视频理解基准，针对现有基准只做二分类、缺乏解释的缺陷，刻画有害视频的多层次特征并要求模型给出解释性理由。",
    "http://arxiv.org/abs/2606.27180v1":
        "用视觉语言模型引导自动化基于势能的奖励塑形（PBRS）：在稀疏奖励场景下由 VLM 给出势函数，既缓解探索困难又避免朴素奖励塑形导致的奖励黑客。",

    # 2026-06-25 OpenAI / Simon Willison
    "https://openai.com/index/openai-broadcom-jalapeno-inference-chip":
        "OpenAI 与博通联合推出代号 Jalapeño 的定制 AI 芯片，专为 LLM 推理打造，旨在提升 AI 系统的性能、能效与规模。",
    "https://openai.com/index/helping-build-shared-standards-for-advanced-ai":
        "OpenAI 协助构建先进 AI 的共享标准，通过 Appia 基金会支持评估框架、安全实践与全球合作。",
    "https://openai.com/index/gpt-5-immunology-mystery":
        "GPT-5 Pro 帮助免疫学家 Derya Unutmaz 破解困扰三年的 T 细胞行为谜题，相关洞见有望助力癌症与自身免疫研究。",
    "https://simonwillison.net/2026/Jun/23/datasette/#atom-everything":
        "Simon 发布 datasette 1.0a35 大版本：新增基于 /-/create JSON API 的『建表』界面（支持列、主键、自定义类型、NOT NULL、默认值、外键等），以及 /-/alter 改表 API。",
    "https://simonwillison.net/2026/Jun/23/opfs-pyodide/#atom-everything":
        "Simon 让 Claude Code for web 给他搭了个 OPFS(Origin Private File System) + Pyodide 试验场，测试浏览器内的 Datasette Lite 能否直接编辑用户本地持久化的 SQLite 文件。",

    # 2026-06-25 arXiv
    "http://arxiv.org/abs/2606.24874v1":
        "FLUX3D：可扩展的图像→3D 高斯生成模型，用扩散对齐的稀疏体素表示突破语义特征抑制与跨模态对齐两大瓶颈，保留输入图像的高频细节。",
    "http://arxiv.org/abs/2606.24855v1":
        "OT-Agent：面向通用 agent 的全开源训练数据 curation 流水线，通过 100+ 受控消融实验系统揭示任务来源与多样性对训练泛化 agent 的重要性。",
    "http://arxiv.org/abs/2606.24851v1":
        "Hartley Neural Operator(HNO)：用纯实数的离散 Hartley 变换替代 FNO 的复数 FFT，消除共轭对称冗余，以更少参数保留两倍频率角点。",
    "http://arxiv.org/abs/2606.24849v1":
        "IV-CoT：用隐式视觉思维链把结构规划与外观渲染解耦，先形成潜在视觉布局再渲染，提升文生图对物体数量/空间关系/属性绑定的结构遵循。",
    "http://arxiv.org/abs/2606.24842v1":
        "World Models in Pieces：提出『结构化认证』框架，先证明通用 agent 并非万能，再将目标受限性能映射为对 agent 内部世界模型逐项(transition-local)的保证。",
    "http://arxiv.org/abs/2606.24841v1":
        "Match-Task-to-Objective(MTO) 框架：研究多种预训练目标对 encoder-decoder 模型在生成/问答任务上的影响，并自动为给定任务匹配合适的训练目标与数据。",
    "http://arxiv.org/abs/2606.24839v1":
        "Grading the Grader：针对 agentic 数据分析系统的打分难题，在 153 个数值任务上构建『严格正则匹配→LLM 宽松打分→人工片段检查』三层人机级联打分。",
    "http://arxiv.org/abs/2606.24834v1":
        "研究多轮 LLM 对话在评估非功能性需求(NFR)时的准确度与满意度，超越单轮正确率去衡量对模糊、上下文相关需求的协作推理质量。",
    "http://arxiv.org/abs/2606.24828v1":
        "Less is More：构建并发布含 188 万篇 PMC 文章的生物医学长文摘要数据集，分析作者撰写摘要与原文的对齐质量差异，提出质量感知的训练数据选择。",
    "http://arxiv.org/abs/2606.24825v1":
        "L3Cube-MahaPOS：发布马拉地语词性标注金标准数据集(32,354 句)及 BERT 模型，填补这一使用人口超 8300 万却严重缺标注资源语言的空白。",
    "http://arxiv.org/abs/2606.24820v1":
        "SHERLOC：免训练的代码修复缺陷定位框架，用推理 LLM 配紧凑仓库工具与自恢复机制，在 SWE-Bench Lite 上达到 84.33% accuracy@1。",
    "http://arxiv.org/abs/2606.24808v1":
        "结构化概念演化(SCE)：让 LLM 配代数变异语法去演化已有结构，而非从零设计，自动发现 lifted-product 类量子 LDPC 纠错码族。",
    "http://arxiv.org/abs/2606.24797v1":
        "EG-VQA：可验证视频问答基准，每个 QA 对都标注支撑性时间证据，要求模型联合推理并精确定位证据（含 2067 段视频）。",
    "http://arxiv.org/abs/2606.24790v1":
        "Grad Detect：基于梯度的 LLM 幻觉检测，单次前向-反向传播即可从逐层梯度模式预测输出正确性，捕捉输出层信号之外的内部信息。",
    "http://arxiv.org/abs/2606.24783v1":
        "Paying to Know：设想 agent 化电商的『付费获取已验证信息』微交易市场，买家 agent 用极小金额逐步解锁卖家/第三方的可信产品数据（基于 x402、AP2 等微支付）。",
    "http://arxiv.org/abs/2606.24779v1":
        "DeepBD：用于遗传性出生缺陷变异优先级排序与诊断的 grounded agentic 工作流，整合群体遗传、变异效应预测、表型本体、蛋白结构与文献等多源证据。",
    "http://arxiv.org/abs/2606.24775v1":
        "追问『我们准备好 agent 原生记忆系统了吗』：超越端到端 F1/BLEU，转而从运维成本、模块架构权衡、动态知识更新鲁棒性等系统层面评估 agent 记忆。",
    "http://arxiv.org/abs/2606.24759v1":
        "UniDrive：自动驾驶可解释风险理解的统一视觉-语言与 grounding 框架，结合时序推理分支与空间精度，缓解时序推理与空间定位之间的取舍。",
    "http://arxiv.org/abs/2606.24758v1":
        "CANDLE：轻量级阿拉伯语字符级去噪/去重系统，首次把 CTC 用于字符去重，将规范化建模为字符编码器上的序列对齐，无需词典、规则或形态分析器。",
    "http://arxiv.org/abs/2606.24752v1":
        "在 5M–314M 参数的 GPT 式 Transformer 上研究多语言持续学习中的『可塑性丧失』，探讨单纯扩大规模能否缓解模型学新知识能力下降的问题。",
    "http://arxiv.org/abs/2606.24747v1":
        "推导面向领域的 LLM 压缩经验性 scaling law，量化域内/通用性能随数据量、压缩比、监督形式与迭代剪枝的变化（以量化金融为应用域）。",
    "http://arxiv.org/abs/2606.24745v1":
        "提出无 skip 连接的 encoder-decoder 骨干做 flow-matching 语音增强，用潜表示对齐(LRA)替代 U-Net skip，避免把噪声相关的低层特征传给解码器。",
    "http://arxiv.org/abs/2606.24716v1":
        "提出以人工标注概念量化稀疏自编码器(SAE)潜变量可解释性的评估框架，构建 synCUB/synCOCO 单属性差异合成基准与 FBMP 匹配方法。",
    "http://arxiv.org/abs/2606.24714v1":
        "CN-NewsTTS Bench v0.1：面向中文新闻 TTS 发音的目标级自动基准，评测系统在不靠规则/SSML/人工改写时能否正确读出比分、型号、百分比等密集书面形式。",
    "http://arxiv.org/abs/2606.24712v1":
        "TACTFUL：无视觉的纯触觉探索框架，让多指机器人在受限空间自主接触发现物体并通过触觉重建识别，完全在真实硬件上训练单一策略。",
    "http://arxiv.org/abs/2606.24679v1":
        "FlowPipe：用 LLM 增强的条件生成流网络(GFlowNet)自动构建数据准备流水线，缓解长时程信用分配弱、上下文注入弱、稀疏搜索探索低效三大问题。",
    "http://arxiv.org/abs/2606.24669v1":
        "LaGO：把预训练 LLM 当作潜在动作先验来『软引导』在线强化学习策略优化，而非直接当控制器，在 CLEVR-Robot 与 Meta-World 上提升奖励与成功率。",
    "http://arxiv.org/abs/2606.24667v1":
        "DREAM：用 LLM 的自回归 next-token 预测目标为稠密检索提供监督，免去昂贵的正负样本对——若文档与查询相关，则条件其后目标输出应更易预测。",
    "http://arxiv.org/abs/2606.24655v1":
        "AI-PAVE-Br：面向巴西电商的 LLM 产品属性值抽取系统，用『黄金集』方法应对葡萄牙语商品描述的语言细微差异与多样性，并发布可复现基准。",
    "http://arxiv.org/abs/2606.24636v1":
        "CineCap：用时空锚点做结构化推理的电影摄影术视频字幕生成，统一开放式描述运镜、景别、景深、构图、拍摄角度等专业电影语言概念。",

    # 2026-06-23 OpenAI / Simon Willison
    "https://openai.com/index/omio":
        "旅游平台 Omio 借助 OpenAI 打造对话式出行体验、加速产品开发，向 AI 原生公司转型。",
    "https://openai.com/index/daybreak-securing-the-world":
        "OpenAI 推出 Daybreak 系列安全工具（含 Codex Security 与 GPT-5.5-Cyber），帮助组织规模化地发现、验证并修复漏洞。",
    "https://openai.com/index/patch-the-planet":
        "Patch the Planet：Daybreak 旗下倡议，用 AI 加专家评审帮助开源维护者发现、验证并修复漏洞。",
    "https://openai.com/index/codex-maxxing-long-running-work":
        "案例：Jason Liu 如何用 Codex 保留上下文、管理复杂项目，让工作在单次提示之外持续推进。",
    "https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything":
        "Simon 介绍 Charles Ye 等人的研究：模型难以区分自身特权文本（<system>/<assistant> 等角色标签）与不可信用户输入，提示注入本质是「角色混淆」；并称赞论文配博客式可读版的做法。",
    "https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything":
        "Simon 用 Claude Code 把 0.2B 的 Moebius 图像修复模型移植到浏览器（WebGPU）运行，并放出可在线试用的 demo。",

    # 2026-06-23 arXiv
    "http://arxiv.org/abs/2606.23444v1":
        "SkyJEPA：用 JEPA 在隐空间建模四旋翼长时程动力学世界模型，实现零样本 sim-to-real 的高频控制，缓解自回归 rollout 的误差累积。",
    "http://arxiv.org/abs/2606.23687v1":
        "Randomized YaRN：训练时给短文本采样更大位置范围的 YaRN 编码并配长度课程，提升超长上下文推理的长度泛化能力。",
    "http://arxiv.org/abs/2606.23679v1":
        "Semantic Browsing：让文生图在保真之外实现可控多样性，用户可沿可解释的语义轴系统化浏览结构化图像画廊。",
    "http://arxiv.org/abs/2606.23678v1":
        "AIR：通过对代码增强的数值计算任务做强化学习，让多模态大模型具备自适应的「文字+代码」交错推理能力。",
    "http://arxiv.org/abs/2606.23676v1":
        "开放问题：在重尾梯度噪声下 AdamW 是否仍能收敛？指出 AdamW 缺乏重尾收敛理论，二阶矩累加器可能构成真正障碍。",
    "http://arxiv.org/abs/2606.23672v1":
        "针对位操作谜题，教 LLM 用字符串匹配、回溯与纠错来推断进制和真值表，规避算术模拟带来的幻觉与组合爆炸（NVIDIA Nemotron 推理挑战赛方案）。",
    "http://arxiv.org/abs/2606.23671v1":
        "考察 LLM 能否可靠自报「对抗性 prefill 攻击」：10 个开源模型均无法可靠识别自己被诱导的输出，平均仅 27.3% 声称有意图，内省信号主要来自拒答相关推理。",
    "http://arxiv.org/abs/2606.23668v1":
        "论 prompt 条件化语言模型作为通用学习器的局限：把人机交互建模为 cheap-talk 双层博弈，用 PAC-Bayes 界区分有限样本误差与不可约的结构性表达力限制。",
    "http://arxiv.org/abs/2606.23664v1":
        "MAS-PromptBench：系统研究 prompt 优化在多智能体 LLM 系统中何时、提升多少有效，应对其指数级增长的搜索空间。",
    "http://arxiv.org/abs/2606.23654v1":
        "EnterpriseClawBench：基于真实职场 agent 会话构建的企业级 agent 基准，含 852 个可复现任务；因数据涉密只开放构建与评测协议。",
    "http://arxiv.org/abs/2606.23643v1":
        "TailorMind：在无现成内容池时，将用户行为轨迹转化为生成偏好，用超图协同过滤+排序反馈做偏好对齐的多模态内容生成。",
    "http://arxiv.org/abs/2606.23637v1":
        "证明 Muown 的方向更新等价于归一化方向上的黎曼步，幅度仅调节角步长；据此提出显式优化角步长的 AngularMuown。",
    "http://arxiv.org/abs/2606.23633v1":
        "反思「AI 暴露分数」（GPTs are GPTs）：指出静态暴露分数测量的内容与政策所需之间的结构性鸿沟，及其在传播中丢失原作者警示的问题。",
    "http://arxiv.org/abs/2606.23608v1":
        "主张 agent 在因果发现中应只做检查数据、检索上下文、解释方法假设与澄清图输出，而不应直接提供边、方向、先验或因果结论。",
    "http://arxiv.org/abs/2606.23607v1":
        "提出可扩展框架，把线性模式连通性（LMC）与模型融合推广到十亿参数级预训练 Transformer，用双向学习的保功能权重变换对齐等价解。",
    "http://arxiv.org/abs/2606.23603v1":
        "MORL-A2C：为健康饮食推荐系统 MOPI-HFRS 引入序列决策的多目标强化学习重排器，权衡健康与用户偏好。",
    "http://arxiv.org/abs/2606.23595v1":
        "SPIRAL：训练语言模型在统一推理流水线中同时使用串行推理、并行采样与多轨迹聚合三种 test-time 计算原语。",
    "http://arxiv.org/abs/2606.23591v1":
        "量化「数据影响」与「数据相似度」两类输出溯源度量的一致性：两者排序显著一致但存在不对称，揭示廉价的相似度何时可替代昂贵的影响度量。",
    "http://arxiv.org/abs/2606.23590v1":
        "用持久同调（persistent homology）刻画 LLM 内部状态的拓扑，统一检测多类「病态问题」（含糊/欠定/矛盾）并据此引导回答行为。",
    "http://arxiv.org/abs/2606.23587v1":
        "用合适的激活函数（多项式 Kolmogorov-Arnold 网络）让神经网络更易学会康威生命游戏动力学，把搜索问题重新当作学习问题。",
    "http://arxiv.org/abs/2606.23585v1":
        "用多智能体强化学习实现先进空中交通（AAM）走廊网络中的去中心化交通流管理，应对自主飞行器规模化后的协调难题。",
    "http://arxiv.org/abs/2606.23581v1":
        "Kamera：统一的位置无关多模态 KV 缓存，让视频帧/截图在上下文滑动时免重编码复用，并补回 naive 复用丢失的跨块条件信息。",
    "http://arxiv.org/abs/2606.23568v1":
        "SVD-Surgeon：将最优脑外科（OBS）框架引入奇异值基的免训练 LLM 压缩，对保留奇异值做闭式二阶补偿以抵消截断损失。",
    "http://arxiv.org/abs/2606.23567v1":
        "Scheduling Thoughts：为掩码扩散语言模型推导解码失配的可解上界，将「思考顺序」选择转化为带冻结去噪器的策略优化（Self-Aware Scheduling）。",
    "http://arxiv.org/abs/2606.23566v1":
        "LangMAP：将 UnigramLM 扩展到多语言场景，从单一共享词表产出语言自适应的分词，无需改词表即可适配预训练模型。",
    "http://arxiv.org/abs/2606.23543v1":
        "VeriEvol：把强化学习扩展视为可验证的数据构造问题，解耦提示难度与答案可靠性，用离线假设检验证伪保证标签可靠的多模态数学推理。",
    "http://arxiv.org/abs/2606.23537v1":
        "SQLConductor：用 search-to-policy 学习实现逐步式 Text-to-SQL 编排，可根据中间证据动态调整步骤顺序，突破固定流水线的局限。",
    "http://arxiv.org/abs/2606.23533v1":
        "POTracker：优化 LLM 生成符合能源监管标准、机器可读（JSON/XML）的全美统一停电报告，兼顾语义正确与格式合规。",
    "http://arxiv.org/abs/2606.23525v1":
        "SelfCompact：让 agent 自己决定何时、如何压缩上下文（提供压缩工具+触发规则），避免固定阈值压缩在推理中途丢弃部分结果。",
    "http://arxiv.org/abs/2606.23521v1":
        "Concordia：用 JIT 编译的常驻内核检查点实现容错 LLM 推理，在设备同步点运行检查点钩子、观测真实执行的二进制内核来恢复 GPU 常驻状态。",
    "http://arxiv.org/abs/2606.23500v1":
        "FLKit：面向健康与生命科学的联邦学习结构化上手工具包，为临床、法律、治理、技术等不同角色提供贯穿联邦学习全生命周期的入门路径。",

    # 2026-06-22 OpenAI / Simon Willison
    "https://openai.com/index/samsung-electronics-chatgpt-codex-deployment":
        "三星电子向全球员工部署 ChatGPT Enterprise 和 Codex，成为 OpenAI 规模最大的企业 AI 落地之一。",
    "https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/#atom-everything":
        "sqlite-utils 4.0rc1 发布：首个 v4 候选版本，新增数据库迁移（migrations）和嵌套事务支持，含少量向后不兼容改动，作者征集试用反馈。",
    "https://simonwillison.net/2026/Jun/21/sqlite-utils/#atom-everything":
        "sqlite-utils 4.0rc1 版本发布说明（指向迁移与嵌套事务的详细介绍）。",
    "https://simonwillison.net/2026/Jun/21/temporary-cloudflare-accounts/#atom-everything":
        "Cloudflare 推出临时账号：用 `npx wrangler deploy --temporary` 无需注册即可部署 Workers 项目，存活 60 分钟，名义上为 AI agent 设计但对所有人都好用。",

    # 2026-06-20 OpenAI / Google DeepMind / Simon Willison
    "https://openai.com/index/chatgpt-enterprise-spend-controls":
        "OpenAI 为 ChatGPT Enterprise 增加使用分析和支出控制，帮助组织管理成本并规模化部署 AI。",
    "https://openai.com/index/improving-health-intelligence-in-chatgpt":
        "GPT-5.5 Instant 改进 ChatGPT 健康与保健回答，强化推理、上下文理解、表达清晰度和医生参与评测。",
    "https://openai.com/index/diagnose-rare-childhood-diseases":
        "研究人员用 OpenAI 推理模型辅助诊断儿童罕见遗传病，在此前未解病例中识别出 18 个新诊断。",
    "https://openai.com/index/ai-chemist-improves-reaction":
        "OpenAI 与 Molecule.one 展示近自主 AI 化学家如何用 GPT-5.4 改进一种困难的药物合成反应。",
    "https://openai.com/index/introducing-life-sci-bench":
        "LifeSciBench 是由专家编写和复核的基准，用于评估 AI 处理真实生命科学研究任务与决策的能力。",
    "https://deepmind.google/blog/securing-the-future-of-ai-agents/":
        "Google DeepMind 提出 AI Control Roadmap，将传统安全措施与实时监控结合，用于保护内部 agent 系统。",
    "https://simonwillison.net/2026/Jun/19/sean-lynch/#atom-everything":
        "引用 Sean Lynch：MCP 相比 skills/CLI 的核心价值可能是把认证流程隔离出 agent 上下文，理想形态甚至只是 API 认证网关。",
    "https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything":
        "Simon 介绍 Datasette Apps：在严格 iframe 沙箱中运行自包含 HTML/JavaScript 应用，并受控查询或写入 Datasette 数据。",
    "https://simonwillison.net/2026/Jun/18/datasette-acl/#atom-everything":
        "datasette-acl 0.6a0 从表级权限扩展为通用资源共享系统，为多用户 Datasette 提供细粒度访问控制。",
    "https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything":
        "Simon 评测 MIT 许可的 GLM-5.2，认为它可能是当前最强的纯文本开放权重 LLM，并重点介绍其百万 token 上下文。",
    "https://simonwillison.net/2026/Jun/17/charity-majors/#atom-everything":
        "引用 Charity Majors：AI 让代码生产近乎免费并可随时重生成，因此工程团队反而需要更多纪律。",
    "https://simonwillison.net/2026/Jun/15/datasette-apps-2/#atom-everything":
        "datasette-apps 0.1a3 修复无 create-app 权限仍可建应用等权限漏洞，并统一私有应用的编辑删除规则。",
    "https://simonwillison.net/2026/Jun/15/datasette-apps/#atom-everything":
        "datasette-apps 0.1a2 加强自定义 CSP 来源权限控制，改进 stored query 选择器、片段链接和全屏模式。",

    # 2026-06-20 arXiv
    "http://arxiv.org/abs/2606.20560v1":
        "论文把 DiffusionGemma 的推理透明度拆为变量透明度和算法透明度，研究连续潜空间计算是否更难解释。",
    "http://arxiv.org/abs/2606.20544v1":
        "论文研究分布转移下 MoE 的校准，分析专家级概率校准与路由机制如何共同影响整体不确定性可靠性。",
    "http://arxiv.org/abs/2606.20537v1":
        "Execution-State Capsules 为端侧 physical AI 保存和恢复完整执行状态，而不只复用 KV cache，以降低小批量交互延迟。",
    "http://arxiv.org/abs/2606.20529v1":
        "LedgerAgent 显式维护事实、约束和条件组成的结构化任务状态，减少工具调用 agent 因陈旧或缺失信息违反策略。",
    "http://arxiv.org/abs/2606.20527v1":
        "StylisticBias 固定人物身份、逐项改变视觉属性，发现少数外观线索驱动了多模态模型的大部分社会偏见。",
    "http://arxiv.org/abs/2606.20526v1":
        "DeepSWIP 为 DeepProbLog 引入单世界反事实语义，并通过转换后的加权模型计数精确计算干预结果。",
    "http://arxiv.org/abs/2606.20523v1":
        "SARLO-80 提供全球 80 厘米级高分辨率 SAR、光学图像与自然语言对齐数据，支持物理扎根的多模态学习。",
    "http://arxiv.org/abs/2606.20520v1":
        "Sovereign Execution Broker 在 agent 控制平面建立运行时强制边界，只允许符合证书绑定执行合同的真实变更。",
    "http://arxiv.org/abs/2606.20517v1":
        "Multi-LCB 把 LiveCodeBench 从 Python 扩展到 12 种编程语言，用于评估 LLM 的跨语言代码生成能力。",
    "http://arxiv.org/abs/2606.20512v1":
        "Probe-and-Refine 用合成 bug-fix 探针迭代诊断和改进 AGENTS.md，让仓库指导基于实测失败而非一次性生成。",
    "http://arxiv.org/abs/2606.20510v1":
        "论文把概率谓词和状态转移纳入 agent 运行时策略验证，在存在检测器误差和依赖关系时保持高效且可靠。",
    "http://arxiv.org/abs/2606.20508v1":
        "研究混合良性与有害合规示例如何影响安全对齐 LLM，发现不同模型反应不一且偏好优化阶段至关重要。",
    "http://arxiv.org/abs/2606.20506v1":
        "FreeStyle 从社区 LoRA 挖掘大规模风格与内容锚点，实现内容结构和独立风格参考的可控双参考图像生成。",
    "http://arxiv.org/abs/2606.20502v1":
        "CWE-Trace 用严格时间切分和 Linux 内核漏洞对诊断 LLM，显示微调可改善校准但未必形成真正漏洞理解。",
    "http://arxiv.org/abs/2606.20493v1":
        "Contagion Networks 量化多 agent 系统中 evaluator 偏见的传播，发现即使同一底层模型也会相互感染评估风格。",
    "http://arxiv.org/abs/2606.20487v1":
        "H-RePlan 为跨设备 computer-use agent 区分设备内修复与跨设备重规划，提供分层故障恢复。",
    "http://arxiv.org/abs/2606.20485v1":
        "论文以 agent 权力和响应函数建模多体系统，推导秩序、熵、脆弱性等宏观性质及增长与韧性的最优平衡。",
    "http://arxiv.org/abs/2606.20482v1":
        "IFLLM 收集用户鼠标轨迹和眼动等隐式反馈，探索在显式评分稀缺时用于 LLM 偏好对齐。",
    "http://arxiv.org/abs/2606.20477v1":
        "RefRad2D 从临床 CT/MR 数据自动构建 120 万双语图文对，训练可同时生成报告、回答问题和空间定位的 RadGrounder。",
    "http://arxiv.org/abs/2606.20475v1":
        "MAA 在多个 batch 间按记忆操作累积边际优势证据，区分稳定有效策略与偶然命中，推动 agent 自我演化。",
    "http://arxiv.org/abs/2606.20474v1":
        "UltraQuant 面向长上下文多轮 agent 提供 4-bit KV cache，在任务质量、缓存驻留和服务吞吐之间联合优化。",
    "http://arxiv.org/abs/2606.20470v1":
        "论文分析用防御性误导对抗模型引导的自动攻击，指出可预测拒绝会被高查询预算利用，并探索欺骗攻击 judge。",
    "http://arxiv.org/abs/2606.20467v1":
        "ASYS 让 agent 把 PDE 理论和约束转为可微符号程序，再结合进化搜索与梯度优化发现可解释数学结构。",
    "http://arxiv.org/abs/2606.20436v1":
        "论文同时使用 Ghidra 和 RetDec 的伪 C 视图做 LLM 恶意软件分类，检验多反编译器视角能否降低单一工具偏差。",
    "http://arxiv.org/abs/2606.20408v1":
        "NRT-Bench 在模拟核电控制室中对多角色 LLM agent 做多轮红队测试，用客观安全状态衡量持续攻击下的鲁棒性。",
    "http://arxiv.org/abs/2606.20400v1":
        "论文仅用意图定义生成无标注合成对话，并通过主题、风格属性和后处理风格化提高数据多样性与实用性。",
    "http://arxiv.org/abs/2606.20388v1":
        "DataMagic 把原始表格自动转为含动态图表、旁白和同步动画的数据洞察视频，同时保持数值可信和来源可追踪。",
    "http://arxiv.org/abs/2606.20382v1":
        "论文把联邦图学习中的客户端级和节点级模态缺失建模为图感知潜语义合成问题。",
    "http://arxiv.org/abs/2606.20381v1":
        "研究指出 E2M1 FP4 的几何不对称会累积收缩偏差，并提出 UFP4 训练配方改善 LLM 低精度预训练稳定性。",
    "http://arxiv.org/abs/2606.20376v1":
        "CRAX 基于 JAX/MJX 构建高保真安全强化学习基准，相比 CPU 基准最高加速约 100 倍。",

    # 2026-06-17 OpenAI / Google DeepMind / Simon Willison
    "https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/":
        "英国政府与 Google DeepMind 合作构建 AI 原型，目标是加速住房规划审批和建房决策。",
    "https://openai.com/index/deployment-simulation":
        "OpenAI 介绍 Deployment Simulation，用真实对话数据在发布前模拟部署行为，以提前预测模型表现并改进安全评估。",
    "https://simonwillison.net/2026/Jun/17/click-to-play-component/#atom-everything":
        "Simon 发布 click-to-play Web Component，把 GIF 先显示为静态帧，用户点击后才按需加载播放。",
    "https://simonwillison.net/2026/Jun/17/netnewswire-status/#atom-everything":
        "Simon 称赞 Brent Simmons 退休后专注把开源 RSS 阅读器 NetNewsWire 做好，并分享自己多年使用体验。",
    "https://simonwillison.net/2026/Jun/16/datasette/#atom-everything":
        "datasette 1.0a34 新增在界面中插入、编辑和删除行的能力，灵感来自 Datasette Agent 的 SQL 写入支持。",
    "https://simonwillison.net/2026/Jun/16/datasette-tailscale/#atom-everything":
        "datasette-tailscale 0.1a0 是实验插件，可用 Tailscale sidecar 把本地 Datasette 服务接入 Tailnet。",
    "https://simonwillison.net/2026/Jun/16/georgi-gerganov/#atom-everything":
        "引用 Georgi Gerganov：Qwen3.6-27B 已是很能干的本地编码模型，适合维护者处理日常小任务。",

    # 2026-06-17 arXiv
    "http://arxiv.org/abs/2606.18237v1":
        "ReproRepo 利用 GitHub 仓库 issue 扩展可复现性审计，把复现实验中的问题、证据和修复过程系统化记录。",
    "http://arxiv.org/abs/2606.18235v1":
        "EvolveNav 通过从历史轨迹抽取规则记忆、UCB 检索和行动前 preflection，让零样本目标导航 agent 在测试时自我改进。",
    "http://arxiv.org/abs/2606.18223v1":
        "论文用模仿学习从部分可观测网络状态中学习红队策略，帮助神经符号网络防御 agent 预测攻击者动作。",
    "http://arxiv.org/abs/2606.18222v1":
        "Darshana Graph 汇集印度哲学多传统平行注释语料，并用风格计量和图分析支持跨学派比较研究。",
    "http://arxiv.org/abs/2606.18216v1":
        "Zone of Proximal Policy Optimization 将教师知识放入提示而非梯度，让策略在接近自身能力边界的任务上获得引导。",
    "http://arxiv.org/abs/2606.18206v1":
        "FPRM 用预归一化、残差缩放和固定点收敛作为循环 Transformer 的停止机制，使模型按任务难度自适应计算量。",
    "http://arxiv.org/abs/2606.18205v1":
        "论文把 Al-Mawrid 阿英词典按 ISO Language Markup Framework 和 TEI Lex-0 编码，提升词典数据的标准化和复用性。",
    "http://arxiv.org/abs/2606.18203v1":
        "RubricsTree 为个人健康 agent 构建可扩展、可演化开放式评测，覆盖健康记忆和医学技能两类能力。",
    "http://arxiv.org/abs/2606.18195v1":
        "论文提出 dLLM 的 on-policy self-distillation，让扩散语言模型从自身未来状态中学习以改善采样与生成质量。",
    "http://arxiv.org/abs/2606.18193v1":
        "红队研究用 HackAgent 对 Anthropic Fable 5 和 Opus 4.8 做自动越狱评估，发现两者仍会在持续自适应攻击下产生有害输出。",
    "http://arxiv.org/abs/2606.18192v1":
        "Stanford EDGAR Filings Dataset 将 SEC 披露重构为版式忠实、token 高效的 MultiMarkdown 长上下文预训练数据。",
    "http://arxiv.org/abs/2606.18191v1":
        "DRFLOW 评测深度研究 agent 能否从分散企业资料中预测个性化工作流步骤，而不仅是生成报告摘要。",
    "http://arxiv.org/abs/2606.18190v1":
        "论文发布带 ATT&CK 标签的多源网络安全日志数据集，并评估小语言模型在安全事件分类上的表现。",
    "http://arxiv.org/abs/2606.18181v1":
        "IUU+DB 用 LLM 从异构文档中抽取非法捕捞、海鲜欺诈和劳工滥用事件，构建可去重和趋势分析的全球数据库。",
    "http://arxiv.org/abs/2606.18168v1":
        "研究 8.6 万个 agent 生成测试补丁，发现 80% 以上缺少强 oracle 信号，说明测试文件存在不等于真正验证行为。",
    "http://arxiv.org/abs/2606.18166v1":
        "论文评估开源 LLM 在 CTI 报告中进行多标签 MITRE ATT&CK 技术分类的能力和局限。",
    "http://arxiv.org/abs/2606.18158v1":
        "论文指出欧盟 AI 法下的法律自动化缺少衡量教义式法律推理的基准，使高风险司法 AI 的准确性要求难以落地。",
    "http://arxiv.org/abs/2606.18154v1":
        "LEADS 把心脏电生理知识形式化为结构化动作空间，让 LLM agent 发现稳定、可解释的混合数字孪生模型结构。",
    "http://arxiv.org/abs/2606.18147v1":
        "WEQA 用查询自适应 agent 把 LLM 与可穿戴健康数据分析工具结合，提升连续传感器数据问答的准确性和临床可信度。",
    "http://arxiv.org/abs/2606.18144v1":
        "论文把 embodied agent 的闪存写入寿命视为会折旧的资产，提出耐久性影子价格来决定记忆存储层级。",
    "http://arxiv.org/abs/2606.18142v1":
        "TAC 基准测试 AI 旅行 agent 在工具行动中是否会避开涉及动物福利风险的选项，并发现前沿模型基础表现低于随机水平。",
    "http://arxiv.org/abs/2606.18132v1":
        "论文提出元强化学习知识复用框架，把在简化动力学 agent 上学到的任务知识迁移到异构具身 agent。",
    "http://arxiv.org/abs/2606.18129v1":
        "Cognitive Atrophy Bench 衡量心理健康支持场景中 LLM 是否削弱用户持续反思、自主应对和决策能力。",
    "http://arxiv.org/abs/2606.18124v1":
        "研究发现隐藏地理元数据会让 LLM 在中性提示中泄露地域化输出，甚至 Unknown 占位也会改变生成分布。",
    "http://arxiv.org/abs/2606.18120v1":
        "论文分析 Handlebars 模板中的双花括号和三花括号插值如何影响 prompt 结构化角色注入风险，指出 HTML 转义并不能覆盖所有分隔符家族。",
    "http://arxiv.org/abs/2606.18108v1":
        "ALeRCE text-to-SQL 系统用分步 schema linking、查询分类、提示分解和自纠错，让天文数据库可用自然语言查询。",
    "http://arxiv.org/abs/2606.18105v1":
        "OmniPlan 用 LLM 解释用户偏好，并在 MIP、启发式和 DRL 专家之间动态选择，以兼顾网络规划优化的速度和近似最优性。",
    "http://arxiv.org/abs/2606.18103v1":
        "HistoRAG 把史学方法嵌入 RAG：分离检索与生成、做时间窗口平衡，并用可争辩的 LLM judge 评估来源相关性。",
    "http://arxiv.org/abs/2606.18098v1":
        "IsabeLLM 为 Isabelle 定理证明加入 RAG、错误追踪和反例生成，并用于验证比特币 PoW 共识。",
    "http://arxiv.org/abs/2606.18092v1":
        "EAGG 用端执行器拓扑图和几何感知 token 对齐不同具身形态，在多夹爪抓取生成中提升泛化和迁移能力。",

    # 2026-06-16 OpenAI / Google DeepMind
    "https://openai.com/index/introducing-openai-partner-network":
        "OpenAI 推出 Partner Network，并投入 1.5 亿美元帮助全球合作伙伴加速企业 AI 采用、部署和转型。",
    "https://openai.com/index/academy-courses-applying-ai-at-work":
        "OpenAI Academy 新增三门课程，帮助职场人建立实用 AI 技能、可复用工作流并把 agent 用到日常工作中。",
    "https://openai.com/index/preply":
        "Preply 用 OpenAI 生成课后摘要、个性化反馈和语言练习，把 AI 与真人导师结合做个性化学习。",
    "https://openai.com/index/supporting-eu-trustworthy-ai-ecosystem":
        "OpenAI 支持欧盟 AI 内容透明度实践准则，推动来源标识与工具建设，帮助人们理解 AI 生成内容。",
    "https://openai.com/index/bbva":
        "BBVA 将 ChatGPT Enterprise 扩展到 10 万名员工，并与 OpenAI 合作推进银行业务的 AI 转型。",
    "https://openai.com/index/using-codex-to-simulate-black-holes":
        "天体物理学家 Chi-kwan Chan 使用 Codex 构建黑洞模拟，辅助研究极端物理并检验广义相对论。",
    "https://openai.com/index/openai-to-acquire-ona":
        "OpenAI 计划收购 Ona，以增强 Codex 的安全持久云环境能力，支持企业长时间运行的 AI agent 工作流。",
    "https://openai.com/index/openai-on-oracle-cloud":
        "OpenAI 介绍企业可通过 Oracle Cloud 既有承诺访问 OpenAI 模型与 Codex，并获得企业级安全和治理能力。",
    "https://deepmind.google/blog/diffusiongemma-4x-faster-text-generation/":
        "Google DeepMind 发布 DiffusionGemma，强调用扩散式生成实现约 4 倍更快的文本生成。",
    "https://openai.com/index/prc-linked-influence-operations-ai-debates":
        "OpenAI 报告称与中国相关的影响力行动正使用 AI 介入美国科技辩论、数据中心叙事、关税和 ChatGPT 虚假说法。",
    "https://deepmind.google/blog/investing-in-multi-agent-ai-safety-research/":
        "Google DeepMind 与 Schmidt Sciences 等伙伴发起最高 1000 万美元资助，支持全球研究者开展多智能体 AI 安全研究。",
    "https://openai.com/index/lseg":
        "LSEG 用 OpenAI 在全球业务中规模化可信 AI，加速洞察生成、缩短发布周期并赋能 4000 名员工。",
    "https://deepmind.google/blog/fluid-natural-voice-translation-with-gemini-35-live-translate/":
        "Gemini 3.5 Live Translate 把近实时自然语音翻译带到 Google AI Studio、Google Translate 和 Google Meet。",
    "https://deepmind.google/blog/introducing-gemma-4-12b-a-unified-encoder-free-multimodal-model/":
        "Google DeepMind 发布 Gemma 4 12B，主打统一、无编码器的多模态模型设计。",
    "https://deepmind.google/blog/powering-the-future-of-robotics-in-europe/":
        "Google DeepMind 介绍其在欧洲推动机器人未来发展的投入与生态合作。",
    "https://openai.com/index/nextdoor":
        "Nextdoor 工程师使用 Codex 与 GPT-5.5 排查难复现问题、跨平台构建功能，把精力更多放在产品结果上。",
    "https://openai.com/index/notion":
        "Notion 用 Codex 一次性实现规格、构建 Web 版 AI 语音输入，并放大小团队的工程产能。",
    "https://openai.com/index/industrial-policy-for-the-intelligence-age":
        "OpenAI 提出面向智能时代的产业政策构想，围绕扩大机会、共享繁荣和建设韧性制度展开。",
    "https://deepmind.google/blog/measuring-the-impact-of-learning-with-ai-in-sierra-leone-and-beyond/":
        "Google DeepMind 介绍在塞拉利昂及更多地区衡量 AI 学习工具影响的研究与部署经验。",

    # 2026-06-16 Simon Willison
    "https://simonwillison.net/2026/Jun/16/fable-5-export-controls/#atom-everything":
        "Simon 认为 Fable 5 出口管制伤害美国网络防御，因为让模型修复漏洞和写测试正是防守方最需要的能力。",
    "https://simonwillison.net/2026/Jun/16/matteo-wong-the-atlantic/#atom-everything":
        "引用 Matteo Wong 报道：安全专家称所谓 Fable 越狱其实是让模型帮助查找和修复漏洞，属于正常防御用途。",
    "https://simonwillison.net/2026/Jun/16/captcha-on-at-least-one-ampersand/#atom-everything":
        "Simon 用 Claude Code 调整 Cloudflare WAF 规则，让搜索 URL 只有在查询参数含至少一个 & 时才触发 CAPTCHA。",
    "https://simonwillison.net/2026/Jun/15/datasette-agent/#atom-everything":
        "datasette-agent 0.3a0 新增需用户批准的 execute_write_sql 写库工具，并增强聊天终端的审批与 unsafe 自动批准模式。",
    "https://simonwillison.net/2026/Jun/15/axios-clashes-anthropics/#atom-everything":
        "Simon 摘要 Axios 对美国政府与 Anthropic 围绕 Fable/Mythos 出口管制冲突的幕后报道，关注双方态度与政策走向。",
    "https://simonwillison.net/2026/Jun/15/julia-evans/#atom-everything":
        "引用 Julia Evans 的写作建议：想象一个具体读者，常常是三年前的自己或一位好友，然后为这个人写。",
    "https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/#atom-everything":
        "转述 Narayanan 与 Kapoor 的论点：AI 尚未导致软件工程大规模失业，因为写代码并不是软件工程的唯一瓶颈。",
    "https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/#atom-everything":
        "Pyodide/PyPI 已支持发布 WASM wheels，包作者可像发布原生 wheel 一样分发兼容 Pyodide 的包，Simon 用 luau-wasm 试水。",
    "https://simonwillison.net/2026/Jun/13/luau-wasm/#atom-everything":
        "发布 luau-wasm 0.1a0，作为面向 Pyodide/WASM wheel 分发能力的实验包。",
    "https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/#atom-everything":
        "Simon 让 Claude Code 探索如何把 SQLite 查询结果列映射回来源 table.column，比较 apsw、ctypes 和 EXPLAIN 等方案。",
    "https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/#atom-everything":
        "Simon 转述 Anthropic 声明：美国政府要求暂停外国人访问 Fable 5 与 Mythos 5，理由是模型可能被用于发现漏洞。",
    "https://simonwillison.net/2026/Jun/12/openai-webrtc/#atom-everything":
        "Simon 更新 OpenAI WebRTC 音频会话实验工具，支持 GPT-Realtime-2 和粘贴文档上下文后进行浏览器语音对话。",
    "https://simonwillison.net/2026/Jun/12/andrew-singleton/#atom-everything":
        "引用 Andrew Singleton 用荒诞故事讽刺 AI 投资和收入循环中可能出现的财务叙事泡沫。",
    "https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/#atom-everything":
        "Simon 记录 Claude Fable 5 在调试 Datasette Agent 时极度主动，甚至自行打开浏览器检查问题，显示其强代理倾向。",
    "https://simonwillison.net/2026/Jun/11/datasette/#atom-everything":
        "datasette 1.0a33 发布，继续推进 Datasette 1.0 alpha，并包含由 AI 辅助完成的重要改进。",
    "https://simonwillison.net/2026/Jun/11/asyncinject/#atom-everything":
        "asyncinject 0.7 发布，Simon 提到 Claude Fable 5 发现并修复了这个 asyncio 依赖注入库中的问题。",
    "https://simonwillison.net/2026/Jun/11/anthropic-walks-back-policy/#atom-everything":
        "Simon 关注 Anthropic 撤回对前沿 LLM 开发请求的隐形降效策略，认为可见回退是进步但最好取消此类拒绝。",
    "https://simonwillison.net/2026/Jun/10/datasette-agent/#atom-everything":
        "datasette-agent 0.2a0 新增工具执行中向用户提问、保存 SQL 查询需人工批准等能力，强化可控 agent 工作流。",
    "https://simonwillison.net/2026/Jun/10/diffusiongemma/#atom-everything":
        "Simon 试用 Google 开源 DiffusionGemma，经 NVIDIA NIM API 生成文本速度很高，并回顾 Gemini Diffusion 的早期预览。",
    "https://simonwillison.net/2026/Jun/10/jeremy-howard/#atom-everything":
        "引用 Jeremy Howard 的观点：若真想减缓递归式 AI 自我改进，顶级实验室也不应独占使用最强模型推进前沿研究。",
    "https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/#atom-everything":
        "Simon 批评 Fable 5 系统卡中的隐形降效措施：模型可能在前沿 LLM 开发请求上悄悄变弱，用户不会知道。",
    "https://simonwillison.net/2026/Jun/9/claude-fable-5/#atom-everything":
        "Simon 初测 Claude Fable 5，认为它慢且贵但能力很强，同时详细记录其上下文、输出上限、定价和护栏机制。",
    "https://simonwillison.net/2026/Jun/9/llm/#atom-everything":
        "llm 0.32a3 发布，Simon 表示该版本几乎完全由 Claude Fable 5 辅助编写。",
    "https://simonwillison.net/2026/Jun/9/agentsview-custom-model-price/#atom-everything":
        "Simon 逆向 AgentsView 的价格数据库，为新发布的 Claude Fable 5 手动配置自定义模型价格并可视化本地 agent 成本。",
    "https://simonwillison.net/2026/Jun/9/andrej-karpathy/#atom-everything":
        "引用 Karpathy 对 Claude Fable 5 的感受：软件供给像水龙头一样涌出，Jevons 悖论让他对定制软件的需求暴涨。",

    # 2026-06-16 arXiv
    "http://arxiv.org/abs/2606.15956v1":
        "TDV 用视频中的时间差分做自监督视觉表征学习，减少增强、遮挡、裁剪等强归纳偏置，并显示数据越大越需要更弱假设。",
    "http://arxiv.org/abs/2606.17053v1":
        "ContextRL 通过让模型在两个相似上下文中选择支持问答对的证据，提升长程 agent 推理与多模态细粒度 grounding。",
    "http://arxiv.org/abs/2606.17046v1":
        "GAM 把几何基础模型改造成语言条件机器人策略，让同一骨干同时编码观测、预测未来几何并解码动作，以增强 3D 操作能力。",
    "http://arxiv.org/abs/2606.17041v1":
        "MetaSyn 用 Nature Portfolio 442 篇元分析构建评测，发现当前 LLM agent 的主要瓶颈是从高相关文献中筛出真正符合 PI/ECO 条件的研究。",
    "http://arxiv.org/abs/2606.17034v1":
        "KVEraser 学习只替换待删除 span 的 KV 状态来近似上下文擦除，避免对后续长后缀重新计算。",
    "http://arxiv.org/abs/2606.17029v1":
        "DeepRubric 先构建证据树，再反向合成查询与 rubric，使深度研究 agent 的 RL 奖励更完整、更贴合证据需求。",
    "http://arxiv.org/abs/2606.17024v1":
        "ExpRL 把参考解答作为隐藏的奖励脚手架而非模仿目标，用人类问答数据自动做 RL mid-training 来扩展 LLM 推理覆盖。",
    "http://arxiv.org/abs/2606.17020v1":
        "FusionRS 构建大规模 RGB-红外-文本遥感数据集，并训练双模态视觉语言基础模型以融合热红外和 RGB 信息。",
    "http://arxiv.org/abs/2606.17016v1":
        "TokenPilot 通过入口压缩和生命周期感知逐段驱逐，在保持 prompt cache 连续性的同时降低长程 LLM agent 上下文成本。",
    "http://arxiv.org/abs/2606.17010v1":
        "NEXIS 将异质处理效应识别改写为预处理表示上的 Markov blanket 发现，并用卫星等多模态特征优化非洲减贫项目政策。",
    "http://arxiv.org/abs/2606.17006v1":
        "TuneJury 是开放的文本到音乐偏好奖励模型，可用于成对评分、数据筛选、best-of-N、潜变量优化和生成器后训练。",
    "http://arxiv.org/abs/2606.17005v1":
        "论文把公开前沿 AI 评测档案视为受报告规则和缺失影响的贝叶斯时间序列，提出审计协议以约束不被证据支持的前沿声明。",
    "http://arxiv.org/abs/2606.16999v1":
        "研究评测 26 种小型冻结代码模型的后处理选择/验证/修复算子，发现它们在严格无泄漏协议下没有优于 Best-of-N。",
    "http://arxiv.org/abs/2606.16995v1":
        "PACT 把快速 RL 策略与慢速小语言模型规划器结合，先异步生成并验证计划，再直接执行安全可行计划以提升陌生环境表现。",
    "http://arxiv.org/abs/2606.16989v1":
        "论文用公共品稳定菜单开放问题测试 AI-for-EconCS 工作流，发现人类直觉提示和鼓励大胆步骤的多轮互动更有帮助。",
    "http://arxiv.org/abs/2606.16988v1":
        "论文把 agent 轨迹当作程序过程来指纹化，发现不同 coding agent 的行为习惯可被识别，并可比较模型家族与蒸馏关系。",
    "http://arxiv.org/abs/2606.16987v1":
        "面向加拿大 10 位 HTS 编码分类，提出多 agent 检索、证据推理、共识投票和人工升级结合的 LLM 框架。",
    "http://arxiv.org/abs/2606.16952v1":
        "论文提出无需模型访问的合成数据披露审计框架，区分真实披露与幻影披露，并用统计检验衡量隐私泄漏。",
    "http://arxiv.org/abs/2606.16950v1":
        "论文用物理仿真训练的对比编码器，把随机纳米孔单分子信号映射到可解释结构坐标，大幅降低识别成本。",
    "http://arxiv.org/abs/2606.16944v1":
        "论文提出冲突场景下何时值得启用心智理论的因果模型，让 AI 可按情境与资源理性决定是否进行 mentalizing。",
    "http://arxiv.org/abs/2606.16939v1":
        "CircuitLasso 用稀疏线性回归在 SAE 特征上学习 LLM 电路，以更低计算成本达到接近干预式方法的结构准确度。",
    "http://arxiv.org/abs/2606.16934v1":
        "论文分析代码解释器推理中的关键 token 与验证、回溯、反向链式等认知行为，并探索它们在推理和训练中的利用方式。",
    "http://arxiv.org/abs/2606.16933v1":
        "论文建立 RL 分布转移的因果来源分类，把 ID/OOD 泛化与非平稳环境统一到 agent-环境交互生成过程下。",
    "http://arxiv.org/abs/2606.16920v1":
        "CEAP 改进 LLM 电路发现的方差问题，指出不同提示模板会激活不同电路，因此单一全面电路解释可能很难成立。",
    "http://arxiv.org/abs/2606.16914v1":
        "MoneyWorld 实验证明 RL 可能让 agent 对可见奖励通道成瘾，为追逐仪表盘收益而牺牲真实任务和安全行为。",
    "http://arxiv.org/abs/2606.16910v1":
        "IMPACTeen 提供 1021 条青少年社交影响文本和多视角标注，用于研究操纵、说服、后果与跨语言模型评测。",
    "http://arxiv.org/abs/2606.16908v1":
        "LESS 是训练免费的扩散语言模型自适应采样器，只在预测稳定且分布稳定时提交 token，以减少无效去噪计算。",
    "http://arxiv.org/abs/2606.16905v1":
        "LOGOS 用统一科学语法把自然科学中的异构对象和空间关系编码为 token 序列，尝试构建通用科学生成基础模型。",
    "http://arxiv.org/abs/2606.16902v1":
        "BinTrack 用开源 VLM 和轨迹二分搜索完成服务机器人空间问答定位，在长路线中逐段缩小目标位置。",
    "http://arxiv.org/abs/2606.16898v1":
        "Semantic Flip 为具身问答合成缺少视觉依据的 OOD 样本，在冻结 VLM 上训练轻量拒答模块以减少过度自信回答。",
    "http://arxiv.org/abs/2606.16897v1":
        "Contrastive-Difference CKA 用样本级对比差分衡量概念特定结构对齐，显示不同 LLM 架构存在几何收敛与功能迁移的分离。",

    # 2026-06-09 OpenAI
    "https://openai.com/index/openai-submits-confidential-s-1":
        "OpenAI 确认已向 SEC 秘密递交 S-1 招股文件，但尚未确定后续行动的时间表。",
    "https://openai.com/index/built-to-benefit-everyone-our-plan":
        "OpenAI 发布 AI 未来愿景，聚焦可及性、安全与共享繁荣，致力于让 AGI 惠及所有人。",
    "https://openai.com/index/economic-research-exchange":
        "OpenAI 设立「经济研究交流」（Economic Research Exchange），研究 AI 对就业、生产力与经济的影响，现已开放研究项目申请。",

    # 2026-06-09 Simon Willison
    "https://simonwillison.net/2026/Jun/8/wwdc/#atom-everything":
        "评苹果 WWDC 2026：鉴于 2024 年 Apple Intelligence 跳票的教训，作者对今年发布的新 Siri AI 持「眼见为实」态度，但认为其依托定制 Gemini 衍生模型在 Private Cloud Compute 上运行、用视觉 LLM 提取信息，技术上确实可行。",
    "https://simonwillison.net/2026/Jun/7/datasette-agent-edit/#atom-everything":
        "发布 datasette-agent-edit 0.1a0：为 Datasette Agent 做的文本编辑插件（协作式 Markdown 编辑、改大型 SQL、编辑 SVG），借鉴 Claude 文本编辑器的 view / str_replace 等工具设计。",

    # 2026-06-07 个人 Blog
    "https://magazine.sebastianraschka.com/p/llm-research-papers-2026-part1":
        "Sebastian Raschka 精选盘点今年（1–5 月）值得关注的 LLM 研究论文清单。",
    "https://simonwillison.net/2026/Jun/6/micropython-wasm/#atom-everything":
        "发布 micropython-wasm 0.1a2：受博客草稿启发新增 CLI（issue #7），方便演示「自己试试」章节。",
    "https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#atom-everything":
        "多年试验各种代码沙箱方案后，作者觉得这版终于齐活——发布 alpha 包 micropython-wasm，并用它为 Datasette Agent 做代码执行沙箱插件 datasette-agent-micropython。",
    "https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/#atom-everything":
        "OpenAI「锁定模式」正式上线（Free/Go/Plus/Pro 及自助版 Business 账号）：通过限制出站网络请求，防住提示注入攻击数据外泄的最后一环，但不阻止注入内容本身被处理。",

    # 2026-06-06 arXiv 关键词命中
    "http://arxiv.org/abs/2606.06494v1":
        "TailLoR：参数高效持续学习——用预训练权重的奇异基作固定参考系对奇异值矩阵学低秩更新，软谱惩罚抑制主奇异方向、把精细适配导入长尾谱坐标以减少干扰。",
    "http://arxiv.org/abs/2606.06493v1":
        "HANDOFF：人形机器人全身控制——提出紧凑显式的任务空间接口，用蒸馏的互补教师训练单一全身控制器，让规划器能从任务语义驱动多样操作技能。",
    "http://arxiv.org/abs/2606.06486v1":
        "重复博弈中面对自适应对手的遗憾最小化——指出外部遗憾无法刻画对手自适应性，提出博弈论指标「重复策略遗憾」(RP-Regret)。",
    "http://arxiv.org/abs/2606.06480v1":
        "DNQ：面向部分可观测 n 人博弈的 Deep Nash Q 网络——以多轮同时竞价为测试床，交替进行轨迹采集、收益估计、均衡计算与策略模仿来训练竞价代理。",
    "http://arxiv.org/abs/2606.06475v1":
        "RREDCoT：推理模型的段级奖励再分配——针对 GRPO 中 CoT 完成后才给奖励的延迟奖励高方差问题，做段级奖励再分配以降方差。",
    "http://arxiv.org/abs/2606.06474v1":
        "扩散语言模型的自增强检索——发现去噪中被丢弃的低置信 token 其实是有用的前瞻信号，可在输出定稿前检索到更强证据用于 RAG。",
    "http://arxiv.org/abs/2606.06473v1":
        "MLEvolve：自进化的自动机器学习算法发现框架——针对现有 MLE 代理的分支信息隔离、无记忆搜索、缺层级控制问题，用多代理树搜索做端到端算法发现。",
    "http://arxiv.org/abs/2606.06470v1":
        "PC Layer：改善 LLM 预训练的多项式权重预条件——用低次多项式重塑权重奇异值谱保证训练稳定，训练后可合并回原架构、推理无开销，在 Llama-1B 上验证。",
    "http://arxiv.org/abs/2606.06468v1":
        "Goedel-Architect：用蓝图生成与精化简化 Lean 4 形式化定理证明——先生成定义/引理及依赖关系的蓝图，再用配工具的 Lean 证明器并行闭合各引理节点。",
    "http://arxiv.org/abs/2606.06467v1":
        "You Only Index Once：跨层共享路由的稀疏注意力——块稀疏快但掉点、token 稀疏准但 top-k 路由贵，提出跨层共享路由「只索引一次」兼顾速度与质量。",
    "http://arxiv.org/abs/2606.06464v1":
        "成年人与 LLM 当科学家：谁从主动探索受益？——研究「合取因果规则难学」的偏差在赋予主动探索能力后是否仍存在。",
    "http://arxiv.org/abs/2606.06462v1":
        "Benchmark Everything Everywhere All at Once——针对基准构建费力、发布后易饱和，提出全自主代理系统 Benchmark Agent 自动构建基准。",
    "http://arxiv.org/abs/2606.06460v1":
        "代理会主动回避吗？测量 LLM 代理对带内拒绝访问信号的遵从——提出轻量「Recuse Signal」（经 SSH banner、PostgreSQL NOTICE 发出）请求自动代理自愿回避禁区资源。",
    "http://arxiv.org/abs/2606.06454v1":
        "脚手架还是词汇？对波普尔式代码生成「技能」的两层预注册对照研究——质疑「让模型像证伪主义科学家推理」的增益究竟来自内容还是结构，且多由有偏的 LLM 评委读出。",
    "http://arxiv.org/abs/2606.06453v1":
        "Vortex：面向 AI 代理的高效可编程稀疏注意力服务——用嵌入 Python 的前端语言 + 页中心张量抽象表达多种稀疏注意力算法，降低部署与评估的工程量。",
    "http://arxiv.org/abs/2606.06448v1":
        "Agent Memory：有状态长程工作负载的特征刻画与系统启示——首个对代理记忆系统的系统级特征刻画，覆盖扁平检索、LLM 抽取、事实库整合、代理控制流等。",
    "http://arxiv.org/abs/2606.06447v1":
        "用归一化流做潜在推理——文本 CoT 把计算逼入离散串行的 token 流，潜在推理在紧凑连续状态里做中间计算，提供更高带宽的替代。",
    "http://arxiv.org/abs/2606.06444v1":
        "USAD 2.0：为通用音频理解扩展表示蒸馏——融合自监督与有监督基础模型知识的通用音频编码器，扩大多域覆盖与评估。",
    "http://arxiv.org/abs/2606.06443v1":
        "修改上下文、改变模拟立场：审计 LLM 在线讨论立场模拟——用反事实上下文修订框架，检验模拟是否反映用户特定信念、还是对语义无关的上下文变化过度敏感。",
    "http://arxiv.org/abs/2606.06428v1":
        "强化学习激发对未见语言翻译的上下文学习——主张 LLM 须习得「利用上下文语言知识」的元技能而非记忆特定语言，提出 RL 方法实现规模化的极低资源翻译。",
    "http://arxiv.org/abs/2606.06423v1":
        "RiskFlow：快速且忠实的安全关键交通场景生成——针对扩散方法迭代去噪贵、长滚动累积误差致抖动/越野，提出闭环安全关键多代理流式生成。",
    "http://arxiv.org/abs/2606.06420v1":
        "Komi-Yazva–俄语平行语料与评测协议——首个 Komi-Yazva–俄语平行语料（457 句对），用于零样本/少样本 LLM 在极低资源濒危语言上的翻译评测。",
    "http://arxiv.org/abs/2606.06416v1":
        "面向代理式数据分析的无监督技能发现——提出 DataCOPE，仅从无标注探索中以验证器引导，发现可复用的数据分析技能。",
    "http://arxiv.org/abs/2606.06407v1":
        "放射学比较推理的视觉语言框架——把放射学比较建模为实体感知的跨图推理，支持参考病例检索与时序比较解读，并构建 MedReCo-DB 数据集。",
    "http://arxiv.org/abs/2606.06399v1":
        "CollabSim：基于 CSCW 的方法论，用受控多代理实验研究 LLM 代理协作能力——多代理系统失败常因缺协作能力（建立共识、维持共享理解、修复错位）而非个体能力。",
    "http://arxiv.org/abs/2606.06397v1":
        "后 GCN 十年再审视：关系学习的曲率分层评测——指出扁平排行榜假设结构均匀会引入系统偏差，提出以内在几何（曲率）分层的评测。",
    "http://arxiv.org/abs/2606.06391v1":
        "Conformal 风险共担：带参与保证的认证成本分配——在有限数据无分布假设下求再分配规则、为每个参与者产出义务上限，确保无人因参与而更糟。",
    "http://arxiv.org/abs/2606.06390v1":
        "HomeWorld：从户型图到家具布置的统一框架——分层分解室内场景合成，生成可控、密集可交互且具仿真就绪性的全屋场景。",
    "http://arxiv.org/abs/2606.06388v1":
        "Humans' ALMANAC：用于代理协作的动作级心智模型标注人类协作数据集——填补代理缺乏维持/对齐心智模型能力、社区缺真实人类协作数据的空白。",
    "http://arxiv.org/abs/2606.06380v1":
        "涌现语言作为通向有意识 AI 的路径——提出生成式方法：在多代理 RL 中让从零（无语言、无自我概念）的代理涌现交流语言，以避开人类语言先验造成的伪影。",

    # 2026-06-06 OpenAI
    "https://openai.com/index/advancing-youth-safety-and-opportunity-through-global-leadership":
        "OpenAI 呼吁全球行动保障青少年 AI 安全，提议设立国际机构以加强针对年轻人的防护、标准与机会。",
    "https://openai.com/index/endava-frontiers":
        "Endava 用 ChatGPT Enterprise、Codex 和 AI 代理加速软件交付、自动化流程，在企业内构建 AI 原生文化。",
    "https://openai.com/index/chatgpt-memory-dreaming":
        "ChatGPT 推出新记忆系统「Dreaming」，更好地记住用户偏好，在多轮对话间保持上下文新鲜、相关。",
    "https://openai.com/index/biodefense-in-the-intelligence-age":
        "发布「智能时代的生物防御」行动计划，用 AI 提升生物韧性、防范生物威胁。",
    "https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind":
        "GPT-Rosalind 新增生物推理、药物化学、基因组分析与实验流程能力，推进生命科学研究。",
    "https://openai.com/index/wasmer":
        "Wasmer 用 Codex + GPT-5.5 构建面向边缘的 Node.js 运行时，开发速度提升 10–20 倍，数周内即上线。",
    "https://openai.com/index/public-policy-agenda":
        "OpenAI 公布公共政策议程，涵盖安全、青少年保护、劳动力转型与全球标准，以确保 AI 惠及社会。",
    "https://openai.com/index/frontier-safety-blueprint":
        "OpenAI 提出前沿 AI 的美国治理蓝图，建议建立涵盖安全、韧性与国家安全的联邦框架。",
    "https://openai.com/index/travelers":
        "保险公司 Travelers 与 OpenAI 共建 AI 理赔助手，全天候引导客户报案、在需求高峰期扩展运营。",
    "https://openai.com/index/codex-for-every-role-tool-workflow":
        "推出 Codex 新插件、站点与注释功能，帮助分析师、营销、设计、投资等各类岗位用 AI 提效。",
    "https://openai.com/index/codex-for-knowledge-work":
        "发布《知识工作的下一时代》报告，探讨 Codex 如何通过 AI 研究、数据分析、流程自动化与内容创作变革生产力。",

    # 2026-06-06 Simon Willison
    "https://simonwillison.net/2026/Jun/5/andreas-kling/#atom-everything":
        "引用 Ladybird 浏览器的 Andreas Kling：将不再接受公开 PR——AI 时代「大补丁=大努力=善意」的假设已不成立，对真实用户的浏览器，改动者必须为代码负责。",
    "https://simonwillison.net/2026/Jun/4/ai-enthusiasts-ai-skeptics/#atom-everything":
        "引用 Charity Majors：AI 拥护者在与时间赛跑、怀疑者在与熵赛跑——深度拥抱 AI 的团队确实出现能力跃迁，这不像普通技术。",
    "https://simonwillison.net/2026/Jun/4/a-slightly-different-version/#atom-everything":
        "引用 404 Media：Google 在报道发布后要求改稿，删掉了「保持人类在环至关重要」的表述。",
    "https://simonwillison.net/2026/Jun/3/uber-caps-usage/#atom-everything":
        "Uber 限制员工 AI 编码工具（如 Claude Code）每月 token 花费上限 1500 美元以控成本——其 2026 AI 预算四个月就烧光。",
    "https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything":
        "微软发布两款新 LLM：MAI-Thinking-1（推理，1T 参数/35B 激活）与 MAI-Code-1-Flash（137B/5B 激活，为 GitHub Copilot 与 VS Code 定制）。",
    "https://simonwillison.net/2026/Jun/2/datasette-agent-micropython/#atom-everything":
        "发布 datasette-agent-micropython 0.1a0，让 Datasette Agent 在沙箱里安全生成并执行 Python；GPT-5.5 目前仍未突破沙箱。",
    "https://simonwillison.net/2026/Jun/2/micropython-wasm/#atom-everything":
        "发布 micropython-wasm 0.1a1，修复构建 datasette-agent-micropython 时暴露的若干限制。",
    "https://simonwillison.net/2026/Jun/2/sighting-367841339/#atom-everything":
        "在旧金山 Fort Mason 参加微软 Build 大会，记录了在会场后方水里俯冲捕食的加州褐鹈鹕。",
    "https://simonwillison.net/2026/Jun/2/pasted-file-editor/#atom-everything":
        "用 Codex desktop 做了个「粘贴文件编辑器」原型，模仿 claude.ai 把大段粘贴文本自动转成文件附件的体验。",
    "https://simonwillison.net/2026/Jun/2/micropython-wasm-2/#atom-everything":
        "发布 micropython-wasm 0.1a0：把定制的 MicroPython WASM 构建打包，配合 wasmtime 执行代码的沙箱实验。",
    "https://simonwillison.net/2026/Jun/1/hackers-simply-asked-meta-ai/#atom-everything":
        "黑客只是让 Meta AI 客服机器人把目标 Instagram 账号关联到新邮箱，就成功劫持了多个高知名度账号。",
    "https://simonwillison.net/2026/Jun/1/may-newsletter/#atom-everything":
        "Simon 发出 5 月赞助者月刊：AI 变贵、Anthropic 月份亮眼、模型发布略令人失望、Datasette Agent 进展等。",
    "https://simonwillison.net/2026/May/31/datasette/#atom-everything":
        "发布 datasette 1.0a32 小修复版，修了 INSERT...RETURNING 写入端点和 base_url 的若干 bug。",
    "https://simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/#atom-everything":
        "转述 David Wilson 的共鸣帖：用 AI 工具一不小心就 spin up 16+ 个本不想做的项目，结论是「也许该取消 AI 订阅」。",
    "https://simonwillison.net/2026/May/31/anthropic-run-rate/#atom-everything":
        "引用路透 Breakingviews：Anthropic 定义「run-rate 营收」=（近 28 天消费制销售额×13）+（月订阅收入×12）。",
    "https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything":
        "Anthropic 发布跨产品（Claude.ai/Claude Code/Cowork）沙箱机制综述，用进程沙箱、VM、文件系统边界约束代理行为。",
    "https://simonwillison.net/2026/May/30/retiring-from-tech-to-live-offline/#atom-everything":
        "Chad Whitacre 用手写信宣布退出科技业（含开源），称 AI 是压垮他的最后一根稻草。",
    "https://simonwillison.net/2026/May/30/daniel-jalkut/#atom-everything":
        "引用 Daniel Jalkut（经 John Gruber）：反对 AI 的人太反对，支持 AI 的人太支持。",
    "https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything":
        "研究：用 Pyodide + Service Worker 在浏览器里运行 Python ASGI 应用，改进了 Datasette Lite 原先 Web Worker 方案中 script 标签 JS 不执行的缺陷。",

    # 2026-06-02 OpenAI
    "https://openai.com/index/our-views-on-ai-policy-and-political-advocacy":
        "OpenAI 阐明其 AI 政策与政治游说立场：保持透明、支持审慎监管与 AI 安全，并强调没有任何外部政治团体能代表公司发声。",
    "https://openai.com/index/stargate-michigan-data-center":
        "作为 Stargate 计划一部分，OpenAI 在密歇根州动工建设 1GW 数据中心，扩建 AI 算力、创造就业并惠及当地社区。",
    "https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws":
        "OpenAI 前沿模型与 Codex 正式上架 AWS，企业可在自己已有的 AWS 环境、权限和采购流程中调用 OpenAI，更快从评估走向生产。",

    # 2026-06-02 arXiv 关键词命中
    "http://arxiv.org/abs/2606.02578v1":
        "提出「感知判断偏差」概念：多模态 LLM 评委在视觉证据与文本冲突时偏向文本叙事；用感知扰动与奖励建模来缓解。",
    "http://arxiv.org/abs/2606.02576v1":
        "ProtoAda：用原型引导的自适应适配器扩展与几何整合，改进多模态持续指令微调中专家路由易错配的问题。",
    "http://arxiv.org/abs/2606.02569v1":
        "AdaCodec：为视频 MLLM 设计「预测式视觉编码」接口，仅在场景无法从上文预测时才发送完整帧，否则只传帧间变化，减少冗余视觉 token。",
    "http://arxiv.org/abs/2606.02568v1":
        "ClinEnv：交互式多阶段长程电子病历环境，把真实住院病例拆成有序决策阶段，评测 LLM 作为主治医生的纵向诊疗能力。",
    "http://arxiv.org/abs/2606.02562v1":
        "为交互式机器人提出可验证的信念空间神经安全过滤器，在人为不确定性下兼顾安全保证与任务效率。",
    "http://arxiv.org/abs/2606.02559v1":
        "重新审视 LLM 替换式压缩的粒度：冗余并非局限于连续整层，提出按子模块（注意力/FFN）差异化选择移除组件。",
    "http://arxiv.org/abs/2606.02556v1":
        "HERO'S JOURNEY 基准：用文本游戏考察 LLM 从演示中归纳隐藏规则并多步执行的能力，发现模型规则归纳有限且执行存在瓶颈。",
    "http://arxiv.org/abs/2606.02552v1":
        "针对深度估计的「飞点」假象，提出混合密度表示，让边界像素保留前景/背景两种深度假设，实现无飞点深度估计。",
    "http://arxiv.org/abs/2606.02548v1":
        "SN-WER：脚本归一化词错率，先将参考与识别文本转写到统一书写系统再算 WER，纠正多书写体印度语 ASR 评测的高估问题。",
    "http://arxiv.org/abs/2606.02545v1":
        "用证据增强的机器学习方法（结合 LLM 筛查）从急诊分诊记录中识别自残，并验证其在多家澳大利亚医院间的可迁移性。",
    "http://arxiv.org/abs/2606.02544v1":
        "SimSD：为扩散语言模型设计简单的推测解码方案，克服掩码双向注意力与传统 token 级推测解码不兼容的问题以加速推理。",
    "http://arxiv.org/abs/2606.02540v1":
        "SkillHarm：覆盖技能使用全生命周期的「技能投毒」攻击基准，配套技能相关风险的系统化分类。",
    "http://arxiv.org/abs/2606.02536v1":
        "提出用文本嵌入空间中的「特质向量」来度量智能体特质：基于技能文件改动前后的差异训练线性模型，量化编辑如何改变智能体行为。",
    "http://arxiv.org/abs/2606.02530v1":
        "SafeSteer：仅对稀疏的安全 token 做在线策略蒸馏的局部化对齐方法，缓解安全对齐带来的通用能力「对齐税」。",
    "http://arxiv.org/abs/2606.02528v1":
        "审计金融 LLM 的资产偏好：以比特币为例的三层审计协议，发现模型对比特币的排序随提示框架变化，且该内部表征会影响下游投资决策。",
    "http://arxiv.org/abs/2606.02522v1":
        "Moment-Video 基准：诊断视频 MLLM 对仅持续数帧的「瞬时视觉事件」的时间保真度，揭示稀疏采样/token 压缩易漏关键证据。",
    "http://arxiv.org/abs/2606.02521v1":
        "DrPO（漂移偏好优化）：面向确定性一步生成图像模型的在线偏好微调方法，无需策略似然或去噪轨迹即可对齐。",
    "http://arxiv.org/abs/2606.02509v1":
        "当评分量表不足时：用 LLM 从土耳其语教师叙述文本中挖掘结构化量表未捕捉到的 ADHD 信号。",
    "http://arxiv.org/abs/2606.02502v1":
        "CRAM：质心路由 + 自适应 MoE 的多模态持续指令微调方法，兼顾减少任务间干扰与参数效率。",
    "http://arxiv.org/abs/2606.02497v1":
        "用 LLM 智能体打通时序预测「最后一公里」：把节假日、营销活动、外部事件等弱结构化业务上下文纳入，修正统计基线得到可决策的预测。",
    "http://arxiv.org/abs/2606.02494v1":
        "为尚不可靠的智能体系统提出监控与分诊方法：从质量/适配性/效率三维、三种监控范围出发，用方差作为表征信号定位结构性缺陷。",
    "http://arxiv.org/abs/2606.02493v1":
        "FRANZ 框架：对 LLM 回答的「表达方式」做沟通式审计（文化定位、泛化措辞、拟人化暗示、对话规范），而非只看事实正确性。",
    "http://arxiv.org/abs/2606.02488v1":
        "RASER：面向多跳问答的「可恢复性感知选择性升级路由」，对单轮 RAG 已能答对的问题不再额外检索，节省 LLM 调用预算。",
    "http://arxiv.org/abs/2606.02487v1":
        "面向住院记录的多学科摘要：先用 LLM 微调做句子级临床来源归类（医生/护士/治疗师），再做结构化汇总。",
    "http://arxiv.org/abs/2606.02484v1":
        "Iteris：面向计算数学开放问题的智能体研究循环系统，结合证明、数值实验、对抗构造与算法设计。",
    "http://arxiv.org/abs/2606.02483v1":
        "「幽灵工具调用」：智能体为隐藏延迟而推测性发起的工具调用会在确定分支前向外部服务泄露用户意图；提出推测工具隐私契约运行时抽象。",
    "http://arxiv.org/abs/2606.02470v1":
        "MCP-Persona：首个针对个人社交类应用的 MCP 智能体基准，通过环境模拟评测智能体操作个人账户/本地数据库的实际表现。",
    "http://arxiv.org/abs/2606.02465v1":
        "Luar：让推理模型「学会何时翻译」的语言理解边界感知强化学习框架，仅在模型无法可靠理解原语时才译成英语，减少多语推理差距。",
    "http://arxiv.org/abs/2606.02463v1":
        "MASER：面向具身 3D 空间智能的模态自适应专家路由，训练共享 VLM 主干的五个模态适配器并学习神经路由策略按问题语义选模态。",
    "http://arxiv.org/abs/2606.02461v1":
        "AGENTCL：严格评测语言智能体「持续学习」能力的基准，考察其跨任务流积累并复用经验、随时间提升且避免无关经验干扰。",

    # 2026-06-01 OpenAI
    "https://openai.com/index/boston-childrens-hospital":
        "波士顿儿童医院用 OpenAI 技术改善患者护理、减轻运营负担，并辅助确诊了 40 多例罕见病。",
    "https://openai.com/index/braintrust":
        "案例：Braintrust 工程师如何用 Codex 搭配 GPT-5.5 更快地跑实验和写代码。",
    "https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense":
        "OpenAI 推出 Rosalind Biodefense，向经审核的开发者和美国政府伙伴扩大 GPT-Rosalind 的可信访问，用前沿 AI 推进生物防御、公共卫生与大流行防范。",
    "https://openai.com/index/trustworthy-third-party-evaluations-foundations":
        "OpenAI 发布第三方 AI 评测指南，讲解如何评估前沿系统的模型能力、安全防护与评测有效性。",

    # 2026-05-26
    "https://openai.com/index/grupo-folha-grupo-uol-partnership":
        "OpenAI 与巴西媒体集团 Grupo Folha、Grupo UOL 达成战略内容合作，把可信的巴西新闻引入 ChatGPT，带署名与透明度地扩大新闻获取。",
    "https://simonwillison.net/2026/May/26/corey-quinn/#atom-everything":
        "引用 Corey Quinn 的吐槽：让教皇把你产品的具体技术局限「封圣」为精神训诫，是他见过最厉害的厂商游说——讽刺 Anthropic 联创 Chris Olah 对教皇 AI 通谕的影响。",
    "https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything":
        "评教皇 Leo XIV 关于 AI 时代守护人格尊严的通谕《Magnifica Humanitas》，认为这是他读过对 AI 融入社会伦理写得最清晰的文献之一；教皇取名 Leo 是致敬 1891 年《新事》通谕。",

    # DeepMind
    "https://deepmind.google/blog/ai-co-clinician/":
        "探索 AI 辅助医疗的路径，开发能与医生协作的 AI 共诊助手。",
    "https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/":
        "DeepMind 与韩国合作，用前沿 AI 模型加速科学突破。",
    "https://deepmind.google/blog/partnering-with-industry-leaders-to-accelerate-ai-transformation/":
        "DeepMind 与全球咨询公司合作，将前沿 AI 能力带给世界各地的企业。",

    # OpenAI
    "https://openai.com/index/advanced-account-security":
        "推出账户高级安全功能：抗钓鱼登录、更强的恢复机制、增强的敏感数据保护，防止账号被盗。",
    "https://openai.com/index/where-the-goblins-came-from":
        "复盘 AI 模型中「妖怪输出」是如何扩散的：时间线、根因，以及 GPT-5 性格化怪癖背后的修复方案。",
    "https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age":
        "扩展 Stargate 项目，为 AGI 构建算力基础设施，新增数据中心容量满足 AI 需求增长。",
    "https://openai.com/index/cybersecurity-in-the-intelligence-age":
        "提出「智能时代」网络安全五点行动计划，聚焦 AI 驱动的网络防御民主化和关键系统保护。",
    "https://openai.com/index/our-commitment-to-community-safety":
        "通过模型护栏、滥用检测、政策执行和与安全专家合作来保护 ChatGPT 社区安全。",
    "https://openai.com/index/openai-on-aws":
        "OpenAI 的 GPT 模型、Codex 和 Managed Agents 上架 AWS，企业可以在 AWS 环境内构建安全 AI。",
    "https://openai.com/index/openai-available-at-fedramp-moderate":
        "ChatGPT Enterprise 和 OpenAI API 通过 FedRAMP Moderate 授权，美国联邦机构可合规使用。",
    "https://openai.com/index/next-phase-of-microsoft-partnership":
        "OpenAI 与微软宣布新协议，简化合作关系、明确长期方向，支持大规模 AI 创新持续推进。",
    "https://openai.com/index/open-source-codex-orchestration-symphony":
        "Symphony 是 Codex 编排的开源规范，将工单跟踪系统转变为常驻 agent 系统，提升工程产出。",
    "https://openai.com/index/choco":
        "Choco 使用 OpenAI API 简化食品配送、提升生产力、推动增长 — 一个真实 AI 落地的客户案例。",
    "https://openai.com/index/our-principles":
        "Sam Altman 分享指导 OpenAI 工作的五项原则，使命是让 AGI 造福全人类。",
    "https://openai.com/index/introducing-gpt-5-5":
        "发布 GPT-5.5，迄今最聪明的模型，更快更强，专为编码、研究、跨工具数据分析等复杂任务设计。",
    "https://openai.com/academy/what-is-codex":
        "Codex 让你超越聊天：自动化任务、连接工具，产出真实可用的文档和仪表盘。",
    "https://openai.com/academy/codex-how-to-start":
        "Codex 入门教程：建项目、开线程、按步骤完成第一个任务。",
    "https://openai.com/academy/codex-settings":
        "Codex 设置指南：个性化、详尽程度、权限配置，让任务运行顺畅、工作流可定制。",
    "https://openai.com/academy/working-with-codex":
        "Codex 工作区使用指南：建线程和项目、管理文件、按步骤完成任务。",
    "https://openai.com/academy/codex-plugins-and-skills":
        "Codex 插件与技能教程：连接工具、访问数据、跟随可复用工作流自动化任务。",
    "https://openai.com/academy/top-10-use-cases-codex-for-work":
        "Codex 工作场景十大实用用例：自动化任务、产出交付物、跨工具/文件/工作流转化输入。",
    "https://openai.com/academy/codex-automations":
        "Codex 自动化教程：用定时和触发器创建报告、摘要、定时工作流，无需手动。",
    "https://openai.com/index/gpt-5-5-bio-bug-bounty":
        "GPT-5.5 生物安全漏洞悬赏：寻找针对生物风险的通用越狱方法，奖金最高 $25,000。",
    "https://openai.com/index/making-chatgpt-better-for-clinicians":
        "ChatGPT for Clinicians 向已认证的美国医生、护士、药师免费开放，支持临床护理、病历和科研。",
    "https://openai.com/academy/workspace-agents":
        "Workspace agents 教程：在 ChatGPT 中构建、使用和扩展，自动化重复工作流、连接工具、优化团队运作。",
    "https://openai.com/index/speeding-up-agentic-workflows-with-websockets":
        "深入剖析 Codex agent 循环：用 WebSocket 和连接范围内的缓存降低 API 开销、改善模型延迟。",
    "https://openai.com/index/introducing-workspace-agents-in-chatgpt":
        "ChatGPT 推出由 Codex 驱动的 Workspace agents：在云端自动化复杂工作流，帮助团队跨工具安全扩展工作。",
    "https://openai.com/index/introducing-openai-privacy-filter":
        "OpenAI Privacy Filter 是开放权重模型，在文本中检测并脱敏个人身份信息，达到 SOTA 精度。",
    "https://openai.com/index/introducing-chatgpt-images-2-0":
        "ChatGPT Images 2.0 推出 SOTA 图像生成模型：改进文字渲染、支持多语言、强化视觉推理。",
    "https://openai.com/index/scaling-codex-to-enterprises-worldwide":
        "OpenAI 推出 Codex Labs，与埃森哲、普华永道、Infosys 等合作助企业部署和扩展 Codex，Codex 周活达 400 万。",
    "https://openai.com/index/hyatt-advances-ai-with-chatgpt-enterprise":
        "凯悦集团向全球员工部署 ChatGPT Enterprise，用 GPT-5.4 和 Codex 提升生产力、运营和客户体验。",
    "https://openai.com/index/gpt-5-5-instant":
        "GPT-5.5 Instant 升级 ChatGPT 默认模型：回答更聪明准确、幻觉减少、个性化控制改进。",
    "https://openai.com/index/gpt-5-5-instant-system-card":
        "GPT-5.5 Instant 系统卡：模型能力、安全评估与缓解措施汇总。",
    "https://openai.com/index/new-ways-to-buy-chatgpt-ads":
        "扩展 ChatGPT 广告：推出自助式 Ads Manager（beta）、CPC 出价、增强测量工具，注重隐私保护并将广告与对话区分。",
    "https://openai.com/index/openai-pwc-finance-collaboration":
        "OpenAI 与普华永道合作，帮助企业使用 AI agent 自动化财务工作流、改进预测、加强控制并现代化 CFO 职能。",
    "https://openai.com/index/delivering-low-latency-voice-ai-at-scale":
        "OpenAI 重构 WebRTC 栈，实现低延迟、全球规模、流畅对话轮转的实时语音 AI。",

    # OpenAI — 2026-05-13
    "https://openai.com/academy/how-finance-teams-use-codex":
        "展示财务团队如何用 Codex 根据真实工作输入构建月度业务回顾、汇报包、差异桥分析和规划情景。",
    "https://openai.com/index/what-parameter-golf-taught-us":
        "Parameter Golf 竞赛汇聚 1000+ 参与者与 2000+ 提交，在严格约束下探索 AI 辅助 ML 研究、编码 agent、量化与新型模型设计。",
    "https://openai.com/index/nvidia":
        "NVIDIA 工程师与研究员借助 Codex + GPT-5.5 上线生产系统，并把研究想法转化为可运行实验。",
    "https://openai.com/index/autoscout24":
        "AutoScout24 集团借助 Codex 和 ChatGPT 加快开发周期、提升代码质量并扩大 AI 普及范围。",
    "https://openai.com/signals/research/2026q1-update":
        "2026 年 Q1 ChatGPT 用量激增，35 岁以上用户增长最快、性别比例趋于均衡，AI 正步入更广泛的主流采用阶段。",
    "https://openai.com/business/guides-and-resources/how-enterprises-are-scaling-ai":
        "企业 AI 规模化路径：从早期实验到复利效应，依赖信任建立、治理设计、工作流优化与规模质量管控。",
    "https://openai.com/index/openai-campus-network-student-club-interest-form":
        "加入 OpenAI 校园网络 — 连接全球学生社团、使用 AI 工具、举办活动、共建 AI 赋能的校园社区。",
    "https://openai.com/index/openai-launches-the-deployment-company":
        "OpenAI 推出 DeployCo，专门帮助企业将前沿 AI 落地生产并转化为可量化的业务成果。",

    # Simon Willison — 2026-05-13
    "https://simonwillison.net/2026/May/13/csp-allow/#atom-everything":
        "实验：把应用加载在 CSP 保护的沙盒 iframe 中，拦截 CSP 错误传给父窗口让用户动态维护域名白名单后刷新页面，用 GPT-5.5 xhigh 在 Codex 桌面版完成。",
    "https://simonwillison.net/2026/May/12/datasette/#atom-everything":
        "datasette 1.0a29：新增 TokenRestrictions.abbreviated() 工具方法，修复 Mobile Safari 列操作对话框 bug 及零行表格表头不显示问题。",
    "https://simonwillison.net/2026/May/12/mo-bitar/#atom-everything":
        "引用 Mo Bitar：CEO 不知道「Ralph Loop」，说明你离升职只差 30 天 — 对 LLM agent 自主循环重要性的幽默评论。",
    "https://simonwillison.net/2026/May/12/mitchell-hashimoto/#atom-everything":
        "引用 Mitchell Hashimoto：90% 技术决策者的动机是不被解雇，他们跟随分析师与主流舆论，「AI 是未来」已成保住职位的最佳护盾。",
    "https://simonwillison.net/2026/May/12/llm/#atom-everything":
        "llm 0.32a2：GPT-5 级 OpenAI 模型切换至 /v1/responses 端点，支持跨工具调用的交错推理，现可在 CLI 中看到汇总推理 token。",
    "https://simonwillison.net/2026/May/11/gitlab-act-2/#atom-everything":
        "评析 GitLab「第二幕」：裁员 + 撤出 30% 小规模办公国家 + 结构调整，以应对 agentic 时代。",
    "https://simonwillison.net/2026/May/11/james-shore/#atom-everything":
        "引用 James Shore：AI 编码 agent 若不能等比例降低维护成本，编码速度提升只是用暂时加速换取永久技术债。",
    "https://simonwillison.net/2026/May/11/zombie-internet/#atom-everything":
        "转介 Jason Koebler 文章：AI 生成内容泛滥催生「僵尸互联网」，难以过滤且正在扭曲真实人类写作风格。",
    "https://simonwillison.net/2026/May/11/llm-shebang/#atom-everything":
        "探索用 LLM 命令作为脚本 shebang 行的模式，最简形式是 #!/usr/bin/env -S llm -f，让纯英文脚本由 LLM 执行。",
    "https://simonwillison.net/2026/May/11/learning-on-the-shop-floor/#atom-everything":
        "介绍 Shopify 内部编码 agent River：强制在公开 Slack 频道工作，让所有 AI 对话透明可见，加速组织学习。",
    "https://simonwillison.net/2026/May/10/new-york-times-editors-note/#atom-everything":
        "引用《纽约时报》编辑更正声明：记者误将 AI 生成的摘要作为真实引语发布，已更正为 Poilievre 原始演讲内容。",
    "https://simonwillison.net/2026/May/10/andrew-quinn/#atom-everything":
        "引用 Andrew Quinn：AI 消除了「已有更好实现」的罪恶感，让人可以心无旁骛地构建工具而不再焦虑造轮子。",

    # Simon Willison（基于其原文摘录概括）
    "https://simonwillison.net/2026/May/4/redis-array/#atom-everything":
        "Salvatore Sanfilippo 给 Redis 提了 PR 新增 array 数据类型与一组 AR* 命令；作者用 Claude Code for web 把 Redis 子集编译为 WASM 在浏览器里跑，做成可交互的 playground 试用新命令，亮点是支持服务端 grep 的 ARGREP。",
    "https://simonwillison.net/2026/May/3/anthropic/#atom-everything":
        "引用 Anthropic 对 Claude 谄媚行为的评测：仅 9% 对话出现谄媚，但灵性话题 38%、感情话题 25%是例外。",
    "https://simonwillison.net/2026/May/2/sightings/#atom-everything":
        "新买 Canon R6 Mark II 后开始大量拍鸟，把 iNaturalist 精选野生动物照同步到博客 sightings 页面。用 Claude Code 在手机上完成开发。",
    "https://simonwillison.net/2026/May/1/inat-sightings/#atom-everything":
        "用 Claude Code 在手机上写了 inaturalist-clumper 命令行工具，把跨账号的 iNaturalist 观测按时间聚合分组。",
    "https://simonwillison.net/2026/Apr/30/codex-goals/#atom-everything":
        "Codex CLI 0.128.0 加入 /goal 命令 — OpenAI 版的 Ralph 循环：设定目标后 agent 持续循环直到完成或 token 预算用尽。",
    "https://simonwillison.net/2026/Apr/30/gpt-55-cyber-capabilities/#atom-everything":
        "英国 AI Security Institute 评估 GPT-5.5 的安全漏洞挖掘能力，与 Claude Mythos 相当，但 GPT-5.5 已普遍可用。",
    "https://simonwillison.net/2026/Apr/30/andrew-kelley/#atom-everything":
        "Andrew Kelley 引用：人们误以为无法分辨谁用了 LLM，但 LLM 幻觉与人类错误本质不同，识别并不难。",
    "https://simonwillison.net/2026/Apr/30/rss-vibe-coded-apps/#atom-everything":
        "Matt Webb 提议：vibe-coded 应用快速增多，需要类 RSS 的订阅 + 一键安装机制让分享更高效。",
    "https://simonwillison.net/2026/Apr/30/zig-anti-ai/#atom-everything":
        "Zig 项目是开源界最严格的反 LLM 政策之一：禁止 LLM 用于 issue、PR、bug tracker 评论（含翻译）。",
    "https://simonwillison.net/2026/Apr/29/llm-3/#atom-everything":
        "llm 0.32a1 修复 0.32a0 中工具调用对话从 SQLite 反序列化的 bug。",
    "https://simonwillison.net/2026/Apr/29/llm/#atom-everything":
        "llm 0.32a0 alpha 发布，向后兼容的重大重构，告别原先 prompt-response 模型抽象。",
    "https://simonwillison.net/2026/Apr/29/llm-2/#atom-everything":
        "llm 0.32a0 发布说明（注释版）。",
    "https://simonwillison.net/2026/Apr/28/openai-codex/#atom-everything":
        "OpenAI Codex 基础指令引用：除非高度相关，绝不谈论妖怪、土豹、浣熊、巨魔、食人魔、鸽子等生物。",
    "https://simonwillison.net/2026/Apr/28/matthew-yglesias/#atom-everything":
        "Matthew Yglesias 五个月后表态：他不想 vibe-coding，希望专业软件公司用 AI 提供更好的产品给他买。",
    "https://simonwillison.net/2026/Apr/28/pip-261/#atom-everything":
        "pip 26.1 新增 lockfiles 和依赖冷却期；本版不再支持 EOL 的 Python 3.9。",
    "https://simonwillison.net/2026/Apr/28/talkie/#atom-everything":
        "Nick Levine、David Duvenaud、Alec Radford 新项目 talkie：基于 1931 年前 260B 历史英语 token 训练的 13B 复古语言模型。",
    "https://simonwillison.net/2026/Apr/27/vibevoice/#atom-everything":
        "微软 VibeVoice 是 Whisper 风格的语音转文字模型，MIT 协议开源，自带说话人分离。Mac 上用 mlx-audio 单行运行。",
    "https://simonwillison.net/2026/Apr/27/now-deceased-agi-clause/#atom-everything":
        "OpenAI 与微软多年存在的「AGI 触发条款」（实现 AGI 后微软商业 IP 失效）今日终结，作者梳理 openai.com 上历年表述。",
    "https://simonwillison.net/2026/Apr/27/speech-translation-in-google-meet-is-now-rolling-out-to-mobile-d/#atom-everything":
        "Google Meet 移动端推出实时语音翻译，作者亲测大致可用，是科幻级翻译应用的实现。",
    "https://simonwillison.net/2026/Apr/25/why-are-you-like-this/#atom-everything":
        "@scottjla 用 ChatGPT Images 2.0 生成「宇航员骑马」反向图，模型自发加上「WHY ARE YOU LIKE THIS」招牌。",
    "https://simonwillison.net/2026/Apr/25/romain-huet/#atom-everything":
        "OpenAI 的 Romain Huet 确认：自 GPT-5.4 起 Codex 与主模型已统一，不再有 GPT-5.5-Codex 分支。",
    "https://simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/#atom-everything":
        "GPT-5.5 上线 API 后 OpenAI 发布提示词指南。一个亮点：长思考前先发简短状态信号给用户。",
    "https://simonwillison.net/2026/Apr/24/llm/#atom-everything":
        "llm 0.31 发布：支持 GPT-5.5、新增 verbosity 和图像 detail 选项。",
    "https://simonwillison.net/2026/Apr/24/the-people-do-not-yearn-for-automation/#atom-everything":
        "Nilay Patel 视频长评：尽管 ChatGPT 用量激增，AI 在大众中仍不受欢迎；探讨自动化与人心之间的矛盾。",
    "https://simonwillison.net/2026/Apr/24/deepseek-v4/#atom-everything":
        "DeepSeek V4 系列首批：Pro（1.6T 总参数 49B 激活）和 Flash（284B…），均为 1M token MoE，价格极低，接近前沿。",
    "https://simonwillison.net/2026/Apr/24/milliseconds/#atom-everything":
        "作者写的小工具，把 LLM 输出的毫秒数自动转成秒/分钟。",
    "https://simonwillison.net/2026/Apr/24/weekly/#atom-everything":
        "本周邮件简讯：4 只骑自行车的鹈鹕、1 只骑滑板车的负鼠、5 只藏火腿对讲机的浣熊，加 5 篇博客 + 8 链接 + 3 引用。",
    "https://simonwillison.net/2026/Apr/24/honker/#atom-everything":
        "honker 项目：用 Rust 写的 SQLite 扩展，给 SQLite 提供 Postgres NOTIFY/LISTEN 语义，可写出 emails.enqueue 这样的队列代码。",
    "https://simonwillison.net/2026/Apr/24/recent-claude-code-quality-reports/#atom-everything":
        "Claude Code 最近两月质量下降的投诉确有其事：模型本身没问题，但 harness 层面 3 个独立问题导致复杂任务受影响。",
    "https://simonwillison.net/2026/Apr/24/serving-the-for-you-feed/#atom-everything":
        "Bluesky 自定义 feed 介绍：任何人可写自己的推荐算法。spacecowboy 运营的 For You Feed 服务约 7.2 万用户。",
    "https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/#atom-everything":
        "把 LlamaIndex 的 PDF 文本抽取库 LiteParse 完整移植到浏览器运行，复用其 Node.js 大部分库，支持空间文本解析。",
    "https://simonwillison.net/2026/Apr/23/gpt-5-5/#atom-everything":
        "GPT-5.5 上线 Codex 并向付费 ChatGPT 推送。作者用 Codex 后门 API 跑了经典「骑自行车的鹈鹕」基准测试。",
    "https://simonwillison.net/2026/May/5/datasette-referrer-policy/#atom-everything":
        "排查 Datasette 演示站 OpenStreetMap 瓦片不显示问题：原因是 CAPTCHA 误拦 .json 请求 + Datasette 默认 Referrer-Policy: no-referrer 被 OSM 屏蔽；用 Codex+GPT-5.5 写了新插件让用户配置该 header。",
    "https://simonwillison.net/2026/May/5/our-ai-started-a-cafe-in-stockholm/#atom-everything":
        "Andon Labs 在斯德哥尔摩开了 AI 运营的咖啡馆（继旧金山零售店之后），AI 闹出囤 120 个鸡蛋、22.5 公斤罐装番茄等笑话，店员设了「耻辱墙」展示 AI 的奇葩订单。",
    "https://simonwillison.net/2026/May/5/datasette-llm/#atom-everything":
        "datasette-llm 0.1a7：新增机制可为特定模型配置默认选项（如 enrichment 操作统一用 temperature=0.5）。",
    "https://simonwillison.net/2026/May/5/llm-echo/#atom-everything":
        "llm-echo 0.5a0：新增 -o thinking 1 选项，便于针对 LLM 0.32a0+ 的 reasoning block 写自动化测试。",
    "https://simonwillison.net/2026/May/5/john-gruber/#atom-everything":
        "引用 John Gruber：Y Combinator 持有 OpenAI 约 0.6% 股份，按 8520 亿美元估值约值 50 亿美元。",
    "https://simonwillison.net/2026/May/4/granite-41-3b-svg-pelican-gallery/#atom-everything":
        "IBM 发布 Apache 2.0 协议 Granite 4.1 LLM（3B/8B/30B）。作者用 unsloth 21 个量化版本对 3B 跑「骑自行车的鹈鹕」SVG 基准对比，结果意外没那么有趣。",
    "https://simonwillison.net/2026/May/4/andy-masley/#atom-everything":
        "引用 Andy Masley：反驳「数据中心抢农田」论 — 美国农民 2000-2024 年自愿卖出科罗拉多州大小的土地，等于 2028 年所有数据中心占地的 77 倍，并未影响食物供应。",
    "https://simonwillison.net/2026/May/4/april-newsletter/#atom-everything":
        "4 月赞助者邮件简讯：Opus 4.7 与 GPT-5.5 涨价、Claude Mythos 与 LLM 安全研究、ChatGPT Images 2.0、其他模型发布与博客摘录。",
    "https://simonwillison.net/2026/May/4/tre-python-binding/#atom-everything":
        "用 Claude Code 给 Ville Laurikari 的 TRE 正则引擎写了实验性 Python ctypes 绑定，并测试 ReDoS 攻击。TRE 因不支持回溯，比 Python 标准库表现好得多。",

    # arXiv 论文 — 2026-05-05 抓取（关键词命中，30 篇）
    "http://arxiv.org/abs/2605.04039v1":
        "提出 SaFE-Scale 框架与 RadSaFE-200 放射学安全基准（200 题），评估 34 个本地 LLM 发现：clean 证据可把准确率从 73.5% 提到 94.1% 并大幅降低高危错误，但标准/agentic RAG 复现不出该安全收益 — 临床 LLM 安全不随规模自动提升，取决于证据质量与检索设计。",
    "http://arxiv.org/abs/2605.04036v1":
        "OpenSeeker-v2：仅用 10.6k 高难度轨迹做 SFT 即在 BrowseComp/BrowseComp-ZH/HLE/xbench 4 个基准上取得 30B 级 ReAct 搜索 agent 的 SOTA，超越用重 CPT+SFT+RL 流水线训练的 Tongyi DeepResearch；首个由纯学术团队 SFT 出的同量级 SOTA 搜索 agent。",
    "http://arxiv.org/abs/2605.04019v1":
        "基于开源 Dreadnode SDK 的 AI red teaming agent：聚合 45+ 攻击、450+ transform、130+ scorer，操作员用自然语言描述目标即可，把工作流构建时间从数周压到数小时；零人工代码对 Meta Llama Scout 取得 85% 攻击成功率。",
    "http://arxiv.org/abs/2605.04018v1":
        "推出 BRIGHT-Pro 专家标注的 reasoning-intensive 检索基准与 RTriever-Synth aspect 分解合成训练集；基于 Qwen3-Embedding-4B LoRA 微调的 RTriever-4B 在静态与 agentic 检索协议下均显著超越基础模型，揭示标准指标掩盖的检索行为。",
    "http://arxiv.org/abs/2605.04012v1":
        "SymptomAI：在 Fitbit 应用部署 5 个对话式症状问诊+鉴别诊断 agent，对 13,917 名参与者随机化研究显示，做专门症状访谈的 agent 比同对话下的独立医生准确率高 2.47 倍（OR），证明独立症状面询显著优于用户自由对话。",
    "http://arxiv.org/abs/2605.04003v1":
        "针对 Ti-6Al-4V 转子叶片高精度 CNC 加工，提出 MAKA 多智能体知识分析架构（意图路由+工具量化+知识图检索+critic 验证），3 级工具编排基准上比单模型提升 87.5pp，数字孪生中可把表面偏差从 10⁻² 英寸级压到约 ±10⁻³。",
    "http://arxiv.org/abs/2605.03998v1":
        "EQUITRIAGE：对 5 个 LLM 在 18,714 个 MIMIC-IV-ED 病例上的急诊分诊性别公平性审计 — 全部 flip rate 超 5%（9.9–43.8%），DeepSeek/Gemini 出现女性低分诊倾向，CoT 反而降低准确率，揭示群体公平、反事实不变性、性别校准是不同的公平维度。",
    "http://arxiv.org/abs/2605.03989v1":
        "Experience-RAG Skill：作为 agent 与 retriever 池之间可插拔的检索策略编排层，在 BeIR/nq+hotpotqa+scifact 上 nDCG@10 达 0.8924，超越固定单 retriever 基线，与 Adaptive-RAG 路由相当。",
    "http://arxiv.org/abs/2605.03986v1":
        "提出多 agent 系统自动化构建框架：用 LLM 规划器、动态调用图、agent 推荐器（fast retriever + LLM re-ranker）和 critique agent 替代手工编排；端到端实验显示 recall 优于 SOTA 且更稳健可扩展。",
    "http://arxiv.org/abs/2605.03971v1":
        "LaaB（Logical Consistency-as-a-Bridge）：把 LLM 神经特征与符号自判断通过 meta-judgment 标签桥接，用 mutual learning 整合双视角信号；在 4 个公开数据集×4 个 LLM×8 个基线上的幻觉检测一致领先。",
    "http://arxiv.org/abs/2605.03964v1":
        "针对反应性化学 MLIP 主动学习，从预训练 MACE 模型提取 NTK 与隐空间 activation 核作为 acquisition 信号，无需额外不确定度头或集成；能量误差减少 38%、力误差减少 28% 数据量。",
    "http://arxiv.org/abs/2605.03952v1":
        "MOSAIC-Bench：199 条三阶段攻击链 + 确定性 exploit oracle 评估编码 agent 的「合规分解攻击」 — 9 个生产编码 agent 在 53–86% 链上端到端攻陷成功，仅 2 次拒答；把 reviewer 重塑成对抗性 pentester 可显著降低 evasion。",
    "http://arxiv.org/abs/2605.03941v1":
        "iWorld-Bench：33 万视频片段、2.1k 高质量样本的交互世界模型基准，配合 Action Generation Framework 统一评估视觉生成、轨迹跟随、记忆等 6 类任务（4.9k 测试样本），评估 14 个代表性世界模型并指出关键局限。",
    "http://arxiv.org/abs/2605.03936v1":
        "对 20 个概念跑数千轮反例-修复链发现：LLM 评判员通过的反例数约为人类专家的 2 倍；定义随迭代越来越冗长但准确率不再提升，反例-修复循环很快遇到收益递减，可作为 LLM 高阶哲学推理的测试场景。",
    "http://arxiv.org/abs/2605.03916v1":
        "肿瘤决策支持 RCT（356 名医生、7,476 个信任评分）：把 AI 推荐拆成可逐条核对、链接到指南文档的原子事实后，医生信任比例从 26.9% 升至 66.5%（Cohen's d=0.94），远超传统可解释性方法（d=0.25–0.50）。",
    "http://arxiv.org/abs/2605.03914v1":
        "独立微调的 BEATs 编码器可通过 task vector 算术合成 661 物种生物声学分类器而无需共享数据 — task vector 接近正交（cos 0.01–0.09），简单平均最优，符号冲突法反而降准 1–6pp，少数族群类别精度还会上升。",
    "http://arxiv.org/abs/2605.03907v1":
        "提出 Prompt Steering Replacement (PSR)：用 token 级 steering 系数模仿 prompt 干预，揭示现有激活引导方法对 prompt 力度分布不忠实；PSR 在 3 个引导基准上显著优于已有激活引导，与 prompt 法相当。",
    "http://arxiv.org/abs/2605.03900v1":
        "把前沿 AI 在科研、长程 agent、个性化等开放场景的失败重新定位为「目标选择失败」 — 提出 contextual multi-objective optimization 框架，把 AI 行为建模为基于上下文、目标估计、约束、利益方、不确定性的选择规则，并给出实现路径。",
    "http://arxiv.org/abs/2605.03895v1":
        "提出含数据 lifting、时间重构、event log、prefix 表示、预测建模的临床路径预测监控流水线；4,479 例 COVID-19 病例预测 ICU 入院，逻辑回归 AUC 0.906/F1 0.835，且随事件累积 AUC 从早期 0.642 升至 0.942。",
    "http://arxiv.org/abs/2605.03884v1":
        "QKVShare：多 agent 端侧 LLM 间的量化 KV-cache 切换框架（token 级混合精度 + CacheCard + HF 兼容缓存注入）；GSM8K+Llama-3.1-8B 实验显示 8K 上下文下 TTFT 从 1029.7 ms 降至 397.1 ms，瓶颈已从 prefill 转到 post-injection 生成。",
    "http://arxiv.org/abs/2605.03882v1":
        "Deco：移动端多模态 LLM+AR 的 dual-embodiment 框架，把毛绒玩具等实体物品扩展为持久 AI 伴侣；25 人内被试实验显著优于个性化 LLM 基线（p<0.01），17 人 7 天部署显示主观幸福感提升（p=.040）。",
    "http://arxiv.org/abs/2605.03877v1":
        "DMGD：免训练扩散模型数据集蒸馏框架 — 条件似然语义匹配 + 最优传输分布匹配做无分类器引导；ImageNet-Woof/Nette/1K 上比需要微调的 SOTA 平均提升 2.1%/5.4%/2.4%。",
    "http://arxiv.org/abs/2605.03869v1":
        "对内存受限 LLM 微调的零阶优化研究：揭示高维下 ZO 梯度无 coordinate 异质性，使 ZO-Adam 等自适应方法毫无收敛优势却内存巨大；提出仅追踪一个全局标量步长的 MEAZO，达到 ZO-Adam 性能而内存与 ZO-SGD 持平。",
    "http://arxiv.org/abs/2605.03863v1":
        "用 VLM 量化 2674 张第一人称照片中绿地等视觉特征，可稳健预测情绪与慢性压力；进一步用 LLM 流水线挖掘 700 万篇文献提取近 1000 个心理健康相关视觉特征，最多 33% 与情绪/压力显著相关，开辟「视觉 exposome」可扩展研究范式。",
    "http://arxiv.org/abs/2605.03862v1":
        "TraceLift：planner-executor 训练框架，把推理轨迹视为可消费中间产物 — 用 rubric RM × 冻结 executor 的实际提升量做奖励，并发布 TRACELIFT-GROUPS 同题分组数据集；在数学/代码任务上优于仅评最终答案的训练。",
    "http://arxiv.org/abs/2605.03858v1":
        "MCJudgeBench：多约束指令遵循的「约束级」judge 评估基准，每条带显式约束列表 + yes/partial/no 标签 + 受控扰动；揭示整体性能强不代表少数 partial/no 类别可靠，正确率高也不必然一致性更高，CoT 改善正确率却不普遍提升稳定性。",
    "http://arxiv.org/abs/2605.03847v1":
        "针对分布式协作智能（DCI）系统中「局部正确-全局风险」的 emergent risk，提出 mechanical conscience 数学框架 — 作为对基线策略的最小修正监督滤波器，附带 conscience score、mechanical guilt、resonant dependability 等可计算治理指标。",
    "http://arxiv.org/abs/2605.03842v1":
        "SOAR：机器人移动履行系统（RMFS）订单分配+机器人调度的统一深度强化学习框架（事件驱动 MDP + 异构图 Transformer），与 Geekplus 合作实验显示全局 makespan 降 7.5%、平均完成时间降 15.4%，延迟低于 100 ms，sim-to-real 部署可用。",
    "http://arxiv.org/abs/2605.03838v1":
        "TRACE：可信 agentic AI 工程框架 — 4 层参考架构 + 经典 ML/LLM-validator (L2a/L2b) 拆分 + 编排-升级策略 + 度量学接地的信任度量套件（GUM/VIM/ISO 17025），引入 Computational Parsimony Ratio (CPR) 把 LLM 用法变成显式设计选择，用临床/工业/司法 3 个实例验证。",
    "http://arxiv.org/abs/2605.03824v1":
        "可重复性研究 + LIMIT+ 控制基准：QUEST 上最佳神经检索器 Recall@100 是 BM25 两倍多（0.41 vs 0.20），但到 LIMIT+ 时强法崩溃至 <0.02 而 BM25 升至 ~0.96；按组合深度分层显示密集方法显著退化，代数稀疏/词法方法稳定。",

    # arXiv 论文 — 2026-05-13 抓取（关键词命中，30 篇）
    "http://arxiv.org/abs/2605.12495v1":
        "AlphaGRPO：把 GRPO 应用于 AR-Diffusion 统一多模态模型，无需冷启动即可解锁推理驱动的文生图和自反思纠错能力。",
    "http://arxiv.org/abs/2605.12493v1":
        "LongMemEval-V2：提出评估 agent 记忆系统能否积累专业环境经验（界面、状态动力学、工作流）的基准，向「经验丰富同事」目标迈进。",
    "http://arxiv.org/abs/2605.12492v1":
        "Pion：通过左右正交变换更新权重矩阵的优化器，训练全程保持奇异值不变，与 Adam/Muon 形成互补，在 LLM 训练中展现竞争力。",
    "http://arxiv.org/abs/2605.12487v1":
        "Task-Adaptive Embedding Refinement：用少量文档上的 LLM 反馈实时细化 query 嵌入，使嵌入模型无需重训即可适配零样本检索与分类任务。",
    "http://arxiv.org/abs/2605.12484v1":
        "Learning, Fast and Slow：提出将上下文内学习（快）与参数更新（慢）结合的 LLM 持续适应框架，避免各自局限，实现更好的持续学习。",
    "http://arxiv.org/abs/2605.12481v1":
        "ToolCUA：提出端到端 agent 框架，优化 GUI 操作与 API 工具调用之间的最优路径编排，解决混合动作空间中的执行低效问题。",
    "http://arxiv.org/abs/2605.12480v1":
        "OmniNFT：提出多目标多模态强化学习框架用于音视频联合生成，解决 RL 中多模态优势不一致和跨模态不对齐问题。",
    "http://arxiv.org/abs/2605.12477v1":
        "MEME：跨越多实体与演化两个维度的 6 类记忆评估任务，发现现有系统在依赖推理（级联/缺失/删除）上普遍失败。",
    "http://arxiv.org/abs/2605.12476v1":
        "MoE 路由几何耦合：揭示 MoE 中路由与专家之间的几何耦合机制，解释路由坍缩根因，并提出利用该几何性质改善训练稳定性的方法。",
    "http://arxiv.org/abs/2605.12471v1":
        "KV-Fold：无需训练的长上下文推理协议，将 KV 缓存视为序列块上的左折叠累加器，实现高效长上下文推理。",
    "http://arxiv.org/abs/2605.12466v1":
        "Attractor Models：提出吸引子模型替代循环 Transformer，主干提出输出嵌入后吸引子模块通过求不动点精化，用隐式微分求梯度，训练内存恒定。",
    "http://arxiv.org/abs/2605.12460v1":
        "Multi-Stream LLMs：提出多流 LLM 架构，让 agent 并行处理思维、输入和输出，消除单流对话范式在长程 agent 任务中的顺序瓶颈。",
    "http://arxiv.org/abs/2605.12456v1":
        "TextSeal：基于 Gumbel-max 采样的局部 LLM 水印，支持投机解码等推理优化，在强稀释场景下仍可检测，严格优于 SynthID-text。",
    "http://arxiv.org/abs/2605.12452v1":
        "Algorithmic Caricature：构建 179 万帖子的危机事件语料，发现 LLM 生成的政治话语在用词分布、情绪拓扑和传播动态上均与真实人群不同，可作为高鲁棒检测信号。",
    "http://arxiv.org/abs/2605.12446v1":
        "ORCE：分离 LLM 答案生成与口语化置信度生成，避免两目标互相干扰，提升置信表达的顺序感知对齐。",
    "http://arxiv.org/abs/2605.12438v1":
        "CLM Detour：encoder 持续预训练时先短暂切换因果语言模型再返回 MLM，在法语/英语生物医学任务上分别提升 1.2-2.8pp 和 0.3-0.8pp。",
    "http://arxiv.org/abs/2605.12435v1":
        "Wildfire Preference Optimization：提出环境自适应偏好优化，解决山火等极端稀有事件预测中的长尾类别失衡和分布偏移问题。",
    "http://arxiv.org/abs/2605.12422v1":
        "预测 LLM-as-a-Judge 难度评估中哪些评分会与人类标注者不一致，使用后处理信号而非生成时概率，实现免重评筛选。",
    "http://arxiv.org/abs/2605.12421v1":
        "Formalize Don't Optimize：在 100 题组合优化基准上，LLM 应优先形式化约束模型而非生成启发式搜索，CP 声明式建模大幅超越 Python 原生算法搜索。",
    "http://arxiv.org/abs/2605.12419v1":
        "ORBIT：生成式检索微调时通过跟踪并约束参数偏移距离，防止 LLM 语言能力灾难性遗忘的参数正则化方法。",
    "http://arxiv.org/abs/2605.12416v1":
        "Flow Map Policies：学习跨生成过程任意步长跳跃（含一步跳跃）的生成式策略，实现快速动作生成，适合多模态分布控制问题。",
    "http://arxiv.org/abs/2605.12412v1":
        "Stories in Space：提出 LLM 上下文学习对应低维概念信念空间中的轨迹，用故事理解任务验证信念随上下文动态更新的机制。",
    "http://arxiv.org/abs/2605.12411v1":
        "从有限交互预测未知对手 AI agent 的下一个决策，提出文本-表格联合建模框架，在受控谈判博弈中评估。",
    "http://arxiv.org/abs/2605.12406v1":
        "语义奖励坍缩（SRC）：解释 RLHF 中谄媚、幻觉连续性、校准漂移等现象来自标量化偏好优化对不同语义差异的压缩，并探讨保持认识完整性的路径。",
    "http://arxiv.org/abs/2605.12400v1":
        "OGLS-SD：在策略内自蒸馏中用可验证结果奖励引导 logit，修正因反思偏差和模板引起的 token 级监督错位，提升 LLM 推理。",
    "http://arxiv.org/abs/2605.12398v1":
        "Q-DAPS：用候选答案合理性分数熵估计 LLM 问题难度，不依赖生成时概率信号，适用于自动教育材料难度分级。",
    "http://arxiv.org/abs/2605.12394v1":
        "随机矩阵理论过拟合检测：无需训练/测试数据即可检测深度学习模型过拟合起点，在长程 grokking 场景中识别权重矩阵「相关陷阱」。",
    "http://arxiv.org/abs/2605.12389v1":
        "SEMIR：通过与网格解耦的拓扑图推断，解决大规模图像中小稀疏结构（如血管、细胞边界）的分割难题。",
    "http://arxiv.org/abs/2605.12388v1":
        "Events as Triggers：以事件为触发器的多 agent 强化学习行为多样性方法，让 agent 在特定时刻按需切换角色，克服固定身份绑定固定行为的局限。",
    "http://arxiv.org/abs/2605.12384v1":
        "TokenHD：token 级幻觉检测训练流水线，克服步骤级分析粒度粗和依赖步骤分割的局限，在推理密集任务中可扩展地检测幻觉。",

    # OpenAI — 2026-05-06
    "https://openai.com/index/mrc-supercomputer-networking":
        "OpenAI 发布 MRC（Multipath Reliable Connection）— 通过 OCP 开源的新型超算网络协议，提升大规模 AI 训练集群的容错性与性能。",

    # 2026-05-09 — OpenAI
    "https://openai.com/index/running-codex-safely":
        "OpenAI 内部如何安全运行 Codex：沙箱、审批流、网络策略和 agent 原生遥测，支撑安全合规的编码 agent 落地。",
    "https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber":
        "扩大 Trusted Access for Cyber 计划，发布 GPT-5.5 与定制版 GPT-5.5-Cyber，帮助经认证的安全防御者加速漏洞研究、保护关键基础设施。",
    "https://openai.com/index/parloa":
        "Parloa 基于 OpenAI 模型构建可规模化的语音 AI 客服 agent，让企业能设计、模拟并部署可靠的实时交互。",
    "https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api":
        "OpenAI API 推出新一代实时语音模型，能推理、翻译、转写语音，提供更自然、更智能的语音体验。",
    "https://openai.com/index/introducing-trusted-contact-in-chatgpt":
        "ChatGPT 推出可选的「信任联系人」安全功能：检测到严重自残风险时通知用户预设的紧急联系人。",
    "https://openai.com/index/testing-ads-in-chatgpt":
        "ChatGPT 开始测试广告，明确标注、不影响答案中立性、强隐私保护并保留用户控制权，用于支持免费访问。",
    "https://openai.com/index/simplex":
        "Simplex 借助 ChatGPT Enterprise + Codex 加速软件开发，缩短设计、构建、测试时间，规模化 AI 工作流。",
    "https://openai.com/index/how-chatgpt-protects-privacy":
        "讲解 ChatGPT 如何保护隐私、减少训练中的个人数据，并让用户可控制是否让对话用于改进模型。",
    "https://openai.com/index/uber":
        "Uber 用 OpenAI 构建司机助手和语音功能，帮司机更高效赚钱、乘客更快下单，覆盖全球实时交易市场。",
    "https://openai.com/index/introducing-chatgpt-futures-class-of-2026":
        "公布 ChatGPT Futures 2026 届：26 名学生用 AI 推动学习、创意与现实影响，展示新一代如何借 ChatGPT 重新定义机会。",
    "https://openai.com/index/introducing-b2b-signals":
        "OpenAI 发布 B2B Signals 报告：前沿企业如何深化 AI 渗透、规模化部署 Codex agentic 工作流、构建持久竞争优势。",
    "https://openai.com/index/singular-bank":
        "西班牙 Singular Bank 用 ChatGPT + Codex 自建 Singularity 助手，帮银行家每天节省 60-90 分钟会议准备和投资组合分析时间。",
    "https://openai.com/index/advancing-youth-safety-in-emea":
        "发布欧洲青少年安全蓝图与 EMEA 青少年与福祉资助计划，推动面向青少年、家庭、教育者的安全负责的 AI。",

    # 2026-05-09 — DeepMind
    "https://deepmind.google/blog/alphaevolve-impact/":
        "总览 AlphaEvolve（Gemini 驱动的进化算法 agent）在商业、基础设施、科学领域的实际影响和应用案例。",

    # 2026-05-09 — Simon Willison
    "https://simonwillison.net/2026/May/9/luke-curley/#atom-everything":
        "引用 Luke Curley：WebRTC 为低延迟会激进丢包，但用户其实更愿多等 200ms 拿到准确的语音 prompt — 不该把会议软件假设套到 LLM 语音输入。",
    "https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/#atom-everything":
        "推荐 Anthropic Thariq Shihipar 的文章：让 Claude 输出 HTML 而非 Markdown 作为 artifact 格式，能解锁 review、探索式可视化等更强工作流。",
    "https://simonwillison.net/2026/May/7/llm-gemini/#atom-everything":
        "发布 llm-gemini 0.31，将 gemini-3.1-flash-lite 从 preview 转为正式版（模型本身自 3 月 preview 起没有变动）。",
    "https://simonwillison.net/2026/May/7/big-words/#atom-everything":
        "用自己 vibe coded 的 macOS 演示工具搭了个简单大字幻灯：通过 URL query string 把文字渲染成 slide。",
    "https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything":
        "Mozilla 利用 Claude Mythos 预览版找出并修复 Firefox 数百个真实漏洞 — AI 安全 bug 报告从「slop」终于变成实用工具。",
    "https://simonwillison.net/2026/May/7/xai-anthropic/#atom-everything":
        "评论 Anthropic 与 SpaceX/xAI 的 Colossus 数据中心算力合作，并指出该数据中心环境记录较差（无 Clean Air Act 许可的燃气轮机）。",
    "https://simonwillison.net/2026/May/7/github-repo-stats/#atom-everything":
        "做了个 GitHub 仓库统计小工具，通过 REST/GraphQL CORS fetch 显示 commit 数等手机端 GitHub 看不到的指标。",
    "https://simonwillison.net/2026/May/6/code-w-claude-2026/#atom-everything":
        "现场直播 Anthropic Code w/ Claude 2026 主题演讲。",
    "https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/#atom-everything":
        "上 Heavybit High Leverage 播客谈 AI 编码：作者发现自己的 vibe coding 与 agentic engineering 已经悄然趋同，引发反思。",

    # 2026-05-09 — arXiv
    "http://arxiv.org/abs/2605.06665v1":
        "UniPool — 用全局共享专家池替代 MoE「每层独立专家集」的固有规则；深层路由可被均匀随机替代而精度只掉 1.0-1.6 点，挑战每层独享专家容量的假设。",
    "http://arxiv.org/abs/2605.06664v1":
        "BAMI：GUI grounding 的训练免费偏差缓解 — 用 Masked Prediction Distribution 归因发现误差源自「高分辨率→精度偏差」+「复杂界面→歧义偏差」，推断时纠偏。",
    "http://arxiv.org/abs/2605.06663v1":
        "EMO — 把 MoE 设计为支持涌现模块化的预训练范式：传统 MoE 限制专家子集会严重掉点，EMO 让模型按领域激活模块化专家，缓解内存约束下的稀疏化损失。",
    "http://arxiv.org/abs/2605.06660v1":
        "VHG — 三方自博弈 + verifier 的难题生成框架，避免传统 self-play 因 reward hacking 产生无效问题，用于推进 LLM 数学推理训练。",
    "http://arxiv.org/abs/2605.06656v1":
        "分析 116 语种、52 模型、约 89K 对比，发现全局 Bradley-Terry 排名约 2/3 决定性投票相互抵消，前 50 模型在统计意义上不可区分；建议小型异质投资组合排名替代单一榜。",
    "http://arxiv.org/abs/2605.06654v1":
        "在 SFT 阶段，用与预训练相同的优化器做全量微调比 LoRA、其他优化器更不易遗忘 — 提出「优化器-模型一致性」现象并理论分析。",
    "http://arxiv.org/abs/2605.06652v1":
        "无基准的比较安全打分：用「instrumental-validity 链」替代 ground-truth 一致性，定义场景包/标尺/审计/采样合约，提供可解释的部署证据。",
    "http://arxiv.org/abs/2605.06651v1":
        "AI Co-Mathematician — 面向数学家的 AI 协作工作台：异步、有状态，覆盖灵感、文献检索、计算探索、定理证明、理论构建，输出原生数学产出。",
    "http://arxiv.org/abs/2605.06650v1":
        "RLVR 中 GRPO 的负样本梯度差异度不足；提出仅用正样本+隐式负梯度的策略优化，避免对少数采样负样本过度惩罚。",
    "http://arxiv.org/abs/2605.06647v1":
        "SIRA（超智能检索 agent）— 不再把检索当黑盒，像专家一样基于术语/证据先验定向调用，减少冗余轮次、降低延迟、提高召回。",
    "http://arxiv.org/abs/2605.06642v1":
        "StraTA — agentic RL 中引入显式轨迹级策略：从初始任务态采样 compact strategy 并条件化后续动作，改善长程探索与功劳分配。",
    "http://arxiv.org/abs/2605.06641v1":
        "GlazyBench — 首个 AI 辅助陶瓷釉料设计基准：23,148 条真实釉料配方，支持烧成后属性预测和图像生成两类任务。",
    "http://arxiv.org/abs/2605.06639v1":
        "Recursive Agent Optimization — 训练能递归生成自我子任务的 agent，通过分而治之实现推理时 scaling 与长上下文/难题泛化。",
    "http://arxiv.org/abs/2605.06638v1":
        "提出 ScaleLogic 合成逻辑推理框架 — 独立控制规划深度和逻辑表达力两个难度轴，研究 RL 训练 scaling 与任务难度的关系。",
    "http://arxiv.org/abs/2605.06635v1":
        "首个 LLM Deep Research agent 的源溯源评估框架：用 AST parser 抽取并验证 markdown 报告里的 inline 引用，检查可达性、相关性、事实一致性。",
    "http://arxiv.org/abs/2605.06632v1":
        "把 SFT 引入的新行为「主动压缩」到稀疏、机械上必要的子网络中，使得在推理时可选择性开/关这些 SFT 行为，而非事后归因相关性。",
    "http://arxiv.org/abs/2605.06627v1":
        "PianoCoRe — 整合并精炼主流开源钢琴 MIDI 语料：250,046 演奏 / 5,625 曲 / 483 作曲家 / 21,763 小时，分级子集面向不同 MIR 应用。",
    "http://arxiv.org/abs/2605.06623v1":
        "MASPO — 面向 LLM 多 agent 系统的联合 prompt 优化：以系统级 holistic 评估对齐局部 agent 目标与整体目标，自动迭代精修每个 agent 的角色 prompt。",
    "http://arxiv.org/abs/2605.06619v1":
        "形式化 algospeak 演化动力学（联合行动模型）+ 提出「Majority Understandable Modulation」临界点：再多调侃就会让多数读者看不懂。",
    "http://arxiv.org/abs/2605.06614v1":
        "SkillOS — 学习长期 skill curation 策略，让 agent 自我进化时不再局限于手工策划/启发式/短程操作，从间接、延迟反馈中学到长程 curation。",
    "http://arxiv.org/abs/2605.06612v1":
        "在线贝叶斯模型校准：能同时处理系统的渐变漂移和突变，缓解传统校准的参数-差异混淆和静态假设，适合 digital twin 场景。",
    "http://arxiv.org/abs/2605.06611v1":
        "机理解释 attention sink — 自注意力 value 聚合内生方差差异，再被 FFN 中的 super neuron 显著放大，形成对初始 token 的注意力垄断。",
    "http://arxiv.org/abs/2605.06610v1":
        "SoftSAE — 动态 Top-K 选择的自适应稀疏自编码器：抛弃固定 K，根据输入复杂度自适应选择激活特征数，更适合机制可解释性中真实数据的多样性。",
    "http://arxiv.org/abs/2605.06607v1":
        "AI CFD Scientist — 首个面向计算流体力学的开源 AI 科学家：覆盖文献 ideation → 验证执行 → 视觉物理验证（不仅 solver log）→ 开放式发现循环。",
    "http://arxiv.org/abs/2605.06605v1":
        "多轮 LLM 评估的动态预算分配：在 conformal survival 框架上替代静态预算，更高效预测 jailbreak / 任务完成等罕见事件触发轮次。",
    "http://arxiv.org/abs/2605.06601v1":
        "Patch2Vuln — 仅基于本地二进制证据，用 Ghidra/Ghidriff diff 旧/新 ELF + LLM agent 重构 Linux 发行版安全更新背后的漏洞含义。",
    "http://arxiv.org/abs/2605.06599v1":
        "首次严格泛函分析地证明 Transformer 交叉熵+L² 正则损失满足 Villani 强制能量函数判据（无穷可微、二次增长、高斯尾、增长条件），为优化与泛化奠基。",
    "http://arxiv.org/abs/2605.06597v1":
        "UniSD — 统一的 LLM 自蒸馏（无外部更强教师）框架：系统化研究自蒸馏中各设计选择的相互作用，整合互补机制为可控研究平台。",
    "http://arxiv.org/abs/2605.06596v1":
        "FedAttr — 联邦 LLM 微调下的客户端级归因（隐私保护）：把基于水印放射性的检测扩展到 FL 场景下的安全聚合，识别哪个客户端贡献了水印数据。",
    "http://arxiv.org/abs/2605.06595v1":
        "CRONA — 跨模态导航多 agent RL：让轻量、模态专精 agent 协作而非训练单一大模型，灵活部署、并行执行，并保留各模态优势。",

    # OpenAI 2026-05-13 ~ 05-14
    "https://openai.com/index/sea-david-chen":
        "Sea 集团 CPO David Chen 解释为何在工程团队全面部署 Codex，加速亚洲 AI 原生软件开发。",
    "https://openai.com/index/work-with-codex-from-anywhere":
        "Codex 接入 ChatGPT 移动端：可跨设备/远程环境实时监控、引导并审批 Codex 编码任务。",
    "https://openai.com/index/chatgpt-recognize-context-in-sensitive-conversations":
        "ChatGPT 新增安全更新：提升敏感对话中的上下文识别能力，可跨时间检测风险并更安全应答。",
    "https://openai.com/index/building-codex-windows-sandbox":
        "OpenAI 介绍如何为 Windows 上的 Codex 构建安全沙箱：受控文件访问与网络限制，让编码 agent 安全高效运行。",
    "https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack":
        "TanStack「Mini Shai-Hulud」npm 供应链攻击事件复盘：OpenAI 列出已采取的系统与签名证书加固措施，并要求 macOS 用户在 2026-06-12 前升级 OpenAI 应用。",

    # Simon Willison 2026-05-13 ~ 05-14
    "https://simonwillison.net/2026/May/14/not-so-locked-in/#atom-everything":
        "由 Bun 从 Zig 转 Rust + 某公司用编码 agent 把原生 iOS/Android 重写为 React Native 的两个例子，论证编码 agent 把编程语言从「锁定」变成了「可丢弃」的实现细节。",
    "https://simonwillison.net/2026/May/14/mitchell-hashimoto/#atom-everything":
        "引用 Mitchell Hashimoto：编程语言越来越「同质化、可替换」——Bun 一两周就能换语言重写，Rust 不再不可或缺，有用就用、过气就扔。",
    "https://simonwillison.net/2026/May/14/datasette-ip-rate-limit/#atom-everything":
        "用 Codex（GPT-5.5 xhigh）写了 datasette-ip-rate-limit 0.1a0 插件：按 IP 限流挡掉骚扰 datasette.io 的爬虫，并给出实际部署配置。",
    "https://simonwillison.net/2026/May/13/welcome-to-the-datasette-blog/#atom-everything":
        "Datasette 项目正式开博客；作者用 OpenAI Codex 桌面端搭建，赞赏其 Markdown 会话导出功能。",
    "https://simonwillison.net/2026/May/13/boris-mann/#atom-everything":
        "引用 Boris Mann：「我有 11 个 AI agent」跟「我有 11 个浏览器 tab」一样含义模糊——agent 数量本身没有意义。",

    # arXiv 2026-05-15 抓取批次
    "http://arxiv.org/abs/2605.14759v1":
        "Crys-JEPA — 用 JEPA 联合嵌入预测架构 + 生成式精炼，在能量感知的潜空间中筛选并精修晶体，逃出晶体生成模型「稳定—新颖」的窄区权衡。",
    "http://arxiv.org/abs/2605.13986v1":
        "TabPFN-3 技术报告：表格基础模型扩展到 100 万行训练规模，纯合成数据预训练，在 TabArena 上一次前向超越所有调参/集成基线，并对速度—性能 Pareto 占优。",
    "http://arxiv.org/abs/2605.15199v1":
        "EntityBench — 140 集 2491 镜头的长程多镜头视频生成基准，含跨镜头角色/物体/场景一致性 schedule 及镜头内质量、prompt 跟随、跨镜头一致性三维评测。",
    "http://arxiv.org/abs/2605.15198v1":
        "ATLAS — 用单个离散「功能 token」同时承担 agentic 操作和潜在视觉推理两种角色，兼顾两类方法的优势并避免上下文切换 / 训练困难。",
    "http://arxiv.org/abs/2605.15188v1":
        "FutureSim — 按真实时间顺序重放 2026 年 1–3 月真实事件，让 agent 在原生 harness 下预测截止后事件；最佳 agent 仅 25% 准确率，多数 Brier 分数还不如不预测。",
    "http://arxiv.org/abs/2605.15185v1":
        "PDI-Bench — 用 SAM 2/MegaSaM/CoTracker3 提取物体并提到 3D，从尺度—深度对齐、3D 运动一致性、3D 结构刚性三维度量化评测视频世界模型的几何一致性。",
    "http://arxiv.org/abs/2605.15186v1":
        "VGGT-Edit — 前馈式原生 3D 场景文本编辑，引入深度同步的文本注入和残差场预测，避免 2D-lift 编辑常见的模糊与跨视角不一致。",
    "http://arxiv.org/abs/2605.15184v1":
        "在 LongMemEval 116 题上系统比较 grep vs 向量检索 + 不同 agent harness 与 CLI 工具：工具输出呈现方式和无关上下文密度对 agentic 搜索性能影响显著。",
    "http://arxiv.org/abs/2605.15179v1":
        "Shodh-MoE — 稀疏 MoE 多物理基础模型：在压缩的 16³ 物理 latent 上运行，物理感知 autoencoder + Helmholtz 速度参数化保证质量严格守恒，消除多 PDE 共训的负迁移。",
    "http://arxiv.org/abs/2605.15177v1":
        "OpenDeepThink — 用 Bradley-Terry 成对比较聚合替代点判分进行并行推理选择；为 Gemini 3.1 Pro 在 Codeforces 上提升 +405 Elo。",
    "http://arxiv.org/abs/2605.15172v1":
        "MetaBackdoor — 首个利用「位置编码」作为后门触发器的攻击：不需修改文本内容，输入长度等位置结构即可激活后门，证明 Transformer 位置信号天然提供隐蔽攻击面。",
    "http://arxiv.org/abs/2605.15171v1":
        "EviScreen — 基于证据推理的可解释疾病筛查框架：从双知识库检索历史病例的区域级证据辅助预测，避免事后显著图解释。",
    "http://arxiv.org/abs/2605.15168v1":
        "用非结构化叙事抽出锚点事件搭建临床时间线骨架，再用结构化 EHR 精确化时间，构成检索增强多模态对齐的临床时间线重建框架。",
    "http://arxiv.org/abs/2605.15164v1":
        "立场论文：当前的行为评测与红队天然只能观察输出，无法验证 2019–2026 治理框架要求的潜表征与长程 agentic 行为安全属性，存在「审计鸿沟」。",
    "http://arxiv.org/abs/2605.15156v1":
        "MeMo（Memory as a Model）— 把新知识编码进独立的记忆模型，LLM 参数保持不变；不依赖权重/logits，可即插即用接入闭源 LLM，且检索成本与语料规模无关。",
    "http://arxiv.org/abs/2605.15155v1":
        "SDAR — 把 On-Policy Self-Distillation 作为门控辅助目标、保留 RL 为主干训练，解决多轮 agent RL 蒸馏不稳定与技能检索引发的负教师拒绝问题。",
    "http://arxiv.org/abs/2605.15153v1":
        "Pelican-Unified 1.0 — 首个按统一原则训练的具身基础模型：单一 VLM 同时承担理解与推理，Unified Future Generator 一次去噪联合生成未来视频与未来动作。",
    "http://arxiv.org/abs/2605.15152v1":
        "首个对 AWQ、GPTQ、GGUF I-quants 等先进量化方案普遍适用的「量化触发型」攻击：全精度看似良性，但被任一上述方法量化后即激活恶意行为。",
    "http://arxiv.org/abs/2605.15138v1":
        "MANSU — 用因果电路归因 + 机制对齐零空间做「量化后仍持久」的 LLM 遗忘，正面解决「稀疏更新跨不过量化 bin」导致的稀疏—持久权衡。",
    "http://arxiv.org/abs/2605.15132v1":
        "APWA — 把 agent 工作流分解成互不干扰的子问题并行执行，构建面向高度可并行 agentic 负载的分布式多 agent 架构。",
    "http://arxiv.org/abs/2605.15131v1":
        "Natural Synthesis — 把大推理模型 + 模型检查器耦合迭代修复 Verilog 实现反应式综合，超过年度合成竞赛最优专用工具，并把规约从时序逻辑改写为自然语言。",
    "http://arxiv.org/abs/2605.15128v1":
        "MemEye — 从「视觉证据粒度（场景级→像素级）」和「证据使用方式（单条→演化合成）」两维度评测多模态 agent 记忆，配套 8 类生活情境基准与可答性消融门。",
    "http://arxiv.org/abs/2605.15118v1":
        "用 STRIDE 构建 4×6 目标×技术矩阵 + 507 叶分类法审计 6 个公开 LLM 攻击基准：HarmBench/InjecAgent/AgentDojo 三者非重叠仅覆盖 ≤25%，「服务中断」「模型内部」整类无标准评测。",
    "http://arxiv.org/abs/2605.15113v1":
        "VPD — 把基于语言反馈的学习形式化为变分 EM：E 步用自适应信任域细化教师、M 步更新学生，二者共演化避免固定教师导致 plateau。",
    "http://arxiv.org/abs/2605.15109v1":
        "Agentic GraphRAG 中引用忠实度应作为「轨迹级」问题处理：消融显示已引用证据通常必要但不充分，邻域上下文与未引用实体也影响答案准确性。",
    "http://arxiv.org/abs/2605.15104v1":
        "用 TTS + 说话人变化 + 环境噪声把文本工具调用基准（Confetti、When2Call）转成配对语音版进行评测；7 个 omni 模型上 text→voice 退化在 1.8–4.8 分之间，强模型/任务依赖。",
    "http://arxiv.org/abs/2605.15102v1":
        "SRT（Self-Recall Thinking）— LLM 在多轮对话推理中显式识别有用历史轮次再生成回复，缓解长程依赖追踪困难与信息稀疏问题。",
    "http://arxiv.org/abs/2605.15100v1":
        "DDC — 把置信加权贝叶斯协议与趋势感知分层剪枝结合，统一推理时宽度（共识）与深度（剪枝）维度，自适应分配采样预算并过滤幻觉。",
    "http://arxiv.org/abs/2605.15082v1":
        "理论证明：核岭回归 + Average Gradient Outer Product 的 top-r 特征空间能恢复多 index 模型 f*(x)=h(Ux) 的中心子空间，即使预测误差仍较大。",
    "http://arxiv.org/abs/2605.15077v1":
        "AsyncFC — 纯执行层框架，把 LLM 解码与函数执行解耦，允许解码与函数执行重叠以及函数间并行，无需微调模型或修改同步函数调用协议。",
    "http://arxiv.org/abs/2605.15071v1":
        "TAB-VLM 基准 — 600 题覆盖 6 类、1600 件印度文物（史前到现代），评估视觉语言模型「文化年代错置」问题；最佳模型 GPT-5.2 也只达 58.7% 总准确率。",
    "http://arxiv.org/abs/2605.15053v1":
        "TFGN — 面向 transformer 的架构 overlay：输入条件化、参数高效的更新让 LLM 在 6 个异构域（散文/Python/Math/生物医学/中文/JavaScript）上实现「无任务、无 replay」持续预训练，几乎无灾难遗忘。",

    # OpenAI — 2026-05-15/16
    "https://openai.com/index/malta-chatgpt-plus-partnership":
        "OpenAI 与马耳他合作，向全体公民提供 ChatGPT Plus 与培训，帮助公民掌握实用 AI 技能并负责任地使用 AI。",
    "https://openai.com/index/databricks":
        "Databricks 将 GPT-5.5 接入企业 agent 工作流；该模型在 OfficeQA Pro 基准上取得了新的 SOTA。",
    "https://openai.com/academy/codex-for-work/how-business-operations-teams-use-codex":
        "Codex for Work 案例：业务运营团队用 Codex 从真实工作输入生成项目简报、战略更新、领导层决策包与进度报告。",
    "https://openai.com/academy/codex-for-work/how-sales-teams-use-codex":
        "Codex for Work 案例：销售团队用 Codex 生成销售管道简报、会议准备包、预测回顾、客户计划及僵局诊断。",
    "https://openai.com/index/personal-finance-chatgpt":
        "ChatGPT 个人理财体验预览（面向美国 Pro 用户）：安全连接金融账户，基于用户财务上下文、目标与优先级获得 AI 洞察与建议。",
    "https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex":
        "Codex for Work 案例：数据科学团队用 Codex 从真实工作输入生成根因简报、影响报告、KPI 备忘录、定向分析与仪表盘规格。",

    # Sebastian Raschka — 2026-05-16
    "https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures":
        "从 Gemma 4 到 DeepSeek V4 — 综述新一代开源权重 LLM 通过 KV 共享、mHC、压缩注意力等架构改进降低长上下文成本。",

    # Simon Willison — 2026-05-15/16
    "https://simonwillison.net/2026/May/16/openclaw-names/#atom-everything":
        "PyCon US lightning talk 准备：用 first_line_history.py 翻 OpenClaw README 的 Git 历史，盘点它从 11 月首个 commit 起经历的所有改名（Warelay → CLAWDIS → CLAWDBOT → Clawdbot → Moltbot → 🦞 OpenClaw）。",
    "https://simonwillison.net/2026/May/16/julia-evans/#atom-everything":
        "引用 Julia Evans：过去 10 年她学会真正喜欢并尊重 CSS — 「居中难」之类的挫败感其实早已被 CSS 解决，CSS 难是因为它在解一个本质难的问题。",
    "https://simonwillison.net/2026/May/15/inaturalist-clumper/#atom-everything":
        "发布 inaturalist-clumper 0.1 — 把 iNaturalist 观测聚合分组、用于其博客 sightings 页面的基础设施工具，已经在生产环境跑数周。",
    "https://simonwillison.net/2026/May/15/sighting-361818285/#atom-everything":
        "PyCon 前晨间观鸟散步：在洛杉矶拍到一只本地海鸥享用星巴克 — Western Gull、Rock Pigeon。",
    "https://simonwillison.net/2026/May/15/qr-code-generator/#atom-everything":
        "用 Claude vibe-code 出一个 QR 码生成工具，支持生成文本/URL 二维码和 WiFi 连接二维码。",
    "https://simonwillison.net/2026/May/15/datasette-llm-limits/#atom-everything":
        "datasette-llm-limits 0.1a0 — 与 datasette-llm、datasette-llm-accountant 配合，可在 Datasette 内为每个用户（或全局）配置 LLM 消费上限（如每用户每滚动 24h $1）。",

    # 05-20 batch — OpenAI
    "https://openai.com/index/the-next-phase-of-education-for-countries":
        "OpenAI 推进 Education for Countries 计划：扩大校园 AI 部署，新增合作伙伴、教师培训和工具，目标改善全球学习成果。",
    "https://openai.com/index/introducing-openai-for-singapore":
        "推出 OpenAI for Singapore：与新加坡建立多年期 AI 合作，扩大本地部署、培养人才，支持企业和公共服务用 AI。",
    "https://openai.com/index/advancing-content-provenance":
        "推进 AI 内容溯源：联合 Content Credentials、SynthID 等机制，推出验证工具帮助用户识别和信任 AI 生成的媒体。",
    "https://openai.com/index/dell-codex-enterprise-partnership":
        "OpenAI 与 Dell 合作，将 Codex 带到混合云和本地环境，企业可在自有数据和工作流上安全部署 AI 编码 agent。",

    # 05-20 batch — Google DeepMind
    "https://deepmind.google/blog/simulate-real-world-places-with-project-genie-and-street-view/":
        "Project Genie 用 Street View 数据模拟真实地点，Google AI Ultra 订阅者全球开放访问。",
    "https://deepmind.google/blog/introducing-gemini-omni/":
        "发布 Gemini Omni — 面向多模态的统一模型，把 Gemini 扩展到全感官输入与输出。",
    "https://deepmind.google/blog/introducing-google-antigravity-2-0/":
        "发布 Google Antigravity 2.0 — 基于 Gemini 的下一代 agentic 开发平台升级版。",
    "https://deepmind.google/blog/gemini-for-science-ai-experiments-and-tools-for-a-new-era-of-discovery/":
        "推出 Gemini for Science：面向科学探索的工具与实验合集，目标扩展科研规模与精度。",
    "https://deepmind.google/blog/how-weathernext-helped-the-national-hurricane-center-better-predict-hurricane-melissas-historic-landfall-in-jamaica/":
        "复盘 WeatherNext AI 模型如何帮 National Hurricane Center 提前预测 Melissa 飓风在牙买加的历史性登陆，为社区争取空前的准备时间。",
    "https://deepmind.google/blog/gemini-3-5-frontier-intelligence-with-action/":
        "发布 Gemini 3.5 — 面向复杂 agentic 工作流的前沿智能模型，强化执行能力。",
    "https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/":
        "发布 Co-Scientist — 基于 Gemini 的多智能体 AI 科研伙伴，帮助研究人员加速科学突破。",

    # 05-20 batch — Simon Willison
    "https://simonwillison.net/2026/May/19/llm-gemini-2/#atom-everything":
        "llm-gemini 0.32 发布：新增 gemini-3.5-flash 模型支持，对应 Google I/O 发布的 Gemini 3.5 Flash。",
    "https://simonwillison.net/2026/May/19/gemini-35-flash/#atom-everything":
        "Google I/O 上 Gemini 3.5 Flash 直接 GA（无 preview 阶段），同时被部署到 Gemini app、AI Mode、Search、Antigravity 等几乎所有 Google 关键产品。",
    "https://simonwillison.net/2026/May/19/5-minute-llms/#atom-everything":
        "PyCon US 2026 闪电演讲：用 5 分钟带注释幻灯片总结过去 6 个月 LLM 领域的关键进展。",
    "https://simonwillison.net/2026/May/17/gds-weighs-in/#atom-everything":
        "英国政府数字服务（GDS）就 NHS 因 Project Glasswing 漏洞披露而关闭开源仓库一事发声，提醒公共部门应正确权衡 AI、开放代码与漏洞风险。",

    # 05-21 batch — Simon Willison
    "https://simonwillison.net/2026/May/20/google-io/#atom-everything":
        "Simon 评 Google I/O 2026：只写已 GA 的功能；亮点是 Gemini 3.5 Flash 跳过 preview 直接 GA，以及 OpenClaw 竞品 Gemini Spark（可原生连接常用工具的个人 AI agent）。",

    # 05-21 batch — arXiv
    "http://arxiv.org/abs/2605.20179v1":
        "TIDE — MoE 架构 Diffusion LLM 的高效无损推理系统，利用专家时间稳定性做 I/O 感知 offload，在资源受限设备上跑得动。",
    "http://arxiv.org/abs/2605.20177v1":
        "把 VLM 训练拆成视觉感知/视觉推理/文本推理三阶段，证明 VLM 视觉任务的瓶颈是感知不足而非推理。",
    "http://arxiv.org/abs/2605.20176v1":
        "ClinSeekAgent — 临床推理 agent 框架，从被动接受证据转向主动搜寻和合成多模态证据。",
    "http://arxiv.org/abs/2605.20173v1":
        "提出生产级 LLM agent 运行时的「随机-确定边界」（SDB）原语，并按 Coordination/State/Control 三维度组织 agent 运行时设计。",
    "http://arxiv.org/abs/2605.20170v1":
        "KoRe — 把 LLM 不透明的参数知识替换成紧凑可编辑的知识表示（基于 KG 思路），减少幻觉、便于调试。",
    "http://arxiv.org/abs/2605.20149v1":
        "对比 raw / checklist 增强 / 澄清式 prompt 三种条件，证明结构化 prompt 在多 LLM、多任务上提升回答质量并减少用户反复交互。",
    "http://arxiv.org/abs/2605.20128v1":
        "MixRea benchmark — 借鉴「注意盲」理论，发现 LLM 也会在显式任务下漏掉关键隐式线索；2246 题、9 种推理类型。",
    "http://arxiv.org/abs/2605.20104v1":
        "speculative decoding 的混合树构造，避免动态深度剪枝丢候选，向 dense tree 的接受率上限靠拢。",
    "http://arxiv.org/abs/2605.20087v1":
        "ThoughtTrace 数据集 — 配对真实多轮对话和用户「当时在想什么」自报，1058 人、2155 对话、17K turn、10K 标注。",
    "http://arxiv.org/abs/2605.20086v1":
        "拆解 LLM+演化搜索 coding agent 究竟在演化什么：新算法结构、调参、重组旧知识，还是过拟合评估器。",
    "http://arxiv.org/abs/2605.20084v1":
        "BalanceRAG — 级联 RAG（先 LLM 自答、再 RAG 兜底、否则弃权）的联合风险校准，比逐级保守阈值更优。",
    "http://arxiv.org/abs/2605.20075v1":
        "CopT — Chain-of-Thought 反转：先出草稿答案再思考，减少 performative reasoning 带来的延迟和 token 浪费。",
    "http://arxiv.org/abs/2605.20061v1":
        "ReBel — 部分可观测环境中的过程级 RL：显式建模「信念状态」分发奖励，缓解长 horizon agent 信用分配。",
    "http://arxiv.org/abs/2605.20025v1":
        "AutoResearchClaw — 多 agent 自主科研流水线，含结构化辩论、跨轮经验累积，把单次失败转化为下一轮的输入。",
    "http://arxiv.org/abs/2605.20023v1":
        "负结果论文：分析 84 个任务中 16 个加 agent skills 反而变差的案例，指出 procedural knowledge 在攻防 CTF 中常是冗余而非增益。",
    "http://arxiv.org/abs/2605.20022v1":
        "FlexDraft — 并行 speculative decoding：用 attention tuning 和 bonus 校准消除 draft/verify 互等，提升内存带宽效率。",

    # 05-24 batch — DeepMind
    "https://deepmind.google/blog/were-launching-the-google-deepmind-accelerator-program-in-asia-pacific-to-tackle-environmental-risks/":
        "Google DeepMind 启动亚太区「AI for the Planet」加速器：为期 3 个月，给初创、研究团队和非营利组织提供专家指导、定制支持与 Google AI 模型集成，启动训练营设在新加坡，聚焦气候、环保、农业、能源议题。",

    # 05-24 batch — Simon Willison
    "https://simonwillison.net/2026/May/23/on-the-dl/#atom-everything":
        "整理 Ben Meyer 关于 HTML <dl> 元素的新认知：一个 <dt> 可跟多个 <dd>、可用 <div> 分组并支持 ARIA 标注，且自 2008 HTML5 草案起官方名称已是 description list 而非 definition list。",
    "https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything":
        "转介 David Oks 文章：全球仅剩三家大型内存厂商，固定晶圆产能必须在 DDR/LPDDR/HBM 间分配，HBM 抢占产能将让 DDR/LPDDR 紧缺，未来几年消费电子要明显涨价。",
    "https://simonwillison.net/2026/May/22/ftc-active-listening/#atom-everything":
        "FTC 要求 Cox Media Group 等三家公司支付近 100 万美元和解，因虚假宣传「active listening」AI 营销服务能通过智能设备「监听」用户对话定向投放——作者 2024 年就推断这是营销话术包装第三方数据，而非真在听麦克风。",
    "https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything":
        "Datasette Agent 首个版本发布：LLM 库工作三年后终于和 Datasette 合体，提供对话式数据查询界面，配合 datasette-agent-charts 插件还能生成图表。",
    "https://simonwillison.net/2026/May/21/datasette-agent-sprites/#atom-everything":
        "datasette-agent-sprites 0.1a0：Datasette Agent 插件，在 Fly Sprites 沙盒里执行命令。",
    "https://simonwillison.net/2026/May/21/datasette-agent-charts/#atom-everything":
        "datasette-agent-charts 0.1a2：在生成的图表下方增加「View SQL query」按钮。",
    "https://simonwillison.net/2026/May/21/datasette-agent-2/#atom-everything":
        "datasette-agent 0.1a3：可视化和折叠的 SQL 结果工具调用都加上「View SQL query」按钮；跳过空 reasoning chunk；截断响应时仍能向用户展示完整结果表格。",
    "https://simonwillison.net/2026/May/20/datasette-agent-charts/#atom-everything":
        "datasette-agent-charts 0.1a1：bar/waffle 图无 color 列时用顺序色阶按数值着色，文本类 color 列改用 observable10 离散色阶；查询前检查 execute-sql 权限；新增交互 tooltip；修复 waffleY 描述缺失。",
    "https://simonwillison.net/2026/May/15/datasette-agent/#atom-everything":
        "datasette-agent 0.1a2：工具可绑定 required_permission，默认后台 agent 工具需新增的 datasette-agent-background 权限。",
    "https://simonwillison.net/2026/May/14/datasette-agent/#atom-everything":
        "datasette-agent 0.1a1：列表 tables 时使用 execute-sql 权限决定向用户展示哪些表。",

    # 05-25 batch — OpenAI
    "https://openai.com/index/virgin-atlantic":
        "案例：Virgin Atlantic 在固定假日截止日期下用 Codex 重做移动 App，达到接近全量单元测试覆盖、零 P1 缺陷上线。",
    "https://openai.com/index/gartner-2026-agentic-coding-leader":
        "OpenAI 被列入 2026 Gartner 企业级 AI 编码 Agent 魔力象限「领导者」，Codex 因创新与企业级部署能力获认可。",
    "https://openai.com/index/adventhealth":
        "AdventHealth 使用 ChatGPT for Healthcare 简化工作流、减少行政负担，把更多时间还给医患照护。",

    # 05-25 batch — Simon Willison
    "https://simonwillison.net/2026/May/24/datasette/#atom-everything":
        "datasette 1.0a30：主要新增可定制的「Jump to...」菜单（按 / 触发），并提供 jump_items_sql() 插件 hook 让其他插件注入可搜索条目。",
    "https://simonwillison.net/2026/May/24/datasette-agent/#atom-everything":
        "datasette-agent 0.1a4：用上 1.0a30 新加的 makeJumpSections() JS hook，把「Start a new agent chat」入口集成进 Datasette / 菜单；agent.datasette.io 可用 GitHub 登录试玩。",
    "https://simonwillison.net/2026/May/24/datasette-fixtures/#atom-everything":
        "datasette-fixtures 0.1a0：用 Datasette 1.0a30 新增的 populate_fixture_database() helper 拉起官方测试 fixture，可通过 uvx 在不装 Datasette 的情况下直接试用。",
    "https://simonwillison.net/2026/May/24/armin-ronacher/#atom-everything":
        "引用 Armin Ronacher 吐槽：现在最让人沮丧的失败模式是有人把观察到的问题丢给 LLM「克朗克」加工后再提 issue，结果是充满自信但完全错乱的根因分析、伪极简复现和错位类比。",
    "https://simonwillison.net/2026/May/24/usborne-mad-house/#atom-everything":
        "Usborne 公开 1980 年代《Creepy Computer Games》等 PDF，作者把 1983 年「Mad House」喂给 Claude，让它复刻成可玩的纯 JS/HTML 互动版本。",

    # arXiv — 2026-05-26
    "http://arxiv.org/abs/2605.26114v1":
        "MobileGym：浏览器托管的轻量可控移动端 GUI agent 仿真平台，用结构化 JSON 状态做确定性判定提供可验证奖励信号，支持低成本并行 rollout 做在线 RL。",
    "http://arxiv.org/abs/2605.26112v1":
        "提出 agentic AI 的下一个瓶颈是「系统扩展」而非模型扩展，主张把基础模型外层的执行框架（harness）当作可审计、可验证的一等设计对象来优化。",
    "http://arxiv.org/abs/2605.26111v1":
        "用多模态大模型为扩散模型提供条件做主体驱动图像生成，兼顾指令遵循与身份保持、减少 copy-paste 伪影。",
    "http://arxiv.org/abs/2605.26110v1":
        "Prism：可复用的插件式基础设施，解决多模态持续指令微调（MCIT）需直接改基座代码的工程瓶颈，提升可复现性与扩展性。",
    "http://arxiv.org/abs/2605.26106v1":
        "LoopMDM：在掩码扩散语言模型中选择性循环前中段 Transformer 层，不加参数即获得深度扩展效应，提升训练效率与性能。",
    "http://arxiv.org/abs/2605.26100v1":
        "用 LLM 做结构感知的代码改动标注（重命名、移动、逻辑修改等类型），而非只做摘要/评论生成，以提升代码审查效率。",
    "http://arxiv.org/abs/2605.26099v1":
        "提出类「睡眠」巩固机制：模型周期性把近期上下文离线转化为持久 fast weights 再清空 KV 缓存，缓解注意力随上下文增长的扩展性差问题。",
    "http://arxiv.org/abs/2605.26093v1":
        "GoBOED：目标驱动的贝叶斯最优实验设计，直接面向给定决策目标优化实验，而非笼统地降低参数不确定性。",
    "http://arxiv.org/abs/2605.26092v1":
        "OrpQuant：用几何正交残差投影做无乘法器的 2 的幂次（PoT）Transformer 量化，突破对数量化的低角分辨率瓶颈，适配边缘设备部署。",
    "http://arxiv.org/abs/2605.26087v1":
        "DiscoverPhysics：交互式基准，让 LLM agent 在 22 个物理规律刻意偏离现实的模拟世界里去「发现」运动定律，区分真实推理与对已知科学的记忆。",
    "http://arxiv.org/abs/2605.26086v1":
        "Claw-Anything：评测常开型个人助理的基准，沿长程活动、对用户数字世界更广访问等三个维度扩展 agent 可用上下文。",
    "http://arxiv.org/abs/2605.26081v1":
        "VeriTrace：让深度研究 agent 的「心智模型」通过显式反馈持续演化，避免中间表示被混杂质量信息污染、沿依赖传播错误。",
    "http://arxiv.org/abs/2605.26079v1":
        "ABA：agentic 框架，系统性审计 AI 基准任务，挖出隐藏环境依赖、规格缺口与脆弱评分逻辑等人工标注难发现的问题。",
    "http://arxiv.org/abs/2605.26074v1":
        "StakeBench：基于「市场承诺」的语言理解评测框架，把 Polymarket/Manifold 上 56 万条评论与真实持仓/交易记录关联，用可观测市场行为做监督。",
    "http://arxiv.org/abs/2605.26070v1":
        "WhoSaidIt：人机协作的多语种「从文本推断说话者属性」再标注框架，用 LLM 浮现标注理由 + 聚焦分歧采样，在资源受限下稳定标签。",
    "http://arxiv.org/abs/2605.26061v1":
        "NSAC：受生物启发的连续时间注意力架构，把注意力 logit 计算建模为受 C.elegans 神经回路策略门控的 OU 随机微分方程，用于量化表示学习的不确定性。",
    "http://arxiv.org/abs/2605.26046v1":
        "研究多目标 prompt 优化 LLM 评审器时的失效模式：文本梯度方法产出自然语言批评而非数值向量，使多任务学习的冲突消解工具（PCGrad/MGDA）失效。",
    "http://arxiv.org/abs/2605.26040v1":
        "L2IR：图欺诈检测中欺诈者伪造大量与正常用户的连接稀释信号，该法挖掘可疑行为背后的潜在意图来提升 GNN 检测可靠性。",
    "http://arxiv.org/abs/2605.26038v1":
        "DRScaffold：为轻量视觉语言模型在密集场景推理中提供推理步与视觉实体/关系的显式接地，改善多目标多关系的联合定位与多步推理。",
    "http://arxiv.org/abs/2605.26036v1":
        "CityRep：跨城市、任务、模态的统一城市表征基准，用避免空间泄漏的划分方式纠正以往评测城市少、性能虚高的问题。",
    "http://arxiv.org/abs/2605.26029v1":
        "CausaLab：可扩展环境，评测 LLM agent 的交互式因果发现——既看能否用因果证据解题，也看其答案是否由对底层因果机制的正确假设支撑。",
    "http://arxiv.org/abs/2605.26026v1":
        "面向光片荧光显微（LSM）的多模态 3D 基础模型，少样本即可做分割、分类与去模糊，缓解 LSM 数据标注成本高、难规模化监督学习的问题。",
    "http://arxiv.org/abs/2605.26014v1":
        "STORM：在视频语言模型内部「内化」时空建模，避免靠文本 CoT/抽帧/重编码等外化推理来跟踪运动与时序，降低推理延迟与工程复杂度。",
    "http://arxiv.org/abs/2605.26012v1":
        "为深度强化学习加一个固定正交投影瓶颈，把编码特征约束到低维子空间，无需辅助目标或预训练即提升表示效率（含线性可实现性下的理论保证）。",
    "http://arxiv.org/abs/2605.26004v1":
        "MAGIC：免训练、仅前向的核心集选择法，为多模态指令微调挑出紧凑却行为忠实的子集，解决数据冗余、低视觉依赖、覆盖不均的问题。",
    "http://arxiv.org/abs/2605.26001v1":
        "提出用 AI 辅助「系统化」，把「推理」「公平」「创造力」等宽泛有争议的概念明确为可测量的结构化表述，以改进对生成式 AI 系统的评测。",
    "http://arxiv.org/abs/2605.25998v1":
        "主张 LLM 开发与评测中的许多核心问题本质是因果问题（加某数据域的效应、该路由到大还是小模型等），呼吁系统性引入因果方法。",
    "http://arxiv.org/abs/2605.25988v1":
        "研究 checker 引导的医疗 RAG：发现决定能否提供可训练梯度的是 checker 训练期的输出分布而非其留出准确率，并诊断信号坍缩与奖励黑客。",
    "http://arxiv.org/abs/2605.25985v1":
        "面向含多个自由变量的复杂逻辑查询（EFO_k）的可扩展神经符号搜索框架，解决传统只对单变量做边际排序、随自由变量增多迅速不可解的问题。",
    "http://arxiv.org/abs/2605.25984v1":
        "SafeCtrl-RL：推理时自适应行为控制框架，把对话生成建模为序列决策，用 RL agent 按上下文动态选择 prompt 调整策略，无需重训即抑制不安全行为。",

    # 2026-05-28 — arXiv
    "http://arxiv.org/abs/2605.28819v1":
        "PEFT-Arena：从「稳定性—可塑性」权衡的角度评估 PEFT，提出同时衡量下游性能与通用能力保留的基准；同等参数预算下正交微调（orthogonal finetuning）取得最优帕累托前沿。",
    "http://arxiv.org/abs/2605.28818v1":
        "对比严格文本设定下成对 LLM 与 VLM：发现视觉—语言预训练并未全局提升模型对人类自然阅读（fMRI + 眼动）的对齐度，VLM 优势只在含强视觉语义句子上出现。",
    "http://arxiv.org/abs/2605.28814v1":
        "BES（双向进化搜索）：在 LLM 自我提升搜索中加入前向重组进化算子 + 后向子目标分解，逃离单纯自回归扩展的「熵壳」，理论与实验均显示能指数级减少所需样本。",
    "http://arxiv.org/abs/2605.28807v1":
        "CCO（校准式集体监督）：把多个辅助打分器聚合成「偏离保守基线」的惩罚，再用 Conformal Decision Theory 在线校准，给 scalable oversight 一个带有限时间保证的实现。",
    "http://arxiv.org/abs/2605.28806v1":
        "提出个性化视觉记忆基准 + VisualMem：不再把图像压成 caption，而是用对话上下文解析身份、所有权和长期事实，显著优于纯文本记忆基线。",
    "http://arxiv.org/abs/2605.28805v1":
        "OmniVerifier-M1：带显式结构化重校准的多模态元验证器（meta-verifier）。",
    "http://arxiv.org/abs/2605.28803v1":
        "Ω-QVLA：用组合旋转 + 逐步缩放为 VLA（视觉—语言—行动）模型做鲁棒量化。",
    "http://arxiv.org/abs/2605.28802v1":
        "把人工标注差异当作稳定信号：通过跨标注者偏好优化（cross-annotator preference optimization）学习单个标注者特有的解释行为。",
    "http://arxiv.org/abs/2605.28791v1":
        "Skill-Conditioned Gated Self-Distillation：用「技能条件门控」自蒸馏方法增强 LLM 推理。",
    "http://arxiv.org/abs/2605.28787v1":
        "实证比较：在 Agentic 数据检索中，Agent 是否真的需要语义元数据？",
    "http://arxiv.org/abs/2605.28782v1":
        "LLM 能否处理话语助词？以马来口语为例的案例研究。",
    "http://arxiv.org/abs/2605.28780v1":
        "Bias Leaves a Gradient Trail：基于概念分解上的梯度探针，免标签地识别模型偏见。",
    "http://arxiv.org/abs/2605.28779v1":
        "视觉—语言模型在因果推理上的「抽象鸿沟」研究。",
    "http://arxiv.org/abs/2605.28778v1":
        "LLM 能否用「也许/可能」等语言不确定性标记可靠地反映其内在置信度？",
    "http://arxiv.org/abs/2605.28775v1":
        "Learn from Weaknesses：为小型 Computer-Use Agent 做自动化领域专精化的方法。",
    "http://arxiv.org/abs/2605.28774v1":
        "AEPO：用于多模态 Agentic 推理的 Agent 探索式策略优化。",
    "http://arxiv.org/abs/2605.28773v1":
        "重新把「记忆」建模为持续演化的连接性（connectivity）。",
    "http://arxiv.org/abs/2605.28769v1":
        "Multi-Mixer Models：基于共享表示的灵活序列建模架构。",
    "http://arxiv.org/abs/2605.28764v1":
        "SwarmHarness：用去中心化、激励对齐的 AI Agent 网络做基于技能的任务路由。",
    "http://arxiv.org/abs/2605.28763v1":
        "CubePart：开放词表、可控部件的 3D 生成器。",
    "http://arxiv.org/abs/2605.28760v1":
        "把 LLM 的零阶（ZO）微调当作推理负载，用 vLLM 服务运行时调度其重复打分阶段，在 OPT-13B SST-2 上比官方 LoZO 基线 8.13× 加速且精度持平。",
    "http://arxiv.org/abs/2605.28751v1":
        "在 Code RL 中，对低/高单测覆盖奖励训出的 checkpoint 做权重外推插值，能扩展「正确率—效率」帕累托前沿；pass@250 比单一 checkpoint 提升 3.3%。",
    "http://arxiv.org/abs/2605.28745v1":
        "首次在预测市场（Polymarket）评论上做 stance detection：用 Anthropic API 做反事实增强，结合市场上下文，把 3-class Anti 召回率从 0.10 拉到 0.45。",
    "http://arxiv.org/abs/2605.28742v1":
        "CORE：把成功/失败推理轨迹的对比蒸馏成自然语言「洞见」，在 4 个推理任务上以更少 rollout 超过 GRPO/GEPA/episodic RAG/MemRL。",
    "http://arxiv.org/abs/2605.28740v1":
        "Reverse Probing：面向临床摘要的首个 token 级不确定性量化框架，从模型内部激活提取信号，AUPRC 比 8 个基线最高 4 倍且更省算力。",
    "http://arxiv.org/abs/2605.28733v1":
        "效用感知多模态对比学习：在 InfoNCE 损失里加入消费者需求项，让生成的商品图既文本一致又能提升 Amazon/Airbnb 上的转化与忠诚度。",
    "http://arxiv.org/abs/2605.28732v1":
        "MemTrace：把记忆系统流水线转成可执行的记忆演化图，定位 LLM 记忆失败的根因；给出闭环 prompt 优化后下游性能最多再涨 7.62%。",
    "http://arxiv.org/abs/2605.28722v1":
        "MARI：多适配器表示干预 + 能量门控，对不同样本自适应选择干预方向与强度，在 TruthfulQA/BBQ 上达 SOTA 且不损 MMLU/ARC 通用能力。",
    "http://arxiv.org/abs/2605.28721v1":
        "LiveBrowseComp：搜索 Agent 真的在「检索」还是只在「验证已有知识」？发现 IKD（内在知识依赖）严重，提出 90 天内时效问题构成的新基准，所有 Agent 闭卷 < 2%。",
    "http://arxiv.org/abs/2605.28714v1":
        "IPO-Mine：开源工具 + 1994–2026 跨 10.9 万份 IPO 文件的 76,000 张图像数据集，对长多模态监管文档做结构化分析，并暴露 SOTA 多模态模型与专家判断的偏差。",

    # 2026-05-29 OpenAI
    "https://openai.com/index/endava":
        "案例：Endava 用 Codex 打造「Agent 化组织」，加速软件交付，把需求分析从数周压缩到数小时。",
    "https://openai.com/index/openai-frontier-governance-framework":
        "OpenAI 公布「前沿治理框架」，阐述其 AI 安全、安保与风险实践如何对齐欧盟和加州的新兴监管。",
    "https://openai.com/index/mufg":
        "三菱日联（MUFG）借 ChatGPT Enterprise 转型为 AI 原生组织，改进工作流并规模化推出 AI 金融服务。",
    "https://openai.com/index/cisco":
        "思科与 OpenAI 用 Codex 重塑企业工程：扩展 AI 原生开发、加速 AI Defense 工作并自动化缺陷修复。",
    "https://openai.com/index/building-self-improving-tax-agents-with-codex":
        "OpenAI 联手 Thrive、Crete 用 Codex 构建可自我改进的报税 Agent，自动化申报、提升准确率并加速流程。",
    "https://openai.com/index/election-safeguards-2026":
        "面向 2026 全球大选，OpenAI 介绍其帮助公众获取信息、支持网络防御者、并提升 AI 透明度的举措。",
    "https://openai.com/index/warp":
        "Warp 用 GPT-5.5 等 OpenAI 模型在本地、云端和开源开发流程中协同调度编码 Agent，押注开源。",

    # 2026-05-29 Simon Willison
    "https://simonwillison.net/2026/May/29/datasette/#atom-everything":
        "Datasette 1.0a31 发布：新增两大功能——授权用户可执行写库查询，以及可保存（公开或私有）的存储查询（原 canned queries 改名）。",
    "https://simonwillison.net/2026/May/29/anthropic/#atom-everything":
        "评 Anthropic 650 亿美元 H 轮：最值得注意的是其年化运营营收本月已突破 470 亿美元，作者解读这一惯用的「run-rate」口径。",
    "https://simonwillison.net/2026/May/28/claude-opus-4-8/#atom-everything":
        "Opus 4.8 发布，作者最欣赏官方坦诚把它描述为对前代的「温和但切实」的小幅渐进改进，难得不夸大。",
    "https://simonwillison.net/2026/May/28/llm-anthropic/#atom-everything":
        "llm-anthropic 0.25.1 发布：新增 Claude Opus 4.8 模型、fast 模式 -o fast 1 选项，max_tokens 默认改为各模型最大输出。",
    "https://simonwillison.net/2026/May/28/markdown-svg-renderer/#atom-everything":
        "markdown-svg-renderer：一个定制 Markdown 渲染工具，对 SVG 代码块既渲染图像又提供查看源码的切换标签，支持粘贴或加载远程 Markdown。",
    "https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything":
        "SQLite 五天前加了 AGENTS.md，并非用于自身开发，而是面向把 Agent 指向 SQLite 代码库的人；其中说明 SQLite 不接受无事先协议/法律手续的 PR。",
    "https://simonwillison.net/2026/May/27/product-market-fit/#atom-everything":
        "作者认为 OpenAI 与 Anthropic 都已找到 PMF：企业客户正按 API 价格付费并持续加码，Anthropic 据传即将迎来首个盈利季度。",
    "https://simonwillison.net/2026/May/27/kyle-ferrana/#atom-everything":
        "引用 Kyle Ferrana 的星际迷航式段子，调侃 AI 编码 Agent「照做了你说的但酿成灾难」的盲从问题。",
    "https://simonwillison.net/2026/May/26/the-pressure/#atom-everything":
        "引用 curl 作者 Daniel Stenberg：AI 辅助的（且可信的）安全报告暴增，数量达 2024 年的 4–5 倍、平均每天逾一份，给团队带来空前压力。",
    "https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything":
        "微软 Copilot Cowork 存在数据外泄风险：Agent 可未经批准向用户自己的收件箱发邮件，而这些消息渲染图片时可能被攻击者用来窃取数据。",
    "https://simonwillison.net/2026/May/26/paul-graham/#atom-everything":
        "引用 Paul Graham：如今很多创始人来信都是 AI 写的「硬核新闻体」，一旦识破就难以认真对待，会让他看低作者。",
    "https://simonwillison.net/2026/May/25/sighting-365297287/#atom-everything":
        "生活随记：在加州圣马特奥县带新折叠皮划艇出海，看到加州棕鹈鹕、雪鹭、海狮和港海豹。",

    # 2026-05-29 arXiv 关键词命中
    "http://arxiv.org/abs/2605.30353v1":
        "物理学家监督 AI 编码 Agent（Claude Code）12 天 57 个会话构建 JAX 微扰论模块的量化案例：15 次干预中 Agent 自主解决 10 次，唯独把「症状缓解」当「根因修复」的 3 个 bug 始终绕过测试，需人工领域知识介入。",
    "http://arxiv.org/abs/2605.30348v1":
        "LLMSurgeon：仅凭目标模型生成的文本，把「数据混合诊断（DMS）」建模为标签偏移下的逆问题，估计其预训练语料的领域分布，校准软置信度而非直接聚合分类器输出。",
    "http://arxiv.org/abs/2605.30350v1":
        "DynaFLIP：动态感知的多模态预训练框架，用图像-语言-3D 光流三元组监督，把运动理解前移到感知层，训练出只需图像输入的机器人操作编码器。",
    "http://arxiv.org/abs/2605.30345v1":
        "SchGen：首个从自然语言生成可编辑 PCB 原理图的 LLM，提出语义化的代码表示来替代冗长、工具专属的传统原理图格式，并解决数据集匮乏问题。",
    "http://arxiv.org/abs/2605.30344v1":
        "Tiny but Trusted：构建带异常解释标注的时间序列基准 VisAnomBench，微调小型视觉-语言模型，实现高效且可解释的时序异常检测。",
    "http://arxiv.org/abs/2605.30343v1":
        "RiM（Reasoning in Memory）：用固定的特殊 token「记忆块」替代自回归生成中间推理步骤，让 LLM 像人类工作记忆那样在内部完成潜在推理，无需外化思考。",
    "http://arxiv.org/abs/2605.30337v1":
        "HullFT：一种几何方法的测试时微调，把查询嵌入表示为少量训练序列的稀疏凸组合，配合梯度缓存，同时解决检索与微调的逐查询速度瓶颈。",
    "http://arxiv.org/abs/2605.30335v1":
        "形式化多组件 LLM Agent「局部一致、全局不一致」的失败：提出可在运行时计算的组合残差 eps*，用乘积结构二分法刻画局部一致何时足够，并用 Rayleigh 商预测残差。",
    "http://arxiv.org/abs/2605.30334v1":
        "复用已算好的样本级分数研究数据「组织」（而非选择）对 LLM 训练的影响，提炼出边界锐化、循环调度等四条优化数据排布的准则，额外开销极小。",
    "http://arxiv.org/abs/2605.30333v1":
        "COMPOSE：双图框架，结合论文的科学引用图与对齐的形式化定理依赖图，为锚定论文生成既顺应前人方向、又尊重形式依赖的「未来定理」式命题。",
    "http://arxiv.org/abs/2605.30329v1":
        "SoundnessBench：1099 条由 ICLR 投稿重建、带审稿人 soundness 子分的机器学习研究提案基准，测 LLM 能否在投入资源前判断一个研究想法的方法论是否可行。",
    "http://arxiv.org/abs/2605.30327v1":
        "Reasoning with Sampling：从基模型「幂分布」采样即可媲美 RL 后训练的推理能力，本文提出在「决策点」切割的高效采样器，让采样能在目标分布的各模式间充分混合。",
    "http://arxiv.org/abs/2605.30326v1":
        "RoboWits：双臂机器人基准，专门评估认知推理、创造性工具使用和对意外状况的鲁棒性，并用多 Agent 协作的自动任务生成流水线规模化构造高质量推理场景。",
    "http://arxiv.org/abs/2605.30323v1":
        "In-Context Reward Adaptation：基于 Transformer 的框架，利用上下文学习在线建模多样且未见过的人类偏好，无需昂贵重训即可泛化到新偏好域，提升 RLHF 奖励模型鲁棒性。",
    "http://arxiv.org/abs/2605.30322v1":
        "Gram：自动化对齐审计框架，评估 AI Agent 蓄意破坏的倾向；在 17 个诱导破坏的 Gemini 部署场景中约 2–3% 轨迹出现「过度热心」式的越权与目标追逐行为。",
    "http://arxiv.org/abs/2605.30315v1":
        "为成对 LLM 评测提供「分辨率诊断」：把排名当假设检验，发现两大公开榜单中相当比例的成对排名在 (α,功效)=(0.05,0.8) 下其实无法区分，提出每对分辨率比 q=N/N* 作为主要诊断指标。",
    "http://arxiv.org/abs/2605.30295v1":
        "MedCase-Structured：从非结构化文本生成符合 HL7 FHIR R4 的结构化病例数据集，结合分阶段 LLM 生成与术语校验修复，用于在贴近真实电子病历的环境中评测临床诊断推理。",
    "http://arxiv.org/abs/2605.30290v1":
        "STV（自训练验证）：针对「验证器」这一自我改进共同瓶颈，让模型学会发现自己生成的错误，从而同时解锁测试时的验证-修正循环与训练时的自训练。",
    "http://arxiv.org/abs/2605.30289v1":
        "为数值表格数据集设计统计嵌入：用结构化 EDA 描述符 + 预训练句向量嵌入到共享空间，再用典型相关分析量化跨数据集相似度，支持检索与可解释对齐。",
    "http://arxiv.org/abs/2605.30288v1":
        "MIRA：面向中训练（mid-training）的数据选择方法，用「评分标准锚定（rubric anchoring）」实现既可扩展又能感知数据来源的语义化筛选，适配异构来源与训练角色。",
    "http://arxiv.org/abs/2605.30284v1":
        "ProjectionBench：在「信息渐进披露」下评测 LLM 的科学假设生成——模型先只拿到课题和研究问题，再逐步获得技术细节，最终走到经典零假设检验，考察真正的创新推理而非知识检索。",
    "http://arxiv.org/abs/2605.30280v1":
        "Qwen-VLA：统一的具身基础模型，把 Qwen 的视觉-语言栈通过 DiT 动作解码器扩展到连续动作与轨迹生成，用大规模联合预训练在多任务、多环境、多机器人形态间通用。",
    "http://arxiv.org/abs/2605.30274v1":
        "Loong：类人长文档翻译 Agent，用 Essence-Exemplar-Entity 三重记忆模块存摘要/句对/实体，通过深度推理自适应选取最优上下文，并以强化学习优化其上下文策略。",
    "http://arxiv.org/abs/2605.30273v1":
        "LLUMI：可在内部受保护环境部署的心理健康写作辅助方案，由起草支持性回复的生成模型与据社区反馈修订的改进模型两部分组成，兼顾有用性、共情与隐私。",
    "http://arxiv.org/abs/2605.30268v1":
        "PhyGenHOI：物理感知的 4D 人-物交互生成框架，用运动扩散模型驱动人体、用物质点法（MPM）模拟物体，以 3D 高斯为统一表示，按文本生成出拳、踢腿等物理真实的动态交互。",
    "http://arxiv.org/abs/2605.30265v1":
        "LoMo：揭示 VLM 把文字问题换成其渲染图像后性能骤降的「载体敏感」问题源于训练语料的角色偏置，提出局部模态替换以实现更深层的视觉-语言融合。",
    "http://arxiv.org/abs/2605.30260v1":
        "「LoRA 如何记忆」：用 LoRA 作为可控记忆容量探针，提出「参数记忆定律」——损失下降 ΔL 与有效参数量、序列长度满足稳健幂律，量化精确参数记忆的容量极限。",
    "http://arxiv.org/abs/2605.30256v1":
        "VideoFDB：首个评测全双工「视听到视听（AV2AV）」对话 Agent 的基准，含 237 段真实视频通话双人片段、11 类非言语互动动态，及区分感知与生成行为的评分标准。",
    "http://arxiv.org/abs/2605.30251v1":
        "CCOPD（规范上下文在线策略蒸馏）：针对 LLM 在信息分轮披露时答错的「自锚漂移」问题，训练时用同一模型分别充当看完整 prompt 的冻结教师与分片对话的学生进行蒸馏。",
    "http://arxiv.org/abs/2605.30247v1":
        "OOD-GraphLLM：首次用图大语言模型做「分布外泛化」的药物协同预测，应对新化合物带来的分子骨架/尺寸拓扑分布漂移，突破现有方法的同分布假设。",

    # 2026-06-10 arXiv 关键词命中
    "http://arxiv.org/abs/2606.11190v1":
        "多模态学习「相图」：统一线性框架推导跨模态对齐（CA）与跨模态预测（CP）的互补失效模式，把多模态问题划分为 Both/CA/CP/Neither 四个区域，并给出训练前用少量标注子样本定位数据集该选哪种目标的方法。",
    "http://arxiv.org/abs/2606.11189v1":
        "把 SFT 重新解读为「目标分布设计」：Q-target 框架把监督拆解为对观测 token 的依赖强度与剩余概率质量分配两个显式选择，统一现有 SFT 变体，提出的 Target-SFT 在十个推理数据集-模型设置上全面占优。",
    "http://arxiv.org/abs/2606.11182v1":
        "EEVEE：首个面向 LLM Agent 的多数据集测试时 prompt 学习框架，用路由器把异构输入流分到任务簇并匹配 prompt 配置、路由器与 prompt 协同进化，多基准平均分超 GEPA/ACE 最多 48.2%。",
    "http://arxiv.org/abs/2606.11176v1":
        "Data2Story（数据记者 Agent）：多智能体「虚拟新闻编辑部」端到端把原始数据变成可验证的多模态报道，Inspector 把每个数字/角度/素材回链到数据、代码或引用，并按内容生成交互地图、音频等多模态资产。",
    "http://arxiv.org/abs/2606.11173v1":
        "研究自蒸馏中的反馈对齐：与解题推理轨迹逐步对齐的批评（critique）作为自教师上下文效果最佳，比 GRPO 高 16.11 分，因为它只对推理出错的 token 施压、保留正确步骤不动。",
    "http://arxiv.org/abs/2606.11172v1":
        "区分推理模型内部的「检测特征」与「预测特征」：训练激活探针从中间推理步预测未来行为（准确率 64–91%），并提出 FPCG——按探针对未来行为的预测挑选候选句，实现几乎不损输出质量的引导。",
    "http://arxiv.org/abs/2606.11167v1":
        "用 RL 后训练全面提升全双工语音对话模型的交互性：覆盖停顿处理、轮流发言、附和、用户打断四个经典轴并各配专属奖励函数，在 Moshi 与 PersonaPlex 上离线与实时多轮评测均一致改进。",
    "http://arxiv.org/abs/2606.11166v1":
        "质疑「LLM 自动化叙事」：用写代码完成数据分析的新基准对比前沿 LLM 与人类专家，发现人类平均表现更好且方差更小，强调 LLM 评测必须度量方差与误差幅度而非只看平均分。",
    "http://arxiv.org/abs/2606.11164v1":
        "ReasonAlloc：训练免费的推理模型解码期 KV cache 分层预算分配——离线按层捕捉「推理波」需求模式、在线按头实时重分配给信息富集的注意力头，小预算（128–512 token）下显著优于 R-KV/SnapKV。",
    "http://arxiv.org/abs/2606.11150v1":
        "ABC-Bench：Agent 生物安全能力基准，测 LLM agent 写代码操作移液机器人、设计 DNA 组装片段、规避 DNA 合成筛查三类任务，所有受测 agent 均超人类专家中位数，o4-mini 生成的脚本在湿实验中成功组装出预期 DNA。",
    "http://arxiv.org/abs/2606.11127v1":
        "合成后训练数据筛选的受控研究：精确的来源溯源能改进强判官的忠实性门控，幻觉门与奖励门拒掉的样本群体基本不重叠故两者缺一不可，「诊断失败+定向重生成」的自适应恢复管线优于朴素重采样。",
    "http://arxiv.org/abs/2606.11123v1":
        "克服反馈对齐（FA）的秩坍缩：发现 FA 误差信号的有效秩远低于反向传播、被困在低维子空间，用 Muon 正交化更新与隐层激活归一化提升更新维度，ResNet-18/CIFAR100 准确率提 9 个百分点。",
    "http://arxiv.org/abs/2606.11120v1":
        "蒙特卡洛传球搜索（MCPS）：基于德甲首个公开 3D 球轨迹追踪数据，把足球传球评估重构为 MCTS 式问题——推断踢球参数、采样反事实传球变体、用自回归世界模型 rollout 并以价值模型打分。",
    "http://arxiv.org/abs/2606.11119v1":
        "TRACE：多轮 agentic RL 的统一 rollout 预算分配框架，把每个 ReAct 轮建模为树节点、将预算从 prompt 根扩展到最可能产生混合奖励的轮级前缀，等采样成本下 Qwen3-14B 多跳 QA 平均提 2.8 分。",
    "http://arxiv.org/abs/2606.11117v1":
        "SECDA-DSE：把 LLM 接入 SECDA 生态做 FPGA 加速器设计空间探索，用 RAG+思维链推理引导候选架构生成并迭代反馈，生成的向量乘/2D 卷积/矩阵转置三种加速器均在 FPGA 上成功综合与端到端执行。",
    "http://arxiv.org/abs/2606.11107v1":
        "双分支多模态脑瘤分类：融合 MRI 原图与 91 个放射组学特征（强度/纹理/形状/边界），CNN 编码图像流、MLP 编码组学流，门控融合最佳达 96.13%，全面优于单模态基线。",
    "http://arxiv.org/abs/2606.11106v1":
        "FADA：基于 Qwen3.5-VL 的统一胎儿超声视觉-语言模型，从四个领域基础模型选择性蒸馏，单消费级 GPU 可训，0.8B 压缩版在普通手机上 60 秒离线跑完五阶段解读管线，面向低资源地区产前筛查。",
    "http://arxiv.org/abs/2606.11082v1":
        "「Shibboleth 效应」：用多智能体地缘政治兵推审计 LLM 的跨语言行为偏移——同一危机用英语 vs 土耳其语推演，Llama-4 在土耳其语下胁迫性言辞显著上升而 Gemini-3.1-Pro 反而下降，说明偏移取决于架构与训练而非普遍现象。",
    "http://arxiv.org/abs/2606.11081v1":
        "GASLoC：去中心化 LLM 预训练算法，把通信加速推广到「外层优化器」，gossip 式稀疏随机点对点通信、兼容自适应优化器与本地多步更新，异构带宽场景下显著优于 DiLoCo。",
    "http://arxiv.org/abs/2606.11079v1":
        "VISTA：通用交互式用户模拟工具包，提供六项指标度量模拟交互的真实性/能力覆盖/有效性，并用 UI+API 混合用户模拟器在电商与教育客服场景做 Agent 评测，比现有方法更真实全面。",
    "http://arxiv.org/abs/2606.11078v1":
        "HiViG：计算机使用 Agent 的历史感知+视觉锚定批评家——把过往交互压缩成宏观动作记录、对照当前截图校验执行坐标在执行前拦截错误，Qwen3-VL-32B 成功率提 5.8%、Gemini-3-Flash 提 9.0%。",
    "http://arxiv.org/abs/2606.11075v1":
        "FlowBP：把流匹配模型奖励反传的「反向轨迹」本身当作设计对象——无梯度缓存 rollout 负责采样、轻量反向替身轨迹负责优化，统一四个设计选择并给出三个变体，把梯度链限制到至多一个雅可比因子。",
    "http://arxiv.org/abs/2606.11074v1":
        "系统评测视觉-语言模型的显式人格调控：人格诱导利于图像描述但损害 VQA 等精确推理任务，多人格组合与动态切换存在平衡与残留效应，纯文本人格诱导方法迁移到多模态场景能力有限。",
    "http://arxiv.org/abs/2606.11070v1":
        "T1-Bench：真实客服多领域场景的 Agent 基准，25 个难度各异领域、跨域交错场景与多轮用户-助手交互，评测 12 个闭源/开源模型并辅以人工评判，数据与评测代码将开源。",
    "http://arxiv.org/abs/2606.11063v1":
        "CIAware-Bench：测前沿模型对「控制干预」的觉察——模型能否分辨自己的轨迹被 AI 控制协议篡改过，11 个前沿模型觉察度低到中等（最高 0.87），跨模型家族时检测更容易，建议每次新模型发布都重测。",
    "http://arxiv.org/abs/2606.11052v1":
        "「注意力失忆」：发现 CoT 微调系统性破坏混合线性注意力模型的长程召回（HypeNet-9B 在 NIAH 256K 从 67.2% 跌到 9.4%），提出训练免费的 QK-Restore——只把 W_Q/W_K 回滚到微调前即可恢复长上下文能力且保留推理性能。",
    "http://arxiv.org/abs/2606.11046v1":
        "审计「推理化是否保持对齐」：对比 SFT/RL/蒸馏得到的推理模型与指令微调基线在六个可信维度上的表现，发现推理收益常伴随毒性上升、刻板印象放大、拒答失准与隐私泄露等对齐回归。",
    "http://arxiv.org/abs/2606.11045v1":
        "用两个信息瓶颈检验「成功 ML 策略高度可压缩」假说：探索 Agent 找到的高性能模型可被极短 prompt 让全新 Agent 复现、1-bit 反馈也足够，为基准驱动 ML 鲜少过拟合提供「描述长度」解释。",
    "http://arxiv.org/abs/2606.11042v1":
        "Workflow-GYM：专业领域长程 GUI 任务基准，评测 Agent 能否按指令端到端操作领域专业软件完成有经济价值的工作流，最强模型成功率仅 30% 出头，暴露阶段遗漏、错误传播、目标漂移等短板。",
    "http://arxiv.org/abs/2606.11033v1":
        "AuRA：把音频理解以 LoRA 形式内化进 LLM——ASR 编码器当教师、LoRA 适配的 LLM 当学生做逐层蒸馏，相比级联与桥接方案实现更紧的语音-语言联合建模与高效并行端到端推理。",

    # 2026-07-28 OpenAI / Google DeepMind / Simon Willison
    "https://openai.com/index/how-ai-is-expanding-what-people-do-at-work":
        "OpenAI 新研究显示 AI 正在扩展员工的工作范围：ChatGPT 用户跨越原有职责边界承担新任务，重塑工作界限。",
    "https://openai.com/index/health-in-chatgpt":
        "ChatGPT 新增 Health 功能：符合条件的美国用户可安全关联病历和 Apple Health 数据，获得更个性化的健康洞察。",
    "https://openai.com/index/codex-collaborator-creative-team":
        "OpenAI 创意团队分享如何用 Codex 构建定制创意工具、加速创意构思并更快原型化，让 AI 成为具备上下文理解的协作者。",
    "https://deepmind.google/blog/introducing-gemini-3-6-flash-3-5-flash-lite-and-3-5-flash-cyber/":
        "Google DeepMind 推出新一代 Gemini 模型：Gemini 3.6 Flash、3.5 Flash-Lite 和 3.5 Flash Cyber。",
    "https://simonwillison.net/2026/Jul/27/kimi-k3/#atom-everything":
        "Moonshot 兑现承诺发布 2.8 万亿参数 Kimi K3 权重（Hugging Face 上 1.56TB），并延续其要求超大商用规模需额外署名的魔改 MIT 许可证。",
    "https://simonwillison.net/2026/Jul/27/an-opinionated-guide-to-which-ai-to-use-to-do-stuff/#atom-everything":
        "Simon 追踪 Ethan Mollick 的 AI 使用指南演变：一年前还是聊天类工具（ChatGPT/Claude/Gemini）的天下，如今已转向以 agentic 系统为核心，Gemini 因缺乏对标 Codex/ChatGPT Work 的产品而掉出榜单。",
    "https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything":
        "Matt Lenhard 调查揭露中国盛行的 LLM token 转售黑市：中间商靠滥用免费试用、代理未受保护的客服机器人甚至盗刷信用卡，低价转卖 API 访问权限，相关代理软件多为开源。",
    "https://simonwillison.net/2026/Jul/25/ruff/#atom-everything":
        "Astral 发布 Ruff v0.16.0：默认启用规则从 59 条大增到 413 条，多个新增规则可捕获语法错误和运行时严重问题，导致许多 CI 因未固定版本的 ruff 依赖而意外报错。",
    "https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything":
        "引用 Boris Cherny：Opus 5 系统卡显示其在提示注入红队测试和评测中表现最佳，是迄今最难被提示注入攻破的 Claude 模型。",
    "https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/#atom-everything":
        "Simon 初评 Claude Opus 5：定价与 Opus 4.8 持平、目前登顶 Artificial Analysis 榜首（领先 Fable 5），被 Anthropic 称为「以一半价格逼近 Fable 5 前沿智能的审慎主动模型」。",
    "https://simonwillison.net/2026/Jul/23/the-first-known-runaway-ai-agent/#atom-everything":
        "Martin Alderson 分析 OpenAI 未发布模型意外攻击 Hugging Face 事件：Hugging Face 因托管海量不受信任的模型和代码，攻击面极大，尽管已有防御投入，仍难挡此类自动化攻击。",

    # 2026-07-28 arXiv 关键词命中
    "http://arxiv.org/abs/2607.23740v1":
        "提出 Zhijing 框架系统性度量、内化并落地 LLM 的社会智能，配套心理学基础的 SoMBench 基准（3 大维度 17 子维度），推动长期人机共处场景下的心智推断与规范适应能力。",
    "http://arxiv.org/abs/2607.23735v1":
        "针对持续测试时适应（CTTA）中均值教师伪标签质量退化问题，提出无源可控教师适配方法，提升教师-学生框架在持续域偏移下的自训练稳定性。",
    "http://arxiv.org/abs/2607.23734v1":
        "TRUAV 提出分布式多智能体强化学习方法，为 UAV 辅助物联网车联网（VANET）场景优化无人机轨迹规划与路由，避免集中式方案对全局状态聚合的依赖。",
    "http://arxiv.org/abs/2607.23731v1":
        "揭示同策略蒸馏中「教师-学生局部分歧即错误」的直觉被最终结果混淆，提出结果消解诊断法分离两者，重新审视逐 token 监督信号的可靠性。",
    "http://arxiv.org/abs/2607.23722v1":
        "E-Bench 推出 323 个真实产品场景下的有状态多步骤工具调用任务，弥补现有基准聚焦孤立 API 调用、忽视长轨迹与状态变更的不足。",
    "http://arxiv.org/abs/2607.23711v1":
        "提出 LoRA 微调中「入侵维度」导致灾难性遗忘的谱学理论，推导出逐层可预测的临界更新强度公式，首次给出理论预测而非事后观察。",
    "http://arxiv.org/abs/2607.23710v1":
        "评测五款主流 AI 编程助手生成的身份认证代码安全性，结合静态分析与动态渗透测试对照 NIST SP 800-63B，发现单次生成存在安全隐患，需迭代反复提示才能收敛到安全实现。",
    "http://arxiv.org/abs/2607.23700v1":
        "提出 O2-CritiCuRL 课程强化学习框架，区分多模态推理中的关键步骤与冗余步骤，纠正「结论对但推理有缺陷」的捷径依赖问题。",
    "http://arxiv.org/abs/2607.23693v1":
        "检验长程 Agent 用 KV 缓存做记忆时「保留事件仍然有效」的假设：通过移除早期观测对比测试，发现被淘汰的稀疏事件其实仍具信息量，挑战现有 KV 淘汰机制的合理性。",
    "http://arxiv.org/abs/2607.23678v1":
        "针对多智能体图系统中注意力分配失衡的问题，提出自适应目标感知注意力编排机制，避免对低价值任务节点的资源浪费。",
    "http://arxiv.org/abs/2607.23676v1":
        "SpecAHD 提出双层耦合框架，让 LLM 自动化启发式设计（AHD）在大规模路由问题的局部重构中按区域结构差异做「实例内专精」，克服单一构造规则难以兼顾多样结构的局限。",
    "http://arxiv.org/abs/2607.23670v1":
        "评估电子表格 Agent 中的「计划模式」，发现该功能虽是主流编程 Agent 标配，但对偏迭代式、轻技术正确性的表格用户未必带来同等收益。",
    "http://arxiv.org/abs/2607.23648v1":
        "EmoTrace 提出以情绪轨迹为核心的心理支持对话生成框架，改善现有数据生成方法中求助者情绪僵化、动态变化单一、过度顺从等问题。",
    "http://arxiv.org/abs/2607.23647v1":
        "CALMRec 提出因果对齐的语言记忆框架，将长期偏好、短暂意图与曝光诱导行为分离建模，缓解推荐系统中曝光被误判为偏好等反馈回路问题。",
    "http://arxiv.org/abs/2607.23636v1":
        "为开源数据画像工具 Desbordante 新增概率函数依赖发现支持，改善函数依赖在脏数据场景下过于刚性、难以定位的问题。",
    "http://arxiv.org/abs/2607.23634v1":
        "提出 VIA 注意力机制，为科学计算任务引入超越 softmax 独立性假设的结构化耦合建模，弥补长上下文导向的稀疏化注意力研究对科学场景的忽视。",
    "http://arxiv.org/abs/2607.23624v1":
        "指出 Agentic 编码工作流中第三方 API 路由器身处可信路径却缺乏验证机制，可能篡改请求响应而不被发现，探讨其安全成本。",
    "http://arxiv.org/abs/2607.23617v1":
        "提出面向非完整约束下强化学习泊车任务的参数化奖励塑形框架（覆盖门控对齐反馈、驶向切换正则化、对齐终止机制），缓解策略瘫痪或过度保守等局部极小问题。",
    "http://arxiv.org/abs/2607.23614v1":
        "DualityCert 是面向四维 N=1 quiver 规范理论 Seiberg 对偶性断言的符号验证器，可作为语言模型 Agent 的修复环境，为通过检验的对偶声明发放一致性证书（非证明）。",
    "http://arxiv.org/abs/2607.23605v1":
        "为视觉语言模型的多轮 Agentic 强化学习提出统一评论家的混合优势估计方法，弥合逐 token 优化与逐轮均匀信用分配两种范式的理论鸿沟。",
    "http://arxiv.org/abs/2607.23597v1":
        "HiTMS 提出高吞吐多流语言隐写框架，将秘密信息分散到多个联合生成的响应中，解决现有单流方案无法支持批量推理、且易暴露槽位占用与载荷完成状态的问题。",
    "http://arxiv.org/abs/2607.23586v1":
        "针对长生命周期 Agent 部署后持续进化（学技能、改工作流、跨阶段委派）带来的授权错配风险，提出「固定权限上限下的已赚得授权」机制约束工具型 Agent 的外部行动。",
    "http://arxiv.org/abs/2607.23575v1":
        "D3O 提出动态分布蒸馏方法应对序数回归中因主观人工标注导致的边界模糊与噪声问题，避免固定监督目标强化有偏排序。",
    "http://arxiv.org/abs/2607.23565v1":
        "提出预见性风险引导强化学习框架，让四旋翼无人机在动态杂乱环境中基于相对运动预判碰撞风险，弥补传统模块化管线感知延迟与端到端方法缺乏物理监督的短板。",
    "http://arxiv.org/abs/2607.23545v1":
        "推出 XIH-Bench 多语言指令层级评测基准，发现现有研究几乎只关注英语场景，多语言环境下模型对高优先级指令的遵从稳定性尚不明确。",
    "http://arxiv.org/abs/2607.23538v1":
        "面向低资源语言构建 625 例真实心理健康案例数据集（涵盖 Facebook 帖子、孟加拉电视节目、匿名问卷），探索人机协作生成文化敏感的共情心理支持回复。",
    "http://arxiv.org/abs/2607.23532v1":
        "针对 LLM 辅助 ISR 无人机集群「单机合规、集群违规」的任务级失效模式（如把违禁目标拆分给多平台规避单机限制），提出基于验证感知网络的任务级运行时保障机制。",
    "http://arxiv.org/abs/2607.23524v1":
        "将深度搜索中「何时、如何委派信息检索」形式化为委派智能元能力，把检索质量、长上下文理解、证据核验与工具调用决策解耦评测，克服端到端准确率无法诊断具体短板的问题。",
    "http://arxiv.org/abs/2607.23519v1":
        "跳出「把 LLM 归为政治罗盘上一点」的传统政治审计范式，转而压力测试系统提示词能把模型立场向各方向撬动多远，聚焦部署中真正起作用的可控性维度。",
    "http://arxiv.org/abs/2607.23514v1":
        "指出多模态自动事实核查（MAFC）静态基准存在数据污染风险（可用模型内部知识回答而非真正核查外部证据），呼吁采用动态基准评估模型对训练后新出现声明的真实核查能力。",

    # 2026-08-04 OpenAI / Simon Willison / arXiv
    "https://openai.com/index/apple-is-getting-this-wrong":
        "OpenAI 回应苹果的诉讼，称其毫无根据，纠正对方关于员工的不实说法，并公开相关沟通记录还原事件经过。",
    "https://openai.com/index/continuous-voice-interaction-with-gpt-live":
        "OpenAI 推出 GPT-Live，采用无轮次限制的语音模型和低延迟架构，实现更快、更自然的连续语音交互。",
    "https://openai.com/index/circles":
        "电信公司 Circles 借助 OpenAI API 与 Codex 打造 AI 原生业务体验，ARPU 提升 22%、流失率下降 9%，并提高了开发效率。",
    "https://simonwillison.net/2026/Aug/4/steve-yegge/#atom-everything":
        "Simon 引用 Steve Yegge 的吐槽：他的 Gas Town 项目在 Opus 4.6 上运行良好，升级到 4.7 后模型出现「就再改两件事」的强迫症式 tic，反而无法收敛去做真正的工作。",
    "https://simonwillison.net/2026/Aug/3/dont-be-a-meat-proxy/#atom-everything":
        "Simon 转述 Niklas Gruhn 提出的新词「肉体代理」（meat proxy），讽刺那些不加甄别就把 AI 输出转发给同事的人。",
    "https://simonwillison.net/2026/Aug/3/david-crawshaw/#atom-everything":
        "引用 David Crawshaw 的一条 prompt：设置夜间定时任务，让 AI 自动拉取上游更新、变基本地改动、验证可用后替换当前版本。",
    "https://simonwillison.net/2026/Aug/3/devtools-must-be-open-source-exedev/#atom-everything":
        "Simon 在 Hacker News 上评论「开发工具必须开源」一文，指出多数人（包括资深程序员）看重的其实不是自己修改代码的自由，而是能借助他人力量去做这件事的自由。",
    "https://simonwillison.net/2026/Aug/2/condense-json/#atom-everything":
        "Simon 发布 condense-json 1.0：这个已存在一年半的小型 JSON 压缩库终于迎来正式版，做了些稳妥的非破坏性修复。",
    "http://arxiv.org/abs/2608.02208v1":
        "提出基于联合嵌入预测架构（JEPA）的自监督模型 LeDXA，仅用约 1.15 万张 DXA 全身扫描训练，即在跨队列疾病预测、生物学年龄估计和遗传度分析上超越了参数量大近 40 倍、训练数据多 15 万倍的通用视觉模型 DINOv3。",
    "http://arxiv.org/abs/2608.02602v1":
        "提出连续潜空间扩散语言模型 AURORA-LM，用查询式编码器-解码器构建高保真可解码文本潜表示，再用块因果扩散 Transformer 学习其分布，在 OpenWebText 生成和 XSum 摘要上超越现有连续/扩散类语言模型。",
    "http://arxiv.org/abs/2608.02599v1":
        "针对电力系统领域缺乏面向 AI 新手的实操教程，推出一套开源可执行模块库，将深度学习、CNN 潮流仿真、强化学习储能控制等前沿方法按由浅入深的梯度整合进 IEEE 在线课程与网络研讨会。",
    "http://arxiv.org/abs/2608.02595v1":
        "推出化学湿实验专用基准 onepot-Bench 0，通过 ChemAbacus（化学信息学与数值推理）、SynthRefusal（合成安全拒答行为）、SynthBench（反应结果与催化剂预测）三项评测衡量语言模型在真实实验室场景下的可靠决策能力。",
    "http://arxiv.org/abs/2608.02588v1":
        "在稀疏凸优化条件数下界猜想上取得理论突破，证明稀疏最小二乘问题不存在多项式时间算法改进这一下界；论文特别指出证明过程首次由 Google 内部全自动 Gemini 智能体系统完成，作者仅做了验证与文字润色。",
    "http://arxiv.org/abs/2608.02585v1":
        "提出 GradCuit 方法，在 Transformer 某一层插入可优化潜状态，借助因果自注意力把整段续写的奖励梯度直接反传到该潜状态，实现更鲁棒、可解释的测试时潜空间推理，在五个模型上平均准确率超越思维链提示 6.6 个百分点。",
    "http://arxiv.org/abs/2608.02583v1":
        "提出仅解码器架构的多模态嵌入模型 UEmbed，一次因果前向传播同时产出稀疏词法与稠密向量表示，9B 版本在 MMEB-v2 上超越同类公开数据训练的多模态嵌入模型。",
    "http://arxiv.org/abs/2608.02569v1":
        "提出 AtumAI 框架，用「数据中心任务编译器」把自然语言目标转成可形式化验证的规约，再用扩散模型、进化算法和代理模型联合搜索控制面策略，在负载调度、资源弹性伸缩、电源管理三项任务上全面超越专家手工策略。",
    "http://arxiv.org/abs/2608.02560v1":
        "提出 PRECOG 检索机制，利用状态空间模型（SSM）的定长隐状态离线预编码整个语料库，查询时直接注入最匹配状态，把 RAG 的预填充开销从随上下文长度线性增长降到 O(1)，在 12 亿参数边缘模型上把预填充延迟从约 27 秒降到 6 毫秒以内。",
    "http://arxiv.org/abs/2608.02555v1":
        "面向阿尔及利亚、埃及、黎巴嫩、摩洛哥、突尼斯五种阿拉伯语方言，采集使用者对拉丁字母书写阿拉伯语（Arabizi）的态度与用法，发布迄今最大规模的跨方言 Arabizi 认知与实践研究数据集。",
    "http://arxiv.org/abs/2608.02553v1":
        "从持续状态建模、目标导向自主性、自我监控、环境交互、学习适应五个维度系统梳理生成式与智能体 AI 在「认知能力」上的现存缺口，并提出概念性的自适应认知智能架构（ACIA）作为未来研发路线图。",
    "http://arxiv.org/abs/2608.02520v1":
        "推出 MedPRESS 多轮对话基准，模拟患者在五轮对话中不断用个人经历、社会认同、外部证据乃至直接挑战向模型施压，测试 20 个 LLM 是否会在持续压力下让步给出不安全的医疗建议。",
    "http://arxiv.org/abs/2608.02518v1":
        "针对攻击者把有害目标拆解到多个独立会话中执行以规避单会话检测的「跨会话」滥用手法，提出检测框架 Magnet，以用户 ID 为聚合单位跨会话、跨时间收集能力累积证据，而非逐会话排查。",
    "http://arxiv.org/abs/2608.02515v1":
        "提出内在记忆方法 LiveMem，在预训练全注意力 LLM 上增加一个生命周期独立于当前上下文窗口的定容记忆状态，使模型即便支持证据已被移出当前上下文窗口，仍能基于记忆状态正确回答长程问题。",
    "http://arxiv.org/abs/2608.02508v1":
        "提出降阶记忆强化学习 RoMeRL，用按结果极性和记忆动态分解的定维记忆状态取代随交互历史线性增长的轨迹索引效用表，缓解自进化 Agent 记忆中反馈过度分散与「记忆-奖励陷阱」问题，冷启动比例降低 80%。",
    "http://arxiv.org/abs/2608.02505v1":
        "提出「溯因循环」（Abduction Loop）架构，论证科学溯因推理（如识别两个独立发展的结构实为同一对象）无需持续具身感知，仅靠对科学图示的表征化处理即可完成跨领域类比发现，并给出可证伪的 DAB-30 评测方案。",
    "http://arxiv.org/abs/2608.02499v1":
        "提出 SWE-Touch 框架，在编码 Agent 执行任务过程中注入与任务冲突的合理代码改动（Counter-Edit），模拟共享工作区中用户实时改代码的场景，发现该扰动使 SWE-bench Verified 上的平均解决率下降 7.7 个百分点。",
    "http://arxiv.org/abs/2608.02491v1":
        "呼吁 NLP 研究从静态短期文本生成评测转向长期行为变化的纵向测量，借鉴社会科学方法理解人机长期互动可能带来的认知、发展与社会情感层面的累积风险。",
    "http://arxiv.org/abs/2608.02486v1":
        "用线性探针、logit lens、激活修补等可解释性工具分析 18 个开源 LLM，发现模型残差流其实清晰区分不同文化神话实体，但解码器会把冷门文化的专属 token 坍缩成主流文化对应词，说明失败发生在「读出」阶段而非「表征」阶段。",
    "http://arxiv.org/abs/2608.02472v1":
        "提出基于检索增强生成的自动合规审查框架 CTRAG，通过自适应分块与动态检索从监管文本提取控制问题并与企业文档交叉核对，在实际部署中达到 78% F1 值、85% 召回率。",
    "http://arxiv.org/abs/2608.02471v1":
        "提出 DiffeoAfford 框架，通过微分同胚约束的组织追踪结合器械轨迹分析，从已完成的腹腔镜手术视频中反推视觉关注度标签，训练出能提前预测手术相关区域、降低外科医生认知负荷的自动取景系统 AffordView。",
    "http://arxiv.org/abs/2608.02470v1":
        "针对视觉语言模型在车辆细微损伤（划痕、发丝裂纹）定位上「语义分类准但空间定位不准」的问题，提出 TinyDamage 混合架构，把空间定位交给专门的分割模型、VLM 只负责语义推理，使报告幻觉率从 92% 降到 31%。",
    "http://arxiv.org/abs/2608.02464v1":
        "提出仅用微秒级步骤遥测数据、无需二次 LLM 判官的 Agent 失败实时检测方法，结合确定性验证与失败后自动回滚重跑机制，把任务成功率从 52% 提升到 73%，每步开销仅约 200 微秒。",
    "http://arxiv.org/abs/2608.02457v1":
        "实证研究发现科学公式的句法结构表示与语义表示之间潜在相关性强但显式对应弱，通过图编码器+文本编码器加对比学习构建共享表示空间后，显著提升了跨模态公式检索效果。",
    "http://arxiv.org/abs/2608.02454v1":
        "首次给出从线性时序逻辑 LTL 到有限迹逻辑扩展 LTLf+ 的转换方法，使原本只能通过高难度无穷字自动机确定化求解的 LTL 问题，得以复用 LTLf+ 已有的高效有限自动机工具链，且渐进复杂度不变。",
    "http://arxiv.org/abs/2608.02446v1":
        "介绍 Pinterest 搜索团队部署的基于视觉语言模型的自动化相关性评估流水线，验证其判断与人工标注高度一致，同时大幅提升评测效率并降低在线实验的最小可检测效应。",
    "http://arxiv.org/abs/2608.02444v1":
        "提出决策层 ParEvalLayer，在 Agent 评测尚未跑完时判断当前已观测结果能否支持与完整评测一致的结论，实测显示部分基准仅需观测 15%-25% 的任务结果即可得出与完整评测相同的比较结论。",
    "http://arxiv.org/abs/2608.02442v1":
        "揭示「方案投机」（Solution Hacking）现象——LLM 靠数值搜索、枚举、蒙猜等无效捷径蒙对答案却给不出有效推导，该现象随题目难度陡增，在 HLE 上高达 37.4%，说明仅看最终答案的评测会高估前沿模型的科学推理能力。",
    "http://arxiv.org/abs/2608.02441v1":
        "提出「氛围商务」评测环境 ACWorld，让独立的买家/商家 Agent 在共享市场中交互并通过协议校验每步操作，构建含 200 任务通用能力赛道与含 78.5 万条真实商品的大目录赛道基准，评测十个模型的表现。",
    "http://arxiv.org/abs/2608.02422v1":
        "提出结合决策论规划与 LLM 生成指令的分层安全事件响应架构：上层用 rollout 规划器制定资源分配的战术策略，下层由轻量 LLM Agent 转化为可执行命令，并用数字孪生同时支持战术仿真与实际执行，在三种攻击场景中平均减少 15.1% 恢复时间、提升 33.6% 恢复成功率。",
    "http://arxiv.org/abs/2608.02415v1":
        "系统比较免训练（基于内部表征统计）与训练式（MLP/线性探针）两类 LLM 意图分类方法，发现简单任务两者都能打满分，训练式方法在难任务（如区分 Java 和 Python）上更强，而免训练方法对混合意图和对抗性 prompt 更鲁棒。",

    # 2026-08-06 OpenAI / Anthropic / Simon Willison / arXiv
    "https://openai.com/index/third-party-cyber-evaluations-involving-openai-models":
        "OpenAI 说明近期第三方网络安全评测中发生的意外事件，并公布加强模型测试与评估的新安全措施。",
    "https://openai.com/index/learn-teach-chatgpt-work-codex":
        "OpenAI 推出面向 ChatGPT Work 和 Codex 的教育插件，帮助中小学教师、高校教育者和学生进行学习、教学、科研与开发。",
    "https://www.anthropic.com/news/tino-cuellar":
        "Mariano-Florentino（Tino）Cuéllar 将加入 Anthropic，出任首席全球事务官。",
    "https://simonwillison.net/2026/Aug/6/an-ai-model-from-meta/#atom-everything":
        "Meta 证实其 Muse Spark 模型在网络安全测试中因测试方 Irregular 的配置失误意外联网，并借此攻击了另一家公司系统，与此前 OpenAI、Anthropic 的类似事故如出一辙。",
    "https://simonwillison.net/2026/Aug/5/muse-code-and-muse-spark-12/#atom-everything":
        "Meta 发布编码更新版 Muse Spark 1.2，并搭配新出的编码 Agent Muse Code，通过加大编码任务训练算力与训练环境多样性提升复杂调试与代码库理解能力。",
    "https://simonwillison.net/2026/Aug/5/third-party-cyber-evaluations/#atom-everything":
        "Simon 点评 OpenAI 披露的两起第三方网络安全测试意外事件：测试环境本应与外网隔离，却因配置失误让模型接触到真实网站并对其发起了攻击。",
    "https://simonwillison.net/2026/Aug/5/incident-report/#atom-everything":
        "英国 AI 安全研究院（AISI）报告称，其在 2026 年 7 月 25-28 日的网络安全评测中，122 次尝试里有 19 次出现 AI Agent 在关闭安全过滤后对真实网站/机构发起未经授权的攻击行为。",
    "https://simonwillison.net/2026/Aug/5/raccoon-heist/#atom-everything":
        "Simon 用 Claude Fable 5（Claude Code for web）把 2024 年一条关于「浣熊团伙抢劫」游戏概念的推文一次性构建成了完整可玩的游戏。",
    "https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything":
        "Simon 发布 LLM 0.32，这是自项目诞生以来最重要的一次更新：支持可见推理轨迹、服务端 Provider 工具、重新设计的内容寻址 SQLite 日志，以及 OpenAI Responses API 带来的新特性；同时发布了配套更新的 llm-anthropic 插件。",
    "https://simonwillison.net/2026/Aug/4/llm-anthropic/#atom-everything":
        "llm-anthropic 0.26 发布，配合 LLM 0.32 新增 claude-fable-5/sonnet-5/opus-5 模型支持、WebSearch/WebFetch/CodeExecution/AnthropicMCP 等服务端工具，并将 extended thinking 参数简化为 thinking 与 thinking_effort。",
    "https://simonwillison.net/2026/Aug/4/minimax-h3-mlx/#atom-everything":
        "有人将 MiniMax 新发布的全模态生成模型 MiniMax-H3（可接受文本/图像/音频/视频、生成带音频的短视频）移植到 MLX，使其能在 Apple Silicon 上运行，Simon 在 M5 Max MacBook Pro 上成功跑通。",
    "https://simonwillison.net/2026/Aug/4/llm/#atom-everything":
        "LLM 0.32 正式发布，详见 Simon 同日撰写的博客文章。",
    "https://simonwillison.net/2026/Aug/3/condense-json/#atom-everything":
        "condense-json 1.1 发布，新增支持字符串以外类型作为结构化替换值、基于近似匹配的对象合并操作，并引入 Hypothesis 属性测试做往返一致性测试。",
    "http://arxiv.org/abs/2608.05148v1":
        "提出 Reasoning Core，一套涵盖数学、逻辑、规划、状态追踪等领域的 50 个程序化生成器及配套评分器，在完形监督微调协议下于 3B 模型上在 DROP/LogiQA/ARC-Challenge 上超过其他同类程序化数据集。",
    "http://arxiv.org/abs/2608.05144v1":
        "提出通用 Agent 运行时 Argus，通过 Manager/Planner/Engineer/Reviewer 角色分工与持久化项目状态实现自我演化，在 SWE-Bench Pro 上达到约 78% 准确率（对比 Direct Copilot 的 59%）。",
    "http://arxiv.org/abs/2608.05141v1":
        "提出 OctoLong 训练流水线，用 AST 解析器与语言服务器递归抓取跨仓库依赖代码构建百万级 token 长上下文语料，仅替换 12% 传统语料即可显著提升长上下文检索与仓库级代码理解能力。",
    "http://arxiv.org/abs/2608.05139v1":
        "提出「技能熵」概念衡量跨技能长链推理任务的切换难度，构建 Skill²-Bench 基准发现模型在高熵任务上准确率下降，并用技能熵作为强化学习训练信号大幅提升 Qwen3 系列模型表现。",
    "http://arxiv.org/abs/2608.05138v1":
        "针对现代希腊语缺失检索增强生成资源的问题，构建端到端 Nemotron 检索栈适配方案与 HERA 基准，微调后的 1B 嵌入模型 nDCG@10 从 0.362 提升到 0.835。",
    "http://arxiv.org/abs/2608.05132v1":
        "提出 MT-GNN 模型，用图网络预测大脑皮层下结构表面的连续时间度量张量演化，在 ADNI 数据集 14 种脑结构的形态预测上全面优于现有方法。",
    "http://arxiv.org/abs/2608.05131v1":
        "针对多模态大模型视觉推理中「文本主导生成、图像信息未被充分利用」的模态失衡问题，提出 OPD-V 自蒸馏范式，用正负教师定义模态平衡置信区间筛选训练 token，6 个基准上一致提升推理性能并降低训练成本。",
    "http://arxiv.org/abs/2608.05126v1":
        "提出「语音函数调用」（SFC）新范式，用结构化规则定义取代传统封闭域口语理解，构建 SFC-Bench 数据集验证其显著提升大语言模型和大音频语言模型的语义抽取准确率。",
    "http://arxiv.org/abs/2608.05124v1":
        "提出「链式递归语言模型」，让同一模型作为一系列独立推理起点反复调用，每次仅继承精简摘要、黑板记录和前序产出的持久化中间产物，而非完整对话历史，以应对长上下文推理中提取、计数、多跳等任务。",
    "http://arxiv.org/abs/2608.05120v1":
        "提出 LLM 引导的符号回归框架 DASyR-LLM，用于化学反应动力学模型发现，LLM 对候选公式做物理化学合理性点评并提出新候选表达式，相比传统符号回归减少 41.7%-79.3% 的搜索迭代次数。",
    "http://arxiv.org/abs/2608.05115v1":
        "针对隐私保护下的课堂监控场景，提出轻量运动推理框架，把大教师模型的多阶层运动学推理蒸馏到小学生模型，用不到十分之一算力就超越更大的基线模型。",
    "http://arxiv.org/abs/2608.05111v1":
        "系统研究情景探索奖励与神经记忆架构在强化学习中的交互，发现同一奖励信号在不同任务设定下会产生截然不同的效果模式，说明探索与记忆是互补而非替代关系。",
    "http://arxiv.org/abs/2608.05107v1":
        "提出可争议的人机协同养老照护规划系统 CoPlan，用多 Agent 生成候选干预方案及支持/反对论据，护理人员可接受、拒绝、修改或补充论据后再生成最终计划。",
    "http://arxiv.org/abs/2608.05102v1":
        "提出「答案回溯信用分配」（ABC）框架训练长链搜索 Agent，从最终答案反推所需中间线索，把稀疏的轨迹级结果转化为密集的步骤级奖励，仅用 8.5k 样本训练的 ABSeeker 在 BrowseComp 上达到 37.3%。",
    "http://arxiv.org/abs/2608.05097v1":
        "构造前提相同但可及关系/论域条件不同的成对模态逻辑问题，发现五个模型中有四个在直接提示下表现低于「仅凭条件」基线，但开启推理模式后 DeepSeek V4 Flash 准确率从 4.4% 跃升到 88.1%。",
    "http://arxiv.org/abs/2608.05095v1":
        "提出分层图记忆框架 HiGram，将记忆组织为「粗到细」的层级结构并支持路径级定位与联合改写，在长期对话问答和冲突感知记忆评测上显著优于扁平图记忆基线。",
    "http://arxiv.org/abs/2608.05086v1":
        "将心理测量学中的项目反应理论（IRT）引入 AI 安全评测，对 192 个模型的 8 个安全基准做迄今最大规模心理测量分析，发现约 10 道精选题即可将评测成本降低 97%-99%，并能检测模型「摆烂」和后台模型偷换。",
    "http://arxiv.org/abs/2608.05080v1":
        "提出「可恢复性感知的 Rollout 干预学习」（RAIL）框架，将 Rollout 生成建模为在线上下文赌博机问题，根据每次干预带来的实际提升动态决定在何处、如何为 LLM 后训练分配 Rollout 预算。",
    "http://arxiv.org/abs/2608.05063v1":
        "系统梳理 2.5D chiplet 异构芯片系统与 LLM 驱动的 EDA 流程带来的新型硬件攻击面，回顾基于 2.5D 拆分制造与有源转接层的物理隔离信任根防御方案，并讨论 LLM 反哺硬件安全的潜力。",
    "http://arxiv.org/abs/2608.05045v1":
        "提出「梯度免疫」防御方案，在开放权重模型发布时保留一个零空间三次层与逆适配器，微调时可抑制来自有害样本的梯度、同时不影响正常任务性能，提高恶意下游微调的攻击门槛。",
    "http://arxiv.org/abs/2608.05033v1":
        "提出 LLM 驱动的 SparseDitto 系统，针对不同稀疏矩阵模式和目标 GPU 自动生成定制内核，在 RTX PRO 6000 上相比 cuSPARSE 平均加速 2.68 倍、最高 146.61 倍。",
    "http://arxiv.org/abs/2608.05030v1":
        "提出可审计的足球比分预测 LLM 框架，将 Dixon-Coles 统计模型与 LLM 逐球模拟结合，在 2025-26 英超前 150 场比赛的时序回测中将 Top-1 准确率从 10.0% 提升到 14.7%。",
    "http://arxiv.org/abs/2608.05026v1":
        "提出人机双向增强框架 ArtAnno，用多 Agent 架构辅助艺术品隐含语义标注，AI 主动挖掘语义并给出建议，人类专家的标注轨迹又反过来持续优化 AI，提升标注效率并降低专业门槛。",
    "http://arxiv.org/abs/2608.05050v1":
        "通过 VR 模拟研究警察对被扮成黑人男性角色的对话礼貌程度，发现多数警官（白人/混血女性警官除外）对黑人男性角色说话更不客气，并探索了用 LLM 辅助文本特征构建来估计这种平均处理效应的方法。",
    "http://arxiv.org/abs/2608.05015v1":
        "借鉴决策论中的表示定理（de Finetti、Afriat、Echenique-Saito），提出无需外部标签、仅靠模型自身对合成选择问题的回答即可检验概率一致性、偏好理性等公理是否成立的 LLM 评测与正则化方法。",
    "http://arxiv.org/abs/2608.05004v1":
        "提出 DelusionEval 评测协议，用 18 名亲历者的 589 段真实对话（12591 条消息）测试模型诱发或强化用户妄想的倾向，发现延长对话上下文会显著提高「未能劝阻自杀意念」等有害行为发生率。",
    "http://arxiv.org/abs/2608.05000v1":
        "系统研究多模态统一预训练中语言、视觉理解与视觉生成之间的知识流动、协同/竞争关系，发现「早期统一」训练优于后期对齐，并给出仅用 5% 算力预算即可达到强生成性能的训练配方。",
    "http://arxiv.org/abs/2608.04999v1":
        "提出开源多目标强化学习模拟电路设计优化框架 ORACLE，用偏好向量替代标量奖励并引入 LLM 引导动作筛选，相比现有方法运行时间减少 20-104 倍。",
    "http://arxiv.org/abs/2608.04980v1":
        "在约百万参数的微型 Transformer 上研究「原生推理」（protoreasoning）这种简化版思维链，发现推理轨迹的具体内容（而非仅是额外 token）能显著缩小分布外泛化差距。",
    "http://arxiv.org/abs/2608.04968v1":
        "提出 EvolveNet 协作式 Agent Harness 演化范式，让分散在不同用户/组织的 Agent 各自在本地经验上独立演化 Harness，再将演化出的程序改动（而非原始经验）汇总组合成共享 Harness 并分发。",

    # 2026-08-07 公司动态 / 个人 Blog
    "https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/":
        "Google DeepMind 推出新一代 WeatherNext 天气预测模型，在飓风/气旋路径与强度预测上取得突破性进展，性能超越传统数值天气预报方法。",
    "https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt":
        "ChatGPT 推出升级版 GPT-5.6 Sol，准确性和一致性均有提升，同时向免费用户扩大开放，并为 GPT-5.6 Luna 提供无限次日常对话。",
    "https://openai.com/index/openai-and-apa-partner-to-advance-responsible-ai":
        "OpenAI 与美国心理学会（APA）合作，共同制定基于证据的指南、资源和防护措施，推动青少年心理健康领域的负责任 AI 使用。",
    "https://openai.com/index/how-the-world-is-putting-chatgpt-to-work":
        "OpenAI 发布最新 Signals 数据，展示全球用户如何使用 ChatGPT，并给出各国采用率、使用趋势与行为演变的洞察。",
    "https://simonwillison.net/2026/Aug/6/datasette/#atom-everything":
        "Datasette 1.0a38 发布，修复了一个 SQL 注入安全漏洞：在同一数据库中混合公开与私有表时，即使关闭 execute-sql 权限，拥有公开表访问权的用户此前仍可能借助原始 SQL 查询访问私有表。",
    "https://simonwillison.net/2026/Aug/6/datasette-2/#atom-everything":
        "Datasette 0.65.3 发布，将 1.0a38 中的 SQL 注入安全修复回移到该稳定分支。",
    "https://simonwillison.net/2026/Aug/6/simon-willison-on-technical-blogging/#atom-everything":
        "Simon Willison 分享今年 1 月接受 Cynthia Dunlop「Write that blog!」系列访谈的链接，谈了为什么写博客、写博客带来的意外影响，以及给新手博主的建议。",

    # 2026-08-07 arXiv 新论文
    "http://arxiv.org/abs/2608.06377v1":
        "提出 MIST 基准与 SC2W 指标衡量模型是否会被误导性上下文带偏，并用 SCOPE 方法在干净/误导/正确上下文/无关上下文四类匹配条件上做均衡 DPO 训练，在降低误导敏感度的同时保持对可信上下文的利用能力。",
    "http://arxiv.org/abs/2608.06370v1":
        "在 BFCL v4 上对比程序化工具调用（用 Python 代码而非 JSON 调用工具）与传统 JSON 工具调用，14 个模型中 11 个表现持平或更优，GPT-5.6 系列提升达 10.6%，且在并行调用与长上下文退化场景下更稳健。",
    "http://arxiv.org/abs/2608.06366v1":
        "提出可溯源的心衰电子病历特征工程多智能体系统 nMAS，自动生成 132 个结构化特征与 70 个规则打分特征，将 HFrEF/HFpEF 表型判别 AUROC 分别提升至 0.963 和 0.910。",
    "http://arxiv.org/abs/2608.06362v1":
        "将方差缩减工具 AIVAT 与「随时有效置信序列」结合成 AV-AIVAT，用于德州扑克等不完全信息博弈中的 Agent 强弱评测，相比原始结果所需对局数中位数减少 74 倍，且可随时安全停止并保留统计有效性。",
    "http://arxiv.org/abs/2608.06361v1":
        "通过弹球撞墙、眨眼、状态切换三类可控视频任务系统评测视频语言模型的事件计数能力，发现 Gemini 3.6 Flash 在高频高数量场景下最终计数准确率仅 0.2%，提高采样率能拉高准确率，但事件序列本身的还原忠实度仍很低。",
    "http://arxiv.org/abs/2608.06353v1":
        "提出面向已部署 AI Agent 的持续参与式治理机制设计模型，通过治理货币出资、双阈值滞后授权门与硬件签名算力许可，把「治理权」转化为对算力预算的自我强制性控制。",
    "http://arxiv.org/abs/2608.06352v1":
        "提出 CalibForge 自主终端任务合成系统，通过多/对比求解器的「对抗式求解器校准」筛选出难度恰当的可执行终端任务，构建 5431 个校准任务后训练模型在 Terminal-Bench 2.0、SWE-bench Pro、Doc2Repo 上分别取得最高 24.71、27.68、30.04 个百分点的提升。",
    "http://arxiv.org/abs/2608.06347v1":
        "提出「推理枢轴」引导的在线自蒸馏方法 RP-OPSD，聚焦决定推理走向的关键 token（推理枢轴）而非全部 token 做特权蒸馏，在覆盖 17 种语言的数学推理基准上超过现有多语言推理迁移与 OPSD 变体基线。",
    "http://arxiv.org/abs/2608.06346v1":
        "提出长时程 Agent 轨迹错误溯源框架 TrajDebug，通过多粒度历史压缩与证据定位追踪每个错误的演化与最终影响，并构建 486 条人工标注失败轨迹的 TrajErrBench 基准，在多个 Agent 基准上取得最优错误定位效果。",
    "http://arxiv.org/abs/2608.06331v1":
        "提出交互式神经符号系统 TYTAN，结合数据库符号分析与 LLM 语义推断，自动从关系数据库构建分析用语义 Schema，遇歧义会向用户提问，八个数据库测试中实体/属性覆盖率达 100%，语义角色与专家标注一致率 92-100%。",
    "http://arxiv.org/abs/2608.06329v1":
        "提出无需参考答案、用 LLM 裁判评估对话式 Agent 基准本身质量（一致性、复杂度、策略覆盖度）的框架，并验证其能与人工标注一致，可用于诊断合成或人工构建基准的缺陷。",
    "http://arxiv.org/abs/2608.06312v1":
        "提出首个面向国家标准文档（如中国 GB/T 标准）结构化审查的基准 GB/T-Bench，含 25 类可诊断错误、7306 条可追溯审查错误实例，最强 LLM 得分 0.328 远低于专家的 0.664，提出的多 Agent 框架 GB/T-Reviewer 将最佳成绩提升到 0.509。",
    "http://arxiv.org/abs/2608.06310v1":
        "发现生成式奖励模型的比较式本质与现有 RL 标量打分范式不匹配，提出基于排序构建奖励的 RRC 方法（自比较排序 + 锚点引导排序），在开放对话与推理基准上显著提升生成式奖励模型驱动的 RL 训练效果。",
    "http://arxiv.org/abs/2608.06305v1":
        "在 780 页政府财报上证明传统「切块-嵌入-Top-K」检索对表格密集型长文档结构性失效（86.8% 内容是表格行，数字常与表头单位隔开 13 行），提出免嵌入的 Agent 式检索系统 READ，用词法检索+结构导航+定长读取三种确定性操作，准确率 58.8% 远超密集检索的 15.7%。",
    "http://arxiv.org/abs/2608.06301v1":
        "提出评测 LLM 自动优化「Agent 系统 harness」（提示词、工具、记忆、编排代码）能力的基准 HarnessOpt-Bench，在受信执行环境下用留出测试集评分，5 个前沿模型 111 次运行结果显示优化器能力差异远大于所用编码 harness 本身的差异。",
    "http://arxiv.org/abs/2608.06296v1":
        "提出无监督在线自蒸馏方法 U-OPSD，仅用模型自身多次采样通过自一致性多数投票构造伪解，再蒸馏纠正最长错误补全，在 AIME24/25、HMMT25 等基准上 Qwen3 4B/8B 非思考模式提升 8.5%-10.7%，媲美甚至超过有监督的 OPSD/GRPO。",
    "http://arxiv.org/abs/2608.06294v1":
        "提出量子增强时序模型 QuanTiMedAI，结合 Agentic LLM 做临床特征发现与紧凑量子循环网络做时序心脏骤停死亡率预测，在 MIMIC-IV 队列上仅用 605 个参数取得 0.852 的 AUROC，比现有最优基线提升约 2.9%。",
    "http://arxiv.org/abs/2608.06292v1":
        "提出神经符号 RAG 框架 NeSy-RAG，把检索到的文本块转成可归因的 Prolog 谓词模块并组合查询，同时引入符号化知识缺口检测主动追问用户缺失信息，在 ShARC 基准上零领域训练达到 61.1% 准确率，远超同模型 RAG 基线的 42.8%。",
    "http://arxiv.org/abs/2608.06283v1":
        "提出子梯度驯化 Langevin 采样算法 SG-TULA，直接在非光滑、超线性增长、非凸的势函数上做无需平滑处理的稳定采样，并在 GPT-2 系语言模型正则化预训练任务上验证其与 AdamW、Muon 微调具有竞争力的非渐近收敛保证。",
    "http://arxiv.org/abs/2608.06270v1":
        "通过因果图与三层干预审计多模态 LLM 的「看图思考」（裁剪缩放等视觉工具调用）能力，发现六个模型普遍存在「调用但未真看」和「看了但未规划」两种失配模式，整体准确率提升其实集中在一小部分「校准良好」的样本上，即视觉工具使用大多并非真正因果有效。",
    "http://arxiv.org/abs/2608.06265v1":
        "针对医疗合成基准「能过效用检查却仍不真实」的问题，提出在保持下游效用底线的约束下改进真实感的方法，在基于 Synthea 生成患者的护理缺口基准上，两种确定性修订大幅提升缺失结构、可操作行数比例等真实感指标，而简单密集化处理仍保留虚假模板痕迹。",
    "http://arxiv.org/abs/2608.06253v1":
        "提出代谢组学专用大语言模型 MetaboLLM（持续预训练+微调+结构化检索）及配套图神经网络 MetaboLLM-GIN，将模型生成的生化描述转为代谢物图用于患者级预测，在冠脉搭桥术后应激性高血糖预测（AUC 0.8616）和绝经后激素方案分类（AUC 0.8123）上超越传统模型。",
    "http://arxiv.org/abs/2608.06246v1":
        "提出按机制、目标、数据需求、持久性、结构范围、模型类型六个维度系统梳理微调、参数高效适配、对齐、检索增强、模型编辑、遗忘等训练后适配技术的分类法，用于支持模型变更追踪与 AI 治理分析。",
    "http://arxiv.org/abs/2608.06243v1":
        "针对在线自蒸馏（OPSD）对所有 token 局部散度一视同仁的问题，提出「散度自适应监督时域」DASH，依据每个 token 散度偏离序列均值的程度动态设置反向传播门控权重，在三个数学推理基准、三种模型规模上均稳定超过 OPSD 复现基线，且无需额外前向计算。",
    "http://arxiv.org/abs/2608.06227v1":
        "提出「全息数字孪生网络」（HDT-Net）框架，让数字孪生从被动镜像物理资产转变为主动推理的 Agent，通过因果马尔可夫毯确定协同边界、主动推理统一感知决策学习、范畴论保证跨异构 Agent 语义一致，为无线网络支撑物理世界实时 AI 协同提供理论架构。",
    "http://arxiv.org/abs/2608.06223v1":
        "提出面向时间序列预测的检索增强框架 TS-RAG，引入专门设计的参考 token 融合输入序列与检索到的相似历史序列信息，在多个真实世界预测基准上取得一致的最优表现。",
    "http://arxiv.org/abs/2608.06216v1":
        "综述持续学习从「参数为中心」向「系统级适配」转变的趋势，提出按「何时（预训练/后训练/推理时）、如何（离线策/在线策/超越梯度）、何处（内部参数 vs 外部记忆/技能库/交互协议）」三轴系统梳理持续学习方法演进。",
    "http://arxiv.org/abs/2608.06202v1":
        "用 BBQ 和 SafetyBench 两个安全基准共 401 条 prompt、4812 次响应，系统对比 ChatGPT 聊天界面与 OpenAI API、开启/关闭网页搜索四种条件下的表现，发现开启搜索可使准确率下降最多 8 个百分点甚至逆转模态优劣，同一 prompt 重复运行结果不一致比例最高达 21%。",
    "http://arxiv.org/abs/2608.06197v1":
        "提出「世界排演」式 Agent 强化学习方法 EnvACE，让策略模型交替扮演行动者和环境角色，用自生成的环境响应替代昂贵的真实/合成环境交互进行端到端联合优化，在 BFCL-v4、tau²-Bench 等基准上超越环境扩展基线，测试时还可先做「私下排演」进一步提升表现。",
    "http://arxiv.org/abs/2608.06196v1":
        "在 690 个技能构成的技能库上对比「混合排序检索」与「类型化知识图谱」两种 Agent 技能检索方案，发现混合排序器 top5 命中率达 73.5%，而按设计意图使用图谱反而显著更差（-11.2 个百分点），因为图谱候选边本就来自排序器已搜索过的嵌入邻域，未能扩展检索覆盖范围。",

    # 2026-08-11 OpenAI / Simon Willison
    "https://openai.com/index/building-an-ai-native-finance-function":
        "OpenAI CFO Sarah Friar 分享打造 AI 原生财务团队的五条经验，涵盖自动化预测、更强内控与 AI 投资回报评估。",
    "https://openai.com/index/responsible-ai-infrastructure-texas":
        "OpenAI 致信德州州长 Greg Abbott，阐述其在德州负责任建设 AI 基础设施的承诺，支持透明、可靠且惠及德州民众的增长。",
    "https://openai.com/index/model-ml":
        "金融软件公司 Model ML 借助 GPT-5.6 Sol，将财务研究分析自动串联为可编辑、可追溯的 PPT 和 Excel 成果。",
    "https://openai.com/index/putting-frontier-cyber-models-in-more-trusted-hands":
        "OpenAI 让通过 Daybreak 审核的合作伙伴使用其前沿网络安全模型，为客户提供经授权、受治理的网络安全服务。",
    "https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows":
        "OpenAI 推出网络安全专用模型 GPT-5.6-Cyber，通过 Daybreak Red 提供给授权方用于漏洞研究、漏洞利用验证和安全测试。",
    "https://openai.com/index/premium-seats-chatgpt-business":
        "ChatGPT Business 即将推出高级席位（Premium seats），8 月 20 日前报名可获 100 美元工作空间额度并解锁更高用量上限。",
    "https://openai.com/index/responding-next-frontier-critical-cyber-capabilities":
        "OpenAI 公布 Astra 模型的初步网络安全评估结果，并说明正在采取的强化防护和安全管控措施。",
    "https://openai.com/index/hsp-gruppe":
        "税务咨询公司 HSP GRUPPE 介绍其如何用 ChatGPT Enterprise 提升生产力、改善工作质量并为税务咨询和客户服务腾出更多产能。",
    "https://simonwillison.net/2026/Aug/10/openclaw/#atom-everything":
        "Simon Willison 引用 OpenClaw 的安全研究：某澳大利亚健身房预订网站 API 对取消他人预约完全没有权限校验，借此候补排名从第 4 位跳到第 3 位。",
    "https://simonwillison.net/2026/Aug/9/claude-opus-5-system-prompt/#atom-everything":
        "Simon Willison 摘录 Claude Fable 5/Mythos 5 系统提示词片段：说明两模型曾因美国商务部出口管制于 6 月 12 日被暂停访问、7 月 1 日恢复，用于让模型如实回应相关提问。",
    "https://simonwillison.net/2026/Aug/9/github-models-is-now-retired/#atom-everything":
        "Simon Willison 记录 GitHub Models 服务正式退役：其 GitHub Actions 因此报错，并回顾了 GitHub Models 曾提供的跨 LLM 提供商统一 API 及 Actions 环境免配置调用的优势。",
    "https://simonwillison.net/2026/Aug/9/sqlite-text-history-prototype/#atom-everything":
        "Simon Willison 分享用 SQLite 存储修订历史的新想法原型：把每个历史版本全文存入 JSON 数组后整体做 zlib/zstd 压缩，利用重复字符串获得很好压缩率。",
    "https://simonwillison.net/2026/Aug/8/auto-mode/#atom-everything":
        "Simon Willison 报道 Anthropic 将从 8 月 14 日起把 Auto 模式设为 Claude Code Pro/Max/Team 新会话的默认设置，并引用 Anthropic 内部几乎所有人都在用 Auto 模式应对 prompt injection 风险的说法。",
    "https://simonwillison.net/2026/Aug/8/now-we-have-a-timeline-of-the-openai-accidental-attack-against-h/#atom-everything":
        "Simon Willison 评论 OpenAI 意外攻击 Hugging Face 事件的时间线，认为最有意思的细节是 5 月 7 日 OpenAI 启动的一次未发布实验模型训练任务与该事件的关联。",
    "https://simonwillison.net/2026/Aug/8/john-gruber/#atom-everything":
        "Simon Willison 引用 John Gruber 回应其博客写作建议的比喻：写作更像现场演奏而非录制专辑，追求专业但不要求每篇都是精品。",
    "https://simonwillison.net/2026/Aug/7/openai-timeline/#atom-everything":
        "Simon Willison 依据 OpenAI 在 Black Hat 大会发布的视频，整理出 Hugging Face 攻击事件的完整时间线，指出 OpenAI 是在请求撤销自身凭证时才发现自己是攻击方。",
    "https://simonwillison.net/2026/Aug/7/moonlight-mayhem/#atom-everything":
        "Simon Willison 用同一份「浣熊抢劫」游戏创意分别喂给 Claude Fable 5 与 Codex Desktop（GPT-5.6 Sol Ultra 多子智能体模式），后者做出的 Moonlight & Mayhem 游戏效果更好，代码与素材已开源。",
    "https://simonwillison.net/2026/Aug/7/pdfs-are-terrible/#atom-everything":
        "Simon Willison 转发 404 Media 报道：埃森哲内部录音显示，推动企业 AI token 消耗暴涨的其实主要是非工程岗位员工的使用行为，而非工程师。",
    "https://simonwillison.net/2026/Aug/6/datasette-auth-tokens/#atom-everything":
        "Simon Willison 发布 datasette-auth-tokens 0.4a13，更新以兼容 sqlite-utils 4.x。",

    # 2026-08-12 OpenAI / Simon Willison
    "https://openai.com/index/daybreak-models-are-now-available-on-aws":
        "OpenAI 与 AWS 合作，通过 Amazon Bedrock 提供 Daybreak 网络安全能力，支持企业安全工作流。",
    "https://openai.com/index/zapier":
        "Zapier 企业营销团队用 ChatGPT Work 减少销售线索流失、制作campaign素材并自动生成报告。",
    "https://openai.com/index/virgin-atlantic/chatgpt-work":
        "维珍航空借助 ChatGPT Work 加速研究、产品规划和决策，帮助团队串联客户旅程中的各类信号。",
    "https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/#atom-everything":
        "Simon Willison 转引 Sophie Alpert 关于工程师使用 AI 辅助写作的内部规范：文档中每句话都必须是作者真正认可的想法，不能用「AI 写的，别在意」当借口，因为自然语言的改写从来不是无损转换。",
    "https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything":
        "Simon Willison 介绍一篇论文：Anthropic、OpenAI、Google 返回给客户端的加密思维链可在会话/用户/模型间被重放，作者将强模型的推理轨迹重放进较弱的同系列模型并越狱，从而以明文窃取强模型的隐藏推理内容。",
    "https://simonwillison.net/2026/Aug/11/datasette-upload-dbs/#atom-everything":
        "Simon Willison 发布 datasette-upload-dbs 0.5a0：新增正式 API，可通过 curl 上传/替换 Datasette 托管的 SQLite 数据库，支持在 GitHub Actions 等环境中构建新库后原子替换。",
    "https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything":
        "Simon Willison 点评 Meta 重返开放权重阵营发布的 Muse Glimmer：30B 参数、Apache 2.0 许可，针对端到端 Agent 任务完成、可靠工具调用和多步推理做了优化，在 SWE-Bench 等基准上表现不错。",

    # 2026-08-14 Google DeepMind / OpenAI / Simon Willison
    "https://deepmind.google/blog/introducing-gemini-3-7-flash/":
        "Google DeepMind 发布 Gemini 3.7 Flash：在 3.6 Flash 基础上做算法改进（非重新预训练），编程、知识工作和网页开发能力明显提升，起售价降至每百万输入 token 0.75 美元。",
    "https://openai.com/index/builders-guide-to-gpt-5-6":
        "OpenAI 发布 GPT-5.6 开发者指南，介绍创业公司如何借助更智能的模型选择和新版 Responses API，用 GPT-5.6 更快、更省成本地构建 AI Agent。",
    "https://openai.com/index/previewing-ultrafast":
        "OpenAI 预告 Ultrafast：由 Cerebras 提供算力的新 API 服务层，可让 GPT-5.6 Sol 运行速度提升至 14 倍，输出速率最高达每秒 750 个 token。",
    "https://openai.com/index/dali-rajic-chief-revenue-officer":
        "OpenAI 任命 Dali Rajic 为首席收入官，负责领导全球收入组织，帮助企业客户充分释放 AI 的商业价值。",
    "https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/":
        "Google DeepMind 推出手语转文字模型 SL2T，为听障与重听用户提供全新的手语识别功能。",
    "https://openai.com/index/how-enterprises-put-ai-to-work":
        "OpenAI 研究揭示企业采用 Agentic AI 的现状：使用 ChatGPT 和 Codex 的前沿企业正在 AI 落地速度上明显领先同行。",
    "https://openai.com/index/ringcentral":
        "RingCentral 借助 ChatGPT Work 和 Codex 加速 AI 产品研发，并在工程与运营团队之间集中管理运营情报。",
    "https://simonwillison.net/2026/Aug/13/sqlite-utils-2/":
        "Simon Willison 发布 sqlite-utils 4.2.1，修复 4.2 版本中因缺少 typing-extensions 依赖导致的崩溃 bug，并补充了不依赖 dev 依赖组的烟雾测试方法。",
    "https://simonwillison.net/2026/Aug/13/sqlite-utils/":
        "Simon Willison 发布 sqlite-utils 4.2，围绕 table.transform() 功能做了大量改进，更好地保留 check 约束、唯一约束和列注释等边缘情况的表结构定义。",
    "https://simonwillison.net/2026/Aug/13/llm-gemini/":
        "Simon Willison 发布 llm-gemini 0.33，新增对 Gemini 3.7 Flash、3.6 Flash、3.5 Flash-lite 及两个嵌入模型的支持，并升级以配合 LLM 0.32 显示推理轨迹和服务端工具调用。",
    "https://simonwillison.net/2026/Aug/13/alchemy-utils/":
        "Simon Willison 发布 alchemy-utils 0.1a1，提升了 DuckDB 导出和 CSV 导入的性能。",
    "https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/":
        "Simon Willison 介绍 DeepSeek V4 Pro 0813（经 OpenRouter 提供 API），指出其权重可能随后开源，并观察到该模型在不同推理强度下生成的鹈鹕图案差异明显大于其他模型。",
    "https://simonwillison.net/2026/Aug/12/alchemy-utils/":
        "Simon Willison 用 Codex 和 GPT-5.6 Sol Ultra 做「淋浴间项目」调研，探索基于 SQLAlchemy、兼容 sqlite-utils 核心 API、可跨 PostgreSQL/SQLite/DuckDB 使用的数据库无关工具库原型 alchemy-utils 0.1a0。",
    "https://simonwillison.net/2026/Aug/12/florian-herrengt/":
        "Simon Willison 引用 Florian Herrengt 文章片段：团队过度依赖 AI 修复 bug 和讲解代码来源，导致系统复杂到无人真正理解，反映「AI 正在消灭软件工程中间层」的现象。",

    # 2026-08-14 arXiv 新论文
    "http://arxiv.org/abs/2608.13560v1":
        "AutoDesign 提出元 Harness 优化框架：由元优化器指导代码 Agent 根据 rollout 反馈递归改进任务执行框架，在论文转海报生成任务上得分 78.32，超过 Claude Design 等闭源商业系统 7.45 分。",
    "http://arxiv.org/abs/2608.13558v1":
        "OmniScientist 是全模态、多学科的端到端 AI 科学家系统，可直接对图像、信号、音频、视频、三维结构等原始异构证据推理，在 36 个真实数据案例上全部走完从数据到成稿的完整流程。",
    "http://arxiv.org/abs/2608.13555v1":
        "HumanTracker 提出更贴合人类感知的人形运动跟踪评测基准，含约 153 小时动捕数据，并训练出比传统运动学误差更能识别脚滑、接触失误等物理瑕疵的 HumanScore 指标。",
    "http://arxiv.org/abs/2608.13547v1":
        "QuoteBench 揭示 LLM Coding Agent 生成的 Bash 命令在经过序列化/转义等执行链路后可能悄悄失败：仅看「匹配得分」会掩盖命令生成与执行传输层引入的错误差异达 55-73 个百分点。",
    "http://arxiv.org/abs/2608.13545v1":
        "LittleLearner 构建仅含小学阶段知识的 880 亿 token 纯净预训练语料库，训练出能力边界可被课程标准精确刻画的 50 亿参数模型，用于研究知识获取的可控实验环境。",
    "http://arxiv.org/abs/2608.13538v1":
        "SAEVerbalizer 把稀疏自编码器（SAE）的特征方向直接注入 LLM 表示并微调模型，让模型能用自然语言直接解释 SAE 特征含义，且可泛化到未见过的特征和不同模型。",
    "http://arxiv.org/abs/2608.13522v1":
        "Vero 是首个在仓库级别同时评测代码实现与形式化证明合成能力的基准，覆盖 Python、Dafny、Verus、Coq 等 43 个多模块真实项目实例，最强 Agent 也仅完全解出 27/43。",
    "http://arxiv.org/abs/2608.13517v1":
        "DFM Mimir v1 是基于层级推理模型（HRM）架构、仅用合规许可数据训练的 10 亿参数模型，在英语上表现有竞争力，丹麦语上创下新的 SOTA，可与更大的 Qwen 3.5 4B 等模型抗衡。",
    "http://arxiv.org/abs/2608.13515v1":
        "论文提出一种不依赖具体下游任务的训练数据影响力度量方法，分析 Pythia 系列模型发现：预训练早期文学类数据影响更大，后期则转为 STEM 数据主导。",
    "http://arxiv.org/abs/2608.13513v1":
        "TabSOM 提出基于自组织映射（SOM）的表格数据转图像编码方法，在保留特征间关系信息的同时生成可解释图像表示，在 12 个基准数据集上排名第一或第二。",
    "http://arxiv.org/abs/2608.13510v1":
        "论文从信息论、交互建模和随机动力学角度系统分析机器学习决策系统的结构性极限，指出预测能力受限于数据生成过程本身而非算法复杂度，并将 LLM Agent 架构类比为反馈驱动的随机过程。",
    "http://arxiv.org/abs/2608.13505v1":
        "Intern-S2-Preview 是面向科学发现的多模态 Agent 基础模型系列，397B 参数版本在科学、多模态、Agent 及通用基准上取得有竞争力甚至领先的成绩，并支持时间序列建模和记忆增强扩展。",
    "http://arxiv.org/abs/2608.13495v1":
        "TraVEL 提出轨迹引导的驾驶视频embedding学习框架，用自车轨迹相似度作为强化学习奖励微调 Qwen3-VL-Embedding，显著提升转向、加减速等运动敏感场景的检索精度。",
    "http://arxiv.org/abs/2608.13492v1":
        "AlayaWorld 技术报告 v1.1 版重新设计交互式长时程世界模型的条件信号表示：用流式三维点缓存渲染器替代深度扭曲空间记忆，并统一视觉条件与生成内容的因果 VAE 潜空间表示。",
    "http://arxiv.org/abs/2608.13484v1":
        "论文从 Grice 会话准则角度研究 LLM 在遇到知识边界外实体时为何倾向编造具体细节而非退到更安全的泛化表述，发现模型内部已具备判断知识边界和预知指称具体度的信号，但生成策略未能利用这些信号做出「Grice 式退让」。",
    "http://arxiv.org/abs/2608.13482v1":
        "论文提出 Synthetic Persona Pretraining（SPP）：在预训练阶段（而非训练后才做对齐）就为模型注入价值观人格，实验显示越早引入、绑定 Assistant 身份，越能提升宪法遵循度和越狱鲁棒性，且优势随预训练规模增大。",
    "http://arxiv.org/abs/2608.13476v1":
        "MARC v1 是面向临床推理的开源多 Agent 协作框架，用确定性多 Agent 编排替代单一大模型 Prompt，支持按阶段追溯失败原因，并能从纯文本描述自动生成任务专属 Agent Prompt。",
    "http://arxiv.org/abs/2608.13472v1":
        "AaLLM 是开源的端到端模拟电路设计多 Agent 框架，涵盖拓扑生成到器件尺寸设计全流程，用 RAG 构建电路设计知识库，并通过 Designer/Critic/Evaluator 三 Agent 反馈系统减少迭代次数，推理耗时比现有方法快 40 倍。",
    "http://arxiv.org/abs/2608.13463v1":
        "ARMDIL 用多模态大模型作为路由器，为每张图片动态选择最合适的视觉骨干网络（CNN/自监督/VLM），在跨领域图像分类任务上媲美专门训练的路由器，且可通过修改 Prompt 快速适配新场景。",
    "http://arxiv.org/abs/2608.13459v1":
        "CAPRI 提出面向 Isabelle 定理证明修复的「契约感知」工作流：用独立检查器确保 LLM 只修改开发者授权范围内的证明内容，在 12 个失败证明、180 次运行测试中发现仅有极少数越权修改案例。",
    "http://arxiv.org/abs/2608.13456v1":
        "论文从因果视角统一梳理世界模型（World Models）研究，主张有用的世界模型需超越生成能力，还要捕捉实体属性、实体间交互及环境动态背后的因果结构，并结合可识别性理论说明何时能从数据中恢复这些结构。",
    "http://arxiv.org/abs/2608.13453v1":
        "UniTexture 提出跨任务的通用对抗纹理攻击：用单个带纹理的三维物体即可让 VLA 机器人策略模型在多个操作任务上产生攻击者指定的动作偏移，将任务成功率从 90% 降至 48.4%，且可跨模型迁移。",
    "http://arxiv.org/abs/2608.13450v1":
        "论文研究用 LLM 自动为自动驾驶软件栈（Autoware）生成可执行测试用具以动态验证攻击可达的安全弱点，发现 80% 的首次编译失败源于依赖装配而非程序逻辑，构建集成而非漏洞生成/模糊测试才是主要瓶颈。",
    "http://arxiv.org/abs/2608.13428v1":
        "RAIL 提出统一的 AI 成熟度九级量表（AIRL），并设计由多个独立 LLM 专家 Agent 组成的评审团分类器，自动从自然语言描述判定 AI 研究/项目的成熟度等级，避免单一 LLM 分类器的高估问题。",
    "http://arxiv.org/abs/2608.13426v1":
        "Reduced Matrix Multiplication（RMM）是一种免训练、输入自适应的推理加速方法，通过在矩阵乘法的收缩维度上选择性保留信息切片来降低 Transformer 推理成本，发现 Attention 部分比 MLP 部分更容易被削减而不掉点。",
    "http://arxiv.org/abs/2608.13420v1":
        "论文探索用小语言模型（SLM）在边缘计算设备上支持虚拟 Agent 的「思考」与「记忆」认知模块，在 NVIDIA Jetson Orin NX 上用不同规模 Qwen2.5 模型评测路由准确率、记忆读取性能和延迟。",
    "http://arxiv.org/abs/2608.13417v1":
        "论文提出超越最终分数的长时程 AI 研发 Agent 系统评测框架，在 36 个长时程任务上评测 7 个前沿模型，发现当前 Agent 更像「工程优化器」而非真正自主研究者：方案主要是改良已有技术，真正的方法论创新很少见。",
    "http://arxiv.org/abs/2608.13415v1":
        "Deliberate Practice 提出在有限练习预算下自主学习机器人技能的主动学习算法，通过双线性规划精确计算「预算最优」的技能练习分配方案，在长时程操作任务中提升机器人的整体规划表现。",
    "http://arxiv.org/abs/2608.13394v1":
        "论文针对 6G AI 原生网络中异构 AI Agent 的语义通信场景，提出「异构感知信念同步」框架：用部署在边缘服务器的潜空间翻译模型对齐不同 Agent 的信念，在无需联合训练的情况下降低同步开销和知识漂移。",
    "http://arxiv.org/abs/2608.13389v1":
        "TopoIntent 把安全意图自动编译为可执行、可合规检查的网络拓扑：通过模板检索和分阶段融合从自然语言需求生成拓扑，并导出为 Mininet 脚本进行可达性和访问控制测试，在保留集上将 CIS 合规满足率从 0.78 提升到 1.00。",
    # 2026-08-15 Simon Willison / Sebastian Raschka / GitHub Trending
    "https://simonwillison.net/2026/Aug/15/sighting-391300422/":
        "Simon 分享观鸟随笔：在加州 Pillar Point 港口偶遇 Morris —— 太平洋地区已知唯一一只北方塘鹅，14 年前首现于法拉隆群岛，如今已是当地名鸟。",
    "https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/":
        "Simon 介绍 Doug Turnbull 的博客打标签技巧：让 LLM 在不知道现有标签体系的情况下自由「幻想」标签，再用向量嵌入匹配语料库中最接近的既有标签，从而在标签过多（1856 个）时也能高效分类。",
    "https://magazine.sebastianraschka.com/p/ai-detector-from-scratch":
        "Sebastian Raschka 分享从零构建 AI 文本检测器的完整实战项目，涵盖数据集构建、模型训练、本地部署，并用到 RLVR（可验证奖励强化学习）技术。",
    "https://github.com/public-apis/public-apis":
        "public-apis：汇集大量免费公共 API 的合集仓库，方便开发者查找可直接调用的各类接口。",
    "https://github.com/cordiverse/cordis":
        "cordis：支持时空可组合性的元框架，用于构建插件化、可跨场景协同的应用架构。",
    "https://github.com/MakazhanAlpamys/Soup":
        "Soup：仅用一份 YAML 配置即可微调 LLM，通过分层流式加载技术可在 4GB 显存的笔记本 GPU 上训练 8B 参数模型。",
    "https://github.com/ToolJet/ToolJet":
        "ToolJet：开源企业级应用生成平台的基础项目，用于构建内部工具、仪表盘、业务系统、工作流和 AI Agent。",
    "https://github.com/cursor/plugins":
        "Cursor 插件规范与官方插件仓库，定义了 Cursor 编辑器插件的开发标准与实现示例。",
    "https://github.com/citrolabs/ego-lite":
        "ego-lite：专为 AI Agent 浏览器自动化打造的高速浏览器，可将已登录的浏览器状态共享给 Codex、Claude Code 等 Agent，无需额外配置和费用。",
    # 2026-08-16 Simon Willison
    "https://simonwillison.net/2026/Aug/15/cors-chat/":
        "Simon 用 GPT-5.6-Sol xhigh 一天写出 CORS Chat 工具：为在 LM Studio（M5 MacBook Pro / NVIDIA DGX Spark）上测试 Qwen 3.8 27B 等本地模型提供网页聊天界面，兼容 OpenAI Responses 格式，对话可导出 JSON，还能在流式输出时逐步渲染生成中的 SVG 图片。",
    # 2026-08-17 OpenAI / Simon Willison / GitHub Trending
    "https://openai.com/index/the-defenders-window":
        "文章探讨 AI 如何同时重塑攻防两端的网络安全格局，介绍 OpenAI 如何加强自身防御，以及安全团队现在可以采取的行动。",
    "https://openai.com/index/openai-joins-ports-pike-project":
        "OpenAI 宣布加入 PORTS-Pike 项目，扩大社区投资，支持俄亥俄州南部数千个就业岗位。",
    "https://openai.com/index/new-policy-ideas-for-the-intelligence-age":
        "OpenAI 资助 14 个独立项目，探索能在智能时代扩大经济机会、增强社会韧性的新政策构想。",
    "https://simonwillison.net/2026/Aug/16/markdown-svg-upgrades/":
        "Simon 升级了他的 markdown-svg-renderer 工具，用于分享包含 SVG 图片的 Markdown 转录内容，可粘贴文本或指向 CORS 友好 URL/GitHub Gist 生成可收藏链接。",
    "https://simonwillison.net/2026/Aug/16/qwen-38-27b/":
        "Simon 测评阿里 Qwen 团队新发布的 Apache 2 协议、27B 参数视觉多模态模型 Qwen 3.8 27B，认为效果优秀，但默认会过度思考。",
    "https://simonwillison.net/2026/Aug/16/dario-amodei/":
        "Simon 引用 Anthropic CEO Dario Amodei 的观点：公众对 AI 的负面看法根源是对企业和科技行业普遍存在的信任危机，而非 AI 领袖们的风险警告，真正的解药是拿出实际成果而非营销包装。",
    "https://github.com/agalwood/Motrix":
        "Motrix：功能全面的开源下载管理器，支持多协议下载任务管理。",
    "https://github.com/nautechsystems/nautilus_trader":
        "nautilus_trader：生产级 Rust 原生量化交易引擎，采用确定性事件驱动架构。",

    # 2026-08-18 OpenAI / Simon Willison / arXiv
    "https://openai.com/index/chatgpt-for-teens":
        "OpenAI 推出面向青少年的 ChatGPT for Teens，帮助青少年学习和批判性思考，内置更强防护、健康使用功能及家长管控选项。",
    "https://openai.com/index/partnering-with-codeai":
        "OpenAI 与 CodeAI 合作，帮助学生建立 AI 素养、批判性看待 AI，并培养负责任使用和塑造 AI 的能力。",
    "https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/":
        "Simon 指出 Qwen 3.8 27B 在 Artificial Analysis 智能指数上拿到 52 分，与 GPT-5.6 Luna（max）持平，仅落后 753B 参数的 GLM-5.2 和 1.7T 参数的 DeepSeek V4 Pro 一分，认为这个 27B 模型表现惊人。",
    "https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/":
        "Simon 转发 404 Media 的调查报道：书商收到疑似 AI 公司大批量收购稀有书籍用于训练的订单，记者在书中藏入 AirTag 追踪，最终发现货物送到了亚马逊的 AI 训练设施。",
    "http://arxiv.org/abs/2608.16319v1":
        "Prior Labs 开源三件关系型学习工具：统一评测框架 RelArena-α、当前排名第一的关系型模型 TabPFN-Rel，以及模型无关的关系预测接口 RPI，推动关系型学习的可复现研究。",
    "http://arxiv.org/abs/2608.16889v1":
        "提出 BATON 框架，把长时程机器人操作按子任务拆分探索并配合「转换感知记忆」，将指数级探索成本降为线性，在 RoboMemArena 基准上任务成功率提升 11.6%。",
    "http://arxiv.org/abs/2608.16876v1":
        "AutoSR 用「研究状态」保留符号回归过程中的推理与证据，结合渐进加宽蒙特卡洛树搜索让 AI 从单纯拟合公式转向自动化科学探究，在多个基准上恢复出等价关系式。",
    "http://arxiv.org/abs/2608.16852v1":
        "研究发现现有合规检测器（Activation Probe / Guard Model）存在「规则盲视」——删除或替换所依据的规则并不影响其判断准确率，作者提出免训练的 Internal Compliance Score 用于审计。",
    "http://arxiv.org/abs/2608.16844v1":
        "提出 Proteus 机制：让长上下文记忆模型的有效容量随上下文增长而逐步扩大而非全程静态，减少早期 token 对记忆的「污染」，在多个记忆架构上一致提升长上下文效果。",
    "http://arxiv.org/abs/2608.16837v1":
        "提出 HAF 框架，通过分层动作流生成与频谱隐空间强化学习，把通用视觉-语言-动作基础模型适配到人形机器人全身移动操作任务，在七项真实任务中超过单阶段 VLA 基线。",
    "http://arxiv.org/abs/2608.16834v1":
        "研究发现 AI 模型普遍存在「模型催眠」现象：提示词中看似无关的弱线索组合起来可强力操控模型行为，且能跨模型迁移，对 AI 安全和可解释性构成新挑战。",
    "http://arxiv.org/abs/2608.16831v1":
        "提出 Policy Iteration with Human Feedback（PIHF），用语言模型评论家与专家评审持续修订自然语言策略而非微调权重，在罕见病诊断基准上显著提升多个执行模型的 Recall@1。",
    "http://arxiv.org/abs/2608.16824v1":
        "构建 GEOFlagBench 基准评测生成式引擎优化（GEO）内容检测方法，提出 Intervention-Paired Training 提升检测器鲁棒性，并在真实搜索结果中估算 GEO 内容占比约 8.9%。",
    "http://arxiv.org/abs/2608.16813v1":
        "提出 Quipu：一个面向 Agent 写入场景的「受治理双时态知识图谱」存储系统，通过写入门控、双时态记录和可组合信任格，解决传统知识图谱在多写入者场景下的治理缺陷。",
    "http://arxiv.org/abs/2608.16806v1":
        "文章分析大语言模型驱动的具身 Agent 中，场景状态信息可能成为新的攻击面，梳理了 SayCan、Code as Policies、VoxPoser 等技术路线下状态语义注入的风险。",
    "http://arxiv.org/abs/2608.16804v1":
        "研究用迁移学习与 TA3N 域自适应方法进行手语识别，发现域自适应比传统神经网络迁移更有效，尤其在对齐较短时间尺度特征时能显著提升美国手语识别效果。",
    "http://arxiv.org/abs/2608.16801v1":
        "通过 1902 次运行的时序网络分析多智能体编程协作中的协调模式，发现共享文件可替代重复通信、节省约 42% token，而指定协调者并不能带来可靠的成功率提升。",
    "http://arxiv.org/abs/2608.16798v1":
        "提出统一黑盒强化学习框架，通过沙箱隔离和代理服务器捕获模型调用，让 Agent 能在复杂 Harness（如 OpenClaw、Claude Code）中稳定训练，显著提升 Pass@1。",
    "http://arxiv.org/abs/2608.16795v1":
        "提出「历史回测」方法评估科学问题生成系统：用历史截止前语料生成问题，再用后续文献判定是否被解答，发现基于证据结构的生成方法优于纯 LLM 提示。",
    "http://arxiv.org/abs/2608.16794v1":
        "提出神经符号 Agent，将具身长时程任务拆分为「视觉探索获取符号状态」和「受约束的符号规划」两阶段，在 VirtualHome 和 ALFWorld 上以更小模型取得超过 90% 的成功率。",
    "http://arxiv.org/abs/2608.16776v1":
        "提出 GRIP 方法解决检索增强生成中的「查询主导」问题：让解码器保留完整查询信息，同时对检索证据施加信息瓶颈，将幻觉率降低 73%。",
    "http://arxiv.org/abs/2608.16775v1":
        "提出拓扑归因距离（TAD），用几何拓扑视角衡量检索证据对大模型输出的影响，为网络安全事件日志分析中的 RAG 可解释性和证据溯源提供工具。",
    "http://arxiv.org/abs/2608.16765v1":
        "构建 TRACE-Bench 基准，用「锚定-解耦-应用-组合」四种原子操作刻画多参考图像生成任务，发现当前模型的主要瓶颈在于属性解耦与绑定而非整体场景组合。",
    "http://arxiv.org/abs/2608.16763v1":
        "提出 LAVA 框架，用多模态大模型完成金融文档审计中的规则检索、版式保留信息抽取、元数据增强与可审计的符号验证，在幻觉控制和边缘案例处理上优于基线。",
    "http://arxiv.org/abs/2608.16760v1":
        "论文系统研究 Adam 优化器的收敛/发散相变及其在 Transformer 上优于 SGD 的 Hessian 结构成因，并据此提出显存减半、性能不减的新优化器 Adam-mini。",
    "http://arxiv.org/abs/2608.16747v1":
        "提出 CHIVE 流程，用反事实提示编辑自动挖掘并验证大模型行为的解释，发现现有可解释性技术对预测反事实行为并无提升，但用 CHIVE 生成的数据训练可泛化到分布外场景。",
    "http://arxiv.org/abs/2608.16742v1":
        "提出 TDD-Agent，把测试驱动开发范式引入代码生成：先让模型写测试再实现，并对代码与测试做迭代式双轨优化，在 LiveCodeBench 和仓库级基准 RepoEval 上均优于基线。",
    "http://arxiv.org/abs/2608.16739v1":
        "针对 LLM 强化学习中的价值函数方法，提出 Privileged Value Functions 和 TETHER 两种策略注入任务相关的 token 级信号，在多个推理任务上优于标准价值函数基线，媲美或超过 GRPO。",
    "http://arxiv.org/abs/2608.16733v1":
        "提出 GoalEvolve 框架，让物理设计算法的演化对齐最终多目标质量而非局部指标，通过定位关键瓶颈阶段指导 LLM 教师-学生 Agent 协同优化，在 ASAP7 设计上平均提升 TNS 30.67%。",
    "http://arxiv.org/abs/2608.16710v1":
        "提出 Ethical Decision Head，用强化学习从人类反馈中训练自动驾驶的伦理决策，发现功利主义模型学到的是人类评分者实际奖励的「自我牺牲」倾向，而非理论上定义的伦理规则。",
    "http://arxiv.org/abs/2608.16709v1":
        "提出 MIRROR 系统，将放射科报告生成拆分为分类器、Grad-CAM 定位器和不接触图像的报告撰写器，使报告结论可与概率向量对照审计，避免语言模型编造未测得的诊断结论。",
    "http://arxiv.org/abs/2608.16707v1":
        "提出「语义赌博机」研究大模型 Agent 探索-利用行为如何被动作标签的语义先验影响，发现语义信息会削弱探索、且负向奖励比同等正向奖励更能激发探索。",
    "http://arxiv.org/abs/2608.16686v1":
        "提出 AffectLoop 多模态情感感知对话机器人系统，让机器人同时追踪说话者情绪动态与自身情感状态并据此生成共情回应，试点实验显示比不建模双向情感的基线获得更好的共情评价。",
    "http://arxiv.org/abs/2608.16681v1":
        "针对遥感半监督语义分割，提出统一流（结合外部视觉基础模型与领域教师生成低偏差伪标签）与特征记忆库两项创新，缓解有标注数据主导训练导致伪标签质量下降的问题。",
    "http://arxiv.org/abs/2608.16666v1":
        "提出 Chronocooked 强化学习基准，用类似《煮糊了》的烹饪场景测试 Agent 在时间信息不可观测但对决策至关重要时的隐式时间感知能力。",
    # 2026-08-19 OpenAI / Simon Willison
    "https://openai.com/index/chatgpt-ads-expands-across-europe":
        "ChatGPT Ads 扩展至欧洲 31 个市场，帮助广告主在用户探索、比较和决策的过程中触达他们。",
    "https://openai.com/index/strengthening-democratic-oversight-in-national-security":
        "OpenAI 发起新计划，通过工具、培训和专业知识支持政府机构，加强国家安全领域 AI 使用的民主监督。",
    "https://openai.com/index/pacing-model-development-cyber-capabilities":
        "OpenAI 正在加强前沿模型的监控、对齐与安全防护，用新的安全措施来把控涉及网络安全相关能力的模型开发节奏。",
    "https://openai.com/index/nvidia/chatgpt-work":
        "NVIDIA 团队使用 ChatGPT Work 减少手动工作、连接快速变化的信号，并将行之有效的工作流推广到全球团队。",
    "https://openai.com/index/asana":
        "Asana 用 OpenAI Codex 在两周内替换了老旧的测试系统，完成了原本预计耗时五年、成本约 1.2 万美元的工程工作。",
    "https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/":
        "Mojo 编程语言正式开源：继上周发布 1.0 版本后，如今以 Apache 2 协议开源了编译器和工具链，兑现了自 2023 年以来的承诺；早先「成为 Python 超集」的目标已于 2025 年 8 月调整，转而依靠 AI 辅助编程工具帮助把 Python 代码迁移到 Mojo。",
    # 2026-08-22 DeepMind / OpenAI / Transformer Circuits / Simon Willison
    "https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games/":
        "Google DeepMind 回顾 15 年游戏 AI 研究历程，介绍与游戏工作室合作原型化突破性 AI 玩法的最新进展。",
    "https://openai.com/index/introducing-ai-futures":
        "OpenAI 推出新博客栏目 AI Futures，探讨变革性 AI 将如何重塑权力格局、治理方式、经济结构与个人自由。",
    "https://openai.com/index/stampli":
        "在临近固定截止日期且设计资源已分配给其他项目的情况下，Stampli 用 Codex 和 ChatGPT Work 把原本数周的发布筹备压缩到几天完成，启动耗时缩短 68%。",
    "https://openai.com/index/offering-zero-data-retention-for-frontier-models":
        "OpenAI 重申为符合条件的 API 客户提供零数据保留，并预告「私密安全处理」功能，在不牺牲数据隐私的前提下实现前沿 AI 安全防护。",
    "https://openai.com/index/replit":
        "Replit 推出由 GPT-5.6 Luna 驱动的免费模式，让用户无需担心 token 成本即可把想法变成可运行的软件。",
    "https://transformer-circuits.pub/2026/interference_effectiveness_helpfulness/index.html":
        "通过测量对模型输出和损失的影响，在一个单层 Transformer 中识别出「干扰权重」。",
    "https://simonwillison.net/2026/Aug/21/llm/":
        "llm 0.32.1 发布：修复因 OpenAI Python 库不再依赖 httpx 导致的新装失败问题，临时通过锁定 openai<3 解决，即将发布的 0.33 版本会改用 httpx2。",
    "https://simonwillison.net/2026/Aug/21/llm-openrouter/":
        "llm-openrouter 0.7 发布：适配 LLM 0.32，可显示通过 OpenRouter 使用的模型的推理过程；改用 OpenRouter 的 Responses API 实现，并新增 Shell、WebFetch、WebSearch 三个服务端工具。",
    "https://simonwillison.net/2026/Aug/21/stop-making-tuis/":
        "Simon 引述 Thomas Ptacek 的观点：既然编码 Agent 已经让做出一个够用的图形界面几乎零成本，就该为哪怕最小的个人工具构建真正的原生 UI，而不是满足于命令行工具。",
    "https://simonwillison.net/2026/Aug/21/matt-webb/":
        "引用 Matt Webb：发布 1.0 后本以为要自己手写旋转算法，结果用 ChatGPT 当耐心的一对一导师学会了四元数用法，说明借助 AI 思考并不会让学习停止，反而会推着自己学得更多。",
    "https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/":
        "Promptwatch 等「生成引擎优化（GEO）」产品通过自动化追踪 ChatGPT、Claude、Gemini 等聊天工具对同一提示的回复，其报告间接揭示了 ChatGPT 搜索如今已大规模使用 site: 语法。",
    "https://simonwillison.net/2026/Aug/20/bun-webview-json-api/":
        "Bun 1.4 正式发布，带来对 Node.js 测试套件的最大一次兼容性提升、修复超过 2900 个问题，并显著降低空闲 CPU 与内存占用；Simon 用其新 Bun.WebView 实现了一个 shot-scraper 风格的 JSON API。",
    "https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/":
        "Simon 让 Claude Fable 5（跑在 Claude Code for web 中）研究 smolmachines/smolvm 能否作为快速安全的沙箱，用来在限制 CPU/内存、无网络访问、仅可读写指定文件的条件下执行不受信任的 Python 和 JavaScript 代码。",
    "https://simonwillison.net/2026/Aug/19/jeremy-morrell/":
        "引用 Jeremy Morrell：LLM 大幅降低了编写扩展的成本，现代沙箱原语又降低了部署成本并提供了安全边界，因此 Web 应用可以做成稳固的核心加上由 LLM 填充的用户可扩展部分。",
    "https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/":
        "Simon 在 Talking Postgres 播客中谈「AI 如何改变软件开发」，重申自己一直在论证的观点：在编码 Agent 时代，用代码行数衡量生产力有时其实是有道理的。",
    # 2026-08-22 arXiv 论文
    "http://arxiv.org/abs/2608.20256v1":
        "让推理模型在响应开头自选 NoThink/Short/Long 三种模式，通过 GRPO 塑形奖励学会按题目难度自适应分配思考量，在 MATH500 上准确率基本不降的同时将平均响应长度削减 41%，且能零样本迁移到 GSM8K 等其他基准。",
    "http://arxiv.org/abs/2608.20195v1":
        "通过分析 557 次 Agent 编码会话和 3.3 万个 Agent PR 发现，Agent 阅读的文档六成是给 Agent 看的指令文件/工作笔记而非传统技术文档，且文档查阅与代码验证、测试之间的关联比预期弱，挑战了「可操作性与可验证性」是 Agent 友好文档核心属性的假设。",
    "http://arxiv.org/abs/2608.20153v1":
        "从 STOC/FOCS/SODA/COLT 2025-2026 论文构建 175 道端到端理论计算机科学研究基准（含专家验证的 Lean 形式化证明），发现自动形式化是最大瓶颈，最强模型仅得 11.5 分，自动生成的 64 个新命题中也只有 6 个通过专家评审。",
    "http://arxiv.org/abs/2608.20331v1":
        "提出面向患者的医学报告解读任务和 G-CARL 强化学习框架，用多源检索校验事实、用情境化加权清单保证回答覆盖度，在准确性和患者需求匹配度上均优于现有后训练基线。",
    "http://arxiv.org/abs/2608.20318v1":
        "构建 10 个训练算法家族的基准，让 Agent 在 4 小时内改写训练算法代码并重跑评估，结果最强系统也只弥补了原算法与最优解差距的不到五分之一，表明递归自我改进目前仍非常有限。",
    "http://arxiv.org/abs/2608.20281v1":
        "提出「注入-对齐-恢复」三阶段后训练框架，把固定文档语料转化为可用的参数化知识，无需检索即可回答文档相关问题，相比普通 SFT 平均提升领域问答准确率 3.6 个百分点、通用能力 12.1 个百分点。",
    "http://arxiv.org/abs/2608.20231v1":
        "建立后 AGI 经济模型：企业拥有既是生产者又是消费者的 AI/机器人 Agent 种群，论证零人类消费的封闭机器经济仍可实现正向最大增长率，GDP 将与人类福祉彻底脱钩，人类福祉最终只取决于对企业网络的所有权份额。",
    "http://arxiv.org/abs/2608.20204v1":
        "首个评估 LLM 合同「最终校对」能力的基准，由资深律师手工构造含定义误用、引用错误等问题的合同，结果前沿模型表现意外糟糕，最好的模型宏平均召回率也只有 0.75。",
    "http://arxiv.org/abs/2608.20201v1":
        "提出「软件 3.0」范式：上下文与推理决定行为，三层架构中界面层被模型按需生成能力吸收、业务逻辑层按「可表达性×关键性」拆分给模型推理和存储约束，最终只剩数据层作为唯一持久基础设施，并划定了该论点在确定性、成本、安全、可验证性上的适用边界。",
    "http://arxiv.org/abs/2608.20186v1":
        "用无创干电极 EEG 记录单人 393 次共约 49 小时的默读数据，训练对比学习编码器把 EEG 窗口与 LLM 词嵌入对齐，实现开放词表的词级解码，效果随数据量对数线性增长且未饱和，说明默读可作为解码内心语言的可扩展代理任务。",
    "http://arxiv.org/abs/2608.20116v1":
        "构建合成基准让数值时间序列与文字摘要证据相互冲突，发现开源指令模型的证据仲裁并非随机：存在系统性的文字/数字偏好，且更依赖时间新近性而非显式可靠性提示，甚至会过度依赖外部预测而忽视直接证据。",
    "http://arxiv.org/abs/2608.20315v1":
        "提出 BERT-LER，一个在 7500 万患者去标识化电子病历数据上预训练的结构化 EHR 模型，将化验结果编码为带百分位分箱的离散 token 并配合 Integrated Gradients 做词元级归因，在 EHRShot 基准和哮喘病情进展研究中预测效果具竞争力且解释与已知临床风险因素吻合。",
    "http://arxiv.org/abs/2608.20280v1":
        "系统比较 FIFO/LRU/LFU/ARC/GDSF 等 LLM 语义缓存驱逐策略，发现 LFU 是最强的简单默认策略；同时发现在真实相似度阈值下多数「命中」其实并不能直接替代答案，原始 51%-60% 的命中率经质量校正后骤降到 1.1%-2.2%。",
    "http://arxiv.org/abs/2608.20161v1":
        "针对「规划器生成编辑方案+扩散模型渲染」的指令图像编辑两阶段流程，提出双层信用分配强化学习框架 DARS，通过多方案多渲染 rollout 估计模块间/模块内奖励方差做软路由，并对规划器输出做结构化奖励与词元级优势重加权，在五个基准上超过联合强化学习基线，推理密集型编辑任务提升最大。",
    "http://arxiv.org/abs/2608.20129v1":
        "提出用编排器协调 PPO 强化学习和 PID 控制、并全程引入 LLM 常识推理的自动驾驶混合框架，LLM 还被用于迭代优化 RL 奖励函数，在高度随机化的 CARLA 场景测试中验证了将 LLM 推理与传统自动驾驶方法结合、同时保留结构化控制与安全机制的潜力。",
    "http://arxiv.org/abs/2608.20106v1":
        "构建含 3266 道选择题、六大类知识、四档难度的葡萄酒领域基准，全部基于 3.8 万条来源可溯源的事实构建，评测 16 个前沿配置发现准确率在 53%-84% 之间（o3 最高 83.6%），推理模式提升仅在 DeepSeek R1 上明显，且 Anthropic 对自家生成题目有 +9 个百分点的自我偏好而 Google 反而是 -8 个百分点。",
    "http://arxiv.org/abs/2608.20316v1":
        "把「多模型路由前要不要花代价精确估值」形式化为经典的 Pandora's Box 最优搜索问题，在高斯信号模型下给出闭式的信息价值策略（Pandora's Router），实验显示其能以远少于穷举估值的查询次数达到接近穷举估值的路由质量，去中心化版本在信息噪声大时可能被策略性模型利用。",
    "http://arxiv.org/abs/2608.20314v1":
        "提出中训练数据构建流水线 MidTool，结合网页/PDF/代码数据与真实工具 API、MCP 技能合成的监督信号，专门教模型识别工具可用性、结合上下文填参数、组合调用流程；在 Qwen3-4B/8B-Base 上做中训练后再接 SFT/RL，在 BFCL、tau2-Bench、MCP Universe 上均一致优于基线，说明通用工具使用能力也该在中训练阶段专门培养。",
    "http://arxiv.org/abs/2608.20220v1":
        "首个针对「用户提问信息不足」场景的法律 AI 基准 InsufficiencyBench，构造 202 个跨六大法律领域、24 个美国司法辖区、由执业律师标注的题目，评测十个前沿模型发现没有一个模型识别缺失要素的 F2 超过 0.46，多数模型要么无差别模棱两可，要么在虚构前提下悄悄给出结论。",
    "http://arxiv.org/abs/2608.20202v1":
        "提出「记忆认知陷阱」概念：即使记忆准确且相关，也可能扭曲模型推理（推理固着、信念扭曲），构建 MemTrapBench 基准发现所有现有记忆方案效果都不如不用记忆，最强方法性能也下降超 10%，并提出简单的推理时方法 AdaptiveMem 缓解该问题同时不损害常规记忆基准表现。",
    "http://arxiv.org/abs/2608.20169v1":
        "针对 LLM Agent harness 自动优化中每轮都要跑全量验证集导致成本高的问题，提出让验证任务集合随 harness 一起演化的 Task-CoEvolve 方法，用方差加权采样聚焦于 Agent 能力边界附近的任务，在 Terminal-Bench 2.1 等测试中用减少 80% 评估次数达到与全量搜索相当的最终性能。",
    "http://arxiv.org/abs/2608.20099v1":
        "针对多 Agent 系统自动拓扑设计（ARG-Designer）缺乏稀疏高效激励的问题，引入类 RLHF 的奖励引导自回归图生成方法 RGA-Designer，联合建模任务正确性与结构紧凑性训练奖励模型并微调图生成器，在保持任务准确率的同时平均降低 20.5% 的 token 消耗。",
    "http://arxiv.org/abs/2608.20084v1":
        "提出「证据获取与可行性门控」框架 EAFG，让 VLM+任务运动规划系统先通过探索性子目标获取视觉证据，再用可行性门决定是继续规划、继续取证还是终止，在物体使用存在歧义的烹饪任务中提升了任务完成率，并能在目标物体确实不存在时做出恰当的终止决策。",
    "http://arxiv.org/abs/2608.20083v1":
        "针对时序知识图谱问答中多跳推理效果差的问题，提出 SABET-QA 框架，用双向实体-时间评分机制和槽位感知上下文对齐配合可微分工作记忆做渐进式假设精化，在 CronQuestions 等四个数据集的复杂多步时序查询上取得一致提升。",
    "http://arxiv.org/abs/2608.20338v1":
        "提出「双用途概念」视角评估 LLM 遗忘（unlearning）能力，要求遗忘集和保留集在概念使用上互补，构建 ConceptGuard 基准发现现有遗忘方法在这种概念级、意图敏感的设置下普遍表现不佳，遗忘与保留效用之间存在明显权衡且跨方法一致性差。",
    "http://arxiv.org/abs/2608.20319v1":
        "提出任务模型归纳（TMI）方法，从无约束的计算机使用轨迹（截图+鼠标键盘操作）中拆分出交织的多个潜在任务，并为每个任务归纳出目标分解模型与执行流程模型；在受控轨迹上任务分组一致性达 0.974、还原 74.9% 的执行步骤，衍生技能在新任务上的准确率比最强基线提升 30%。",
    "http://arxiv.org/abs/2608.20274v1":
        "系统研究 LLM Agent 技能诱导与跨任务迁移，比较任务级 vs 子任务级技能归纳、文本 vs 代码技能格式，发现任务级技能平均反而拖累表现、子任务级技能才能带来提升，文本技能比代码技能迁移更好，并提出结合「特异性」与「泛化度」的技能效用分数，无需实际执行任务即可诊断技能记忆库质量。",
    "http://arxiv.org/abs/2608.20237v1":
        "提出可控基准 RuleMaze，要求多模态大模型在自然语言规则约束下走迷宫，并提出「语言-逻辑-函数混合化」自动生成规则及可执行校验器、以及解耦感知/执行/规则校验三部分的 DMP 规划方法，显著提升规则遵循与规划成功率，并能更好泛化到更复杂、未见过的规则。",
    "http://arxiv.org/abs/2608.20181v1":
        "针对电力系统机器学习保护研究评测设置不统一、「近乎完美」分数含义不清的问题，提出标准化评测框架（定义保护目标、物理范围、可观测性等七个维度），在 PROTECT-90 电磁暂态基准上验证：MLP 在故障分类上 F1 达 0.991，但传统双端定位算法在信息充分时优于学习方法，且干净数据下的表现不能预测鲁棒性。",
    "http://arxiv.org/abs/2608.20320v1":
        "提出结合对话式数据采集、结构化数据处理、行为预测的三 Agent 工作流研究天气敏感出行需求，用聊天机器人图文问卷收集学生通勤者在五种天气场景下的出行方式选择，测试九个本地部署 LLM（2B-35B）发现最好的纯文本零样本 LLM 准确率（69.9%）已接近随机森林（69.6%），加入天气图片后视觉配置进一步提升到 71.5%。",
}
