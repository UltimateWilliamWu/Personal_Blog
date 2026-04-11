# COMP6713 Week 7 POS Tagging and NER 中英对照笔记

说明：这份笔记以 `Week7-POSTagging-NER.pdf` 33 页课件为主线，并对照 `week7-demos.zip` 中的 BERT token classification、CRF POS tagger 和 BiLSTM-CRF demo 补全实现细节。每个知识点按“英文一句，中文一句”的顺序整理，便于理解、背诵和考试作答。

---

## 1. Announcements and Weekly Roadmap / 课程提醒与本周路线图

- The lecture begins with a Christopher Manning quote asking whether linguistics still matters after POS tagging accuracy rose from 97% toward 100%.
- 课件开头引用 Christopher Manning 的一句话，追问在 POS tagging 准确率接近 100% 之后，语言学是否仍然重要。

- The announcements congratulate students on completing the assignment and remind them to progress on the group project.
- announcement 页先祝贺大家完成了 assignment，并提醒大家继续推进 group project。

- The lecture also announces a talk by Dr. Raj Dabré from Google Sydney.
- 课件还宣布会有来自 Google Sydney 的 Dr. Raj Dabré 的 guest talk。

- It notes that Week 8 has a public holiday on Monday and that students should watch the videos shared earlier in the week.
- 课件说明 Week 8 的周一是 public holiday，学生需要提前观看本周分享的视频材料。

- The weekly roadmap lists introduction, task definition, tag sets, rule-based tagging, BERT-based sequence tagging, HMM, Markov chain, Viterbi decoding, CRF, BiLSTM+CRF, and special cases.
- 本周路线图依次列出 introduction、task definition、tag set、rule-based tagging、BERT-based sequence tagging、HMM、Markov chain、Viterbi decoding、CRF、BiLSTM+CRF 和 special cases。

---

## 2. Sequence Tagging as a Task Family / 序列标注任务家族

- Week 7 is positioned as the course module on sequence tagging or sequence labeling.
- Week 7 被定位为 sequence tagging 或 sequence labeling 的课程模块。

- The lecture explicitly contrasts Week 5 sequence classification with Week 7 sequence tagging.
- 课件明确对比了 Week 5 的 sequence classification 和 Week 7 的 sequence tagging。

- Sequence tagging means assigning a label to every unit in a sequence.
- sequence tagging 的定义是：给序列中的每一个单位分配一个标签。

- POS tagging and NER are the two canonical examples introduced this week.
- 本周介绍的两个经典例子分别是 POS tagging 和 NER。

- The lecture notes that transformer models perform these tasks under the token-classification setup.
- 课件指出，transformer 模型通常在 token-classification 的设置下完成这类任务。

- A quoted result from Ma and Hovy is used to show that strong neural models already reach very high performance on POS and NER.
- 课件引用 Ma and Hovy 的结果，说明强神经模型在 POS 和 NER 上已经能达到很高性能。

---

## 3. POS Tagging / 词性标注

- POS tagging is defined as assigning a part-of-speech tag to every word in a sentence.
- POS tagging 的定义是：给句子中的每个词分配一个词性标签。

- The lecture references the Penn Treebank and also mentions the Brown Corpus.
- 课件提到 Penn Treebank，也顺带提到了 Brown Corpus。

- The Penn Treebank is presented as a major annotated English resource with millions of words.
- Penn Treebank 被介绍为一个规模很大的英语标注资源，包含数百万词。

- The POS tagset slide reminds students that tags are linguistically meaningful and sometimes subtly defined.
- POS tagset 那页提醒学生，词性标签具有语言学含义，而且有些标签定义很细。

- One example in the slide compares `IN` with `TO` to show that tags are not always as obvious as they first appear.
- 课件用 `IN` 和 `TO` 的对比说明，词性标签并不总像表面看起来那么直观。

---

## 4. Named Entity Recognition / 命名实体识别

- NER is defined as tagging every word with an entity-related label.
- NER 的定义是给每个词分配一个和实体相关的标签。

- A named entity is introduced as an entity of a certain type.
- named entity 被定义为某种特定类型的实体。

- An NER tag indicates both whether the token belongs to an entity and what type that entity is.
- NER tag 同时说明一个 token 是否属于实体，以及它属于哪种实体类型。

- The lecture uses the B/I/O tagging scheme.
- 课件使用的是 B/I/O tagging scheme。

- `B` stands for beginning, `I` stands for inside, and `O` stands for outside.
- `B` 表示 beginning，`I` 表示 inside，`O` 表示 outside。

- The lecture explicitly notes that some tagsets also use `E` for end and `S` for single, but the course will restrict itself to B/I/O.
- 课件明确说明有些 tagset 还会使用 `E` 表示 end、`S` 表示 single，但本课程只使用 B/I/O。

- The example sentence about Commonwealth Bank of Australia shows that one surface string can contain both organisation and location mentions.
- 以 Commonwealth Bank of Australia 为例的句子展示了同一表面字符串中既可能出现 organisation，也可能出现 location。

- The lecture mentions the MUC tagset when discussing possible entity categories.
- 课件在介绍可能的实体类型时提到了 MUC tagset。

---

## 5. Ambiguity Resolution in POS and NER / POS 与 NER 中的歧义消解

- The lecture formulates tagging as selecting the best tag sequence `Y* = argmax P(Y|X)` for a sentence `X`.
- 课件把 tagging 形式化为：对输入句子 `X` 选择最佳标签序列 `Y* = argmax P(Y|X)`。

- In POS tagging, the same word may have multiple possible POS tags, such as `bank` as noun or verb.
- 在 POS tagging 中，同一个词可能对应多个可能的词性标签，例如 `bank` 可以是 noun 也可以是 verb。

- In NER, ambiguity can involve both whether something is an entity and what entity type it should receive.
- 在 NER 中，歧义既可能来自某个词是不是实体，也可能来自它到底属于哪种实体类型。

- The lecture decomposes sequence tagging into two components.
- 课件把 sequence tagging 分解成两个核心组成部分。

- The first component is information about the current word itself, roughly captured by terms like `P(y_i | x_i)`.
- 第一部分是关于当前词本身的信息，可以粗略理解为 `P(y_i | x_i)` 这类项。

- The second component is information about neighboring tags, which captures sequence constraints and tag dependencies.
- 第二部分是邻近标签的信息，它建模序列约束和标签之间的依赖关系。

- The lecture explicitly asks whether future tags should also matter, which motivates richer sequence models.
- 课件还明确追问未来标签是否也应该影响当前决策，这为更复杂的序列模型埋下伏笔。

---

## 6. Why POS and NER Matter / 为什么 POS 与 NER 重要

- The lecture explains that POS and NER help downstream tasks such as sentiment analysis, information retrieval, question answering, and information extraction.
- 课件说明 POS 和 NER 可以帮助 sentiment analysis、information retrieval、question answering 和 information extraction 等下游任务。

- POS tagging can help sentiment systems focus on adjectives and other relevant syntactic categories.
- POS tagging 可以帮助 sentiment system 更关注形容词等和情感密切相关的词类。

- NER can make retrieval systems distinguish between specific entities rather than broad string matches.
- NER 能帮助检索系统区分具体实体，而不是只做宽泛的字符串匹配。

- The lecture also observes that POS tagging performance is already very high, making error analysis and domain adaptation especially important.
- 课件还指出 POS tagging 的性能已经很高，因此 error analysis 和 domain adaptation 会变得更加重要。

---

## 7. Rule-Based and Lookup-Based Tagging / 基于规则与词典的标注方法

- A first obvious approach is to use lexicons and rules.
- 第一种显而易见的方法是使用 lexicon 和 rules。

- For POS tagging, a lexicon can list possible tags for a word.
- 对于 POS tagging，lexicon 可以列出一个词所有可能的词性标签。

- Rules can then use local context to choose among candidate tags.
- 接着可以用上下文规则在候选标签中做选择。

- The lecture gives a simple example in which `bank` is tagged as a noun if the preceding word is `a`, `an`, or `the`.
- 课件给出一个简单规则例子：如果 `bank` 前面是 `a`、`an` 或 `the`，它更可能是 noun。

- Brill tagging is cited as a classic rule-based POS approach.
- Brill tagging 被作为经典 rule-based POS 方法提及。

---

## 8. BERT for Token Classification / 用 BERT 做 Token Classification

- The lecture presents BERT as an obvious modern approach for sequence tagging.
- 课件把 BERT 作为 sequence tagging 的一个现代而直接的方案。

- Using BERT for NER requires changes relative to simple sentence classification.
- 用 BERT 做 NER 相比句子分类需要做一些调整。

- The lecture specifically mentions a case-sensitive tokenizer.
- 课件特别提到了 case-sensitive tokenizer。

- It also notes that one typically uses the representation of the first subword token to predict the label for a word.
- 课件还指出，通常会使用某个词的第一个 subword token 的表示来预测该词的标签。

- The BERT token-classification diagram shows tokens, subword pieces, final layer representations, and B/I/O labels predicted for each token position.
- BERT token-classification 那张图展示了 tokens、subword pieces、final layer representations，以及对每个 token 位置输出的 B/I/O 标签。

- The lecture again positions this as token-level multi-class classification.
- 课件再次强调，这本质上是 token-level 的 multi-class classification。

- The `1-ner-bert.ipynb` notebook loads the WNUT-17 dataset, inspects the label set, tokenizes inputs, aligns labels with subwords, and fine-tunes a transformer token-classification model.
- `1-ner-bert.ipynb` 演示了加载 WNUT-17 数据集、查看标签集合、对输入做 tokenization、把标签对齐到 subword，并微调 transformer token-classification 模型。

---

## 9. Datasets and the Bender Rule / 数据集与 Bender Rule

- The lecture lists POS datasets such as Penn Treebank and Universal Dependencies.
- 课件列举了 Penn Treebank 和 Universal Dependencies 等 POS 数据集。

- It lists NER datasets such as CoNLL, OntoNotes, and WNUT emerging-entity data.
- 它还列出了 CoNLL、OntoNotes 和 WNUT emerging-entity 数据等 NER 数据集。

- The lecture explicitly highlights the Bender Rule: always state the language of the dataset because English is not the default.
- 课件明确强调 Bender Rule：必须说明数据集的语言，因为 English is not the default。

- This is a research convention as well as an ethical and scientific reminder.
- 这既是研究写作规范，也是一个伦理和科学上的提醒。

---

## 10. Hidden Markov Models for Tagging / 用 HMM 做序列标注

- The lecture now moves to probabilistic sequence models and begins with HMM.
- 接下来课件转向概率序列模型，并从 HMM 开始讲起。

- The lecture introduces transition probability as the probability of moving from one tag to the next.
- 课件把 transition probability 定义为从一个标签转移到下一个标签的概率。

- It introduces observation likelihood as the probability of generating a word given a tag.
- 课件把 observation likelihood 定义为在给定标签时生成某个词的概率。

- The weather example is used to build intuition for Markov chains before switching to POS tags as hidden states.
- 课件先用天气例子建立 Markov chain 的直觉，再把 hidden states 换成 POS tags。

- In the HMM view of tagging, the tags are hidden states arranged in a Markov chain and the words are observations.
- 在 HMM 的 tagging 视角里，tags 是按 Markov chain 排列的 hidden states，而 words 是 observations。

- A central assumption is that a word depends only on its own tag.
- 一个核心假设是：每个词只依赖于它自己的 tag。

- Another central assumption is the Markov assumption over the hidden tag sequence.
- 另一个核心假设是 hidden tag sequence 满足 Markov assumption。

- The lecture states that HMM is a generative model because it models how tags generate words.
- 课件明确指出 HMM 是 generative model，因为它建模的是 tags 如何生成 words。

- The lecture also points out a limitation: HMM needs enough examples to estimate `P(w_i | t_i)` and does not directly use word features such as suffixes.
- 课件同时指出 HMM 的局限：它需要足够多的数据估计 `P(w_i | t_i)`，并且不能直接利用词缀这类 word features。

- The lecture uses simple ambiguous words such as `dance` and `people` to illustrate why sequence context matters.
- 课件使用 `dance` 和 `people` 这类歧义词来说明序列上下文的重要性。

- Viterbi is introduced as the dynamic-programming algorithm that finds the best state sequence for an observed word sequence.
- Viterbi 被介绍为一种 dynamic programming 算法，用来寻找给定 word sequence 的最佳 state sequence。

- The lecture explicitly refers to this as Viterbi decoding.
- 课件明确把这个过程称为 Viterbi decoding。

---

## 11. Conditional Random Fields / 条件随机场

- After HMM, the lecture introduces discriminative models and contrasts them with generative models.
- 在 HMM 之后，课件转向 discriminative models，并把它们和 generative models 做对比。

- Generative models are said to model a joint distribution, while discriminative models model a conditional distribution.
- 课件指出 generative models 建模 joint distribution，而 discriminative models 建模 conditional distribution。

- CRF is introduced as the main discriminative sequence-tagging model in the lecture.
- CRF 被介绍为本讲的主要 discriminative sequence-tagging 模型。

- In a CRF, words can be represented using features rather than only raw observation counts.
- 在 CRF 中，词可以通过 features 表示，而不只是依赖原始 observation counts。

- The lecture describes CRF as a finite-state model with unnormalized transition probabilities over a graph connecting words and tags.
- 课件把 CRF 描述为一种 finite-state model，其中 words 和 tags 在图结构上相连，使用未归一化的 transition probabilities。

- The graph for linear-chain CRF is a simple chain over neighboring tags.
- 线性链 CRF 的图结构就是在相邻标签之间构成的一条链。

- The argmax objective for CRF sums weighted features over possible tag sequences.
- CRF 的 argmax 目标是在所有可能标签序列上比较加权 feature 总和。

- The lecture emphasizes that a human designer selects the feature templates and the training algorithm learns the corresponding weights.
- 课件强调：由人工设计 feature template，而训练算法负责学习对应的权重。

- Example CRF features include the suffix of the current word and conjunctions of the current word’s suffix with the previous tag.
- CRF 的示例特征包括当前词的 suffix，以及当前词 suffix 和前一个 tag 的组合特征。

- The lecture notes that CRF MAP inference can be done with a modified Viterbi algorithm.
- 课件指出 CRF 的 MAP inference 可以通过 modified Viterbi 来完成。

- A key advantage of CRF is its ability to use arbitrary combinations of relevant tags and word features and to better handle unseen words.
- CRF 的一个关键优势是它能结合多种相关 tag 和 word features，并且更好地处理 unseen words。

- The `2-pos-tagger-crf.ipynb` notebook demonstrates hand-designed feature extraction, sentence-to-feature conversion, training with `pycrfsuite`, and prediction on POS-tagging examples.
- `2-pos-tagger-crf.ipynb` 演示了人工设计 feature extraction、把句子转成 feature 序列、使用 `pycrfsuite` 训练，以及做 POS tagging 预测。

---

## 12. BiLSTM plus CRF / BiLSTM 与 CRF 结合

- The lecture next asks whether neural models can remove the need for manual feature engineering.
- 接着课件追问：神经模型能否去掉人工 feature engineering 的需要。

- This motivates hybrid sequence tagging models such as BiLSTM+CRF.
- 这就引出了 BiLSTM+CRF 这样的 hybrid sequence tagging models。

- In BiLSTM+CRF, the BiLSTM produces hidden representations for every word position.
- 在 BiLSTM+CRF 中，BiLSTM 会为每个词位置生成 hidden representation。

- The CRF layer then uses those hidden representations as observation-side inputs while still modeling tag transitions.
- 然后 CRF 层把这些 hidden representation 当成 observation-side 输入，同时继续建模 tag transition。

- The lecture explicitly revisits the “two components” idea here: observation information plus transition information.
- 课件在这里再次回到了 “two components” 的思想，也就是 observation information 加上 transition information。

- Embedding dimensions effectively act like learned features of the observed word.
- embedding 的各个维度在这里相当于自动学出来的 observed word features。

- The lecture also highlights that subword information is valuable for POS and NER.
- 课件还特别强调 sub-word information 对 POS 和 NER 很有价值。

- The complete diagram includes word embeddings, character embeddings, concatenation, BiLSTM, and CRF.
- 完整架构图包含 word embeddings、character embeddings、concatenation、BiLSTM 和 CRF。

- The training algorithm referenced for this hybrid architecture is the forward-backward algorithm.
- 课件给这个 hybrid architecture 提到的训练算法是 forward-backward algorithm。

- The `3-bilstm-crf.ipynb` notebook implements a toy BiLSTM-CRF, builds a vocabulary, defines transition constraints, and trains on toy tagged sentences.
- `3-bilstm-crf.ipynb` 实现了一个 toy BiLSTM-CRF，构建词表、定义 transition constraints，并在 toy tagged sentences 上训练。

---

## 13. Special Cases and Frontier Issues / 特殊情况与前沿问题

- The lecture devotes a final section to special cases of POS tagging and NER.
- 课件最后专门留出一部分讨论 POS tagging 和 NER 的特殊情况。

- Social-media POS tagging is difficult because informal text may violate standard grammar, drop subjects, and invent creative spellings.
- social-media POS tagging 很难，因为非正式文本经常违反标准语法、省略主语并创造新拼写。

- The lecture asks whether the same grammatical tagset should always be used for such data.
- 课件专门追问，对于这类数据是否还应该无条件沿用传统 grammatical tagset。

- Word clustering and specialized features are suggested as ways to help tag unseen social-media words.
- word clustering 和专门设计的 features 被提出作为处理未见社交媒体词汇的方法。

- Domain-specific NER is highlighted as a special case because entities in medicine, law, or finance may not align with generic news-domain tagsets.
- domain-specific NER 被强调为一个 special case，因为医疗、法律、金融等领域的实体并不总能被通用新闻领域 tagset 覆盖。

- Nested NER is introduced through the example `COVID-19 Moderna vaccine`, where one span can contain another entity span.
- nested NER 通过 `COVID-19 Moderna vaccine` 这个例子被引入，说明一个 span 里可以嵌套另一个实体 span。

- Region classification is mentioned as one approach for nested NER.
- region classification 被提到是处理 nested NER 的一种思路。

- The lecture also discusses unknown or emerging entities.
- 课件还讨论了 unknown 或 emerging entities 的问题。

- Retrieval-augmented or self-adaptive NER is presented as a way to query external information when the base model is uncertain.
- retrieval-augmented 或 self-adaptive NER 被介绍为一种在模型不确定时检索外部信息的做法。

---

## 14. High-Frequency Exam Points / 高频考点总结

- POS tagging and NER are sequence tagging tasks, not sequence classification tasks.
- POS tagging 和 NER 是 sequence tagging tasks，而不是 sequence classification tasks。

- In sequence tagging, every token receives a label.
- 在 sequence tagging 中，每个 token 都会获得一个标签。

- POS tagging predicts syntactic categories such as noun, verb, or adjective, whereas NER predicts entity-boundary and entity-type labels.
- POS tagging 预测 noun、verb、adjective 等句法类别，而 NER 预测实体边界和实体类型标签。

- NER commonly uses BIO tagging.
- NER 常用 BIO tagging scheme。

- Sequence tagging depends on both word-level evidence and neighboring-tag dependencies.
- sequence tagging 同时依赖词本身的信息以及相邻标签之间的依赖关系。

- HMM is a generative model using transition probabilities and observation likelihoods.
- HMM 是 generative model，核心由 transition probability 和 observation likelihood 构成。

- Viterbi decoding finds the best hidden tag sequence for an observed word sequence.
- Viterbi decoding 用来寻找给定 observed word sequence 的最佳 hidden tag sequence。

- CRF is a discriminative model that directly models conditional distributions and can use rich feature functions.
- CRF 是 discriminative model，直接建模 conditional distribution，并能使用丰富的 feature functions。

- BiLSTM+CRF replaces manual feature engineering with neural representations while retaining structured tag decoding.
- BiLSTM+CRF 用神经表示替代了手工特征，但仍保留结构化的标签解码。

- BERT token classification predicts one label per token, usually from subword-aware transformer representations.
- BERT token classification 是每个 token 预测一个标签，通常依赖 subword-aware 的 transformer 表示。

- Important special cases include social-media text, domain-specific entities, nested NER, and emerging entities.
- 重要 special cases 包括 social-media text、domain-specific entities、nested NER 和 emerging entities。

- The Bender Rule requires researchers to state dataset language explicitly.
- Bender Rule 要求研究者明确说明数据集语言。

---

## 15. Model Answers to Likely Exam Questions / 常见考题标准答案

### Q1. What is the difference between sequence classification and sequence tagging?

- Sequence classification assigns one label to an entire input sequence, whereas sequence tagging assigns one label to each token in the sequence.
- sequence classification 给整个输入序列分配一个标签，而 sequence tagging 给序列中的每个 token 分配一个标签。

### Q2. What is the objective of POS tagging?

- The objective of POS tagging is to assign the correct part-of-speech label to every word in a sentence.
- POS tagging 的目标是为句子中的每个词分配正确的 part-of-speech label。

### Q3. What is the objective of NER?

- The objective of NER is to identify entity spans and assign entity-type labels to them using token-level tagging schemes such as BIO.
- NER 的目标是识别实体 span，并通过 BIO 这类 token-level tagging scheme 给它们分配实体类型标签。

### Q4. What does the BIO scheme mean?

- In BIO, `B` marks the beginning of an entity, `I` marks a token inside an entity, and `O` marks tokens outside all entities.
- 在 BIO 中，`B` 表示实体开头，`I` 表示实体内部 token，`O` 表示不属于任何实体的 token。

### Q5. What are the two components of sequence tagging highlighted in the lecture?

- The two components are information about the current word itself and information about neighboring tags or sequence structure.
- 课件强调的两个组成部分是：当前词本身的信息，以及邻近标签或序列结构的信息。

### Q6. Why is HMM called a generative model?

- HMM is called a generative model because it models how hidden tags generate observed words through observation likelihoods while also modeling tag transitions.
- HMM 被称为 generative model，是因为它通过 observation likelihood 建模 hidden tags 如何生成 observed words，同时还建模标签之间的转移。

### Q7. What does Viterbi decoding do in HMM tagging?

- Viterbi decoding uses dynamic programming to compute the most likely hidden tag sequence for a given observed word sequence.
- 在 HMM tagging 中，Viterbi decoding 使用 dynamic programming 计算给定 observed word sequence 的最可能 hidden tag sequence。

### Q8. How is CRF different from HMM?

- CRF is discriminative rather than generative, models conditional distributions directly, and can incorporate rich hand-designed feature functions.
- CRF 与 HMM 的不同在于：它是 discriminative 而不是 generative，直接建模 conditional distribution，并且可以加入丰富的人工 feature functions。

### Q9. Why are features important in CRF?

- Features are important in CRF because they let the model use useful cues such as suffixes, previous tags, capitalization, and other combinations that HMM cannot easily encode.
- feature 在 CRF 中很重要，因为它让模型可以利用 suffix、previous tags、capitalization 等有用线索，而这些信息 HMM 很难直接编码。

### Q10. Why combine BiLSTM with CRF?

- BiLSTM is combined with CRF so that neural hidden states can replace manual observation features while the CRF still enforces structured dependencies among output tags.
- 把 BiLSTM 和 CRF 结合起来，是为了让神经 hidden state 取代手工 observation features，同时让 CRF 继续建模输出标签之间的结构依赖。

### Q11. Why is subword information useful in POS tagging and NER?

- Subword information is useful because morphology and character patterns often help determine tag identity, especially for rare or unseen words.
- subword information 很有用，因为 morphology 和字符模式经常能帮助判断标签，特别是面对稀有词和未见词时。

### Q12. What changes when BERT is used for NER instead of sentence classification?

- When BERT is used for NER, labels are predicted at token level, a case-sensitive tokenizer may be preferred, and subword-token alignment must be handled carefully.
- 当 BERT 用于 NER 而不是句子分类时，标签是在 token level 预测的，通常更偏好 case-sensitive tokenizer，并且必须仔细处理 subword 标签对齐。

### Q13. What are important special cases in POS tagging and NER?

- Important special cases include social-media POS tagging, domain-specific NER, nested NER, and NER for emerging or unknown entities.
- POS tagging 和 NER 中的重要 special cases 包括 social-media POS tagging、domain-specific NER、nested NER，以及面向 emerging 或 unknown entities 的 NER。

### Q14. What is the Bender Rule mentioned in the lecture?

- The Bender Rule is the research convention that the language of a dataset must always be stated explicitly because English should not be treated as the default.
- 课件提到的 Bender Rule 是一种研究规范：必须明确写出数据集的语言，因为 English 不应被当作默认语言。

### Q15. Why does Week 7 naturally lead into Week 8?

- Week 7 naturally leads into Week 8 because both input and output become sequences, and the course moves from sequence tagging to full sequence-to-sequence generation in machine translation.
- Week 7 很自然地过渡到 Week 8，因为输入和输出都逐渐变成序列，课程也从 sequence tagging 走向 machine translation 这种完整的 sequence-to-sequence generation。

---

## 16. One-Sentence Summary / 一句话总括 Week 7

- Week 7 explains how POS tagging and NER are sequence tagging problems that combine local word evidence with tag-sequence structure, and it surveys the progression from rules to HMM, CRF, BiLSTM+CRF, and BERT token classification.
- Week 7 说明了 POS tagging 和 NER 是把局部词信息与标签序列结构结合起来的 sequence tagging 问题，并系统梳理了从 rules 到 HMM、CRF、BiLSTM+CRF 再到 BERT token classification 的演进路径。
