---
tags:
  - Assignment
---
### 1. Task and Objective

The goal of this assignment is to transform a sentence from one CEFR level to another (e.g., A2 to B2) while preserving the original meaning and grammaticality as much as possible.  
Given three inputs, sentence, source_level, and target_level, the system should produce a revised sentence whose lexical difficulty better matches the target CEFR level.

My approach treats this as a **controlled lexical substitution** problem. It changes only selected content words (nouns, verbs, adjectives, adverbs) and leaves sentence structure mostly unchanged to avoid unnecessary errors. The objective is to balance three constraints:

1. semantic preservation,
2. contextual fluency, and
3. CEFR-level alignment.

To achieve this, the model combines dataset-driven word difficulty estimates with lexical resources (WordNet and spaCy), then ranks candidate replacements and applies only a limited number of high-confidence edits.
- - - 
### 2. Technical Details of the Approach

The system is implemented as a hybrid lexical substitution pipeline centered on the required function transform_sentence(sentence, source_level, target_level).

At initialization, resources are built once and cached globally (_get_resources) to avoid repeated preprocessing. The code loads data.csv and checks required columns (text, cefr_level). It then constructs two key statistics:

1. **Word difficulty profile** from the training data.  
    For each word, counts are collected across CEFR levels (A1..C2 mapped to indices 0..5). A continuous difficulty score is computed as:

$$\mathrm{score}(w)=\frac{\sum_{i} i \cdot c_i(w)}{\sum_{i} c_i(w)}$$

where ci(w)ci​(w) is the count of word ww at CEFR index ii.  
This gives a data-driven estimate of lexical difficulty.

2. **Language-model context statistics** (bigram models).  
    The method builds both:
    - a global bigram model over all data, and
    - one bigram model per CEFR level.  
        Probability is estimated with add-αα smoothing (α=0.1α=0.1):

$$P(w_t \mid w_{t-1})=\frac{\mathrm{count}(w_{t-1}, w_t)+\alpha}{\mathrm{count}(w_{t-1})+\alpha |V|}$$

Context compatibility for a candidate replacement is scored by log-probability of left and right bigrams.

---

During transformation, the function first validates CEFR labels and handles trivial cases (empty input or same source/target level). It parses the sentence with spaCy and considers only **content tokens** (NOUN, VERB, ADJ, ADV) that are alphabetic and not stopwords.

For each eligible token, candidate generation uses **WordNet**:

- possible substitutes are collected from synsets of the token lemma,
- Lesk WSD is used when available to prioritize context-relevant sense,
- only single-word alphabetic candidates are kept.

Each candidate is inflected back to the original token morphology using pyinflect/getInflection, with case restoration.

---

The ranking stage combines multiple constraints:

- **Level-direction constraint**: candidate difficulty should move toward target CEFR (harder for upward transfer, simpler for downward transfer).
- **Semantic similarity**: spaCy vector similarity with POS-specific thresholds (stricter for nouns/verbs).
- **Context fit**: candidate should not significantly reduce bigram fluency under target/global LMs.
- **Form constraints**: avoid near-duplicates (including -ise/-ize normalization), invalid alpha forms, and adverb-form mismatches.

A strict score is computed:

$$\mathrm{final}=0.35\cdot \mathrm{sem}+0.40\cdot \mathrm{ctx}+0.25\cdot \mathrm{level}-0.05\cdot \mathrm{syn\_rank}$$

with an additional tie-break term favoring better movement toward target level.  
If strict candidates are weak, a relaxed pass is used with looser thresholds and a frequency bonus.

---
### 3.  Experiments and Results
#### 3.1 Experimental Setup

I evaluated the system in a local conda environment (cefr) using:

- python main.py z5518601 for qualitative inspection on public unit tests.
- python test.py z5518601 --tests unit_tests.csv --out_dir test_outputs_final_unit for quantitative metrics.

The public test set (unit_tests.csv) contains 10 sentence-level CEFR transfer cases (mostly downward transfers such as B2/C1 to A2/B1).  
I report four metrics:

- success_rate: fraction of cases without runtime errors.
- avg_changed_ratio: proportion of changed tokens.
- avg_difficulty_shift: average lexical difficulty movement (negative = simplification).
- direction_success_rate: fraction of outputs moving in the expected CEFR direction.

#### 3.2 Quantitative Results

On unit_tests.csv, the final system achieved:

- success_rate = 1.0000 (10/10, no runtime errors)
- avg_changed_ratio = 0.1888
- avg_difficulty_shift = -0.1009
- direction_success_rate = 0.9000

These numbers indicate that the method is stable and generally performs controlled simplification while avoiding excessive rewriting.

![[Pasted image 20260307230734.png]]

#### 3.3 Qualitative Examples

**Example 1 (C1 -> A2)**  
Input: _I purchased a magnificent house yesterday._  
Output: _I purchased an impressive home yesterday._  
Discussion: The model simplified one noun phrase (_house -> home_) and corrected article agreement (_a -> an_ before _impressive_). The sentence remains grammatical and close in meaning, though simplification strength is moderate.

![[Pasted image 20260307230925.png]]

**Example 2 (B2 -> A2)**  
Input: _The scientist conducted an experiment._  
Output: _The scientist did an experiment._  
Discussion: A previous version produced semantically drifted verbs (e.g., _conveyed/moved_). The final version adds a context-sensitive verb filter and keeps a simpler but semantically safer replacement.

![[Pasted image 20260307231023.png]]

**Example 3 (C1 -> B1)**  
Input: _The committee will evaluate the proposal tomorrow._  
Output: _The committee will judge the proposal tomorrow._  
Discussion: The replacement preserves the core meaning and reduces lexical complexity.

![[Pasted image 20260307231043.png]]
#### 3.4 Result Interpretation

Overall, the system shows a good trade-off between lexical control and meaning preservation. The model is robust (no crashes) and directionally correct in most cases (90%). Remaining errors are mainly due to limited candidate quality for some words, where stronger simplification may conflict with semantic precision.