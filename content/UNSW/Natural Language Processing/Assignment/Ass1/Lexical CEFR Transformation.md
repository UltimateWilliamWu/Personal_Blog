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

From the data contained in the file named "data.csv", I construct global statistics on a single occasion and then cache them. Each word is assigned a continuous difficulty score based on its position across the CEFR levels:

$$\mathrm{score}(w)=\frac{\sum_i i \cdot c_i(w)}{\sum_i c_i(w)}$$

where $c_i(w)$ is the count of word $w$ at CEFR index $i$, with A1 to C2 mapped to 0 to 5. This score is simple, but it gives a usable approximation of whether a word tends to be easier or harder in the training corpus.

I also train add-$\alpha$ smoothed bigram language models, one global and one per CEFR level:

$$P(w_t \mid w_{t-1})=\frac{\mathrm{count}(w_{t-1}, w_t)+\alpha}{\mathrm{count}(w_{t-1})+\alpha |V|}$$

While these bigram probabilities are not a strong language model, they are enough to reject many options that seem good on their own but are not good in a local context.

#### 2.2 Candidate Generation

At this point, the spaCy framework is used to break the sentence into smaller parts and find the possible content words (nouns, verbs, adjectives and adverbs). Most of the candidates come from WordNet synsets of the lemma. The approach used involves keeping single-word alphabetic forms and then ranking them based on how similar they are to each other. The system has a built-in fallback option for content words, which is used when WordNet alone is not enough or too advanced. The fallback function looks for common words in the training data and keeps only those that have both 'semantic overlap' and 'downward CEFR movement'.

This part of the machine was changed a lot while it was being made. Using a simple WordNet pipeline was easy, but it didn't include many helpful changes and sometimes gave unusual results. Adding a fallback mechanism based on a corpus has been shown to improve recall, but only when the approach is kept at a conservative level. At first, it looked like having more candidates might be a good idea. However, it has been shown that this often makes semantic drift worse instead of making the system better.

#### 2.3 Semantic Filtering and Ranking

The code can be used in more than one way. Making a decision is complicated. There are lots of things to think about, and they all have to be considered. One big change that happened during the development process was the decision to stop using spaCy vector similarity as the only way to do things. In the current version of the model, I use a combination of how similar words are to each other and how similar they are to the meanings in WordNet. Verbs are given the strongest sense weighting because they are more likely to cause problems with the meaning of words.

The core ranking scores are:

$$\mathrm{final}_{strict}=0.33\cdot \mathrm{sem}+0.44\cdot \mathrm{ctx}+0.17\cdot \mathrm{level}+0.06\cdot \mathrm{colloc}-0.05\cdot \mathrm{syn\_rank}$$

and

$$\mathrm{final}_{relaxed}=0.30\cdot \mathrm{sem}+0.25\cdot \mathrm{ctx}+0.33\cdot \mathrm{level}+0.10\cdot \mathrm{freq}+0.02\cdot \mathrm{colloc}-0.03\cdot \mathrm{syn\_rank}$$

The above are the primary ranking formulas, not the entire decision logic.The actual code hides these words behind several layers of complex filters, especially when it comes to replacing verbs and nouns. If the first edits don't improve the sentence enough, you can try adding one or two more safe candidates to see if that helps.

#### 2.4 Morphology and Surface Repair

Candidates are inflected back into the original surface form with **pyinflect**, so the system can preserve tense or number whenever possible. I also added a small article-fix post-processing step for **a/an**. This is not sophisticated grammar correction, but it prevents some very obvious surface errors and helped stabilize the outputs.

- - -
### 3. Development

The final system was created after trying and failing many times. The main issue was with verb substitution, where earlier versions could make things simpler in terms of numbers, but also change what events meant. A case in point is the substitution of "push evaluate" for "judge" or the generation of unconventional replacements for "conducted". It was therefore necessary to impose stricter semantic filters on verb filtering than on noun or adjective filtering. This was achieved by the implementation of stronger semantic thresholds and additional sense-based checks.

The present study also found that candidate ordering mattered. In the absence of stable sorting prior to truncation, WordNet occasionally yielded divergent results across iterations. The sorting of synsets and lemmas rectified the issue and rendered the system deterministic.

Ultimately, broader vector-neighbour candidate pools and additional slot-style scoring for adjective-noun and verb-object combinations were employed. The aforementioned concepts appeared to be beneficial, yet their implementation resulted in a decline in overall evaluation performance. Consequently, their removal was deemed necessary. The final system is conservative by design; it demonstrates a preference for a missed edit over a bad edit.

- - -
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
Input: I purchased a magnificent house yesterday. 
Output: I purchased a wonderful house yesterday.  

![[Pasted image 20260316002137.png]]

This is a good example of how the system usually works. The adjective change is reasonable and simpler, but the verb 'purchased' is kept. The sentence is better, but it's not quite an A2-style rewrite.

**Example 2: A strong local substitution**  
Input: He quickly realised his mistake.  
Output: He quickly saw his mistake. 

![[Pasted image 20260316002153.png]]

This is one of the cleaner successes. The edit is local, makes sense, and is simpler. This is an example of when the current system works really well.

**Example 3: Conservative no-change**  
Input: The committee will evaluate the proposal tomorrow.  
Output: The committee will evaluate the proposal tomorrow. 

![[Pasted image 20260316002207.png]]

This isn't the best example of simplification strength, but it does show the current trade-offs of the system. Candidate verbs such as 'judge' are easier to understand, but in this context they change the meaning too much. So the model doesn't want to change.

**Example 4: Remaining semantic weakness**  
Input: The results demonstrate a significant improvement.
Output: The results prove a large improvement. 

![[Pasted image 20260316002231.png]]

This sentence still has a problem. The output moves down lexically, but 'prove' is slightly stronger than 'demonstrate', so the meaning doesn't match perfectly. This shows that the current filters reduce semantic drift, but do not completely get rid of it.

- - -
### 5. Limitations

#### 5.1 Candidate Generation Is Still Narrow

Even though it has a system to fall back on if there are problems, the system still relies a lot on WordNet. This suggests that some effective ways of simplifying things may not be included in the candidate pool. For example, a verb like 'review' may be more suitable in the given situation than 'judge', but if it is not chosen early enough, the system cannot choose it.

#### 5.2 CEFR Control Is Mostly Word-Level

The system utilises a word-by-word estimation of difficulty and employs a bigram model to analyse local context. This degree of movement is sufficient for directional movement, but not for full CEFR control. It is evident that a sentence can become lexically simpler while maintaining a level of naturalness that is less pronounced in comparison to a human simplification.

#### 5.3 The Model Under-Edits Difficult Cases

The system is deliberately cautious. This reduces catastrophic semantic errors, but it also increases no-change and partial-change cases. 

#### 5.4 Evaluation Still Has Gaps

The public unit tests are too small, so I still cannot say that the model performs like a human simplifier. A better future evaluation would combine CEFR control with a set of data that directly measures how well meaning is kept when things are rewritten based on a reference.

- - -
### 6. Conclusion

The final system is basically a careful lexical baseline. It can move many sentences toward the target CEFR level and avoid many of the bad substitutions that appeared in earlier versions. The biggest improvements came from handling verbs more carefully, adding stronger filters, and choosing small safe edits instead of trying to rewrite too much.

The main lesson from this assignment was that a more complicated system is not always better. I tried several more complex ideas, but some of them actually made the results worse, so I removed them. In the end, a smaller system worked better: word difficulty scores, limited replacement candidates, part-of-speech based filtering, local context checks, and simple grammar fixes. It is not a complete solution to CEFR-aware rewriting, but it does give a simple and fairly stable way to simplify vocabulary.
