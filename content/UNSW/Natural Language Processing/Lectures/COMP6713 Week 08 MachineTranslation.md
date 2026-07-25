---
tags:
  - UNSW
  - UNSW/COMP6713
  - Topic/NLP
  - Type/Lecture
---

## 1. Announcements and Weekly Roadmap / 课程提醒与本周路线图

- The lecture opens with Warren Weaver’s classic quote about translation as decoding.
- 课件开头引用了 Warren Weaver 的经典观点，把翻译比作 decoding。

- The announcement slide explains the final exam format in concrete terms.
- announcement 页用很具体的方式说明了 final exam 的形式。

- The exam is described as a centrally invigilated BYOD Inspera exam.
- 课件说明期末考试是 centrally invigilated 的 BYOD Inspera exam。

- The slide says the exam includes multiple-choice, short-answer, and long-answer questions.
- 课件写明考试包括 multiple-choice、short-answer 和 long-answer 三种题型。

- It also warns that long-answer questions will receive negative marking for incorrect detail.
- 它还特别提醒 long-answer 会对错误细节进行 negative marking。

- The roadmap for the week includes introduction and terminology, MT evaluation, statistical MT, transformer-based MT, decoding, LLM-based MT, and special cases.
- 本周路线图包括 introduction 和 terminology、MT evaluation、statistical MT、transformer-based MT、decoding、LLM-based MT 以及 special cases。

---

## 2. What Machine Translation Tries to Do / 机器翻译到底要做什么

- Machine translation is defined as translating text from a source language to a target language while preserving meaning.
- machine translation 的定义是：把 source language 的文本翻译成 target language，并尽量保持 meaning。

- The lecture explicitly frames MT as a sequence-to-sequence task.
- 课件明确把 MT 视为 sequence-to-sequence task。

- It revisits the motivation for Transformer from Weeks 3 and 4, because MT was one of the landmark applications for encoder-decoder models.
- 课件回顾了 Weeks 3 和 4 中 Transformer 的动机，因为 MT 正是 encoder-decoder 模型的标志性应用之一。

- The lecture emphasizes that translation must deal with word correspondence, reordering, and cases where one source word maps to multiple target words or none.
- 课件强调翻译必须同时处理词对齐、词序重排，以及一个 source word 对应多个 target words 或根本没有显式对应项的情况。

- The examples from Italian, Irish, and Marathi show that different language pairs require different amounts of reordering.
- 课件用 Italian、Irish 和 Marathi 的例子说明，不同语言对对重排的需求并不相同。

- MT therefore requires both lexical translation knowledge and target-language fluency constraints.
- 因此 MT 同时需要 lexical translation knowledge 和 target-language fluency constraints。

---

## 3. Challenges and Motivation / 挑战与动机

- The lecture shows language families to remind students that related languages may share some properties but still diverge in important ways.
- 课件展示了 language families，提醒学生相关语言可能共享某些性质，但仍会在重要方面出现分歧。

- It highlights promotional divergence, lexical divergence, and pragmatic differences as translation challenges.
- 课件特别强调 promotional divergence、lexical divergence 和 pragmatic differences 这些翻译难点。

- Lexical divergence means one language may carve up semantic space differently from another.
- lexical divergence 指的是不同语言对语义空间的划分方式可能不同。

- Pragmatic meaning can also make literal translation misleading.
- pragmatic meaning 也会使得字面对译变得具有误导性。

- The fictional-language exercise is used to help students infer the ideas of alignment and target-side ordering from parallel examples.
- fictional language 练习被用来帮助学生从 parallel examples 中直观理解 alignment 和 target-side ordering。

- The lecture then motivates MT through historical systems such as SYSTRAN and modern systems such as Google and Bing.
- 课件随后通过历史系统 SYSTRAN 和现代系统 Google、Bing 来说明 MT 的实际价值。

- It also mentions zero-shot prompting as a modern path to MT.
- 课件还提到了 zero-shot prompting 作为现代 MT 的一种路径。

---

## 4. MT Evaluation: Why It Is Hard / MT 评测为什么难

- MT evaluation compares candidate translations with reference translations.
- MT evaluation 的核心是把 candidate translation 和 reference translation 进行比较。

- The lecture stresses that MT metrics belong to the broader class of NLG evaluation metrics.
- 课件强调 MT metrics 本质上属于更广义的 NLG evaluation metrics。

- Good evaluation should reflect both content correctness and language quality.
- 好的评测应该同时反映内容是否正确，以及语言本身是否自然。

- Automatic metrics are convenient, but the lecture repeatedly notes that they have known limitations.
- automatic metrics 很方便，但课件反复提醒它们存在公认的局限。

---

## 5. BLEU / BLEU 指标

- BLEU stands for Bilingual Evaluation Understudy.
- BLEU 是 Bilingual Evaluation Understudy 的缩写。

- BLEU is presented as an automatic metric for MT evaluation.
- BLEU 被介绍为一种自动 MT 评测指标。

- The lecture begins by asking what proportion of candidate words occur in the reference, which motivates precision.
- 课件先追问 candidate 中有多少词出现在 reference 里，由此引出 precision。

- It then introduces clipped precision to avoid giving unlimited credit for repeated words.
- 接着课件引入 clipped precision，避免对重复堆砌的词给予无限奖励。

- The lecture then asks whether precision alone is enough and uses this to motivate recall and brevity concerns.
- 然后课件追问 precision 是否足够，并借此引出 recall 和 brevity 的问题。

- BLEU handles recall indirectly through the brevity penalty.
- BLEU 会通过 brevity penalty 的方式间接处理 recall 问题。

- The formula combines clipped n-gram precisions across multiple `n` values.
- BLEU 公式会把多个 `n` 的 clipped n-gram precision 结合起来。

- The lecture notes that BLEU ranges between 0 and 1, with higher values indicating better overlap-based quality.
- 课件指出 BLEU 取值在 0 到 1 之间，数值越高通常表示 overlap-based 质量越好。

- The BLEU slides are important because they build the metric from intuitive sentence comparisons rather than only presenting the final formula.
- BLEU 这一部分的重要性在于，它是从直观的句对比较逐步推导到最终公式，而不是只给结论。

- The `1-metrics.ipynb` notebook demonstrates BLEU computation with `nltk.translate.bleu_score`.
- `1-metrics.ipynb` 演示了如何用 `nltk.translate.bleu_score` 计算 BLEU。

---

## 6. Other MT Metrics / 其他 MT 指标

- The lecture introduces ROUGE as another family of overlap-based metrics.
- 课件把 ROUGE 介绍为另一类 overlap-based metrics。

- It mentions ROUGE-N, ROUGE-L, weighted ROUGE-L, and ROUGE-S.
- 它提到了 ROUGE-N、ROUGE-L、weighted ROUGE-L 和 ROUGE-S。

- ROUGE is especially well known in summarization, but the lecture mentions it as a related text-generation metric.
- ROUGE 在 summarization 中尤其常见，但课件把它作为相关 text-generation metric 一并介绍。

- METEOR is introduced as a metric based on alignment, harmonic mean of precision and recall, and matching beyond exact word identity.
- METEOR 被介绍为一种基于 alignment、precision/recall 调和平均，以及超越精确词匹配的指标。

- The lecture highlights that METEOR can incorporate stemming and synonyms.
- 课件强调 METEOR 可以考虑 stemming 和 synonyms。

- Manual evaluation strategies are also discussed through adequacy and fluency scoring.
- 课件还讨论了 adequacy 和 fluency 打分这样的 manual evaluation strategies。

- Adequacy asks whether the meaning is translated correctly.
- adequacy 关注的是 meaning 是否被正确翻译出来。

- Fluency asks whether the output is grammatically well formed and natural.
- fluency 关注的是输出是否语法正确、语言自然。

- The lecture explicitly warns that automated metrics such as BLEU often correlate poorly with human judgments.
- 课件明确提醒，像 BLEU 这样的自动指标往往和 human judgments 的相关性有限。

- BLEURT is presented as a learned metric built with BERT and fine-tuning.
- BLEURT 被介绍为一种基于 BERT 并经过 fine-tuning 的 learned metric。

- The lecture explains BLEURT in two stages: first synthetic regression data based on perturbations and BLEU-like scores, then fine-tuning on human ratings.
- 课件把 BLEURT 分成两个阶段：先基于 perturbations 和 BLEU-like score 构造 synthetic regression data，再在 human ratings 上 fine-tune。

- The `1-metrics.ipynb` notebook also computes ROUGE and BLEURT in addition to BLEU.
- `1-metrics.ipynb` 除了 BLEU 之外，也演示了 ROUGE 和 BLEURT 的计算。

---

## 7. Statistical Machine Translation / 统计机器翻译

- After evaluation, the lecture moves to statistical MT.
- 在讲完评测之后，课件转入 statistical MT。

- It mentions classic parallel datasets such as EuroParl, the UN parallel corpus, and OpenSubtitles.
- 课件提到了 EuroParl、UN parallel corpus 和 OpenSubtitles 等经典 parallel datasets。

- The noisy-channel model is introduced as a classical way of thinking about translation.
- noisy-channel model 被引入作为理解翻译的经典框架。

- An alignment model is needed to connect source and target words.
- translation system 需要 alignment model 来连接 source 和 target 的词。

- A target-side language model `P(t)` is needed to prefer fluent target sentences.
- 还需要 target-side language model `P(t)` 来偏好 fluent 的目标语言句子。

- The lecture explicitly ties `P(t)` back to perplexity and fluency.
- 课件明确把 `P(t)` 和 perplexity、fluency 重新联系起来。

- IBM Models are listed as canonical statistical MT models.
- IBM Models 被列为经典的 statistical MT 模型。

- The expectation-maximization algorithm is introduced because translation probabilities and alignments depend on each other.
- expectation-maximization algorithm 被引入，是因为 translation probabilities 和 alignments 互相依赖。

- The lecture explains EM as alternating between assigning probabilities to missing data in the E step and updating parameters in the M step.
- 课件把 EM 解释为在 E step 给 missing data 分配概率，再在 M step 更新参数的交替过程。

- The MT example specifically mentions initializing the word translation function, computing alignments, and repeatedly updating the translation probabilities.
- 课件中的 MT 例子特别提到初始化 word translation function、计算 alignments，并反复更新 translation probabilities。

- Moses appears in the topic outline as the classic SMT toolkit ecosystem connected to this statistical tradition.
- Moses 出现在 topic outline 中，代表了和这套 statistical MT 传统紧密相关的经典 SMT toolkit 生态。

---

## 8. Transformer-Based MT / 基于 Transformer 的机器翻译

- The lecture next returns to Transformer-based MT.
- 接着课件回到 Transformer-based MT。

- It reminds students that Transformer is an encoder-decoder seq2seq architecture.
- 课件提醒学生，Transformer 是 encoder-decoder 的 seq2seq architecture。

- The decoder uses masked self-attention and cross-attention over encoder outputs.
- decoder 会同时使用 masked self-attention 和对 encoder output 的 cross-attention。

- The lecture revisits teacher forcing during training.
- 课件重新回顾了 training 时的 teacher forcing。

- Teacher forcing means that during training, the decoder is fed the gold previous output tokens rather than its own sampled predictions.
- teacher forcing 的意思是：训练时 decoder 看到的是 gold previous output tokens，而不是自己刚刚采样出来的预测。

- The lecture includes an OpenNMT side note as a practical open-source NMT toolkit.
- 课件还专门插入了 OpenNMT 这个 practical open-source NMT toolkit 的 side note。

- The `3-opennmt.ipynb` notebook walks through a practical OpenNMT-style pipeline including corpus download, filtering, subword vocabulary training, and later MT training preparation.
- `3-opennmt.ipynb` 演示了一个 OpenNMT 风格的实践流程，包括语料下载、过滤、subword vocabulary 训练，以及后续 MT training preparation。

---

## 9. Transformer Decoding / Transformer 解码

- During inference, a Transformer MT system generates the target sequence autoregressively.
- 在 inference 阶段，Transformer MT system 会以 autoregressive 的方式逐词生成目标序列。

- The lecture defines decoding as producing an output sequence from hidden states.
- 课件把 decoding 定义为：根据 hidden states 生成 output sequence。

- It lists two desirable properties for decoding: output diversity and coherence with respect to the input.
- 课件列出 decoding 的两个 desirable properties：输出多样性，以及相对输入的 coherence。

- Greedy decoding picks the highest-probability word at each step.
- greedy decoding 会在每一步选择概率最高的词。

- Its advantages are determinism and simplicity, but it lacks diversity and can get stuck in bad choices.
- 它的优点是确定性和简单性，但缺点是缺乏多样性，而且一旦早期选错就会一路错下去。

- Random sampling draws a word from the full output distribution.
- random sampling 会从完整输出分布中采样一个词。

- Sampling introduces diversity but can generate strange outputs.
- sampling 会带来多样性，但也可能生成怪异输出。

- Top-k sampling restricts sampling to the top-k words.
- top-k sampling 会把采样范围限制在 top-k 个词之内。

- Top-k is more controlled than unrestricted sampling, and `k = 1` reduces to greedy decoding.
- top-k 比完全随机采样更可控，而 `k = 1` 时就退化为 greedy decoding。

- The lecture also mentions top-p sampling and temperature sampling as other ways to reshape or restrict the distribution.
- 课件还提到 top-p sampling 和 temperature sampling，作为进一步重塑或截断分布的方法。

- Beam search keeps multiple partial sequences and returns the best completed sequence among them.
- beam search 会同时保留多条 partial sequence，并在完成后返回其中最优的一条。

- The lecture notes that typical beam widths for MT are around 5 to 10.
- 课件说明 MT 中常见的 beam width 大约是 5 到 10。

- Beam search is explicitly linked back to the historical notion of decoding, including a reminder of Viterbi-style ideas.
- beam search 被明确和历史上的 decoding 概念联系起来，课件还回顾了 Viterbi-style 的思想。

- The `2-decoding-alternatives.ipynb` notebook compares greedy decoding, top-k sampling, and other generation strategies on a translation model.
- `2-decoding-alternatives.ipynb` 演示了在 translation model 上比较 greedy decoding、top-k sampling 等 generation strategies。

---

## 10. Speculative Decoding / 推测式解码

- Speculative decoding is introduced as an optimization for reducing inference latency.
- speculative decoding 被介绍为一种降低 inference latency 的优化方法。

- The lecture frames the problem as reducing decoding time in an LLM-based system.
- 课件把问题表述为：如何降低 LLM-based system 的 decoding 时间。

- The intuition is to let a faster draft model propose several tokens while a stronger slower model verifies them.
- 它的直觉是：让更快的 draft model 先提出若干 token，再由更强但更慢的 model 去验证。

- The lecture explains this with a data-scientist versus principal-data-scientist analogy.
- 课件用 “data scientist 与 principal data scientist” 的类比来帮助理解这个流程。

- A speculation window defines how many draft tokens are proposed before verification.
- speculation window 表示在一次验证前要先提出多少个 draft tokens。

- The best case occurs when the strong model accepts many draft tokens at once.
- best case 是强模型一次性接受了很多 draft tokens。

- The point of speculative decoding is not to change the model’s task, but to reduce latency for the same task.
- speculative decoding 的重点不是改变模型任务，而是在同一任务上减少 latency。

- The lecture cites Leviathan, Kalman, and Matias (2023) as the reference.
- 课件引用 Leviathan、Kalman 和 Matias (2023) 作为核心参考。

---

## 11. LLM-Based and Multilingual MT / 基于 LLM 的多语言机器翻译

- The lecture then moves from classical NMT to LLM-based MT.
- 课件随后从 classical NMT 过渡到 LLM-based MT。

- Multilingual neural machine translation is defined as translating among multiple source and target languages using a shared model.
- multilingual neural machine translation 被定义为使用共享模型在多个 source 和 target 语言之间翻译。

- Such systems are typically trained on parallel corpora for many language pairs and are often English-centric.
- 这类系统通常在多语言对的 parallel corpora 上训练，并且很多时候是 English-centric 的。

- The lecture names continued pre-training and instruction tuning as typical techniques.
- 课件点名 continued pre-training 和 instruction tuning 作为常见技术。

- One way to specify the target language is to prepend a special token.
- 指定目标语言的一种方式是在输入前面加 special token。

- Another way is instruction tuning, which turns tasks into an instruction-plus-input to output format.
- 另一种方式是 instruction tuning，也就是把任务统一改写成 instruction + input -> output 的格式。

- The lecture asks students to imagine what instruction tuning would look like specifically for MT.
- 课件还专门要求学生思考 instruction tuning 在 MT 里到底应该长什么样。

- Stanford Alpaca is mentioned as an instruction-following model example.
- Stanford Alpaca 被提及为 instruction-following model 的一个例子。

- TowerLLM is introduced as an open multilingual large language model for translation-related tasks.
- TowerLLM 被介绍为一个 open multilingual large language model，专门面向 translation-related tasks。

- The lecture stresses that one need not always pretrain from scratch and can instead continue training on appropriate multilingual data.
- 课件强调，不一定要从头 pretrain，也可以在合适的 multilingual data 上继续训练。

- The `0-zero-shot.ipynb` notebook shows translation by prompting a pretrained seq2seq model directly.
- `0-zero-shot.ipynb` 演示了如何通过 prompt 直接让预训练 seq2seq model 完成翻译。

- The `4-llm-based-mt.ipynb` notebook demonstrates many-to-many translation with explicit language tokens.
- `4-llm-based-mt.ipynb` 演示了使用显式 language tokens 的 many-to-many translation。

- The `5-simple-instruction-tuning.ipynb` notebook shows a simple instruction-tuning workflow for translation using a seq2seq model and a translation dataset.
- `5-simple-instruction-tuning.ipynb` 演示了使用 seq2seq 模型和翻译数据集进行简单 instruction tuning 的流程。

---

## 12. Special Cases of MT / 机器翻译的特殊情况

- The lecture next turns to low-resource and special-case MT settings.
- 接下来课件转向 low-resource 和 special-case MT 场景。

- Pivot-based MT is introduced for cases where parallel data between the source and target language is unavailable.
- pivot-based MT 被引入，用于 source 和 target 语言之间缺少 parallel data 的情况。

- In pivot-based MT, translation is done through an intermediate pivot language such as English.
- 在 pivot-based MT 中，翻译会先经过一个中间的 pivot language，例如 English。

- The lecture notes that pivot-language choice may depend on language similarity.
- 课件指出，pivot language 的选择可能会受到语言相似性的影响。

- Unsupervised MT is introduced for cases where parallel data is limited but monolingual corpora exist.
- unsupervised MT 被介绍为：parallel data 很少，但 monolingual corpora 可用时的一种方法。

- The lecture emphasizes learning a common embedding space for the two languages.
- 课件强调要为两种语言学习 common embedding space。

- Two alternating steps are highlighted: denoising and back-translation.
- 课件特别强调两个交替步骤：denoising 和 back-translation。

- The note on the slides says the diagram uses pre-Transformer encoder-decoders, but the thematic ideas still carry over.
- 课件备注说明图中使用的是 pre-Transformer encoder-decoder，但主题思想仍然延续到了现代系统中。

- Post-editing is defined as humans correcting MT output.
- post-editing 被定义为由人类来修正 MT 输出。

- Automatic post-editing is then presented as learning to correct MT output automatically.
- 随后课件引入 automatic post-editing，也就是让模型自动修正 MT 输出。

- The APE diagram uses source, raw target, and post-edited target as part of the architecture.
- APE 那张图把 source、raw target 和 post-edited target 一起放进架构中。

---

## 13. High-Frequency Exam Points / 高频考点总结

- Machine translation is a sequence-to-sequence task that must preserve meaning while producing fluent output in the target language.
- machine translation 是一个 sequence-to-sequence task，既要保持 meaning，又要在目标语言中生成 fluent output。

- MT requires lexical translation knowledge, word alignment, and target-side ordering.
- MT 需要 lexical translation knowledge、word alignment 和 target-side ordering。

- BLEU is based on clipped n-gram precision plus brevity penalty.
- BLEU 基于 clipped n-gram precision 和 brevity penalty。

- BLEU has known limitations and should not be treated as a perfect proxy for human judgment.
- BLEU 有公认局限，不能被视为 human judgment 的完美替代。

- ROUGE, METEOR, BLEURT, and human evaluation provide alternative or complementary evaluation views.
- ROUGE、METEOR、BLEURT 和 human evaluation 提供了替代或补充性的评测视角。

- Statistical MT uses alignment models, target-language models, IBM Models, and EM-style learning.
- statistical MT 使用 alignment models、target-language models、IBM Models 和 EM-style learning。

- Transformer-based MT uses an encoder-decoder architecture and autoregressive decoding at inference time.
- Transformer-based MT 使用 encoder-decoder architecture，并在 inference 时进行 autoregressive decoding。

- Greedy decoding is deterministic, sampling adds diversity, top-k/top-p/temperature control randomness, and beam search keeps multiple candidate sequences.
- greedy decoding 是确定性的，sampling 会增加多样性，top-k/top-p/temperature 用来控制随机性，而 beam search 会保留多条候选序列。

- Speculative decoding reduces latency by combining a fast draft model with a slower verification model.
- speculative decoding 通过结合快速 draft model 和较慢的 verification model 来降低 latency。

- Multilingual and LLM-based MT often rely on special language tokens, instruction tuning, or continual pretraining.
- multilingual 和 LLM-based MT 通常依赖 language tokens、instruction tuning 或 continual pretraining。

- Important MT special cases include pivot-based MT, unsupervised MT, and automatic post-editing.
- MT 的重要 special cases 包括 pivot-based MT、unsupervised MT 和 automatic post-editing。

---

## 14. Model Answers to Likely Exam Questions / 常见考题标准答案

### Q1. Why is machine translation a sequence-to-sequence task?

- Machine translation is a sequence-to-sequence task because it maps an input sequence of source-language tokens to an output sequence of target-language tokens.
- machine translation 是 sequence-to-sequence task，因为它把 source-language token 序列映射成 target-language token 序列。

### Q2. Why is translation harder than word substitution?

- Translation is harder than word substitution because languages differ in word order, lexical granularity, alignment structure, and pragmatic meaning.
- 翻译比逐词替换更难，因为语言之间在词序、词汇粒度、alignment 结构和 pragmatic meaning 上都存在差异。

### Q3. What does BLEU measure?

- BLEU measures n-gram overlap quality between a candidate translation and reference translation using clipped precision and brevity penalty.
- BLEU 衡量的是 candidate translation 和 reference translation 之间的 n-gram overlap 质量，核心由 clipped precision 和 brevity penalty 构成。

### Q4. Why do we need clipped precision in BLEU?

- We need clipped precision so that repeating the same word many times does not receive unfairly high credit.
- 我们需要 clipped precision，是为了避免通过重复堆砌同一个词来获得不公平的高分。

### Q5. Why is BLEU not enough on its own?

- BLEU is not enough on its own because it may miss meaning adequacy, fluency, paraphrastic variation, and other qualities better captured by human judgment or learned metrics.
- BLEU 单独使用并不够，因为它可能忽略 meaning adequacy、fluency、释义变化等更适合由 human judgment 或 learned metric 捕捉的质量。

### Q6. What is the role of a target-side language model in statistical MT?

- The target-side language model assigns higher probability to fluent target sentences and helps choose better translations among alternatives.
- 在 statistical MT 中，target-side language model 会给 fluent 的目标语言句子更高概率，从而帮助系统在多个翻译候选中做出更好的选择。

### Q7. Why is EM used in classical MT?

- EM is used because alignments are latent variables and translation probabilities depend on those alignments, so the model alternates between estimating them and updating parameters.
- classical MT 里使用 EM，是因为 alignments 是 latent variables，而 translation probabilities 又依赖这些 alignments，所以模型需要在估计隐变量和更新参数之间交替进行。

### Q8. What is teacher forcing in neural MT?

- Teacher forcing means that during training the decoder sees the gold previous output tokens instead of its own predicted tokens.
- teacher forcing 指的是训练时 decoder 看到的是 gold previous output tokens，而不是自己预测出来的 token。

### Q9. What is the difference between greedy decoding and beam search?

- Greedy decoding keeps only the single best next token at each step, whereas beam search keeps multiple partial hypotheses and chooses the best completed sequence later.
- greedy decoding 每一步只保留一个最优 next token，而 beam search 会同时保留多条 partial hypotheses，并在之后选择最优完整序列。

### Q10. What problem does speculative decoding solve?

- Speculative decoding solves the problem of slow inference latency by allowing a fast model to draft tokens and a stronger model to verify them efficiently.
- speculative decoding 要解决的是 inference latency 过高的问题，它通过让快模型先起草 token、强模型再验证，来提高效率。

### Q11. How can a multilingual MT model know the target language?

- A multilingual MT model can know the target language through a special language token or through an instruction-style input format.
- multilingual MT model 可以通过 special language token，或者 instruction-style 的输入格式来知道目标语言。

### Q12. What is pivot-based MT?

- Pivot-based MT translates from source to target through an intermediate pivot language when direct parallel data is unavailable.
- pivot-based MT 指的是在 source 和 target 没有直接 parallel data 时，先经过一个中间 pivot language 再完成翻译。

### Q13. What is unsupervised MT according to the lecture?

- Unsupervised MT is MT in which direct parallel corpora are limited or absent, and the model relies on monolingual data plus steps such as denoising and back-translation.
- 按课件的定义，unsupervised MT 指的是 direct parallel corpora 很少甚至没有时，系统主要依赖 monolingual data，并结合 denoising 和 back-translation 等步骤来学习翻译。

### Q14. What is automatic post-editing?

- Automatic post-editing is the task of automatically correcting the output of an MT system, often using the source sentence together with the raw MT output.
- automatic post-editing 指的是自动纠正 MT 系统的输出，通常会同时利用 source sentence 和原始 MT output。

### Q15. Why does Week 8 matter in the overall course structure?

- Week 8 matters because it extends the course from classification and tagging to full sequence generation, while also connecting older SMT ideas with modern Transformer and LLM-based systems.
- Week 8 很重要，因为它把课程从 classification 和 tagging 推进到了完整的 sequence generation，同时也把早期 SMT 思想和现代 Transformer、LLM-based systems 连接了起来。

---

## 15. One-Sentence Summary / 一句话总括 Week 8

- Week 8 explains machine translation as a sequence-to-sequence problem and surveys how MT systems are evaluated, modeled statistically, implemented with Transformer decoding, accelerated with speculative decoding, and extended to multilingual, low-resource, and post-editing settings.
- Week 8 把 machine translation 解释为一个 sequence-to-sequence 问题，并系统梳理了 MT system 如何被评测、如何用 statistical 和 Transformer 方法建模、如何借助 speculative decoding 加速，以及如何扩展到 multilingual、low-resource 和 post-editing 等场景。
