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
}

