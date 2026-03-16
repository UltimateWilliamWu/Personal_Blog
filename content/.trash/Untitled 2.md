#### 1. Task Overview & My Strategy

The goal of this assignment was to transform sentences between different CEFR levels. Early on, I realized that trying to rewrite the entire sentence structure usually led to a mess—either the grammar broke or the meaning drifted too far.

Instead of building a "black box" rewriter, I decided to focus on **controlled lexical substitution**. My rule was simple: only swap a word if I’m reasonably sure it fits the context and actually moves the sentence toward the target level. If no safe candidate exists, I’d rather keep the original word than produce a broken sentence.

#### 2. How the Pipeline Works

I broke the `transform_sentence` function into a few straightforward steps:

- **Step 1: Scoring Word Difficulty:**
    
    I didn't use any fancy external LLMs. I relied entirely on the provided `data.csv`. I calculated a "difficulty score" for each word by averaging its occurrences across the CEFR levels. This gave me a much more reliable signal than just looking at the raw counts.
    
    $$\text{score}(w) = \frac{\sum i \cdot c_i(w)}{\sum c_i(w)}$$
    
    Basically, if a word appears mostly in C2, it gets a high score; if it’s an A1 staple, it gets a low one.
    
- **Step 2: Finding Candidates:**
    
    I used WordNet to grab synonyms. To keep things stable, I limited the search to Nouns, Verbs, Adjectives, and Adverbs.
    
- **Step 3: Filtering (The "Hard" Part):**
    
    This is where most of my debugging happened. To stop the system from picking weird synonyms, I added:
    
    1. **Semantic Check:** Using FastText/Vector similarity to make sure the new word actually means the same thing.
        
    2. **Level Check:** Making sure the candidate’s score is actually lower (for simplification) or higher (for "up-scaling") than the original.
        
    3. **Local Context:** A quick bigram check to see if the new word "sounds right" with its immediate neighbors.
        
- **Step 4: Grammar Fixes:**
    
    Replacing a verb like _evaluate_ with _judge_ often breaks the tense (e.g., _evaluates_ becomes _judges_). I wrote a small utility to map the original word's tags onto the new one so the sentence doesn't look illiterate.
    

#### 3. What Didn't Work (Lessons Learned)

The final system is actually my third attempt.

- **Version 1** was too aggressive—it tried to change every word it could find, which made the sentences unreadable.
    
- **Version 2** relied too much on raw vector similarity, but vectors don't understand "difficulty," so it would often replace an easy word with a much harder one just because they were synonyms.
    

The "breakthrough" for me was realizing that **less is more**. By adding stricter "guardrails" and being more conservative with the edits, the output quality improved significantly.

#### 4. Self-Evaluation

My system is definitely on the **cautious** side.

- **Pros:** It rarely produces "hallucinations" or totally broken grammar. It’s very good at swapping out high-level verbs for simpler ones.
    
- **Cons:** It’s limited by WordNet’s dictionary. If a word isn't in there, the system just skips it. It also doesn't handle complex phrase-level changes (like changing "take part in" to "participate").
    

#### 5. Conclusion

Building this taught me that in NLP tasks like this, data-driven constraints (like the CSV scores) are often more useful than just throwing a complex model at the problem. The final pipeline is a balance between moving the CEFR needle and keeping the English sounding natural.