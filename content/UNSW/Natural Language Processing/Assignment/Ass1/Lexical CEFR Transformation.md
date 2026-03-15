---
tags:
  - Assignment
---
### 1. Task and Objective

The goal of this assignment is to transform a sentence from one CEFR level to another (e.g., A2 to B2) while preserving meaning and grammaticality as much as possible.  
Given the three inputs `sentence`, `source_level`, and `target_level`, the system should output a revised sentence whose lexical difficulty moves toward the target level.

I framed the task as a **controlled lexical substitution** problem instead of full sentence rewriting. This was mainly a practical decision: with the provided training data and the unit-test style evaluation, aggressive rewriting created more grammatical errors than useful CEFR movement. In the final system I therefore edit only a small number of content words (nouns, verbs, adjectives, adverbs) and keep the original sentence structure unless there is a clear benefit. The design tries to balance three constraints:

1. semantic preservation,
2. contextual fluency, and
3. CEFR-level alignment.

To achieve this, the system combines corpus-based word difficulty estimates, WordNet candidate generation, spaCy analysis, and local language-model checks. Replacements are only applied when they improve CEFR direction without causing obvious semantic or grammatical damage.
- - - 
### 2. Technical Details of the Approach

I implemented the system as a lexical substitution pipeline around **transform_sentence(sentence, source_level, target_level)**. The design goal was practical: change as little as possible, but make lexical difficulty move in the required CEFR direction.

The first step is to build reusable statistics from **data.csv** and cache them globally. I compute a continuous difficulty score for each word from its CEFR distribution:

$$\mathrm{score}(w)=\frac{\sum_{i} i \cdot c_i(w)}{\sum_{i} c_i(w)}$$

where \(c_i(w)\) is the frequency of word \(w\) at CEFR index \(i\) (A1 to C2 mapped to 0 to 5). This gives a corpus-based estimate of how advanced a word tends to be. I also train bigram language models (one global and one per CEFR level) with add-\(\alpha\) smoothing:

$$P(w_t \mid w_{t-1})=\frac{\mathrm{count}(w_{t-1}, w_t)+\alpha}{\mathrm{count}(w_{t-1})+\alpha |V|}$$

These probabilities are used to check whether a replacement still fits local context.

At inference time, the sentence is parsed by spaCy, and only content words (NOUN/VERB/ADJ/ADV) are considered. Candidate substitutions are collected from WordNet synsets of the lemma, then filtered to single-word alphabetic forms. To keep grammar stable, each candidate is inflected back to the original surface form using **pyinflect** (tense, number, etc.), and casing is restored.

The final decision is not a single fixed formula in the code. Instead, I use a **strict mode** and a **relaxed mode** with different weights. In strict mode, context fit is weighted slightly more than level movement:

$$\mathrm{final}_{strict}=0.33\cdot \mathrm{sem}+0.44\cdot \mathrm{ctx}+0.17\cdot \mathrm{level}+0.06\cdot \mathrm{colloc}-0.05\cdot \mathrm{syn\_rank}$$

If strict filtering finds nothing acceptable, the system switches to a relaxed mode that gives more weight to CEFR movement and token frequency:

$$\mathrm{final}_{relaxed}=0.30\cdot \mathrm{sem}+0.25\cdot \mathrm{ctx}+0.33\cdot \mathrm{level}+0.10\cdot \mathrm{freq}+0.02\cdot \mathrm{colloc}-0.03\cdot \mathrm{syn\_rank}$$

This two-stage design reflects what happened during debugging. A neat single score looked cleaner in a report, but in practice it was not enough. Different POS types needed different semantic thresholds, and verbs were clearly the hardest case. In early versions, **conducted an experiment** could become verbs like **conveyed** or **moved**, which followed distributional signals but changed the event meaning. I therefore tightened verb-specific checks, especially when a verb is followed by an article, and added sense-based filtering before allowing strong simplifications.

Another recurring issue was grammatical side effects after replacement. The most common ones were article agreement (**a**/**an**) and occasional form mismatch after inflection. I added a post-processing step for article correction and stricter surface-form checks before accepting a candidate. This does not solve every fluency problem, but it reduced several obvious errors in the public test cases.

Overall, the final pipeline is still lightweight, but it is much more stable than the initial baseline because each scoring component has explicit guardrails against meaning loss and grammar breakage.
### 3. Experiments and Results
#### 3.1 Experimental Setup

I re-ran the current version in my local conda environment (**cefr**) with:

- python main.py z5518601 for qualitative inspection on public unit tests.
- python test.py z5518601 --tests unit_tests.csv --out_dir test_outputs_report_current for quantitative metrics.

The test file **unit_tests.csv** has 10 transfer cases, and all of them are downward transformations (B1/B2/C1 to A2/B1).  
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

- The current pipeline is operationally stable on this small test set because it completed all 10 cases without runtime errors.
- Simplification is present but conservative: **avg_changed_ratio** is below 0.2, so the system usually changes only one or two words.
- All 10 outputs move in the expected direction in this run, but this should be read as a public-test result rather than evidence of broad robustness.

![[Pasted image 20260308015022.png]]
#### 3.3 Qualitative Examples

**Example 1 (C1 -> A2)**  
Input: _I purchased a magnificent house yesterday._  
Output: _I purchased a wonderful house yesterday._  
Discussion: This is a useful example because it shows both a success and a limitation. The change _magnificent -> wonderful_ lowers lexical difficulty without distorting the sentence (**difficulty_shift = -0.1719**), but the verb _purchased_ remains untouched. So the output does move downward, yet it is still only a partial simplification rather than a full A2-style rewrite.

![[Pasted image 20260308015127.png]]

**Example 2 (Strong simplification, B2 -> A2)**  
Input: _He quickly realised his mistake._  
Output: _He quickly saw his mistake._  
Discussion: This is one of the strongest downward moves in the set (**difficulty_shift = -0.2599**). The verb change is simple and the sentence remains natural, so this is the type of substitution the system handles best: one local edit with clear semantic overlap and clear CEFR gain.

![[Pasted image 20260308015305.png]]

**Example 3 (Semantic safety improvement, B2 -> A2)**  
Input: _The scientist conducted an experiment._  
Output: _The scientist did an experiment._  
Discussion: Earlier iterations sometimes produced semantic drift here (e.g., odd verb substitutions). In this run, the system chose _did_, which is simpler and semantically safe in context. It is not the most elegant paraphrase, but it is a better trade-off than a more specific verb with the wrong meaning. This example captures how the final system often prefers safety over stylistic richness.

![[Pasted image 20260308015341.png]]
#### 3.4 Result Interpretation

On the public unit tests, the system is consistently moving outputs in the intended direction. The strongest downward effects appear in the larger-gap simplification settings such as **B2 -> A2** and **C1 -> A2**, which is where the scoring function has the most room to reward simpler candidates.

At the same time, these results should be interpreted carefully. The evaluation set is small, all cases are simplification tasks, and several successes are only partial simplifications rather than full target-level rewrites. So the main claim I can support here is directional control with conservative editing, not complete CEFR conversion in a human-like sense.

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

This assignment shows that a lightweight lexical pipeline can produce useful CEFR movement when the constraints are tuned carefully. On the provided public unit tests, the system runs without runtime failures and pushes every case in the expected direction, but it usually does so through small local edits rather than full rewriting.

The main lesson from building it was that word difficulty alone is a weak signal. The system became noticeably more reliable only after I added POS-specific thresholds, extra verb checks, and post-edit grammar repair. Even then, the output quality is best described as cautious: when the model is uncertain, it prefers keeping the original token or making only a partial simplification. For that reason, I see the final system as a controlled lexical baseline with good debugging value, not as a complete solution to CEFR-aware rewriting. A better next step would be evaluation on more diverse transfers, especially upward transfer, plus stronger sentence-level modeling.
