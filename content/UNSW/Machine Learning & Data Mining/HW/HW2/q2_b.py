import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def backward_elimination(X, y):
    """
    Perform backward elimination using logistic regression with no penalty.
    At each step, remove the feature with the smallest absolute coefficient.
    Stop when only 5 features remain.
    """
    remaining = list(range(X.shape[1]))
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    while len(remaining) > 5:
        # Fit logistic regression on current features
        clf = LogisticRegression(penalty=None, solver='lbfgs', max_iter=500, random_state=4)
        clf.fit(X_scaled[:, remaining], y)

        # Get absolute coefficients
        coefs = np.abs(clf.coef_[0])

        # Identify feature with smallest absolute coefficient
        min_idx = np.argmin(coefs)
        feature_to_remove = remaining[min_idx]

        # Remove that feature
        remaining.remove(feature_to_remove)

    return remaining


# Generate data (informative features are first 5)
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=5,
    n_redundant=15,
    shuffle=False,
    random_state=4
)

# Apply backward elimination
selected_features = backward_elimination(X, y)

# Count how many informative features (index 0~4) are retained
num_informative = sum(1 for i in selected_features if i < 5)

# Output results
print(f"Remaining features at round 15: {selected_features}")
print(f"Number of informative features retained: {num_informative}")
