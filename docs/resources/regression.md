# Regression overview

Regression models predict continuous target variables by learning relationships between input features and outputs. This guide covers essential regression techniques, evaluation metrics, and best practices for building effective predictive models.

## 1. Best practices

### 1.1. General guidelines

#### **Start Simple**
   - Begin with linear regression
   - Add complexity only when justified
   - Compare models systematically

#### **Always Split Your Data**
   - Use train-test split (70-30 or 80-20)
   - Set `random_state` for reproducibility
   - Never fit scalers/transformers on test data

#### **Scale Your Features**
   - Essential for regularized regression
   - Use `StandardScaler` after train-test split
   - Apply same transformation to test data

#### **Use Cross-Validation**
   - Provides robust performance estimates
   - K-Fold (k=5 or k=10) is standard
   - Use `cross_val_score()` for quick evaluation

#### **Monitor Overfitting**
   - Compare training vs test performance
   - Large gap indicates overfitting
   - Use regularization if needed

#### **Leverage Pipelines**
   - Combine preprocessing and modeling
   - Prevents data leakage
   - Simplifies deployment
   - Use `sklearn.pipeline.Pipeline`

#### **Document Everything**
   - Track preprocessing steps
   - Record hyperparameters
   - Note performance metrics

### 1.2. Common pitfalls

| **Pitfall** | **Problem** | **Solution** |
|-------------|-------------|--------------|
| **Not splitting data** | Can't evaluate generalization | Always use train-test split |
| **Data leakage** | Overly optimistic results | Fit transformers only on training data |
| **Ignoring overfitting** | Poor test performance | Monitor train vs test metrics |
| **Wrong metric** | Misleading conclusions | Use multiple metrics (MSE, MAE, R²) |
| **Skipping cross-validation** | Unreliable estimates | Use K-Fold cross-validation |
| **Not scaling** | Regularization ineffective | Standardize features |
| **Categorical encoding errors** | Model can't learn | Use one-hot or ordinal encoding |
| **Missing values** | Training fails or biased | Impute before modeling |
| **High multicollinearity** | Unstable coefficients | Use Ridge or ElasticNet |

## 2. Regression workflow

```
1. Data Loading & Inspection
   ↓
2. Train-Test Split
   ↓
3. Exploratory Data Analysis
   ↓
4. Data Preprocessing
   - Handle missing values
   - Encode categorical variables
   - Scale numerical features
   ↓
5. Model Selection & Training
   - Linear regression
   - Regularized regression
   - Other models as appropriate
   ↓
6. Cross-Validation
   ↓
7. Model Evaluation (RSS, MSE, RMSE, MAE, R²)
   ↓
8. Hyperparameter Tuning
   ↓
9. Final Model Selection
   ↓
10. Predictions on Test Set
```


## 3. Model selection guide

| **Algorithm** | **Data Considerations** | **Regularization** | **Strengths** | **Weaknesses** |
|---------------|-------------------------|-------------------|---------------|----------------|
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html" target="_blank">**Linear Regression**</a> | Remove or handle outliers; check for multicollinearity (VIF); may need feature scaling for regularized versions | Lasso (L1), Ridge (L2), ElasticNet | Simple, fast, interpretable; works well with linear relationships; provides feature importance via coefficients | Assumes linearity; sensitive to outliers; poor with non-linear patterns; affected by multicollinearity |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html" target="_blank">**K-Nearest Neighbors**</a> | Feature scaling required (StandardScaler, MinMaxScaler); remove irrelevant features; handle missing values | None (non-parametric) | No training phase; simple concept; naturally handles multi-class; non-parametric (no assumptions) | Slow predictions; memory intensive; sensitive to feature scaling; struggles with high dimensions (curse of dimensionality) |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html" target="_blank">**Decision Trees**</a> | Minimal preprocessing needed; handles missing values; no scaling required; can handle mixed data types | Pruning (max_depth, min_samples_split, min_samples_leaf) | Interpretable; handles non-linear relationships; no feature scaling needed; captures interactions | Prone to overfitting; unstable (small data changes cause big tree changes); biased toward features with more levels |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html" target="_blank">**Support Vector Machines**</a> | Feature scaling critical (StandardScaler); remove outliers; ensure balanced classes for classification | C parameter (controls margin), kernel parameters | Effective in high dimensions; memory efficient; works well with clear margins; robust to outliers (with proper kernel) | Slow with large datasets; sensitive to kernel choice; requires feature scaling; difficult to interpret |
| <a href="https://scikit-learn.org/stable/modules/neural_networks_supervised.html" target="_blank">**Neural Networks**</a> | Feature scaling required; handle missing values; may need normalization; consider data augmentation for small datasets | L1, L2, Dropout, Early stopping, Batch normalization | Highly flexible; captures complex non-linear patterns; scales well with large data; automatic feature learning | Computationally expensive; requires large datasets; black box (hard to interpret); sensitive to hyperparameters; prone to overfitting |


## 4. Performance metrics

Performance metrics quantify the difference between model predictions and true values of the label. When using for training a metric is referred to as the 'loss'.

| **Metric** | **Formula** | **Units** | **Outlier Sensitivity** | **Best For** |
|------------|-------------|-----------|-------------------------|--------------|
| **RSS** | $\sum(y_i - \hat{y}_i)^2$ | Squared | Highest | OLS optimization |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html" target="_blank">**MSE**</a> | $\frac{1}{n}\sum(y_i - \hat{y}_i)^2$ | Squared | Higher | Higher penalty for larger errors |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html" target="_blank">**RMSE**</a> | $\sqrt{\text{MSE}}$ | Same as y | High | Interpretable magnitude, penalizes large errors less than MSE, but more then MAE |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html" target="_blank">**MAE**</a> | $\frac{1}{n}\sum\|y_i - \hat{y}_i\|$ | Same as y | Low | Robust to outliers |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html" target="_blank">**R²**</a> | $1 - \frac{\text{SS}\_\{\text{res}\}}{\text{SS}\_\{\text{tot}\}}$ | 0 to 1 | Moderate | Variance explained |

**Best practice**: Report multiple metrics for comprehensive evaluation


## 5. Core regression techniques

These techniques are crucial for successful regression modeling with any algorithm. Proper application of cross-validation, regularization, and hyperparameter tuning significantly improves model performance and generalization across all regression methods.

### 5.1. Cross-validation

Trains and evaluates model on multiple train-validation splits called 'folds' to estimate generalization performance without overusing the test set.

#### **Cross-validation functions:**
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html" target="_blank">`cross_val_score()`</a>: Returns array of scores for each fold
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html" target="_blank">`cross_validate()`</a>: Returns dict with scores, folds, fit times, etc for each fold

#### **Cross-validation fold generators**:
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html" target="_blank">**K-Fold**</a>: k equal folds, each used once for validation
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html" target="_blank">**Leave-One-Out (LOOCV)**</a>: k = n (very computationally expensive)
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html" target="_blank">**Repeated K-Fold**</a>: Multiple K-Fold runs with different splits
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html" target="_blank">**Time Series Split**</a>: Preserves temporal order

### 5.2. Regularization methods

Add penalty terms to prevent overfitting and handle multicollinearity.

| **Method** | **Penalty** | **Feature selection** | **Best for** | **Implementation** |
|---|---|---|---|---|
| **Lasso (L1)** | $\alpha \sum\|\beta_j\|$ | Yes (sets coefficients to 0) | Sparse models, irrelevant features | [`Lasso(alpha=1.0)`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html) |
| **Ridge (L2)** | $\alpha \sum \beta_j^2$ | No (shrinks but keeps all) | Multicollinearity, all features relevant | [`Ridge(alpha=1.0)`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) |
| **ElasticNet** | $\lambda_1 \sum\|\beta_j\| + \lambda_2 \sum \beta_j^2$ | Partial (some set to 0) | Both multicollinearity and sparse features | [`ElasticNet(alpha=1.0, l1_ratio=0.5)`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html) |

#### **Key parameter**:
- **alpha (α)**: Controls regularization strength
  - Higher α → stronger penalty → simpler model
  - Lower α → weaker penalty → more complex model
  - Use cross-validation to find optimal value

### 5.3. Hyperparameter tuning

Systematically searches for optimal model parameters.

| **Method** | **Strategy** | **Pros** | **Cons** | **Implementation** |
|---|---|---|---|---|
| **Grid search** | Exhaustive search of parameter grid | Guaranteed to find best in grid | Computationally expensive | [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) |
| **Random search** | Random sampling from distributions | More efficient, explores wider space | May miss optimal combination | [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html) |

## Additional resources

### Python libraries

- **[scikit-learn](https://scikit-learn.org)**: Comprehensive ML library
  - [`linear_model`](https://scikit-learn.org/stable/modules/linear_model.html): LinearRegression, Lasso, Ridge, ElasticNet
  - [`model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html): train_test_split, cross_val_score, GridSearchCV
  - [`metrics`](https://scikit-learn.org/stable/modules/model_evaluation.html): mean_squared_error, mean_absolute_error, r2_score
  - [`pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html): Pipeline, ColumnTransformer
- **[scipy](https://scipy.org/)**: Scientific computing library
  - [`stats`](https://docs.scipy.org/doc/scipy/reference/stats.html): Statistical functions, distributions, hypothesis tests
  - [`optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html): Optimization algorithms for parameter estimation
  - [`linalg`](https://docs.scipy.org/doc/scipy/reference/linalg.html): Linear algebra operations for matrix computations

### Key sklearn modules

- **[sklearn.linear_model](https://scikit-learn.org/stable/modules/linear_model.html)**: All regression algorithms
- **[sklearn.model_selection](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection)**: Train-test split, CV, tuning
- **[sklearn.metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)**: Performance metrics
- **[sklearn.pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)**: Workflow management

### Recommended reading

- <a href="https://scikit-learn.org/stable/modules/linear_model.html" target="_blank">**Scikit-learn Linear Models Guide**</a>: Comprehensive regression documentation
- <a href="https://www.statlearning.com/" target="_blank">**"Introduction to Statistical Learning"**</a> by James, Witten, Hastie, Tibshirani
- <a href="https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/" target="_blank">**"Hands-On Machine Learning"**</a> by Aurélien Géron
