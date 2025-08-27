import numpy as np
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend to avoid GUI conflicts
import matplotlib.pyplot as plt

# Generate synthetic classification data with 20 features,
# of which 5 are informative and 15 are redundant
X, y = make_classification(n_samples=1000, n_features=20, n_informative=5,
                           n_redundant=15, shuffle=False, random_state=0)

# Normalize the feature values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Shuffle the feature columns using a fixed seed for reproducibility
shuffled_idxs = np.random.default_rng(seed=0).permutation(X.shape[1])
X_shuffled = X_scaled[:, shuffled_idxs]

# Train a decision tree using entropy as the splitting criterion
clf = DecisionTreeClassifier(criterion='entropy', random_state=4)
clf.fit(X_shuffled, y)

# Get feature importance scores from the trained tree
importance = clf.feature_importances_
# Identify the top 5 most important features
top_5 = np.argsort(importance)[-5:][::-1]

# Count how many of the top 5 features are actually informative (original indices 0–4)
recovered = sum(idx in shuffled_idxs[:5] for idx in top_5)
print(f"Recovered informative features: {recovered}/5")

# Step 7: Plot sorted importance with feature indices as x-axis labels
sorted_idx = np.argsort(importance)[::-1]  # Sort by importance
sorted_importance = importance[sorted_idx]
sorted_feature_labels = [shuffled_idxs[idx] for idx in sorted_idx]  # Map back to original indices
plt.figure(figsize=(10, 5))
plt.bar(range(len(importance)), sorted_importance)
plt.xticks(ticks=range(len(importance)), labels=sorted_feature_labels)
plt.xlabel("Feature Index (sorted by importance)")
plt.ylabel("Feature Importance Score")
plt.title("Decision Tree Feature Importance Histogram")
plt.tight_layout()
plt.savefig("Q1a_feature_importance_index_labels.png")
plt.show()



