import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import log_loss
from itertools import combinations
from tqdm import tqdm


def best_subset_selection(X, y, k=3):
    """
    Searches all k-feature subsets and returns the one with the lowest training error (log-loss).
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    best_loss = np.inf
    best_subset = None

    for subset in combinations(range(X.shape[1]), k):
        model = LogisticRegression(penalty=None, solver='lbfgs', max_iter=500, random_state=4)
        model.fit(X_scaled[:, subset], y)

        # Evaluate train error via log-loss
        probs = model.predict_proba(X_scaled[:, subset])
        loss = log_loss(y, probs)

        if loss < best_loss:
            best_loss = loss
            best_subset = subset

    return best_subset


# Run 1000 trials
recovered_counts = []

for i in tqdm(range(1, 1001)):
    X, y = make_classification(n_samples=1000, n_features=7, n_informative=3,
                               n_redundant=4, shuffle=False, random_state=i)
    best_features = best_subset_selection(X, y)
    recovered = sum(1 for idx in best_features if idx < 3)  # informative features are 0,1,2
    recovered_counts.append(recovered)

# Plot histogram
plt.hist(recovered_counts, bins=np.arange(5) - 0.5, edgecolor='black')
plt.xticks(range(4))
plt.xlabel("Number of Informative Features Recovered")
plt.ylabel("Frequency")
plt.title("Best Subset Selection (1000 Trials, 7 features, k=3)")
plt.tight_layout()
plt.show()

# Report average
average_recovered = np.mean(recovered_counts)
print(f"Average number of informative features recovered over 1000 trials: {average_recovered:.2f}")
