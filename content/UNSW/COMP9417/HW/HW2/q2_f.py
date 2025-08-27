import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import permutation_importance
from tqdm import tqdm

# Use permutation importance over 1000 trials
recovered_counts = []

for i in tqdm(range(1, 1001)):
    # Create dataset
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=5,
                               n_redundant=15, shuffle=False, random_state=i)

    # Fit model
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = LogisticRegression(penalty=None, solver='lbfgs', max_iter=500, random_state=4)
    model.fit(X_scaled, y)

    # Compute permutation importance
    result = permutation_importance(model, X_scaled, y, n_repeats=5,
                                    random_state=4, scoring='accuracy', n_jobs=-1)

    # Take top 5 features by mean importance
    top5_indices = np.argsort(result.importances_mean)[::-1][:5]
    recovered = sum(1 for idx in top5_indices if idx < 5)
    recovered_counts.append(recovered)

# Plot results
plt.hist(recovered_counts, bins=np.arange(7) - 0.5, edgecolor='black')
plt.xticks(range(6))
plt.xlabel("Number of Informative Features Recovered (Permutation Importance)")
plt.ylabel("Frequency")
plt.title("Q2(f): Permutation Feature Importance (1000 Trials)")
plt.tight_layout()
plt.show()

# Print average
avg = np.mean(recovered_counts)
print(f"Average number of informative features recovered using permutation importance: {avg:.3f}")
