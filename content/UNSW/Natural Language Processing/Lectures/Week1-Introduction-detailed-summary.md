# COMP6713 Week 1 Introduction 详细总结

说明：本总结以 `Lectures/Week1-Introduction.pdf`（共 55 页）为主线整理。由于若干页只写了 `Demo time!` 或只给出工具名，我额外对照了 `Lectures/Week_1.zip` 中的 `simple-nltk.ipynb`、`simple-spacy.ipynb`、`simple-huggingface.ipynb`，补全了演示内容，保证知识点尽量不遗漏。

---

## 1. 课程导入与课程结构（P1-P13）

### 1.1 开场主题：从图灵问题切入 NLP

课件第一页以 Alan Turing 的经典问题开场：

> “What will happen when a machine takes the part of A in this game?”

它强调的不是抽象地问“机器能否思考”，而是把问题转化为：机器能否在语言交互中表现得像人。这实际上为整门课定下了基调：

- NLP 是 AI 中最直接处理“人类语言”的方向。
- 语言交互能力是衡量机器智能的重要窗口。
- 课程后续讨论的大量任务，本质上都和“机器能否理解/生成自然语言”有关。

### 1.2 课程基本信息

- 课程：`COMP6713 Natural Language Processing (NLP)`
- 学期：`2026 T1`
- 任课教师：`Dr. Aditya Joshi`
- 邮箱：`aditya.joshi@unsw.edu.au`
- 办公室：`K17-217B`
- 技术问题：`WebCMS Forum`
- 技术/个人问题邮箱：`cs6713@cse.unsw.edu.au`

教师个人背景页还给出两层信息：

- 研究方向：`Foundational and Applied NLP`
- 实践经历：情感分析、计算讽刺、疫情情报、职位推荐、会议摘要等

这说明课程不会只讲“模型”，而是会把 NLP 放回真实应用语境中来看。

### 1.3 教学团队与研究快照

课件列出课程团队成员，并展示了教师近年的一些研究/培训活动，例如：

- 面向司法系统的 `Introduction to AI & LLMs` 培训
- 主题涉及：`jailbreaking`、`multimodal hate speech detection`、`code language models`、`climate science NLP`

这里隐含两个信号：

- 现代 NLP 已经深入法律、公共治理、行业应用。
- 课程不会把 NLP 只当成“文本分类”小工具，而是会覆盖 LLM、伦理、安全等现代议题。

### 1.4 课程定位与教学哲学

课件明确说明：这是一门 `introductory course`，但已经是第 3 次开设；选课人数从 2024 年约 55 人增长到 2026 年约 420 人。

课程哲学用三个问题概括：

- `What`：语言现象是什么
- `How`：如何用计算模型处理这些现象
- `Why`：这些方法为何会这样发展，背后的历史脉络是什么

这三个词非常重要，因为它们几乎对应课程三条主线：

- 语言学现象
- 计算方法
- 方法演化史

### 1.5 推荐资源与先修要求

推荐教材：

1. Jurafsky & Martin, *Speech and Language Processing*, 2025 online manuscript
2. Pushpak Bhattacharyya & Aditya Joshi, *Natural Language Processing*, Wiley, 2023

先修要求：

- 研究生：`COMP9020` 和 `COMP9814 or COMP9444`
- 本科生：`MATH1081` 和 `COMP3411 or COMP9444`
- 允许特殊情况例外

课件还给了“你是否会喜欢这门课”的非正式判断：

- 你喜欢语言
- 你喜欢编程
- 你对 AI 模型如何工作有好奇心
- 你喜欢把现代技术与历史思想联系起来

### 1.6 学习目标（CL01-CL04）

这一页是重要考点，建议直接记住：

- `CL01`：能够描述 NLP 问题，如 POS tagging、sentiment analysis、information extraction、machine translation，并说明它们在歧义消解上的挑战。
- `CL02`：能够解释典型 NLP 方法，尤其是统计方法与神经方法。
- `CL03`：能够使用 NLP 库（如 `NLTK`、`scikit-learn`、`Transformers`）训练模型并做推理。
- `CL04`：能够为具体应用设计 NLP 方案，包括问题建模、方法选择和评估策略。

这 4 个目标基本覆盖“概念理解 + 工具使用 + 系统设计”三层能力。

### 1.7 为什么还要学深度学习以前的 NLP

课件明确回答了一个很多学生都会问的问题：既然已经有 LLM，为什么还学经典 NLP？

原因有：

- `LLMs are far from perfect`：大模型并没有解决所有问题。
- 传统方法仍被很多企业使用，尤其在可解释、成本、数据量受限场景中。
- 理解经典方法，有助于理解深度学习方法的巧妙之处。
- 语言学例子帮助理解 NLP 的 `what`。
- 神经模型帮助理解 NLP 的 `how`。
- “三代 NLP”视角帮助理解 NLP 的 `why`。

这是本周的核心总纲之一：**课程不是“旧方法 vs 新方法”，而是用方法演化史去理解现代 NLP。**

### 1.8 课程反馈与 2026 版变化

2025T1 学生反馈总体非常正面。课件同时指出 2026T1 的调整：

- 行业项目组在团队凝聚方面更容易出问题
- 因此 `this term no industry project`
- 课程将加入更多 `RL-based LLM alignment` 内容

### 1.9 课程内容安排

课件给出按周模块安排：

- `Week 1`：Introduction
  - NLP tasks
  - ambiguity resolution
  - generations of NLP
  - ethical considerations
  - black-box NLP libraries
  - datasets + API calls for LLMs
- `Week 2`：Representation learning
  - grammar
  - probabilistic language models
  - word vectors
  - sequential models review
- `Week 3`：Attention & Transformer
  - attention
  - fine-tuning
  - prompt tuning
- `Week 4`：Language models
  - encoder models
  - decoder models
  - LoRA
  - LangChain
- `Week 5`：Sentiment Analysis
  - lexicons
  - statistical classifiers
  - LSTM stacks
  - BERT-based models
  - evaluation and benchmarks
- `Week 7`：POS tagging and NER
  - HMM-based POS tagging
  - POS as seq2seq
  - CRF-based NER
- `Week 8`：Machine Translation
  - rule-based / statistical / neural MT
  - decoding
  - speculative decoding
- `Week 9`：Summarisation & QA
  - extractive / abstractive summarisation
  - RL-based LLM alignment
- `Week 10`：Other NLP tasks
  - shared tasks
  - benchmarks
  - applications
  - emerging architectures
  - guest lectures
  - how to read an NLP paper

可以看出，本课不是只讲 LLM，而是覆盖从传统到现代、从底层任务到应用任务的完整链条。

### 1.10 上课时间与资源平台

- Lecture：Monday 16:00-18:00
- Lecture：Wednesday 9:00-11:00
- 地点：`Mathews Theatre B (K-D23-203)`
- 课程主页：`WebCMS` / `Moodle`
- 提醒：是否已加入 WebCMS/Moodle、是否收到 tutorial allotment
- 特别提醒：`Monday 6 April 2026` 为 Easter Monday public holiday

### 1.11 Assessment 结构

这一部分要记熟，因为它既是课程规则，也是可能在 quiz/考试/平时问答中出现的信息。

#### Weekly Quizzes（20%）

- Moodle 上进行
- `closed-book`
- 时间：`Week 2-5, 7-9`
- `one attempt`
- `no time limit`
- 自动评分
- 开放时间：`Wednesday 12pm` 到 `Monday 12pm`
- Week 1 有 sample quiz，但不计分

#### Assignment（10%）

- 个人编程作业
- 往年题目例子：从招聘广告/简历中抽取技能、诗歌生成等
- `released in Week 3`
- `due end of Week 5`
- 主要基于 Weeks 1-3 内容
- 评分：测试脚本 + 人工评价（风格、正确性等）

#### Group Project（25%）

- 每组 `4-5` 人
- `Week 4` 注册组和题目，之后不能改
- `due Friday of Week 10, 5pm`
- `Week 11` 线上展示和 Q&A，所有成员都必须参加
- 提交物：`code(zip)`、`report(pdf)`、`presentation(pdf)`

#### Final Exam（45%）

- `2 hours`
- exam period 内进行
- `Inspera`，线下监考
- 题型：`multiple-choice`、`short answers`、`code analysis`
- 及格门槛：`students must score more than 40% on the final exam`

这条 final exam hurdle 很重要，说明不是总分高就一定过，期末本身必须过线。

### 1.12 Project 组队建议与学术诚信

课件建议：

- 尽早组队
- 平衡 NLP 经验
- 不要只在熟人圈里找队友
- 后续会给 rubric 帮助界定项目范围

同时明确提醒：

- 你需要理解并遵守 `UNSW Academic Integrity policy`
- 编程课程中的学术诚信同样严格适用

### 1.13 课程资源

课件列出：

- Lecture slides & recordings
- Tutorial problem sets（不计分）
- 建议教材

这里说明：tutorial 不是为了刷分，而是为了巩固概念与方法。

---

## 2. NLP 的今天与昨天（P14-P27）

### 2.1 什么是 NLP

课件定义：

`Natural language processing (NLP) is the branch of artificial intelligence that deals with computational processing of human languages.`

关键词是：

- `branch of AI`
- `computational processing`
- `human languages`

此外课件还指出：

- NLP 又常与 `computational linguistics` 相联系
- 与 `human language technology`、`text analytics` 有显著重叠
- `natural languages` 指人类使用的语言
- `artificial languages` 指编程语言等人工形式化语言

一句话总结：**NLP 研究的是“怎样让机器计算性地处理人类语言”。**

### 2.2 NLP today：现代 NLP 的典型应用

课件列举了很多“你已经在现实中见过”的 NLP 系统：

- `Siri`
- `ChatGPT`
- `Grammarly`
- `spell checker`
- `DeepSeek`
- 以及围绕 ChatGPT 产品化的新闻链接

这里的教学意图是：NLP 已经不是学术边缘方向，而是用户每天都在接触的核心 AI 技术。

课件进一步给出应用场景例子：

- 流感疫情监测（social media / epidemic intelligence）
- 法律 AI
- AI companions 等社会技术问题

所以 Week 1 一开始就强调：**NLP 的应用范围极广，而且已经带来真实社会影响。**

### 2.3 Early NLP：NLP 并不是最近才出现

课件给出三个历史节点：

- `1964: ELIZA`，心理咨询式聊天机器人
- `1968: SYSTRAN`，机器翻译系统（俄译英）
- `2006: IBM Watson`，问答系统

这说明：

- 语言自动化不是 LLM 时代才开始
- 早期 NLP 已经在聊天、翻译、问答三个方向探索
- 今天很多“新”问题，历史上都出现过原型

### 2.4 什么是 natural language

课件从语言本身出发做了一个很重要的铺垫：

- 自然语言是人类说的语言，例如中文、西班牙语、英语、阿拉伯语、印地语、孟加拉语等
- 语言的功能包括：传递知识、协作、表达、甚至 gossip
- 语言不仅传递已有想法，也会共同创造新想法
- 语言有专门化形式，例如医生的话语体系、电工的话语体系、不同学科教师的话语体系
- 语言内部也高度多样化：
  - 母语者 vs 非母语者
  - 方言 vs 所谓“标准语”
  - 语域/register，如礼貌表达 vs 对抗性表达

这一页非常关键，因为它告诉你：**NLP 面对的对象不是简单、统一、标准的文本，而是复杂、多样、动态演化的人类语言。**

### 2.5 Words：词是语言的基本单位

课件从“词”出发讲语言：

- 词是语言的基本单位
- 词最早是声音，后来发展出书写系统
- 书写使知识得以跨代传播
- 词承载“idea”
- 同一个概念在不同语言中用不同词表达
- 课件还以象形文字与 `tea/cha` 为例，说明语言与文化传播的历史性

这里实际上是在为后面的 token、词形归一化、词向量打基础。

### 2.6 Words -> Word order：语序

课件强调，语言不仅有词，还要看词序。它列出三种典型语序：

- `SVO`：Subject-Verb-Object
  - 例：English, Chinese, Italian
- `SOV`：Subject-Object-Verb
  - 例：Japanese, Marathi, Tamil
- `VSO`：Verb-Subject-Object
  - 例：Arabic, Irish

这提醒我们：

- NLP 不能只用英语直觉看所有语言
- 语法结构差异会直接影响分词、解析、翻译、表示学习等问题

### 2.7 Language families

课件简略提到 `language families`，意思是：

- 语言之间有谱系关系
- 相似语言可能共享某些结构特征
- 跨语言 NLP 往往要考虑语系与结构共性/差异

### 2.8 So... what is NLP：NLU 与 NLG

课件把 NLP 拆成两大方向：

- `Natural Language Understanding (NLU)`：机器“理解”语言
- `Natural Language Generation (NLG)`：机器“生成”语言

可以对应为：

- `Text -> Label / Set of labels`
- `Text -> Text`

例如：

- 情感分类是 NLU
- 机器翻译、摘要、对话回复是 NLG

注意：现实任务常常混合两者，例如问答系统需要先理解问题，再生成回答。

### 2.9 Turing 的 imitation game

课件再次回到 Turing：

- 如果机器在语言交互中能够骗过人类评判者，它是否达到了语言智能的高峰？

这页的意义不是要求你背哲学史，而是强调：

- 语言能力是 AI 智能的重要试金石
- 对话、问答、推理、上下文理解，都能被放到“模仿人类语言行为”的框架下理解

### 2.10 NLP 的三个维度

课件给出一个非常重要的三维视角：

- `Language`：英语、普通话、印地语等
- `Task`：情感分析、问答、POS tagging 等
- `Model`：HMM、BERT、SVM 等

这意味着任何一个 NLP 系统都可以被理解为：

- 在某种语言上
- 做某类任务
- 使用某种模型

考试中常见陷阱是把“任务”和“模型”混淆，例如：

- `POS tagging` 是任务，不是模型
- `BERT` 是模型，不是任务
- `English` 是语言，不是任务也不是模型

### 2.11 Black-box 视角

课件在 Week 1 里有意使用 `black-box` 视角：

- 先把 NLP 系统视为“输入 -> 输出”的黑盒
- 暂时不展开内部细节
- 先看系统能做什么，再逐步拆解其内部机制

给出的黑盒例子：

- 拼写纠错：输入句子中的 misspelt words，输出可能的纠正候选
- LLM：输入问题（甚至可能是多模态输入），输出文本/多模态响应

这也是本周课程组织方式：先看黑盒，再到后面模块拆黑盒。

### 2.12 语言学任务（linguistic tasks）

课件列出几类典型的语言学层面任务：

#### 1. POS tagging

给句子中每个词打词性标签。

- 输入：句子
- 输出：按 tag set 标注的词序列

#### 2. Chunking

把词组织成短语块。

- 例如识别名词短语 `[The blue book]`

#### 3. Parsing

建立句法树，尤其是以主要谓词为中心的依存结构。

#### 4. Co-reference resolution

在文档中把代词等指代表达连接回正确的先行词。

这些任务不是最终应用，但它们是很多高层应用的基础。

### 2.13 Ambiguity hierarchy：从低层到高层的歧义

课件非常重要地指出，上述任务对应语言歧义层次中的较低层：

- `Phonological`：声音到词
- `Morphological`：词到词素/词形结构
  - 例：`informing -> inform`
- `Lexical`：词到词义/词类
- `Semantic`：句子到字面意义
  - 例：`I love this sandwich -> POSITIVE`
- `Pragmatic`：句子到隐含意义
  - 例：`I love being ignored -> NOT POSITIVE`

这里特别值得注意：

- 语义层面是“字面意思”
- 语用层面是“说话人真正想表达的意思”

这直接为后面“pragmatic ambiguity”“sarcasm”“bias”“hallucination”等内容埋下伏笔。

### 2.14 Demo: NLTK

课件里只写了 `Demo: NLTK`，但 notebook 里实际演示了很多基础功能。

NLTK 的定位：

- `Natural Language Toolkit`
- 支持多语言文本处理 pipeline
- 自带多个 corpus
- 常被作为更大系统中的一个组件

对照 notebook，本次 demo 覆盖：

#### 1. Tokenization

- 输入：原始句子
- 输出：tokens
- 示例函数：`wordpunct_tokenize`

#### 2. POS tagging

- 对 token 序列打词性标签
- 示例函数：`pos_tag`

#### 3. Chunking

- 用规则文法做短语分块
- 示例：`RegexpParser(grammar)`

#### 4. Morphological normalization

- `stemming`
  - 示例工具：`PorterStemmer`
  - 是基于规则的词干截断，不一定得到字典中的真实单词
- `lemmatisation`
  - 示例工具：`WordNetLemmatizer`
  - 更接近词典合法词形

#### 5. WordNet

- 查 `synsets`
- 读词义定义、词性信息
- 展示词汇资源如何支持 NLP

#### 6. SentiWordNet

- 观察词在不同 sense 下的情感倾向
- 说明“词的情感值”也依赖 sense，而不是一个词只有一个固定情感分数

#### 7. Stopword removal

- 从文本中去掉高频虚词，保留内容词

#### 8. Word cloud

- 用 Gutenberg 语料（如 `Moby Dick`）可视化高频词

这部分 demo 的教学目的非常明确：**先用工具建立对基础 NLP 操作的直觉。**

### 2.15 Downstream tasks：面向应用的任务

课件指出：NLP 的重心逐渐从纯语言学任务转向 `application-oriented tasks`。典型下游任务包括：

- `Sentiment Analysis`
- `Information Extraction`
- `Named Entity Recognition`
- `Paraphrase detection`
- `Machine Translation`
- `Summarisation`
- `Question Answering`
- `Document Question Answering`

这些任务与前面的 linguistic tasks 的关系是：

- linguistic tasks 常常是基础能力
- downstream tasks 更接近实际产品或业务问题

### 2.16 Conversational AI 中的任务

课件单独提到会话 AI 场景：

- `Question-answering`
- `Document question-answering`
- 对“conversation itself”进行处理

这说明现代 NLP 已经不只是句子级处理，而是走向多轮对话、长上下文、文档级理解。

### 2.17 研究生态：ACL Anthology

课件给出 `ACL Anthology`，意思是：

- NLP 有成熟的学术共同体
- 主要论文可在 Anthology 查找
- 研究任务和研究轨道不断演进

### 2.18 多语言意识

课件特别提醒：虽然这门课主要聚焦英语，但你应该不断问自己：

- 这个方法在我会的其他语言上还成立吗？
- 数据是否足够？
- 模型是否适配？
- 语言现象是否不同？

课件用三元组概括跨语言思考框架：

- `Data`
- `Model`
- `Linguistic phenomena`

这其实是在培养一种正确的 NLP 思维方式：**不要把英语世界的现象默认当成语言普遍规律。**

---

## 3. 歧义、规则、数据与概率（P28-P41）

### 3.1 Week 1 的课程安排提醒

课件给出一些 operational 信息：

- Week 1 没有 assessment，也没有 tutorial
- Week 1 的 sample quiz 会放到 Moodle，但不计分
- 从 Week 2 开始 quiz 正式计分
- Week 2 的 quiz 会覆盖 `Week 1 + Week 2`
- consultation hour：`Tuesdays 1:30pm-2:30pm`, Weeks 2-10, K-17 217-B
- 应尽早开始考虑 project group

对复习来说，这里最关键的是：**Week 1 内容会很快进入 quiz 范围。**

### 3.2 Ambiguity：为什么 NLP 的核心是歧义消解

课件先说：语言传达想法，但语言本身天然是 ambiguous 的。定义是：

> Ambiguity: The quality of being open to more than one interpretation.

然后给出三类歧义：

#### 1. Lexical ambiguity（词汇歧义）

一个词可能有多个意义。

示例：

- `Love means nothing to them`

这里的 `love` 在网球计分中是 `0`，但字面上又是“爱”的意思。

#### 2. Syntactic ambiguity（句法歧义）

同一串词可以对应不同结构。

示例：

- `I saw a boy with a telescope.`
  - 是“我拿望远镜看见一个男孩”？
  - 还是“我看见一个带望远镜的男孩”？
- `I got a job offer from SEEK`
  - `SEEK` 可能是公司名，也可能让人按动词 `seek` 去误解

#### 3. Pragmatic ambiguity（语用歧义）

句子真实意图和字面意义不一致。

示例：

- `Being stranded in traffic is the best way to start the week.`

字面上是正面评价，实际通常表达抱怨/讽刺。

课件随后明确指出：

- NLP 的核心任务之一就是构造计算技术去解决这些歧义。
- `Ambiguity resolution is at the heart of NLP.`

这是本周最核心的理论结论之一。

### 3.3 一个简单却经典的问题：句子边界识别

课件提出一个看似简单、实则非常经典的任务：

- 让计算机识别 document 中哪里是 sentence boundary

对人类来说很简单，但对计算机来说，句号 `.` 本身就有歧义：

- 可能是句末符号
- 可能是缩写的一部分，如 `U.S.`
- 可能是小数点，如 `183.32`

课件用金融文本做例子：

- `The Bank of New York ADR Index ... gained 1.3% to 183.32 points ...`
- 文本中既有缩写，又有数字，又有真实句界

所以“看到句号就断句”是不可靠的。

### 3.4 Rule-based thinking：如果让人手写规则会怎样

课件让学生尝试定义规则，例如：

- 如果字符是 `.`，就开始新句子
- 或者如果 `.` 后面跟空格和大写字母，就开始新句子

这页想说明：

- 规则方法很直观
- 很容易从人类语言直觉出发
- 但一旦进入真实文本，就会迅速遇到 corner cases

### 3.5 规则系统与 ELIZA

课件用 ELIZA 和 Prolog/LISP 的例子说明：

- 早期 NLP 大量依赖 `human designer / expert`
- 专家把规则编码进系统
- 系统靠规则来处理语言现象和歧义

所以第一代 NLP 的核心模式可以概括为：

- 语言歧义
- 由专家设计规则
- 用规则做决策

### 3.6 规则方法如何评估：Precision / Recall

课件用断句规则继续往下推，讨论：

- `Precision`：系统判定为正例时，有多少是真的正例
- `Recall`：所有真实正例中，有多少被系统找到了

给出的含义是：

- 很粗糙的规则，可能召回和精度都很差
- 更复杂一点的规则，在某个文本上也许看起来很好
- 但换一个文本，很可能马上失效

课件明确指出：

- rule-based systems 常见问题是 `high precision, low recall`
- 规则容易 `overfit`

### 3.7 为什么规则不够

课件明确给出规则方法的缺点：

- 编写规则费时费力
- 需要专家知识
- 规则可能带有专家主观偏见
- 规则容易过拟合特定文本/场景
- 语言会演化，新词、新表达、新事件不断出现
  - 例：`lit`
  - `kickass`
  - `I googled`
  - `COVID`

因此结论是：

**Rules are inadequate to capture linguistic phenomena.**

即：靠纯规则难以覆盖真实语言的复杂性。

### 3.8 从规则走向数据：观察可以消解歧义

课件接着用 Abma 语言小练习说明：

- 如果给你若干句对照数据
- 你可以通过“观察规律”来猜测翻译方式
- 这类规律不一定是专家先写好的，也可以从数据中归纳

课件引导学生反思：

- 你用了哪些数据？
- 你做了什么假设？
- 哪些句子仍然不能确定翻译？

这一页的真正教学重点是：

- 数据可以帮助解决歧义
- 但数据的覆盖范围决定你能学到什么
- 数据不足时，不确定性仍然存在

### 3.9 Corpus / Dataset 的概念

课件用 Rosetta Stone 举例，把它称作最早的一类“corpus”雏形：

- 同一内容有多种语言版本
- 可以借助对齐观察去理解未知语言

进一步，课件指出：

- digitisation 让数据集规模大增
- internet 让数据量爆炸式增长
- 但网站也开始阻止爬虫抓取

这说明现代 NLP 一方面建立在大规模数据上，另一方面又受到版权、平台规则、抓取许可等限制。

### 3.10 数据标注与学习范式术语

这一页必须熟记。

#### 1. Supervised

- 数据带有人工或已知标签
- 例：
  - `I love the movie -> Positive`
  - `The movie sucks -> Negative`

#### 2. Distant-supervised

- 标签是通过某种启发式自动构造出来的
- 不是完全人工逐条标注
- 例：通过 hashtag 等弱信号去推测 sarcasm 标签

#### 3. Unsupervised

- 数据没有目标标签
- 只是原始文本本身

#### 4. Self-supervised

- 监督信号来自数据自身
- 例：
  - `I love the movie -> I ____ the movie`
  - 目标词是 `love`

课件特别说明：self-supervised 是现代深度学习 NLP 的关键思想之一。

易错点：

- `unsupervised` 不是“什么目标都没有”这么简单，而是没有人工给的目标标签。
- `self-supervised` 仍然有学习目标，只是目标从数据本身构造出来。

### 3.11 Enter: Probability

课件在这里把方法论再推进一步：

- 只有规则还不够
- 只有数据也不够
- 还需要 `probability`

列出的关键词包括：

- `Naïve Bayes`
- `conditional independence assumption`
- `N-grams`
- `skip-grams`
- `argmax`

这意味着后续课程会进入统计 NLP 的典型逻辑：

- 通过概率建模语言/标签分布
- 比较不同候选输出的概率
- 用 `argmax` 选最优输出

### 3.12 随机变量、词表示与 softmax

课件紧接着提出：

- 词真的是随机变量吗？
- 从 `one-hot vector` 如何走向 `word vector representations`
- 神经网络输出的是 `logits`
- 把 logits 变成概率通常用 `softmax`

这里是从经典统计 NLP 向神经 NLP 的桥梁：

- 统计 NLP：显式概率、显式特征
- 神经 NLP：先得到向量与 logits，再通过 softmax 形成概率分布

### 3.13 数据、概率、歧义三者关系

课件有两页图示，本质上表达的是：

- 语言里存在歧义
- 规则是一种解决方式
- 数据是另一种关键来源
- 概率把“观察到的数据”和“如何做决策”连接起来

可以把这一部分概括为：

**现代 NLP 的许多方法，本质上是在用数据支持的概率计算来做歧义消解。**

### 3.14 Lexicons：语言资源也是重要“数据”

课件提醒，数据不只是大规模原始文本，还可以是结构化词汇资源，例如：

- `WordNet`
- `LIWC`
- 领域本体/词典（如 medical ontologies）
- 公司内部自建 lexicons

这些资源可能表示为：

- `graphs`
- `lists`

它们在实际系统中很有价值，尤其在：

- 规则匹配
- 特征工程
- 领域知识注入
- 可解释系统

### 3.15 WordNet 的关键概念

课件给出 WordNet 的核心要点：

- 是英语词汇数据库
- 1985 年开始建设
- 启发了其他语言的 WordNet
- 由 `synsets` 组织词义
- synsets 之间通过语义关系连接

要记住的关系：

- `synonymy`
- `antonymy`
- `hyponymy / hypernymy`
- `meronymy / holonymy`

考点提醒：

- WordNet 是 lexical database，不是分类模型。
- synset 是“同义词集合 + 某个 sense”，不是“这个词的全部含义”。

### 3.16 Demo: spaCy

课件给出 spaCy 的定位：

- 开源 NLP 库
- 多语言支持
- `industrial-strength NLP`
- 支持深度学习 pipeline
- AllenNLP 建立在 spaCy + PyTorch 之上
- 也支持和 LLM 集成

课件还给出安装方式：

- `pip install spacy`
- `python -m spacy download en_core_web_sm`

### 3.17 spaCy matcher 与 rule-based matching

课件指出：

- 正则表达式本身也是 rule-based NLP 的一种遗产
- spaCy 的 `Matcher` 支持多种 pattern-matching primitive
- `PhraseMatcher` 对 ontology-based matching 很有用

这说明即使在现代库里，规则方法依然没消失，而是作为组件存在。

### 3.18 对照 notebook：spaCy demo 实际演示了什么

根据 `simple-spacy.ipynb`，demo 至少覆盖：

#### 1. spaCy linguistic processing pipeline

对一句原始文本，一次 pipeline 可返回：

- token
- lemma
- POS
- fine-grained tag
- dependency relation
- shape
- sentence boundaries
- named entities

#### 2. Sentence segmentation

用带省略号、问号、缩写、数字的句子看 spaCy 如何断句。

#### 3. Named Entity Recognition

示例：

- `University of New South Wales is in Sydney`

展示如何识别组织和地点实体。

#### 4. Ontology-based matching

使用 `cities`、`dwellings` 文件里的词表，通过 `PhraseMatcher` 做概念匹配。

例如：

- `This is an apartment in Sydney.`

可以匹配出 dwelling 和 city 类概念。

#### 5. Semantic similarity

使用 `en_core_web_md` 中的向量表示比较文本相似度。

这部分说明：

- spaCy 不只是“规则工具”
- 也连接了词向量/表示学习

### 3.19 Black-box NLP library 的意义

在 Week 1 这里，spaCy 被放在“black-box NLP library”语境中介绍，目的是让学生先形成以下直觉：

- 现代 NLP 工具可以很快完成多个任务
- 库往往把复杂模型封装起来
- 你先知道它能做什么，再在后续模块里理解它为什么能做

---

## 4. 三代 NLP 范式、Transformer、HuggingFace 与 API（P42-P47）

### 4.1 三代 NLP 的总体划分

课件把 NLP 的计算技术演化概括为三代：

#### Generation 1: Rule-based NLP

- 依赖人工书写规则
- 可解释性强
- 系统修改和迁移需要人工介入

#### Generation 2: Statistical NLP

- 依赖人工设计特征
- 概率和 `argmax` 是核心计算逻辑

#### Generation 3: Neural NLP

- 不再强依赖显式任务特征工程
- foundation models 可从 self-supervised data 中学习
- 再用任务数据做适配

这页是整门课的核心框架页之一，必须会。

### 4.2 三代方法的本质差异

结合相邻几页，可以把三代差异整理为：

#### 1. 知识来源不同

- Rule-based：知识主要来自专家规则
- Statistical：知识来自数据 + 人工特征
- Neural：知识主要来自参数化模型在大规模数据中的学习

#### 2. 对人工特征的依赖不同

- Rule-based：人工规则本身就是系统主体
- Statistical：仍然需要人工特征工程
- Neural：显式特征工程的重要性下降

#### 3. 可解释性不同

- Rule-based：最高
- Statistical：中等，可从特征和概率角度解释
- Neural：通常最低，尤其是大模型

#### 4. 迁移与适配方式不同

- Rule-based：改规则
- Statistical：改特征、改模型、重新训练
- Neural：预训练后 fine-tune / prompt / adapter / LoRA 等

#### 5. 数据需求与规模倾向不同

- Rule-based：更依赖专家知识而非海量数据
- Statistical：需要标注数据和统计观察
- Neural：通常依赖更大规模数据，尤其是自监督预训练

### 4.3 Lexicons 在三代方法中的位置

课件特别提醒：三代 NLP 还可以被 `lexicons` 这类“curated, structured resources”所表征。

例如：

- `WordNet`
- `SentiWordNet`

这说明词汇资源不是只属于“老方法”的东西，而是跨代存在的知识资产。

### 4.4 Transformer 对神经 NLP 的影响

课件明确指出：

- `Transformer` 最初是为 NLP 提出的架构
- 后来扩展到其他 AI 领域
- 现代神经 NLP 深受 Transformer 影响

并给出两类代表模型：

- `Encoder-only models: BERT`
- `Decoder-only models: GPT`

考点：

- `BERT` 不是 decoder-only
- `GPT` 不是 encoder-only

### 4.5 神经 NLP pipeline

课件给出的现代 pipeline 是：

1. `Pre-training`
   - 使用 large unlabeled datasets
   - 例如 web-scale corpora
2. 得到 `Language Models`
   - 又称 `LLM`、`Foundation models`、`Pre-trained Language Models (PTLM)`
3. 用 `task-specific labeled dataset`
   - 适配到具体任务
4. 得到 `task-specific models`

课件还强调：

- `PTLMs` 和 `task-specific models` 都可以用于 inference
- 后续课程将详细讨论：
  - language model 如何预训练
  - 如何适配到具体任务

### 4.6 HuggingFace：模型与数据平台

课件中的 HuggingFace 部分包括：

- HuggingFace 提供预训练/微调模型
- `HuggingFace Hub` 是社区贡献的模型和数据集仓库
- 它易于与 `Gradio` 等部署库结合
- 历史上 HuggingFace 起初并不是今天这样的平台公司

Week 1 把 HuggingFace 作为另一个 `black-box library` 引入，目的是让学生快速接触现代模型生态。

### 4.7 对照 notebook：HuggingFace demo 实际演示内容

根据 `simple-huggingface.ipynb`，demo 包含：

#### 1. Sentiment Classification / Text Classification

- 通过 `pipeline("text-classification", model=...)`
- 示例模型：`cardiffnlp/twitter-roberta-base-sentiment`
- 输出标签如 `NEGATIVE / NEUTRAL / POSITIVE`

#### 2. Question Answering

- 输入：`context + question`
- 示例模型：`distilbert/distilbert-base-cased-distilled-squad`
- 关键结论：**该 QA 模型不是在“自由生成答案”，而是在 context 中抽取一个 span。**

这是非常高频的概念辨析点。

#### 3. Named Entity Recognition / Token Classification

- 示例模型：`dslim/bert-base-NER`
- 使用 `B-` / `I-` 标记实体片段
- notebook 里还写了 helper function 去合并连续实体 span

#### 4. Summarisation / Seq2Seq Generation

- 示例模型：`facebook/bart-large-cnn`
- 输入较长文档，输出较短摘要

所以 HuggingFace demo 贯穿了多种任务范式：

- classification
- extractive QA
- token classification
- seq2seq generation

### 4.8 APIs for LLMs

课件指出：

- 许多商业大模型通过 `API calls` 提供服务
- 用户并不直接拿到全部模型参数，而是通过接口使用模型能力

这对现代 NLP 非常关键，因为真实工业场景中，大量系统不是“自己训练模型”，而是：

- 调用商业 API
- 构建 prompt
- 处理返回结果
- 集成进更大应用中

### 4.9 OpenAI API 示例

课件给了一个 OpenAI API 样例：

- 使用 `client.chat.completions.create(...)`
- system prompt 要求把句子转成标准英语
- user input：`She no went to the market.`

教学重点不是某个具体 SDK 版本，而是理解：

- 现代 LLM 可以通过 API 嵌入软件系统
- prompt 本身成为系统设计的一部分
- 输入输出依旧可以抽象成黑盒映射：`User Input -> LLM Response`

---

## 5. 关键问题、风险与新范式（P48-P55）

### 5.1 课件态度：NLP 远远不是“已解决问题”

课件明确提醒：

- web demo 很容易让人误以为 NLP 已经 solved
- 但真实情况是，很多关键问题仍然没有被彻底解决

这句话非常重要，因为它决定了你后续看待 LLM 的方式：

- 不能只看 demo 成功时刻
- 必须看失败模式、风险、适用边界

### 5.2 Hallucination

课件在生成模型语境下指出：hallucination 至少包括：

- `factually incorrect`
- `semantically inconsistent`

并提醒：

- halluncination 的定义还可能有其他版本
- 这本身就是研究问题

这里至少要掌握：

- 幻觉不是单一现象
- 它可以表现为事实错、语义不一致、无依据编造等
- 生成模型“看起来流畅”不代表“真实可靠”

课件还给出：

- `Chatbot Arena` 可作为不同 LLM 效果比较的参考

### 5.3 Jailbreaking

课件引用 ACL 2025 论文介绍 `jailbreaking`：

- 通过某些机制绕过 LLM 的安全保护
- 使模型输出原本不应输出的有害内容
- 常见形式包括 `prompt crafting`

要点：

- LLM 的安全机制不是绝对稳固的
- “会答题”不等于“安全可靠”
- 安全对齐本身是现代 NLP/LLM 的重要研究方向

### 5.4 Ethical considerations

课件把几个关键词并列给出：

- `Bias`
- `Privacy`
- `Transparency`

#### Bias

- 句子补全等生成任务可能产生性别、种族、宗教等偏见输出

#### Privacy

- 用户或企业数据可能泄露到模型使用流程中
- 训练集/测试集也可能发生数据污染或泄漏

#### Transparency

- 输出为什么是这样？
- 能否解释？
- 能否给出来源引用？

这说明现代 NLP 不再只是“准确率最大化”，还必须考虑可信、安全、公平与责任。

### 5.5 Gender bias 与 dialectal bias

课件单独给出两个现代偏差问题：

#### Gender bias in modern NLP

- 尤其在翻译中，模型可能对性别做不当推断或强化刻板印象

#### Dialectal bias in modern NLP

- 模型对非标准语、方言、区域变体往往更不公平
- 这会直接影响系统在真实人群中的可用性与公平性

这两页想强调：

- NLP 的“准确”往往不是平均意义上的准确就够了
- 需要看不同群体、不同语言变体上的表现差异

### 5.6 Privacy in modern NLP

课件用 `Samsung bans Generative AI use` 的案例说明：

- 企业员工把内部数据粘贴给生成式 AI，可能造成泄露
- 一旦敏感信息进入外部服务，风险很大

这里的核心考点是：

- 数据不只是“训练模型的燃料”
- 数据也可能是风险源
- 现代 NLP 工程中，数据治理与访问控制同样关键

### 5.7 Novel paradigms: Transparency

课件以 `Perplexity` 一类产品为例，引出新的透明性范式：

- 系统不仅给答案
- 还尽量给来源/证据

这表明新一代 NLP 系统正在往“可追踪”“可解释”“可验证”方向发展。

### 5.8 Novel paradigms: Agentic AI

课件给出的定义是：

- 不只是回答问题
- 还会 `take action`, `plan`, 等等

这意味着系统角色从“文本生成器”变成了“带任务执行能力的代理”。

但课件也特别补充：

- 在深入这些前沿主题前，课程会先把基础打牢

这说明 Week 1 的任务不是追逐概念热点，而是建立分析框架。

### 5.9 本周总结页的含义

最后 summary 页把 Week 1 收束成几条主线：

- NLP today & yesterday
- Ambiguity
- Data + Probability + Ambiguity resolution
- spaCy text matching
- Three-generational view of NLP
- Open-source NLP models via HuggingFace
- NLP is far from solved：hallucination, privacy, bias, etc.
- Emerging tools and paradigms

### 5.10 下周预告

下一个模块将开始拆解黑盒，主题包括：

- grammar
- probabilistic language models
- word vectors
- sequential networks

所以 Week 1 的真正作用是搭骨架，而 Week 2 开始进入方法细节。

---

## 6. 本周所有高频考点整理

下面这一节是为复习和 quiz/final 准备的“考点压缩版”。

### 6.1 概念定义类

1. 什么是 NLP？
- NLP 是 AI 中处理人类自然语言的计算方法。

2. NLP 与 computational linguistics、human language technology、text analytics 的关系。
- 有显著重叠，但课程主轴是 AI 中的计算处理。

3. NLU 与 NLG 的区别。
- NLU 偏理解，NLG 偏生成。

4. 自然语言与人工语言的区别。
- 自然语言是人类语言；人工语言如编程语言。

### 6.2 任务辨析类

1. 语言学任务 vs 下游任务
- 语言学任务：POS tagging、chunking、parsing、coreference
- 下游任务：sentiment、IE/NER、paraphrase、MT、summarisation、QA

2. QA 与 document QA 的区别
- QA 直接回答问题
- document QA 需要基于给定文档作答

3. HuggingFace 的 QA demo 为什么不是“生成式 QA”？
- 因为它抽取 context 中的答案 span。

### 6.3 歧义类

1. 三种歧义要会举例
- lexical ambiguity
- syntactic ambiguity
- pragmatic ambiguity

2. ambiguity 为什么是 NLP 核心
- 因为同一语言形式可能对应多个解释，NLP 要做的就是在计算上作出正确判别。

3. lower level ambiguity hierarchy 要会对应
- phonological
- morphological
- lexical
- semantic
- pragmatic

### 6.4 方法演化类

1. Rule-based NLP 的特点
- 人工规则
- 强可解释性
- 改动要人工完成

2. Statistical NLP 的特点
- 人工特征
- 概率建模
- argmax 决策

3. Neural NLP 的特点
- 自监督预训练
- foundation models
- 任务适配

4. 为什么要学 pre-deep learning NLP
- LLM 不完美；传统方法仍有价值；有助于理解现代方法。

### 6.5 数据与学习范式类

1. supervised / distant-supervised / unsupervised / self-supervised 的定义和区别

2. self-supervised 为什么重要
- 现代大模型预训练的重要基础

3. corpus / dataset 的作用
- 为观察语言规律、建模概率、训练模型提供基础

### 6.6 概率与表示类

1. Naïve Bayes、conditional independence、n-gram、argmax 是什么层面的关键词
- 它们属于统计 NLP 的核心概念群。

2. logits 与 softmax 的关系
- 神经网络先输出 logits，再用 softmax 转为概率分布。

3. one-hot 与 word vector 的关系
- 从离散表示走向稠密语义表示。

### 6.7 资源与工具类

1. NLTK 常见演示功能
- tokenization
- POS tagging
- chunking
- stemming
- lemmatisation
- WordNet
- SentiWordNet
- stopword removal
- wordcloud

2. spaCy 常见演示功能
- token/lemma/POS/dependency/entity/sentence boundaries
- matcher / PhraseMatcher
- ontology matching
- similarity

3. HuggingFace 常见演示功能
- text classification
- QA
- NER
- summarisation

4. WordNet 是什么
- 词汇数据库，按 synset 组织词义，并通过语义关系连接。

### 6.8 现代 LLM 类

1. BERT 与 GPT 的结构定位
- BERT：encoder-only
- GPT：decoder-only

2. Transformer 在课程里的定位
- 是现代神经 NLP 的关键架构基础

3. PTLM / foundation model / LLM 的关系
- 课件把它们放在预训练语言模型的大框架下理解

4. API-based LLM use 的意义
- 很多真实系统通过 API 使用模型，而非从零训练

### 6.9 风险与伦理类

1. hallucination 的基本定义
- 事实错误 / 语义不一致 / 无依据生成

2. jailbreaking 的定义
- 绕过安全机制，诱导模型产生不当输出

3. ethical considerations 三大关键词
- bias
- privacy
- transparency

4. 现代偏差问题示例
- gender bias
- dialectal bias

5. 数据泄露风险
- 企业/个人敏感内容输入外部生成式 AI 可能泄露

6. 新范式
- transparency-oriented systems
- agentic AI

### 6.10 课程规则类考点

这些不一定是“理论题”，但常常会被问到：

- weekly quiz 的开放时间
- sample quiz 是否计分
- final exam 的及格门槛
- group project 的组队规模、时间线、交付物

---

## 7. 易混淆点与复习建议

### 7.1 易混淆点

1. `task` 和 `model` 不要混淆
- POS tagging 是任务
- BERT / HMM / SVM 是模型

2. `semantic` 和 `pragmatic` 不要混淆
- semantic 更偏字面意义
- pragmatic 更偏言外之意、讽刺、上下文意图

3. `unsupervised` 和 `self-supervised` 不要混淆
- self-supervised 仍然有训练目标，只是目标来自数据本身

4. `WordNet` 不是模型
- 它是词汇知识库/词汇数据库

5. `QA pipeline` 不一定是生成式模型
- notebook 里的 QA 是抽取式 span selection

6. `black-box library` 不等于“没有理论”
- Week 1 只是暂时把它视为输入输出系统，后面课程会拆解内部原理

### 7.2 复习建议

建议按下面顺序复习 Week 1：

1. 先背课程主线
- NLP 是做什么的
- 为什么核心是 ambiguity resolution
- 为什么要从三代方法去理解 NLP

2. 再背术语
- NLU/NLG
- supervised/distant/self-supervised
- hallucination/jailbreaking/bias/privacy/transparency

3. 然后把任务分层
- linguistic tasks
- downstream tasks
- conversational AI tasks

4. 最后做工具映射
- NLTK 做基础处理
- spaCy 做工业级 pipeline + matching
- HuggingFace 做预训练模型与 pipeline 调用

---

## 8. 一句话总括 Week 1

Week 1 的核心不是教你一个具体模型，而是建立一个完整认知框架：

- NLP 研究“机器如何处理人类语言”
- 语言的核心挑战是 `ambiguity`
- 解决歧义经历了 `规则 -> 统计 -> 神经` 的演化
- 现代工具（NLTK、spaCy、HuggingFace、LLM APIs）让能力调用变容易，但并不意味着问题已被解决
- 真正的现代 NLP 还必须正视 `hallucination`、`jailbreaking`、`bias`、`privacy`、`transparency` 等问题

如果把这周内容压缩成最核心的一句，那就是：

**NLP 的本质，是在复杂、歧义、多样、不断演化的人类语言中，用计算方法做出合理解释与生成。**
