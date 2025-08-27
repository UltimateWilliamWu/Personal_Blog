# Re-import required libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# ------Question 1 Data cleaning------
# Load dataset
data = pd.read_csv("heart.csv")

# (a) Separate features and target, remove 'Last Checkup'
X = data.drop(columns=['Heart_Disease', 'Last_Checkup'])
y = data['Heart_Disease']

# (b) Fix negative ages
X['Age'] = X['Age'].abs()

# (c) Standardize 'Gender' and 'Smoker' values
X['Gender'] = X['Gender'].replace({'Female': 'F', 'Male': 'M', 'Unknown': 'Unknown'})
X['Smoker'] = X['Smoker'].replace({'No': 'N', 'Yes': 'Y'})

# Encode categorical variables
X['Gender'] = X['Gender'].map({'M': 0, 'F': 1, 'Unknown': 2})
X['Smoker'] = X['Smoker'].map({'N': 0, 'Y': 1, np.nan: 2})

# (d) Split Blood Pressure into Systolic and Diastolic
X[['Systolic', 'Diastolic']] = X['Blood_Pressure'].str.split('/', expand=True).apply(pd.to_numeric, errors='coerce')
X = X.drop(columns=['Blood_Pressure'])

# (e) Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)

# (f) Impute missing Age values in test set
median_male_age = X_train.loc[X_train['Gender'] == 0, 'Age'].dropna().median()
median_female_age = X_train.loc[X_train['Gender'] == 1, 'Age'].dropna().median()
X_test.loc[(X_test['Gender'] == 0) & (X_test['Age'].isnull()), 'Age'] = median_male_age
X_test.loc[(X_test['Gender'] == 1) & (X_test['Age'].isnull()), 'Age'] = median_female_age

# (g) Apply Min-Max Scaling to selected columns
scaler = MinMaxScaler()
cols_to_scale = ['Age', 'Height_feet', 'Weight_kg', 'Cholesterol', 'Systolic', 'Diastolic']
X_train[cols_to_scale] = scaler.fit_transform(X_train[cols_to_scale])
X_test[cols_to_scale] = scaler.transform(X_test[cols_to_scale])

# (h) Create new binary target variable
plt.hist(y_train, bins=20, edgecolor='black')
plt.xlabel('Heart Disease')
plt.ylabel('Frequency')
plt.title('Histogram of Heart Disease')
plt.show()
y_train_binary = (y_train > 0.1).astype(int)
y_test_binary = (y_test > 0.1).astype(int)

# ------Question 2 ------
# Q(2)b Grid search over C values and plot log-loss
C_values = np.logspace(-4, 4, 100)
train_losses = []
test_losses = []

for C in C_values:
    model = LogisticRegression(penalty='l2', solver='lbfgs', C=C, max_iter=1000)
    model.fit(X_train, y_train_binary)

    # Predict probabilities
    y_train_pred_proba = model.predict_proba(X_train)[:, 1]
    y_test_pred_proba = model.predict_proba(X_test)[:, 1]

    # Compute log-loss
    train_losses.append(log_loss(y_train_binary, y_train_pred_proba))
    test_losses.append(log_loss(y_test_binary, y_test_pred_proba))

# Plot train and test log-loss
plt.figure(figsize=(8, 6))
plt.plot(C_values, train_losses, label="Train Log-Loss", marker='o')
plt.plot(C_values, test_losses, label="Test Log-Loss", marker='s')
plt.xscale("log")
plt.xlabel("C (Inverse of Regularization Strength)")
plt.ylabel("Log-Loss")
plt.title("Train and Test Log-Loss vs C")
plt.legend()
plt.grid(True)
plt.show()

# Q2(c) Define 5-fold cross-validation manually
N = len(X_train)
fold_size = N // 5
C_values = np.logspace(-4, 4, 100)

cv_results = {C: [] for C in C_values}

# Perform manual 5-fold cross-validation
for C in C_values:
    fold_losses = []

    for i in range(5):
        # Define fold indices
        val_start = i * fold_size
        val_end = (i + 1) * fold_size if i < 4 else N  # Ensure last fold takes remaining data

        # Split train and validation sets manually
        X_fold_train = pd.concat([X_train.iloc[:val_start], X_train.iloc[val_end:]])
        y_fold_train = pd.concat([y_train_binary.iloc[:val_start], y_train_binary.iloc[val_end:]])
        X_fold_val = X_train.iloc[val_start:val_end]
        y_fold_val = y_train_binary.iloc[val_start:val_end]

        # Train model on training folds
        model = LogisticRegression(penalty='l2', solver='lbfgs', C=C, max_iter=1000)
        model.fit(X_fold_train, y_fold_train)

        # Predict probabilities on validation fold
        y_val_pred_proba = model.predict_proba(X_fold_val)[:, 1]

        # Compute log-loss for this fold
        fold_losses.append(log_loss(y_fold_val, y_val_pred_proba))

    # Store cross-validation losses for this C value
    cv_results[C] = fold_losses

# Convert results to DataFrame for visualization
cv_df = pd.DataFrame(cv_results)

# Plot cross-validation log-loss as a boxplot
plt.figure(figsize=(10, 5))
cv_df.boxplot()
plt.xscale("log")
plt.xlabel("C (Inverse of Regularization Strength)")
plt.ylabel("Log-Loss")
plt.title("5-Fold Cross-Validation Log-Loss for Different C Values")
plt.grid(True)
plt.show()

# Find the best C (one with the lowest mean log-loss)
best_C_manual = min(cv_results, key=lambda C: np.mean(cv_results[C]))

# Train final model with best C and report accuracy
final_model = LogisticRegression(penalty='l2', solver='lbfgs', C=best_C_manual, max_iter=1000)
final_model.fit(X_train, y_train_binary)

y_train_pred = final_model.predict(X_train)
y_test_pred = final_model.predict(X_test)

train_accuracy = final_model.score(X_train, y_train_binary)  # accuracy_score(y_train_binary, y_train_pred)
test_accuracy = final_model.score(X_test, y_test_binary)  # accuracy_score(y_test_binary, y_test_pred)

# Q2(d) Define logistic regression model
logreg = LogisticRegression(penalty='l2', solver='lbfgs', max_iter=1000)

# Define hyperparameter grid
param_grid = {'C': np.logspace(-4, 4, 100)}

# Implement GridSearchCV with 5-fold cross-validation
grid_search = GridSearchCV(logreg, param_grid, scoring='neg_log_loss', cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train_binary)

# Get best C value
best_C_sklearn = grid_search.best_params_['C']

# Train model with best C from GridSearchCV
final_model_sklearn = LogisticRegression(penalty='l2', solver='lbfgs', C=best_C_sklearn, max_iter=1000)
final_model_sklearn.fit(X_train, y_train_binary)

y_train_pred_sklearn = final_model_sklearn.predict(X_train)
y_test_pred_sklearn = final_model_sklearn.predict(X_test)

train_accuracy_sklearn = accuracy_score(y_train_binary, y_train_pred_sklearn)
test_accuracy_sklearn = accuracy_score(y_test_binary, y_test_pred_sklearn)

# Optimized Manual CV
kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=2)
cv_results_optimized = {C: [] for C in C_values}

for C in C_values:
    fold_losses = []

    for train_idx, val_idx in kf.split(X_train, y_train_binary):
        X_fold_train, X_fold_val = X_train.iloc[train_idx], X_train.iloc[val_idx]
        y_fold_train, y_fold_val = y_train_binary.iloc[train_idx], y_train_binary.iloc[val_idx]

        model = LogisticRegression(penalty='l2', solver='lbfgs', C=C, max_iter=1000)
        model.fit(X_fold_train, y_fold_train)

        y_val_pred_proba = model.predict_proba(X_fold_val)[:, 1]
        fold_losses.append(log_loss(y_fold_val, y_val_pred_proba))

    cv_results_optimized[C] = fold_losses

# Find best C from optimized manual cross-validation
best_C_optimized = min(cv_results_optimized, key=lambda C: np.mean(cv_results_optimized[C]))

models = {
    "Manual CV": best_C_manual,
    "GridSearchCV": best_C_sklearn,
    "Optimized Manual CV": best_C_optimized
}

final_results = {}
for method, best_C in models.items():
    model = LogisticRegression(penalty='l2', solver='lbfgs', C=best_C, max_iter=1000)
    model.fit(X_train, y_train_binary)

    train_accuracy = model.score(X_train, y_train_binary)
    test_accuracy = model.score(X_test, y_test_binary)

    final_results[method] = (best_C, train_accuracy, test_accuracy)

# Display final results
df_results = pd.DataFrame(final_results, index=["Best C", "Train Accuracy", "Test Accuracy"]).T
print(df_results)



