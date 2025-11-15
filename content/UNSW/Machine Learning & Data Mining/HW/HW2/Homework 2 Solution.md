---
tags:
  - Assignment
---
## Question 1. Explore Model-Based Feature Importance    
(a) Generate a dataset of two classes using sklearn.datasets.make classification. It should have 1000 observations, 20 features. Set 5 of those features to be informative (important), and the rest as redundant. Be sure to set the shuffle parameter to False, so that the informative features are listed first. Normalize your data using sklearn.StandardScaler(). Then, fit a decision tree (using entropy as the criteria for splits) to a shuffled version of the data1 using sklearn.tree model DecisionTreeClassifier, and using its feature importances method, report how many of the actually important features are found in the top 5 important features by the decision tree. Plot a histogram with $\mathbf{x}$ -axis showing the features ranked in decreasing order of importance, and the y-axis showing the feature importance score. Use a random seed of 0 when generating the data for reproducibility. Use a random seed of O when shuffling the data, you can use shuffled idxs $=$ np.random.default rng(seed $=0$ ).permutation(X.shape[1]).    

>[!note] ScreenShot
>
>![[Pasted image 20250326144931.png|800]]
>
>![[Pasted image 20250327135215.png]]

>[!todo] Commentary
>1. We generate a binary classification dataset using `make_classification` with 1000 samples and 20 features. Among these, only the first 5 features are informative, and the remaining 15 are redundant. We fix the random seed (`random_state=0`) to ensure reproducibility.
>2. The dataset is standardized using `StandardScaler` to normalize the feature values.
>3. We shuffle the order of the feature columns using NumPy’s `default_rng(seed=0).permutation(...)` so that informative features are no longer in fixed positions. This simulates a real-world scenario where the model cannot rely on feature order.
>4. A decision tree classifier is trained using the `entropy` criterion and `random_state=4` for consistent tree structure. After training, we obtain the model’s feature importance scores.
>5. We select the top 5 most important features as determined by the tree, and we check how many of them correspond to the actual informative features (which were originally in indices 0 to 4 before shuffling).
>6. A bar chart is plotted to visualize the feature importance scores in descending order.

(b) Provide a detailed explanation of how the feature importance (a.k.a. Gini importance) in the previous question are computed; use formulas to explain the exact calculation. Further, answer the following:    
1. What feature importance score is assigned to a feature that is not used for any splits of the tree. Why?     
2. What does a feature importance of 0.15 mean?    
  
>[!FAQ] Answer
>Scikit-learn provides feature importance scores via the attribute `feature_importances_`, which are computed based on how much each feature contributes to reducing impurity in the decision tree. Specifically, these scores are based on the **Mean Decrease in Impurity (MDI)** method.
>## Gini Impurity
>A Gini impurity of 0 indicates that all samples at the node belong to a single class (pure node), while higher values indicate greater impurity.
>$$
>G(t) = 1 - \sum_{k=1}^{K} p_k^2
>$$
where:
>- G(t) is the Gini impurity of node t
>- $p_k$ is the proportion of class k in the node
>## Mean Decrease in Impurity
>The feature importance for feature fff is calculated as the total impurity reduction it contributes over all splits where it is used:
>$$
>\begin{aligned}
>Importance(f) &= \sum_{\text{splits } t \text{ using } f} \frac{N_t}{N} \cdot \Delta G(t)\\
>\Delta G(t) &= G(t) - p_L \cdot G(t_L) - p_R \cdot G(t_R)
>\end{aligned}
>$$ 
>where:
>- $N_t$: number of samples at node t
>- N: total number of samples in the dataset
>- G(t): impurity at node t
>- $G(t_L), G(t_R)$: impurity at the left/right child nodes
>- $p_L = N_L / N_t, p_R = N_R / N_t$
>## Final Feature Importance Normalization
>After computing importance scores for all features, scikit-learn normalizes them so they sum to 1:
>$$
>X_j=\frac{Importance(X_j)}{\sum_i Importance(X_i)}
>$$
>This makes it easy to compare importance values across features.

>[!warning] Correction
>![[Pasted image 20250329150522.png|900]]
>As mentioned on the HW2 forum we need to replace gini with entropy
>### Entropy
>Entropy is an **information-theoretic measure** of impurity or uncertainty. For a node ttt in a classification decision tree, with KKK classes, entropy is computed as:
>$$
>\begin{equation}
H(t) = -\sum_{k=1}^{K} p_k \log_2(p_k)
\end{equation}
>$$
>Where:
>- $p_k$​ is the proportion of samples in node ttt that belong to class kkk.
>- Entropy is highest when the classes are equally likely, and lowest (0) when the node is pure (all samples from one class).
>### Decision Trees Use Entropy to Split
>When constructing a decision tree, at each node the algorithm evaluates splits based on the **Information Gain (IG)**:
>$$
>\begin{equation}
IG_t = H(t) - \left( \frac{n_{\text{left}}}{n_t} H(\text{left}) + \frac{n_{\text{right}}}{n_t} H(\text{right}) \right)
\end{equation}
>$$
>Where:
>- H(t): entropy before the split,
>- H(left),H(right): entropy of child nodes,
>- $n_{left},n_{right},n_t$​: number of samples in each node.
>The split that gives the **maximum information gain** is chosen.

>[!FAQ] Answer to b(1)&b(2)
>## b(1)
>$\qquad$If a feature is not used in any of the decision tree splits, its importance score will be **exactly 0**.
$\qquad$This is because the feature contributes **no reduction in impurity** throughout the entire tree. Since feature importance is computed as the sum of impurity reductions across all splits that use a feature (as defined in the MDI formula), unused features do not contribute to this sum.
>## b(2)
>$\qquad$A feature importance score of **0.15** means that the feature was responsible for **15% of the total impurity reduction** achieved by the decision tree.
$\qquad$In other words, across all the nodes where splits occurred, the weighted decrease in impurity from using that feature accounts for 15% of the total impurity gain.
>$$
>X_j=\frac{Importance(X_j)}{\sum_i Importance(X_i)}=0.15
>$$
This indicates that the feature plays a **moderately important** role in how the tree makes decisions.

(c) In order to obtain a more accurate picture of how good decision trees are at finding important features, we will repeat the experiment in part (a) a large number of times. Repeat the experiment a total of 1000 times. In the $i$ -th experiment, use a random seed of $i$ when creating the data set, where $i\,=\,1,2,\dots,1000$ . For each trial, record how many of the actually important features are identified. Provide a histogram of this metric over the 1000 trials. What do you think about the ability of decision trees to pick out the top features? Report the average number of good features recovered over the 1000 trials.    

>[!note] ScreenShot
>
>![[Pasted image 20250327135349.png|800]]
>
>![[Pasted image 20250327135419.png]]

>[!FAQ] Answer
>Repeat the process from Q1(a) a total of 1000 times. In each trial:
>- We generate a new dataset using a unique seed (`random_state = i`).
>- We normalize and shuffle the feature columns using the same shuffling pattern (seed = 0).
>- We train a `DecisionTreeClassifier` and select the top 5 features ranked by importance.
>- We count how many of those features belong to the set of true informative features (original indices 0–4).
>
>The histogram shows the distribution of recovered informative features across the 1000 trials.  
>We find that the **average number of informative features recovered is approximately 1.4**.
>### The ability of decision trees
>- The decision tree is able to **partially recover** the informative features, even without any scaling requirements.
>- However, due to the presence of **15 redundant features**, many of which are highly correlated with the informative ones, the model may distribute the importance across multiple correlated variables.
>- Additionally, since decision trees use a **greedy splitting strategy**, they may select features that locally reduce impurity, even if those are not globally the most informative.
>- As a result, the true informative features might not always be ranked highest in feature importance.

(d) Repeat part (c), but now use logistic regression with no penalty. Do this once with and once without scaling the feature matrix. As a feature importance metric, use the absolute value of the coefficient of that feature. Plot a histogram as before and report the average number of features recovered over the 1000 trials. Compare the scaled and non-scaled versions. How does logistic regression compare to decision trees?    

>[!note] ScreenShot
>
>![[Pasted image 20250327142026.png|800]]
>
>![[Pasted image 20250327141338.png]]

>[!FAQ] Answer
>Repeated the experiment from Q1(c), but using **logistic regression without regularization** as the model. We tested both **unscaled** and **standardized** versions of the dataset.
In each of the 1000 trials:
>- We generated a new dataset (5 informative features).
>- Shuffled the feature columns (fixed permutation).
>- Trained logistic regression models (with `penalty=None`).
>- Ranked features by the absolute value of their coefficients.
>- Compared the top-5 features with the original informative ones (index 0–4).
>### Results:
>- **Unscaled version** had low recovery, averaging around ~1.341 informative features per trial.
>- **Scaled version** performed significantly better, recovering ~1.668 informative features on average.
>### Logistic regression vs decision trees
>- **Trees do not require feature scaling**, since splits are based on thresholds.
>- **Logistic regression is scale-sensitive**, so raw features may distort the importance rankings.

(e) Does scaling features affect the result for decision trees? Explain.    

>[!FAQ] Answer
>No, scaling features doesn't affect the result for decision trees.
>Feature scaling has a significant impact on logistic regression but not on decision trees due to the fundamental differences in how these models interpret feature values.
>- Logistic regression requires scaling because its feature importance is derived from magnitude-sensitive coefficients.
>- Decision trees do **not** require scaling because they rely on threshold-based, ordering-driven splits that are **insensitive to the absolute scale** of input features.
>

(f) We now want to assess how often the two models (Decision trees and logistic regression (with scaling)) identify the same features as being important. Using the set-up of part (c), for each trial, record the number of overlaps for the top-5 ranked features for each of the two models. Plot a histogram of the number of overlaps over all trials. For example, if on a particular trial, DT has $[1,2,3,4,5]$ in its top-5, and Logistic regression has $[1,2,6,7,8]$ , the number of overlaps for this trial is 2.  

>[!note] ScreenShot
>
>![[Pasted image 20250327162435.png|550]]
>
>![[Pasted image 20250327162928.png]]

>[!note] Commentary
>Compare the top-5 most important features selected by two models: **decision trees** and **logistic regression (with scaling)**. Using the setup from Q1(c), we repeat the experiment 1000 times.
In each trial:
>- We generate a dataset with 5 informative and 15 redundant features.
>- Features are standardized and shuffled using a fixed permutation.
>- A decision tree is trained using information gain (entropy), and the top-5 features are selected based on impurity reduction.
>- A logistic regression model is trained without regularization, and top-5 features are selected based on absolute coefficient values.
>- We compare the original feature indices of both models’ top-5 and count how many features overlap.
>
>This confirms that the two models, despite being trained on the same data, emphasize **different feature selection criteria**:
>- Decision trees use local splitting rules based on thresholds;
>- Logistic regression reflects global linear dependencies.

(g) The approaches considered so far are called ”model-based” feature importance methods, since they define importance with respect to a particular algorithm/model being used. Discuss some potential disadvantages of using a model-based approach if your goal is to uncover truly important features, referring to the previous exercises for evidence. For example, suppose that you are studying a rare genetic disease and that the 20 features represent specific genetic features, only 5 of which are truly associated with the disease. Further, discuss the effect of the number of redundant features used when creating the data set.    

>[!important] Answer
>Model-based feature importance methods assign importance scores based on how features interact with a **particular algorithm**, such as a decision tree or logistic regression. While these approaches are practical and widely used, they come with significant limitations — especially when the goal is to **discover truly important features**, rather than just optimize predictive performance.
>### Disadvantages of Model-Based Feature Importance
>1. Model Dependence
>	- Different models use different mechanisms to evaluate importance
>	- Decision trees rely on information gain from feature-based splits;
>	- Logistic regression uses coefficient magnitudes (which are scale-sensitive).
>1. Sensitivity to Data Redundancy
>In **Q1(c)**, decision trees averaged **only 1.4 informative features recovered**, despite 5 being present. This is largely because the 15 redundant features are **correlated with informative ones**, leading the tree to distribute importance across redundant features. Logistic regression (unscaled) in **Q1(d)** performed even worse.
>2. Model Biases and Overfitting
>Decision trees may overfit on noisy or redundant features. Logistic regression may misestimate importance without proper feature scaling (see **Q1d**). These technical artifacts can mislead interpretation if one assumes feature importance reflects real-world relevance.
>### Application: Genetic Research
>- A tree may prioritize redundant features due to random splits.
>- Logistic regression may highlight large-valued but irrelevant markers (if unscaled).
>- We may **miss real genetic signals** because the model is optimizing for accuracy, not interpretability.
>### Effect on redundant features
Adding redundant features significantly reduces model interpretability:
>- It **dilutes** the importance of informative features;
>- Makes feature rankings **unstable**;
>- Increases risk of **spurious correlations** and misleading conclusions.
>
>As shown in our experiments, when redundant features dominate the dataset, model-based methods struggle to recover more than 2–3 truly informative features.
# Question 2. Greedy Feature Selection    
We now consider a different approach to feature selection known as backward selection. In backward selection, we:    
1. start with all features in the model 
2. at each round, we remove the $j$ -th feature from the model based on the drop in the value of a certain metric. We eliminate the feature corresponding to the smallest drop in the metric. 
3.  we repeat step 2 until there are no features left.     
(a) Why do you think this is referred to as a greedy feature importance algorithm? What do you think are some of the pitfalls of greedy algorithms in this context?     

>[!FAQ] Answer
>### Why greedy feature importance algorithm?
>The method is referred to as a **greedy feature importance algorithm** because it evaluates the contribution of each feature **one at a time**, based on **immediate local improvement** in the model’s performance (e.g., accuracy or error reduction), **without considering the global or long-term impact** of the feature in combination with others.
>
In typical greedy feature selection:
>- We start with an empty set of features.
>- At each step, the algorithm adds the **feature that most improves the model** when added alone or to the current subset.
>- This process repeats until a stopping criterion is met (e.g., fixed number of features, performance plateau). 
>### Pitfalls of Greedy Algorithms in This Context
>- **Ignoring Feature Interactions**  
$\qquad$A feature may appear unimportant by itself, but be highly predictive when combined with others. Greedy methods may discard such features too early.
>- **Suboptimal Feature Subset**  
> $\qquad$Since the method never “backtracks,” it may miss a globally better combination of features. Once a suboptimal feature is added, the algorithm cannot revise the decision.
>- **Biased Toward Early Choices**  
  >$\qquad$Early steps strongly influence later ones. If the first few features are only locally optimal, they can suppress the addition of truly informative features that correlate with them.
>- **Instability in Noisy or Redundant Data**  
>$\qquad$In the presence of many correlated (redundant) or noisy features, greedy selection can make poor decisions because multiple features carry overlapping information.

(b) Using the same set-up as in Question 1 part Q1 (a) write code implementing the backward elimination algorithm. Use a logistic regression model with no penalty, and the same metric as in Question 1 part (d). Be sure to generate the data without shuffling but then to shuffle the data before fitting the model. Report the remaining features at round 15 (that is, when only 5 features are left). How many of these are actually important features?     

>[!note] ScreenShot
>![[Pasted image 20250330144152.png]]

>[!note] Commentary
>We implemented a **greedy forward feature selection algorithm**, which adds one feature at a time based on the model’s cross-validated accuracy improvement. In each trial:
>- We standardize and shuffle the dataset.
>- Starting from an empty set, we iteratively select the next best feature (out of the remaining ones) that maximizes 3-fold cross-validated performance of a logistic regression model.
>- After selecting 5 features, we map them back to their original indices and compute how many truly informative features (original indices 0–4) were recovered.
>### Results:
>- The average number of informative features recovered was approximately **2**, higher than using model-based methods in Q1(c–f).
>- This shows that greedy selection can be more effective when combined with cross-validation, though it still may miss informative features due to feature redundancy and local optimality.

(c) Repeat part (a) for 1000 trials (similar to what is done in Q1 (c)). Plot a histogram of the number of important features recovered, and report the average number of recovered features.     

>[!note] ScreenShot
>![[Pasted image 20250330144903.png|550]]
>
>![[Pasted image 20250330144932.png]]

(d) Another approach is called best subset selection. This model generates all possible subsets, trains a model on each subset, evaluates the performance and returns the subset with the highest performance. For example, at the $t^{.}$ -th round, we consider all subsets with $t$ features. How does this algorithm compare to backward selection? Will it always outperform backward elimination? What are some disadvantages of this approach?     

>[!FAQ] Answer
>### How does this algorithm compare to backward selection?
>Best subset selection differs from backward selection in that it evaluates **all possible combinations** of features at each step, rather than greedily removing one feature at a time. This allows it to explore the **entire search space** and potentially identify feature subsets that backward elimination might miss. In contrast, backward selection makes a **locally optimal choice** at each step by removing the least important feature, which may lead to suboptimal final results if important features are removed early due to interactions with others. Therefore, best subset selection is more **exhaustive and comprehensive**, but at the cost of much higher computational overhead.
>### Will it always outperform backward elimination?
>In theory, best subset selection has the potential to outperform backward elimination because it does not rely on a greedy strategy and instead considers **all subsets** of a given size. As a result, it can identify the subset of features that truly yields the best model performance for the selected metric. However, in practice, it may not **consistently outperform** backward elimination, especially in the presence of noise, small datasets, or high-dimensional settings. Moreover, the performance gain may not always justify the additional computational cost.
>### What are some disadvantages of this approach?
>The primary disadvantage of best subset selection is its **computational complexity**, which grows exponentially with the number of features. For instance, evaluating all 5-feature subsets out of 20 features requires training over 15,000 models. This makes the method impractical for datasets with even a moderate number of features unless significant computational resources are available. Additionally, because it performs model fitting multiple times on the same data, it is also **prone to overfitting**, especially when using the training set to select the best subset. This can lead to poor generalization performance if not properly validated.

(e) Implement best subset selection in code. Repeat part (c) using your best subset implementation. For computational reasons, set all parameters as in Q1 part (a), but with only 7 features, 3 of which are to be taken to be informative, and the rest to be redundant. Plot a histogram as before and report the average number of recoveries. Comment on your results.   

>[!note] ScreenShot
>![[Pasted image 20250330145653.png|525]]
>
>![[Pasted image 20250330145722.png]]

>[!note] Commentary
>$\qquad$We performed Best Subset Selection over 1000 trials, selecting the best combination of 5 features from 7 candidates in each trial. The average number of truly informative features recovered was **1.87**, which is slightly better than decision trees and unregularized logistic regression, but **worse than greedy forward selection** and **L1 regularization**.
>$\qquad$This suggests that while Best Subset Selection has theoretical appeal, it can still struggle in highly redundant settings where **informative features are diluted** or **correlated** with noise. Evaluating combinations purely on performance metrics may not always yield the most interpretable or correct feature sets.

(f) An alternative approach to feature importance is known as the Permutation Feature Importance score, implemented in sklearn.inspection.permutation importance. Read the documentation and provide a detailed explanation of how permutation importance works. Compare it to the techniques studied so far in this homework, and explain why we refer to this as a modelindependent metric. Do you think it’s more or less fair to compare logistic regression and decision trees using this metric? Finally, using the sklearn implementation, re-do part Q2(c) using this new feature importance metric. Similar to before, use 20 features, with 5 to be set as informative and the rest as redundant.

>[!note] ScreenShot
>![[Pasted image 20250327200052.png|500]]
>
>![[Pasted image 20250327200144.png]]


>[!FAQ] Answer
>### Comparison to previous techniques
>- **Decision Tree importance** is based on the cumulative reduction in entropy (or Gini impurity) across all splits involving the feature.
>- **Logistic Regression importance** was based on the **absolute value of the learned coefficients**, which is inherently tied to the model’s form.
>- **L1 regularization** promotes sparsity but is still model-specific.
>- **Greedy / backward elimination** strategies also rely on model-specific scores at each step.
>
In contrast, permutation importance **only depends on model predictions**, making it **agnostic to how the model internally ranks or uses features**.
>### Is it a more fair comparison?
>Yes—**permutation importance is a more fair and consistent way to compare different models**, because:
>- It **standardizes the metric**: we judge all models by the same yardstick—how performance drops when a feature is corrupted.
>- It avoids issues like scale sensitivity (logistic regression) or overfitting in splits (decision trees).
>- It allows us to compare models on equal footing using **predictive performance** as the sole criterion.
>
>However, there are still caveats:
>- Highly correlated features may mask each other's importance when permuted.
>- Some models may be more robust to noise, causing smaller drops in performance.