import numpy as np
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Store overlap counts between DT and LR top-5 features
overlap_counts = []

# Repeat experiment 1000 times
for seed in range(1, 1001):
    # Step 1: Generate synthetic data
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=5,
                               n_redundant=15, shuffle=False, random_state=seed)

    # Step 2: Standardize features
    X_scaled = StandardScaler().fit_transform(X)

    # Step 3: Shuffle feature columns (fixed shuffle pattern)
    shuffled_idxs = np.random.default_rng(seed=0).permutation(X.shape[1])
    X_shuffled = X_scaled[:, shuffled_idxs]

    # === Decision Tree ===
    clf_tree = DecisionTreeClassifier(criterion='entropy', random_state=4)
    clf_tree.fit(X_shuffled, y)
    importances_tree = clf_tree.feature_importances_
    top5_tree = np.argsort(importances_tree)[::-1][:5]
    top5_tree_original = set(shuffled_idxs[idx] for idx in top5_tree)

    # === Logistic Regression (no penalty, scaled input) ===
    clf_lr = LogisticRegression(penalty=None, solver='lbfgs', max_iter=1000)
    clf_lr.fit(X_shuffled, y)
    importances_lr = np.abs(clf_lr.coef_[0])
    top5_lr = np.argsort(importances_lr)[::-1][:5]
    top5_lr_original = set(shuffled_idxs[idx] for idx in top5_lr)

    # Step 4: Count overlap between DT and LR top-5 original indices
    overlap = len(top5_tree_original & top5_lr_original)
    overlap_counts.append(overlap)

# Step 6: Print average overlap
print("Average number of overlapping features:", np.mean(overlap_counts))

# Step 5: Plot histogram
plt.hist(overlap_counts, bins=range(7), edgecolor='black', rwidth=0.8, align='left')
plt.title("Top-5 Feature Overlap: Decision Tree vs Logistic Regression (scaled)")
plt.xlabel("Number of Overlapping Features")
plt.ylabel("Frequency")
plt.xticks(range(6))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("Q1f_DT_LR_top5_overlap.png")
plt.show()


