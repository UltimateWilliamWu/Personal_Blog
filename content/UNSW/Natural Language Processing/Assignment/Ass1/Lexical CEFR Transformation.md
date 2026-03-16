---
tags:
  - Assignment
---
### 1. Task and Framing

The task is to change a sentence from one CEFR level to another without changing the meaning or grammar too much. In practice, I treated this as a controlled word replacement task rather than full rewriting. I tried broader rewriting earlier, but it usually made the output worse. The CEFR score moved more, but the sentence often sounded unnatural or the meaning changed too much. Because of that, the final system only changes a small number of content words and keeps the original sentence structure.

This way of framing the task is also closer to what the system actually does. It is not trying to rewrite sentences like a human editor. Instead, it makes small changes to move the sentence toward the target CEFR level, while avoiding replacements that look risky. That is why many of the final outputs are only partial simplifications. They are not very aggressive, but they are usually safer.

- - -
### 2. Final Approach

The core function is **transform_sentence(sentence, source_level, target_level)**. The pipeline has four main parts: word difficulty estimation, candidate generation, candidate filtering/ranking, and light grammatical repair.

#### 2.1 Difficulty Signal from the Training Data

From **data.csv**, I construct global statistics once and then cache them. Each word is assigned a continuous difficulty score based on how it is distributed across CEFR levels:

$$\mathrm{score}(w)=\frac{\sum_i i \cdot c_i(w)}{\sum_i c_i(w)}$$

where $c_i(w)$ is the count of word $w$ at CEFR index $i$, with A1 to C2 mapped to 0 to 5. This score is simple, but it gives a usable approximation of whether a word tends to be easier or harder in the training corpus.

I also train add-$\alpha$ smoothed bigram language models, one global and one per CEFR level:

$$P(w_t \mid w_{t-1})=\frac{\mathrm{count}(w_{t-1}, w_t)+\alpha}{\mathrm{count}(w_{t-1})+\alpha |V|}$$

While these bigram probabilities are not a strong language model, they are enough to reject many options that seem good on their own but are not good in a local context.

#### 2.2 Candidate Generation

At this stage, spaCy is used to tokenize the sentence and identify content words (nouns, verbs, adjectives, and adverbs). Most candidates come from WordNet synsets of the lemma. I keep only single-word alphabetic forms, assign them a candidate rank based on synset distance, and later filter and rescore them. The system also has a fallback for content words when WordNet alone is too limited or too advanced. This fallback searches common words in the training data and keeps only those that show both semantic overlap and downward CEFR movement.

This part changed a lot during development. A simple WordNet pipeline was easy to build, but it missed many useful substitutions and sometimes returned odd options. A corpus-based fallback improved recall, but only when I kept it conservative. At first, adding more candidates looked helpful, but in practice it often made semantic drift worse.

#### 2.3 Semantic Filtering and Ranking

In the current version, I use a combination of word similarity and WordNet sense similarity. Verbs are given the strongest sense weighting because they are more likely to cause meaning problems.

The core ranking scores are:

$$\mathrm{final}_{strict}=0.33\cdot \mathrm{sem}+0.44\cdot \mathrm{ctx}+0.17\cdot \mathrm{level}+0.06\cdot \mathrm{colloc}-0.05\cdot \mathrm{syn\_rank}$$

and

$$\mathrm{final}_{relaxed}=0.30\cdot \mathrm{sem}+0.25\cdot \mathrm{ctx}+0.33\cdot \mathrm{level}+0.10\cdot \mathrm{freq}+0.02\cdot \mathrm{colloc}-0.03\cdot \mathrm{syn\_rank}$$

The above are the primary ranking formulas, not the entire decision logic. They operate after several hard filters, especially for verbs. If the first-pass edits do not move the sentence enough, a second stage can add one or two extra safe candidates with positive directional gain.

#### 2.4 Morphology and Surface Repair

Candidates are inflected back into the original surface form with **pyinflect**, so the system can preserve tense or number whenever possible. I also added a small article-fix post-processing step for **a/an**. This is not sophisticated grammar correction, but it prevents some very obvious surface errors and helped stabilize the outputs.

- - -
### 3. Development

The final system was created after several failed attempts. The main issue was verb substitution, where earlier versions could make the sentence simpler in score but also change the event meaning. A clear example is replacing *evaluate* with *judge* or generating odd replacements for *conducted*. I therefore applied stricter semantic filtering to verbs than to nouns or adjectives. This was done by adding stronger semantic thresholds and extra sense-based checks.

I also found that candidate ordering mattered. Without stable sorting before truncation, WordNet sometimes produced different outputs across runs. Sorting synsets and lemmas fixed this and made the system deterministic.

I also tried broader vector-neighbour candidate pools and extra slot-style scoring for adjective-noun and verb-object combinations. These ideas looked useful, but they reduced overall evaluation performance, so I removed them. The final system is conservative by design and prefers a missed edit over a bad edit.

- - -
### 4. Evaluation

#### 4.1 Setup

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
Input: I purchased a magnificent house yesterday. 
Output: I purchased a wonderful house yesterday.  

![[Pasted image 20260316002137.png]]

This is a good example of how the system usually works. The adjective change is reasonable and simpler, but the verb 'purchased' is kept. The output moves in the right direction, but it is still not quite an A2-style rewrite.

**Example 2: A strong local substitution**  
Input: He quickly realised his mistake.  
Output: He quickly saw his mistake. 

![[Pasted image 20260316002153.png]]

This is one of the cleaner successes. The edit is local, makes sense, and is simpler. This is an example of when the current system works really well.

**Example 3: Conservative no-change**  
Input: The committee will evaluate the proposal tomorrow.  
Output: The committee will evaluate the proposal tomorrow. 

![[Pasted image 20260316002207.png]]

This is not the best example of simplification strength, but it does show the current trade-off of the system. Candidate verbs such as 'judge' are simpler, but in this context they change the meaning too much. So the model leaves the sentence unchanged.

**Example 4: Remaining semantic weakness**  
Input: The results demonstrate a significant improvement.
Output: The results prove a large improvement. 

![[Pasted image 20260316002231.png]]

This sentence still has a problem. The output moves down lexically, but 'prove' is slightly stronger than 'demonstrate', so the meaning does not match perfectly. This shows that the current filters reduce semantic drift, but do not fully remove it.

- - -
### 5. Limitations

#### 5.1 Candidate Generation Is Still Narrow

Even though it has a fallback mechanism, the system still relies heavily on WordNet. This means that some useful simplification options may never enter the candidate pool. For example, a verb like 'review' may be more suitable in the given situation than 'judge', but if it is not generated early enough, the system cannot choose it.

#### 5.2 CEFR Control Is Mostly Word-Level

The system estimates difficulty word by word and uses a bigram model to check local context. This is enough for directional movement, but not for full CEFR control. A sentence can become lexically simpler and still sound less natural than a human simplification.

#### 5.3 The Model Under-Edits Difficult Cases

The system is deliberately cautious. This reduces catastrophic semantic errors, but it also increases no-change and partial-change cases. 

#### 5.4 Evaluation Still Has Gaps

The public unit tests are too small, so I still cannot say that the model performs like a human simplifier. A better future evaluation would combine CEFR control with a dataset that directly measures how well meaning is preserved against a reference rewrite.

- - -
### 6. Conclusion

The final system is basically a lexical baseline. It can move many sentences toward the target CEFR level and avoid many of the bad substitutions that appeared in earlier versions. The biggest improvements came from handling verbs more carefully, adding stronger filters, and choosing small safe edits instead of trying to rewrite too much.

The main lesson from this assignment was that a more complicated system is not always better. I tried several more complex ideas, but some of them actually made the results worse, so I removed them. In the end, a smaller system worked better: word difficulty scores, limited replacement candidates, part-of-speech based filtering, local context checks, and simple grammar fixes. It is not a complete solution to CEFR-aware rewriting, but it does give a simple and fairly stable way to simplify vocabulary.
