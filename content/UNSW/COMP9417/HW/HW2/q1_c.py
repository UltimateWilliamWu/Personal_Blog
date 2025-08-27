import numpy as np
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Store number of informative features recovered in each trial
results = []

for seed in range(1, 1001):
    # Step 1: Generate dataset (5 informative, 15 redundant)
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=5,
                               n_redundant=15, shuffle=False, random_state=seed)

    # Step 2: Normalize the data
    X_scaled = StandardScaler().fit_transform(X)

    # Step 3: Shuffle the feature columns (fixed seed = 0 for reproducibility)
    shuffled_idxs = np.random.default_rng(seed=0).permutation(X.shape[1])
    X_shuffled = X_scaled[:, shuffled_idxs]

    # Step 4: Train decision tree
    clf = DecisionTreeClassifier(criterion='entropy', random_state=4)
    clf.fit(X_shuffled, y)

    # Step 5: Get feature importances (indices in shuffled space)
    importances = clf.feature_importances_
    top5 = np.argsort(importances)[::-1][:5]  # top-5 indices in shuffled space

    # Step 6: Map back to original feature indices
    top5_original = [shuffled_idxs[idx] for idx in top5]

    # Step 7: Count how many of them are from the original informative features (indices 0–4)
    recovered = sum(idx < 5 for idx in top5_original)
    results.append(recovered)

# Step 8: Plot histogram
plt.hist(results, bins=range(7), edgecolor='black')
plt.title("Recovery of Informative Features (Decision Tree, 1000 Trials)")
plt.xlabel("Number of Informative Features Recovered")
plt.ylabel("Frequency")
plt.xticks(range(6))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("Q1c_recovery_decision_tree_fixed.png")
plt.show()

# Step 9: Report average
print("Average recovery:", np.mean(results))
