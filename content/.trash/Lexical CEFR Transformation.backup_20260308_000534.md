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

I implemented the system as a lexical substitution pipeline around `transform_sentence(sentence, source_level, target_level)`. The design goal was practical: change as little as possible, but make lexical difficulty move in the required CEFR direction.

The first step is to build reusable statistics from `data.csv` and cache them globally. I compute a continuous difficulty score for each word from its CEFR distribution:

$$\mathrm{score}(w)=\frac{\sum_{i} i \cdot c_i(w)}{\sum_{i} c_i(w)}$$

where \(c_i(w)\) is the frequency of word \(w\) at CEFR index \(i\) (A1 to C2 mapped to 0 to 5). This gives a corpus-based estimate of how advanced a word tends to be. I also train bigram language models (one global and one per CEFR level) with add-\(\alpha\) smoothing:

$$P(w_t \mid w_{t-1})=\frac{\mathrm{count}(w_{t-1}, w_t)+\alpha}{\mathrm{count}(w_{t-1})+\alpha |V|}$$

These probabilities are used to check whether a replacement still fits local context.

At inference time, the sentence is parsed by spaCy, and only content words (NOUN/VERB/ADJ/ADV) are considered. Candidate substitutions are collected from WordNet synsets of the lemma, then filtered to single-word alphabetic forms. To keep grammar stable, each candidate is inflected back to the original surface form using `pyinflect` (tense, number, etc.), and casing is restored.

The final decision is based on a weighted score:

$$\mathrm{final}=0.35\cdot \mathrm{sem}+0.40\cdot \mathrm{ctx}+0.25\cdot \mathrm{level}-0.05\cdot \mathrm{syn\_rank}$$

The score balances semantic similarity (`sem`), context fitness from bigrams (`ctx`), and CEFR movement (`level`). `syn_rank` is a small penalty so very remote WordNet candidates are less preferred. I run a strict pass first; if nothing acceptable is found, a relaxed pass is allowed with extra safety checks.

The main implementation challenge was semantic drift in verbs during simplification. In early versions, **conducted an experiment** could become verbs like **conveyed** or **moved**, which followed frequency signals but changed meaning. I fixed this by tightening verb constraints: stronger semantic thresholds, sense-aware checks (Lesk/Wu-Palmer when available), and a fallback that keeps the original token if no safe candidate exists.

Another issue was grammatical side effects after replacement. The common errors were article agreement (`a`/`an`) and occasional form mismatch. I added a post-processing pass for article correction and stricter POS/form filters before accepting candidates. This improved fluency without using any hand-written answer lexicon.

Overall, the final pipeline is still lightweight, but it is much more stable than the initial baseline because each scoring component has explicit guardrails against meaning loss and grammar breakage.
### 3. Experiments and Results
#### 3.1 Experimental Setup

I evaluated the system in a local conda environment (cefr) using:

- python main.py z5518601 for qualitative inspection on public unit tests.
- python test.py z5518601 --tests unit_tests.csv --out_dir test_outputs_final_unit for quantitative metrics.

The public test set (unit_tests.csv) contains 10 sentence-level CEFR transfer cases (mostly downward transfers such as B2/C1 to A2/B1).  
I report four metrics:

- success_rate: fraction of cases without runtime errors.
- avg_changed_ratio: proportion of changed tokens.
- avg_difficulty_shift: average lexical difficulty movement (negative = simplification).
- direction_success_rate: fraction of outputs moving in the expected CEFR direction.

#### 3.2 Quantitative Results

On unit_tests.csv, the final system achieved:

- success_rate = 1.0000 (10/10, no runtime errors)
- avg_changed_ratio = 0.1888
- avg_difficulty_shift = -0.1009
- direction_success_rate = 0.9000

These numbers indicate that the method is stable and generally performs controlled simplification while avoiding excessive rewriting.

![[Pasted image 20260307230734.png]]

#### 3.3 Qualitative Examples

**Example 1 (C1 -> A2)**  
Input: _I purchased a magnificent house yesterday._  
Output: _I purchased an impressive home yesterday._  
Discussion: The model simplified one noun phrase (_house -> home_) and corrected article agreement (_a -> an_ before _impressive_). The sentence remains grammatical and close in meaning, though simplification strength is moderate.

![[Pasted image 20260307230925.png]]

**Example 2 (B2 -> A2)**  
Input: _The scientist conducted an experiment._  
Output: _The scientist did an experiment._  
Discussion: A previous version produced semantically drifted verbs (e.g., _conveyed/moved_). The final version adds a context-sensitive verb filter and keeps a simpler but semantically safer replacement.

![[Pasted image 20260307231023.png]]

**Example 3 (C1 -> B1)**  
Input: _The committee will evaluate the proposal tomorrow._  
Output: _The committee will judge the proposal tomorrow._  
Discussion: The replacement preserves the core meaning and reduces lexical complexity.

![[Pasted image 20260307231043.png]]
#### 3.4 Result Interpretation

Overall, the system shows a good trade-off between lexical control and meaning preservation. The model is robust (no crashes) and directionally correct in most cases (90%). Remaining errors are mainly due to limited candidate quality for some words, where stronger simplification may conflict with semantic precision.

### 4. Limitations of the Current Approach

#### 4.1 Candidate Generation and Semantic Drift

Although the system is stable on the unit tests, candidate quality is still a bottleneck. The model depends heavily on WordNet for substitution proposals, so performance is bounded by WordNet coverage and sense granularity. For some verbs and abstract words, candidates can be semantically close in embedding space but still wrong in event meaning. The sense-based filter reduces this problem, but it does not eliminate it.

#### 4.2 Imperfect CEFR Control

CEFR difficulty is estimated from corpus-level word distributions and combined with local bigram context. This gives useful directional control, but CEFR complexity is not purely lexical. Collocations, idiomatic usage, and syntax also affect readability. As a result, some outputs move toward the target level numerically while still sounding less natural than human rewriting.

#### 4.3 Limited Structural Rewriting

The system is intentionally conservative because it mainly performs token-level substitution with light post-processing. It can fix local issues such as article agreement, but it does not do full sentence restructuring. When simplification requires structural change, the model may keep the original word instead of making a risky replacement.

#### 4.4 Evaluation Scope

Evaluation is still limited in scale. Results on `unit_tests.csv` are useful for debugging and comparison, but stronger evidence would require larger and more diverse CEFR transfer sets, especially for upward transfer and domain-specific text.

### 5. Conclusion

This project implemented a CEFR lexical transformation system using a hybrid pipeline: corpus-based difficulty scoring, smoothed bigram language modeling, WordNet candidate generation, and embedding-based semantic filtering with spaCy. The final model is robust on the provided unit tests (100% runtime success) and usually moves outputs in the intended CEFR direction while keeping edits controlled.

The main engineering focus was balancing simplification strength and meaning preservation. Through iterative refinement, I reduced common failure modes such as semantic drift in verb substitution and local grammatical errors after replacement. Although the method remains limited by lexical resources and does not perform full syntactic rewriting, it provides a practical and interpretable baseline for CEFR-aware text transformation. Future work should prioritize broader evaluation and stronger context-sensitive candidate generation for more natural outputs.

