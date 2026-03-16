### 1. The task and its framing

The task requires the transformation of sentences between CEFR levels while maintaining semantic integrity. The approach taken was to treat this as a problem of controlled lexical substitution rather than a full rewriting. Initial experiments involving broader rewriting frequently resulted in a more pronounced CEFR shift; however, the outputs were often less natural and occasionally semantically inaccurate. The final system is thus only concerned with editing a limited number of content words, whilst preserving the original sentence structure, unless the replacement is clearly beneficial.

The following assumptions have been made:


It is important to note that the sole purpose of the file entitled 'data.csv' is to estimate word difficulty and to construct contextual statistics.
In this study, the CEFR is approached as a lexical difficulty signal rather than a comprehensive model of grammar or discourse complexity.
In instances where the preservation of meaning is uncertain, it is preferable to replace fewer words, as opposed to undertaking extensive rewriting.

In the absence of a candidate that is both simpler and semantically safe, it is considered acceptable to retain the original word.

- - -

### 2. The aircraft is now commencing its final approach.

  

The core function is **transform_sentence(sentence, source_level, target_level)**. The pipeline comprises four constituent elements: word difficulty estimation, candidate generation, candidate filtering/ranking, and light grammatical repair.

  

The second point to consider is the difficulty signal from the training data.

  

From the data contained in the file named "data.csv", I construct global statistics on a single occasion and then cache them. Each word is assigned a continuous difficulty score based on its position across the CEFR levels:

  

The score is calculated as follows: the sum of the i^(th) element of w is divided by the sum of the i^(th) element of w.

  

In this study, the count of word w at CEFR index i is denoted by $c_i(w)$. The range of values for $c_i(w)$ is from 0 to 5, with A1 to C2 mapped to 0 to 5, respectively. This methodology provides a straightforward corpus-based estimate of lexical difficulty.

  

In addition, the training of add-$\alpha$ smoothed bigram language models, comprising one global model and one model per CEFR level, is undertaken.

  

The posterior probability of the occurrence of the word 'w_t' given the preceding word 'w_{t-1}', denoted by P(w_t | w_{t-1} = α), is calculated as follows:

  

The bigram models are uncomplicated, yet they are sufficient to reject a multitude of plausible-in-isolation but detrimental-in-context alternatives.

  

The subsequent section will address the process of candidate generation.

  

At inference time, spaCy identifies content words (NOUN, VERB, ADJ, ADV). The majority of candidates are derived from WordNet synsets of the lemma, filtered to single-word alphabetic forms. In addition, a conservative corpus-driven fallback strategy is employed, whereby frequent words from the training data are only considered if they demonstrate semantic overlap and clear CEFR movement. This was incorporated due to the fact that a purely WordNet pipeline frequently failed to identify pertinent substitutions.

  

The following section will address the topic of semantic filtering and ranking.

  

The decision-making process involves the application of various filters and the subsequent calculation of a ranking score. A significant modification that occurred during the developmental process was the decision to cease reliance on the utilisation of spaCy vector similarity exclusively. The current version combines vector similarity with WordNet sense similarity, assigning the strongest sense weight to verbs due to their propensity to induce the most semantic errors. Candidates are then filtered by semantic thresholds, CEFR direction checks, local context, and collocation strength.

  

Candidates who successfully pass the initial filters are then subjected to a ranking process, which is classified as either 'strict' or 'relaxed'. The core ranking scores are as follows:

  

The final value, when calculated using the strict method, is equivalent to 0.33 multiplied by the sem, 0.44 multiplied by the cx, 0.17 multiplied by the level, 0.06 multiplied by the colloc, and -0.05 multiplied by the syn_rank.

  

Furthermore,

  

The final relaxed value is determined by the following equation: 0.30 × sem + 0.25 × ctx + 0.33 × level + 0.10 × freq + 0.02 × colloc − 0.03 × syn_rank.

  

The following are the primary ranking formulas, not the entire decision logic. The operation of these filters is particularly pronounced in the case of verbs, with multiple layers of filtration being employed. In the event that the initial edits prove insufficient in terms of altering the sentence's substance, a subsequent stage may involve the introduction of one or two additional safe candidates, accompanied by a positive directional gain.

  

The following section will address the topic of morphology and surface repair.

  

Candidates are inflected back into the original surface form with **pyinflect** so that tense and number are preserved wherever possible. In addition, a minor post-processing step was incorporated with the objective of identifying and rectifying any evident surface imperfections.

  

### 3. The process of development is underway.

  

The final system was derived from multiple unsuccessful iterations. The most significant issue encountered pertained to verb substitution, wherein earlier iterations had the capacity to simplify numerically while concomitantly altering the semantic content of events. This phenomenon could be illustrated by the substitution of 'evaluate' for 'judge' or the generation of unconventional replacements for 'conducted'. It was therefore necessary to impose stricter semantic filters on verb filtering than on noun or adjective filtering. This was achieved by the implementation of stronger semantic thresholds and additional sense-based checks.

  

The present study also found that candidate ordering mattered. In the absence of stable sorting prior to truncation, WordNet occasionally yielded divergent results across iterations. The sorting of synsets and lemmas rectified the issue and rendered the system deterministic.

  

In conclusion, broader vector-neighbour candidate pools and extra slot-style scoring for adjective-noun or verb-object combinations were employed. The aforementioned concepts appeared to be beneficial, yet their implementation resulted in a decline in overall evaluation performance. Consequently, their removal was deemed necessary. The final system is conservative by design; it demonstrates a preference for a missed edit over a bad edit.

  

### 4. Evaluation

  

The following section outlines the setup process.

  

The final version was executed in the local **cefr** conda environment, utilising the following command:

  

The command to be entered is "python main.py z5518601".

The Python program is to be evaluated using the 'z5518601' test file, with the 'unit_tests.csv' file providing the necessary parameters. The 'evaluation_outputs_unit_current_reportcheck' directory will be used as the output directory.

  

The 10-case **unit_tests.csv** file is diminutive in size, yet it is the provided public evaluation file and it is sufficient to ascertain whether the system is moving outputs in the intended lexical direction.

  

The following section details the results of the public unit tests.

  

The present execution of the **unit_tests.csv** programme yielded the following results:

  

It can be posited that the success rate is equal to 1.0000.

The average change ratio is thus 0.1579.

The average difficulty shift is -0.1209.

The directional success rate was found to be 0.9000.

The value of the 'no_change_rate' variable is 0.1000.

  

The results obtained demonstrate a cautious system, which generally simplifies in the correct direction, yet does not force a change in every instance.

  

The following section will present a series of qualitative examples.

  

Example 1: Partial but safe simplification

Input: The acquisition of a splendid residence was completed yesterday.

Output: The acquisition of a superior domestic property was completed on the previous day.

  

The image has been pasted. It is entitled '20260316002137.png'.

  

This is a common occurrence in the final system. The adjective becomes simpler, but the verb 'purchased' remains, so the sentence moves downward only partially.

  

Example 2: A strong local substitution

Input: It was swiftly apparent that an error had been made.

Output: It became evident to him that an error had been made.

  

The image has been pasted. It is entitled '20260316002153.png'.

  

This is an exemplary instance of a successful replacement, characterised by its local provenance, semantic congruence, and evident simplicity.

  

Example 3: Conservative, no-change

Input: The evaluation of the proposal is scheduled to take place by the committee on the morrow.

Output: The evaluation of the proposal is scheduled to take place by the committee on the morrow.

  

The image has been pasted. It is entitled '20260316002207.png'.

  

This example elucidates the fundamental trade-off inherent in the final system. The model is capable of identifying simpler verb candidates; however, these candidates do not meet the necessary semantic criteria for acceptance. In this particular sentence, replacing "evaluate" with a word such as "judge" would result in a simplification of the word, yet it would also lead to a shift in its connotation. Consequently, the system demonstrates a preference for the absence of change.

  

Example 4: Remaining semantic weakness

Input: The results obtained demonstrate a significant improvement.

Output: The results indicate a substantial enhancement.

  

The image has been pasted. It is entitled '20260316002231.png'.

  

This failure case is a valuable addition to the existing body of knowledge. The output exhibits a downward movement in the lexical hierarchy, with the word 'significant' becoming 'large'. However, the word 'prove' maintains a slight advantage in strength over 'demonstrate'. The sentence is not entirely erroneous; nevertheless, it does demonstrate that the present filtering system is more effective in obstructing highly unfavourable substitutions than in ensuring optimal substitutions.

  

### 5. The following limitations must be noted:

  

As demonstrated in Section 5.1, the candidate generation process remains constrained.

  

Despite the incorporation of a corpus-driven fallback mechanism, the system continues to demonstrate a significant reliance on WordNet. It is evident that a number of promising contextual options never progress beyond the candidate pool. For instance, the term 'review' may be a more suitable option than 'judge' for 'evaluate the proposal', however, the system is unable to select it if it has not been generated.

  

As indicated in section 5.2 of the Common European Framework of Reference (CEFR), control is predominantly at the word level.

  

The system estimates the difficulty of each word on an individual basis, while focusing exclusively on the local bigram context. This degree of movement is sufficient for directional control; however, it does not meet the criteria for full CEFR control.

  

In the fifth section, the Model Under-Edits Difficult Cases.

  

The system is deliberately cautious. This approach has been shown to reduce catastrophic semantic errors; however, it has also been demonstrated to increase no-change and partial-change cases.

  

As indicated in section 5.4, the evaluation process is not yet complete and there are still some aspects that require attention.

  

The public unit tests are beneficial in terms of debugging, yet they are insufficiently extensive to substantiate sweeping assertions regarding generalisation.

  

### 6. Conclusion

  

The final system can be best understood as a cautious lexical baseline. It has been demonstrated that the software can move many sentences in the required CEFR direction while avoiding many bad substitutions from earlier versions. The primary gains were derived from the tightening of verb semantics, the incorporation of more robust filtering mechanisms, and the acknowledgement that conservative editing is preferable to aggressive but erroneous rewriting.

  

The primary conclusion derived from the assignment is that the introduction of additional machinery did not inherently enhance the efficacy of the model. A smaller pipeline incorporating explicit guardrails, difficulty estimates, constrained candidates, semantic filters, local context checks and light grammatical repair was found to be more reliable than several more ambitious variants.