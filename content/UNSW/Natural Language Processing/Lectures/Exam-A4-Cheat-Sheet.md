# NLP Exam A4 Cheat Sheet

## Core Pipeline
- Text -> tokenization/BPE -> token IDs -> one-hot lookup -> embeddings -> model blocks -> output head -> logits -> softmax/sigmoid -> loss -> backprop -> optimizer update.
- Tokenization: splits text into units; BPE learns frequent subword merges; handles rare/OOV words better than word-level vocab.
- One-hot: sparse vector of length `V`; only identity, no semantic similarity; huge and inefficient.
- Embedding: dense vector of size `d`; learned from prediction tasks; similar contexts push words closer.
- `V`: vocabulary size. `d`: chosen embedding dimension/hyperparameter. Usually `d << V`.
- Embedding lookup: one-hot `x in R^V`, matrix `W in R^{Vxd}`, hidden vector `h=xW`; this selects the row for the token.

## Why Method A Was Not Enough
- One-hot not enough: no similarity, sparse, high-dimensional; `cat` and `dog` equally distant as `cat` and `table`.
- Need word vectors: dense learned vectors encode distributional similarity from context.
- N-gram not enough: sparse counts, fixed short context, no semantics, poor generalization to unseen phrases.
- Need RNN/LSTM: sequential hidden state models variable-length context and word order.
- LSTM improves RNN: gates reduce vanishing gradients and preserve longer dependencies.
- LSTM still not enough: sequential training is slow; long-range dependencies still hard; no full parallelism.
- Attention helps: each token directly weights relevant tokens; shorter dependency path.
- Transformer wins: attention-only, parallelizable, scalable, supports pretraining on massive corpora.

## Word2Vec
- Goal: learn embeddings by predicting co-occurrence, not by manually assigning meaning.
- Skip-gram: input center word, predict surrounding context words.
- CBOW: input surrounding context words, predict center word.
- Skip-gram is useful because many center-context pairs across large corpora reveal distributional patterns.
- Input matrix `W`: maps center word to hidden embedding `h`.
- Output matrix `W'`: maps `h` to scores for context words; also learned from random initialization.
- Full softmax is expensive: computes probability over all `V` words.
- Negative sampling: convert multiclass word prediction into binary classification of real vs fake center-context pairs.
- Boolean task: predict whether a specific center word and context word co-occur as a true pair.
- Negative sample: randomly sampled word that did not appear as the true context for that center word.
- Negative sampling rate: proportion of negative examples in the Boolean training dataset.
- Hierarchical softmax: replaces full vocabulary softmax with binary decisions along a tree path.
- Huffman tree: frequent words near root; shorter paths reduce average computation.
- Ordinary binary tree can work theoretically; Huffman is more efficient for skewed word frequencies.

## Neural Training
- Parameters start random; learning comes from loss gradients, not from prewritten meanings.
- Loss defines what "wrong" means; optimizer defines how parameters change.
- Backpropagation: computes gradients of loss w.r.t. all trainable parameters by chain rule.
- Optimizer: updates parameters, e.g. `theta <- theta - eta * grad(loss)`.
- Activation function: adds nonlinearity; without it, stacked linear layers collapse to one linear map.
- Activation is not "glue"; it transforms layer outputs before the next computation.
- Hidden activations: ReLU, GELU, tanh. Output activations: sigmoid, softmax.
- Not every sublayer needs an activation; attention already uses softmax internally; FFN usually uses GELU/ReLU.
- Deep learning still uses standard ML ideas: parameters, loss, gradients, optimization, validation.

## Formula Bank
- Softmax: `p_i = exp(z_i) / sum_j exp(z_j)`; turns logits into a categorical distribution.
- Sigmoid: `sigma(z)=1/(1+exp(-z))`; binary probability for one logit.
- Binary softmax equals sigmoid on logit difference: `softmax([a,b])_1 = sigmoid(a-b)`.
- Cross-entropy: `L=-sum_i y_i log(p_i)`; for one-hot target: `L=-log(p_gold)`.
- Cosine similarity: `cos(a,b)=a.b/(||a|| ||b||)`; `[1,0,0,1]` vs `[0,0,0,1]` = `1/(sqrt(2)*1)=0.707`.
- Attention: `Attention(Q,K,V)=softmax(QK^T/sqrt(d_k))V`.
- HMM/Viterbi: `delta_t(j)=max_i delta_{t-1}(i)a_ij b_j(x_t)`.
- Cohen's kappa: `kappa=(P_o-P_e)/(1-P_e)`.
- BLEU: clipped n-gram precision plus brevity penalty.
- LoRA: `W' = W0 + DeltaW`, `DeltaW = BA`, rank `r << d`; freeze `W0`, train `A,B`.
- LoRA init in diagram: `A` random Gaussian, `B=0`, so the initial update is zero and the base model starts unchanged.

## Transformer Essentials
- Transformer input: token embedding + positional encoding.
- Positional encoding: added because attention has no built-in word order.
- Q/K/V are learned projections inside attention.
- Query asks "what do I need?"; Key says "what do I contain?"; Value carries information to mix.
- Self-attention: Q, K, V come from same sequence.
- Cross-attention: decoder queries attend to encoder keys/values.
- Multi-head attention: several Q/K/V projections in parallel; each head can learn different relations.
- In code, `range(3)` linear layers usually means Q, K, V projections, not three heads.
- Masked self-attention: decoder cannot attend to future output tokens.
- Feed-forward network: applied independently to each token position; no context mixing.
- Add & Norm: residual connection plus normalization; stabilizes deep training.
- LM head: maps final hidden state to vocabulary logits; softmax gives next-token probabilities.
- Original Transformer: encoder-decoder architecture for MT; BPE vocab, `d_model=512`, 8 heads, 6 encoder layers, 6 decoder layers.

## Encoder, Decoder, Model Types
- Encoder block: self-attention + FFN; sees full input bidirectionally.
- Decoder block: masked self-attention + cross-attention + FFN in seq2seq; decoder-only models omit cross-attention.
- Decoder is not just encoder plus one head; it changes attention masking and may add encoder-decoder attention.
- Encoder-only: BERT; good for classification, NER, retrieval-style representations.
- Decoder-only: GPT/LLaMA; good for next-token generation and instruction following.
- Encoder-decoder: original Transformer, T5, BART; good for translation, summarization, seq2seq.
- BERT: autoencoding, bidirectional context, MLM; NSP uses final `[CLS]` representation, not `[SEP]`.
- GPT/LLaMA: autoregressive decoder-only; predicts next token from previous tokens.
- BART: encoder-decoder denoising model; strong for summarization/generation.
- XLNet: permutation language modeling.
- SciBERT: BERT variant pretrained on scientific text; BioBERT is biomedical.
- Longformer: modifies attention to sliding-window plus selected global tokens for long documents.
- LoRA: parameter-efficient fine-tuning; `phi0` = frozen pretrained base parameters/weights.

## Prompting, LLMs, APIs
- LLM pretraining is mostly self-supervised next-token prediction on large text.
- Correctness comes from data patterns, supervised tuning, RLHF/RLAIF, retrieval, and evaluation; not guaranteed.
- Instruction following is learned from instruction-response data and preference optimization.
- Chain-of-thought prompting: decomposes complex reasoning into intermediate steps; does not require fine-tuning.
- LangChain: engineering framework for chaining LLM calls/tools/retrieval; unrelated to whether CoT works.
- RAG: retrieves external evidence, then conditions generation on retrieved context.

## POS Tagging and NER
- POS tagging: assign grammatical tag to each token, e.g. noun, verb, modal.
- NER: assign entity labels to spans, e.g. PER, LOC, ORG.
- POS and NER are sequence tagging: input length equals output label length.
- Use `BertForTokenClassification` / `AutoModelForTokenClassification`, not sequence classification.
- Sequence classification outputs one label per whole text; token classification outputs one label per token.
- BIO: `B-X` begins entity, `I-X` inside, `O` outside.
- BIOES: adds `E-X` end of multi-token span and `S-X` single-token span.
- Single-token location `Waterloo` -> `S-LOC`.
- HMM POS: hidden states are tags; observations are words.
- `a_ij`: transition probability from tag/state `i` to tag/state `j`.
- `B_i` or `b_i(w)`: emission/observation probability `P(word | tag_i)`.
- CRF: discriminative sequence model estimating `P(labels | input)`, not generative.
- HMM is generative: models joint process of tags and words.
- BiLSTM+CRF: BiLSTM gives contextual token representations; CRF enforces valid label sequence structure.
- Retrieval can help NER for emerging entities by adding up-to-date evidence.

## Decoding
- Viterbi decoding: exact dynamic programming for best tag sequence in HMM/structured finite-state models.
- Beam search: approximate decoding; keeps top `k` partial sequences at each step.
- Similarities: both search high-scoring output sequences; both combine local step scores into sequence scores.
- Differences: Viterbi keeps best path per state and can be exact; beam keeps top-k hypotheses and may miss optimum.
- Differences: Viterbi usually fixed-length tagging; beam search often open-ended generation/MT.
- Greedy decoding: choose best next token each step; fast but myopic.
- Speculative decoding: draft model proposes tokens; target model verifies to speed generation.

## Machine Translation
- Parallel corpus: aligned/equivalent sentence pairs in source and target languages.
- Rule-based MT: hand-written grammar/dictionaries; interpretable but brittle.
- Statistical MT: learns phrase/probability tables from parallel corpora.
- Neural MT: encoder-decoder models learn representations and generation end-to-end.
- SVO/SOV/VSO: subject-verb-object word order types; languages differ structurally.
- BLEU: automatic MT metric using clipped n-gram precision and brevity penalty.

## Sentiment Analysis
- Lexicon/rule-based: uses positive/negative word lists; often high precision, low recall.
- CountVectorizer: bag-of-words counts; ignores order.
- TF-IDF: weights terms high if frequent in document but rare across corpus.
- Statistical classifier: features -> classifier, e.g. logistic regression/SVM/Naive Bayes.
- Neural sentiment: LSTM/BiLSTM/BERT encode context and composition.
- Aspect-based sentiment: aspect = attribute/part of target, e.g. restaurant ambience, movie plot.
- Valence: positive/negative feeling. Arousal: intensity/activation. Dominance: control/power.
- Multi-task learning: shared base encoder learns unified representation; task-specific heads learn each task.
- Auxiliary task: related helper task, e.g. hate speech detection; backprop applies to auxiliary loss too.
- BERT classification: use `[CLS]` representation with classification head.
- AutoPrompt: searches trigger words to add to prompt.

## Summarization and QA
- Extractive summarization: select original sentences from source.
- Extractive method: score sentences, rank/select above threshold or top-k.
- TextRank: graph of sentences; edges by similarity; central sentences selected.
- Abstractive summarization: generates new wording not necessarily copied from source.
- Pointer-generator: can generate from vocabulary or copy tokens from source.
- Longformer attention diagram: sliding window applies to every token; global attention only selected tokens.
- In attention matrices, dark diagonal cells often represent the token attending to itself.
- QA types: extract answer span, generate answer, or retrieve evidence then answer.
- RLHF/RLAIF alignment: optimize model behavior using human/AI preference signals, often via reward models.

## Hallucination and Factuality
- Intrinsic hallucination: contradicts or distorts the provided source.
- Extrinsic hallucination: adds unsupported information not found in the source.
- If evidence says "ranked 19th" and output says "ranked 20th": intrinsic hallucination.
- If output says "has six campuses" but source never says it: extrinsic hallucination.
- Factuality checks: source entailment, retrieval verification, NLI, human annotation.
- Degeneration: repetitive/incoherent output; different from factual hallucination.

## Bias, Ethics, Evaluation
- Selection bias: training data not representative.
- Label bias: annotator labels encode subjective or social bias.
- Semantic bias: word associations reflect stereotypes.
- Bias amplification: model strengthens bias beyond data.
- Over/under-exposure: groups are shown too much/too little in outputs.
- Group fairness: compare metrics across demographic groups.
- Demographic parity: prediction independent of protected attribute.
- Counterfactual fairness: output should not change when only protected attribute changes.
- CDA: counterfactual data augmentation by swapping protected attributes.
- Annotation agreement: high Cohen's kappa means clearer label definition or better annotator consistency.

## Common Traps
- Word2Vec is not WordNet. WordNet is lexical database; Word2Vec is embedding learning method/model output.
- NLTK/spaCy are NLP libraries/toolkits; not embeddings themselves.
- Softmax is usually an output activation/probability transform; cross-entropy is the loss.
- Sigmoid is for binary/multi-label probabilities; softmax is for mutually exclusive classes.
- Transformer still uses embeddings; it does not process raw one-hot vectors directly after lookup.
- Word2Vec can mean the training algorithms and the learned embedding matrix.
- Decoder output hidden state is not a sentence; LM head + decoding converts hidden states to tokens.
- MHA option vs LM head: attention mixes contextual information; LM head predicts vocabulary distribution.
- BART is not BERT; BART is encoder-decoder, BERT is encoder-only.
- LLaMA is decoder-only.
- SYSTRAN and ELIZA are rule-based-generation-era NLP systems.

## Mock-Style Answers
- Negative sampling Boolean task: decide whether a center-context pair is real or sampled fake.
- 50% negative sampling rate: 50% of Boolean training examples are negative samples.
- LoRA `phi0`: pretrained frozen weights/base model.
- MHA code `ModuleList([... for _ in range(3)])`: three Q/K/V projection matrices.
- BERT NSP: based on `[CLS]`, not `[SEP]`.
- Parallel corpus: equivalent source-target sentence pairs.
- Model match: BERT = encoder-only; LLaMA = decoder-only; BART = encoder-decoder; Longformer = window/global attention; LoRA = adapter fine-tuning method.
- Cohen example with 4 agreements out of 7: `P_o=57.14%`; if marginals are 3/4 and 4/3, `kappa=0.16`.
