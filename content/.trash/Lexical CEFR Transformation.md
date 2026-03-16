---
tags:
  - Assignment
---
### 1. Task and Framing

The task requires the transformation of sentences between CEFR levels while maintaining semantic integrity. The approach adopted in this case was to treat the problem as a controlled lexical substitution problem rather than a full rewriting. Initial experiments involving broader rewriting frequently resulted in a more pronounced CEFR shift; however, the outputs were often less natural and occasionally semantically inaccurate. The final system is thus employed to edit only a limited number of content words, whilst preserving the original sentence structure, unless a replacement is clearly beneficial.

It is important to note that the sole purpose of the data.csv file is to estimate word difficulty and to construct contextual statistics.
In this study, the CEFR is approached as a lexical difficulty signal rather than a comprehensive model of grammar or discourse complexity.
In instances where the preservation of meaning is uncertain, it is preferable to replace fewer words, as opposed to undertaking extensive rewriting.
In the event that no candidate is both simpler and semantically safe, it is acceptable to retain the original word.

- - -
### 2. Final Approach

The core function is **transform_sentence(sentence, source_level, target_level)**. The pipeline has four main parts: word difficulty estimation, candidate generation, candidate filtering/ranking, and light grammatical repair.

#### 2.1 Difficulty Signal from the Training Data

From **data.csv**, I build global statistics once and cache them. Each word gets a continuous difficulty score based on where it appears across CEFR levels:

$$\mathrm{score}(w)=\frac{\sum_i i \cdot c_i(w)}{\sum_i c_i(w)}$$

where $c_i(w)$ is the count of word $w$ at CEFR index $i$, with A1 to C2 mapped to 0 to 5. This gives a simple corpus-based estimate of lexical difficulty.

I also train add-$\alpha$ smoothed bigram language models, one global and one per CEFR level:

$$P(w_t \mid w_{t-1})=\frac{\mathrm{count}(w_{t-1}, w_t)+\alpha}{\mathrm{count}(w_{t-1})+\alpha |V|}$$

The bigram models are simple, but they are enough to reject many replacements that look plausible in isolation and bad in context.

#### 2.2 Candidate Generation

At inference time, spaCy identifies content words (NOUN, VERB, ADJ, ADV). Most candidates come from WordNet synsets of the lemma, filtered to single-word alphabetic forms. I also use a conservative corpus-driven fallback: frequent words from the training data are considered only if they show semantic overlap and clear CEFR movement. This was added because a pure WordNet pipeline often missed useful substitutions.

#### 2.3 Semantic Filtering and Ranking

The decision process is a combination of hard filters and then a ranking score. One important change during development was to stop relying only on spaCy vector similarity. The current version mixes vector similarity with WordNet sense similarity, with the strongest sense weighting on verbs because they caused the most semantic errors. Candidates are then filtered by semantic thresholds, CEFR direction checks, local context, and collocation strength.

Once a candidate passes these filters, it is ranked in **strict** or **relaxed** mode. The core ranking scores are:

$$\mathrm{final}_{strict}=0.33\cdot \mathrm{sem}+0.44\cdot \mathrm{ctx}+0.17\cdot \mathrm{level}+0.06\cdot \mathrm{colloc}-0.05\cdot \mathrm{syn\_rank}$$

and

$$\mathrm{final}_{relaxed}=0.30\cdot \mathrm{sem}+0.25\cdot \mathrm{ctx}+0.33\cdot \mathrm{level}+0.10\cdot \mathrm{freq}+0.02\cdot \mathrm{colloc}-0.03\cdot \mathrm{syn\_rank}$$

These are the main ranking formulas, not the whole decision logic. They operate after several hard filters, especially for verbs. If the first-pass edits do not move the sentence enough, a second stage can add one or two extra safe candidates with positive directional gain.

#### 2.4 Morphology and Surface Repair

Candidates are inflected back into the original surface form with **pyinflect** so that tense and number are preserved where possible. I also added a small **a/an** post-processing step to catch obvious surface errors.

### 3. Development

The final system was derived from multiple unsuccessful iterations. The most significant issue encountered pertained to verb substitution, where earlier iterations had the capacity to simplify numerically while concomitantly altering the semantics of events. A case in point is the substitution of "push evaluate" for "judge" or the generation of unconventional replacements for "conducted". It was therefore necessary to impose stricter semantic filters on verb filtering than on noun or adjective filtering. This was achieved by the implementation of stronger semantic thresholds and additional sense-based checks.

The present study also found that candidate ordering mattered. In the absence of stable sorting prior to truncation, WordNet occasionally yielded divergent results across iterations. The sorting of synsets and lemmas rectified the issue and rendered the system deterministic.

Ultimately, broader vector-neighbour candidate pools and additional slot-style scoring for adjective-noun and verb-object combinations were employed. The aforementioned concepts appeared to be beneficial, yet their implementation resulted in a decline in overall evaluation performance. Consequently, their removal was deemed necessary. The final system is conservative by design; it demonstrates a preference for a missed edit over a bad edit.

### 4. Evaluation

#### 4.1 Setup

I ran the final version in my local **cefr** conda environment with:

```python
python main.py z5518601
python evaluate.py z5518601 --tests unit_tests.csv --out_dir evaluation_outputs_unit_current_reportcheck
```

The 10-case **unit_tests.csv** file is small, but it is the provided public evaluation file and is enough to inspect whether the system is moving outputs in the intended lexical direction.

#### 4.2 Public Unit Test Results

The current run on **unit_tests.csv** produced:

```txt
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

![[Pasted image 20260316002137.png]]

This is typical of the final system. The adjective becomes simpler, but the verb *purchased* remains, so the sentence moves downward only partially.

**Example 2: A strong local substitution**  
Input: _He quickly realised his mistake._  
Output: _He quickly saw his mistake._  

![[Pasted image 20260316002153.png]]

This is one of the cleaner successes: the replacement is local, semantically close, and clearly simpler.

**Example 3: Conservative no-change**  
Input: _The committee will evaluate the proposal tomorrow._  
Output: _The committee will evaluate the proposal tomorrow._  

![[Pasted image 20260316002207.png]]

This example shows the main trade-off in the final system. The model can see simpler verb candidates, but they are not safe enough semantically. In this sentence, replacing *evaluate* with something like *judge* would simplify the word, but it would also shift the meaning. The system therefore prefers no change.

**Example 4: Remaining semantic weakness**  
Input: _The results demonstrate a significant improvement._  
Output: _The results prove a large improvement._  

![[Pasted image 20260316002231.png]]

This is a useful failure case. The output does move downward lexically because *significant* becomes *large*, but *prove* is slightly stronger than *demonstrate*. So the sentence is not completely wrong, yet it still shows that the current filtering is better at blocking very bad substitutions than at guaranteeing the best one.

### 5. Limitations

#### 5.1 Candidate Generation Is Still Narrow

Even with the corpus-driven fallback, the system still depends heavily on WordNet. Some good contextual options never enter the candidate pool. For example, *review* may be a better fit than *judge* for *evaluate the proposal*, but the system cannot pick it if it is not generated.

#### 5.2 CEFR Control Is Mostly Word-Level

The system estimates difficulty word by word and checks only local bigram context. That is enough for directional movement, but not for full CEFR control.

#### 5.3 The Model Under-Edits Difficult Cases

The system is deliberately cautious. This reduces catastrophic semantic errors, but it also increases no-change and partial-change cases.

#### 5.4 Evaluation Still Has Gaps

The public unit tests are useful for debugging, but they are too small to support broad claims about generalization.

### 6. Conclusion

The final system can be best understood as a cautious lexical baseline. The tool has been demonstrated to facilitate the progression of numerous sentences in the required CEFR direction, while simultaneously circumventing a multitude of erroneous substitutions that were prevalent in earlier iterations. The primary gains were derived from the tightening of verb semantics, the incorporation of more robust filtering mechanisms, and the acknowledgement that conservative editing is preferable to aggressive but erroneous rewriting.

The primary conclusion derived from the assignment is that the introduction of additional machinery did not inherently enhance the efficacy of the model. A smaller pipeline incorporating explicit guardrails, difficulty estimates, constrained candidates, semantic filters, local context checks and light grammatical repair was found to be more reliable than several more ambitious variants.
