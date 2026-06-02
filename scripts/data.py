"""URL → 中文摘要 / 翻译 数据。

两个字典：
- MANUAL_SUMMARIES: HTML 类源（无 RSS description），值为我手写的中文摘要。
- TRANSLATIONS: RSS 源拿到的英文 description 的中文翻译/概括。

新条目无英文翻译时，渲染只显示英文原文。Anthropic/Dario 已是中文，无需翻译。
"""

# 无 RSS 的 HTML 源（Anthropic, Dario Amodei, 以及个别 RSS 缺 description 的）
MANUAL_SUMMARIES: dict[str, str] = {
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
}


# RSS description 的英中翻译（一句话级别的中文化概括，非逐字翻译）
TRANSLATIONS: dict[str, str] = {
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
}

