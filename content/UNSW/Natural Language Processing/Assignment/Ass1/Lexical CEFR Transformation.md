---
tags:
  - Assignment
---
### 1. Task and Framing

The task focuses on rewriting a sentence so that it matches a different CEFR level without altering its original meaning or grammatical structure. In the actual implementation, this goal was not pursued through full-sentence rewriting; instead, the system mainly operated by replacing selected individual words. This design choice emerged from repeated experimentation. When broader rewriting strategies were attempted, the resulting sentences often achieved better CEFR scores on the surface, yet the overall quality tended to deteriorate. In many cases, the outputs sounded less natural, and subtle shifts in meaning also began to appear. Against this background, the final system was designed to modify only a limited number of content words while keeping the original sentence structure intact.

Seen from an operational perspective, this solution also aligns more closely with how the system functions in practice. Rather than behaving like a human editor who rewrites a sentence holistically, the model makes controlled lexical adjustments to move the sentence closer to the target CEFR level, while minimizing the risk of inappropriate substitutions. This is also why the final outputs are typically characterized by partial simplification rather than extensive reformulation. Although such changes may appear modest, they proved to be more dependable in actual testing, especially when preserving meaning and fluency was treated as a priority.

- - -
### 2. Final Approach

The core function is **transform_sentence(sentence, source_level, target_level)**. The pipeline comprises four main stages: word difficulty estimation, candidate generation, candidate filtering/ranking and light grammatical correction.

#### 2.1 Difficulty Signal from the Training Data

From **data.csv**, I construct global statistics once and then cache them. Each word is assigned a continuous difficulty score based on how it is distributed across CEFR levels:

$$\mathrm{score}(w)=\frac{\sum_i i \cdot c_i(w)}{\sum_i c_i(w)}$$

where $c_i(w)$ is the count of word $w$ at CEFR index $i$, with A1 to C2 mapped to 0 to 5. This score is simple, but it gives a usable approximation of whether a word tends to be easier or harder in the training corpus.

I also train add-$\alpha$ smoothed bigram language models, one global and one per CEFR level:

$$P(w_t \mid w_{t-1})=\frac{\mathrm{count}(w_{t-1}, w_t)+\alpha}{\mathrm{count}(w_{t-1})+\alpha |V|}$$

While these bigram probabilities are not a strong language model, they are enough to reject many options that seem good on their own but are not good in a local context.

#### 2.2 Candidate Generation

At this stage, spaCy is used to tokenise the sentence and identify the content words (nouns, verbs, adjectives and adverbs). Most candidates originate from WordNet synsets of the root word. I retain only single-word alphabetic forms, assign them a candidate rank based on synset distance and then filter and rescore them later. 

The system also has a fallback for content words when WordNet alone is insufficient or too advanced. This fallback searches for common words in the training data and retains only those that demonstrate semantic overlap and downward CEFR movement.

#### 2.3 Semantic Filtering and Ranking

In the current version, I use a combination of word similarity and WordNet sense similarity. Verbs are given the strongest weighting in terms of sense because they are more likely to cause problems with meaning.

The core ranking scores are:

$$\mathrm{final}_{strict}=0.33\cdot \mathrm{sem}+0.44\cdot \mathrm{ctx}+0.17\cdot \mathrm{level}+0.06\cdot \mathrm{colloc}-0.05\cdot \mathrm{syn\_rank}$$

and

$$\mathrm{final}_{relaxed}=0.30\cdot \mathrm{sem}+0.25\cdot \mathrm{ctx}+0.33\cdot \mathrm{level}+0.10\cdot \mathrm{freq}+0.02\cdot \mathrm{colloc}-0.03\cdot \mathrm{syn\_rank}$$

The above are the primary ranking formulas, not the entire decision logic. They operate after several hard filters, especially for verbs. If the first-pass edits do not move the sentence enough, a second stage can add one or two extra safe candidates with positive directional gain.

#### 2.4 Morphology and Surface Repair

Candidates are inflected back into the original surface form with **pyinflect**, so the system can preserve tense or number whenever possible. I also added a small article-fix post-processing step for **a/an**. This is not sophisticated grammar correction, but it prevents some very obvious surface errors and helped stabilize the outputs.

- - -
### 3. Development

The final system was created after trying and failing many times. The main issue was with verb substitution, where earlier versions could make things simpler in terms of numbers, but also change what events meant. A case in point is the substitution of "push evaluate" for "judge" or the generation of unconventional replacements for "conducted". It was therefore necessary to impose stricter semantic filters on verb filtering than on noun or adjective filtering. This was achieved by the implementation of stronger semantic thresholds and additional sense-based checks. 

The present study also found that candidate ordering mattered. In the absence of stable sorting prior to truncation, WordNet occasionally yielded divergent results across iterations. The sorting of synsets and lemmas rectified the issue and rendered the system deterministic. 

Ultimately, broader vector-neighbour candidate pools and additional slot-style scoring for adjectivenoun and verb-object combinations were employed. The aforementioned concepts appeared to be beneficial, yet their implementation resulted in a decline in overall evaluation performance. Consequently, their removal was deemed necessary. The final system is conservative by design; it demonstrates a preference for a missed edit over a bad edit.

- - -
### 4. Evaluation

#### 4.1 How to Use

I ran the final version in my local **cefr** conda environment with:

```Python
python main.py z5518601
python evaluate.py z5518601 --tests unit_tests.csv --out_dir evaluation_outputs_unit_current_reportcheck
```

The 10-case **unit_tests.csv** file is small, but it is the provided public evaluation file and is enough to inspect whether the outputs move in the intended direction.

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

![[Pasted image 20260316002137.png]]

This is a good example of how the system usually works. While the adjective has changed, the verb 'purchased' has been kept. While the output moves in the right direction, it is still not quite an A2-style rewrite.

**Example 2: A strong local substitution**  

![[Pasted image 20260316002153.png]]

This is one of the cleaner successes. The local edit makes sense and is simpler. It's a great example of when the current system works really well.

**Example 3: Conservative no-change**  

![[Pasted image 20260316002207.png]]

While this is not the best example of simplification strength, it does demonstrate the current trade-off of the system. Although candidate verbs such as 'judge' are simpler, they change the meaning too much in this context. Therefore, the model leaves the sentence unchanged.

**Example 4: Remaining semantic weakness**  

![[Pasted image 20260316002231.png]]

There is still a problem with this sentence. Although the output moves down lexically, 'prove' is slightly stronger than 'demonstrate', meaning the two do not match perfectly. This demonstrates that, while the current filters reduce semantic drift, they do not eliminate it entirely.

- - -
### 5. Limitations

#### 5.1 Candidate Generation Is Still Narrow

Even though it has a system to fall back on if there are problems, the system still relies a lot on WordNet. This suggests that some effective ways of simplifying things may not be included in the candidate pool. For example, a verb like 'review' may be more suitable in the given situation than 'judge', but if it is not chosen early enough, the system cannot choose it.

#### 5.2 CEFR Control Is Mostly Word-Level

The system utilises a word-by-word estimation of difficulty and employs a bigram model to analyse local context. This degree of movement is sufficient for directional movement, but not for full CEFR control. It is evident that a sentence can become lexically simpler while maintaining a level of naturalness that is less pronounced in comparison to a human simplification.

#### 5.3 The Model Under-Edits Difficult Cases

The system is deliberately cautious. This reduces catastrophic semantic errors, but it also increases nochange and partial-change cases.

#### 5.4 Evaluation Still Has Gaps

The public unit tests are too small, so I still cannot say that the model performs like a human simplifier. A better future evaluation would combine CEFR control with a set of data that directly measures how well meaning is kept when things are rewritten based on a reference.

- - -
### 6. Conclusion

The final system is essentially a vocabulary-focused benchmark model. It makes many sentences easier to understand. It also avoids the awkward substitutions seen in earlier versions. These improvements came from tighter control, not from making the system more complex. I handled verbs more carefully during development. I also added stricter filters and limited the system to small, conservative edits.

This result led to an important lesson. More complicated systems do not always perform better. I tested several complex approaches, but some reduced overall quality. In some cases, the scores improved. Even so, the rewritten sentences sounded less natural. Their original meaning was also harder to preserve. That pattern shaped the final design. I stopped using methods that pushed the system toward excessive rewriting. Instead, I kept the approach simple and focused.

The most effective version combined several modest features. It used word-difficulty scores and a small set of candidate replacements. It also checked part of speech, context, and whether a simple change was enough.

This system does not fully solve CEFR-aligned rewriting. Even so, it offers a practical and fairly robust way to simplify vocabulary. Within the scope of this project, that was the most reliable outcome.
