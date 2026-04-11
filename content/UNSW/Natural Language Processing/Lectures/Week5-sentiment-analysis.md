# COMP6713 Week 5 Sentiment Analysis 中英对照笔记

说明：这份笔记以 `Week5-sentiment-analysis.pdf` 33 页课件为主线，并对照 `Week_5.zip` 中的 rule-based、statistical、neural 和 prompt tuning demo 补全实现细节。每个知识点按“英文一句，中文一句”的顺序整理，便于理解、背诵和考试作答。

---

## 1. Announcements and Weekly Roadmap / 课程提醒与本周路线图

- The lecture begins with a quote from Pang and Lee about how the web makes large-scale public opinion accessible.
- 课件一开始引用了 Pang 和 Lee 的观点，强调互联网让大规模公众意见变得可获取。

- The announcement slide thanks students for registering project teams and notes that unregistered students will be paired later.
- announcement 页感谢大家完成 project team 注册，并说明未注册的同学之后会被安排配组。

- The slide also states that there are no lectures, tutorials, or consultation in Week 6 because of flexi week.
- 课件还说明，由于 flexi week，Week 6 没有 lecture、tutorial 和 consultation。

- The assignment due date shown again is Friday, 20 March 2026, at 5:00 PM.
- 课件再次强调作业截止时间是 2026 年 3 月 20 日周五下午 5 点。

- The roadmap for this week includes formulations of sentiment analysis, lexicons and datasets, rule-based and statistical SA, feature engineering, neural SA, BERT-based fine-tuning, and prompt-based methods.
- 本周路线图包括 sentiment analysis 的任务形式、lexicons and datasets、rule-based 和 statistical SA、feature engineering、neural SA、BERT 微调，以及 prompt-based 方法。

- The lecture situates Week 5 as the first downstream task module after foundations and language models.
- 课件把 Week 5 定位为在基础理论和语言模型之后进入的第一个下游任务模块。

- The rationale slide says sentiment analysis is a sequence classification task that maps text to a single label.
- rationale 页明确指出，sentiment analysis 是一个 sequence classification task，也就是把文本映射成单个标签。

---

## 2. What Sentiment Analysis Covers / Sentiment Analysis 到底涵盖什么

- Sentiment analysis is introduced as an umbrella term for text-based affective computing.
- sentiment analysis 被定义为 text-based affective computing 的 umbrella term。

- Affective computing is broader than text and concerns enabling computers to understand and express emotion.
- affective computing 的范围比文本更广，核心是让计算机理解和表达情绪。

- The lecture defines sentiment as the polarity of opinion.
- 课件把 sentiment 定义为 opinion 的 polarity，也就是意见倾向。

- The most popular version of SA is Boolean sentiment classification, but the lecture repeatedly stresses that SA is more than Boolean classification.
- 最常见的版本是 Boolean sentiment classification，但课件反复强调 SA 绝不只是二分类。

- Sentiment analysis includes applications in both commercial and non-commercial settings.
- sentiment analysis 同时具有商业场景和非商业场景的应用价值。

- Commercial use cases include brand reputation management, call center analytics, content moderation, and customer relations.
- 商业场景包括品牌声誉管理、呼叫中心分析、内容审核和客户关系管理。

- Non-commercial use cases include analysis of public debates, disaster or outbreak monitoring, and analysis of literature or art.
- 非商业场景包括公共议题分析、灾害或疫情早期监测，以及文学艺术分析。

- The lecture explicitly asks students to think beyond simple product-review positivity and negativity.
- 课件明确要求学生不要把 SA 仅仅理解为商品评论的正负面判断。

---

## 3. Formulations and Related Tasks / 任务形式与相关子任务

- The lecture lists Boolean sentiment, multi-class sentiment, aspect-based sentiment, and domain-specific sentiment as core formulations.
- 课件列出的核心任务形式包括 Boolean sentiment、多分类情感、aspect-based sentiment 和 domain-specific sentiment。

- Multi-class sentiment extends the label space beyond positive and negative, for example to strongly positive or neutral.
- 多分类情感会把标签空间扩展到 positive 和 negative 之外，例如 strongly positive 或 neutral。

- Aspect-based sentiment analysis predicts sentiment toward a specific aspect rather than the whole sentence.
- aspect-based sentiment analysis 关注的是句子中某个 aspect 的情感，而不是整句的总体情感。

- Domain-specific sentiment analysis depends on domain conventions, such as health mentions or customer support messages.
- domain-specific sentiment analysis 强依赖领域特性，例如健康相关文本或客服对话。

- The lecture also includes implicit polarity detection, speaker-side sentiment detection, emotion detection, sarcasm detection, and stance detection.
- 课件还涵盖 implicit polarity detection、speaker-side sentiment detection、emotion detection、sarcasm detection 和 stance detection。

- Implicit polarity detection covers cases where sentiment is implied rather than stated directly.
- implicit polarity detection 处理的是情感没有被直接说出来、而是通过暗示体现出来的情况。

- Speaker-side sentiment detection asks whose sentiment is being modeled and whether the speaker is the opinion holder.
- speaker-side sentiment detection 要求区分情感到底来自谁，以及 speaker 是否就是 opinion holder。

- Emotion detection predicts categories such as joy, anger, surprise, fear, disgust, or sadness rather than coarse sentiment polarity.
- emotion detection 预测的是 joy、anger、surprise、fear、disgust、sadness 等情绪类别，而不是粗粒度的 polarity。

- Sarcasm detection identifies utterances whose literal surface meaning and intended sentiment diverge.
- sarcasm detection 要识别字面含义与真实情感相反的表达。

- Stance detection predicts whether a text is pro, anti, or neutral toward a target topic.
- stance detection 预测文本对某个目标议题是支持、反对还是中立。

- The “revisiting the tasks” slide also includes opinion mining and opinion quintuple extraction.
- revisiting the tasks 那页还包含 opinion mining 和 opinion quintuple extraction。

- Opinion mining may be represented as tuples such as holder, target, aspect, polarity, and time.
- opinion mining 可以表示成 holder、target、aspect、polarity、time 这样的结构化五元组。

---

## 4. Challenges and Ambiguity in SA / SA 中的难点与歧义

- The lecture highlights semantic ambiguity, sarcasm, thwarting, temporality, target specificity, and new terms as major challenges.
- 课件把 semantic ambiguity、sarcasm、thwarting、temporality、target specificity 和 new terms 列为主要挑战。

- Semantic ambiguity means a word or phrase may carry different sentiment implications in different contexts.
- semantic ambiguity 指的是同一个词或表达在不同上下文里可能具有不同的情感含义。

- Sarcasm is difficult because the literal wording and intended attitude conflict.
- sarcasm 难是因为字面内容和真实态度是冲突的。

- Thwarting refers to long contexts whose sentiment flips near the end.
- thwarting 指的是长文本在后部突然发生情感翻转。

- Temporality matters because a sentence that sounded positive historically may no longer be positive today.
- temporality 很重要，因为一个在过去听起来是正面的表达，现在未必还是正面。

- Target specificity matters because sentiment toward one entity may be expressed via comparison with another entity.
- target specificity 很重要，因为针对某个实体的情感常常通过和另一个实体对比来表达。

- New terms matter because slang and emergent vocabulary may not exist in lexicons or training data.
- new terms 很关键，因为俚语和新兴词汇往往不在 lexicon 或训练数据里。

- The lecture gives exercises requiring students to invent sentences illustrating ambiguity, sarcasm, temporality, and target specificity.
- 课件专门设计练习，让学生自己编写体现 ambiguity、sarcasm、temporality 和 target specificity 的句子。

---

## 5. Opinion Structure and Emotion Modeling / 观点结构与情绪建模

- The lecture introduces the opinion quintuple as a richer representation than a single sentiment label.
- 课件引入 opinion quintuple，说明它比单一 sentiment label 更丰富。

- The quintuple contains opinion holder, target, aspect, valence, and time.
- 这个 quintuple 包含 opinion holder、target、aspect、valence 和 time。

- A single text may contain multiple opinions with different targets and times.
- 同一段文本可能同时包含多个针对不同目标、不同时间点的 opinion。

- The lecture also introduces emotion models such as Ekman’s six basic emotions and Plutchik’s wheel of emotions.
- 课件还介绍了 Ekman 的六种基本情绪和 Plutchik 的情绪轮等情绪理论。

- VAD stands for valence, arousal, and dominance.
- VAD 指的是 valence、arousal 和 dominance。

- Valence measures pleasantness, arousal measures intensity, and dominance measures control.
- valence 表示愉悦程度，arousal 表示强度，dominance 表示控制感。

- The VAD discussion reminds students that affect can be represented on continuous dimensions rather than discrete categories alone.
- VAD 的讨论提醒学生，affect 不一定只能用离散类别表示，也可以用连续维度建模。

---

## 6. Sentiment Lexicons and Datasets / 情感词典与数据集

- Sentiment lexicons are structured or unstructured dictionaries of sentiment-bearing words.
- sentiment lexicons 是包含情感信息词汇的结构化或非结构化词典资源。

- LIWC is presented as a curated dictionary of word categories and emotions.
- LIWC 被介绍为一种人工整理的词类别和情绪词典。

- SentiWordNet labels WordNet synsets with positive, negative, and objective scores.
- SentiWordNet 会给 WordNet synset 标上 positive、negative 和 objective 三类分数。

- The creation of SentiWordNet is described as a multi-step process involving seed synsets, expansion through WordNet relations, and classifier-based propagation.
- SentiWordNet 的构建过程被描述为：先有 seed synset，再通过 WordNet 关系扩展，最后借助分类器传播情感分数。

- NRC Emotion Lexicon associates words with emotions and VAD-like affective dimensions.
- NRC Emotion Lexicon 把词汇和情绪类别以及类似 VAD 的情绪维度对应起来。

- Example datasets include SST-2, Amazon Reviews, and Sentiment140.
- 例子数据集包括 SST-2、Amazon Reviews 和 Sentiment140。

- SST-2 contains movie-review sentences and Boolean sentiment labels.
- SST-2 包含来自电影评论的句子以及 Boolean sentiment 标签。

- Amazon Reviews is much larger and provides user ratings over many domains.
- Amazon Reviews 更大，并且覆盖许多不同领域的用户评分数据。

- Sentiment140 uses distant supervision on tweets.
- Sentiment140 使用 distant supervision 给 tweets 打标签。

- The dataset creation slides cover topic selection, time period selection, hashtag selection, manual annotation, distant supervision, and crowdsourcing.
- 数据集构建部分涵盖 topic 选择、时间范围、hashtag 选择、manual annotation、distant supervision 和 crowdsourcing。

- The lecture stresses ethics review, held-out data, annotator suitability, annotator diversity, and inter-annotator agreement.
- 课件强调 ethics review、held-out dataset、annotator suitability、annotator diversity 以及 inter-annotator agreement 的重要性。

- Cohen’s Kappa is introduced as one metric for inter-annotator agreement.
- Cohen’s Kappa 被介绍为衡量 inter-annotator agreement 的一个指标。

---

## 7. Evaluation for SA / SA 的评测方式

- The lecture lists cross-validation and held-out evaluation as standard evaluation protocols.
- 课件把 cross-validation 和 held-out evaluation 列为标准评测协议。

- Precision measures the proportion of predicted positives that are actually correct.
- precision 衡量的是被预测为正类的样本中有多少是真的正确的。

- Recall measures the proportion of true positives that the system successfully retrieved.
- recall 衡量的是所有真实正类中有多少被系统成功找回。

- F-score is the harmonic mean of precision and recall.
- F-score 是 precision 和 recall 的调和平均。

- The lecture includes numerical exercises where students compute class-wise precision and recall from confusion-style tables.
- 课件包含具体练习，让学生根据类似混淆矩阵的表格计算 precision 和 recall。

- Evaluation is linked to dataset quality because poor labels can invalidate the metric values.
- 评测与数据质量直接相关，因为低质量标签会使指标失去意义。

---

## 8. Rule-Based Sentiment Analysis / 基于规则的情感分析

- Rule-based sentiment analysis uses hand-crafted rules to predict sentiment.
- rule-based sentiment analysis 使用人工编写的规则来预测情感。

- A typical word-level pipeline looks up a sentiment lexicon and resolves word sense ambiguity if needed.
- 典型的词级流程会先查 sentiment lexicon，并在需要时处理词义歧义。

- A sentence-level rule system may count positive and negative words.
- 句子级规则系统通常会统计 positive 和 negative 词的数量。

- A document-level rule system may aggregate sentence-level sentiment and account for sentence position.
- 文档级规则系统会聚合句子级情感，并且可能考虑句子在文档中的位置。

- Additional rules may flip sentiment under negation.
- 额外规则可以在出现 negation 时翻转情感极性。

- Additional rules may also treat contrastive conjunctions such as “but” specially.
- 额外规则还可以专门处理像 “but” 这样的转折连词。

- The lecture explicitly asks students to think of their own rule sets.
- 课件明确要求学生自己思考可行的规则集合。

- The stated limitations are dependence on lexicon completeness and correctness, along with high precision but low recall.
- 课件明确指出其局限是过度依赖 lexicon 的完整性和正确性，并且通常 high precision but low recall。

- The `1-rule-based-sa.ipynb` notebook demonstrates SentiWordNet lookup, word-level score extraction, score aggregation, and simple sentence classification.
- `1-rule-based-sa.ipynb` 演示了 SentiWordNet 查询、词级得分提取、句级聚合以及简单句子分类。

---

## 9. Statistical Sentiment Analysis and Features / 统计式情感分析与特征工程

- Statistical SA converts text into a structured feature representation and learns a classifier from X to y.
- statistical SA 会先把文本变成结构化特征表示，再学习从 X 到 y 的分类器。

- The lecture gives Naïve Bayes and SVM as canonical examples.
- 课件把 Naïve Bayes 和 SVM 作为典型代表。

- Feature engineering means that a human designer decides what textual properties should be represented explicitly.
- feature engineering 指的是由人工设计者决定哪些文本属性应被显式表示出来。

- Example feature types include one-hot vectors, term frequency, TF-IDF, unigrams, bigrams, POS tags, word embeddings, and engineered cues such as emojis or capitalization.
- 例子特征包括 one-hot、term frequency、TF-IDF、unigrams、bigrams、POS tags、word embeddings，以及 emoji、capitalization 这类人工特征。

- The lecture contrasts raw frequency counts with embedding-based sentence representations.
- 课件对比了原始词频统计和基于 embedding 的句子表示。

- Word embeddings can also be used as features rather than as end-to-end trainable representations.
- word embeddings 也可以作为 feature 使用，而不一定是 end-to-end 训练的一部分。

- The sarcasm example combines unigrams, qualitative features, and embedding-based similarity features before SVM classification.
- 讽刺识别的例子把 unigrams、定性特征以及 embedding 相似度特征拼接后交给 SVM 分类。

- The `2-statistical-sentiment-analysis.ipynb` notebook loads SST-2, creates TF-IDF features, splits train/test data, and trains a standard classifier.
- `2-statistical-sentiment-analysis.ipynb` 演示了加载 SST-2、构建 TF-IDF 特征、划分训练测试集，并训练标准分类器。

---

## 10. Neural SA Before Decoder Models / Decoder 时代之前的神经情感分析

- Neural approaches to SA include sequential chains based on RNNs, LSTMs, or CNNs, as well as encoder-based fine-tuning.
- neural SA 包括基于 RNN、LSTM、CNN 的顺序链模型，以及 encoder-based fine-tuning。

- The lecture labels these as “pre-decoder SA” to distinguish them from prompt-based decoder usage.
- 课件把这些方法称为 “pre-decoder SA”，用来和后面的 decoder/prompt 方法区分。

- Linear chain models perform classification after reading a sequence representation.
- linear chain models 会先读取序列表示，再进行分类。

- Extensions include appended context, multi-task learning, and one-hot feature concatenation.
- 这些链式模型的扩展包括 appended context、multi-task learning 以及 one-hot feature concatenation。

- In aspect-specific sentiment classification, the aspect acts as additional context and its embedding may be appended to word embeddings or hidden states.
- 在 aspect-specific sentiment classification 中，aspect 会作为额外上下文，其 embedding 可以拼接到词向量或隐藏状态上。

- Attention allows all hidden states to contribute to the final prediction rather than using only the last hidden state.
- attention 允许所有 hidden states 共同参与最终预测，而不是只依赖最后一个 hidden state。

- Multi-task learning shares an encoder across related tasks while attaching task-specific heads.
- multi-task learning 会在相关任务之间共享 encoder，并为不同任务接 task-specific heads。

- The lecture’s example combines emotion detection with abusive language detection.
- 课件给出的 multi-task example 把 emotion detection 和 abusive language detection 结合起来。

- One-hot feature concatenation allows human-designed features such as sentiment-lexicon scores to be injected into neural models.
- one-hot feature concatenation 允许把情感词典得分这类人工特征注入神经模型。

- The figurative health-report example uses partitions and lexicon-based sentiment scores to help distinguish literal from figurative disease mention.
- figurative health-report 的例子使用文本分区表示和 lexicon 情感得分来区分字面疾病提及和比喻性提及。

- The `3-neural-sentiment-analysis.ipynb` notebook loads SST-2, tokenizes it with a pretrained tokenizer, and fine-tunes a transformer-based sentiment classifier.
- `3-neural-sentiment-analysis.ipynb` 演示了加载 SST-2、用预训练 tokenizer 进行 tokenization，并微调 transformer-based sentiment classifier。

---

## 11. Fine-Tuning BERT for Sentiment / 用 BERT 做情感分类

- The lecture shows BERT fine-tuning with a classification head on top of the `[CLS]` representation.
- 课件展示了在 `[CLS]` 表示上接分类头来做 BERT fine-tuning。

- The label is predicted from the final representation of the `[CLS]` token.
- 标签是根据 `[CLS]` token 的最终表示来预测的。

- The lecture notes that, in practice, updating only later layers may already be sufficient.
- 课件指出，在实践中有时只更新后面的几层就已经足够。

- BERT can also be combined with other neural modules rather than used alone.
- BERT 不一定必须单独使用，也可以和其他神经模块结合。

- One lecture example combines the `[CLS]` representation with user and product representations from graph neural networks.
- 课件中的一个例子把 `[CLS]` 表示和图神经网络得到的 user/product 表示结合起来。

- This illustrates a larger design pattern in which pretrained language models are fused with structured external information.
- 这说明了一个更大的设计模式：把 pretrained language models 和结构化外部信息融合起来。

---

## 12. Decoder-Based SA and Prompt Methods / 基于 Decoder 的 SA 与 Prompt 方法

- The lecture transitions from encoder fine-tuning to decoder-based sentiment analysis through prompting.
- 课件从 encoder fine-tuning 转向通过 prompting 使用 decoder-based 模型做 sentiment analysis。

- Zero-shot and few-shot prompting can already perform sentiment detection without gradient updates.
- zero-shot 和 few-shot prompting 已经可以在不更新参数的情况下完成 sentiment detection。

- However, a single prompt may not work well for complex tasks such as implicit sentiment detection.
- 但单个 prompt 对 implicit sentiment detection 这类复杂任务未必有效。

- The lecture therefore introduces chain-of-thought prompting for implicit sentiment reasoning.
- 因此课件引入 chain-of-thought prompting，用来处理隐式情感推理。

- The lecture then argues that human trial-and-error prompt writing is sub-optimal.
- 课件接着指出，靠人手工 trial-and-error 写 prompt 并不是最优策略。

- AutoPrompt is introduced as a search algorithm for finding trigger words automatically.
- AutoPrompt 被介绍为一种自动寻找 trigger words 的 prompt search 算法。

- The key intuition is that the prompt need not be a natural-sounding sentence if it can reliably trigger the desired output.
- 核心直觉是：如果某些提示词能稳定触发正确输出，那么 prompt 不一定非得是自然语言句子。

- Prompt tuning freezes the language model and learns only a small number of prompt tokens.
- prompt tuning 会冻结语言模型，只学习少量 prompt tokens。

- These prompt tokens are often called soft prompts because they are learnable vectors rather than discrete words.
- 这些 prompt tokens 常被称为 soft prompts，因为它们是可学习向量而不是离散词。

- The lecture explains prompt tuning as parameter-efficient tuning.
- 课件把 prompt tuning 明确归类为 parameter-efficient tuning。

- The “why prompt tuning works” slide compares learned prompt representations to dedicated task-conditioning vectors.
- “why prompt tuning works” 那页把学习到的 prompt 表示理解为一种 task-conditioning 向量。

- The “math of prompt tuning” slide emphasizes that only a very small number of parameters may need updating.
- “math of prompt tuning” 那页强调，真正需要更新的参数量可能非常小。

- DSPy is mentioned as a declarative framework that is especially convenient for prompt optimization.
- DSPy 被提及为一个特别适合做 prompt optimization 的 declarative framework。

- The `4-prompt-tuning-sentiment-analysis.ipynb` notebook uses `PromptTuningConfig`, attaches a prompt adapter to a pretrained model, and trains on the `tweet_eval` sentiment dataset.
- `4-prompt-tuning-sentiment-analysis.ipynb` 演示了使用 `PromptTuningConfig`、给预训练模型挂上 prompt adapter，并在 `tweet_eval` sentiment 数据集上训练。

---

## 13. Generalization Beyond Sentiment / 从情感分类推广到其他分类任务

- The lecture ends by generalizing sequence classification methods to tasks such as hate speech detection, misogyny detection, homophobia/transphobia detection, intent classification, email priority classification, and sarcasm classification.
- 课件最后把 sequence classification 的方法推广到 hate speech detection、misogyny detection、homophobia/transphobia detection、intent classification、email priority classification 和 sarcasm classification 等任务。

- This is conceptually important because the model families are reusable even when the labels change.
- 这一点在概念上很重要，因为即使标签空间改变，模型家族本身依然可以复用。

- Week 5 therefore serves as a bridge from language modeling into practical supervised classification.
- 因此 Week 5 起到了从 language modeling 走向实际监督分类任务的桥梁作用。

---

## 14. High-Frequency Exam Points / 高频考点总结

- Sentiment analysis is an umbrella term and is not limited to Boolean polarity classification.
- sentiment analysis 是 umbrella term，不能把它只等同于 Boolean polarity classification。

- Key SA formulations include Boolean, multi-class, aspect-based, domain-specific, emotion, sarcasm, stance, and opinion-mining tasks.
- 关键 SA 任务形式包括 Boolean、多分类、aspect-based、domain-specific、emotion、sarcasm、stance 和 opinion-mining。

- SentiWordNet assigns positive, negative, and objective scores to WordNet synsets.
- SentiWordNet 会为 WordNet synset 分配 positive、negative 和 objective 分数。

- Dataset quality depends on task definition, annotation strategy, ethics, and inter-annotator agreement.
- 数据集质量取决于 task definition、annotation strategy、ethics 以及 inter-annotator agreement。

- Rule-based SA is interpretable and precise but often limited by lexicon coverage and low recall.
- rule-based SA 可解释、精确，但经常受 lexicon coverage 限制并且 recall 偏低。

- Statistical SA relies on feature engineering and classifiers such as Naïve Bayes or SVM.
- statistical SA 依赖 feature engineering，以及 Naïve Bayes 或 SVM 等分类器。

- Word embeddings can be used either as learned representations or as handcrafted downstream features.
- word embeddings 既可以作为 learned representations 使用，也可以作为人工设计的下游 features 使用。

- Neural SA before decoder models includes RNN/LSTM/CNN chains, appended context, multi-task learning, and feature concatenation.
- decoder 模型普及前的 neural SA 包括 RNN/LSTM/CNN 链式模型、appended context、multi-task learning 和特征拼接。

- BERT-based sentiment analysis typically uses the `[CLS]` representation plus a classification head.
- 基于 BERT 的 sentiment analysis 通常使用 `[CLS]` 表示再接分类头。

- Decoder-based SA includes zero-shot/few-shot prompting, CoT prompting, AutoPrompt, and prompt tuning.
- decoder-based SA 包括 zero-shot/few-shot prompting、CoT prompting、AutoPrompt 和 prompt tuning。

- Prompt tuning freezes the model and learns only a small set of soft prompt vectors.
- prompt tuning 会冻结模型，只学习少量 soft prompt 向量。

- Sequence classification is a reusable modeling pattern that extends to many toxicity, abuse, intent, and priority tasks.
- sequence classification 是一种可复用的建模模式，可以推广到多种 toxicity、abuse、intent 和 priority 任务。

---

## 15. Model Answers to Likely Exam Questions / 常见考题标准答案

### Q1. Why does the lecture say sentiment analysis is an umbrella term?

- The lecture calls sentiment analysis an umbrella term because it includes many related affective tasks such as polarity classification, emotion detection, sarcasm detection, aspect-based SA, and stance detection rather than one single task.
- 课件把 sentiment analysis 称为 umbrella term，是因为它包含 polarity classification、emotion detection、sarcasm detection、aspect-based SA 和 stance detection 等多个相关任务，而不是单一任务。

### Q2. What is aspect-based sentiment analysis?

- Aspect-based sentiment analysis predicts the sentiment expressed toward a specific aspect of an entity instead of assigning one overall label to the entire text.
- aspect-based sentiment analysis 是针对实体的某个特定 aspect 预测情感，而不是给整段文本只打一个总体标签。

### Q3. What is the opinion quintuple?

- The opinion quintuple is a structured representation containing opinion holder, target, aspect, valence, and time.
- opinion quintuple 是一种结构化表示，包含 opinion holder、target、aspect、valence 和 time。

### Q4. What are sentiment lexicons used for?

- Sentiment lexicons provide prior affective information about words or synsets and are especially useful in rule-based systems and feature engineering.
- sentiment lexicons 为词或 synset 提供先验情感信息，尤其适用于 rule-based 系统和 feature engineering。

### Q5. Why is SentiWordNet different from a simple word list?

- SentiWordNet is different because it labels WordNet synsets with positive, negative, and objective scores, so it distinguishes sentiment at the sense level rather than only at the surface-word level.
- SentiWordNet 的不同点在于它给 WordNet synset 标注 positive、negative 和 objective 分数，因此它区分的是 sense 级而不只是 surface-word 级的情感。

### Q6. Why is inter-annotator agreement important?

- Inter-annotator agreement is important because it measures how consistently humans can assign labels, which directly affects dataset reliability.
- inter-annotator agreement 很重要，因为它衡量人类标注者打标签的一致性，并直接影响数据集的可靠性。

### Q7. What are the main limitations of rule-based sentiment analysis?

- The main limitations are dependence on lexicon completeness and correctness, difficulty handling unseen expressions, and typically high precision but low recall.
- rule-based sentiment analysis 的主要局限包括过度依赖 lexicon 的完整性和正确性、难以处理未见表达，并且通常 high precision but low recall。

### Q8. What is feature engineering in statistical sentiment analysis?

- Feature engineering is the manual design of structured input features such as unigrams, bigrams, TF-IDF values, embeddings, or emoji counts for a classifier.
- statistical sentiment analysis 中的 feature engineering 指的是为分类器人工设计结构化输入特征，例如 unigrams、bigrams、TF-IDF、embeddings 或 emoji 计数。

### Q9. How can word embeddings be used in SA without full end-to-end neural training?

- Word embeddings can be averaged or otherwise transformed into feature vectors and then concatenated with other handcrafted features before feeding them into a classifier such as SVM.
- 即使不做完整的 end-to-end 神经训练，也可以把 word embeddings 平均或变换成特征向量，再与其他人工特征拼接后输入 SVM 等分类器。

### Q10. What are linear chain-based neural sentiment models?

- Linear chain-based neural sentiment models encode the text as a sequence, usually with RNN, LSTM, or related architectures, and then classify from the resulting sentence representation.
- linear chain-based neural sentiment models 会把文本编码成一个序列表示，通常使用 RNN、LSTM 或相关结构，然后基于句子表示进行分类。

### Q11. How does BERT perform sentiment classification?

- BERT performs sentiment classification by taking the `[CLS]` representation and passing it to a task-specific classification head, typically with fine-tuning.
- BERT 通过取 `[CLS]` 表示并将其送入特定任务的分类头来完成 sentiment classification，通常需要 fine-tuning。

### Q12. Why might one prompt be insufficient for some sentiment tasks?

- One prompt may be insufficient because tasks such as implicit sentiment detection require intermediate reasoning and cannot always be solved with a shallow direct instruction.
- 单个 prompt 可能不够，是因为 implicit sentiment detection 这类任务需要中间推理，不能总靠一个浅层的直接指令解决。

### Q13. What is AutoPrompt?

- AutoPrompt is a search-based method that automatically finds trigger tokens or prompt words that elicit the desired output from a language model.
- AutoPrompt 是一种基于搜索的方法，它会自动寻找能够触发目标输出的 trigger tokens 或 prompt words。

### Q14. What is prompt tuning?

- Prompt tuning is a parameter-efficient method that freezes a pretrained language model and learns only a small set of soft prompt vectors for a task.
- prompt tuning 是一种 parameter-efficient 方法，它会冻结预训练语言模型，只学习少量面向任务的 soft prompt 向量。

### Q15. Why is Week 5 a bridge module in the course?

- Week 5 is a bridge module because it applies earlier modeling ideas to a practical downstream classification task and prepares students for later token-level and seq2seq tasks.
- Week 5 是课程中的桥梁模块，因为它把前面学过的建模思想应用到一个具体的下游分类任务上，并为后续 token-level 和 seq2seq 任务做铺垫。

---

## 16. One-Sentence Summary / 一句话总括 Week 5

- Week 5 shows that sentiment analysis is a broad family of affective classification problems and surveys how lexicons, features, neural encoders, BERT fine-tuning, and prompt-based methods can all be used to solve them.
- Week 5 展示了 sentiment analysis 是一大类 affective classification 问题，并系统梳理了 lexicon、特征工程、神经编码器、BERT 微调以及 prompt-based 方法如何共同用于解决这些任务。
