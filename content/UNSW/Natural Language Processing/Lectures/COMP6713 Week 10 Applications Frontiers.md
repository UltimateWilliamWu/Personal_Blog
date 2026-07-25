---
tags:
  - UNSW
  - UNSW/COMP6713
  - Topic/NLP
  - Type/Lecture
---

﻿# Week 10: Applications & Frontiers

- These notes cover the Week 10 lecture, which shifts from individual NLP tasks to deployment-facing applications, model risks, fairness, reasoning, and final-exam recap.
- 这份笔记覆盖 Week 10 课件；这一周的重点从单个 NLP task 转向面向部署的应用、模型风险、公平性、reasoning，以及 final exam recap。

## 1. Weekly Position and Main Topics / 本周定位与核心主题

- Week 10 is framed as the applications-and-frontiers week of the course.
- Week 10 被定位为整门课的 applications-and-frontiers 周。

- The lecture topics are organised around applications, hallucination, bias, reasoning, and course recap.
- 课件主题围绕 applications、hallucination、bias、reasoning 和课程 recap 展开。

- The opening administrative slides note that there is no quiz in Week 10 and that the final exam will be discussed in class.
- 开头的行政说明指出 Week 10 没有 quiz，且 final exam 会在课堂中讨论。

- The lecture schedule also includes guest talks, which reinforces that this week is meant to connect class concepts to real-world NLP practice.
- 课件安排中还包含 guest talk，这说明本周的目的之一就是把课堂概念与真实世界的 NLP 实践连接起来。

## 2. Application Domains / 应用领域

- The lecture uses several application areas to show that NLP is not tied to a single industry.
- 课件通过多个应用领域说明，NLP 并不局限于某一个行业。

- Law is used as an example domain in which NLP supports tasks such as document analysis, retrieval, summarization, and legal reasoning assistance.
- Law 被用作一个示例领域，说明 NLP 可以支持 document analysis、retrieval、summarization 和 legal reasoning assistance 等任务。

- Science is presented through domain-specific large language models for natural science.
- Science 这一部分则通过面向自然科学的 domain-specific large language model 来展示。

- Cybersecurity is highlighted both as an application domain and as a safety/security domain for LLMs themselves.
- Cybersecurity 既被当作应用领域来讲，也被当作 LLM 自身 safety/security 风险的重要场景来讲。

- Mobility is included to show that language models can be used even in areas such as human mobility forecasting through prompt-based formulations.
- Mobility 的出现说明 language model 甚至可以被用在 human mobility forecasting 这种看似不典型的领域，并通过 prompt-based formulation 来完成任务。

- Public health is included as another example where NLP and AI can help with analysis, access to information, and decision support.
- Public health 则被用来说明 NLP 和 AI 可以在信息分析、信息可达性和决策支持中发挥作用。

- The broader takeaway is that the same NLP foundations can be reconfigured for very different application constraints and ethics requirements.
- 更重要的 takeaway 是：同一套 NLP foundation 可以被重组到完全不同的应用约束和 ethics 要求之下。

## 3. Hallucination and Related Failure Modes / 幻觉与相关失败模式

- Hallucination is introduced as one of the central challenges of modern NLP and LLM deployment.
- hallucination 被明确介绍为现代 NLP 和 LLM 部署中的核心挑战之一。

- The lecture distinguishes hallucination from degeneration.
- 课件把 hallucination 与 degeneration 做了区分。

- Degeneration refers to outputs that are bland, incoherent, or trapped in repetitive loops.
- degeneration 指的是 bland、incoherent，或者陷入 repetitive loop 的输出。

- Hallucination refers to undesirable generation whose content is nonsensical or unfaithful to the source input or context.
- hallucination 则指那些内容上不合理、或者对 source input/context 不忠实的生成结果。

- The lecture uses the terms intrinsic hallucination and extrinsic hallucination.
- 课件使用了 intrinsic hallucination 和 extrinsic hallucination 两个术语。

- Intrinsic hallucination means the generated output contradicts or distorts information present in the source.
- intrinsic hallucination 指生成结果与 source 中已有信息相矛盾，或者歪曲了 source 中的信息。

- Extrinsic hallucination means the generated output introduces unsupported content that is not grounded in the source.
- extrinsic hallucination 指生成结果引入了 source 中没有支撑的内容，也就是缺乏 grounding 的内容。

- The slide example contrasts a faithful statement about COVID-19 clinical trials with an unsupported or incorrect statement about Ebola vaccine timing to illustrate these categories.
- 课件通过对比关于 COVID-19 临床试验的 faithful 说法，以及关于 Ebola vaccine 时间线的错误说法，来说明这些类别的区别。

## 4. How Hallucination Can Be Measured / 如何衡量幻觉

- The lecture says hallucination can be measured through human evaluation.
- 课件指出，hallucination 可以通过 human evaluation 来评估。

- It can also be checked against an external knowledge base when such a resource exists.
- 如果存在外部知识库，也可以把生成结果与知识库进行核验。

- Reference-based automatic metrics such as ROUGE can sometimes be used when reference outputs are available.
- 当 reference output 存在时，也可以使用 ROUGE 之类的 reference-based automatic metric。

- The lecture also proposes Natural Language Inference as a way to test whether a generated sentence is entailed, contradicted, or unsupported by the given document or context.
- 课件还提出可以使用 Natural Language Inference 来判断生成句子是否被 document/context entail、contradict，或者 unsupported。

- The important point is that hallucination evaluation is context-sensitive, so no single metric is always sufficient.
- 这里最重要的一点是，hallucination evaluation 具有明显的 context-sensitive 特征，因此不存在一个总是足够的单一 metric。

## 5. What Bias Means in NLP / NLP 中的 Bias 是什么

- The lecture defines bias both in a dictionary sense and in a machine-learning sense.
- 课件同时从 dictionary 意义和 machine-learning 意义来定义 bias。

- In the ordinary sense, bias is an unfair inclination or prejudice toward or against a person or group.
- 在普通意义上，bias 是对某个人或群体的 unfair inclination 或 prejudice。

- In the modeling sense, bias is framed as a mismatch between ideal and actual distributions of labels and user attributes in the training and application of a system.
- 在建模意义上，bias 被表述为：系统在训练和应用中，label 分布和 user attribute 分布相对于理想状态发生了偏离。

- The lecture lists several types of bias: selection bias, label bias, semantic bias, bias amplification, and over- or under-exposure.
- 课件列出了多种 bias：selection bias、label bias、semantic bias、bias amplification，以及 over- 或 under-exposure。

- Bias is especially important because model behaviour often differs across socially meaningful subgroups.
- bias 之所以重要，是因为模型在 socially meaningful subgroup 上的表现往往并不一致。

- The lecture motivates this with protected attributes listed under the Fair Work Act, such as race, sex, age, disability, religion, gender identity, and related status markers.
- 课件借助 Fair Work Act 中列出的 protected attribute 来说明这个问题，例如 race、sex、age、disability、religion、gender identity 等。

## 6. Why Bias Must Be Measured / 为什么必须测量 Bias

- Measuring bias is described as necessary for understanding and addressing unfairness in NLP systems.
- 课件把 bias measurement 描述为理解和应对 NLP 系统中 unfairness 的必要步骤。

- The aim is to quantify how a model behaves differently across social groups.
- 目标是量化模型在不同 social group 上的行为差异。

- The lecture says that a fairness metric typically has two components: a scoring function for subsets of samples and a comparison function that turns those subset scores into a fairness score.
- 课件指出，fairness metric 通常由两部分构成：一是对 sample subset 打分的 scoring function，二是把不同 subset score 转成 fairness score 的 comparison function。

- This framing is important because it explains why many fairness metrics look different on the surface while sharing a common structure.
- 这种表述很重要，因为它解释了为什么许多 fairness metric 虽然形式不同，但底层结构其实相似。

## 7. Group Fairness and Demographic Parity / 群体公平与 Demographic Parity

- Group fairness requires parity of some statistical measure across protected groups.
- group fairness 要求某种统计量在 protected group 之间保持 parity。

- The lecture uses demographic parity as a concrete example.
- 课件以 demographic parity 作为一个具体例子。

- Demographic parity requires the positive classification rate to be equal across different groups.
- demographic parity 要求不同 group 的 positive classification rate 相等。

- This is a group-level notion of fairness rather than an individual-level one.
- 这是一种 group-level 的 fairness 观念，而不是 individual-level 的公平定义。

- The lecture treats it as an intuitive but limited criterion, because equal rates do not guarantee fairness in every operational sense.
- 课件把它当作一个直观但有限的标准，因为 rate 相等并不意味着所有 operational sense 上都公平。

## 8. Counterfactual Fairness / 反事实公平

- Counterfactual fairness is introduced as an invariance requirement.
- counterfactual fairness 被介绍为一种 invariance requirement。

- The idea is to compare an individual in the actual world with hypothetical versions of that same individual in counterfactual worlds where a protected attribute is changed.
- 其核心思想是：把现实世界中的某个个体，与多个 counterfactual world 中“只改变 protected attribute 的同一个个体”进行比较。

- If the output changes inappropriately when only the protected attribute is altered, the model may be unfair.
- 如果只改变 protected attribute 就导致输出发生不恰当变化，那么模型就可能存在 unfairness。

- The lecture uses an example from resume-job matching, such as changing name, city, or gender to see whether the ranking outcome changes.
- 课件用 resume-job matching 举例，例如改变 name、city 或 gender，观察 ranking 结果是否改变。

## 9. Bias Measurement Metrics / Bias 测量指标

- The lecture organizes bias measurement along two dimensions: group fairness versus counterfactual fairness, and pairwise comparison versus background comparison.
- 课件把 bias measurement 放在两个维度上理解：group fairness 与 counterfactual fairness，以及 pairwise comparison 与 background comparison。

- Pairwise comparison compares scores between two groups directly.
- pairwise comparison 会直接比较两个 group 之间的 score。

- Background comparison compares a group against a background set, which may be the full population or an overall reference pool.
- background comparison 则把某个 group 与一个 background set 做比较，这个 background 可以是总体数据或某个总体参照集合。

- Pairwise Comparison Metric (PCM) quantifies how far apart, on average, the scores of two randomly selected groups are.
- Pairwise Comparison Metric（PCM）量化的是：随机选取两个 group 时，它们的 score 平均相距多远。

- Background Comparison Metrics (BCM) compare the score of a protected group with that of its background.
- Background Comparison Metric（BCM）则比较 protected group 与其 background 的 score 差异。

- The lecture emphasises vector-valued BCM, which avoids collapsing all groups into one aggregate score and instead returns a vector of per-group comparisons.
- 课件特别强调 vector-valued BCM，它不会把所有 group 压缩成单个 aggregate score，而是返回一个按 group 展开的 comparison vector。

- Counterfactual metrics are described through perturbation: perturb the input so that protected-group identity changes, then check whether the output changes.
- counterfactual metric 则通过 perturbation 来描述：对输入做改变，使 protected-group identity 变化，再观察输出是否变化。

## 10. Bias Mitigation / Bias 缓解方法

- The lecture gives counterfactual data augmentation as a debiasing strategy during pre-training.
- 课件把 counterfactual data augmentation 作为 pre-training 阶段的一种 debiasing strategy。

- The core idea is to rebalance the corpus by swapping bias-sensitive attribute words such as `he` and `she`.
- 其核心思想是通过交换 `he`、`she` 之类的 bias-sensitive attribute word 来重新平衡 corpus。

- The lecture also notes that debiasing can be done during fine-tuning.
- 课件还指出，debiasing 也可以在 fine-tuning 阶段完成。

- The broader point is that fairness intervention can happen at multiple stages of the training pipeline rather than only at evaluation time.
- 更重要的观点是：fairness intervention 可以发生在训练 pipeline 的多个阶段，而不只是停留在 evaluation 阶段。

## 11. Commonsense Reasoning / 常识推理

- The final technical section turns to commonsense reasoning as a frontier challenge for NLP systems.
- 最后的技术部分把 commonsense reasoning 作为 NLP system 的一个 frontier challenge 来讨论。

- The lecture divides commonsense knowledge into social commonsense, temporal commonsense, and physical commonsense.
- 课件把 commonsense knowledge 分为 social commonsense、temporal commonsense 和 physical commonsense。

- Social commonsense concerns mental states, intentions, and interpersonal situations.
- social commonsense 关注 mental state、意图和人际情境。

- Temporal commonsense concerns chronology and event ordering.
- temporal commonsense 关注时间顺序和 event ordering。

- Physical commonsense concerns likely outcomes of physical actions in the world.
- physical commonsense 关注现实世界中 physical action 的合理结果。

## 12. Reasoning as Natural Language Entailment / 把推理看成自然语言蕴含

- The lecture shows that some reasoning problems can be reformulated as Natural Language Entailment.
- 课件展示了：某些 reasoning problem 可以被重写成 Natural Language Entailment 问题。

- In this setup, a premise and a hypothesis are compared, and the output is entailment, contradiction, or neither.
- 在这种 setup 中，会比较 premise 与 hypothesis，并输出 entailment、contradiction 或 neither。

- The lecture uses simple examples such as `He is snoring` to infer whether `He is sleeping`, `He is dreaming`, or `He is awake` is entailed, contradicted, or unsupported.
- 课件通过 `He is snoring` 这类简单例子来判断 `He is sleeping`、`He is dreaming` 或 `He is awake` 分别是被 entail、contradict 还是 unsupported。

- This framing matters because many reasoning problems can be solved by converting them into a textual relation classification problem.
- 这种表述非常重要，因为很多 reasoning problem 都可以通过把问题改写成文本关系分类问题来解决。

## 13. Other Reasoning Formulations / 其他推理任务形式

- The lecture also mentions reasoning as coreference resolution.
- 课件还提到了把 reasoning 理解为 coreference resolution。

- It introduces COPA, the Choice of Plausible Alternatives benchmark.
- 它还介绍了 COPA，也就是 Choice of Plausible Alternatives 这个 benchmark。

- COPA focuses on choosing the more plausible cause or effect among alternatives.
- COPA 的核心是从多个 alternative 中选出更 plausible 的 cause 或 effect。

- These examples show that reasoning benchmarks often differ in surface form while still testing latent commonsense structure.
- 这些例子说明，reasoning benchmark 虽然表面形式各不相同，但它们共同测试的是 latent commonsense structure。

## 14. Explain-and-Predict / 先解释再预测

- The lecture presents explain-and-predict as a way of using language models for commonsense reasoning.
- 课件把 explain-and-predict 作为一种利用 language model 做 commonsense reasoning 的思路来介绍。

- The two-step idea is first to generate an explanation and then to make a selection or prediction based on that explanation.
- 它的两步法是：先生成 explanation，再基于 explanation 做 selection 或 prediction。

- The lecture links this idea to fine-tuned BERT models using special tokens such as `[CLS]` and `[SEP]`.
- 课件把这一思路与使用 `[CLS]` 和 `[SEP]` 等 special token 的 fine-tuned BERT model 联系起来理解。

- This matters because explanations can act as intermediate reasoning traces rather than relying only on a single final label.
- 这一点之所以重要，是因为 explanation 可以充当 intermediate reasoning trace，而不是只依赖单个最终 label。

## 15. Final Exam Information / 期末考试信息

- The lecture includes a concrete note about the final exam.
- 课件中包含了非常具体的 final exam 说明。

- The exam is described as an Inspera-based, invigilated, BYOD exam.
- 考试被描述为基于 Inspera 的、invigilated 的、BYOD exam。

- The slide states that there will be about 20 compulsory questions.
- 幻灯片指出考试大约会有 20 道 compulsory question。

- Most questions will have subquestions, and students are reminded to answer all of them.
- 多数题目会包含 subquestion，课件也提醒学生要把所有小问都答完。

- Students are allowed to bring one handwritten A4 cheat sheet written on both sides and a UNSW-approved calculator.
- 学生可以携带一张双面 handwritten 的 A4 cheat sheet，以及一台 UNSW-approved calculator。

- Question formats may include multiple choice, true/false, matching, drop-down selection, short answers, and concept- or formula-explanation questions.
- 题型可能包括 multiple choice、true/false、matching、drop-down selection、short answer，以及解释概念、公式、代码或输出的题目。

## 16. Course Recap and Learning Outcomes / 课程回顾与学习结果

- The final slides recap the major techniques from Weeks 1 to 10.
- 最后的 recap 幻灯片总结了 Weeks 1 到 10 的主要 technique。

- Week 1 is recapped through tools such as spaCy, NLTK, and HuggingFace pipelines.
- Week 1 通过 spaCy、NLTK 和 HuggingFace pipeline 等工具被回顾。

- Week 2 is recapped through one-hot vectors, word2vec, GloVe, and probabilistic language modeling.
- Week 2 通过 one-hot vector、word2vec、GloVe 和 probabilistic language modeling 被回顾。

- Week 3 is recapped through attention, Transformer architecture, and byte-pair tokenization.
- Week 3 通过 attention、Transformer architecture 和 byte-pair tokenization 被回顾。

- Week 4 is recapped through masked language modeling, generative language modeling, prompting, LoRA, and benchmarking.
- Week 4 通过 masked language modeling、generative language modeling、prompting、LoRA 和 benchmarking 被回顾。

- Week 5, Week 7, Week 8, and Week 9 are recapped through their task-specific techniques such as sentiment analysis, HMM/CRF, IBM models and decoding, graph-based summarization, pointer-generator networks, and RL-based alignment.
- Week 5、Week 7、Week 8 和 Week 9 则通过各自的 task-specific technique 被回顾，例如 sentiment analysis、HMM/CRF、IBM model 与 decoding、graph-based summarization、pointer-generator network，以及 RL-based alignment。

- The final slide also revisits the course learning outcomes: describing NLP tasks and ambiguity, explaining statistical and neural approaches, using NLP libraries, and designing an NLP solution with suitable formulation, method, and evaluation.
- 最后的幻灯片还回顾了课程学习结果：描述 NLP task 与 ambiguity、解释 statistical 和 neural approach、使用 NLP library，以及设计合适的问题表述、方法与评估策略。

## 17. High-Frequency Exam Points / 高频考点总结

- You should be able to define hallucination and distinguish it from degeneration.
- 你应该能够定义 hallucination，并把它与 degeneration 区分开来。

- You should know the difference between intrinsic hallucination and extrinsic hallucination.
- 你应该知道 intrinsic hallucination 与 extrinsic hallucination 的区别。

- You should be able to explain at least two ways of measuring hallucination.
- 你应该能够解释至少两种衡量 hallucination 的方式。

- You should know what bias means in NLP and be able to list types such as selection bias, label bias, semantic bias, and bias amplification.
- 你应该知道 NLP 中 bias 的含义，并能够列举 selection bias、label bias、semantic bias 和 bias amplification 等类型。

- You should be able to explain group fairness, demographic parity, and counterfactual fairness.
- 你应该能够解释 group fairness、demographic parity 和 counterfactual fairness。

- You should know what PCM and BCM measure, and why vector-valued BCM avoids over-aggregation.
- 你应该知道 PCM 和 BCM 分别测什么，以及为什么 vector-valued BCM 可以避免过度聚合。

- You should be able to describe counterfactual data augmentation as a debiasing method.
- 你应该能够把 counterfactual data augmentation 描述为一种 debiasing method。

- You should know the three common types of commonsense knowledge: social, temporal, and physical.
- 你应该知道 commonsense knowledge 的三类常见形式：social、temporal 和 physical。

- You should be able to explain reasoning as natural language entailment and reasoning as explain-and-predict.
- 你应该能够解释 reasoning as natural language entailment，以及 reasoning as explain-and-predict。

- You should also remember the final-exam format because it was explicitly included in the lecture content.
- 你还应该记住 final exam 的形式，因为这部分内容在课件中被明确写出。

## 18. Standard Answer Templates / 标准答题模板

- Hallucination is an undesirable generation phenomenon in which the model produces content that is nonsensical or unfaithful to the source or context, whereas degeneration refers more to bland, repetitive, or incoherent generation.
- hallucination 是一种不理想的生成现象，指模型产生与 source 或 context 不一致、或者本身不合理的内容；而 degeneration 更偏向 bland、repetitive 或 incoherent 的生成问题。

- Intrinsic hallucination contradicts or distorts the source, while extrinsic hallucination introduces unsupported information that is not grounded in the source.
- intrinsic hallucination 会与 source 矛盾或歪曲 source，而 extrinsic hallucination 则会引入 source 中没有依据的 unsupported information。

- Group fairness requires parity of a chosen statistic across protected groups, while counterfactual fairness requires output invariance when only a protected attribute is changed.
- group fairness 要求某个统计量在 protected group 间保持 parity，而 counterfactual fairness 要求当只改变 protected attribute 时，输出应保持不变。

- Demographic parity means that the positive prediction rate should be the same across groups.
- demographic parity 指的是不同 group 的 positive prediction rate 应该相同。

- PCM measures the average distance between scores from two groups, whereas BCM compares a protected group with a background population, and vector-valued BCM preserves per-group information instead of hiding it in a single scalar.
- PCM 衡量两个 group 之间 score 的平均距离；BCM 把 protected group 与 background population 做比较；而 vector-valued BCM 则保留了每个 group 的单独信息，而不是把它们隐藏在一个 scalar 中。

- Counterfactual data augmentation mitigates bias by creating balanced alternative examples through protected-attribute swaps such as `he` and `she`.
- counterfactual data augmentation 通过交换 `he`、`she` 等 protected-attribute word 来构造更平衡的替代样本，从而缓解 bias。

- Commonsense reasoning can be reformulated as natural language entailment by comparing a premise and a hypothesis and predicting entailment, contradiction, or neither.
- commonsense reasoning 可以被重写成 natural language entailment：比较 premise 与 hypothesis，并预测 entailment、contradiction 或 neither。

- Explain-and-predict improves reasoning by first generating an explanation and then using that explanation to support the final decision.
- explain-and-predict 通过先生成 explanation，再利用 explanation 支撑最终判断，来改进 reasoning。
