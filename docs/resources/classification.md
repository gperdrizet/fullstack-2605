# Classification overview

Classification models predict categorical target variables by learning decision boundaries that separate different classes. This guide covers essential classification techniques, evaluation metrics, and best practices for building effective classifiers.

## 1. Best practices

### 1.1. General guidelines

#### **Start Simple**
   - Begin with logistic regression or Naive Bayes
   - Add complexity only when justified
   - Compare models systematically

#### **Always Split Your Data**
   - Use train-test split (70-30 or 80-20)
   - Set `random_state` for reproducibility
   - Never fit scalers/transformers on test data

#### **Check Class Balance**
   - Examine class distribution before training
   - Apply balancing techniques if needed
   - Use stratified splits for imbalanced data

#### **Scale Your Features**
   - Essential for KNN and SVM
   - Beneficial for logistic regression
   - Not needed for decision trees
   - Use `StandardScaler` after train-test split

#### **Use Cross-Validation**
   - Provides robust performance estimates
   - Use Stratified K-Fold for imbalanced data
   - Use `cross_val_score()` for quick evaluation

#### **Choose Appropriate Metrics**
   - Don't rely solely on accuracy
   - Use precision, recall, F1 for imbalanced data
   - Consider business context (FP vs FN costs)

#### **Visualize Results**
   - Plot confusion matrix
   - Examine ROC curves
   - Use Precision-Recall curves for imbalanced data

#### **Document Everything**
   - Track preprocessing steps
   - Record hyperparameters
   - Note performance metrics

### 1.2. Common pitfalls

| **Pitfall** | **Problem** | **Solution** |
|-------------|-------------|--------------|
| **Using accuracy for imbalanced data** | Misleading performance | Use precision, recall, F1-score |
| **Not scaling features** | Poor KNN/SVM performance | Standardize features |
| **Ignoring class imbalance** | Biased toward majority class | Use SMOTE, undersampling, or class weights |
| **Overfitting decision trees** | Poor generalization | Use pruning (max_depth, min_samples_split) |
| **Wrong metric choice** | Misaligned with business goals | Consider cost of FP vs FN |
| **Not using cross-validation** | Unreliable estimates | Use Stratified K-Fold |
| **Applying balancing before split** | Data leakage | Balance after train-test split |
| **Using ROC for imbalanced data** | Overly optimistic | Use Precision-Recall curve |
| **Not tuning hyperparameters** | Suboptimal performance | Use GridSearchCV or RandomizedSearchCV |
| **Ignoring probability calibration** | Poor probability estimates | Consider threshold tuning |


## 2. Classification workflow

```
1. Data Loading & Exploration
   ↓
2. Check Class Balance
   ↓
3. Train-Test Split (stratified if imbalanced)
   ↓
4. Data Preprocessing
   - Handle missing values
   - Encode categorical variables
   - Scale numerical features (if needed)
   ↓
5. Apply Balancing Techniques (if needed)
   - SMOTE
   - Undersampling
   ↓
6. Model Selection & Training
   - Logistic Regression
   - Naive Bayes
   - KNN
   - Decision Tree
   - SVM
   ↓
7. Cross-Validation (Stratified K-Fold)
   ↓
8. Model Evaluation
   - Confusion matrix
   - Accuracy, precision, recall, F1
   - ROC curve and AUC
   - Precision-Recall curve (for imbalanced data)
   ↓
9. Hyperparameter Tuning
   ↓
10. Final Model Selection
   ↓
11. Predictions on Test Set
```

---

## 3. Model selection guide

| **Algorithm** | **Data Considerations** | **Regularization** | **Strengths** | **Weaknesses** |
|---------------|-------------------------|-------------------|---------------|----------------|
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html" target="_blank">**Logistic Regression**</a> | Feature scaling beneficial; handles binary and multiclass; check for multicollinearity | L1 (Lasso), L2 (Ridge), ElasticNet | Fast, interpretable, provides probabilities; linear decision boundary; good baseline | Assumes linearity; poor with non-linear relationships; may need feature engineering |
| <a href="https://scikit-learn.org/stable/modules/naive_bayes.html" target="_blank">**Naive Bayes**</a> | No scaling needed; works well with small datasets; handles high dimensions | None (probabilistic) | Very fast training/prediction; good baseline; handles missing data; works with small datasets | Assumes feature independence (often violated); can be outperformed by other models |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html" target="_blank">**K-Nearest Neighbors**</a> | Feature scaling critical; remove irrelevant features; handle missing values | None (instance-based) | Simple concept; no training phase; non-parametric; naturally handles multiclass | Slow predictions; memory intensive; sensitive to feature scaling; curse of dimensionality |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html" target="_blank">**Decision Trees**</a> | Minimal preprocessing; no scaling required; handles mixed data types; can handle missing values | Pruning (max_depth, min_samples_split, min_samples_leaf) | Highly interpretable; handles non-linear relationships; no scaling needed; visualizable | Prone to overfitting; unstable; biased toward features with more levels |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html" target="_blank">**Support Vector Machines**</a> | Feature scaling critical; works well in high dimensions; effective with clear margins | C parameter (regularization), kernel parameters | Effective in high dimensions; memory efficient; versatile kernels; good with clear margins | Slow with large datasets; difficult to interpret; sensitive to kernel choice; requires scaling |


## 4. Performance metrics

Performance metrics evaluate how well a classifier distinguishes between classes and the types of errors it makes.

### 4.1. Metric comparison

| **Metric** | **Formula** | **Range** | **Best For** | **Limitations** |
|------------|-------------|-----------|--------------|-----------------|
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html" target="_blank">**Accuracy**</a> | $(TP + TN) / \text{Total}$ | 0-1 | Balanced datasets | Misleading for imbalanced data |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html" target="_blank">**Precision**</a> | $TP / (TP + FP)$ | 0-1 | Minimizing false positives | Ignores false negatives |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html" target="_blank">**Recall**</a> | $TP / (TP + FN)$ | 0-1 | Minimizing false negatives | Ignores false positives |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html" target="_blank">**F1-Score**</a> | $2 \times \frac{P \times R}{P + R}$ | 0-1 | Balancing precision and recall | Equal weight to both metrics |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html" target="_blank">**AUC-ROC**</a> | Area under ROC curve | 0-1 | Balanced datasets | Optimistic for imbalanced data |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html" target="_blank">**AUCPR**</a> | Area under PR curve | 0-1 | Imbalanced datasets | More conservative than AUC |

### 4.2. Confusion matrix

The confusion matrix shows all combinations of predicted vs. actual class labels:

|                | **Predicted Positive** | **Predicted Negative** |
|----------------|------------------------|------------------------|
| **Actual Positive** | True Positive (TP)     | False Negative (FN)    |
| **Actual Negative** | False Positive (FP)    | True Negative (TN)     |

**Key terms**:
- **TP**: Correctly predicted positive cases
- **TN**: Correctly predicted negative cases
- **FP**: Type I error (false alarm)
- **FN**: Type II error (missed detection)

**Best practice**: Use <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html" target="_blank">`confusion_matrix()`</a> and visualize with heatmap

### 4.3. When to use each metric

| **Scenario** | **Recommended Metrics** | **Rationale** |
|--------------|------------------------|---------------|
| **Balanced classes** | Accuracy, F1, AUC-ROC | All metrics reliable |
| **Imbalanced classes** | Precision, Recall, F1, AUCPR | Accuracy misleading |
| **False positives costly** | Precision | Minimize FP (e.g., spam detection) |
| **False negatives costly** | Recall | Minimize FN (e.g., disease detection) |
| **Both FP and FN important** | F1-Score | Balances precision and recall |
| **Threshold-independent evaluation** | AUC-ROC, AUCPR | Evaluates across all thresholds |


## 5. Core classification techniques

These techniques are crucial for successful classification modeling with any algorithm. Proper application of cross-validation, imbalanced data handling, and hyperparameter tuning significantly improves model performance.

### 5.1. Cross-validation

Trains and evaluates model on multiple train-validation splits to estimate generalization performance.

**Cross-validation functions:**
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html" target="_blank">`cross_val_score()`</a>: Returns array of scores for each fold
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html" target="_blank">`cross_validate()`</a>: Returns dict with scores, folds, fit times, etc

**Cross-validation fold generators:**
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html" target="_blank">**Stratified K-Fold**</a>: Maintains class proportions in each fold (recommended for classification)
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html" target="_blank">**K-Fold**</a>: Standard k equal folds
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html" target="_blank">**Repeated Stratified K-Fold**</a>: Multiple runs with different random splits

### 5.2. Handling imbalanced data

Address class imbalance to prevent bias toward majority class.

<table>
  <thead>
    <tr>
      <th><strong>Technique</strong></th>
      <th><strong>Type</strong></th>
      <th><strong>How It Works</strong></th>
      <th><strong>Best For</strong></th>
      <th><strong>Implementation</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>SMOTE</strong></td>
      <td>Oversampling</td>
      <td>Generates synthetic minority samples</td>
      <td>Moderate imbalance</td>
      <td><a href="https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html" target="_blank"><code>SMOTE()</code></a> from imblearn</td>
    </tr>
    <tr>
      <td><strong>Random Undersampling</strong></td>
      <td>Undersampling</td>
      <td>Randomly removes majority class samples</td>
      <td>Large datasets</td>
      <td><a href="https://imbalanced-learn.org/stable/references/generated/imblearn.under_sampling.RandomUnderSampler.html" target="_blank"><code>RandomUnderSampler()</code></a> from imblearn</td>
    </tr>
    <tr>
      <td><strong>Class Weights</strong></td>
      <td>Algorithm parameter</td>
      <td>Penalizes misclassification of minority class</td>
      <td>Slight imbalance</td>
      <td><code>class_weight='balanced'</code> in most sklearn classifiers</td>
    </tr>
  </tbody>
</table>

**Key considerations:**
- Apply balancing **after** train-test split to avoid data leakage
- Use Stratified K-Fold for cross-validation
- Evaluate with precision, recall, F1, and AUCPR

### 5.3. Hyperparameter tuning

Systematically searches for optimal model parameters.

<table>
  <thead>
    <tr>
      <th><strong>Method</strong></th>
      <th><strong>Strategy</strong></th>
      <th><strong>Pros</strong></th>
      <th><strong>Cons</strong></th>
      <th><strong>Implementation</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Grid Search</strong></td>
      <td>Exhaustive search of parameter grid</td>
      <td>Guaranteed to find best in grid</td>
      <td>Computationally expensive</td>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html" target="_blank"><code>GridSearchCV</code></a></td>
    </tr>
    <tr>
      <td><strong>Random Search</strong></td>
      <td>Random sampling from distributions</td>
      <td>More efficient, explores wider space</td>
      <td>May miss optimal combination</td>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html" target="_blank"><code>RandomizedSearchCV</code></a></td>
    </tr>
  </tbody>
</table>

**Common hyperparameters to tune:**

| **Algorithm** | **Key Hyperparameters** |
|---------------|------------------------|
| **Logistic Regression** | `C` (regularization strength), `penalty` (L1, L2, ElasticNet) |
| **KNN** | `n_neighbors` (k), `weights` (uniform, distance), `metric` (euclidean, manhattan) |
| **Decision Tree** | `max_depth`, `min_samples_split`, `min_samples_leaf`, `criterion` (gini, entropy) |
| **SVM** | `C` (regularization), `gamma` (kernel coefficient), `kernel` (linear, rbf, poly) |

---

## Additional resources

### Python libraries

- **[scikit-learn](https://scikit-learn.org)**: Comprehensive ML library
  - [`linear_model`](https://scikit-learn.org/stable/modules/linear_model.html): LogisticRegression
  - [`naive_bayes`](https://scikit-learn.org/stable/modules/naive_bayes.html): GaussianNB, MultinomialNB, BernoulliNB
  - [`neighbors`](https://scikit-learn.org/stable/modules/neighbors.html): KNeighborsClassifier
  - [`tree`](https://scikit-learn.org/stable/modules/tree.html): DecisionTreeClassifier
  - [`svm`](https://scikit-learn.org/stable/modules/svm.html): SVC
  - [`model_selection`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection): train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
  - [`metrics`](https://scikit-learn.org/stable/modules/model_evaluation.html): confusion_matrix, classification_report, roc_curve, precision_recall_curve
- **[imbalanced-learn](https://imbalanced-learn.org/)**: Handling imbalanced datasets
  - [`over_sampling`](https://imbalanced-learn.org/stable/references/over_sampling.html): SMOTE
  - [`under_sampling`](https://imbalanced-learn.org/stable/references/under_sampling.html): RandomUnderSampler
  - [`pipeline`](https://imbalanced-learn.org/stable/references/pipeline.html): Pipeline (imbalanced-aware)

### Key sklearn modules

- **[sklearn.linear_model](https://scikit-learn.org/stable/modules/linear_model.html)**: Logistic regression and variants
- **[sklearn.model_selection](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection)**: Train-test split, CV, tuning
- **[sklearn.metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)**: Classification metrics
- **[sklearn.preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)**: Feature scaling and encoding

### Recommended reading

- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html" target="_blank">**Scikit-learn Classification Guide**</a>: Comprehensive classification documentation
- <a href="https://www.statlearning.com/" target="_blank">**"Introduction to Statistical Learning"**</a> by James, Witten, Hastie, Tibshirani
- <a href="https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/" target="_blank">**"Hands-On Machine Learning"**</a> by Aurélien Géron
- <a href="https://imbalanced-learn.org/stable/" target="_blank">**Imbalanced-learn Documentation**</a>: Guide to handling imbalanced datasets
