import numpy as np
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Storage for results
results_unscaled = []
results_scaled = []

for seed in range(1, 1001):
    # Step 1: Generate dataset
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=5,
                               n_redundant=15, shuffle=False, random_state=seed)

    # Step 2: Shuffle feature columns (fixed pattern)
    shuffled_idxs = np.random.default_rng(seed=0).permutation(X.shape[1])

    # === Unscaled version ===
    X_unscaled = X[:, shuffled_idxs]
    clf_unscaled = LogisticRegression(penalty=None, solver='lbfgs', max_iter=1000)
    clf_unscaled.fit(X_unscaled, y)
    coefs_unscaled = np.abs(clf_unscaled.coef_[0])
    top5_unscaled = np.argsort(coefs_unscaled)[::-1][:5]
    top5_unscaled_original = [shuffled_idxs[i] for i in top5_unscaled]
    recovered_unscaled = sum(idx < 5 for idx in top5_unscaled_original)
    results_unscaled.append(recovered_unscaled)

    # === Scaled version ===
    X_scaled = StandardScaler().fit_transform(X)
    X_scaled = X_scaled[:, shuffled_idxs]
    clf_scaled = LogisticRegression(penalty=None, solver='lbfgs', max_iter=1000)
    clf_scaled.fit(X_scaled, y)
    coefs_scaled = np.abs(clf_scaled.coef_[0])
    top5_scaled = np.argsort(coefs_scaled)[::-1][:5]
    top5_scaled_original = [shuffled_idxs[i] for i in top5_scaled]
    recovered_scaled = sum(idx < 5 for idx in top5_scaled_original)
    results_scaled.append(recovered_scaled)


# Print average recoveries
avg_unscaled = np.mean(results_unscaled)
avg_scaled = np.mean(results_scaled)
print("Average informative features recovered (unscaled):", avg_unscaled)
print("Average informative features recovered (scaled):", avg_scaled)

# === Plot histograms ===
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(results_unscaled, bins=range(7), align='left', rwidth=0.8, edgecolor='black')
plt.title("Logistic Regression (Unscaled)")
plt.xlabel("Number of Informative Features Recovered")
plt.ylabel("Frequency")
plt.xticks(range(6))

plt.subplot(1, 2, 2)
plt.hist(results_scaled, bins=range(7), align='left', rwidth=0.8, edgecolor='black')
plt.title("Logistic Regression (Scaled)")
plt.xlabel("Number of Informative Features Recovered")
plt.ylabel("Frequency")
plt.xticks(range(6))

plt.tight_layout()
plt.savefig("Q1d_logreg_scaled_vs_unscaled.png")
plt.show()


