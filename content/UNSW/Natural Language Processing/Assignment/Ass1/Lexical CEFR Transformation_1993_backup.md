---
tags:
  - Assignment
---
### 1. Task and Framing

The task requires the transformation of sentences between Common European Framework of Reference for Languages (CEFR) levels, whilst preserving the integrity of meaning and grammar to the greatest extent possible. In practice, the approach adopted was to treat this as a controlled lexical substitution task rather than a full rewriting. An initial approach involved broader rewriting ideas, but these generally resulted in more unfavourable trade-offs. Specifically, the sentence moved more in CEFR score, but the output became awkward or semantically off. Consequently, the final system edits a limited number of content words and preserves the original structure in its majority.

This framing of the project engendered a sense of authenticity. The model does not aspire to "rewrite like a human editor". The objective is to simplify or enhance the direction of a sentence through local edits, while maintaining a conservative approach when the replacement appears to be a potential risk. This design choice elucidates many of the final outputs: some are merely partial simplifications, but they are generally considered to be safer than an aggressive rewrite.

- - -
### 2. Final Approach

The core function is **transform_sentence(sentence, source_level, target_level)**. The pipeline has four main parts: word difficulty estimation, candidate generation, candidate filtering/ranking, and light grammatical repair.

#### 2.1 Difficulty Signal from the Training Data

From the data contained in the file named "data.csv", I construct global statistics on a single occasion and then cache them. Each word is assigned a continuous difficulty score based on its position across the CEFR levels:

$$\mathrm{score}(w)=\frac{\sum_i i \cdot c_i(w)}{\sum_i c_i(w)}$$

where $c_i(w)$ is the count of word $w$ at CEFR index $i$, with A1 to C2 mapped to 0 to 5. This score is simple, but it gives a usable approximation of whether a word tends to be easier or harder in the training corpus.

I also train add-$\alpha$ smoothed bigram language models, one global and one per CEFR level:

$$P(w_t \mid w_{t-1})=\frac{\mathrm{count}(w_{t-1}, w_t)+\alpha}{\mathrm{count}(w_{t-1})+\alpha |V|}$$

While these bigram probabilities do not constitute a robust language model, they are sufficient to reject numerous alternatives that appear satisfactory when considered in isolation but are deemed inadequate within a local context.

#### 2.2 Candidate Generation

At inference time, the spaCy framework is employed to tokenize the sentence and identify candidate content words (NOUN, VERB, ADJ, ADV). The majority of candidates are derived from WordNet synsets of the lemma. The approach adopted involves the maintenance of single-word alphabetic forms, with subsequent ranking according to synset distance. The system incorporates a corpus-driven fallback mechanism for content words, which is invoked when WordNet alone is inadequate or too sophisticated. The fallback function performs searches for frequently occurring words in the training data, and retains only those candidates that demonstrate both semantic overlap and downward CEFR movement.

This component underwent significant modifications during the developmental process. The implementation of a pure WordNet pipeline was uncomplicated; however, it failed to incorporate numerous beneficial substitutions and, on occasion, yielded unconventional results. The incorporation of a corpus-based fallback mechanism has been demonstrated to enhance recall, a phenomenon that manifests only when the approach is maintained at a conservative level. Initially, the prospect of more assertive candidate expansion appeared to be a potentially beneficial strategy. However, subsequent analysis has revealed that this approach often results in an increase in semantic drift rather than contributing to the enhancement of the system's functionality.

#### 2.3 Semantic Filtering and Ranking

The code does not rely on a single neat formula. The decision-making process is a multifaceted one, involving a series of complex filters and a subsequent ranking score. A significant modification that occurred during the developmental process was the decision to cease reliance on the utilisation of spaCy vector similarity exclusively. In the current version of the model, a combination of vector similarity with WordNet sense similarity is employed, with verbs receiving the strongest sense weighting due to their propensity to induce semantic issues.

The core ranking scores are:

$$\mathrm{final}_{strict}=0.33\cdot \mathrm{sem}+0.44\cdot \mathrm{ctx}+0.17\cdot \mathrm{level}+0.06\cdot \mathrm{colloc}-0.05\cdot \mathrm{syn\_rank}$$

and

$$\mathrm{final}_{relaxed}=0.30\cdot \mathrm{sem}+0.25\cdot \mathrm{ctx}+0.33\cdot \mathrm{level}+0.10\cdot \mathrm{freq}+0.02\cdot \mathrm{colloc}-0.03\cdot \mathrm{syn\_rank}$$

The above are the primary ranking formulas, not the entire decision logic. In the actual code, these words are obscured by several layers of complex filters, particularly in the context of verb and noun substitutions. Should the initial edits prove ineffective in sufficiently advancing the sentence towards the desired level, a subsequent stage may involve the addition of one or two additional safe candidates that demonstrate positive directional gain.

#### 2.4 Morphology and Surface Repair

Candidates are inflected back into the original surface form with **pyinflect**, so the system can preserve tense or number whenever possible. I also added a small article-fix post-processing step for **a/an**. This is not sophisticated grammar correction, but it prevents some very obvious surface errors and helped stabilize the outputs.

### 3. Development

The final system was derived from multiple unsuccessful iterations. The most significant issue encountered pertained to verb substitution, where earlier iterations had the capacity to simplify numerically while concomitantly altering the semantics of events. A case in point is the substitution of "push evaluate" for "judge" or the generation of unconventional replacements for "conducted". It was therefore necessary to impose stricter semantic filters on verb filtering than on noun or adjective filtering. This was achieved by the implementation of stronger semantic thresholds and additional sense-based checks.

The present study also found that candidate ordering mattered. In the absence of stable sorting prior to truncation, WordNet occasionally yielded divergent results across iterations. The sorting of synsets and lemmas rectified the issue and rendered the system deterministic.

Ultimately, broader vector-neighbour candidate pools and additional slot-style scoring for adjective-noun and verb-object combinations were employed. The aforementioned concepts appeared to be beneficial, yet their implementation resulted in a decline in overall evaluation performance. Consequently, their removal was deemed necessary. The final system is conservative by design; it demonstrates a preference for a missed edit over a bad edit.

### 4. Evaluation

#### 4.1 Setup

I ran the final version in my local **cefr** conda environment with:

```Python
python main.py z5518601
python evaluate.py z5518601 --tests unit_tests.csv --out_dir evaluation_outputs_unit_current_reportcheck
```

The 10-case **unit_tests.csv** file is small, but it is the provided public evaluation file and is enough to inspect whether the system is moving outputs in the intended lexical direction.

#### 4.2 Public Unit Test Results

The current run on **unit_tests.csv** produced:

```TXT
success_rate = 1.0000
avg_changed_ratio = 0.1579
avg_difficulty_shift = -0.1209
direction_success_rate = 0.9000
no_change_rate = 0.1000
```

These results show a cautious system: it usually simplifies in the correct direction, but it does not force a change in every case.

#### 4.3 Qualitative Examples

**Example 1: Partial but safe simplification**  
Input: _I purchased a magnificent house yesterday._  
Output: _I purchased a wonderful house yesterday._  
This is a good illustration of the system's general behaviour. The adjective change is reasonable and simpler, but the verb *purchased* remains. So the sentence moves in the right direction without fully reaching an A2-style rewrite.

**Example 2: A strong local substitution**  
Input: _He quickly realised his mistake._  
Output: _He quickly saw his mistake._  
This is one of the cleaner successes. The edit is local, semantically close, and clearly simpler. Cases like this are where the current system works best.

**Example 3: Conservative no-change**  
Input: _The committee will evaluate the proposal tomorrow._  
Output: _The committee will evaluate the proposal tomorrow._  
This is not a success in terms of simplification strength, but it is a useful example of the system's current trade-off. Candidate verbs such as *judge* are simpler, but in this context they shift the meaning too much. The model therefore prefers no change.

**Example 4: Remaining semantic weakness**  
Input: _The results demonstrate a significant improvement._  
Output: _The results prove a large improvement._  
This sentence still exposes a limitation. The output moves downward lexically, but *prove* is slightly stronger than *demonstrate*, so the semantic match is not ideal. This shows that the current filters reduce semantic drift but do not eliminate it.

### 5. Limitations

#### 5.1 Candidate Generation Is Still Narrow

Despite incorporating a corpus-driven fallback mechanism, the system continues to demonstrate a significant reliance on WordNet. This suggests that certain effective contextual simplifications may not be included in the candidate pool. For instance, a verb like 'review' may be more suitable in context than 'judge', but if it is not generated early enough, the system cannot choose it.

#### 5.2 CEFR Control Is Mostly Word-Level

The system utilises a word-by-word estimation of difficulty and employs a bigram model to analyse local context. This degree of movement is sufficient for directional movement, but not for full CEFR control. It is evident that a sentence can become lexically simpler while maintaining a level of naturalness that is less pronounced in comparison to a human simplification.

#### 5.3 The Model Under-Edits Difficult Cases

The system is deliberately cautious. This reduces catastrophic semantic errors, but it also increases no-change and partial-change cases. The CEFR-SP results make that clear: the model is reliable as a directional lexical baseline, but it is not strong at forcing difficult sentences all the way into the target band.

#### 5.4 Evaluation Still Has Gaps

The public unit tests are too small, and CEFR-SP is not a gold simplification dataset. So even though the evaluation is better than before, I still cannot claim that the model performs like a human simplifier. A stronger future evaluation would combine CEFR control with a dataset that directly measures meaning preservation against reference rewrites.

### 6. Conclusion

The final system is best understood as a cautious lexical baseline. It can move many sentences in the required CEFR direction, and it avoids a large number of the bad substitutions that appeared in earlier versions. The main gains came from tightening verb semantics, adding better filtering, and accepting that conservative editing was better than aggressive but wrong rewriting.

The most useful lesson from this assignment was not that a more complicated pipeline always wins. In fact, several more elaborate ideas hurt performance and had to be removed. What worked better was a smaller system with explicit guardrails: word difficulty estimates, constrained candidate generation, POS-specific semantic filters, local context checks, and light grammatical repair. That does not solve CEFR-aware rewriting in a complete sense, but it does produce a defensible and reasonably stable lexical simplification system.
