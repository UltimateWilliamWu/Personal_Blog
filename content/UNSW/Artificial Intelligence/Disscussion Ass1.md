## 🔍 Assignment Summary & Discussion Preparation

### ✅ Overview of Tasks

This assignment consists of two main tasks:
- **Task A**: Binary classification to detect hot events.
- **Task B**: Regression to predict monthly temperatures in the Amazon region.

For Task B, I implemented:
- A **random split**, which randomly partitions the dataset into training/validation/test.
- A **year-wise split**, where each year appears in only one split to simulate forecasting future years.

---

### ⚙️ Model Architectures

- All models used **three Dense layers**.
- **Classification model**: `Dense(16) → Dense(8) → Dense(1, activation='sigmoid')`
- **Regression model**: `Dense(32) → Dense(16) → Dense(1)`
- Hidden layers used **ReLU** activation.  
- Regression output used **linear activation** (i.e., no activation function).

---

### 📦 Batch Size

- Batch size used in all models: **32**
- Defined in `model.fit(batch_size=32, ...)`

---

### 🔁 Data Preprocessing

- **Input features** were standardized using `StandardScaler`.
- **Month** was encoded using **cyclic encoding**: `Month_sin`, `Month_cos`.
- For **year-wise regression only**, the **target temperature** was normalized using a separate `MinMaxScaler`, as allowed by the assignment.
- Random-split regression **must not** normalize the target variable (as per step (l) in the instructions).

---

### 📈 Evaluation Metrics

- **Classification**: Balanced Accuracy, Sensitivity (TPR), Specificity (TNR)
- **Regression**: Pearson Correlation Coefficient (r), Mean Absolute Error (MAE)

---

### 📉 Overfitting & Solutions

#### How to detect:
- Training loss continues to drop while validation loss increases.

#### Solutions used:
- `EarlyStopping` to stop training when val_loss plateaus.
- `Dropout` layers to reduce overfitting.
- `L2 regularization` in dense layers.
- Smaller network sizes to reduce capacity.

---

### 🎯 Optimizer and Learning Rate

- I used the **Adam** optimizer.
- Default learning rate: **0.001**
- Though not explicitly set, it can be customized via:
  ```python
  Adam(learning_rate=0.001)
```
### ❓ Why does year-wise split perform better?

1. **No data leakage**: Year-wise split ensures no overlapping years between train/test.
    
2. **Better generalization**: Forces the model to learn temporal patterns that generalize.
    
3. **Realistic scenario**: Simulates prediction on future, unseen years.
    
4. **Preserved seasonality**: Keeps entire years intact, maintaining time consistency.
    
5. **Avoids memorization**: Random split can let the model memorize month-specific patterns.
### 🔍 Activation Functions Used

|Function|Applied To|Purpose|
|---|---|---|
|`ReLU`|Hidden layers (all models)|Introduce non-linearity, avoid vanishing gradients|
|`Sigmoid`|Classifier output layer|Outputs probability for binary classification|
|Linear|Regressor output layer|Predicts continuous temperature values|
### 📉 Hidden Test Evaluation Notes

- Lower performance on the hidden test set is expected due to:
    
    - Different year distribution
        
    - No exposure to hidden years during training
        
- `UserWarning: feature names mismatch` → Caused by passing DataFrame to scaler fitted on NumPy
    
- `tf.function retracing` warnings → Safe to ignore unless looping over models dynamically