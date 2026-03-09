---
tags:
  - Assignment
---
### 1. Task and Objective

The goal of this assignment is to transform a sentence from one CEFR level to another (e.g., A2 to B2) while preserving the original meaning and grammaticality as much as possible.  
Given three inputs, sentence, source_level, and target_level, the system should produce a revised sentence whose lexical difficulty better matches the target CEFR level.

My approach treats this as a **controlled lexical substitution** problem. It changes only selected content words (nouns, verbs, adjectives, adverbs) and leaves sentence structure mostly unchanged to avoid unnecessary errors. The objective is to balance three constraints:

1. semantic preservation,
2. contextual fluency, and
3. CEFR-level alignment.

To achieve this, the model combines dataset-driven word difficulty estimates with lexical resources (WordNet and spaCy), then ranks candidate replacements and applies only a limited number of high-confidence edits.
- - - 
### 2. Technical Details of the Approach

I implemented the system as a lexical substitution pipeline around **transform_sentence(sentence, source_level, target_level)**. The design goal was practical: change as little as possible, but make lexical difficulty move in the required CEFR direction.

The first step is to build reusable statistics from **data.csv** and cache them globally. I compute a continuous difficulty score for each word from its CEFR distribution:

$$\mathrm{score}(w)=\frac{\sum_{i} i \cdot c_i(w)}{\sum_{i} c_i(w)}$$

where \(c_i(w)\) is the frequency of word \(w\) at CEFR index \(i\) (A1 to C2 mapped to 0 to 5). This gives a corpus-based estimate of how advanced a word tends to be. I also train bigram language models (one global and one per CEFR level) with add-\(\alpha\) smoothing:

$$P(w_t \mid w_{t-1})=\frac{\mathrm{count}(w_{t-1}, w_t)+\alpha}{\mathrm{count}(w_{t-1})+\alpha |V|}$$

These probabilities are used to check whether a replacement still fits local context.

At inference time, the sentence is parsed by spaCy, and only content words (NOUN/VERB/ADJ/ADV) are considered. Candidate substitutions are collected from WordNet synsets of the lemma, then filtered to single-word alphabetic forms. To keep grammar stable, each candidate is inflected back to the original surface form using **pyinflect** (tense, number, etc.), and casing is restored.

The final decision is based on a weighted score:

$$\mathrm{final}=0.35\cdot \mathrm{sem}+0.40\cdot \mathrm{ctx}+0.25\cdot \mathrm{level}-0.05\cdot \mathrm{syn\_rank}$$

The score balances semantic similarity (**sem**), context fitness from bigrams (**ctx**), and CEFR movement (**level**). **syn_rank** is a small penalty so very remote WordNet candidates are less preferred. I run a strict pass first; if nothing acceptable is found, a relaxed pass is allowed with extra safety checks.

The main implementation challenge was semantic drift in verbs during simplification. In early versions, **conducted an experiment** could become verbs like **conveyed** or **moved**, which followed frequency signals but changed meaning. I fixed this by tightening verb constraints: stronger semantic thresholds, sense-aware checks (Lesk/Wu-Palmer when available), and a fallback that keeps the original token if no safe candidate exists.

Another issue was grammatical side effects after replacement. The common errors were article agreement (**a**/**an**) and occasional form mismatch. I added a post-processing pass for article correction and stricter POS/form filters before accepting candidates. This improved fluency without using any hand-written answer lexicon.

Overall, the final pipeline is still lightweight, but it is much more stable than the initial baseline because each scoring component has explicit guardrails against meaning loss and grammar breakage.
### 3. Experiments and Results
#### 3.1 Experimental Setup

I re-ran the current version in my local conda environment (**cefr**) with:

- python main.py z5518601 for qualitative inspection on public unit tests.
- python test.py z5518601 --tests unit_tests.csv --out_dir test_outputs_report_current for quantitative metrics.

The test file **unit_tests.csv** has 10 transfer cases, mostly downward transformations (B2/C1 to A2/B1).  
I report four metrics:

- success_rate: fraction of cases without runtime errors.
- avg_changed_ratio: proportion of changed tokens.
- avg_difficulty_shift: average lexical difficulty movement (negative = simplification).
- direction_success_rate: fraction of outputs moving in the expected CEFR direction.

#### 3.2 Quantitative Results

The refreshed run produced:

- success_rate = 1.0000 (10/10, no runtime errors)
- avg_changed_ratio = 0.1721
- avg_difficulty_shift = -0.1315
- direction_success_rate = 1.0000

My reading of these numbers is:

- Stability is strong (no crashes at all).
- Simplification is consistent but still controlled (**avg_changed_ratio** is below 0.2).
- All 10 test cases move in the expected CEFR direction in this run.

![[Pasted image 20260308015022.png]]
#### 3.3 Qualitative Examples

**Example 1 (C1 -> A2)**  
Input: _I purchased a magnificent house yesterday._  
Output: _I purchased a wonderful house yesterday._  
Discussion: This version is a clearer simplification than earlier runs because _magnificent -> wonderful_ lowers lexical difficulty without changing core meaning (**difficulty_shift = -0.1719**).

![[Pasted image 20260308015127.png]]

**Example 2 (Strong simplification, B2 -> A2)**  
Input: _He quickly realised his mistake._  
Output: _He quickly saw his mistake._  
Discussion: This is one of the strongest downward moves in the set (**difficulty_shift = -0.2599**). The verb change is simple but effective, and meaning is preserved.

![[Pasted image 20260308015305.png]]

**Example 3 (Semantic safety improvement, B2 -> A2)**  
Input: _The scientist conducted an experiment._  
Output: _The scientist did an experiment._  
Discussion: Earlier iterations sometimes produced semantic drift here (e.g., odd verb substitutions). In this run, the system chose _did_, which is simpler and semantically safe in context. This is a representative case of the new verb filtering logic working as intended.

![[Pasted image 20260308015341.png]]
#### 3.4 Result Interpretation

The pair-level breakdown is now fully consistent on unit tests: all tested source-target pairs reached **direction_success = 1.0**. The strongest average downward movement appears in **B2 -> A2** and **C1 -> A2**, which matches the intended behavior for simplification-heavy cases.

In short, the current system is stable and directionally reliable on the public test set, while still keeping edits relatively conservative rather than aggressively rewriting whole sentences.

### 4. Limitations of the Current Approach

#### 4.1 Candidate Generation and Semantic Drift

The most difficult part is still verb substitution. Even after adding semantic and sense filters, some WordNet candidates look acceptable in isolation but feel wrong in sentence-level meaning. Earlier outputs such as replacing *conducted* with *conveyed* showed this clearly. The current version blocks many of these cases, but it is still a filter-based fix rather than true semantic understanding.

#### 4.2 Imperfect CEFR Control

The CEFR signal in this system is word-centered. I estimate difficulty from level-wise word statistics and then combine that with local bigram context. This works for directional movement, but CEFR level is not only about single-word difficulty. Phrase-level naturalness, idioms, and syntax are only weakly modeled, so a sentence can score as "simpler" while still sounding less natural than a human rewrite.

#### 4.3 Limited Structural Rewriting

The pipeline is intentionally conservative: it mainly edits tokens and avoids large structural changes. This keeps grammar safer and prevents aggressive errors, but it also means some difficult cases are under-edited. When simplification really needs clause-level rewriting, the model often keeps the original structure and only makes small lexical changes.

#### 4.4 Evaluation Scope

Current evaluation is still small. The `unit_tests.csv` results are useful for debugging and iteration, but 10 cases are not enough to claim broad generalization. A stronger evaluation should include larger sets, more upward transfers (e.g., A2 -> B2/C1), and more varied domains to test whether the same strategy remains stable outside the provided examples.

### 5. Conclusion

This assignment shows that a lightweight lexical pipeline can still produce stable CEFR transfer when the constraints are designed carefully. On the provided unit tests, the system runs without runtime failures and usually moves sentences in the expected direction, while avoiding excessive rewriting.

The key lesson from implementation was that difficulty signals alone are not enough. Early versions could simplify words but sometimes damaged meaning (especially for verbs). The final version became more reliable after I added stricter semantic checks, sense-aware filtering, and post-edit grammar fixes such as article correction. At the same time, the method is still word-level and conservative, so it is best viewed as a practical baseline rather than a complete rewriting system. The next step is larger-scale evaluation and stronger sentence-level modeling for more natural outputs.
