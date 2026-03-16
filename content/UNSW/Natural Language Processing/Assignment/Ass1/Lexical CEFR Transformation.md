---
tags:
  - Assignment
---
### 1. Task and Framing

The task is to rewrite a sentence so that it is at a different CEFR level, while ensuring that the original meaning and grammar are retained. In practice, I achieved this by replacing individual words rather than rewriting the entire sentence. Earlier attempts at broader rewriting usually resulted in lower-quality output. Although the CEFR score improved, the sentence often sounded unnatural or had a different meaning. For this reason, the final system only replaces a small number of content words while retaining the original sentence structure.

This approach also more closely reflects what the system actually does. It does not attempt to rewrite sentences as a human editor would. Instead, it makes minor adjustments to bring the sentence closer to the target CEFR level while avoiding risky replacements. This explains why many of the final outputs are only partial simplifications. They are not very aggressive, but they are usually safer.

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

This part changed a lot during development. Although a simple WordNet pipeline was easy to build, it missed many useful substitutions and sometimes returned unusual options. Using a corpus-based fallback improved recall, but only when it was kept conservative. Initially, adding more candidates seemed helpful, but in practice it often exacerbated semantic drift.

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

The final system was created after several failed attempts. The main issue was verb substitution: earlier versions could simplify the sentence in terms of scoring but also alter the meaning of the event.

For instance, 'evaluate' could be replaced with 'judge', or unusual replacements could be generated for 'conducted'. I therefore applied stricter semantic filtering to verbs than to nouns or adjectives.This was achieved by adding stronger semantic thresholds and extra sense-based checks.

I also found that candidate ordering mattered. Without stable sorting before truncation, WordNet sometimes produced different outputs across runs. Sorting synsets and lemmas resolved this issue and made the system deterministic.
I experimented with broader vector-neighbour candidate pools and additional slot-style scoring for adjective-noun and verb-object combinations. While these ideas appeared promising, they reduced the system's overall performance, so I removed them. The final system is conservative by design, favouring a missed edit over a bad edit.

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

This is a good example of how the system usually works. While the adjective has changed, the verb 'purchased' has been kept. While the output moves in the right direction, it is still not quite an A2-style rewrite.

**Example 2: A strong local substitution**  
Input: He quickly realised his mistake.  
Output: He quickly saw his mistake. 

![[Pasted image 20260316002153.png]]

This is one of the cleaner successes. The local edit makes sense and is simpler. It's a great example of when the current system works really well.

**Example 3: Conservative no-change**  
Input: The committee will evaluate the proposal tomorrow.  
Output: The committee will evaluate the proposal tomorrow. 

![[Pasted image 20260316002207.png]]

While this is not the best example of simplification strength, it does demonstrate the current trade-off of the system. Although candidate verbs such as 'judge' are simpler, they change the meaning too much in this context. Therefore, the model leaves the sentence unchanged.

**Example 4: Remaining semantic weakness**  
Input: The results demonstrate a significant improvement.
Output: The results prove a large improvement. 

![[Pasted image 20260316002231.png]]

There is still a problem with this sentence. Although the output moves down lexically, 'prove' is slightly stronger than 'demonstrate', meaning the two do not match perfectly. This demonstrates that, while the current filters reduce semantic drift, they do not eliminate it entirely.

- - -
### 5. Limitations

#### 5.1 Candidate Generation Is Still Narrow

Even though it has a fallback mechanism, the system still relies heavily on WordNet. This means that some useful simplification options may never enter the candidate pool. 
For example, a verb like 'review' may be more suitable in the given situation than 'judge', but if it is not generated early enough, the system cannot choose it.

#### 5.2 CEFR Control Is Mostly Word-Level

The system estimates difficulty word by word and uses a bigram model to check local context. This is enough for directional movement, but not for full CEFR control. A sentence can become lexically simpler and still sound less natural than a human simplification.

#### 5.3 The Model Under-Edits Difficult Cases

The system is deliberately cautious. This reduces catastrophic semantic errors, but it also increases no-change and partial-change cases. 

#### 5.4 Evaluation Still Has Gaps

The public unit tests are too small, so I still cannot say that the model performs like a human simplifier. A better future evaluation would combine CEFR control with a dataset that directly measures how well meaning is preserved against a reference rewrite.

- - -
### 6. Conclusion

The final system is essentially a lexical baseline. It can bring many sentences closer to the target CEFR level while avoiding the poor substitutions that appeared in earlier versions. The most significant improvements were achieved by handling verbs more carefully, adding stronger filters and opting for minor, safe edits rather than attempting to rewrite too much.

The main lesson from this assignment is that a more complicated system is not necessarily better. I experimented with several more complex ideas, but some of these actually produced worse results, so I removed them. 
Ultimately, a smaller system comprising word difficulty scores, limited replacement candidates, part-of-speech-based filtering, local context checks and simple grammar fixes worked better. While not a complete solution to CEFR-aware rewriting, it provides a simple and fairly stable way to simplify vocabulary.
