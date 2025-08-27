import numpy as np
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from tqdm import tqdm
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def backward_elimination(X, y):
    """
    Performs backward elimination using logistic regression.
    Returns the indices of the last 5 remaining features.
    """
    remaining = list(range(X.shape[1]))
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    while len(remaining) > 5:
        # Fit model on current features
        model = LogisticRegression(penalty=None, solver='lbfgs', max_iter=500, random_state=4)
        model.fit(X_scaled[:, remaining], y)

        # Get absolute coefficients
        coefs = np.abs(model.coef_[0])

        # Find the feature with the smallest abs coef
        min_idx = np.argmin(coefs)
        feature_to_remove = remaining[min_idx]

        # Remove that feature
        remaining.remove(feature_to_remove)

    return remaining


# Run 1000 trials
recovered_counts = []

for i in tqdm(range(1, 1001)):
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=5,
                               n_redundant=15, shuffle=False, random_state=i)
    selected = backward_elimination(X, y)
    recovered = sum(1 for idx in selected if idx < 5)  # informative features are indexed 0-4
    recovered_counts.append(recovered)

# Plot histogram
plt.hist(recovered_counts, bins=np.arange(7) - 0.5, edgecolor='black')
plt.xticks(range(6))
plt.xlabel("Number of Informative Features Retained")
plt.ylabel("Frequency")
plt.title("Backward Elimination: Recovery of Informative Features (1000 Trials)")
plt.tight_layout()
plt.show()

# Report average
avg_recovered = np.mean(recovered_counts)
print(f"Average number of informative features retained over 1000 trials: {avg_recovered:.2f}")
