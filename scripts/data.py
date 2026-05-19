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
}


# RSS description 的英中翻译（一句话级别的中文化概括，非逐字翻译）
TRANSLATIONS: dict[str, str] = {
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
}

