# Financial Sentiment Analysis Across Short and Long Text

Team: [Fill in team member names and student IDs]

Course: [Fill in course code and term]

Repository: `Financial sentiment classification`

## Abstract

This project studies financial sentiment analysis in two complementary settings: short-text classification for market headlines and finance posts, and long-text classification for longer financial news and transcript-style documents. The main goal is to build a reproducible finance-domain NLP workbench and compare interpretable baselines, classical machine learning, domain-specific pretrained transformers, and task-specific fine-tuning. For short text, we combine Financial PhraseBank and FiQA into a unified three-way sentiment dataset with labels `negative`, `neutral`, and `positive`. For long text, we combine the public `matthewchung74/catalyst` and `Aiera/aiera-transcript-sentiment` datasets. The implemented system includes data preparation, grouped splitting to reduce text leakage, training and evaluation pipelines, visualization, a unified Gradio demo, and a LangChain-based tool-augmented agent for interactive use.

The experiments show a clear pattern. On short text, fine-tuned DistilRoBERTa achieves the best overall performance with 0.9343 accuracy and 0.9191 macro-F1, outperforming lexicon, TF-IDF, and pretrained transformer baselines. On long text, fine-tuned FinBERT remains the strongest model with 0.7693 accuracy and 0.7235 macro-F1, substantially outperforming direct chunked inference from pretrained models. These results suggest that finance-domain pretraining is already valuable for both settings, while fine-tuning becomes especially important for long documents where document-level sentiment is harder to infer from local spans alone.

## 1. Introduction

Sentiment analysis is widely used in finance for market monitoring, headline triage, investment research support, and risk screening. However, financial sentiment is more difficult than general-domain sentiment because the polarity of a sentence often depends on context, numeric changes, forecasts, and target-specific interpretation. For example, a price cut may be negative for margin expectations but positive for sales growth, and a narrower loss may still be interpreted as an improvement.

This project investigates a practical question: how much performance improvement can be achieved by moving from interpretable baselines to finance-specific transformers and fine-tuned models in both short-text and long-text settings? Instead of focusing on a novel neural architecture, the project emphasizes a reproducible end-to-end system that supports comparison, error analysis, visualization, and demonstration.

The work makes three main contributions:

1. It builds a unified financial NLP workbench covering both short-text and long-text sentiment analysis.
2. It benchmarks multiple model families, from lexicon scoring and TF-IDF baselines to pretrained and fine-tuned transformer models.
3. It adds a tool-augmented agent and interactive Gradio interface so that the system is not only evaluable offline but also usable as a demonstrable application.

## 2. Task Definition

The primary task is three-way sentiment classification with labels:

- `negative`
- `neutral`
- `positive`

The short-text track focuses on financial headlines and short finance posts. The long-text track focuses on longer market-news documents and transcript-style text. In both cases, the output is a single document-level sentiment label.

The central research questions are:

1. How much do finance-specific pretrained transformers outperform lexicon and classical baselines?
2. Does task-specific fine-tuning further improve performance?
3. Are the best model choices the same for short text and long text?

## 3. Datasets

### 3.1 Short-Text Datasets

The short-text track uses two public datasets:

- `Financial PhraseBank`
- `FiQA Sentiment`

These datasets are complementary. Financial PhraseBank provides curated sentence-level financial sentiment annotations, while FiQA contributes finance-related text with sentiment scores that can be mapped into the same three-label scheme.

FiQA scores are converted to labels using the following rule:

- score `<= -0.1` -> `negative`
- score `>= 0.1` -> `positive`
- otherwise -> `neutral`

After schema unification and cleaning, the short-text dataset is stored with the common fields:

- `text`
- `label`
- `source`

Short-text dataset summary:

| Item | Value |
| --- | ---: |
| Total rows | 3040 |
| PhraseBank rows | 2259 |
| FiQA rows | 781 |
| Average characters per text | 109.57 |
| Average words per text | 19.77 |
| Negative | 530 |
| Neutral | 1452 |
| Positive | 1058 |
| Train | 2126 |
| Dev | 305 |
| Test | 609 |

The short-text split is grouped by exact text to reduce leakage from repeated sentences appearing across train and test.

### 3.2 Long-Text Datasets

The long-text track uses two public datasets:

- `matthewchung74/catalyst`
- `Aiera/aiera-transcript-sentiment`

The catalyst dataset contributes longer market-news style documents, while the Aiera dataset contributes financial transcript-style text. This combination produces a more professional long-document benchmark than short headline sentiment alone.

As in the short-text pipeline, the long-text data is unified into a common schema. Additional length metadata is stored for analysis:

- `char_length`
- `word_length`

Long-text dataset summary:

| Item | Value |
| --- | ---: |
| Total rows | 7174 |
| Catalyst rows | 6918 |
| Aiera rows | 256 |
| Average characters per text | 320.29 |
| Average words per text | 48.94 |
| Negative | 1074 |
| Neutral | 4459 |
| Positive | 1641 |
| Train | 5021 |
| Dev | 718 |
| Test | 1435 |

The long-text split is also grouped by exact text to reduce document leakage.

### 3.3 Preprocessing

The preprocessing pipeline includes:

- schema unification across datasets
- label normalization to the shared three-class task
- exact-text deduplication and grouped splitting
- export to local CSV for reproducibility

For long text, document-level models use a chunking strategy with:

- `max_tokens = 256`
- `overlap_tokens = 64`

This allows standard transformer backbones to process longer documents without requiring a dedicated long-context architecture.

## 4. Methods

### 4.1 Lexicon Baseline

The lexicon baseline uses a finance-domain sentiment lexicon based on the Loughran-McDonald resource. The method counts positive and negative finance terms and uses a polarity-based decision rule to produce the final label. This baseline is highly interpretable and useful for qualitative error analysis, but it cannot model compositional context, negation, or numeric reasoning well.

### 4.2 TF-IDF + Logistic Regression

The classical supervised baseline uses TF-IDF text features with Logistic Regression. For short text, this provides a strong non-neural benchmark over sentence-level headlines and posts. For long text, an analogous `tfidf_longdoc` model is used at document level.

### 4.3 Pretrained Transformer Models

The project evaluates finance-domain pretrained transformers without task-specific fine-tuning:

- `ProsusAI/finbert`
- `mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis`

For short text, these models are applied directly to the input text. For long text, they are used in chunked inference mode, where each document is split into chunks, each chunk is scored independently, and the probabilities are averaged to obtain a document-level prediction.

### 4.4 Fine-Tuned Transformer Models

The short-text track fine-tunes:

- `FinBERT`
- `DistilRoBERTa`

The long-text track fine-tunes:

- `FinBERT (LongDoc)`
- `DistilRoBERTa (LongDoc)`

For long-text fine-tuning, each document is chunked, each chunk inherits the document label during training, and document-level prediction is obtained by aggregating chunk probabilities at evaluation time. Although this is still an approximation of full document modeling, it is substantially stronger than zero-shot chunked inference from pretrained models.

Model selection uses macro-F1 because the datasets are class-imbalanced, especially toward `neutral`.

### 4.5 Tool-Augmented Agent

In addition to the main benchmark pipeline, the project implements a tool-augmented agent using LangChain for interactive use. The agent is not treated as the main benchmark model in the report. Instead, it serves as an explainability and demonstration extension.

The short-text agent integrates:

- FinBERT inference
- Loughran-McDonald lexicon scoring
- Chroma retrieval over financial headlines

The long-text agent follows the same idea, but prioritizes the fine-tuned long-text model for classification and uses retrieval over long-text examples. When an OpenAI API key is available, the tool calls can be orchestrated through LangChain; otherwise, the system falls back to deterministic tool fusion.

## 5. Experimental Setup

### 5.1 Metrics

The primary metric is:

- `Macro-F1`

Secondary metrics are:

- `Accuracy`
- `Macro Precision`
- `Macro Recall`
- per-class precision, recall, and F1

Macro-F1 is emphasized because both tracks have imbalanced label distributions, and a model that performs well on the dominant neutral class may still be weak on negative or positive classes.

### 5.2 Environment

The project is implemented in Python with a reproducible Conda environment named `NLP`. Training and evaluation are run through a unified command launcher:

- `python main.py short ...`
- `python main.py long ...`

Artifacts are organized into:

- `artifacts/shorttext/...`
- `artifacts/longtext/...`

The report-ready summary outputs are collected under:

- `output/shorttext/...`
- `output/longtext/...`

### 5.3 Reproducibility

The core experiment flow is:

```powershell
conda activate NLP

python main.py short prepare-data --dataset all
python main.py short train --model tfidf_logreg
python main.py short train --model finetuned_finbert --epochs 3 --batch-size 8
python main.py short train --model finetuned_distilroberta_financial --epochs 3 --batch-size 8
python main.py short evaluate --model lexicon
python main.py short evaluate --model tfidf_logreg
python main.py short evaluate --model finbert
python main.py short evaluate --model distilroberta_financial
python main.py short evaluate --model finetuned_finbert
python main.py short evaluate --model finetuned_distilroberta_financial
python main.py short visualize

python main.py long prepare-data --dataset all
python main.py long train --dataset merged --model tfidf_longdoc
python main.py long train --dataset merged --model finetuned_finbert_longdoc --epochs 2 --batch-size 4
python main.py long train --dataset merged --model finetuned_distilroberta_longdoc --epochs 2 --batch-size 4
python main.py long evaluate --dataset merged --model tfidf_longdoc
python main.py long evaluate --dataset merged --model finbert_chunked
python main.py long evaluate --dataset merged --model distilroberta_chunked
python main.py long evaluate --dataset merged --model finetuned_finbert_longdoc
python main.py long evaluate --dataset merged --model finetuned_distilroberta_longdoc
python main.py long visualize --dataset merged
```

## 6. Results

### 6.1 Short-Text Results

Short-text benchmark results are shown below.

| Model | Accuracy | Macro-F1 |
| --- | ---: | ---: |
| Lexicon | 0.5583 | 0.3788 |
| TF-IDF + LR | 0.7915 | 0.7527 |
| FinBERT | 0.8259 | 0.8066 |
| DistilRoBERTa | 0.8719 | 0.8603 |
| Finetuned FinBERT | 0.9048 | 0.8878 |
| Finetuned DistilRoBERTa | 0.9343 | 0.9191 |

The short-text results show a clear improvement trajectory:

- the lexicon baseline is interpretable but much weaker than learned models
- TF-IDF already provides a strong classical baseline
- finance-specific pretrained transformers outperform the classical baseline
- fine-tuning improves both transformer families
- fine-tuned DistilRoBERTa achieves the best overall short-text performance

This is an important finding because the best short-text model is not the same as the best long-text model. In the short-text setting, DistilRoBERTa achieves both strong accuracy and the highest macro-F1, suggesting an excellent efficiency-performance trade-off.

Short-text summary figure:

![Short-Text Summary](../output/shorttext/figures/model_summary_metrics.png)

Short-text per-class F1:

![Short-Text Per-Class F1](../output/shorttext/figures/per_class_f1.png)

Short-text confusion matrices:

![Short-Text Confusion Matrices](../output/shorttext/figures/confusion_matrices.png)

### 6.2 Long-Text Results

Long-text benchmark results are shown below.

| Model | Accuracy | Macro-F1 |
| --- | ---: | ---: |
| TF-IDF + LR | 0.7003 | 0.6523 |
| FinBERT (Chunked) | 0.4585 | 0.4636 |
| DistilRoBERTa (Chunked) | 0.4523 | 0.4585 |
| Finetuned FinBERT (LongDoc) | 0.7693 | 0.7235 |
| Finetuned DistilRoBERTa (LongDoc) | 0.7345 | 0.7090 |

The long-text results tell a different story:

- direct chunked inference from pretrained models is weak
- TF-IDF remains a surprisingly strong baseline for long documents
- fine-tuning is far more important in the long-text setting than in short text
- fine-tuned FinBERT is the strongest long-text model

The comparison between pretrained and fine-tuned FinBERT is especially informative:

- `FinBERT (Chunked)`: 0.4585 accuracy, 0.4636 macro-F1
- `Finetuned FinBERT (LongDoc)`: 0.7693 accuracy, 0.7235 macro-F1

This is a very large improvement and supports the claim that document-level financial sentiment cannot be handled well by naive chunked inference alone.

Long-text summary figure:

![Long-Text Summary](../output/longtext/figures/model_summary_metrics.png)

Long-text per-class F1:

![Long-Text Per-Class F1](../output/longtext/figures/per_class_f1.png)

Long-text confusion matrices:

![Long-Text Confusion Matrices](../output/longtext/figures/confusion_matrices.png)

Pretrained vs fine-tuned FinBERT on long text:

![Long-Text FinBERT Comparison](../output/longtext/figures/finbert_variant_comparison.png)

### 6.3 Cross-Track Interpretation

The most important cross-track conclusion is that model choice depends on the text regime:

- for short text, `Finetuned DistilRoBERTa` is the best model
- for long text, `Finetuned FinBERT (LongDoc)` is the best model

This indicates that the relative strengths of backbones change when the task shifts from sentence-level polarity classification to document-level sentiment inference. Short financial headlines benefit strongly from DistilRoBERTa after fine-tuning, while longer financial documents appear to favor FinBERT under the current chunk-based training setup.

## 7. Error Analysis and Discussion

The quantitative results are consistent with the qualitative behavior seen in the saved prediction and error files.

### 7.1 Short-Text Discussion

Short-text models are generally strong on the neutral class, but the negative class remains more difficult because it has the smallest support. The lexicon baseline performs particularly poorly on negative examples because financial polarity often depends on numbers, comparison, or guidance changes rather than isolated positive or negative words.

Transformer models reduce these issues substantially, and fine-tuning especially improves class balance. The best short-text model, fine-tuned DistilRoBERTa, achieves:

- negative F1: 0.8664
- neutral F1: 0.9689
- positive F1: 0.9220

This is a well-balanced result across all three labels.

### 7.2 Long-Text Discussion

The long-text setting is harder for two main reasons:

1. sentiment cues are distributed across multiple spans rather than concentrated in one sentence
2. documents often contain mixed signals, such as positive performance with weaker guidance or negative restructuring with long-term upside

The poor performance of direct pretrained chunked inference suggests that document-level sentiment cannot be recovered reliably by simple off-the-shelf local scoring. Fine-tuning on task-specific long-text data helps the model adapt to document-level label patterns.

However, long-text performance still lags short-text performance. This is expected because the current long-text approach is still based on chunking and aggregation rather than a full hierarchical or long-context architecture.

## 8. Tool-Augmented Agent and Demo

The repository includes a practical demonstration layer in addition to the offline benchmark:

- a unified Gradio application for both short-text and long-text sentiment analysis
- CLI commands for single prediction, multi-model comparison, and batch CSV inference
- a tool-augmented agent that combines model inference, lexicon scoring, and retrieval

This module is useful for:

- explainability
- qualitative inspection
- presentation and demo purposes

It is intentionally not treated as the main benchmark result in this report. The benchmark conclusions are based on the explicit `train`, `evaluate`, and `visualize` pipeline.

## 9. Limitations and Future Work

The project is complete enough for a course deliverable, but several limitations remain.

First, the long-text pipeline still relies on chunk-based document approximation. A stronger future version could explore hierarchical document models, trainable aggregation, or dedicated long-context transformers.

Second, the long-text fine-tuning strategy assigns document labels to all chunks during training. This is practical, but it introduces label noise because not every chunk expresses the same local polarity as the full document.

Third, the agent module is a system-extension feature rather than a novel modeling contribution. Its value lies in usability and interpretability, not in redefining the benchmark.

Fourth, the current report compares existing model families and fine-tuning strategies rather than proposing a new neural architecture. The project should therefore be positioned as a strong experimental and systems project, not as a new-model paper.

Future work could include:

- hierarchical long-document sentiment modeling
- multiple-instance learning for long-text supervision
- stronger aspect-aware or target-aware sentiment analysis
- expanded qualitative error analysis over numeric reasoning and mixed signals
- ablation studies on chunk size, overlap, and training schedule

## 10. Conclusion

This project demonstrates that finance-domain NLP models substantially outperform lexicon and classical baselines for financial sentiment analysis. The repository now supports both short-text and long-text workflows in a unified system, with data preparation, training, evaluation, visualization, CLI inference, Gradio demos, and tool-augmented agents.

The final conclusions are:

- fine-tuned DistilRoBERTa is the best short-text model
- fine-tuned FinBERT is the best long-text model
- fine-tuning becomes especially valuable in the long-text setting

Overall, the project satisfies the goal of building a reproducible, demonstrable, and analytically useful financial sentiment analysis system across two text regimes.

## References

1. Malo, P., Sinha, A., Korhonen, P., Wallenius, J., and Takala, P. Financial PhraseBank.
2. FiQA Sentiment dataset.
3. `matthewchung74/catalyst` dataset.
4. `Aiera/aiera-transcript-sentiment` dataset.
5. Loughran-McDonald financial sentiment lexicon.
6. `ProsusAI/finbert`.
7. `mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis`.
8. Hugging Face Transformers.
9. LangChain.
10. Chroma.

## Appendix A. Key Artifact Locations

- Short-text summary table: `output/shorttext/figures/model_metrics_summary.csv`
- Long-text summary table: `output/longtext/figures/model_metrics_summary.csv`
- Short-text metrics JSON: `output/shorttext/reports/`
- Long-text metrics JSON: `output/longtext/reports/`
- Unified app entry: `app.py`
- Unified command entry: `main.py`

