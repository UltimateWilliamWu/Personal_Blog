# COMP6713 Week 4 Language Models 中英对照笔记

说明：这份笔记以 `Week4-language-models.pdf` 37 页课件为主线，并对照 `Week_4.zip` 中的 BERT、GPT、LoRA 和 PEFT notebook 补全 demo 细节。每个知识点按照“英文一句，中文一句”的顺序排列，方便理解、背诵和考试作答。

---

## 1. Announcements and Weekly Roadmap / 课程提醒与本周路线图

- The lecture begins with an Emily Bender quote warning that fluent text generation should not be mistaken for genuine understanding or mind.
- 课件开头引用了 Emily Bender 的话，提醒大家不要把流畅的文本生成误当成真正的理解或心智。

- The announcement slide says the project team registration form has been sent by email.
- announcement 页说明，project team registration form 已经通过邮件发出。

- It also states that teams can have 5 members and that the scope entered in the form is tentative and meant to get early feedback.
- 课件还说明，每组可以有 5 名成员，而且表单中的 scope 是暂定的，目的是尽早获得课程组反馈。

- Weekly quizzes continue on Moodle, but there will be no quiz in Weeks 6 and 10.
- weekly quizzes 继续在 Moodle 上进行，但 Week 6 和 Week 10 没有 quiz。

- The lecture also announces 30-minute guest speaker sessions in Weeks 7 and 10.
- 课件还宣布，Week 7 和 Week 10 会有 30 分钟的 guest speaker 环节。

- The topic roadmap for this week includes BERT, GPT, fine-tuning methods, and LangChain.
- 本周的主题路线图包括 BERT、GPT、fine-tuning methods 和 LangChain。

- The broader lecture title is Transformer-based language models.
- 这一讲更大的主题标题是 Transformer-based language models。

---

## 2. Transformer-Derived Language Models / Transformer 派生语言模型

- The lecture starts by situating modern language models as derivatives of Transformer.
- 课件先把现代语言模型放到 Transformer 派生模型这个大背景中来理解。

- A Vauquois Triangle slide is shown to remind students that language processing can be thought of at different representational levels, from surface forms to deeper meaning.
- 课件展示了 Vauquois Triangle，用来提醒大家：语言处理可以在不同表示层次上理解，从表层形式一直到更深的意义层次。

- The immediate operational distinction then becomes sentence encoding versus incomplete-sentence completion.
- 接着课件把问题转化为两个操作性方向：句子编码和不完整句子的补全。

### 2.1 Broad Categories / 大类划分

- The lecture divides Transformer-based language models into encoder models and decoder models.
- 课件把 Transformer-based language models 分成 encoder models 和 decoder models 两大类。

- Encoder models use the encoder stack of Transformer.
- encoder models 使用的是 Transformer 的 encoder stack。

- They are described as auto-encoding models, meaning the current word is estimated from neighbouring words.
- 课件把它们描述成 auto-encoding models，也就是当前词由前后邻近词来估计。

- The lecture gives denoising in speech processing as an analogy for this category.
- 课件用 speech processing 中的 denoising 来类比这一类模型。

- Decoder models use the decoder stack of Transformer.
- decoder models 使用的是 Transformer 的 decoder stack。

- They are described as auto-regressive models, meaning the current word is estimated from previous words.
- 它们被描述成 auto-regressive models，也就是当前词由前面的词来估计。

- The lecture gives time-series forecasting as an analogy for decoder models.
- 课件用 time-series forecasting 来类比 decoder models。

- The slide also notes that additional effective transformer-derived models such as XLNet and BART will be revisited later.
- 课件还提到，像 XLNet 和 BART 这样其他有效的 Transformer 派生模型会在后续继续讨论。

---

## 3. Encoder Models and BERT / Encoder 模型与 BERT

- Encoder-only models learn representations for sentences by applying attention over the full input.
- encoder-only 模型通过对整个输入应用 attention，来学习句子表示。

- The lecture says the most popular encoder model is BERT.
- 课件指出，最流行的 encoder model 就是 BERT。

- BERT stands for Bidirectional Encoder Representations from Transformers.
- BERT 的全称是 Bidirectional Encoder Representations from Transformers。

- It is described as an auto-encoding model because the current state is learned from both previous and next states.
- 课件把它描述成 auto-encoding model，因为当前状态的学习会用到前后的状态。

- The BERT pipeline has two stages: pre-training on large unlabeled corpora and fine-tuning on labeled data for specific tasks.
- BERT 的流程分成两步：先在大规模无标注语料上做 pre-training，再在标注数据上为具体任务做 fine-tuning。

- The lecture explicitly shows the pipeline `Large unlabeled corpus -> Pre-trained BERT -> Labeled corpus -> Fine-tuned BERT`.
- 课件明确画出了 `Large unlabeled corpus -> Pre-trained BERT -> Labeled corpus -> Fine-tuned BERT` 这条管线。

### 3.1 BERT Pre-training Objectives / BERT 预训练目标

- The lecture says BERT argues that knowing a language requires two self-supervised capabilities.
- 课件说，BERT 认为“掌握语言”至少需要两种自监督能力。

- The first is masked language modeling, where the model predicts missing words.
- 第一种是 masked language modeling，也就是预测被遮掉的词。

- The lecture connects this to the human cloze task and even to understanding people with unfamiliar accents.
- 课件把它类比到人类的 cloze task，也类比到理解带陌生口音的人。

- The second objective is next sentence prediction, where the model predicts whether one sentence follows another.
- 第二个目标是 next sentence prediction，也就是判断一个句子是否跟在另一个句子后面。

- The human analogy for NSP is that if a text is scrambled, humans can often recover the right sentence order.
- 对 NSP 的人类类比是：如果一篇文本被打乱，人类通常仍然能恢复正确句子顺序。

- The lecture explicitly names the two objectives as MLM and NSP.
- 课件明确把这两个目标命名为 MLM 和 NSP。

### 3.2 Special Tokens and Input Format / 特殊标记与输入格式

- BERT uses three special tokens emphasized in the lecture: `[CLS]`, `[SEP]`, and `[MASK]`.
- 课件强调 BERT 使用三个重要 special tokens：`[CLS]`、`[SEP]` 和 `[MASK]`。

- `[CLS]` is placed at the beginning of a pair of sentences and its representation is used for NSP or sentence-level classification.
- `[CLS]` 放在句子对的最前面，它的表示会用于 NSP 或句子级分类任务。

- `[SEP]` separates the two sentences and marks a sentence boundary.
- `[SEP]` 用来分隔两个句子，并标记新的句子边界。

- `[MASK]` marks a token that has been hidden and must be predicted for MLM.
- `[MASK]` 表示一个被遮盖的 token，模型需要在 MLM 任务中把它预测出来。

- The lecture also says that 15% of words are randomly masked.
- 课件还说明，训练时会随机 mask 15% 的词。

- It further states that 50% of sentence pairs are in the correct order, and the rest are not.
- 课件还说，sentence pairs 里有 50% 的顺序是正确的，剩下 50% 是错误的。

- The lecture specifies WordPiece as the tokenizer used in BERT pre-training.
- 课件明确说，BERT 预训练里使用的是 WordPiece tokenizer。

### 3.3 What Is Being Trained? / BERT 到底在训练什么

- The slide “So, what is being trained?” shows token embeddings going through stacked encoder layers with feed-forward sublayers and supervision from MLM and NSP.
- “So, what is being trained?” 那页展示了：token embeddings 会经过多层 encoder 和 feed-forward 子层，并同时接受 MLM 和 NSP 的监督。

- This means BERT is learning contextualized encoder representations that are useful both for masked token prediction and sentence-pair classification.
- 这意味着 BERT 学到的是上下文化的 encoder 表示，它既要服务于 masked token prediction，也要服务于 sentence-pair classification。

### 3.4 Example Code and Notebook Alignment / 代码与 notebook 对齐补充

- The lecture’s code slide tells students to look for how special tokens are defined, how random masking is done, how MLM and NSP heads are implemented, and how BERT input representations are assembled.
- 课件的代码页提醒大家重点关注：special tokens 如何定义、random masking 如何实现、MLM 和 NSP heads 如何实现，以及 BERT 输入表示如何组装。

- The corresponding notebook in `Week_4.zip` demonstrates RoBERTa for masked language modeling and for sequence classification.
- `Week_4.zip` 中对应的 notebook 演示了 RoBERTa 的 masked language modeling 和 sequence classification。

- It shows tokenization into token IDs, predicting a `<mask>` token, trying different mask positions, and then using a fine-tuned emotion classifier model.
- 它展示了如何把文本 tokenization 成 token IDs、如何预测 `<mask>` 位置、如何尝试不同的 mask 位置，然后再使用一个 fine-tuned 的情绪分类模型。

- This reinforces the lecture’s point that pretrained encoder models can be used directly for MLM and can also be reused for downstream classification tasks.
- 这进一步强化了课件的观点：pretrained encoder models 可以直接做 MLM，也可以被复用到下游分类任务中。

### 3.5 Winograd Example and Fine-Tuning / Winograd 例子与 Fine-Tuning

- The lecture uses a Winograd-style example with “they feared violence” versus “they advocated violence” to highlight context-sensitive understanding.
- 课件用 Winograd 风格的例子——“they feared violence” 和 “they advocated violence”——来强调上下文敏感理解。

- This is meant to show that sentence meaning depends on subtle contextual cues, not just local word identity.
- 这说明句子意义依赖细微的上下文线索，而不仅仅是局部词项本身。

- Fine-tuning BERT is introduced as attaching an appropriate task head to a pretrained model and training it on labeled data.
- Fine-tuning BERT 被描述为：在 pretrained model 上接一个合适的 task head，然后用标注数据进行训练。

- The lecture says the `[CLS]` token is assumed to be the sentence representation for sentence-level tasks.
- 课件说，在句子级任务中，通常把 `[CLS]` token 的表示当作句子表示。

- A language model head or a task-specific linear layer plus softmax can be attached to the `[CLS]` representation.
- 可以在 `[CLS]` 表示上接 language model head，或者接 task-specific 的 linear layer 加 softmax。

- The lecture explicitly says fine-tuning can be used for tasks such as sentiment classification and named entity recognition.
- 课件明确说，fine-tuning 可以用于情感分类、命名实体识别等任务。

- It also notes that all parameters may be updated during full fine-tuning.
- 课件还说明，在 full fine-tuning 中，所有参数都可以更新。

### 3.6 BERT Variants / BERT 变体

- The lecture lists several categories of BERT-derived models.
- 课件列出了几类 BERT 派生模型。

- RoBERTa is described as a more robust BERT with changes such as dynamic masking.
- RoBERTa 被描述成更“robust”的 BERT，其中包括 dynamic masking 等改进。

- ERNIE is described as a knowledge-aware BERT with ideas such as entity masking.
- ERNIE 被描述成一个 knowledge-aware 的 BERT，例如使用 entity masking。

- Domain-specific BERTs include SciBERT, BioBERT, and LegalBERT.
- 领域化 BERT 包括 SciBERT、BioBERT 和 LegalBERT。

- Smaller or more efficient BERT variants include DistilBERT and ALBERT.
- 更小或更高效的 BERT 变体包括 DistilBERT 和 ALBERT。

- DistilBERT is characterized as a distilled, resource-efficient BERT.
- DistilBERT 被描述成 distilled、resource-efficient 的 BERT。

- ALBERT is characterized as a lighter BERT with parameter sharing across layers.
- ALBERT 被描述成一个更轻量的 BERT，它会在层之间共享参数。

- The lecture also mentions XLNet in this broader family discussion and says students should look these models up on HuggingFace.
- 课件还在这个 broader family 讨论里提到 XLNet，并建议学生去 HuggingFace 上查这些模型。

### 3.7 BERT as a Vacuum Cleaner / “BERT 是吸尘器” 类比

- The lecture uses a vacuum cleaner analogy for BERT.
- 课件用“吸尘器”来类比 BERT。

- A vacuum cleaner simulates cleaning through suction, and BERT simulates language understanding through pre-training objectives such as MLM.
- 吸尘器通过吸力来“模拟清洁”，而 BERT 则通过 MLM 等预训练任务来“模拟语言理解”。

- Different vacuum heads correspond to different task heads for BERT fine-tuning.
- 不同的吸尘器头，对应的就是 BERT fine-tuning 时接上的不同 task heads。

- The point of the analogy is that pre-training gives a general-purpose mechanism, and fine-tuning customizes it for specific surfaces or tasks.
- 这个类比的核心意思是：pre-training 提供通用能力，而 fine-tuning 则把它定制到具体表面或具体任务上。

---
## 4. Decoder Models and GPT / Decoder 模型与 GPT

- The lecture then moves to decoder-only models.
- 接着课件转到 decoder-only models。

- Decoder models are described as learning to complete sentences.
- decoder models 被描述成“学会补全句子”的模型。

- They use only the decoder stack of the Transformer.
- 它们只使用 Transformer 的 decoder stack。

- The lecture calls this causal language modeling.
- 课件把这种建模方式称为 causal language modeling。

- GPT is given as the canonical example of a decoder-only model.
- GPT 被作为 decoder-only 模型的典型代表。

- The human analogy used in the slide is that best friends complete each other’s sentences.
- 课件给的人类类比是：最好的朋友会替彼此把句子补完。

### 4.1 GPT Architecture and Prompting / GPT 架构与 Prompting

- The lecture emphasizes that in GPT-style models there is no encoder input sequence.
- 课件强调，在 GPT 这类模型里，没有 encoder 输入序列。

- Instead, the model autoregressively predicts the next token from the prompt and previously generated tokens.
- 相反，模型会从 prompt 和已经生成的 token 出发，自回归地预测下一个 token。

- The GPT-3 slide states that it has 175 billion parameters.
- GPT-3 那页明确写了它有 175 billion 参数。

- The lecture stresses that with such a model, you may not need to fine-tune at all for some tasks; you can just prompt it.
- 课件强调，对于这种模型，有些任务甚至不需要 fine-tune，直接 prompting 就可以。

- The example prompt asks for the sentiment of “I love the movie” and expects the output “positive”.
- 课件举的 prompt 例子是：判断 “I love the movie” 的情感，预期输出是 “positive”。

- In this setting, no weights are updated, so the task is solved through in-context use of the pretrained model.
- 在这种设置里，没有任何权重被更新，因此任务是通过 in-context 使用 pretrained model 来完成的。

### 4.2 GPT Demo Notes / GPT demo 补充

- The GPT notebook in `Week_4.zip` uses GPT-2 medium for autoregressive text generation.
- `Week_4.zip` 里的 GPT notebook 使用 GPT-2 medium 来做自回归文本生成。

- It shows that the model predicts the next token given all previous tokens in the prompt.
- 它明确展示：模型是在给定 prompt 中前面所有 tokens 的条件下预测下一个 token。

- The notebook also highlights practical decoding parameters such as `max_length`, `do_sample`, `num_beams`, and `no_repeat_ngram_size`.
- notebook 还强调了几个实际解码参数，例如 `max_length`、`do_sample`、`num_beams` 和 `no_repeat_ngram_size`。

- It further shows that changing the prompt can dramatically change the generated output.
- 它还演示了 prompt 略微变化就会显著改变生成结果。

- This supports the lecture’s point that prompting is a central mode of interaction with decoder-only language models.
- 这进一步支持了课件的观点：prompting 是使用 decoder-only 语言模型的核心方式。

### 4.3 Open and GPT-Like Models / 开放模型与 GPT 类模型

- The lecture includes OLMo as an example of a powerful open language model released with open data, code, checkpoints, and logs.
- 课件用 OLMo 作为一个开放语言模型的例子，它同时开放了数据、代码、checkpoints 和训练日志。

- The slide also notes architectural or training differences such as modified BPE, rotary position encoding, and SwiGLU replacing ReLU.
- 课件还顺带提到一些架构或训练上的差异，例如 modified BPE、rotary position encoding，以及用 SwiGLU 替换 ReLU。

- A separate side-track slide introduces Rotary Position Encoding, or RoPE.
- 课件还单独用一页 side-track 介绍了 Rotary Position Encoding，也就是 RoPE。

- The lecture lists OPT, T5, LLaMA, and Qwen among models similar to GPT and encourages students to explore pretrained versions on HuggingFace.
- 课件把 OPT、T5、LLaMA、Qwen 等列为和 GPT 同属这一波语言模型生态的代表，并鼓励大家去 HuggingFace 上查看 pretrained versions。

---

## 5. Fine-Tuning Methods / 微调方法

- The lecture then turns to how decoder models and other pretrained language models can be adapted to specific tasks.
- 接着课件转到：如何把 decoder models 和其他 pretrained language models 定制到具体任务上。

- Fine-tuning means updating model parameters using labeled data.
- fine-tuning 指的是：基于标注数据去更新模型参数。

- The lecture notes that you may freeze some layers, using the `requires_grad` mechanism.
- 课件指出，你也可以冻结一部分层，这通常通过 `requires_grad` 机制实现。

### 5.1 Prefix-Tuning and Prompt Tuning / Prefix-Tuning 与 Prompt Tuning

- Prefix-tuning adds special prefix tokens at the beginning of the sequence.
- prefix-tuning 会在序列开头加入 special prefix tokens。

- The vectors corresponding to these prefix tokens are learned, while the majority of model parameters remain frozen.
- 这些 prefix tokens 对应的向量会被学习，而大多数原模型参数保持冻结。

- The slide cites the Prefix-Tuning paper by Li and Liang.
- 课件引用了 Li 和 Liang 的 Prefix-Tuning 论文。

- Prompt tuning is then introduced as a generalization where learned prompts or soft prompts are optimized instead of full model weights.
- 接着课件介绍 prompt tuning，把它描述成一种更一般的做法：优化 learned prompts，也就是 soft prompts，而不是更新完整模型权重。

- The lecture says that in this setup the resultant prompts are called soft prompts.
- 课件明确说，在这种设置下，得到的 prompts 被称为 soft prompts。

### 5.2 PEFT / 参数高效微调

- The lecture groups several such methods under parameter-efficient fine-tuning, or PEFT.
- 课件把这类方法统一归为 parameter-efficient fine-tuning，也就是 PEFT。

- The main idea is that for larger models, full fine-tuning carries significant computational overhead.
- 核心思想是：对于更大的模型，full fine-tuning 会带来非常显著的计算开销。

- Therefore, instead of updating all parameters, we keep most pretrained weights frozen and update only a small carefully chosen subset.
- 因此我们不更新所有参数，而是冻结大部分 pretrained weights，只更新一小部分精心选择的参数。

### 5.3 LoRA / LoRA

- The lecture gives LoRA, or Low-Rank Adaptation, as a central PEFT method.
- 课件把 LoRA，也就是 Low-Rank Adaptation，作为 PEFT 的核心方法来讲。

- LoRA keeps pretrained weights frozen and learns only two low-rank matrices, often called `A` and `B`.
- LoRA 会冻结 pretrained weights，只额外学习两个低秩矩阵，通常写作 `A` 和 `B`。

- Because these matrices are low-rank, they represent a compact update to a large weight matrix.
- 因为这些矩阵是低秩的，所以它们相当于对大权重矩阵做了一个很紧凑的增量更新。

- The lecture explicitly says this can reduce the number of trainable parameters by orders of magnitude.
- 课件明确说，这样可以把需要训练的参数量减少好几个数量级。

- The slide gives an intuition example comparing a full `512 x 512` weight update with a low-rank decomposition using rank `r = 4`.
- 课件用一个直观的例子比较了完整的 `512 x 512` 权重更新和使用 `r = 4` 的低秩分解。

- The point is that two skinny matrices can be much cheaper to train than one full matrix.
- 核心意思是：两个瘦矩阵的训练成本会远小于一个完整大矩阵。

- The lecture also states that LoRA can be applied to any weight matrices such as `Q`, `K`, or `V` matrices in the neural network.
- 课件还明确说，LoRA 可以加在神经网络里的任何权重矩阵上，例如 `Q`、`K`、`V` 矩阵。

### 5.4 LoRA Demo Notes / LoRA demo 补充

- The simple LoRA notebook in `Week_4.zip` compares a standard feedforward network with a LoRA version using `loralib`.
- `Week_4.zip` 中的简单 LoRA notebook 用 `loralib` 对比了普通 feedforward network 和 LoRA 版本。

- It counts total and trainable parameters and shows that only LoRA parameters are trainable in the adapter version.
- 它会统计总参数量和可训练参数量，并展示在 adapter 版本里只有 LoRA 参数是可训练的。

- The notebook then trains both versions on synthetic data to illustrate lower training cost for the LoRA version.
- 然后 notebook 会在 synthetic data 上训练两个版本，用来展示 LoRA 版本的训练开销更低。

- Another notebook applies PEFT-style LoRA fine-tuning to `facebook/opt-350m` using the HuggingFace `peft` library.
- 另一个 notebook 则使用 HuggingFace 的 `peft` 库，把 LoRA 风格的 PEFT fine-tuning 应用到 `facebook/opt-350m` 上。

- It builds a `LoraConfig`, wraps the model with `get_peft_model`, loads a dataset of English quotes, fine-tunes the model, and then generates text again.
- 它会构建 `LoraConfig`，用 `get_peft_model` 包装模型，加载 English quotes 数据集，对模型做 fine-tuning，然后再次生成文本。

---
## 6. Prompt Engineering and Reasoning Prompts / Prompt Engineering 与推理式 Prompting

- The lecture defines prompt engineering as crafting careful instructions to obtain a desired output from a language model.
- 课件把 prompt engineering 定义为：通过精心设计指令，从语言模型获得期望输出。

- A prompt is defined simply as a natural language query or instruction to a language model.
- prompt 则被简单定义为：输入给语言模型的自然语言查询或指令。

- The lecture also notes that prompt engineering has become visible enough in industry to show up in job-market discussions.
- 课件还提到，prompt engineering 在工业界已经足够显性，甚至开始出现在岗位讨论里。

### 6.1 Zero-Shot and Few-Shot Prompting / Zero-shot 与 Few-shot Prompting

- Zero-shot prompting means asking the model to perform a task without demonstrations.
- zero-shot prompting 指的是在不给示例的情况下让模型执行任务。

- Few-shot prompting means giving a small number of demonstrations, such as 1-shot or 3-shot, before the real query.
- few-shot prompting 指的是在正式问题前给少量示例，例如 1-shot 或 3-shot。

- The lecture says few-shot prompting is especially useful for new or obscure tasks.
- 课件明确说，few-shot prompting 对新任务或较冷门任务尤其有帮助。

- It also says that selecting shots is itself a skill.
- 课件还强调，如何选 shots 本身就是一种能力。

### 6.2 Prompting for Reasoning / 面向推理的 Prompting

- The lecture introduces chain-of-thought prompting, including zero-shot CoT and few-shot CoT.
- 课件引入了 chain-of-thought prompting，并区分了 zero-shot CoT 和 few-shot CoT。

- Chain-of-thought prompting aims to elicit intermediate reasoning steps.
- chain-of-thought prompting 的目标是引出中间推理步骤。

- The lecture then introduces tree-of-thought prompting as a more deliberate reasoning framework.
- 接着课件介绍了 tree-of-thought prompting，把它看成一种更审慎的推理框架。

- Step-back prompting is introduced as another method that encourages abstraction before solving the problem directly.
- 课件还介绍了 step-back prompting，它鼓励模型先做抽象，再回到具体问题。

- The lecture presents System 2 Attention as a two-step prompting approach where irrelevant context is first removed and then the model reasons over the cleaned context.
- 课件介绍的 System 2 Attention 是一种两步 prompting 方法：先移除无关上下文，再让模型基于清洗后的上下文进行推理。

- It also says irrelevant information in the prompt can derail the model.
- 课件还明确说，prompt 里的无关信息会把语言模型带偏。

### 6.3 Prompting to Reduce Hallucination / 用 Prompting 减少幻觉

- Hallucination is defined here as the language model producing factually incorrect responses.
- 这里把 hallucination 定义成：语言模型生成事实错误的回答。

- The lecture introduces Chain-of-Verification prompting as a way to reduce hallucination.
- 课件引入了 Chain-of-Verification prompting，作为减少 hallucination 的方法。

- The four steps shown are: generate an answer, generate verification questions, execute verification, and generate the final verified response.
- 课件给出的四个步骤是：先生成答案，再生成验证问题，执行验证，最后生成经过验证的最终回答。

### 6.4 How to Read an NLP Paper / 如何读 NLP 论文

- The lecture includes a short framework for reading NLP papers: What, How, Why, How well, and So what.
- 课件专门给了一个读 NLP 论文的框架：What、How、Why、How well、So what。

- It suggests a practical reading order of Abstract, Introduction, Conclusion, and then diving into specific details as needed.
- 课件建议一种实用阅读顺序：先读 Abstract、Introduction、Conclusion，再按需深入具体细节。

- The lecture explicitly says students are expected to read the highlighted paper carefully.
- 课件还明确说，学生应该认真阅读那篇被点名的论文。

---

## 7. Evaluation, Benchmarks, and Datasets / 评测、基准与数据集

- The lecture defines a benchmark as a dataset together with evaluation over multiple encoder and decoder models.
- 课件把 benchmark 定义为：一个数据集加上一套对多个 encoder 和 decoder 模型进行评测的方法。

- Reproducibility is highlighted as an important property of benchmarks.
- reproducibility，也就是可复现性，被课件强调为 benchmark 的重要属性。

### 7.1 GLUE / GLUE

- GLUE stands for General Language Understanding Evaluation.
- GLUE 的全称是 General Language Understanding Evaluation。

- The lecture gives examples such as entailment, contradiction, and duplicate-question detection.
- 课件举了 entailment、contradiction 和 duplicate-question detection 的例子。

- This shows that a benchmark is typically a collection of multiple tasks rather than a single dataset only.
- 这说明 benchmark 往往不是单一数据集，而是一个多任务集合。

### 7.2 MMLU, BigBench, and Humanity’s Last Exam / MMLU、BigBench 与 Humanity’s Last Exam

- MMLU is introduced as a benchmark with 57 tasks covering subjects such as mathematics, history, computer science, and law.
- 课件介绍 MMLU 时强调它包含 57 个任务，覆盖数学、历史、计算机科学、法律等领域。

- BigBench is described as a user-contributed repository of tasks and datasets, including both JSON tasks and programmatic tasks.
- BigBench 被描述成一个用户共建的任务和数据集仓库，其中既有 JSON tasks，也有 programmatic tasks。

- The lecture encourages students to browse BigBench for project ideas.
- 课件鼓励学生去 BigBench 里找 project ideas。

- Humanity’s Last Exam is introduced as a benchmark of expert-level academic questions for evaluating AI capabilities.
- Humanity’s Last Exam 被介绍成一个由 expert-level academic questions 构成的 benchmark，用来评估 AI 能力。

- The lecture then raises the contamination problem.
- 课件接着提出 contamination 问题。

- Pre-training corpora are pulled from the internet, newer language models may have seen benchmark data, and reported performance may therefore be inflated.
- 由于 pre-training corpora 来自互联网，更新的语言模型可能已经见过 benchmark 数据，因此报告出来的性能可能会被污染和高估。

### 7.3 Shared Tasks and Public Datasets / Shared Task 与公共数据集

- The lecture mentions SemEval as an example of competitions run by workshops or conferences where datasets are provided to participants.
- 课件用 SemEval 作为例子，说明很多 workshop 或 conference 会组织比赛，并向参赛者提供数据集。

- It also reminds students that labeled datasets are available on HuggingFace.
- 课件还提醒大家，HuggingFace 上也能找到很多 labeled datasets。

---

## 8. LangChain and Augmented Language Models / LangChain 与增强型语言模型

- The lecture introduces LangChain as a framework for combining LLMs with other components through composability.
- 课件把 LangChain 介绍成一个通过 composability 把 LLM 与其他组件组合起来的框架。

- It says LangChain is primarily used to productionise LLMs, but also has potential for interdisciplinary applications.
- 课件说，LangChain 主要被用来把 LLMs 工程化和生产化，但也有跨学科应用潜力。

- The lecture warns that LangChain is fast-evolving and the sample notebook shown is only illustrative.
- 课件还提醒，LangChain 变化很快，展示的 sample notebook 只能作为 illustrative 示例。

### 8.1 Augmented Language Models / 增强型语言模型

- The lecture uses the phrase “augmented language models” for systems that combine foundation language models with reasoning and external tools.
- 课件用 “augmented language models” 来指代那些把 foundation language models 与推理和外部工具结合起来的系统。

- The key idea is that external information can guide model output rather than forcing the model to rely only on its internal parameters.
- 核心思想是：通过外部信息来引导模型输出，而不是让模型只依赖内部参数。

### 8.2 Key Elements of LangChain / LangChain 的关键要素

- The lecture lists key elements such as LLMs, prompt templates, tools, chains, and routers.
- 课件列出的关键要素包括 LLMs、prompt templates、tools、chains 和 routers。

- The LLM side may include providers such as HuggingFace, OpenAI, and Databricks.
- 在 LLM 这一侧，课件举的例子包括 HuggingFace、OpenAI 和 Databricks。

- The tools side may include Google Search, DuckDuckGo, ShellTool, Wikipedia, PubMed, and arXiv.
- 在 tools 一侧，课件举的例子包括 Google Search、DuckDuckGo、ShellTool、Wikipedia、PubMed 和 arXiv。

- Prompt templates with input parameters are explicitly highlighted.
- 课件还特别强调了带输入参数的 prompt templates。

### 8.3 Chains / Chains

- A chain can first produce an essay from a prompt.
- 一个 chain 可以先根据 prompt 生成一篇 essay。

- Another chain can take that essay and ask the LLM to generate tutor feedback.
- 另一个 chain 可以接收这篇 essay，再让 LLM 生成 tutor feedback。

- A reasoning chain can first ask for a formula and then use that formula to compute a numeric answer.
- 一个推理 chain 可以先询问公式，再利用公式去算出数值答案。

- Another example chains together search results and answer generation for recent or reliable information.
- 课件还展示了把 search 结果和 answer generation 串起来的例子，以获得更及时或更可靠的信息。

### 8.4 Tool Calling and Toolformer / 工具调用与 Toolformer

- The lecture asks how language models can call tools.
- 课件明确提出一个问题：语言模型是怎么去调用工具的。

- Toolformer is given as one answer.
- Toolformer 被作为一个回答给出。

- The lecture says API calls can themselves be represented as special tokens to generate.
- 课件说，API calls 本身也可以被表示为模型要生成的 special tokens。

- When the model outputs those special tokens, the actual function call can then be executed.
- 当模型输出这些 special tokens 时，系统就可以去执行真实的函数调用。

- The Toolformer slide says a GPT-based model can be fine-tuned on API-call examples so that tool usage becomes part of generation.
- Toolformer 那页说明，可以在 API-call examples 上 fine-tune 一个 GPT-based 模型，从而让工具使用成为生成过程的一部分。

---
## 9. Closing Summary, Readings, and Epilogue / 收束总结、阅读建议与尾声

### 9.1 Lecture Summary Slide / 课程总结页

- The summary slide groups the week into Transformer derivatives, encoder models, decoder models, prompt engineering, fine-tuning methods, and datasets plus libraries.
- summary 页把本周内容归纳为 Transformer 衍生模型、encoder models、decoder models、prompt engineering、fine-tuning methods，以及 datasets + libraries。

- The summary explicitly ties BERT to pre-training and fine-tuning and ties GPT to prompting.
- 这页总结明确把 BERT 和 pre-training / fine-tuning 联系起来，也把 GPT 和 prompting 联系起来。

- It also states that prompt engineering covers zero-shot, few-shot, chain-of-thought, tree-of-thought, and related prompting ideas.
- 它还明确指出 prompt engineering 包括 zero-shot、few-shot、chain-of-thought、tree-of-thought 等相关 prompting 思路。

- The lecture frames PEFT, prompt tuning, prefix tuning, and LoRA as the key adaptation methods for large pretrained models.
- 课件把 PEFT、prompt tuning、prefix tuning 和 LoRA 归纳为大规模预训练模型的核心适配方法。

- The summary also links benchmarks, LangChain, and tool calling into one practical toolkit layer around language models.
- 这页总结还把 benchmarks、LangChain 和 tool calling 连接成语言模型外围的一个实用工具层。

### 9.2 PTLMs and the Need for Adaptation / 预训练语言模型与适配需求

- The lecture explicitly states that pre-trained language models are powerful on their own but still need to be adapted to the data and use case.
- 课件明确写道，pre-trained language models 本身已经很强大，但仍然需要根据具体数据和使用场景进行适配。

- This statement is conceptually important because it explains why prompting, fine-tuning, PEFT, and tool use all matter.
- 这句话在概念上很重要，因为它解释了为什么 prompting、fine-tuning、PEFT 和 tool use 都有存在的必要。

- A model with broad general capability is not automatically optimized for a specific domain, task definition, or evaluation metric.
- 一个具有广泛通用能力的模型，并不会自动针对某个具体领域、任务定义或评测指标做到最优。

- In practice, customization may happen through labeled fine-tuning, low-rank adapters, prompt design, retrieval, or chained tools.
- 在实践中，这种定制化可能通过 labeled fine-tuning、low-rank adapters、prompt design、retrieval 或 chained tools 来完成。

### 9.3 Critical Reading: Stochastic Parrots / 批判性阅读：随机鹦鹉

- The lecture explicitly recommends reading the paper `On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?`
- 课件明确推荐阅读论文 `On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?`。

- This recommendation reminds students that language models must also be evaluated critically in terms of social impact, data use, and risk.
- 这个推荐提醒学生，对语言模型的评估不能只看性能，还要批判性地考虑社会影响、数据使用与风险问题。

- The phrase `stochastic parrots` warns that language models may reproduce patterns fluently without genuine understanding or grounded reasoning.
- `stochastic parrots` 这个说法提醒我们，语言模型可能只是流畅地复现模式，而不具备真正的理解或 grounded reasoning。

- This connects back to the opening Emily Bender quote and gives a cautionary lens for the entire week.
- 这也和开头的 Emily Bender 引言相呼应，为整周内容提供了一个批判性观察视角。

### 9.4 Transition to the Next Week / 通向下一周

- The lecture ends by asking how language models and other NLP techniques can be customized for specific NLP tasks.
- 课件最后提出一个过渡问题：语言模型和其他 NLP 技术究竟如何为特定 NLP 任务进行定制。

- It then announces that the next week will focus on sentiment analysis.
- 然后课件宣布，下一周的主题将是 sentiment analysis。

- This transition is important because Week 4 mainly introduces model families and adaptation tools, while Week 5 moves into a concrete downstream task.
- 这个过渡很重要，因为 Week 4 主要介绍模型家族与适配工具，而 Week 5 会进入一个具体的下游任务。

### 9.5 Suggested Reading / 推荐阅读

- The lecture recommends the Stanford SLP chapter as background for the following week.
- 课件推荐了 Stanford SLP 的相关章节，作为下一周内容的背景阅读。

- It specifically recommends the original BERT paper by Devlin et al. (2019).
- 它还特别推荐了 Devlin 等人发表于 2019 年的原始 BERT 论文。

- It also recommends visual intuition material such as Jay Alammar's illustrated BERT explanation.
- 同时课件也推荐了 Jay Alammar 的 illustrated BERT 这类强调直观理解的材料。

- For decoder models, it points students to the GPT-3 paper `Language Models are Few-Shot Learners`.
- 在 decoder models 方面，课件建议学生阅读 GPT-3 论文 `Language Models are Few-Shot Learners`。

- For adaptation methods, it recommends the LoRA paper and strongly recommends the HuggingFace PEFT repository.
- 在模型适配方法方面，课件推荐了 LoRA 论文，并且强烈建议查看 HuggingFace 的 PEFT 仓库。

- These readings are not random references; they map directly onto the week's central technical themes.
- 这些阅读材料不是随意附带的参考，而是直接对应本周最核心的技术主题。

### 9.6 BERT Epilogue: Input Representation / BERT 尾声：输入表示

- The final epilogue slide states that BERT input is represented by adding token embeddings, segment embeddings, and position embeddings.
- 最后一页 epilogue 明确说明，BERT 的输入表示是由 token embeddings、segment embeddings 和 position embeddings 相加得到的。

- Token embeddings encode lexical identity.
- token embeddings 用来编码词项本身的身份信息。

- Segment embeddings encode which sentence segment a token belongs to, such as sentence A versus sentence B.
- segment embeddings 用来编码一个 token 属于哪个句段，例如 sentence A 还是 sentence B。

- Position embeddings encode the token's position in the sequence.
- position embeddings 用来编码 token 在序列中的位置。

- This detail matters because it shows that BERT's input representation combines lexical, structural, and positional information before entering the encoder stack.
- 这个细节很重要，因为它说明 BERT 在进入 encoder stack 之前，就已经把 lexical、structural 和 positional 三类信息融合进了输入表示里。

---

## 10. High-Frequency Exam Points / 高频考点总结

- Encoder models use bidirectional context and are commonly trained with auto-encoding objectives such as masked language modeling.
- encoder models 使用双向上下文，常见训练目标是 masked language modeling 这类 auto-encoding objective。

- Decoder models use left-to-right causal prediction and are commonly trained with autoregressive language modeling.
- decoder models 使用从左到右的 causal prediction，常见训练目标是 autoregressive language modeling。

- BERT is encoder-only, bidirectional, pretrained, then fine-tuned for downstream tasks.
- BERT 是 encoder-only、bidirectional、先预训练、再对下游任务进行 fine-tuning 的模型。

- GPT is decoder-only and is especially associated with prompting and in-context learning.
- GPT 是 decoder-only 模型，并且特别与 prompting 和 in-context learning 联系在一起。

- MLM predicts masked tokens from surrounding context, while NSP predicts whether sentence pairs are in the correct order or relation.
- MLM 是根据周围上下文去预测被 mask 的 token，而 NSP 是判断句子对是否处于正确顺序或关系。

- Fine-tuning updates model parameters for a task, whereas prompting changes the input without changing model weights.
- fine-tuning 会为了任务更新模型参数，而 prompting 只改变输入形式，不会改变模型权重。

- Prefix tuning and prompt tuning are PEFT methods that keep most pretrained parameters frozen.
- prefix tuning 和 prompt tuning 都属于 PEFT 方法，并且通常会冻结大部分预训练参数。

- LoRA freezes the original weights and learns low-rank updates, greatly reducing trainable parameter count.
- LoRA 会冻结原始权重，只学习低秩更新，因此能显著减少可训练参数数量。

- Zero-shot prompting provides no examples, while few-shot prompting provides a small number of examples before the real query.
- zero-shot prompting 不给示例，而 few-shot prompting 会在真实问题前给少量示例。

- Chain-of-thought prompts intermediate reasoning, tree-of-thought explores multiple reasoning branches, and chain-of-verification checks an answer for errors.
- chain-of-thought 会显式提示中间推理，tree-of-thought 会探索多个推理分支，而 chain-of-verification 会对答案进行错误检查。

- Benchmarks are not just datasets; they also include evaluation setups that enable comparison and reproducibility.
- benchmark 不只是数据集，它还包含评测设置，从而支持比较和可复现性。

- Benchmark contamination happens when test material is already present in pretraining data or otherwise leaks into the model.
- benchmark contamination 指的是测试材料已经出现在 pretraining data 中，或者以其他方式泄露给了模型。

- LangChain is a compositional framework for combining LLMs with prompts, tools, chains, and routers.
- LangChain 是一个组合式框架，用来把 LLMs、prompts、tools、chains 和 routers 连接起来。

- Toolformer treats API calls as special tokens and fine-tunes a model so tool usage becomes part of generation.
- Toolformer 把 API calls 当作 special tokens，并通过 fine-tune 让工具使用成为生成过程的一部分。

- BERT input representation is the sum of token embeddings, segment embeddings, and position embeddings.
- BERT 的输入表示等于 token、segment 和 position embeddings 三者之和。

---

## 11. Model Answers to Likely Exam Questions / 常见考题标准答案

### Q1. What is the difference between encoder models and decoder models?

- Encoder models use bidirectional context to build representations of input tokens, while decoder models generate tokens autoregressively using only preceding context.
- encoder models 使用双向上下文来构建输入 token 的表示，而 decoder models 则只利用前文上下文进行自回归生成。

### Q2. Why is BERT called an auto-encoding model?

- BERT is called an auto-encoding model because it reconstructs masked input information from surrounding context rather than predicting the next token left to right.
- BERT 被称为 auto-encoding model，是因为它通过周围上下文去恢复被遮蔽的输入信息，而不是从左到右预测下一个 token。

### Q3. What are the two classic BERT pre-training objectives introduced in the lecture?

- The two classic objectives are masked language modeling and next sentence prediction.
- 课件介绍的两个经典 BERT 预训练目标是 masked language modeling 和 next sentence prediction。

### Q4. What is the role of the `[CLS]` token in BERT fine-tuning?

- The `[CLS]` token is commonly used as a sentence-level representation that is fed into a task-specific head for classification.
- `[CLS]` token 通常被当作句子级表示，再送入特定任务的输出头中做分类。

### Q5. Why is GPT associated with prompting rather than standard fine-tuning in the lecture narrative?

- GPT is associated with prompting because decoder-only autoregressive models can often perform tasks from carefully designed instructions and examples without updating model weights.
- 在这节课的叙事里，GPT 与 prompting 联系更紧密，因为 decoder-only 的自回归模型常常可以通过精心设计的指令和示例完成任务，而不需要更新模型权重。

### Q6. What is the difference between zero-shot and few-shot prompting?

- Zero-shot prompting provides only the task instruction, while few-shot prompting also includes a small number of demonstration examples.
- zero-shot prompting 只提供任务指令，而 few-shot prompting 还会额外提供少量示范样例。

### Q7. What problem is PEFT trying to solve?

- PEFT tries to adapt large pretrained models efficiently by reducing the number of trainable parameters, memory use, and computational cost.
- PEFT 试图解决的问题是：如何以更高效的方式适配大型预训练模型，减少可训练参数、内存开销和计算成本。

### Q8. Explain LoRA in one concise answer.

- LoRA freezes the original model weights and learns low-rank update matrices, allowing task adaptation with far fewer trainable parameters.
- LoRA 会冻结原始模型权重，只学习低秩更新矩阵，因此可以用更少的可训练参数完成任务适配。

### Q9. What is the difference between full fine-tuning and prompt tuning?

- Full fine-tuning updates many or all model parameters, while prompt tuning keeps model weights frozen and learns task-specific prompt representations.
- full fine-tuning 会更新很多甚至全部模型参数，而 prompt tuning 会冻结模型权重，只学习任务特定的 prompt 表示。

### Q10. Why are benchmarks important in NLP?

- Benchmarks are important because they provide shared datasets and evaluation procedures so different models can be compared systematically and reproducibly.
- benchmarks 之所以重要，是因为它们提供了共享的数据集和评测流程，使不同模型可以被系统地、可复现地进行比较。

### Q11. Why is benchmark contamination a serious concern?

- Benchmark contamination is serious because a model may appear strong simply because it has already seen benchmark material during pretraining, which makes the reported score misleading.
- benchmark contamination 之所以严重，是因为模型可能只是由于在预训练阶段见过 benchmark 内容才表现得很强，从而让分数产生误导性。

### Q12. What does LangChain add beyond a bare language model?

- LangChain adds composability by linking language models with prompt templates, tools, chains, and routing logic.
- LangChain 在裸语言模型之外增加的是 composability，也就是把语言模型和 prompt templates、tools、chains 以及 routing logic 连接起来。

### Q13. How does Toolformer relate tool calling to language modeling?

- Toolformer relates tool calling to language modeling by treating API calls as tokens that can be generated and then executed.
- Toolformer 把 tool calling 和 language modeling 联系起来的方式是：把 API calls 当作可生成的 token，然后在生成后执行它们。

### Q14. Why can we say that pretrained language models still need adaptation?

- We can say this because a general model may not match a target domain, task definition, or operational setting unless it is adapted through prompting, fine-tuning, PEFT, or external tools.
- 我们可以这样说，是因为一个通用模型通常并不会天然匹配目标领域、任务定义或真实应用环境，必须通过 prompting、fine-tuning、PEFT 或外部工具进一步适配。

### Q15. What are the three components added together in BERT input representation?

- BERT input representation is the sum of token embeddings, segment embeddings, and position embeddings.
- BERT 的输入表示是 token embeddings、segment embeddings 和 position embeddings 三者相加的结果。

### Q16. Why does the lecture mention `stochastic parrots`?

- The lecture mentions `stochastic parrots` to remind students that strong surface fluency does not automatically imply understanding, safety, fairness, or grounded reasoning.
- 课件提到 `stochastic parrots`，是为了提醒学生：表面上的高流畅度并不自动意味着真正的理解、安全、公平或 grounded reasoning。

### Q17. How should you read an NLP paper according to the lecture?

- You should ask what the paper does, how it does it, why the method is needed, how well it works, and why the result matters.
- 按照课件的建议，读 NLP 论文时应该问：它做了什么、它怎么做、为什么需要这个方法、它做得怎么样，以及这些结果为什么重要。

### Q18. Why does Week 4 naturally lead into Week 5?

- Week 4 introduces the major language model families and adaptation methods, and Week 5 applies such models to the concrete downstream task of sentiment analysis.
- Week 4 介绍了主要的语言模型家族和适配方法，而 Week 5 会把这些模型应用到一个具体下游任务，也就是 sentiment analysis。

---

## 12. One-Sentence Summary / 一句话总括 Week 4

- Week 4 explains how Transformer-based language models split into encoder and decoder families, how they are adapted through fine-tuning, PEFT, and prompting, and how evaluation, tool use, and LangChain turn them into practical NLP systems.
- Week 4 说明了 Transformer-based language models 如何分化为 encoder 和 decoder 两大家族，又如何通过 fine-tuning、PEFT 和 prompting 被适配，并进一步借助评测、工具调用和 LangChain 变成可落地的 NLP 系统。
