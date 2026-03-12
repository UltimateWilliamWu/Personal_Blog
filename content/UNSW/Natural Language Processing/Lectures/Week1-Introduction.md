
## 1. 课程导入与课程信息 / Course Introduction and Logistics

### 1.1 课程开场 / Opening Idea

- The lecture opens with Turing’s question. Instead of asking “Can machines think?”, it asks whether a machine can behave like a human in linguistic interaction.
- 课件用图灵的问题开场，核心意思是，不直接问“机器能否思考”，而是问“机器能否在语言交互中表现得像人类”。

- This shows that language ability is a major window into machine intelligence, and NLP is a core field for studying that ability.
- 这说明语言能力是衡量机器智能的重要窗口，而 NLP 正是处理这种能力的核心方向。

### 1.2 课程基本信息 / Basic Course Information

- The course is `COMP6713 Natural Language Processing`, offered in `2026 T1`.
- 课程名称是 `COMP6713 Natural Language Processing`，学期是 `2026 T1`。

- The convener is `Dr. Aditya Joshi`, and technical questions should mainly go to the `WebCMS Forum`.
- 任课教师是 `Dr. Aditya Joshi`，技术问题主要走 `WebCMS Forum`。

- The course covers fundamental theory, practical applications, and modern LLM-related topics.
- 课程会同时关注基础理论、实际应用和现代 LLM 相关议题。

### 1.3 课程哲学 / Course Philosophy

- The course philosophy can be summarized with three questions: `What`, `How`, and `Why`.
- 课程哲学可以概括成三个问题：`What`、`How`、`Why`。

- `What` refers to language phenomena, `How` refers to computational models, and `Why` refers to the historical evolution of these methods.
- `What` 指语言现象是什么；`How` 指如何用计算模型处理；`Why` 指这些方法为何会这样演化。

### 1.4 学习目标 / Learning Objectives

- `CL01` requires you to describe NLP tasks such as POS tagging, sentiment analysis, information extraction, and machine translation, together with their ambiguity-resolution challenges.
- `CL01` 要求你能描述 NLP 任务，如词性标注、情感分析、信息抽取和机器翻译，并理解它们的歧义消解挑战。

- `CL02` requires you to explain typical NLP approaches, especially statistical and neural methods.
- `CL02` 要求你能解释典型 NLP 方法，尤其是统计方法和神经方法。

- `CL03` requires you to use NLP libraries to train models and perform inference.
- `CL03` 要求你会用 NLP 库训练模型并进行推理。

- `CL04` requires you to design an NLP solution for a real application, including task formulation, method selection, and evaluation strategy.
- `CL04` 要求你能针对实际应用设计一个 NLP 方案，包括问题建模、方法选择和评估策略。

### 1.5 为什么还要学经典 NLP / Why Study Classical NLP

- Even though we now have LLMs, the slides explicitly say `LLMs are far from perfect`, so classical NLP is still worth studying.
- 虽然现在有 LLM，但课件明确说 `LLMs are far from perfect`，所以经典 NLP 仍然值得学。

- Classical methods are still used in industry, and understanding them helps us understand why deep learning methods work.
- 经典方法在企业中仍然被使用，而且理解经典方法有助于理解深度学习方法为什么有效。

- The course uses the “three generations of NLP” view to help you understand how modern NLP emerged.
- 课程想通过“三代 NLP”的视角帮助你理解现代 NLP 的来龙去脉。

### 1.6 Assessment 结构 / Assessment Structure

- `Weekly Quizzes` are worth `20%`. They start in Week 2, are closed-book, allow one attempt, have no time limit, and are usually open from Wednesday noon to Monday noon.
- `Weekly Quizzes` 占 `20%`，从 Week 2 开始，闭卷、一次机会、无时间限制，开放时间通常是周三中午到周一中午。

- The `Assignment` is worth `10%`, is an individual programming task, released in Week 3 and due at the end of Week 5.
- `Assignment` 占 `10%`，是个人编程作业，Week 3 发布，Week 5 末截止。

- The `Group Project` is worth `25%`, has 4 to 5 students per group, is registered in Week 4, due in Week 10, and presented in Week 11.
- `Group Project` 占 `25%`，每组 4 到 5 人，Week 4 注册，Week 10 截止，Week 11 展示。

- The `Final Exam` is worth `45%`, and to pass the course, you must score more than `40%` on the final exam itself.
- `Final Exam` 占 `45%`，而且要想通过这门课，期末考试本身必须拿到 `40%` 以上。

### 1.7 本周提醒 / Week 1 Reminder

- There is no formal quiz or tutorial in Week 1, but a sample quiz will be available on Moodle and will not be graded.
- Week 1 没有正式 quiz 和 tutorial，但 sample quiz 会放到 Moodle，且不计分。

- From Week 2 onward, quizzes will cover Week 1 content, so Week 1 is not just a casual introduction.
- 从 Week 2 开始，quiz 会开始覆盖 Week 1 的内容，所以 Week 1 不是“随便看看”。

---

## 2. 什么是 NLP / What Is NLP

### 2.1 NLP 的定义 / Definition of NLP

- NLP is the branch of artificial intelligence that deals with the computational processing of human language.
- NLP 是人工智能中专门处理人类语言计算问题的分支。

- The slides also note that NLP overlaps significantly with `computational linguistics`, `human language technology`, and `text analytics`.
- 课件还提到它与 `computational linguistics`、`human language technology`、`text analytics` 有较大重叠。

- Natural languages are the languages used by humans, whereas artificial languages include programming languages and other formal systems.
- 自然语言是人类使用的语言，人工语言则是编程语言等形式化语言。

### 2.2 NLP Today / Modern NLP

- Modern NLP has already entered everyday life through systems such as Siri, ChatGPT, Grammarly, and spell checkers.
- 现代 NLP 已经进入日常生活，例如 Siri、ChatGPT、Grammarly、拼写检查器等。

- The lecture also highlights applications such as legal AI, epidemic monitoring, and AI companions, showing that NLP is deeply embedded in social systems.
- 课件还强调了法律 AI、疫情监测、AI companions 等应用，说明 NLP 已经深度进入社会系统。

### 2.3 NLP Yesterday / Historical NLP

- The lecture lists three historical milestones: `ELIZA (1964)`, `SYSTRAN (1968)`, and `IBM Watson (2006)`.
- 课件列举了三个历史节点：`ELIZA (1964)`、`SYSTRAN (1968)`、`IBM Watson (2006)`。

- This shows that language automation did not begin in the LLM era; it has a long historical trajectory.
- 这说明语言自动化并不是 LLM 时代才出现的，而是有长期历史积累。

### 2.4 语言本身的复杂性 / The Complexity of Language

- Language is used not only to transmit knowledge, but also to collaborate, express attitudes, build relationships, and even gossip.
- 语言不仅用于传递知识，也用于合作、表达态度、建立关系，甚至 gossip。

- Language also contains large internal variation, including native vs non-native use, dialect vs standard language, and formal vs informal register.
- 语言内部也有巨大差异，包括母语/非母语、方言/标准语、正式/非正式语域。

- This means NLP does not deal with a single clean static object, but with something complex, dynamic, and socially situated.
- 这意味着 NLP 处理的不是一个统一、干净、静态的对象，而是一个复杂、动态、社会化的对象。

### 2.5 词与语序 / Words and Word Order

- Words are the fundamental units of language, and writing systems allow linguistic knowledge to be transmitted across generations.
- 词是语言的基本单位，书写系统让语言知识得以跨代传播。

- The lecture reminds us that different languages have very different word orders, such as `SVO`, `SOV`, and `VSO`.
- 课件提醒，不同语言的语序差异很大，例如 `SVO`、`SOV`、`VSO`。

- Therefore, we cannot directly apply English structural intuitions to all languages.
- 因此，不能把英语的结构直觉直接套到所有语言上。

### 2.6 NLU 与 NLG / NLU and NLG

- NLP can be broadly divided into `Natural Language Understanding` and `Natural Language Generation`.
- NLP 可以粗略分成两类：`Natural Language Understanding` 和 `Natural Language Generation`。

- The former focuses on understanding, while the latter focuses on generation.
- 前者偏向“理解”，后者偏向“生成”。

- For example, text classification is closer to NLU, while machine translation and summarization are closer to NLG.
- 例如，文本分类更接近 NLU，而机器翻译和摘要更接近 NLG。

### 2.7 NLP 的三维框架 / A Three-Dimensional View of NLP

- The lecture presents NLP through three dimensions: `language`, `task`, and `model`.
- 课件用三个维度理解 NLP：`language`、`task`、`model`。

- Languages include English, Mandarin, and Hindi; tasks include sentiment analysis, QA, and POS tagging; models include HMM, SVM, and BERT.
- 语言例如 English、Mandarin、Hindi；任务例如 sentiment analysis、QA、POS tagging；模型例如 HMM、SVM、BERT。

- In exams, be careful not to confuse tasks, models, and languages.
- 考试中要特别注意不要把任务、模型和语言混淆。

### 2.8 Black-box View / 黑盒视角

- Week 1 first treats NLP systems as black boxes, focusing on inputs and outputs before discussing internal mechanisms.
- Week 1 先把 NLP 系统当作黑盒，即只看输入和输出，不先讨论内部细节。

- For example, spell correction can be seen as “input a sentence, output possible corrections”, and an LLM can be seen as “input a question, output a response”.
- 例如，拼写纠错可以看成“输入一个句子，输出可能的纠正候选”；LLM 可以看成“输入一个问题，输出一个回答”。

---

## 3. 语言学任务与下游任务 / Linguistic Tasks and Downstream Tasks

### 3.1 语言学任务 / Linguistic Tasks

- The lecture first introduces classic linguistic tasks such as `POS tagging`, `chunking`, `parsing`, and `co-reference resolution`.
- 课件先介绍了一些经典语言学任务，如 `POS tagging`、`chunking`、`parsing`、`co-reference resolution`。

- These tasks are often not final products themselves, but they serve as foundational capabilities for more complex applications.
- 这些任务常常不是最终产品，但它们是很多复杂应用的基础能力。

#### POS tagging
- `POS tagging` assigns a part-of-speech tag to each word in a sentence.
- `POS tagging` 是给句子中的每个词打词性标签。

#### Chunking
- `chunking` groups words into phrase chunks, such as noun phrases.
- `chunking` 是把词组合成短语块，比如识别名词短语。

#### Parsing
- `parsing` constructs a syntactic structure, such as a dependency tree or parse tree.
- `parsing` 是构建句法结构，比如依存树或句法树。

#### Co-reference resolution
- `co-reference resolution` links pronouns and other referring expressions to the entities they refer to.
- `co-reference resolution` 是把代词等指代表达和它真正指向的实体连接起来。

### 3.2 歧义层级 / Ambiguity Hierarchy

- The lecture points out that these tasks correspond to lower levels of ambiguity processing.
- 课件指出，上述任务对应较低层次的歧义处理。

- The ambiguity hierarchy includes `phonological`, `morphological`, `lexical`, `semantic`, and `pragmatic` levels.
- 歧义层级包括：`phonological`、`morphological`、`lexical`、`semantic`、`pragmatic`。

- `semantic` is closer to literal meaning, while `pragmatic` is closer to the speaker’s intended meaning in context.
- `semantic` 更接近字面意义，而 `pragmatic` 更接近上下文中的真实意图。

### 3.3 下游任务 / Downstream Tasks

- The lecture emphasizes that NLP gradually shifted from purely linguistic tasks to application-oriented `downstream tasks`.
- 课件强调，NLP 的研究重心后来逐渐从语言学任务转向应用导向任务，也就是 `downstream tasks`。

- Typical downstream tasks include sentiment analysis, information extraction, named entity recognition, paraphrase detection, machine translation, summarization, and question answering.
- 典型下游任务包括情感分析、信息抽取、命名实体识别、释义检测、机器翻译、摘要和问答。

- In conversational AI, QA and document QA are important tasks, showing that NLP has moved from sentence-level processing to document-level and interactive processing.
- 在会话 AI 中，问答和 document QA 是重要任务，说明 NLP 已经从句子级处理走向文档级与交互级处理。

### 3.4 多语言思维 / Multilingual Thinking

- The lecture explicitly reminds us that although the course focuses on English, we should constantly ask whether a method also works in other languages.
- 课件特别提醒，虽然课程主要讲英语，但你应该不断思考：这个方法在其他语言上还成立吗？

- The key variables in cross-lingual thinking are `data`, `model`, and `linguistic phenomena`.
- 跨语言思考的关键变量是：`data`、`model`、`linguistic phenomena`。

---

## 4. 歧义、规则、数据与概率 / Ambiguity, Rules, Data, and Probability

### 4.1 为什么歧义是核心 / Why Ambiguity Is Central

- The lecture explicitly defines `ambiguity` as the property that a linguistic form may have multiple interpretations.
- 课件明确定义了 `ambiguity`，即一种语言形式可能有多种解释。

- One of the core tasks of NLP is to build computational methods that choose the correct interpretation among these alternatives.
- NLP 的核心任务之一就是构造计算方法，在这些可能解释中作出正确选择。

### 4.2 三类高频歧义 / Three Common Types of Ambiguity

#### Lexical ambiguity
- The same word may have multiple senses. For example, `love` means `0` in tennis scoring, but “affection” in ordinary usage.
- 同一个词可能有多个义项，例如 `love` 在网球比分里表示 `0`，在一般语境里表示“爱”。

#### Syntactic ambiguity
- The same sentence may have multiple syntactic structures, for example `I saw a boy with a telescope.`
- 同一句话可能有多种句法结构，例如 `I saw a boy with a telescope.`

#### Pragmatic ambiguity
- A sentence’s intended meaning may differ from its literal meaning, as in irony or sarcasm.
- 一句话的真实意思可能和字面意思不同，例如反讽表达。

### 4.3 断句问题 / Sentence Segmentation Problem

- The lecture uses sentence segmentation to show that tasks humans find easy are not necessarily easy for computers.
- 课件用断句任务说明，很多人类觉得简单的任务，对计算机并不简单。

- A period `.` may mark a sentence boundary, be part of an abbreviation, or function as a decimal point.
- 句号 `.` 既可能是句末，也可能是缩写的一部分，还可能是小数点。

- Therefore, “split at every period” is an overly crude rule.
- 所以“看到句号就断句”是一个过于粗糙的规则。

### 4.4 规则方法 / Rule-Based Approach

- Early NLP often relied on expert-written rules, which is the core idea of first-generation `rule-based NLP`.
- 早期 NLP 经常依赖专家手工写规则，这就是第一代 `rule-based NLP` 的核心思路。

- ELIZA is a representative historical example of this type of system.
- ELIZA 就是这类系统的代表性历史例子。

### 4.5 规则系统的优缺点 / Strengths and Weaknesses of Rules

- The advantage of rule-based methods is strong explainability, because you know why the system made a particular decision.
- 规则方法的优点是可解释性强，因为你知道系统为什么做出某个判断。

- The disadvantages are that rule-based methods are time-consuming, expert-dependent, subjective, and prone to overfitting a particular type of text.
- 规则方法的缺点是耗时、依赖专家、带有主观性，而且很容易过拟合某一类文本。

- The lecture specifically notes that rule-based systems often show `high precision, low recall`.
- 课件特别指出，规则系统常见现象是 `high precision, low recall`。

- Language constantly changes, so rules struggle to keep up with new words, new expressions, and new events.
- 语言是不断变化的，所以规则很难长期覆盖新词、新表达和新事件。

### 4.6 从规则走向数据 / From Rules to Data

- The lecture uses an Abma translation exercise to show that observing data can help us infer linguistic patterns.
- 课件通过 Abma 语言练习说明，观察数据可以帮助我们推断语言规律。

- This shows that ambiguity need not be handled only by expert rules; it can also be addressed through statistical regularities in data.
- 这说明解决歧义不一定只能靠专家规则，也可以靠数据中的统计规律。

- However, data can only support the phenomena it covers; when data is insufficient, uncertainty remains.
- 不过，数据只能支持它覆盖到的现象；数据不够时，不确定性仍然存在。

### 4.7 Corpus / Dataset 的意义 / The Role of Corpora and Datasets

- The lecture uses the Rosetta Stone as an analogy for early corpora and emphasizes that digitization and the internet greatly expanded data scale.
- 课件用 Rosetta Stone 类比早期语料资源，并强调数字化和互联网极大扩展了数据规模。

- Modern NLP depends on large amounts of data, but also faces practical issues such as crawler blocking, copyright, and restricted data access.
- 现代 NLP 依赖大量数据，但也面临网页封禁爬虫、版权和数据获取限制等现实问题。

### 4.8 学习范式术语 / Learning Paradigms

#### Supervised
- The data includes both inputs and target labels.
- 有输入，也有目标标签。

#### Distant-supervised
- The labels are not manually assigned item by item, but are created automatically through heuristics.
- 标签不是逐条人工标注，而是由某种启发式规则自动构造。

#### Unsupervised
- There are no target labels, only raw data.
- 没有目标标签，只有原始数据。

#### Self-supervised
- The supervision signal comes from the data itself, for example through masked prediction.
- 监督信号来自数据本身，例如掩码预测。

- `Self-supervised learning` is one of the core ideas behind modern large-model pre-training.
- `self-supervised learning` 是现代大模型预训练的核心思想之一。

### 4.9 概率进入 NLP / Probability Enters NLP

- At this point the lecture moves into statistical NLP, with keywords such as `Naive Bayes`, `conditional independence`, `n-grams`, and `argmax`.
- 课件从这里把主题推进到统计 NLP，关键词包括 `Naive Bayes`、`conditional independence`、`n-grams`、`argmax`。

- This means the system is no longer just “writing rules”; it estimates probabilities from data and then makes decisions using those probabilities.
- 这表示系统不再只是“写规则”，而是根据数据估计概率，再用概率进行决策。

### 4.10 logits、softmax 与向量表示 / Logits, Softmax, and Vector Representations

- In neural networks, the model usually outputs `logits` first, and then uses `softmax` to convert them into a probability distribution.
- 在神经网络里，模型通常先输出 `logits`，然后用 `softmax` 转成概率分布。

- The lecture also reminds us to move from discrete `one-hot vectors` to dense `word vectors`.
- 课件还提醒要从 `one-hot vector` 的离散表示，过渡到 `word vectors` 的稠密表示。

- This part serves as a bridge from statistical NLP to neural NLP.
- 这部分是从统计 NLP 走向神经 NLP 的桥梁。

---

## 5. 词汇资源与库工具 / Lexical Resources and NLP Libraries

### 5.1 Lexicons 的作用 / The Role of Lexicons

- The lecture reminds us that “data” in NLP includes not only raw text, but also structured lexical resources such as `WordNet`, `LIWC`, medical ontologies, and in-house company lexicons.
- 课件提醒，NLP 中的“数据”不只是原始文本，还包括结构化词汇资源，如 `WordNet`、`LIWC`、医学本体和企业内部词典。

- These resources can be represented as lists or graphs, and are often used for rule matching, feature engineering, and domain knowledge injection.
- 这些资源可以表示为 list 或 graph，并常用于规则匹配、特征工程和领域知识注入。

### 5.2 WordNet / WordNet

- `WordNet` is a lexical database for English that organizes word senses into `synsets` and links them via semantic relations.
- `WordNet` 是英语词汇数据库，它把词义组织成 `synsets`，并通过语义关系把它们连接起来。

- The relations you should remember include `synonymy`, `antonymy`, `hyponymy/hypernymy`, and `meronymy/holonymy`.
- 要记住的关系包括 `synonymy`、`antonymy`、`hyponymy/hypernymy`、`meronymy/holonymy`。

- WordNet is a knowledge resource, not a classification model.
- WordNet 是知识资源，不是分类模型。

### 5.3 NLTK demo / NLTK Demo

- In the lecture, `NLTK` is introduced as a foundational NLP toolkit that is suitable for demonstrations and for building text-processing pipelines.
- 课件中 `NLTK` 被介绍为一个基础性的 NLP 工具包，适合演示和搭建文本处理 pipeline。

- According to the notebook, the NLTK demo includes tokenization, POS tagging, chunking, stemming, lemmatization, WordNet, SentiWordNet, stopword removal, and word clouds.
- 对照 notebook，NLTK demo 包括分词、词性标注、chunking、stemming、lemmatisation、WordNet、SentiWordNet、停用词去除和词云。

- The purpose of this part is to let students see what basic NLP operations actually look like.
- 这部分的意义是先让学生看到“基础 NLP 操作长什么样”。

### 5.4 spaCy / spaCy

- `spaCy` is described in the lecture as `industrial-strength NLP`, emphasizing its suitability for real engineering settings.
- `spaCy` 被课件称为 `industrial-strength NLP`，强调它适合真实工程场景。

- It supports multiple languages, deep learning pipelines, and integration with LLMs.
- 它支持多语言、深度学习 pipeline，也能与 LLM 集成。

- According to the notebook, the spaCy demo shows tokens, lemmas, POS tags, dependencies, sentence boundaries, named entities, PhraseMatcher, and similarity computation.
- 对照 notebook，spaCy demo 展示了 token、lemma、POS、dependency、sentence boundary、named entities、PhraseMatcher 和相似度计算。

- The key point here is that rule-based methods have not disappeared in modern NLP; they are often packaged as matchers, patterns, and ontology-matching modules.
- 这里要记住：现代 NLP 里，规则方法并没有消失，而是常常被封装成 matcher、pattern、ontology matching 等模块。

### 5.5 HuggingFace / HuggingFace

- `HuggingFace` is introduced in the lecture as a platform for pre-trained/fine-tuned models and datasets.
- `HuggingFace` 在课件里被介绍为预训练/微调模型与数据集的平台。

- The `HuggingFace Hub` is a community repository that makes it easy to access models and datasets quickly.
- `HuggingFace Hub` 是一个社区共享仓库，方便快速获取模型和数据。

- According to the notebook, the HuggingFace demo includes text classification, question answering, named entity recognition, and summarization.
- 对照 notebook，HuggingFace demo 包括文本分类、问答、命名实体识别和摘要。

- Extractive QA is a high-frequency exam point because it selects an answer span from the context rather than generating an answer freely.
- 其中抽取式 QA 是高频考点，因为它是从上下文里选出答案片段，而不是自由生成。

---

## 6. 三代 NLP、Transformer 与 LLM / The Three Generations, Transformer, and LLMs

### 6.1 三代 NLP / The Three Generations of NLP

#### 第一代：规则驱动 / Generation 1: Rule-Based NLP
- The core is hand-written rules. The advantage is strong explainability, while the disadvantage is difficulty in adaptation and maintenance.
- 核心是人工编写规则，优点是可解释性强，缺点是迁移和维护困难。

#### 第二代：统计方法 / Generation 2: Statistical NLP
- The core is hand-crafted features, probabilistic modeling, and `argmax` decision-making.
- 核心是人工特征、概率建模和 `argmax` 决策。

#### 第三代：神经方法 / Generation 3: Neural NLP
- The core is learning distributed representations and model parameters from large-scale data, rather than relying heavily on explicit feature engineering.
- 核心是通过大规模数据学习分布式表示和模型参数，不再强依赖显式特征工程。

### 6.2 三代方法的对比 / Comparing the Three Generations

- Rule-based methods are the most interpretable but the most manually dependent; statistical methods start to use data and probability; neural methods rely most heavily on large-scale learning and representation power.
- 规则方法最可解释，但最依赖人工；统计方法开始利用数据和概率；神经方法最依赖大规模学习和表示能力。

- From the course perspective, these three generations do not replace one another cleanly; rather, they form a continuous evolutionary chain.
- 从课程视角看，这三代不是互相取代得干干净净，而是形成了一条连续演化链。

### 6.3 Transformer / Transformer

- The lecture emphasizes that the `Transformer` was originally introduced for NLP and later influenced the whole of AI.
- 课件强调，`Transformer` 最初是为 NLP 提出的架构，后来影响了整个 AI。

- Two representative model families are `BERT` and `GPT`.
- 两类代表模型是 `BERT` 和 `GPT`。

- `BERT` is an `encoder-only model`, while `GPT` is a `decoder-only model`.
- `BERT` 是 `encoder-only model`，`GPT` 是 `decoder-only model`。

### 6.4 神经 NLP pipeline / Neural NLP Pipeline

- The typical modern neural NLP pipeline is to perform `pre-training` on large unlabeled data, obtain a language model, and then adapt it using task-specific data.
- 现代神经 NLP 的典型流程是：先在大规模无标签数据上做 `pre-training`，得到语言模型，再用任务数据进行适配。

- The lecture refers to these models as `language models`, `foundation models`, `PTLMs`, or `LLMs`.
- 课件把这些模型称为 `language models`、`foundation models`、`PTLMs` 或 `LLMs`。

- Later lectures will explain in more detail how pre-training works and how models are adapted to specific tasks.
- 后续课程会进一步解释预训练如何进行，以及模型如何适配到具体任务。

### 6.5 API-based LLM Usage / 基于 API 的 LLM 使用方式

- The lecture points out that many commercial LLMs are provided through APIs rather than by directly giving users the model weights.
- 课件指出，很多商业 LLM 通过 API 提供，而不是把模型权重直接给用户。

- This means that modern NLP engineering often consists not of “training your own model”, but of “integrating an API into a system”.
- 这意味着现代 NLP 工程经常不是“自己训练一个模型”，而是“把 API 接到系统里”。

- The OpenAI API example in the lecture shows that prompt design is itself part of system design.
- 课件中的 OpenAI API 示例说明，prompt 设计也是系统设计的一部分。

---

## 7. 风险、伦理与新范式 / Risks, Ethics, and New Paradigms

### 7.1 NLP 不是已解决问题 / NLP Is Not a Solved Problem

- The lecture explicitly rejects the idea that NLP is solved just because web demos look impressive.
- 课件明确反对“web demo 看起来很强，所以 NLP 已经被解决”的想法。

- A system may be fluent without being correct, reliable, fair, or safe.
- 系统可能流畅，但并不一定正确、可靠、公平或安全。

### 7.2 Hallucination / 幻觉

- In generative models, `hallucination` refers to content that is factually incorrect or semantically inconsistent.
- 在生成模型中，`hallucination` 指模型产生事实错误或语义不一致的内容。

- This shows that sounding human-like in generation is not the same as being trustworthy.
- 这说明自然语言生成的“像人”不等于“可信”。

### 7.3 Jailbreaking / 越狱攻击

- `Jailbreaking` refers to bypassing a model’s safety mechanisms so that it produces content it should not produce.
- `jailbreaking` 是指绕过模型安全机制，让模型输出本不该输出的内容。

- This shows that safety is not an optional extra beyond model performance, but part of model capability itself.
- 这说明安全不是模型性能之外的附加问题，而是模型能力的一部分。

### 7.4 Bias / 偏差

- The lecture mentions `gender bias` and `dialectal bias` in modern NLP.
- 课件提到现代 NLP 中存在 `gender bias` 和 `dialectal bias`。

- This shows that models are not equally fair to all groups, and that language varieties and social attributes can affect system performance.
- 这说明模型不是对所有群体都同样公平，语言变体和社会属性会影响系统表现。

### 7.5 Privacy / 隐私

- The lecture uses the Samsung case to show that employees can cause serious leaks by inputting company data into generative AI systems.
- 课件用 Samsung 的案例说明，员工把企业数据输入生成式 AI 可能造成严重泄露。

- Therefore, data governance and access control are also central issues in modern NLP.
- 所以在现代 NLP 中，数据治理和访问控制同样是核心问题。

### 7.6 Transparency / 透明性

- The lecture treats `transparency` as an important direction, emphasizing that systems should not only give answers but also better explain their evidence and sources.
- 课件把 `transparency` 作为重要方向，强调系统不仅要给答案，还要更好地说明依据和来源。

### 7.7 Agentic AI / 代理式 AI

- `Agentic AI` refers not only to answering questions, but also to planning, acting, and executing tasks.
- `Agentic AI` 指的不只是回答问题，而是还会规划、行动、执行任务。

- This can be seen as the evolution of NLP systems from “generating text” toward “completing tasks”.
- 这可以看作 NLP 系统从“生成文本”进一步走向“完成任务”。

---

## 8. 考前背诵清单 / Memorization Checklist

### 8.1 必背定义 / Must-Memorize Definitions

- What is NLP?
- NLP 是什么？

- What is the difference between NLU and NLG?
- NLU 和 NLG 的区别是什么？

- What is ambiguity?
- 什么是 ambiguity？

- What are supervised, distant-supervised, unsupervised, and self-supervised learning?
- 什么是 supervised、distant-supervised、unsupervised、self-supervised？

### 8.2 必会区分 / Must-Be-Able-To Distinguish

- Lexical ambiguity, syntactic ambiguity, and pragmatic ambiguity.
- 词汇歧义、句法歧义、语用歧义。

- Linguistic tasks versus downstream tasks.
- 语言学任务与下游任务。

- Rule-based, statistical, and neural methods.
- 规则方法、统计方法、神经方法。

- BERT versus GPT.
- BERT 与 GPT。

- Extractive QA versus generative answering.
- 抽取式 QA 与生成式回答。

### 8.3 必会解释 / Must Be Able to Explain

- Why is ambiguity resolution central to NLP?
- 为什么说歧义消解是 NLP 的核心？

- Why are rule-based methods insufficient?
- 为什么规则方法不够？

- Why do data and probability drive the development of NLP?
- 为什么数据和概率会推动 NLP 发展？

- Why can we still say that modern NLP is “far from solved”?
- 为什么说现代 NLP 仍然“远未解决”？

### 8.4 必记工具映射 / Must-Remember Tool Mapping

- `NLTK` is more suitable for understanding basic NLP operations and traditional resources.
- `NLTK` 更适合理解基础 NLP 操作与传统资源。

- `spaCy` is more oriented toward engineering pipelines and matching systems.
- `spaCy` 更偏工程化 pipeline 和匹配系统。

- `HuggingFace` is more oriented toward pre-trained models and modern task pipelines.
- `HuggingFace` 更偏预训练模型与现代任务调用。

---

## 9. 一句话总结 / One-Sentence Summary

- The core of Week 1 is to build a big-picture framework: language is inherently ambiguous, and NLP is the ongoing effort to improve the computational handling of that ambiguity through rules, data, probability, and models.
- Week 1 的核心是在建立一个大框架：语言天然有歧义，NLP 就是在用规则、数据、概率和模型不断改进这种歧义的计算处理方式。

- From the course perspective, what matters most is not memorizing one model, but understanding why NLP evolved from rules to statistics, and then to neural methods and LLMs.
- 从课程角度看，真正重要的不是死记一个模型，而是理解 NLP 为什么会从规则走到统计，再走到神经和 LLM。

