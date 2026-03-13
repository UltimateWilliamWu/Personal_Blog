# COMP6713 Week 2 Representation Learning 中英对照笔记

说明：这份笔记以 `Week2-RepresentationLearning.pdf` 45 页课件为主线，并对照 `Week_2.zip` 里的 4 个 notebook 补全 demo 细节。每个知识点按照“英文一句，中文一句”的顺序排列，方便理解、背诵和考试作答。

---

## 1. Announcements and Weekly Roadmap / 课程提醒与本周路线图

- The first assessable quiz opens on Wednesday at 12pm and stays open until next Monday at 12pm, with only one attempt allowed.
- 第一次正式计分 quiz 从周三中午 12 点开放到下周一中午 12 点，而且只有一次作答机会。

- Tutorials start this week, and the lecturer explicitly says they help with the assignment, the final exam, and the course learning outcomes.
- tutorial 从这周开始，老师明确说 tutorial 会帮助你准备作业、期末考试以及课程学习目标。

- Consultation is on Tuesdays from 1:30pm to 2:30pm, either online or in person in K17-217B.
- consultation 时间是每周二 1:30pm 到 2:30pm，可以线上或去 K17-217B 线下咨询。

- The module roadmap is divided into representing words and representing sentences.
- 本周模块主线分成两大部分：表示词语和表示句子。

- For words, the lecture covers one-hot vectors, their inadequacy, word2vec, GloVe, and sentence representations built from word vectors.
- 在词语表示部分，课件讲 one-hot vectors、它们的不足、word2vec、GloVe，以及如何用词向量表示句子。

- For sentences, the lecture moves from computational grammar to probabilistic language modeling, and then to linear sequential neural models such as RNNs and LSTMs.
- 在句子表示部分，课件从 computational grammar 过渡到 probabilistic language modeling，再到 RNN 和 LSTM 这类顺序神经模型。

- The explicit topic list for the week is one-hot vectors, probabilistic language modeling, computational grammar, word2vec, GloVe, and LSTM-based language modeling.
- 课件明确列出的本周主题是 one-hot vectors、probabilistic language modeling、computational grammar、word2vec、GloVe，以及基于 LSTM 的语言建模。

---

## 2. Representation Matters / 为什么表示很重要

- The lecture starts by unpacking the NLP black box and asks what representation makes text useful for computation.
- 课件一开始就说要把 NLP 黑盒拆开，核心问题是：怎样的表示才能让文本可以被计算处理。

- A representation is an abstraction that captures the essence of an idea or entity for a specific goal.
- 表示本质上是一种抽象，它为了特定目标抓住一个概念或实体的核心信息。

- There can be multiple incomplete representations of the same entity, and they may still be sufficient for a specific task.
- 同一个实体可以有多种不完整的表示，而这些不完整表示在某个具体任务里依然可能足够用。

- The lecture uses examples such as a real-world dog, the word “dog”, the sentence “The dog is on the table”, and even emoticons or emojis to show that representations exist at multiple levels.
- 课件用真实世界中的狗、单词 “dog”、句子 “The dog is on the table”，甚至表情符号来说明：表示可以存在于多个层级。

- Meaning can move from the meaning of a word to the meaning of a sentence through composition.
- 语义可以从词的意义通过组合上升到句子的意义。

- In NLP, representations are ways of converting text into a form that is understandable by and useful for a machine learning algorithm.
- 在 NLP 中，表示就是把文本转成机器学习算法能够理解并有效利用的形式。

- The lecture explicitly contrasts word, sentence, and discourse as different units of representation.
- 课件明确区分了 word、sentence 和 discourse 这三个不同层次的表示单位。

---

## 3. One-Hot Vectors and Classical Vectorization / One-Hot 向量与经典向量化

- A very early and very important idea is to represent each word as a vector with one active position and all other positions set to zero.
- 一个非常早期但很重要的想法是，把每个词表示成一个只有一个位置为 1、其他位置全为 0 的向量。

- In this view, each word becomes a random variable or a feature dimension for a machine learning algorithm.
- 在这种表示里，每个词都变成一个随机变量，或者说机器学习算法里的一个特征维度。

- The number of columns in a one-hot representation is the size of the vocabulary, written as `|V|`.
- one-hot 表示的列数就是词表大小，通常记作 `|V|`。

- The lecture also calls one-hot vectors unigram vectors.
- 课件也把 one-hot vectors 叫作 unigram vectors。

- One-hot representations became the ruling paradigm in statistical NLP before modern embedding methods became dominant.
- 在现代词向量方法流行之前，one-hot 表示是 statistical NLP 中的主流范式。

- The “hot” in one-hot comes from electronics engineering, where a terminal carrying current is described as hot.
- one-hot 里的 “hot” 来源于电子工程，表示某个端口有电流通过、处于激活状态。

- The slide explicitly asks why we do not simply use shorter binary encodings instead of one-hot vectors.
- 课件还专门提问：为什么不直接用更短的二进制编码，而要用 one-hot。

- The practical reason is that one-hot gives every word its own independent dimension, while arbitrary binary codes introduce meaningless structural similarity between unrelated words.
- 实际原因是，one-hot 给每个词独立维度，而任意二进制编码会给无关词引入没有语义意义的结构相似性。

- One-hot vectors can also represent sentences in a bag-of-words style, but word order information is lost.
- one-hot 也可以用 bag-of-words 的方式表示句子，但词序信息会丢失。

- The lecture asks what information is lost and when it is acceptable to lose it.
- 课件还追问：这种表示丢掉了什么信息，以及在什么场景下丢掉这些信息是可以接受的。

- In practice, the lecture points to `scikit-learn` as a standard library for vectorization.
- 在实践上，课件把 `scikit-learn` 作为经典向量化方法的标准工具库来介绍。

- `CountVectorizer` is presented as similar to one-hot or bag-of-words style vectorization.
- `CountVectorizer` 在课件里被当作与 one-hot 或 bag-of-words 风格相近的向量化方法。

- `TF-IDF Vectorizer` is introduced as a weighted alternative where TF means term frequency and IDF means inverse document frequency.
- `TF-IDF Vectorizer` 被介绍为一种带权重的替代方案，其中 TF 是词频，IDF 是逆文档频率。

- These vectorizers convert text into numeric format and can then be used by classical machine learning models such as logistic regression and Naive Bayes.
- 这些向量化工具会把文本转成数值形式，然后交给 logistic regression、Naive Bayes 等经典机器学习模型使用。

- The lecture explicitly says this will be used later for sentiment analysis in Week 6.
- 课件还明确说，这套向量化思路会在 Week 6 的情感分析里再次用到。

### 3.1 Limitations of One-Hot Vectors / One-Hot 的局限

- One-hot vectors treat all words as equally dissimilar because any two different one-hot vectors differ in the same crude way.
- one-hot 向量会把不同词之间都处理成“差不多一样不相似”，因为任意两个不同 one-hot 向量之间的差异方式都非常粗糙。

- The lecture asks whether words are really equally dissimilar, using examples such as dog, cat, chair, and table.
- 课件用 dog、cat、chair、table 的例子反问：词之间真的都一样不相似吗。

- Synonyms such as “trousers” and “pants” become completely different variables in a one-hot system.
- 像 “trousers” 和 “pants” 这样的近义词，在 one-hot 系统里会变成完全不同的变量。

- This creates a problem for the learning algorithm because semantic similarity is invisible to the representation.
- 这会让学习算法很吃亏，因为语义相似性在这种表示里完全不可见。

- The lecture then asks us to add dimensions such as Animal, Furniture, Garment, Bottom-garment, Top-garment, and “Can it be placed on a table?”.
- 接着课件让我们尝试增加像 Animal、Furniture、Garment、Bottom-garment、Top-garment、以及 “Can it be placed on a table?” 这样的维度。

- This illustrates that better representations should capture properties instead of just identity.
- 这说明更好的表示应该编码“属性”，而不仅仅是“身份编号”。

- However, hand-crafted dimensions are neither complete nor accurate.
- 但是手工设计的这些维度既不完整，也不够准确。

- This motivates continuous representations, where the dimensions are learned rather than manually designed.
- 这就引出了连续表示，也就是维度不是手工写死，而是从数据中学习出来。

---

## 4. Continuous Word Representations / 连续词表示与词向量

- Continuous representations are dense real-valued vectors instead of sparse binary indicator vectors.
- 连续表示是稠密的实数向量，而不是稀疏的二进制指示向量。

- The lecture refers to them as word vectors, word embeddings, word representations, or semantic vector space models.
- 课件把这类表示称为 word vectors、word embeddings、word representations，或者 semantic vector space models。

- A word embedding is a continuous vector that represents the semantics of a word in a k-dimensional space.
- 词向量就是把词的语义编码到一个 k 维连续空间中的向量。

- The key idea is not to map words into a pre-defined hash map, but to learn representations of their meanings.
- 核心思想不是把词塞进一个预先定义好的哈希表，而是学习词义的表示。

- Once words are represented as dense vectors, similarity between words can be computed numerically.
- 一旦词被表示成稠密向量，词与词之间的相似性就可以数值化计算。

- The lecture gives examples such as similarity(dog, cat) being high and similarity(dog, chair) being low.
- 课件举例说 similarity(dog, cat) 会比较高，而 similarity(dog, chair) 会比较低。

- This means a representation can now reflect semantic closeness instead of mere token identity.
- 这意味着表示开始能反映语义接近性，而不只是词的编号差异。

- The linguistic idea behind this is distributional similarity.
- 这背后的语言学思想就是 distributional similarity，也就是分布式相似性。

- The lecture states the famous principle “A word is known by the company it keeps.”
- 课件直接给出了著名观点：“A word is known by the company it keeps.”

- Similar words tend to occur in similar contexts, and the distribution of surrounding words helps define meaning.
- 相似的词往往出现在相似的上下文中，周围词的分布可以帮助定义一个词的意义。

- The examples with bank, money, fish, dog, cat, and chair are used to show that contextual neighborhoods are what make embeddings semantic.
- 课件用 bank、money、fish、dog、cat、chair 等例子说明，正是上下文邻域让词向量具有语义性。

---
## 5. Word2Vec / Word2Vec

- The lecture groups word2vec and GloVe together as two major algorithms for learning word representations.
- 课件把 word2vec 和 GloVe 归为学习词表示的两大经典算法。

- Word2Vec is connected to paradigmatic similarity, meaning that similar words are substitutable in context.
- Word2Vec 对应 paradigmatic similarity，也就是相似词往往可以在上下文中互相替换。

- GloVe is connected to syntagmatic similarity, meaning that related words often co-occur together.
- GloVe 对应 syntagmatic similarity，也就是相关词往往会共同出现。

- The slide gives the contrast “green” and “red” for substitutable similarity, and “dog” and “bone” for co-occurrence-based relatedness.
- 课件用 “green” 和 “red” 说明可替换相似性，用 “dog” 和 “bone” 说明共现相关性。

### 5.1 The Core Learning Setup / 核心学习设置

- Word2Vec learns to convert words into vectors through a self-supervised task.
- Word2Vec 通过自监督任务把词学习成向量。

- The lecture explicitly says its labels come from a self-supervised “fill in the gaps” task over spans of words.
- 课件明确说，word2vec 的标签来自对词序列做 “fill in the gaps” 的自监督任务。

- Unlabeled text is modified into a context-prediction task, and learned word representations emerge from that process.
- 无标注文本会被改造成上下文预测任务，而词表示就是在这个过程中学出来的。

- The lecture points out that word2vec does not capture multiple meanings of a word well.
- 课件也明确指出，word2vec 不能很好地处理一词多义。

- This is an important limitation because a word such as “bank” may have different senses but still receive a single embedding.
- 这是一个重要局限，因为像 “bank” 这样的词有多个词义，但通常只会得到一个向量。

### 5.2 Skip-gram and CBOW / Skip-gram 与 CBOW

- The two classic word2vec formulations are skip-gram and continuous bag of words, or CBOW.
- word2vec 的两种经典形式是 skip-gram 和 continuous bag of words，也就是 CBOW。

- Skip-gram takes a center word as input and predicts surrounding context words.
- Skip-gram 用中心词作为输入，去预测周围的上下文词。

- CBOW does the reverse: it takes surrounding context words as input and predicts the center word.
- CBOW 正好相反：它用周围上下文词作为输入，去预测中心词。

- The lecture explicitly asks students to adapt the skip-gram architecture to CBOW as an exercise.
- 课件还把“把 skip-gram 结构改写成 CBOW”作为一个课堂练习。

- The slide sequence also reminds students that this is conceptually connected to the n-gram idea from probabilistic language modeling.
- 课件还提醒，这个思路和 probabilistic language modeling 里的 n-gram 直觉是连着的。

### 5.3 Architectural View of Skip-gram / Skip-gram 的结构视图

- In skip-gram, the input word is first represented as a one-hot vector of size `|V|`.
- 在 skip-gram 中，输入词先表示成大小为 `|V|` 的 one-hot 向量。

- This one-hot vector is multiplied by a center-word embedding matrix of shape `|V| x |D|`.
- 这个 one-hot 向量会和一个形状为 `|V| x |D|` 的中心词嵌入矩阵相乘。

- The result is a dense vector of size `|D|`, which is the learned representation of the center word.
- 乘完之后得到一个大小为 `|D|` 的稠密向量，这就是中心词的表示。

- That vector is then multiplied by a context-word matrix of shape `|D| x |V|` to produce scores over vocabulary items.
- 接着这个向量再和一个 `|D| x |V|` 的上下文词矩阵相乘，生成整个词表上的分数。

- A softmax followed by argmax can then turn those scores into predicted context words.
- 然后通过 softmax 和 argmax，就可以把这些分数变成对上下文词的预测。

- The lecture stresses that at the end of learning, the word embedding matrix becomes a useful embedding matrix for downstream use.
- 课件强调，训练完成后，这个词嵌入矩阵本身就成为后续任务可用的 embedding matrix。

### 5.4 Softmax in Word2Vec / Word2Vec 中的 Softmax

- Softmax maps vector scores to a normalized probability-like score over all vocabulary choices.
- Softmax 会把一组向量分数映射成对整个词表的归一化概率式分布。

- The lecture says softmax is useful because it is differentiable and common in neural NLP.
- 课件说 softmax 很重要，因为它可微，而且在 neural NLP 中非常常见。

- It also represents a choice among alternatives, so it can be interpreted as a form of ambiguity resolution.
- 它还对应在多个候选之间做选择，因此也可以被理解成一种 ambiguity resolution。

- The “tale of two vectors” slide points out that word2vec actually learns two vectors per word: a center vector and a context vector.
- “A Tale of Two Vectors” 那一页强调，word2vec 实际上会为每个词学习两个向量：center vector 和 context vector。

- The lecture also notes that next week attention will introduce a setting with three vectors, foreshadowing Transformer-style mechanisms.
- 课件还顺便预告，下周 attention 会出现“三个向量”的设定，为 Transformer 机制做铺垫。

### 5.5 Why Softmax Becomes Expensive / 为什么 Softmax 会变贵

- The slide “What the V?” emphasizes that the vocabulary size `V` can be very large.
- “What the V?” 那页强调，词表大小 `V` 可能会非常大。

- If we compute a full softmax over all vocabulary items for every training step, computation becomes expensive.
- 如果每一步训练都对整个词表做完整 softmax，计算量就会很大。

- The lecture therefore introduces two optimizations: hierarchical softmax and negative sampling.
- 所以课件接着引入两种优化：hierarchical softmax 和 negative sampling。

### 5.6 Hierarchical Softmax / 分层 Softmax

- Hierarchical softmax computes a word probability through a path in a tree instead of across all vocabulary items directly.
- hierarchical softmax 不是直接对整个词表算概率，而是通过树中的一条路径来计算一个词的概率。

- The tree used in the lecture is a Huffman tree.
- 课件里使用的是 Huffman tree。

- The lecture lists three desirable properties of the Huffman tree: words are leaf nodes, frequent words are closer to the root, and every word has a unique root-to-leaf path.
- 课件列出了 Huffman tree 的三个理想性质：词是叶节点、高频词更靠近根节点、每个词都有唯一的 root-to-leaf 路径。

- These properties reduce computation because frequent words need fewer decisions to be reached.
- 这些性质可以减少计算，因为高频词只需要更短路径就能被到达。

- The probability of a target word can be decomposed into a product of binary choices along the path.
- 一个目标词的概率可以分解成路径上一系列二元选择概率的乘积。

- The lecture also points out that intermediate-node representations participate in these computations.
- 课件还指出，中间节点的表示也会参与这些概率计算。

- The slide challenges students to think about whether a binary tree would work, but the point is that Huffman coding is especially efficient for frequency-skewed vocabularies.
- 课件还让学生思考普通二叉树能不能用，而核心点是 Huffman 编码对频率分布偏斜的词表特别高效。

### 5.7 Negative Sampling / 负采样

- Negative sampling reframes the problem from full multinomial classification into binary classification.
- negative sampling 会把原来的多项分类问题改写成二分类问题。

- The new subtask is: given a context word and a target word, predict whether the combination is valid or invalid.
- 新的子任务是：给定一个 context word 和一个 target word，判断这个组合是有效还是无效。

- Because the corpus only contains seen combinations, we must create dummy invalid examples by sampling negative pairs.
- 因为语料里只有见过的组合，所以我们必须通过采样构造假的无效组合，也就是 negative pairs。

- The lecture uses examples such as Withdraw money being true, Eat money being false, and Catch fish being true.
- 课件用 Withdraw money 为真、Eat money 为假、Catch fish 为真等例子来说明这个过程。

- Each target word effectively becomes a logistic regression style binary classifier for the sampled training step.
- 在每个采样训练步骤里，每个目标词可以被理解为一个 logistic regression 风格的二分类判断。

- The slide explicitly asks how many negative samples should be used and whether they should be sampled randomly.
- 课件还明确提出两个问题：该采多少 negative samples，以及是否应该随机采样。

- The notation warning on the slide says that some sources use `c` for context word and `w` for center word.
- 课件还提醒符号记号可能变化，有的地方用 `c` 表示 context word，用 `w` 表示 center word。

- The optional homework note says that only a subset of vocabulary classifiers is trained per instance, and students are asked to think about why this makes computation cheaper.
- optional homework 那页还提示，每个训练样本只训练词表中的一个子集，目的是降低计算开销。

### 5.8 Word2Vec Recap, Extensions, and Limitations / Word2Vec 小结、扩展与局限

- The lecture summarizes word2vec as a method for learning dense word representations by predicting words from context or context from words.
- 课件把 word2vec 总结为：通过“根据上下文预测词”或“根据词预测上下文”来学习稠密词表示的方法。

- The two principal model types are skip-gram and CBOW.
- 它的两种核心模型就是 skip-gram 和 CBOW。

- The two main optimization tricks are hierarchical softmax and negative sampling.
- 两种主要优化技巧就是 hierarchical softmax 和 negative sampling。

- The lecture mentions extensions such as wang2vec, sense2vec, and task-specific word vectors for sentiment analysis.
- 课件提到了若干扩展，例如 wang2vec、sense2vec，以及面向情感分析的 task-specific word vectors。

- Wang2vec explicitly models word order in context.
- Wang2vec 会显式考虑上下文中的词序。

- Sense2vec learns sense-aware representations instead of a single embedding per surface form.
- Sense2vec 会学习带 sense 区分的表示，而不是给一个词形只配一个向量。

- Task-specific vectors learn representations optimized for a downstream objective such as sentiment analysis.
- task-specific vectors 则会针对下游目标，例如情感分析，来学习专门的词表示。

- The “contronym” slide uses words such as Dust, Screen, Rent, and Sanction to show that one word form can carry opposite meanings.
- “contronym” 那页用 Dust、Screen、Rent、Sanction 说明：同一个词形可能携带相反意义。

- The lecture explicitly points out that a standard word embedding will still assign only one embedding to such a word.
- 课件明确指出，标准词向量通常还是只会给这种词分配一个向量。

- This is another reminder that standard embeddings do not resolve all ambiguity.
- 这再次提醒我们，标准词向量并不能解决所有歧义问题。

### 5.9 Word2Vec Demo Notes from the Notebook / notebook 里的 Word2Vec demo 补充

- The accompanying gensim notebook trains Word2Vec on the Brown corpus and shows that similarity scores become more stable as training data grows.
- 配套的 gensim notebook 在 Brown corpus 上训练 Word2Vec，并展示随着训练数据增多，相似度会变得更稳定。

- The notebook also demonstrates pretrained embeddings, nearest neighbors, vector arithmetic such as `king - man + woman`, and bias-related behavior in learned vectors.
- notebook 还演示了 pretrained embeddings、最近邻、`king - man + woman` 这种向量运算，以及词向量中可能出现的偏见现象。

- This complements the lecture’s main message that embeddings are learned geometry, not predefined lookup tables.
- 这补充了课件的主旨：embedding 是学习出来的几何结构，而不是预先写死的查表系统。

---
## 6. GloVe / GloVe

- GloVe stands for Global Vectors for Word Representation.
- GloVe 的全称是 Global Vectors for Word Representation。

- The lecture describes GloVe as a weighted least squares model trained on global word-word co-occurrence counts.
- 课件把 GloVe 描述为一个训练在全局词-词共现计数上的 weighted least squares 模型。

- `X_ij` denotes the number of times word `j` occurs in the context of word `i`.
- `X_ij` 表示词 `j` 出现在词 `i` 上下文中的次数。

- `X_i` is the total count of all context words around word `i`, and `P_ij = P(j|i) = X_ij / X_i`.
- `X_i` 是词 `i` 的上下文总计数，而 `P_ij = P(j|i) = X_ij / X_i`。

- The word “global” refers to the fact that the co-occurrence matrix is built over the corpus as a whole rather than over one local prediction event at a time.
- 这里的 “global” 指的是共现矩阵是面向整个语料构建的，而不是像局部预测那样只关注某一个窗口事件。

- The goal is to learn word vectors whose dot products correlate with co-occurrence statistics.
- GloVe 的目标是学习一组词向量，使它们的点积和共现统计相关联。

- The derivation in the lecture starts from log conditional probability and then rewrites the relationship into a learnable linear form with bias terms.
- 课件中的推导从对数条件概率开始，再把它改写成一个带偏置项、可以学习的线性关系。

- The key optimization objective shown on the slide is a weighted squared-error loss over `(w_i · q_k + a + b - log X_ki)`.
- 课件给出的核心优化目标，就是对 `(w_i · q_k + a + b - log X_ki)` 做一个带权平方误差最小化。

- The weighting function `f(X_ki)` is introduced so that not all co-occurrence pairs are treated equally.
- 其中的权重函数 `f(X_ki)` 是为了让不同共现对不被一视同仁地处理。

### 6.1 Word2Vec vs GloVe / Word2Vec 与 GloVe 的对比

- Word2Vec is a prediction-based, window-based method.
- Word2Vec 是 prediction-based、window-based 的方法。

- GloVe is presented as a hybrid of count-based and window-based intuition, but operationally count-based in its learning objective.
- GloVe 被课件描述成兼有 count-based 和 window-based 直觉，但在学习目标上本质更偏 count-based。

- Word2Vec learns vectors so that context words can be predicted from a center word or vice versa.
- Word2Vec 学的是：如何用中心词预测上下文词，或者反过来。

- GloVe learns vectors so that co-occurrence statistics can be predicted for word pairs.
- GloVe 学的是：如何让词对之间的共现统计被向量关系刻画出来。

- In the slide comparison, Word2Vec treats distance to context as a step function defined by the window, whereas GloVe models it more like a long-tailed weighting over co-occurrences.
- 在课件对比里，Word2Vec 对上下文距离的处理更像窗口式的 step function，而 GloVe 更像是基于共现的长尾加权。

- The lecture also contrasts Word2Vec as more predictive in spirit and GloVe as more tied to dimensionality reduction over co-occurrence structure.
- 课件还把 Word2Vec 描述得更偏 predictive，而把 GloVe 描述得更偏在共现结构上做维度压缩。

- Word2Vec learns per context window, while GloVe learns from word-pair co-occurrence aggregates.
- Word2Vec 是围绕每个上下文窗口学习，而 GloVe 是围绕词对共现汇总统计来学习。

### 6.2 How Embeddings Are Used / 词向量怎么使用

- The lecture explicitly asks how word embeddings can be used after they are learned from large unlabeled corpora.
- 课件明确提出：当我们从大规模无标注语料学到词向量之后，这些向量该怎么使用。

- A simple approach is to feed word embeddings into another statistical or neural model as input features.
- 最直接的做法，是把词向量作为输入特征，喂给另一个 statistical 或 neural 模型。

- Another simple approach is to average word embeddings to form a sentence embedding.
- 另一个简单做法，是把多个词向量做平均，从而得到句向量。

- The lecture warns that Transformer gives a better way to represent sentences, but for now averaging is a useful baseline idea.
- 课件也提醒，Transformer 会提供更好的句子表示方式，但目前“平均词向量”是一个实用的 baseline。

---

## 7. Computational Grammar and Sentence Representation / 计算语法与句子表示

- Before probabilistic language modeling, the first generation of NLP often represented sentences through computational grammar.
- 在 probabilistic language modeling 之前，第一代 NLP 往往用 computational grammar 来表示句子。

- This idea derives historically from compilers and formal language systems in programming languages.
- 这个思路在历史上来源于编译器和编程语言里的形式语言系统。

- The focus of grammar-based modeling is belongingness.
- 基于语法的建模重点是 belongingness，也就是“这个句子是否属于该语言”。

- A language is treated as a set of valid strings, and grammar decides whether a string belongs to that set.
- 在这种视角里，语言被看成一个合法字符串集合，而语法的任务是判断一个字符串是否属于这个集合。

- The lecture defines non-terminals as capital letters, terminals as lower-case words, and epsilon as end of string.
- 课件定义：non-terminals 用大写字母表示，terminals 是小写词，epsilon 表示空串或字符串结束。

- Grammar is written as production rules.
- 语法通过一系列 production rules 来书写。

- The lecture gives an example grammar such as `S -> K A B`, `K -> a | the | ep`, `A -> happy | sad`, `B -> man | woman | person`.
- 课件举了一个例子语法，比如 `S -> K A B`，`K -> a | the | ep`，`A -> happy | sad`，`B -> man | woman | person`。

- This grammar defines which strings are valid, such as “the happy woman” or “sad person”.
- 这样的语法可以定义哪些字符串是合法的，例如 “the happy woman” 或 “sad person”。

### 7.1 Growing a Grammar / 构造和扩展语法

- The lecture constructs a grammar for a tiny language containing sentences such as “The boy eats rice” and “The girl drinks milk”.
- 课件先为一个非常小的人造语言构造语法，其中包括 “The boy eats rice” 和 “The girl drinks milk” 之类的句子。

- It then grows the grammar to include more patterns such as “The boy eats pizza”, “The girl eats”, and “The boy occasionally eats rice”.
- 然后又继续扩展语法，让它可以表示 “The boy eats pizza”、“The girl eats” 和 “The boy occasionally eats rice” 这类句子。

- This illustrates that rule-based grammars can be extended, but only by explicitly adding more structure.
- 这说明 rule-based grammar 当然可以扩展，但扩展方式往往是继续显式添加结构规则。

### 7.2 Limitations of Grammar / 语法方法的局限

- The lecture says that the list of sentences effectively needs to be known in advance, or at least the set of structures must be anticipated.
- 课件指出，句子列表实际上需要事先知道，或者至少要提前预判语言中会出现哪些结构。

- Accommodating new sentences can be cumbersome.
- 要容纳新的句子，往往会非常麻烦。

- Grammar is good at testing belongingness, but not as good at assigning graded likelihood or supporting realistic generation.
- grammar 很适合测试 belongingness，但不擅长给出渐进式 likelihood，也不太适合真实语言生成。

- This motivates the move from belongingness to likelihood.
- 这就引出了从 belongingness 转向 likelihood 的必要性。

---

## 8. Probabilistic Language Modeling / 概率语言模型

- Probabilistic language modeling asks not only whether a sentence is valid, but how likely it is.
- 概率语言模型不再只问一个句子是否合法，而是问这个句子有多可能。

- The lecture explicitly reframes the question as `Belongingness -> Likelihood`.
- 课件明确把问题重写成 `Belongingness -> Likelihood`。

- For a sentence `w1, w2, w3, ...`, the model assigns a probability to the full sequence.
- 对于一个句子 `w1, w2, w3, ...`，模型会给整个序列分配一个概率。

- The lecture writes sentence likelihood using a chain of conditional probabilities.
- 课件把句子概率写成一连串条件概率的乘积。

- For example, `P(The girl eats rice) = P(rice | The girl eats) * P(eats | The girl) * P(girl | The) * P(The | ep)`.
- 例如，`P(The girl eats rice) = P(rice | The girl eats) * P(eats | The girl) * P(girl | The) * P(The | ep)`。

- These probabilities can be estimated from a dataset using counts.
- 这些条件概率可以通过语料中的计数来估计。

- The lecture works through a concrete count-based example and obtains a sentence probability of `0.25` for “The girl eats rice” under a tiny dataset.
- 课件用一个具体的小语料计数例子，算出 “The girl eats rice” 的句子概率为 `0.25`。

### 8.1 N-gram Assumption / N-gram 假设

- Exact chain-rule modeling uses very long histories, which quickly becomes difficult to estimate from finite data.
- 如果严格按 chain rule 使用完整历史，上下文会越来越长，很快就难以用有限数据估计。

- To simplify the problem, the lecture introduces the n-gram assumption.
- 为了简化问题，课件引入了 n-gram assumption。

- A bigram assumption says that a word depends only on the word immediately before it.
- bigram assumption 认为一个词只依赖它前面的那个词。

- This is easier to compute on large datasets and still supports useful language generation.
- 这种假设在大数据上更容易计算，同时仍然能支持有用的语言生成。

- The lecture then connects probabilistic modeling to sentence completion by selecting the most likely candidate word for a gap.
- 课件进一步把概率模型和填空联系起来：选择条件概率最大的候选词来补空。

- Examples such as `three ____`, `ate three ____`, and `drank three ____` show how probability can encode plausibility.
- `three ____`、`ate three ____`、`drank three ____` 这几个例子说明，概率可以表达语言的合理性。

### 8.2 The Zero-Probability Problem / 零概率问题

- A major problem appears when the dataset has never seen a needed pattern.
- 当数据集从未见过某个需要的模式时，就会出现一个重大问题。

- If one conditional probability becomes zero, the full sentence probability collapses to zero.
- 如果其中某个条件概率变成 0，那么整个句子概率就会直接变成 0。

- The lecture shows this with a reduced dataset where `P(eats | girl)` becomes zero and therefore the whole sentence gets probability zero.
- 课件用删减后的数据集展示了这一点：当 `P(eats | girl)` 变成 0 时，整个句子的概率也会变成 0。

### 8.3 Smoothing / 平滑

- Smoothing is introduced as the standard statistical fix for zero probabilities.
- smoothing 被引入为解决零概率问题的标准统计方法。

- The lecture defines smoothing as modifying probabilities so that differences are reduced and impossible events become possible.
- 课件把 smoothing 定义为：修改概率分布，让差异变小，并让原本不可能的事件获得非零概率。

- The phrase used on the slide is “making impossible possible”.
- 课件在 slide 上直接把 smoothing 概括成 “making impossible possible”。

- Add-one smoothing, also called Laplace smoothing, adds one to counts before normalization.
- add-one smoothing，也叫 Laplace smoothing，会在归一化之前给计数加一。

- The lecture also lists interpolation-based smoothing as another smoothing family.
- 课件还列出了 interpolation-based smoothing，说明平滑并不只有加一这一种方法。

- In the “good joke” example, smoothing turns an unseen bigram from probability zero into a small non-zero value.
- 在 “good joke” 的例子里，平滑会把原来概率为 0 的未见 bigram 调整成一个小的非零值。

### 8.4 Language Generation and Perplexity / 语言生成与困惑度

- A probabilistic language model can be used for generation by taking a sequence so far as input and predicting the next word over the vocabulary.
- 概率语言模型可以用于生成：把“目前为止的词序列”作为输入，预测词表中的下一个词。

- The slide also asks why sampling can be used during generation.
- 课件还问到：为什么生成时可以用 sampling。

- The reason is that sampling introduces diversity instead of always choosing only the single most probable continuation.
- 原因是 sampling 可以带来多样性，而不是每次都只选概率最高的那个后续词。

- The lecture then asks what the problems of simple n-gram based generation are.
- 接着课件追问：简单 n-gram 生成会有什么问题。

- The main limitations are limited context length, potentially nonsensical output, and inability to reliably capture long-distance dependencies.
- 主要局限包括：上下文长度有限、生成结果可能不合语义，以及难以稳定捕捉长距离依赖。

- The agreement example `The students in a class ... learn or learns?` is used to show why longer context matters.
- `The students in a class ... learn 还是 learns?` 这个例子被用来说明为什么长距离上下文很重要。

- Perplexity is introduced as a metric for language models.
- 课件接着引入了 language model 的评价指标 perplexity。

- The lecture describes perplexity as the inverse probability of a test set and says lower perplexity is better.
- 课件把 perplexity 描述为测试集概率的逆，而且明确说 perplexity 越低越好。

- Intuitively, a lower perplexity means the model is less “perplexed” by valid test sentences.
- 直觉上，较低的 perplexity 表示模型对合法测试句子没有那么“困惑”。

- Perplexity is therefore an estimate of how well the model captures the sentences in the test set.
- 所以 perplexity 可以被看作：模型对测试集句子的拟合好坏的一种估计。

---
## 9. Sequential Neural Language Modeling / 顺序神经语言建模

- The lecture then moves from count-based probabilistic language models to sequential neural language modeling.
- 接着课件从基于计数的概率语言模型过渡到顺序神经语言模型。

- The “For sale: baby shoes, never worn.” example is used to emphasize that longer text meaning often depends on sequence and context beyond short n-grams.
- “For sale: baby shoes, never worn.” 这个例子被用来强调：较长文本的意义往往依赖超出短 n-gram 范围的顺序和上下文。

### 9.1 Auto-regressive Models and RNNs / 自回归模型与 RNN

- An auto-regressive language model predicts the next word from the sequence generated so far.
- 自回归语言模型会根据目前已经出现的序列来预测下一个词。

- The lecture summarizes the shift as `Prob -> Recurrent`, meaning that recurrent neural models can replace hand-counted short contexts with learned sequential state.
- 课件把这种变化概括成 `Prob -> Recurrent`，意思是 recurrent 模型会用学习出来的顺序状态来替代手工截断的短上下文计数。

- In an RNN, each time step receives an input `x_t`, updates a hidden state `h_t`, and produces an output `o_t`.
- 在 RNN 中，每个时间步接收输入 `x_t`，更新隐藏状态 `h_t`，并产生输出 `o_t`。

- The hidden state carries information from previous time steps, which is why the model is called recurrent.
- 隐状态会携带前面时间步的信息，这就是它被称为 recurrent 的原因。

- The lecture visually unrolls the RNN over time to show repeated computation across sequence positions.
- 课件通过把 RNN 在时间维度上展开，来说明它是在不同位置重复同一套计算。

### 9.2 LSTM as a Specialized RNN / LSTM 作为专门化 RNN

- The lecture introduces LSTM as Long Short-Term Memory, designed to improve distant memory compared with a simple RNN.
- 课件把 LSTM 介绍为 Long Short-Term Memory，它的目标是比普通 RNN 更好地保留长距离记忆。

- The intuition slides describe LSTM as maintaining memory, forgetting what is unnecessary, collecting what should be stored, retrieving information, and producing output.
- 课件用直觉化语言描述 LSTM：维护记忆、忘记不重要信息、收集需要存储的信息、提取需要的信息、最后产生输出。

- Another slide paraphrases the cell behavior as “Act now”, “Forget what is not important”, and “Remember what is important for the future”.
- 另一页把 LSTM cell 的行为概括成 “Act now”、“Forget what is not important” 和 “Remember what is important for the future”。

- The important conceptual point is that LSTM adds gating-style control to recurrent computation.
- 核心概念是：LSTM 给 recurrent computation 增加了门控式控制。

- This allows the model to keep some information, discard some information, and update memory more selectively than a plain RNN.
- 这让模型可以比普通 RNN 更有选择地保留信息、丢弃信息和更新记忆。

### 9.3 Training an LSTM Language Model / 训练 LSTM 语言模型

- The lecture shows an LSTM chain trained on a sequence such as `the boy eats rice`.
- 课件展示了一个 LSTM 链如何在 `the boy eats rice` 这样的序列上训练。

- At each step, the model takes either a one-hot or word2vec-style input representation.
- 在每个时间步，模型都接收一个 one-hot 或 word2vec 风格的输入表示。

- It then predicts the next word through a softmax over the vocabulary.
- 然后它通过对整个词表做 softmax，来预测下一个词。

- The loss is backpropagated through the chain so that earlier states are updated based on later prediction errors.
- 损失会沿着整条链反向传播，这样前面的状态也会根据后面预测的错误进行更新。

- In modern deep learning terms, this is backpropagation through time.
- 用现代深度学习术语来说，这就是 backpropagation through time。

### 9.4 Demo Notes from the LSTM Notebook / LSTM notebook 补充

- The accompanying PyTorch notebook builds a neural language model with an embedding layer, an LSTM layer, and a linear output layer.
- 配套的 PyTorch notebook 构建了一个神经语言模型，结构是 embedding layer、LSTM layer 和 linear output layer。

- The training data comes from the Gutenberg corpus, specifically `Moby Dick`.
- 训练数据来自 Gutenberg corpus，具体用的是 `Moby Dick`。

- The notebook tokenizes text, builds a vocabulary, maps words to indices, creates fixed-length training sequences, and then trains the model with cross-entropy loss and Adam.
- notebook 会先做分词、建立词表、把词映射成索引、构造固定长度训练序列，然后用 cross-entropy loss 和 Adam 训练模型。

- The notebook also uses teacher forcing during training.
- 这个 notebook 在训练时还使用了 teacher forcing。

- The generation demo seeds the model with an initial phrase and repeatedly predicts the next word, feeding predictions back into the model.
- 生成 demo 会先给模型一个 seed phrase，然后反复预测下一个词，并把预测结果继续喂回模型。

### 9.5 Limitations of LSTMs / LSTM 的局限

- The lecture still calls LSTM-based information passing linear in the sense that information moves along the chain one step at a time.
- 课件依然认为 LSTM 的信息传递是线性的，因为信息还是沿着时间链一步一步传过去。

- Long-distance dependencies remain difficult for such sequential mechanisms.
- 对这种顺序机制来说，长距离依赖依然很难完全处理好。

- This motivates the question: can we pass information directly between non-consecutive hidden states?
- 这就引出了一个关键问题：我们能不能让非相邻隐藏状态之间直接传递信息。

- That question is the explicit bridge to the next week’s topic: attention.
- 这个问题就是通向下周 attention 主题的明确桥梁。

---

## 10. The Elephant Metaphor and Week 2 Summary / 盲人摸象隐喻与 Week 2 总结

- The lecture begins and ends with the six blind men and the elephant.
- 课件开头和结尾都用了 “六个盲人摸象” 的故事。

- The metaphor suggests that each representation or modeling approach captures only one aspect of language.
- 这个隐喻强调：每一种表示或建模方法都只抓住了语言的一部分。

- One-hot vectors capture discrete identity but miss semantics.
- one-hot vectors 能抓住离散身份，但抓不住语义。

- Word embeddings capture distributional semantics but struggle with polysemy and context sensitivity.
- 词向量能抓住分布式语义，但对一词多义和上下文敏感性处理有限。

- Computational grammar captures structural belongingness but is brittle and hard to scale.
- computational grammar 能表达结构上的 belongingness，但很脆弱，也不易扩展。

- Probabilistic language models capture likelihood and enable generation, but short contexts and sparse data are limiting.
- 概率语言模型能表达 likelihood 并支持生成，但短上下文和数据稀疏是它的硬伤。

- RNNs and LSTMs improve sequential modeling but still struggle with long-distance dependencies.
- RNN 和 LSTM 改善了顺序建模能力，但对长距离依赖依然不够理想。

- The summary slide therefore presents the week as a progression from one-hot vectors to embeddings, from grammar to probabilistic language modeling, and from probabilistic models to neural sequential models.
- 所以 summary 页把这周概括成一个连续演化：从 one-hot 到 embeddings，从 grammar 到 probabilistic language modeling，再从概率模型走向神经顺序模型。

### 10.1 Suggested Reading / 推荐阅读

- The lecture ends with reading links for probabilistic language modeling, RNN/LSTM, the Illustrated Word2Vec article, the original word2vec paper, the original GloVe paper, gensim tutorials, the GloVe project page, and spaCy vectors documentation.
- 课件最后给出了 probabilistic language modeling、RNN/LSTM、Illustrated Word2Vec、word2vec 原始论文、GloVe 原始论文、gensim 教程、GloVe 项目页，以及 spaCy 向量文档等阅读链接。

- The last slide again asks whether information can pass between non-consecutive hidden states, which directly foreshadows attention in Week 3.
- 最后一页再次追问：信息能否在非连续隐藏状态之间直接传递，这直接为 Week 3 的 attention 埋下伏笔。

### 10.2 Demo Alignment with Week_2.zip / 与 Week_2.zip demo 的对齐说明

- The `1-one-hot-vectors.ipynb` notebook demonstrates Bag-of-Words, stopword-aware vectorization, and TF-IDF, reinforcing that classical representations are sparse, interpretable, and useful for traditional models.
- `1-one-hot-vectors.ipynb` 这个 notebook 演示了 Bag-of-Words、带停用词处理的向量化以及 TF-IDF，进一步说明经典表示是稀疏、可解释、并适合传统模型的。

- The `2-gensim-word2vec.ipynb` notebook demonstrates training Word2Vec with different corpus sizes, loading pretrained embeddings, nearest neighbors, analogies, and bias effects.
- `2-gensim-word2vec.ipynb` 演示了用不同规模语料训练 Word2Vec、加载 pretrained embeddings、查看最近邻、做类比运算以及观察偏见效应。

- The `3-prob-lang-modeling.ipynb` notebook builds a trigram language model on the Brown corpus and uses it for sentence completion.
- `3-prob-lang-modeling.ipynb` 在 Brown corpus 上构建了一个 trigram language model，并用它做句子补全。

- The `4-nn-llm.ipynb` notebook builds a PyTorch LSTM language model with embeddings, next-word prediction, cross-entropy loss, Adam, teacher forcing, and text generation from a seed phrase.
- `4-nn-llm.ipynb` 用 PyTorch 搭建了一个 LSTM 语言模型，其中包括 embeddings、next-word prediction、cross-entropy loss、Adam、teacher forcing，以及基于 seed phrase 的文本生成。

---

## 11. High-Frequency Exam Points / 高频考点总结

- Representation means an abstraction that captures the essence of an entity for a task.
- Representation 指的是为某个任务抓住实体核心信息的一种抽象。

- One-hot vectors are sparse identity-based representations with vocabulary-sized dimensions.
- One-hot vectors 是基于身份编号的稀疏表示，维度等于词表大小。

- The main weaknesses of one-hot vectors are sparsity, no semantic similarity, and no handling of synonymy or graded relatedness.
- One-hot vectors 的主要缺点是稀疏、无法表达语义相似性，也无法处理近义词和程度化相关性。

- CountVectorizer and TF-IDF are classical vectorization techniques used before or alongside neural methods.
- CountVectorizer 和 TF-IDF 是经典向量化技术，常用于神经方法之前或与之并用。

- Word embeddings are dense real-valued vectors learned from context.
- 词向量是从上下文中学出来的稠密实值向量。

- Distributional similarity means words are similar if they appear in similar contexts.
- Distributional similarity 指的是：如果两个词出现在相似上下文中，它们就倾向于相似。

- Word2Vec is a self-supervised embedding method based on predicting context from words or words from context.
- Word2Vec 是一种自监督词向量方法，本质是用词预测上下文，或用上下文预测词。

- Skip-gram predicts context words from a center word, while CBOW predicts the center word from context words.
- Skip-gram 用中心词预测上下文词，而 CBOW 用上下文词预测中心词。

- Word2Vec learns center vectors and context vectors, and uses softmax for vocabulary-level prediction.
- Word2Vec 会学习 center vectors 和 context vectors，并用 softmax 在整个词表上做预测。

- Hierarchical softmax reduces the cost of full softmax by traversing a Huffman tree.
- Hierarchical softmax 通过遍历 Huffman tree 来降低 full softmax 的计算成本。

- Negative sampling converts vocabulary prediction into binary classification on positive and sampled negative pairs.
- Negative sampling 会把词表预测改写成对正样本和采样负样本的二分类任务。

- Word2Vec usually gives one embedding per word form, so it struggles with polysemy and contronyms.
- Word2Vec 通常只给每个词形一个向量，因此难以处理一词多义和 contronyms。

- GloVe learns embeddings from global co-occurrence counts using a weighted least squares objective.
- GloVe 用全局共现计数和 weighted least squares 目标来学习词向量。

- Word2Vec is prediction-based, while GloVe is more count-based and co-occurrence-driven.
- Word2Vec 更偏 prediction-based，而 GloVe 更偏 count-based 和 co-occurrence-driven。

- Grammar-based language representation focuses on belongingness, not likelihood.
- grammar-based 句子表示关注的是 belongingness，而不是 likelihood。

- Probabilistic language modeling replaces belongingness with sentence likelihood.
- 概率语言建模用句子 likelihood 替代了单纯的 belongingness。

- N-gram models simplify sentence probability by assuming limited dependence on recent words.
- N-gram 模型通过假设只依赖最近几个词来简化句子概率建模。

- Unseen n-grams cause zero probabilities, which is why smoothing is necessary.
- 未见过的 n-gram 会导致零概率，这正是 smoothing 必要的原因。

- Add-one smoothing gives every possible n-gram a small non-zero count.
- Add-one smoothing 会给每个可能的 n-gram 一个小的非零计数。

- Perplexity is a standard language-model metric, and lower perplexity is better.
- Perplexity 是标准的语言模型指标，而且 perplexity 越低越好。

- RNNs model sequences by passing hidden states through time.
- RNN 通过在时间上传递隐藏状态来建模序列。

- LSTMs improve RNNs by using memory and gating mechanisms.
- LSTM 通过记忆和门控机制来改进 RNN。

- LSTMs still pass information linearly through time, so long-distance dependencies remain difficult and motivate attention.
- LSTM 仍然是沿时间线性传递信息，所以长距离依赖依然困难，这也正是 attention 的动机。

---
## 12. Model Answers to Likely Exam Questions / 常见考题标准答案

### Q1. What is a representation in NLP?

- A representation in NLP is an abstraction that converts language into a form that a machine learning algorithm can use.
- NLP 中的 representation 是一种抽象，它把语言转成机器学习算法可用的形式。

- A good representation captures enough of the essence of an entity or text to support a specific task.
- 一个好的 representation 会为具体任务保留足够多的核心信息。

### Q2. What is a one-hot vector, and what are its limitations?

- A one-hot vector is a sparse vector with one active dimension corresponding to a word and zeros elsewhere.
- one-hot vector 是一种稀疏向量，其中只有对应某个词的一个维度为 1，其余维度为 0。

- Its limitations are that it is sparse, ignores semantic similarity, treats all different words as equally unrelated, and cannot naturally capture synonymy or graded relatedness.
- 它的局限在于：非常稀疏、忽略语义相似性、把所有不同词都看成差不多一样不相关、也无法自然表达近义词和程度化相关性。

### Q3. Why do we move from one-hot vectors to dense word embeddings?

- We move to dense word embeddings because they can encode semantic similarity and allow similar words to have similar vector representations.
- 我们从 one-hot 走向稠密词向量，是因为词向量能够编码语义相似性，让相似词拥有相似表示。

- This gives machine learning models much richer information than identity-only sparse vectors.
- 相比只编码身份编号的稀疏向量，这会给机器学习模型更丰富的信息。

### Q4. What is distributional similarity?

- Distributional similarity is the idea that words are similar if they occur in similar contexts.
- Distributional similarity 的意思是：如果两个词出现在相似上下文中，它们就是相似的。

- This is the linguistic intuition behind many word embedding methods.
- 这正是很多词向量方法背后的语言学直觉。

### Q5. What is Word2Vec?

- Word2Vec is a self-supervised method that learns dense word representations by predicting context from words or words from context.
- Word2Vec 是一种自监督方法，它通过“根据词预测上下文”或“根据上下文预测词”来学习稠密词表示。

- It is one of the foundational methods for representation learning in NLP.
- 它是 NLP 表示学习中最基础的经典方法之一。

### Q6. What is the difference between skip-gram and CBOW?

- Skip-gram takes a center word as input and predicts surrounding context words.
- Skip-gram 以中心词为输入，去预测周围上下文词。

- CBOW takes surrounding context words as input and predicts the center word.
- CBOW 以上下文词为输入，去预测中心词。

### Q7. Why is softmax used in Word2Vec?

- Softmax is used to map vocabulary scores into a normalized distribution over possible words.
- 在 Word2Vec 里，softmax 用来把词表上的分数映射成归一化分布。

- It is differentiable and supports learning through gradient-based optimization.
- 它是可微的，因此可以支持基于梯度的优化学习。

### Q8. Why do we need hierarchical softmax or negative sampling?

- We need them because computing a full softmax over a very large vocabulary is expensive.
- 我们需要 hierarchical softmax 或 negative sampling，是因为对超大词表计算完整 softmax 非常昂贵。

- Hierarchical softmax reduces this cost through a Huffman tree, while negative sampling turns the problem into binary classification on sampled examples.
- hierarchical softmax 通过 Huffman tree 降低成本，而 negative sampling 则把问题改写成对采样样本的二分类。

### Q9. What is negative sampling?

- Negative sampling trains the model to distinguish valid word-context pairs from randomly sampled invalid pairs.
- negative sampling 会训练模型去区分“真实的词-上下文组合”和“随机采样的无效组合”。

- This avoids updating the full vocabulary distribution for every training example.
- 这样就避免了每个训练样本都更新完整词表分布。

### Q10. What is GloVe?

- GloVe is a word embedding method that learns vectors from global word-word co-occurrence statistics.
- GloVe 是一种利用全局词-词共现统计来学习词向量的方法。

- It uses a weighted least squares objective so that vector dot products reflect co-occurrence structure.
- 它用 weighted least squares 目标，让向量点积反映共现结构。

### Q11. What is the difference between Word2Vec and GloVe?

- Word2Vec is prediction-based and learns from local context windows, whereas GloVe is more count-based and learns from global co-occurrence statistics.
- Word2Vec 更偏 prediction-based，并从局部上下文窗口学习；而 GloVe 更偏 count-based，并从全局共现统计学习。

- Word2Vec focuses on predictive context learning, while GloVe focuses on matching co-occurrence structure in vector space.
- Word2Vec 侧重预测式上下文学习，而 GloVe 侧重让向量空间匹配共现结构。

### Q12. What is the limitation of standard word embeddings with respect to ambiguity?

- Standard word embeddings usually assign one vector to one word form, so they do not properly separate multiple senses of a word.
- 标准词向量通常为一个词形分配一个向量，因此不能很好地区分一个词的多个词义。

- This is why polysemy and contronyms remain difficult for basic embedding methods.
- 这就是为什么一词多义和 contronyms 对基础 embedding 方法来说仍然困难。

### Q13. What is computational grammar, and what is its limitation?

- Computational grammar is a rule-based way of defining which strings belong to a language.
- computational grammar 是一种基于规则的方法，用来定义哪些字符串属于某种语言。

- Its main limitation is that it focuses on belongingness rather than graded likelihood, and it is cumbersome to expand to new patterns.
- 它的主要局限是只关注 belongingness，而不是渐进式 likelihood，而且扩展到新模式会很繁琐。

### Q14. What is probabilistic language modeling?

- Probabilistic language modeling assigns probabilities to word sequences and asks how likely a sentence is.
- probabilistic language modeling 会给词序列分配概率，并回答“一个句子有多可能”。

- It replaces a yes-or-no view of sentence validity with a graded likelihood view.
- 它用“渐进式可能性”替代了原先“非黑即白的合法性判断”。

### Q15. What is the n-gram assumption?

- The n-gram assumption says that the probability of a word depends only on a limited number of previous words.
- n-gram assumption 认为，一个词的概率只依赖于前面有限个词。

- This makes language modeling computationally feasible, but it also limits context.
- 这让语言建模变得可计算，但也限制了上下文长度。

### Q16. Why do we need smoothing?

- We need smoothing because unseen n-grams can otherwise receive zero probability, which can make an entire sentence probability zero.
- 我们需要 smoothing，是因为未见 n-gram 否则会得到零概率，从而让整个句子的概率变成零。

- Smoothing redistributes probability mass so that unseen events remain possible.
- smoothing 会重新分配概率质量，让未见事件保持非零可能性。

### Q17. What is perplexity?

- Perplexity is a standard metric for language models, and lower perplexity means the model better fits the test set.
- perplexity 是语言模型的标准指标，perplexity 越低，说明模型对测试集拟合得越好。

- Intuitively, it measures how surprised or perplexed the model is by the test data.
- 直觉上，它衡量的是模型面对测试数据时有多惊讶、或者说有多困惑。

### Q18. Why are RNNs and LSTMs introduced after n-gram models?

- They are introduced because n-gram models use only short fixed-length context, whereas RNNs and LSTMs can carry information through a sequence.
- 它们之所以在 n-gram 模型之后出现，是因为 n-gram 只能用短且固定长度的上下文，而 RNN 和 LSTM 可以沿着序列传递信息。

- This makes them better suited to modeling longer dependencies in language.
- 这使它们更适合处理语言中的较长依赖关系。

### Q19. What does an LSTM add beyond a simple RNN?

- An LSTM adds memory and gating mechanisms that help decide what to keep, what to forget, and what to output.
- LSTM 在普通 RNN 基础上增加了记忆和门控机制，用来决定保留什么、忘掉什么、输出什么。

- This makes it more effective than a plain RNN for longer sequences.
- 因此在较长序列上，LSTM 通常比普通 RNN 更有效。

### Q20. Why is Week 3 attention motivated at the end of Week 2?

- Attention is motivated because even LSTMs still pass information through a linear sequential chain, which makes long-distance interaction difficult.
- Week 2 结尾之所以引出 attention，是因为即使 LSTM 仍然是沿线性顺序链传递信息，长距离交互依然困难。

- Attention offers a way for non-consecutive positions to interact more directly.
- attention 提供了一种让非相邻位置更直接交互的方法。

---

## 13. One-Sentence Summary / 一句话总括 Week 2

- Week 2 shows that NLP progressed from sparse identity-based representations to learned semantic vectors, from rule-based sentence membership to probabilistic likelihood, and from short-context probabilistic models to sequential neural language models.
- Week 2 展示了 NLP 如何从稀疏的身份表示走向学习得到的语义向量，从基于规则的句子归属判断走向概率 likelihood，再从短上下文概率模型走向顺序神经语言模型。
