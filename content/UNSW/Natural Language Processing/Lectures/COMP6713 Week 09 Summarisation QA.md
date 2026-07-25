---
tags:
  - UNSW
  - UNSW/COMP6713
  - Topic/NLP
  - Type/Lecture
---

# Week 9: Summarisation & Question-Answering

- These notes cover the Week 9 lecture, the summarization pipeline ideas in the slides, and the demo notebooks in `week9-demos.zip`.
- 这份笔记覆盖 Week 9 课件、课件中的 summarization pipeline 思路，以及 `week9-demos.zip` 里的 demo notebook 内容。

## 1. Weekly Position and Task Framing / 本周定位与任务形式

- Week 9 moves from sentence-level tasks to document-level and question-driven generation tasks.
- Week 9 把课程重点从 sentence-level task 推进到 document-level 和 question-driven generation task。

- The lecture contrasts earlier tasks with this week by showing that summarization and QA take a document or a question-document pair as input and produce a summary or an answer as output.
- 课件通过对比前几周任务说明，本周 summarization 和 QA 的输入通常是 document 或 question-document pair，输出则是 summary 或 answer。

- The lecture explicitly says that summarization, MT, and QA are all seq2seq-style tasks, but their constraints are different.
- 课件明确指出 summarization、MT 和 QA 都可以看成 seq2seq-style task，但它们的约束条件并不相同。

- In MT, the output is translated text of roughly similar length, while in summarization the output is usually shorter, and in QA the answer may be short, long, extractive, or generative.
- 在 MT 中，输出通常是长度相近的翻译文本；而在 summarization 中，输出通常更短；在 QA 中，答案则可能很短、很长、extractive，或者 generative。

- The lecture highlights that summarization often uses almost the same vocabulary as the source, whereas QA may require generation beyond a simple extractive span.
- 课件强调 summarization 往往与源文档共享相近词汇，而 QA 则可能超出简单 span extraction，需要更强的生成能力。

## 2. What a Summary Is / 什么是 Summary

- A summary is defined as a short and clear expression of the most important facts or ideas from a source document.
- summary 被定义为对 source document 中最重要事实或观点的简短而清晰的表达。

- The objective of summarization is to produce a shorter text that still covers the core content of the source.
- summarization 的目标是生成更短的文本，同时仍然覆盖 source 的核心内容。

- The lecture notes that some genres already contain a natural summary structure, such as journalistic leads and research abstracts.
- 课件指出，有些文体本身就带有天然 summary 结构，例如新闻导语和论文摘要。

- This matters because summarization systems often exploit document structure, position, and genre conventions.
- 这点之所以重要，是因为 summarization system 往往会利用文档结构、句子位置和 genre convention。

- A good summary is therefore not only short, but also representative, informative, and faithful to the source.
- 因此，一个好的 summary 不只是短，还必须具有代表性、信息性和对 source 的忠实性。

## 3. Extractive vs Abstractive Summarisation / 抽取式与生成式摘要

- Extractive summarization selects a subset of sentences from the original document.
- extractive summarization 会从原文中选出一部分句子作为摘要。

- The number of selected sentences can be a parameter, so the task can be formulated as retrieval or sentence classification.
- 被选句子的数量可以作为参数，因此该任务既可以被表述为 retrieval，也可以被表述为 sentence classification。

- Abstractive summarization generates a new summary that may not appear verbatim in the original document.
- abstractive summarization 则会生成新的 summary，而这些句子不一定逐字出现在原文里。

- The lecture frames abstractive summarization as a long seq2seq generation problem.
- 课件把 abstractive summarization 表述为一种 long seq2seq generation problem。

- The slides also mention that real systems often combine extractive and abstractive components rather than staying purely in one category.
- 课件还提到，真实系统往往会把 extractive 和 abstractive 组件结合起来，而不是纯粹只做其中一种。

- Other special formulations include topic-oriented summarization, opinion summarization, and multi-document summarization.
- 其他特殊形式还包括 topic-oriented summarization、opinion summarization 和 multi-document summarization。

- Example applications listed in the lecture include news summarization, opinion summarization, and meeting summarization.
- 课件列出的应用例子包括 news summarization、opinion summarization 和 meeting summarization。

## 4. How Summarisation Is Evaluated / 摘要如何评估

- The lecture asks how summarization should be evaluated and points to overlap-based metrics such as ROUGE and BLEU.
- 课件提出“如何评估 summarization”这个问题，并给出 ROUGE、BLEU 等 overlap-based metric。

- These metrics compare a system summary against one or more reference summaries.
- 这些 metric 会把系统生成的 summary 与一个或多个 reference summary 进行比较。

- The important limitation is that many good summaries can exist for the same document, so overlap is not the full story.
- 这里的重要局限在于，同一篇 document 往往存在多个合理 summary，因此 overlap 并不能完整反映质量。

- In practice, summary evaluation should consider informativeness, coverage, faithfulness, fluency, and sometimes task-specific constraints such as length or structure.
- 在实践中，summary evaluation 应同时考虑 informativeness、coverage、faithfulness、fluency，以及有时还要考虑长度或结构等 task-specific constraint。

## 5. Extractive Summarisation as Graph Ranking / 抽取式摘要作为图排序问题

- One major extractive approach is graph-based summarization, inspired by HITS and PageRank.
- extractive summarization 的一条主要路线是 graph-based summarization，其灵感来自 HITS 和 PageRank。

- In this view, a document is represented as a graph whose nodes are sentences.
- 在这种视角下，document 会被表示成一个 graph，而其中的 node 就是 sentence。

- Summarization then becomes the problem of selecting the most important nodes.
- 这样一来，summarization 就变成了“选出最重要 node”的问题。

- The lecture models the document as a complete graph in which edge weights encode sentence similarity.
- 课件把 document 建模成 complete graph，其中 edge weight 用于编码 sentence similarity。

- Node weights can reflect sentence importance through TF-IDF, the number of unique words, or sentence position in the document.
- node weight 可以通过 TF-IDF、unique word 数量，或者句子在文档中的位置来反映 sentence importance。

- Edge weights can be computed using common-word counts, cosine similarity, longest common subsequence, or related similarity measures.
- edge weight 则可以通过 common-word count、cosine similarity、longest common subsequence 等方式来计算。

## 6. TextRank / TextRank

- TextRank is presented as a seminal unsupervised algorithm for extractive summarization.
- TextRank 被介绍为 extractive summarization 中一个经典的 unsupervised algorithm。

- It derives salience scores for sentences and then clips the ranked list to form a summary.
- 它会先为 sentence 计算 salience score，再从 ranked list 中截取一部分句子作为 summary。

- The lecture emphasises that TextRank does not require sentence labels and instead relies on sentence-to-sentence similarity.
- 课件强调，TextRank 不需要 sentence label，而是依赖 sentence 之间的相似性来工作。

- The algorithm consists of three core steps: initialize the similarity matrix, compute node scores, and iteratively update those scores.
- 这个算法有三个核心步骤：初始化 similarity matrix、计算 node score、以及迭代更新这些 score。

- The lecture explicitly reminds students of the connection to HITS-style iterative ranking.
- 课件明确提醒学生把它与 HITS-style iterative ranking 联系起来理解。

- The demo notebooks reinforce this by showing both a library implementation and a manual similarity-matrix version.
- demo notebook 又进一步强化了这一点：既展示了现成库实现，也展示了手工构造 similarity matrix 的版本。

- In `1-textrank.ipynb`, the summary is first generated with the `summa` library and then reconstructed via a manual sentence-similarity matrix and ranking loop.
- 在 `1-textrank.ipynb` 中，先使用 `summa` 库生成 summary，随后又通过手工构造的 sentence-similarity matrix 和 ranking loop 复现 TextRank 思路。

## 7. Extractive Summarisation as Classification / 抽取式摘要作为分类任务

- A second extractive formulation treats sentence selection as a supervised classification problem.
- 第二种 extractive formulation 把 sentence selection 视为 supervised classification problem。

- Each sentence is assigned a label indicating whether it should appear in the summary.
- 每个句子都会被赋予一个 label，用于表示它是否应该出现在 summary 里。

- The lecture points out that this is often a skewed classification task because only a small fraction of sentences end up in the final summary.
- 课件指出，这通常是一个 skewed classification task，因为最终 summary 只会包含很少一部分句子。

- Sentence-level features include unigrams and modified TF-IDF.
- sentence-level feature 包括 unigrams 和 modified TF-IDF。

- The lecture specifically notes that IDF can be modified into ISF for sentence-focused scoring.
- 课件特别指出，IDF 在这里可以被改成 ISF，以适配 sentence-focused scoring。

- Document-sentence features include sentence position, unique-word counts, and related salience cues.
- document-sentence feature 则包括 sentence position、unique-word count，以及相关的 salience cue。

## 8. Pre-Deep-Learning Abstractive Summarisation / 深度学习之前的生成式摘要

- Before neural methods, abstractive summarization was often approached with phrase selection plus language-model stitching or template-like generation.
- 在 neural method 普及之前，abstractive summarization 常通过 phrase selection 加 language-model stitching，或者 template-like generation 来完成。

- The lecture asks students to imagine a two-step process: identify important phrases and then stitch them into fluent sentences.
- 课件让学生把这类方法理解成两步：先找到重要 phrase，再把它们拼接成 fluent sentence。

- This matters historically because pointer-generator networks and encoder-decoder models inherit this intuition in learned form.
- 这段历史很重要，因为 pointer-generator network 和 encoder-decoder model 在学习式框架中继承了这种直觉。

## 9. Pointer-Generator Networks / Pointer-Generator 网络

- Pointer-generator networks are introduced as a pre-Transformer neural approach to abstractive summarization.
- pointer-generator network 被介绍为 pre-Transformer 时代的 neural abstractive summarization 方法。

- Their central idea is a soft choice between pointing to words in the source and generating words from the vocabulary.
- 它们的核心思想是在 source 中“指向某个词”和“从 vocabulary 中生成一个词”之间做 soft choice。

- The pointer component selects words from positions in the input document.
- pointer component 会从输入文档的位置中选择词。

- The generator component predicts words over the full vocabulary and can therefore produce tokens not copied from the source.
- generator component 则会在完整 vocabulary 上进行预测，因此能够生成 source 中并不存在的新词。

- The mixture coefficient `p_gen` controls the trade-off between pointer behaviour and generator behaviour.
- 混合系数 `p_gen` 控制 pointer 行为与 generator 行为之间的权衡。

- This architecture is motivated by the need to preserve factual content by copying while still maintaining fluent generation.
- 这种架构的动机是：一边通过 copying 保留 factual content，一边仍然保持 fluent generation。

## 10. Post-Transformer Abstractive Summarisation / Transformer 之后的生成式摘要

- The lecture then asks whether the pointer-vs-generate choice can be modeled implicitly by a decoder.
- 接着课件追问：pointer-vs-generate 这种选择，能不能由 decoder 隐式学出来？

- This leads to encoder-decoder Transformer models for abstractive summarization.
- 这就引出了用于 abstractive summarization 的 encoder-decoder Transformer model。

- BART is presented as a key example of such a model.
- BART 被作为这一路线的关键代表模型。

- BART is described as an encoder-decoder Transformer that combines bidirectional and auto-regressive ideas.
- BART 被描述为一个融合 bidirectional 与 auto-regressive 思想的 encoder-decoder Transformer。

- The lecture explains BART through denoising pretraining: first corrupt the input text, then train the model to reconstruct the original.
- 课件用 denoising pretraining 来解释 BART：先破坏输入文本，再训练模型恢复原文。

- Summarization fine-tuning for BART is then described as vanilla seq2seq fine-tuning using the document as input and the shifted summary as target output.
- 随后的 summarization fine-tuning 被描述为 vanilla seq2seq fine-tuning：document 作为输入，shifted summary 作为目标输出。

- In `2-blackbox.ipynb`, this idea is demonstrated with `facebook/bart-large-cnn`, including different generation settings and summary lengths.
- 在 `2-blackbox.ipynb` 中，这一路线通过 `facebook/bart-large-cnn` 进行了演示，并展示了不同 generation setting 和 summary length 的影响。

## 11. Long Documents, Longformer, and LED / 长文档、Longformer 与 LED

- The lecture explains that vanilla self-attention has quadratic time complexity, which restricts standard Transformers to relatively short inputs.
- 课件解释说，vanilla self-attention 具有 quadratic time complexity，因此标准 Transformer 只能处理相对较短的输入。

- The slide explicitly mentions 512-token limits as a practical bottleneck for summarization.
- 课件明确把 512-token 限制当作 summarization 的一个实际 bottleneck。

- This motivates Longformer, which replaces full self-attention with sliding-window attention plus selective global attention.
- 这就引出了 Longformer，它用 sliding-window attention 加 selective global attention 来替代 full self-attention。

- Window attention limits each token to a local context window rather than all positions in the sequence.
- window attention 会把每个 token 的可见范围限制在 local context window 内，而不是整个序列。

- The lecture explains the efficiency gain as reducing the expected attention cost to roughly `n * w`, where `w` is the fixed window size.
- 课件把它的效率提升解释为把注意力计算成本降到大约 `n * w`，其中 `w` 是固定窗口大小。

- Longformer Encoder-Decoder (LED) extends this idea to encoder-decoder summarization models.
- Longformer Encoder-Decoder（LED）则把这一思想扩展到了 encoder-decoder summarization model。

- The lecture notes that LED can be initialized from RoBERTa or BART.
- 课件指出，LED 的参数可以从 RoBERTa 或 BART 初始化而来。

- The slide also states that LED uses local attention over up to 1024 tokens and global attention for selected positions such as the first `<s>` token.
- 幻灯片还指出，LED 使用局部 attention 处理最多 1024 token 的窗口，并对诸如第一个 `<s>` token 这样的特定位置施加 global attention。

- In `3-longformer-simple.ipynb`, the contrast is shown by comparing truncated BERT-style processing with Longformer-style long-document handling.
- 在 `3-longformer-simple.ipynb` 中，这一点通过对比被截断的 BERT-style 处理和 Longformer-style 长文档处理来展示。

- In `4-longformer-summarization.ipynb`, `allenai/led-base-16384` is used for long-document summarization.
- 在 `4-longformer-summarization.ipynb` 中，`allenai/led-base-16384` 被用于长文档 summarization。

## 12. Special Cases of Summarisation / 摘要任务的特殊情形

- The lecture identifies three especially important special cases: multi-document summarization, structure-controlled summarization, and length-controlled summarization.
- 课件重点指出了三类特殊情形：multi-document summarization、structure-controlled summarization 和 length-controlled summarization。

- Multi-document summarization must combine information from several documents rather than one source.
- multi-document summarization 需要把多个 document 的信息整合起来，而不是只处理单一 source。

- The lecture states that such systems must avoid repetition while ensuring broad representation of the source set.
- 课件指出，这类系统必须同时避免重复，并保证多个 source 的信息得到充分代表。

- Structure-controlled summarization is motivated by domains such as law, where summaries follow a fixed schema.
- structure-controlled summarization 的动机来自法律等领域，因为这些 summary 往往遵循固定 schema。

- Legal summarization is therefore presented as a case where summary structure matters as much as summary content.
- 因此，legal summarization 被视为一种 summary structure 与 summary content 同样重要的场景。

- Length-controlled summarization aims to generate summaries of exactly a given length.
- length-controlled summarization 的目标则是生成长度恰好符合要求的 summary。

- The lecture explains this using the `</s>` token and a remaining length budget `l_t`, together with a length-aware attention mechanism.
- 课件通过 `</s>` token、remaining length budget `l_t`，以及 length-aware attention mechanism 来解释这一点。

## 13. Early Question-Answering Formulations / 早期问答形式

- The QA section begins by revisiting early generation-based and template-based question answering.
- QA 部分首先回顾了早期 generation-based 和 template-based question answering。

- The lecture mentions question type classification and frame extraction as early pipeline components.
- 课件提到了 question type classification 和 frame extraction 作为早期 pipeline component。

- These systems were mainly designed for factoid questions such as who, what, when, how, and why.
- 这些系统主要是为 factoid question 设计的，例如 who、what、when、how、why。

- Frame-like patterns such as `X is the Y of Z` are used to map questions to answer structures.
- 类似 `X is the Y of Z` 这样的 frame pattern 会被用来把问题映射到答案结构上。

- The lecture links these older QA pipelines to Week 7 tools such as NER and POS tagging.
- 课件把这些早期 QA pipeline 与 Week 7 中的 NER 和 POS tagging 工具联系起来理解。

## 14. Modern Neural QA / 现代神经问答

- The lecture groups modern neural QA into three broad areas: encoder-based QA, retrieval-augmented generation, and RL-based alignment.
- 课件把现代 neural QA 概括为三大方向：encoder-based QA、retrieval-augmented generation，以及 RL-based alignment。

- Document question-answering can be framed as an extractive task that extracts a phrase from a document.
- document question-answering 可以被表述为一个 extractive task，即从 document 中抽取一个 phrase 作为答案。

- The lecture says this can reuse ideas from POS tagging and NER, which is why BERT-style QA can be viewed as a span-extraction setup.
- 课件指出，这类方法可以复用 POS tagging 和 NER 的思路，因此 BERT-style QA 可以被看成一种 span-extraction setup。

- Decoder models can also be instruction-fine-tuned on question-answer pairs.
- decoder model 也可以在 question-answer pair 上进行 instruction fine-tuning。

- However, the lecture immediately warns that decoder-only or generative QA systems face hallucination risk.
- 但课件也紧接着提醒：decoder-only 或 generative QA system 会面临 hallucination 风险。

- The lecture also remarks that modern QA can subsume many other NLP tasks when phrased as questions, such as asking for sentiment or labels.
- 课件还指出，现代 QA 实际上可以吸收很多其他 NLP task，只要把它们改写成 question 的形式，例如询问 sentiment 或其他 label。

## 15. Retrieval-Augmented Generation (RAG) / 检索增强生成

- The lecture contrasts black-box zero-shot or in-context LLM behaviour with retrieval-based grounding.
- 课件把 black-box 的 zero-shot 或 in-context LLM 行为，与 retrieval-based grounding 做了对比。

- RAG first retrieves a set of relevant documents and then uses them to generate the response.
- RAG 会先检索一组相关 document，然后再利用这些 document 生成 response。

- The mathematical notation in the lecture uses `x` for the question, `y` for the response, and `z` for the top-`k` retrieved documents relevant to `x`.
- 课件中的数学记号使用 `x` 表示 question，`y` 表示 response，`z` 表示与 `x` 相关的 top-`k` retrieved document。

- The main motivation given for RAG is mitigating hallucination by grounding the answer in retrieved evidence.
- 课件给出 RAG 的主要动机是通过 grounding 到被检索出的 evidence 上来减轻 hallucination。

## 16. Why QA Is Not Fully Deterministic / 为什么 QA 不是完全确定性的

- The lecture argues that QA is not a fully deterministic task because many prompts admit multiple acceptable answers.
- 课件强调，QA 并不是一个完全 deterministic 的任务，因为很多 prompt 对应多个都可以接受的答案。

- Some answers are judged partly by style, helpfulness, or behaviour rather than strict factual correctness alone.
- 有些答案不仅要看 factual correctness，还要看 style、helpfulness 和行为是否符合预期。

- It is also impractical to build exhaustive supervised datasets for all possible questions.
- 此外，为所有可能问题建立 exhaustive 的 supervised dataset 也是不现实的。

- This motivates the transition from plain supervised learning to alignment and preference-based learning.
- 这就推动了从普通 supervised learning 向 alignment 和 preference-based learning 的过渡。

## 17. LLM Alignment, RLHF, and DPO / LLM 对齐、RLHF 与 DPO

- LLM alignment is defined as aligning model behaviour with human values and user expectations in a socially beneficial way.
- LLM alignment 被定义为：以对用户、开发者和社会更有益的方式，让模型行为与 human value 和 user expectation 对齐。

- The lecture identifies RL as the dominant paradigm for alignment.
- 课件把 RL 视为 alignment 的主导范式。

- The big-picture slide shows supervised fine-tuning, reinforcement learning, preference datasets, and programmatic verifiers as the main components of post-training.
- big-picture 幻灯片把 supervised fine-tuning、reinforcement learning、preference dataset 和 programmatic verifier 视为 post-training 的主要组成部分。

- RLHF starts with a policy model and then collects preference information over model responses.
- RLHF 会先从一个 policy model 出发，然后收集模型 response 的 preference information。

- A reward model is trained to map prompt-response pairs to scalar rewards.
- reward model 会被训练成把 prompt-response pair 映射到 scalar reward。

- The policy model is then optimised using those rewards, with PPO shown in the lecture as the representative optimisation method.
- 随后，policy model 会利用这些 reward 进行优化，而课件用 PPO 作为代表性的优化方法。

- The lecture asks why supervised fine-tuning alone is insufficient here, and the answer is that preference data gives relative rankings rather than a single gold output.
- 课件专门追问“为什么仅靠 supervised fine-tuning 不够”，答案是：preference data 往往给的是相对排序，而不是单个 gold output。

- The lecture also emphasises that RLHF usually includes a constraint that the aligned model should not drift too far from the base model.
- 课件还强调，RLHF 通常会加入一个约束，防止对齐后的模型偏离 base model 太远。

- For programmatically verifiable tasks such as mathematics or code compilation, rewards can come from explicit verifiers.
- 对于数学题或代码编译这种 programmatically verifiable task，reward 可以来自显式 verifier。

- For non-programmatically verifiable tasks, reward modeling and preference learning become necessary.
- 对于不能程序化验证的任务，则必须依赖 reward modeling 和 preference learning。

- DPO is introduced as a method that bypasses the explicit learning of a reward model.
- DPO 被介绍为一种绕过显式 reward model 学习的办法。

- The lecture also stresses that RL-based alignment is relevant not only to model producers but also to model consumer companies such as empathetic conversational systems, cybersecurity firms, and localisation-focused products.
- 课件还强调，RL-based alignment 不只是 model producer 的问题，对 empathetic conversational system、cybersecurity 公司和 localisation 产品等 consumer company 也同样重要。

- In `5-trl-summarization.ipynb`, these post-training ideas are connected to practice through `trl`, the `trl-lib/tldr` dataset, and `Qwen/Qwen2-0.5B-Instruct`.
- 在 `5-trl-summarization.ipynb` 中，这些 post-training 思路通过 `trl`、`trl-lib/tldr` dataset 以及 `Qwen/Qwen2-0.5B-Instruct` 被连接到了实际代码层面。

## 18. Demo and Startup Exercise / Demo 与课堂练习

- The notebook bundle for this week demonstrates TextRank, BART summarization, Longformer for long inputs, LED summarization, and TRL-based summarization training.
- 本周 notebook bundle 分别演示了 TextRank、BART summarization、Longformer 长输入处理、LED summarization，以及基于 TRL 的 summarization training。

- The final lecture slides also include a group exercise asking students to analyse startup websites from an NLP-system-design perspective.
- 课件最后还安排了一个 group exercise，要求学生从 NLP system design 的角度分析 startup 网站。

- The discussion questions focus on underlying NLP tasks, datasets for fine-tuning, throughput and ethics, offline or online evaluation, and deployment challenges.
- 这些讨论问题主要围绕 underlying NLP task、fine-tuning dataset、throughput 与 ethics、offline/online evaluation，以及 deployment challenge 展开。

## 19. High-Frequency Exam Points / 高频考点总结

- You must be able to distinguish extractive summarization from abstractive summarization in terms of output form and task formulation.
- 你必须能够从输出形式和任务表述两个角度区分 extractive summarization 与 abstractive summarization。

- You should know why TextRank is unsupervised and why it can be explained as graph ranking over sentences.
- 你需要知道为什么 TextRank 是 unsupervised 方法，以及为什么它可以被解释成 sentence graph 上的 ranking 问题。

- You should be able to explain pointer-generator networks as a soft choice between copying from the source and generating from the vocabulary.
- 你应该能够解释 pointer-generator network，即它是在 source copying 与 vocabulary generation 之间做 soft choice。

- You should know why BART is suitable for summarization and how denoising pretraining differs from plain next-token training.
- 你应该知道为什么 BART 适合 summarization，以及 denoising pretraining 与普通 next-token training 有什么不同。

- You should know why summarization needs long-document models and how Longformer reduces attention cost through sliding-window attention plus global attention.
- 你应该知道为什么 summarization 需要 long-document model，以及 Longformer 如何通过 sliding-window attention 加 global attention 来降低 attention 成本。

- You should be able to name special cases such as multi-document summarization, legal summarization, and length-controlled summarization, and state what makes them difficult.
- 你应该能够列出 multi-document summarization、legal summarization、length-controlled summarization 等特殊情形，并说明它们各自的难点。

- You should know the distinction between extractive BERT-style QA and generative decoder-style QA.
- 你应该清楚 extractive 的 BERT-style QA 与 generative 的 decoder-style QA 之间的区别。

- You should be able to explain the motivation and core pipeline of RAG.
- 你应该能够解释 RAG 的动机和核心 pipeline。

- You should know why QA is not fully deterministic and why preference-based alignment is needed.
- 你应该知道为什么 QA 不是 fully deterministic task，以及为什么需要 preference-based alignment。

- You should be able to compare SFT, RLHF, reward modeling, PPO, and DPO at a high level.
- 你应该能够在高层面比较 SFT、RLHF、reward modeling、PPO 和 DPO。

## 20. Standard Answer Templates / 标准答题模板

- Extractive summarization selects original sentences from the document, whereas abstractive summarization generates new text that may not appear verbatim in the source.
- extractive summarization 直接选择原文句子，而 abstractive summarization 会生成原文中未必逐字出现的新文本。

- TextRank is an unsupervised graph-based summarization algorithm in which sentences are nodes, sentence similarities are edges, and iterative ranking determines sentence salience.
- TextRank 是一种 unsupervised 的 graph-based summarization algorithm，其中 sentence 是 node，sentence similarity 是 edge，而迭代式 ranking 用于决定 sentence salience。

- Pointer-generator networks combine a pointer mechanism for copying source words with a generator mechanism for producing words from the vocabulary, and `p_gen` controls the balance between the two.
- pointer-generator network 把用于复制 source word 的 pointer mechanism 与用于从 vocabulary 生成词的 generator mechanism 结合起来，而 `p_gen` 用来控制二者之间的平衡。

- BART is an encoder-decoder Transformer pretrained with denoising, so it is well suited to summarization because it learns to reconstruct coherent text from corrupted input.
- BART 是一个通过 denoising 进行预训练的 encoder-decoder Transformer，因此它很适合 summarization，因为它学会了从被破坏的输入中恢复连贯文本。

- Longformer reduces the cost of full self-attention by restricting most attention to a local window while preserving selected global attention positions for important tokens.
- Longformer 通过把大多数 attention 限制在局部窗口内、同时保留对关键 token 的 selected global attention，来降低 full self-attention 的成本。

- RAG mitigates hallucination by retrieving relevant documents first and then conditioning generation on those retrieved documents.
- RAG 先检索相关 document，再基于这些 retrieved document 进行生成，因此能够缓解 hallucination。

- RLHF uses preference data to train a reward model and then optimises the policy model with reinforcement learning, whereas DPO bypasses explicit reward-model training and directly optimises preferences.
- RLHF 使用 preference data 训练 reward model，再用强化学习优化 policy model；而 DPO 则绕过显式 reward-model training，直接对 preference 进行优化。

- The key reason supervised fine-tuning alone is insufficient for alignment is that many tasks have multiple acceptable responses, and preference data often gives relative quality judgments rather than a single gold answer.
- alignment 中仅靠 supervised fine-tuning 不足的关键原因是：许多任务存在多个可接受答案，而 preference data 给出的往往是相对质量判断，而不是单一 gold answer。
