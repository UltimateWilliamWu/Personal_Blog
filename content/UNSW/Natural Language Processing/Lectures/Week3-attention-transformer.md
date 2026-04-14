## 1. Announcements and Weekly Roadmap / 课程提醒与本周路线图

- The lecture begins by congratulating students on completing the first quiz.
- 课件一开始先祝贺大家完成了第一次 quiz。

- The lecturer explicitly says the final exam will not require memorizing code syntax word for word.
- 老师明确说，期末考试不会要求逐字背代码语法。

- Instead, the exam may ask fill-in-the-gap style code questions or ask what a piece of code is doing.
- 相反，考试可能会问代码填空，或者问某段代码在做什么。

- The lecture also says the final exam will not be only code-based, and a sample exam will be provided.
- 课件还说明期末不只是代码题，并且之后会提供 sample exam。

- The final exam is an invigilated BYOD exam, and the timetable will be announced later.
- 期末考试是监考的 BYOD 考试，具体时间表之后通知。

- The individual assignment covers material from Weeks 1 to 3 and was announced as available later that day.
- 个人作业覆盖 Week 1 到 Week 3 的内容，并在当天稍后发布。

- The assignment due date shown on the slide is Friday, 20 March 2026, at 5:00 PM.
- 课件给出的作业截止时间是 2026 年 3 月 20 日周五下午 5 点。

- The weekly roadmap lists attention intuition, attention in recurrent language modeling, key-query-value attention, Transformer architecture, multi-head attention, encoder, decoder, byte-pair encoding, positional encoding, and the impact of Transformer.
- 本周路线图包括 attention 直觉、recurrent language modeling 中的 attention、key-query-value attention、Transformer 架构、多头注意力、encoder、decoder、byte-pair encoding、positional encoding，以及 Transformer 的影响。

---

## 2. Why Attention? / 为什么需要 Attention

- The lecture motivates attention through a simple visual example: to answer a question, you focus on parts of the image that matter to the key term.
- 课件先用一个简单视觉例子来引出 attention：为了回答问题，你会重点关注图像中和关键词相关的部分。

- This is described as an intuition for cross-attention.
- 这被用来作为 cross-attention 的直觉。

- The recap from Week 2 is that recurrent language models rely on sequential information passing.
- 对 Week 2 的回顾是：recurrent language models 依赖顺序式信息传递。

- Fixed-length vectors become a bottleneck when a model has to compress too much information into one running state.
- 当模型不得不把过多信息压进一个持续更新的状态向量时，fixed-length vectors 会形成 bottleneck。

- The lecture gives long-range semantic completion and coreferential pronoun selection as examples of where this bottleneck hurts.
- 课件用长距离语义填空和指代代词选择来说明，这种 bottleneck 会在哪些任务上出问题。

- In long-distance prediction, the model may need to connect a later blank with a much earlier state name or entity mention.
- 在长距离预测中，模型可能需要把后面的空位和前面很早出现的地点名或实体联系起来。

- In pronoun resolution, the correct next token may depend on which earlier noun phrase is the relevant antecedent.
- 在代词消解里，正确的下一个词常常取决于前面哪个名词短语才是合适的先行词。

- The lecture says that when generating the next word, we want to pay attention to some words more than others.
- 课件明确说，在生成下一个词时，我们希望对某些词更“关注”，而不是平均地看所有词。

- Attention is therefore introduced as a way for a neural layer to focus on specific parts of a sequence.
- 因此，attention 被引入为一种让神经层聚焦序列中特定部分的机制。

- The lecture distinguishes self-attention from cross-attention.
- 课件明确区分了 self-attention 和 cross-attention。

- Self-attention models relationships among words inside one sentence or sequence.
- self-attention 建模的是同一句子或同一序列内部词与词之间的关系。

- Cross-attention models relationships across paired sequences, such as source and target sequences in translation.
- cross-attention 建模的是成对序列之间的关系，例如机器翻译里的 source sequence 和 target sequence。

- The lecture also notes that bidirectional LSTMs help in some settings, but they do not remove the sequential bottleneck that motivates attention.
- 课件也提到 bidirectional LSTM 在一些场景里有帮助，但它并没有消除 attention 要解决的顺序瓶颈。

---

## 3. Attention in Recurrent Language Modeling / Recurrent 语言模型中的 Attention

- Before introducing Transformer, the lecture first discusses attention added to recurrent models, especially in the Bahdanau style.
- 在正式进入 Transformer 之前，课件先讲了加在 recurrent 模型上的 attention，尤其是 Bahdanau 风格的 attention。

- The Bahdanau attention reference on the slide is the 2015 neural machine translation paper.
- 课件引用的 Bahdanau attention 就是 2015 年那篇神经机器翻译论文。

- The lecture’s math board introduces an energy score between the current position and previous positions.
- 课件的数学板书先引入了当前位置和过去位置之间的 energy score。

- These energy scores are turned into attention weights.
- 这些 energy scores 会进一步转成 attention weights。

- The attention weights are then used to build a context vector.
- attention weights 接着会被用来构造一个 context vector。

- The lecture defines the context vector as a vector formed from a combination of attention-weighted past information.
- 课件把 context vector 定义为：由过去信息按 attention 权重组合而成的向量。

- It defines state vectors as vectors that store contextual information about past positions in the sentence.
- 课件把 state vectors 定义为：存储句子中过去位置上下文信息的向量。

- It defines attention vectors as vectors that capture the association between the current position and past positions.
- 课件把 attention vectors 定义为：刻画当前位置与过去位置关联程度的向量。

- It defines the hidden state as the vector of the current position used to compare with past positions.
- 课件把 hidden state 定义为：当前位置的向量，用来和过去位置进行比较。

- The next word is then generated as a combination of the current state and the context over past positions.
- 最终，下一个词会基于当前位置状态和所有过去位置构成的 context 来生成。

- The lecture calls this useful but also warns that backpropagation through such recurrent attention structures becomes messy and difficult.
- 课件认为这种方法很有用，但也明确提醒：在这样的 recurrent attention 结构里做反向传播会非常麻烦。

- This complexity is one of the motivations for a model that relies entirely on attention rather than recurrence.
- 这种复杂性正是“完全依赖 attention 而非 recurrence”的模型出现的动机之一。

### 3.1 PyTorch Demo Context / PyTorch demo 的背景知识

- The lecture briefly introduces PyTorch before moving into Transformer code examples.
- 在进入 Transformer 代码例子前，课件先非常简短地介绍了 PyTorch。

- PyTorch is described as originally developed by Meta and now part of the Linux Foundation.
- 课件把 PyTorch 描述为最初由 Meta 开发，现在归属于 Linux Foundation 体系。

- Tensors are described as objects similar to NumPy arrays but able to use GPUs.
- tensor 被描述成类似 NumPy array，但可以利用 GPU 的对象。

- TensorFlow is mentioned as an alternative framework.
- 课件也提到了 TensorFlow 作为替代框架。

- The accompanying PyTorch basics notebook shows how to define a simple neural network, run a forward pass, compute loss, optimize with Adam, use DataLoader mini-batching, and track train/validation loss.
- 配套的 PyTorch basics notebook 演示了如何定义简单神经网络、做 forward pass、计算 loss、用 Adam 优化、使用 DataLoader 小批训练，并跟踪 train/validation loss。

---

## 4. From Attention to Transformer / 从 Attention 走向 Transformer

- The lecture summarizes the key historical jump with the phrase “Attention is all you need.”
- 课件用 “Attention is all you need.” 这句话来概括这次关键历史跃迁。

- The slide quotes the original Transformer paper as “eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output.”
- 课件引用原始 Transformer 论文的话，强调它“抛弃 recurrence，完全依靠 attention 来建立 input 和 output 之间的全局依赖”。

- Transformer is introduced as a sequence-to-sequence model that uses attention.
- Transformer 被定义为一个使用 attention 的 sequence-to-sequence 模型。

- It is also described as a transducer that transforms one sentence into another.
- 课件还把它描述成一个 transducer，也就是把一个句子转换成另一个句子的系统。

- The lecture notes that Transformer was originally evaluated on machine translation and other seq2seq tasks.
- 课件说明，Transformer 最早是在机器翻译和其他 seq2seq 任务上验证的。

- It then spawned many other models, including encoder-only and decoder-only derivatives such as BERT and GPT.
- 后来它衍生出许多其他模型，包括 encoder-only 和 decoder-only 类型的模型，例如 BERT 和 GPT。

### 4.1 Components of a Transformer / Transformer 的组成部分

- The lecture explicitly lists five components: tokenizer, positional encoding, encoder, decoder, and transformer head.
- 课件明确列出了 Transformer 的五个组成：tokenizer、positional encoding、encoder、decoder，以及 transformer head。

- The tokenizer represents a sentence as a sequence of tokens.
- tokenizer 会把一个句子表示成 token 序列。

- Positional encoding injects sequence information and is one key reason Transformer can get rid of recurrence.
- positional encoding 会注入序列位置信息，这也是 Transformer 能摆脱 recurrence 的关键原因之一。

- A stack of encoders receives the input sentence and maps it to hidden representations.
- 一叠 encoder 会接收输入句子，并把它映射成隐藏表示。

- A stack of decoders receives the encoder output together with the generated output-so-far and predicts the next token.
- 一叠 decoder 会接收 encoder 的输出以及当前已经生成的部分，并预测下一个 token。

- The transformer head is the task-specific prediction formulation attached on top.
- transformer head 指的是加在模型顶端、用于具体预测目标的那一层或那组层。

### 4.2 A Translation Example / 翻译例子

- The lecture uses a toy translation example: input “The boy drinks milk” and output “Il ragazzo beve il latte”.
- 课件用一个简单翻译例子来说明 Transformer：输入 “The boy drinks milk”，输出 “Il ragazzo beve il latte”。

- The decoder predicts the next output token conditioned on the encoder representation of the source sentence and the target prefix generated so far.
- decoder 预测下一个输出 token 时，会同时依赖 source sentence 的 encoder 表示以及目前已经生成的 target prefix。

- The pseudocode slide summarizes this as predicting the next word in the output sequence conditional on the input sequence and the output sequence so far.
- 课件里的伪代码把这件事总结成：在给定 input sequence 和当前 output sequence 前缀的条件下，预测输出序列的下一个词。

---
## 5. Query, Key, Value, and Scaled Dot-Product Attention / Query、Key、Value 与缩放点积注意力

- The lecture then rebuilds attention in Transformer language using key-query-value terminology.
- 接着课件用 key-query-value 术语重新解释 Transformer 里的 attention。

- Query, keys, values, and outputs are all vectors.
- query、key、value 以及输出本质上都是向量。

- The query represents the current token position asking what information it should retrieve.
- query 表示当前位置的 token 在“发问”：我应该从哪里取信息。

- Keys represent addresses or comparison handles for candidate tokens.
- key 可以理解成候选 token 的“地址”或“可比较标识”。

- Values represent the content that will actually be aggregated when attention weights are applied.
- value 表示真正会被加权汇总的内容。

- Scaled dot-product attention computes similarity scores between a query and keys, scales them, normalizes them, and then uses those weights to combine values.
- scaled dot-product attention 会先计算 query 和 keys 的相似度分数，再做缩放和归一化，最后用这些权重去加权 values。

- The lecture explicitly introduces scaled dot-product attention as the standard formulation.
- 课件明确把 scaled dot-product attention 作为标准形式来介绍。

- The supermarket example and pen-and-paper slide are used to stress that one query can compare itself with many key-value pairs and then decide which values matter more.
- 课件用 supermarket example 和手算例子强调：一个 query 可以和很多 key-value 对比较，再决定哪些 values 更重要。

- The pseudocode slide emphasizes that there are no linear chains in this formulation.
- 课件里的伪代码还强调：在这种 formulation 下，不再依赖线性链式传递。

### 5.1 Self-Attention / Self-Attention

- Self-attention means attention for a token with respect to all other tokens in the same sentence.
- self-attention 指的是：某个 token 对同一句子里所有其他 token 做 attention。

- The lecture explicitly defines it that way on the self-attention slide.
- 课件在 self-attention 那页就是这样直接定义的。

- This lets each token build a contextualized representation by looking at all relevant tokens in the sequence.
- 这样每个 token 都能通过查看序列里相关的其他 token，构造出带上下文的表示。

- The lecture uses a colorful sentence like “I love nature: green trees, pink flowers, red apples” to stress that semantics is multi-dimensional.
- 课件用 “I love nature: green trees, pink flowers, red apples” 这类例子来强调：语义是多维的。

### 5.2 Multi-Head Attention / 多头注意力

- The lecture asks whether multiple projections can be learned to capture different aspects of semantics.
- 课件提出一个问题：我们能不能学多组投影，分别捕捉语义的不同方面。

- The answer is multi-head attention.
- 答案就是 multi-head attention。

- Different heads are independent and therefore can be parallelized.
- 不同的 attention heads 相互独立，因此可以并行计算。

- The original Transformer paper used 8 heads.
- 原始 Transformer 论文使用了 8 个 heads。

- Multi-head attention lets the model capture different relations or interaction patterns in parallel.
- multi-head attention 让模型能够并行捕捉不同类型的关系或交互模式。

- After attention heads produce separate outputs, these outputs must be combined.
- 各个 attention heads 产生输出之后，还需要把这些输出重新组合起来。

- The lecture then introduces Add & Normalize together with residual connections.
- 课件接着引入了 Add & Normalize，以及 residual connections。

### 5.3 Encoder Blocks / Encoder 块

- Each encoder contains multi-head self-attention, a position-wise feed-forward network, and residual plus add-norm operations around these sublayers.
- 每个 encoder 都包含 multi-head self-attention、position-wise feed-forward network，以及包在这些子层外面的 residual 和 add-norm。

- The lecture explicitly says the fully connected feed-forward network is applied to every position separately.
- 课件明确说，fully connected feed-forward network 是对每个位置分别应用的。

- The original Transformer uses `N = 6` encoder layers.
- 原始 Transformer 使用 `N = 6` 个 encoder layers。

- The illustrative Transformer notebook in `Week_3.zip` mirrors this structure with a `MultiHeadAttention` module, a position-wise feed-forward network, encoder layers, decoder layers, and a full Transformer class.
- `Week_3.zip` 里的 illustrative Transformer notebook 也复现了这个结构，包含 `MultiHeadAttention`、position-wise feed-forward network、encoder layer、decoder layer 和完整的 Transformer 类。

---

## 6. Decoder and Masked Attention / Decoder 与 Masked Attention

- The decoder cannot freely look at future tokens while generating a sequence.
- decoder 在生成序列时不能自由地看未来 token。

- The lecture asks this explicitly: can the decoder use subsequent tokens when generating a sequence?
- 课件直接把这个问题写出来：decoder 在生成时能不能使用后面的 token。

- The answer is no, so masked attention is used.
- 答案是否定的，所以要使用 masked attention。

- Masked attention prevents a position from attending to subsequent positions in the output sequence.
- masked attention 会阻止当前位置去关注输出序列中后面的那些位置。

- The pseudocode slide says that for subsequent positions, we mask the value during attention computation.
- 课件伪代码页写得很直接：对于后续位置，要在 attention 计算中做 mask。

- In the decoder, there are two kinds of attention.
- 在 decoder 中，其实有两种 attention。

- First, there is masked self-attention over the output sequence generated so far.
- 第一种是对当前已经生成的 output sequence 做 masked self-attention。

- Second, there is attention over the encoder output, which is effectively cross-attention.
- 第二种是对 encoder 输出做 attention，本质上就是 cross-attention。

- The decoder also includes a feed-forward network plus add-norm and residual-style structure.
- decoder 还包含 feed-forward network，以及 add-norm 和 residual 风格结构。

- The original Transformer uses `N = 6` decoder layers as well.
- 原始 Transformer 同样使用 `N = 6` 个 decoder layers。

- The lecture’s decoder slide explicitly lists four components for each decoder: masked multi-head attention, position-wise feed-forward, residual plus add-norm, and encoder-output attention.
- 课件在 decoder 那页明确列出每个 decoder 的四个组成：masked multi-head attention、position-wise feed-forward、residual + add-norm，以及对 encoder 输出的 attention。

---

## 7. Tokenization and Byte-Pair Encoding / 分词与字节对编码

- After explaining the core Transformer blocks, the lecture turns to input representations.
- 讲完 Transformer 核心结构之后，课件开始讲输入表示。

- Tokenization is defined as the process of splitting a sequence into tokens.
- tokenization 被定义为把一个序列切分成 tokens 的过程。

- The lecture reminds students that representations will ultimately be learned for tokens.
- 课件提醒大家：最终被学习表示的是 tokens。

- It also explicitly asks students to remember stemming and lemmatization from earlier weeks.
- 课件还明确提醒大家回想前面学过的 stemming 和 lemmatization。

- Three tokenization types are shown: word-level, character-level, and sub-word tokenization.
- 课件展示了三类 tokenization：word-level、character-level 和 sub-word tokenization。

- Word-level tokenization keeps whole words as tokens.
- word-level tokenization 会把完整单词当作 token。

- Character-level tokenization breaks everything down to characters.
- character-level tokenization 会把一切拆到字符级别。

- Sub-word tokenization keeps common words whole but breaks rarer forms into reusable pieces.
- sub-word tokenization 会保留常见词的整体形式，同时把较少见的词拆成可复用的子词片段。

- The lecture specifically introduces byte-pair encoding, or BPE.
- 课件专门引入了 byte-pair encoding，也就是 BPE。

- BPE was originally developed as a text compression algorithm.
- BPE 最初是作为一种文本压缩算法提出的。

- The intuition is to retain the most common words as whole tokens and split less common words into sub-word tokens.
- 它的直觉是：最常见的词保留为整体 token，较少见的词拆成 sub-word tokens。

- This is related to compression because common patterns are kept and reused efficiently.
- 这和压缩的关系在于：常见模式会被保留和高效复用。

### 7.1 Corpus-Based Tokenization / 语料驱动的分词

- The lecture presents BPE as a corpus-based tokenizer.
- 课件把 BPE 描述成一种 corpus-based tokenizer。

- Step 1 is the learner phase, where tokenization rules are learned from a corpus.
- 第一步是 learner 阶段，在这个阶段里会从语料中学习分词规则。

- The algorithm starts with a vocabulary of basic symbols such as letters.
- 算法一开始会以最基础的符号集合为词表，例如字母。

- It repeatedly finds the most common pair, merges it into a new symbol, stores the merge, and updates the vocabulary.
- 然后它不断寻找最常见的符号对，把它们合并成新符号，记录 merge 规则，并更新词表。

- Step 2 is the tokenizer phase, where the learned merge rules are applied to new test sentences.
- 第二步是 tokenizer 阶段，此时会把学到的 merge rules 应用到新的测试句子上。

- The lecture also mentions WordPiece tokenization as a related sub-word method.
- 课件还提到了 WordPiece tokenizer，说明它和 BPE 同属相关的 sub-word 方法。

### 7.2 BPE Demo Notes / BPE demo 补充

- The BPE notebook in `Week_3.zip` trains a byte-level BPE tokenizer on a Brown corpus sample.
- `Week_3.zip` 里的 BPE notebook 会在 Brown corpus 的 sample 上训练一个 byte-level BPE tokenizer。

- It defines special tokens such as `<s>`, `<pad>`, `</s>`, `<unk>`, and `<mask>`.
- 它还定义了 `<s>`、`<pad>`、`</s>`、`<unk>`、`<mask>` 这些 special tokens。

- The notebook then encodes example sentences into tokens and token IDs and decodes them back.
- 接着 notebook 会把示例句子编码成 tokens 和 token IDs，再解码回来。

- This reinforces the lecture’s point that tokenization is a learned preprocessing stage tightly tied to model input.
- 这进一步强化了课件的观点：tokenization 不是随便切词，而是和模型输入紧密耦合的学习式预处理。

---

## 8. Token Embeddings and Positional Encoding / Token Embedding 与位置编码

- Once the input has been tokenized, token embeddings are learned during training.
- 一旦输入被切成 tokens，token embeddings 就会在训练过程中被学习出来。

- During inference, the already learned embedding matrix is reused to map token IDs to vectors.
- 在推理阶段，已经学好的 embedding matrix 会被重复使用，把 token IDs 映射成向量。

- However, Transformer has no recurrence, so token embeddings alone do not tell the model where each token occurs in the sequence.
- 但是 Transformer 没有 recurrence，所以光有 token embeddings 还不能告诉模型每个 token 在序列中的位置。

- The lecture therefore says the model injects positional encoding.
- 所以课件说，Transformer 会“注入” positional encoding。

- Input encoding is presented as token embedding plus positional encoding.
- 课件把输入编码写成 token embedding 加上 positional encoding。

### 8.1 Positional Encoding Requirements / 位置编码的要求

- The lecture says that if token embeddings have length 50 and the maximum sequence length is 25, we want 25 position vectors of length 50.
- 课件举例说，如果 token embeddings 的长度是 50，而最大序列长度是 25，那么我们就需要 25 个长度为 50 的位置向量。

- Each position vector should be unique.
- 每个位置向量都应该是唯一的。

- The positional scheme should also generalize to longer lengths.
- 这种位置编码还应该能够泛化到更长的序列长度。

- The original Transformer uses fixed positional encoding.
- 原始 Transformer 使用 fixed positional encoding。

- Newer variants may use learnable positional encodings.
- 更新的模型变体也可能使用 learnable positional encodings。

- The quote on the slide explains that the sinusoidal design was hypothesized to help the model learn relative positions, because a fixed offset can be represented as a linear function of another position encoding.
- 课件上的引用解释说，正弦位置编码的设计假设有助于模型学习相对位置，因为对于固定偏移量，后一个位置编码可以表示成前一个位置编码的线性函数。

### 8.2 Positional Encoding Demo Notes / 位置编码 demo 补充

- The positional encoding notebook visualizes sinusoidal encodings with different sequence lengths, dimensions, and even a modified base value.
- positional encoding notebook 会把 sinusoidal encodings 在不同序列长度、不同维度，甚至不同 base 设置下可视化出来。

- This helps show the alternating sine-cosine structure and why different dimensions oscillate at different rates.
- 这有助于理解正弦和余弦交替出现的结构，以及为什么不同维度的变化速度不同。

- The notebook directly implements the original Transformer-style sinusoidal formula.
- 这个 notebook 直接实现了原始 Transformer 风格的 sinusoidal 公式。

---

## 9. Looking Back at Transformer / 回看 Transformer 全图

- The lecture includes a quiz slide asking students to match textual descriptors to components in a Transformer diagram.
- 课件里有一页 quiz，让学生把文字描述和 Transformer 图中的部件对应起来。

- The provided answers are that fixed embeddings correspond to item `[1]`, masked preceding-token-only attention corresponds to `[7]`, the language-model head corresponds to `[3]`, and key-query-value based attention corresponds to `[2], [4], [7]`.
- 课件给出的答案是：fixed embeddings 对应 `[1]`，只看前面 token 的 masked attention 对应 `[7]`，language model head 对应 `[3]`，而使用 key-query-value 的 attention 对应 `[2]、[4]、[7]`。

- This slide is important because it checks whether students can map textual descriptions to architectural components instead of only memorizing the diagram visually.
- 这页很重要，因为它考的是：你能不能把文字描述准确映射到架构组件，而不是只会看图背图。

### 9.1 Configuration Parameters / 配置参数

- The lecture includes typical Transformer configuration parameters such as vocabulary size, number of GPUs, `d_model`, number of layers `N`, and training benchmarks.
- 课件还列出了典型 Transformer 配置参数，例如词表大小、GPU 数量、`d_model`、层数 `N` 以及训练 benchmark。

- The slide lists vocabulary size `37000`, `8` NVIDIA P100 GPUs, `d_model = 512`, and `N = 6`.
- 课件列出的参数包括：词表大小 `37000`、`8` 张 NVIDIA P100 GPU、`d_model = 512`、`N = 6`。

- It also states that the original model was trained on the English-to-German and English-to-French WMT benchmarks.
- 课件还说明原始模型是在英德和英法 WMT benchmark 上训练的。

- The lecturer explicitly notes that it is customary to include such configuration parameters in model papers.
- 老师还明确说，在模型论文里写清这些配置参数是很常见、也很重要的做法。

### 9.2 Impact and Legacy / 影响与遗产

- The lecture points students to the Illustrated Transformer article as another view of the model.
- 课件把 Illustrated Transformer 那篇文章作为理解模型的另一个视角推荐给学生。

- It then discusses the impact of Transformer on the world, including the rise of derivative models and social or regulatory consequences.
- 接着课件讲了 Transformer 对世界的影响，包括衍生模型的爆发式出现，以及社会和监管层面的后果。

- The lecture says new models continue to be released, often each larger than the previous one.
- 课件指出，新模型仍在不断发布，而且常常一个比一个更大。

- It also states explicitly that Transformer is the basis of state-of-the-art models and that it spawned large language models.
- 课件还明确说，Transformer 是许多 state-of-the-art 模型的基础，并且催生了 large language models。

- The final slide of the lecture asks what kind of models Transformer led to and answers: large language models, which is the topic of Week 4.
- 课件最后一页问：Transformer 最终带来了什么样的模型，答案就是 large language models，这正好引向 Week 4。

- The lecture also includes a reflective reminder that this introductory course is only a distilled version of NLP and asks students to think about why they want to study NLP.
- 课件还插入了一张反思页，提醒大家这门 introductory 课程只是 NLP 的精简版，并让大家思考自己为什么要学 NLP。

---
## 10. High-Frequency Exam Points / 高频考点总结

- Attention is introduced to overcome the bottleneck of sequential information passing in recurrent models.
- 引入 attention 的核心原因，是为了缓解 recurrent 模型中顺序式信息传递带来的 bottleneck。

- Self-attention models relations within one sequence, while cross-attention models relations across paired sequences.
- self-attention 建模同一序列内部的关系，而 cross-attention 建模成对序列之间的关系。

- Bahdanau-style attention uses similarity or energy scores, turns them into attention weights, and forms a context vector.
- Bahdanau 风格的 attention 先算 similarity 或 energy scores，再转成 attention weights，并形成 context vector。

- Query, key, and value are all vectors, and scaled dot-product attention compares queries with keys and aggregates values.
- query、key、value 都是向量，而 scaled dot-product attention 会比较 query 和 keys，再汇总 values。

- Multi-head attention learns multiple independent projections in parallel to capture different semantic aspects.
- multi-head attention 会并行学习多组独立投影，用来捕捉语义的不同方面。

- An encoder block contains multi-head self-attention, a position-wise feed-forward network, and residual plus add-norm structure.
- 一个 encoder block 包含 multi-head self-attention、position-wise feed-forward network，以及 residual + add-norm 结构。

- A decoder block contains masked self-attention, cross-attention over encoder output, a feed-forward network, and residual plus add-norm structure.
- 一个 decoder block 包含 masked self-attention、对 encoder 输出的 cross-attention、feed-forward network，以及 residual + add-norm 结构。

- Masked attention prevents access to future output tokens during generation.
- masked attention 会阻止生成时看到未来输出 token。

- Transformer is a seq2seq model and a transducer, originally evaluated on translation and other seq2seq tasks.
- Transformer 是一个 seq2seq model，也是一个 transducer，最初主要在翻译和其他 seq2seq 任务上验证。

- Tokenization splits a sequence into tokens, and sub-word tokenization such as BPE is especially important in Transformer pipelines.
- tokenization 会把序列切成 tokens，而 BPE 这类 sub-word tokenization 在 Transformer 流程中尤其重要。

- BPE learns merge rules from corpus statistics by repeatedly merging the most frequent symbol pair.
- BPE 会根据语料统计反复合并最常见的符号对，从而学习 merge rules。

- Token embeddings are learned during training, but positional encodings must be added because Transformer has no recurrence.
- token embeddings 会在训练中学习出来，但由于 Transformer 没有 recurrence，还必须加入 positional encoding。

- The original Transformer uses fixed sinusoidal positional encodings, while later models may use learnable or modified variants.
- 原始 Transformer 使用固定的 sinusoidal positional encoding，而后来的模型可能用可学习或改进版本。

- Key configuration parameters from the original paper include `d_model = 512`, `N = 6`, and multi-head attention with 8 heads.
- 原始 Transformer 的关键配置参数包括 `d_model = 512`、`N = 6`，以及 8 个头的 multi-head attention。

- Transformer removed recurrence, parallelized attention, and became the basis of large language models.
- Transformer 去掉 recurrence、实现了 attention 的并行化，并最终成为 large language models 的基础。

---

## 11. Model Answers to Likely Exam Questions / 常见考题标准答案

### Q1. Why was attention introduced?

- Attention was introduced because recurrent models pass information sequentially, which creates bottlenecks and makes long-distance dependencies difficult to capture.
- attention 被引入，是因为 recurrent 模型靠顺序传递信息，这会形成瓶颈，也让长距离依赖难以捕捉。

### Q2. What is the difference between self-attention and cross-attention?

- Self-attention models relations among tokens in the same sequence, while cross-attention models relations between tokens in different sequences, such as source and target sentences.
- self-attention 建模同一序列内部 token 的关系，而 cross-attention 建模不同序列之间的关系，例如源句和目标句之间的关系。

### Q3. What is a context vector in attention?

- A context vector is a weighted combination of information from other positions, where the weights are determined by attention scores.
- context vector 是其他位置的信息加权组合，其中权重由 attention scores 决定。

### Q4. What are query, key, and value?

- The query represents what the current token is looking for, keys represent matchable addresses for candidate tokens, and values represent the content that will be aggregated.
- query 表示当前位置在寻找什么，key 表示候选 token 可被匹配的标识，value 表示真正会被聚合的内容。

### Q5. What is scaled dot-product attention?

- Scaled dot-product attention computes dot-product similarity between a query and keys, scales the scores, normalizes them, and uses them to combine values.
- scaled dot-product attention 会计算 query 与 keys 的点积相似度，对分数做缩放与归一化，再用这些权重加权组合 values。

### Q6. Why do we use multi-head attention?

- We use multi-head attention because a single attention projection may capture only one aspect of semantic or structural relation, whereas multiple heads can capture different aspects in parallel.
- 使用 multi-head attention，是因为单一 attention 投影往往只能捕捉一种语义或结构关系，而多个 heads 可以并行捕捉不同方面。

### Q7. What does Add & Normalize do in Transformer?

- Add & Normalize combines residual connections with normalization so that training is more stable and information from previous layers is preserved.
- Add & Normalize 把 residual connection 和 normalization 结合起来，从而让训练更稳定，并保留前层信息。

### Q8. Why does the decoder need masking?

- The decoder needs masking because during generation it must not look at future output tokens that have not been generated yet.
- decoder 需要 masking，是因为在生成过程中它不能看到那些尚未生成的未来 output tokens。

### Q9. What are the main components of a Transformer?

- The main components are a tokenizer, positional encoding, encoder stack, decoder stack, and a task-specific head.
- Transformer 的主要组成是 tokenizer、positional encoding、encoder stack、decoder stack，以及 task-specific head。

### Q10. What is byte-pair encoding?

- Byte-pair encoding is a corpus-based sub-word tokenization method that repeatedly merges the most frequent symbol pair to build a token vocabulary.
- byte-pair encoding 是一种基于语料的 sub-word tokenization 方法，它会不断合并最常见的符号对来构建 token vocabulary。

### Q11. Why is sub-word tokenization useful?

- Sub-word tokenization is useful because it keeps common words intact while still allowing rare or unseen words to be represented through reusable pieces.
- sub-word tokenization 很有用，因为它既能保留常见词整体形式，又能用可复用子词片段来表示罕见词或未见词。

### Q12. Why does Transformer need positional encoding?

- Transformer needs positional encoding because attention alone does not tell the model where a token occurs in the sequence.
- Transformer 需要 positional encoding，是因为 attention 本身并不能告诉模型一个 token 位于序列的什么位置。

### Q13. What is the difference between token embeddings and positional encodings?

- Token embeddings represent lexical identity or meaning, while positional encodings represent token position in the sequence.
- token embeddings 表示词项身份或语义，而 positional encodings 表示 token 在序列中的位置。

### Q14. What is an encoder block?

- An encoder block is a Transformer layer containing multi-head self-attention, a position-wise feed-forward network, and residual plus add-norm operations.
- encoder block 是 Transformer 中的一层，其中包含 multi-head self-attention、position-wise feed-forward network，以及 residual + add-norm 操作。

### Q15. What is a decoder block?

- A decoder block contains masked self-attention, cross-attention over encoder outputs, a position-wise feed-forward network, and residual plus add-norm operations.
- decoder block 包含 masked self-attention、对 encoder 输出的 cross-attention、position-wise feed-forward network，以及 residual + add-norm 操作。

### Q16. Why is Transformer considered a major advance over recurrent models?

- Transformer is considered a major advance because it removes recurrence, allows parallel attention-based computation, and models long-range dependencies more directly.
- Transformer 被认为是对 recurrent 模型的重大推进，因为它去掉了 recurrence，允许并行 attention 计算，并且能更直接地建模长距离依赖。

### Q17. What is the significance of the original Transformer configuration values?

- Values such as `d_model = 512`, `N = 6`, and 8 attention heads are important because they specify the concrete architecture used in the original paper and are part of how model papers report reproducible setups.
- 像 `d_model = 512`、`N = 6` 和 8 个 attention heads 这样的参数之所以重要，是因为它们规定了原始论文里的具体结构，也是模型论文进行可复现实验报告的一部分。

### Q18. Why does Week 3 naturally lead to Week 4?

- Week 3 naturally leads to Week 4 because Transformer became the foundation of large language models, which are the focus of the next lecture.
- Week 3 很自然地引向 Week 4，因为 Transformer 最终成为 large language models 的基础，而后者正是下一讲的主题。

---

## 12. One-Sentence Summary / 一句话总括 Week 3

- Week 3 shows how NLP moved from sequential bottlenecks to direct relation modeling through attention, and how Transformer combined self-attention, masking, tokenization, and positional encoding into the architecture that underlies modern large language models.
- Week 3 展示了 NLP 如何从顺序式 bottleneck 走向通过 attention 直接建模关系，并说明 Transformer 如何把 self-attention、masking、tokenization 和 positional encoding 组合成支撑现代大语言模型的核心架构。
