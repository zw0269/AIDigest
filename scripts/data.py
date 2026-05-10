"""URL → 中文摘要 / 翻译 数据。

两个字典：
- MANUAL_SUMMARIES: HTML 类源（无 RSS description），值为我手写的中文摘要。
- TRANSLATIONS: RSS 源拿到的英文 description 的中文翻译/概括。

新条目无英文翻译时，渲染只显示英文原文。Anthropic/Dario 已是中文，无需翻译。
"""

# 无 RSS 的 HTML 源（Anthropic, Dario Amodei, 以及个别 RSS 缺 description 的）
MANUAL_SUMMARIES: dict[str, str] = {
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
}

