# Ensemble methods overview

Ensemble learning combines multiple models to achieve better predictive performance than any single model. By leveraging the collective wisdom of diverse models, ensembles reduce variance, bias, and improve robustness across classification and regression tasks.

## 1. Best practices

### 1.1. Design guidelines

#### **Start Simple**
   - Begin with voting or averaging ensembles
   - Add complexity only when justified
   - Compare ensemble to best individual model

#### **Ensure Model Diversity**
   - Use different algorithms (voting, stacking)
   - Use different hyperparameters (bagging, boosting)
   - Train on different data subsets (bagging)
   - Different models should make different errors

#### **Use Cross-Validation**
   - Essential for robust performance estimates
   - Use Stratified K-Fold for classification
   - Prevents overfitting to validation set

#### **Leverage OOB Scores**
   - Use out-of-bag estimates for bagging
   - Free validation without separate holdout
   - Reliable performance indicator

#### **Monitor Training Time**
   - Parallel ensembles (bagging) train faster
   - Sequential ensembles (boosting) take longer
   - Balance accuracy gains with computational cost

#### **Tune Systematically**
   - Start with number of estimators
   - Then tune base model parameters
   - Use grid or random search
   - More estimators ≠ always better

#### **Prevent Overfitting**
   - Use regularization in boosting
   - Limit tree depth in bagging
   - Monitor training vs validation performance
   - Stop early if performance plateaus

#### **Choose Appropriate Base Models**
   - Weak learners for boosting (shallow trees)
   - Stronger learners for bagging
   - Diverse algorithms for voting/stacking
   - Match complexity to data size

### 1.2. Common pitfalls

| **Pitfall** | **Problem** | **Solution** |
|-------------|-------------|--------------|
| **Identical base models** | No diversity, limited improvement | Use different algorithms or hyperparameters |
| **Too many estimators** | Diminishing returns, overfitting | Find plateau in learning curves |
| **Wrong ensemble for data** | Suboptimal performance | Bagging for high variance, boosting for high bias |
| **Not using diverse models** | Weak ensemble in voting/stacking | Combine different algorithm types |
| **Ignoring computation cost** | Impractical for deployment | Consider parallel options (bagging) |
| **Overfitting with boosting** | Poor generalization | Use regularization, limit iterations |
| **Data leakage in stacking** | Overly optimistic results | Use out-of-fold predictions for meta-model |
| **Skipping hyperparameter tuning** | Suboptimal ensemble | Tune n_estimators, learning_rate, max_depth |
| **Using soft voting without probabilities** | Runtime error | Ensure base models have predict_proba |
| **Complex ensemble for simple problem** | Unnecessary overhead | Start with simpler models first |

## 2. Ensemble selection guide

| **Technique** | **Training** | **Best For** | **Primary Benefit** | **Computational Cost** |
|---------------|-------------|--------------|---------------------|----------------------|
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html" target="_blank">**Voting**</a> | Parallel | Combining diverse models quickly | Simple, robust predictions | Low (trains models once) |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html" target="_blank">**Bagging**</a> | Parallel | Reducing variance, stabilizing predictions | Variance reduction | Medium (parallelizable) |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html" target="_blank">**Random Forest**</a> | Parallel | General-purpose, out-of-the-box performance | Balanced performance | Medium (parallelizable) |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html" target="_blank">**AdaBoost**</a> | Sequential | Reducing bias, simple implementation | Bias reduction | Medium (sequential) |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html" target="_blank">**Gradient Boosting**</a> | Sequential | High accuracy, flexible loss functions | Bias + variance reduction | High (sequential) |
| <a href="https://xgboost.readthedocs.io/" target="_blank">**XGBoost**</a> | Sequential | Large datasets, competitions | Speed + accuracy | Medium (optimized) |
| <a href="https://catboost.ai/" target="_blank">**CatBoost**</a> | Sequential | Categorical features, minimal tuning | Automatic categorical handling | Medium (optimized) |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html" target="_blank">**Stacking**</a> | Parallel + Meta | Maximum accuracy from diverse models | Leverages algorithm strengths | High (multiple layers) |

## 3. Core ensemble techniques

### 3.1. Voting and averaging

Combines predictions from multiple independent models through voting (classification) or averaging (regression).

#### **Hard voting (classification)**:
   - Each model votes for a class
   - Final prediction: majority vote
   - Simple and interpretable

#### **Soft voting (classification)**:
- Uses probability estimates from each model
- Averages probabilities across models
- Often more accurate than hard voting
- Requires models with `predict_proba()`

#### **Averaging (regression)**:
- Mean of all model predictions
- Reduces variance
- Simple weighted average optional

#### **When to use**:
- Quick ensemble from existing diverse models
- Combining models with different strengths
- Need for interpretable ensemble
- Balanced datasets

### 3.2. Bagging

Bootstrap Aggregating trains multiple models on random subsets (with replacement) and aggregates predictions.

#### **How it works**:
1. Create bootstrap samples (random sampling with replacement)
2. Train separate model on each sample
3. Aggregate via voting (classification) or averaging (regression)
4. Each model sees ~63% of training data

#### **Key advantages**:
- Reduces variance
- Prevents overfitting
- Parallelizable (fast training)
- Out-of-bag (OOB) error estimation

#### **Random Forest**: Bagging with decision trees plus random feature selection at each split

#### **When to use**:
- High-variance models (deep decision trees)
- Overfitting issues
- Need for parallelization
- Want built-in validation (OOB)

### 3.3. Boosting

Sequential ensemble where each model corrects errors of previous models by focusing on difficult instances.

**Common boosting algorithms**:

<table>
  <thead>
    <tr>
      <th><strong>Algorithm</strong></th>
      <th><strong>Key Features</strong></th>
      <th><strong>Best For</strong></th>
      <th><strong>Key Hyperparameters</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html" target="_blank"><strong>AdaBoost</strong></a></td>
      <td>Adjusts instance weights based on errors</td>
      <td>Simple boosting, binary classification</td>
      <td><code>n_estimators</code>, <code>learning_rate</code></td>
    </tr>
    <tr>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html" target="_blank"><strong>Gradient Boosting</strong></a></td>
      <td>Fits to residual errors, flexible loss functions</td>
      <td>High accuracy, small to medium data</td>
      <td><code>n_estimators</code>, <code>learning_rate</code>, <code>max_depth</code></td>
    </tr>
    <tr>
      <td><a href="https://xgboost.readthedocs.io/" target="_blank"><strong>XGBoost</strong></a></td>
      <td>Optimized gradient boosting, regularization, handles missing data</td>
      <td>Large datasets, competitions, production</td>
      <td><code>n_estimators</code>, <code>learning_rate</code>, <code>max_depth</code>, <code>reg_alpha</code>, <code>reg_lambda</code></td>
    </tr>
    <tr>
      <td><a href="https://catboost.ai/" target="_blank"><strong>CatBoost</strong></a></td>
      <td>Native categorical feature handling, automatic preprocessing</td>
      <td>Categorical-heavy data, minimal tuning</td>
      <td><code>n_estimators</code>, <code>learning_rate</code>, <code>depth</code></td>
    </tr>
  </tbody>
</table>

#### **When to use**:
- Have sufficient training time
- High-bias problems
- Structured/tabular data
- Production systems (XGBoost, CatBoost)

### 3.4. Stacking

Multi-level ensemble where base models (level 0) make predictions used as features for meta-model (level 1).

#### **How it works**:
1. Train diverse base models on training data
2. Generate out-of-fold predictions for training set
3. Train meta-model on base model predictions
4. Final prediction from meta-model

#### **Common meta-models**:
- Logistic Regression (most common for classification)
- Linear Regression (for regression)
- Ridge/Lasso (with regularization)
- Simple models often work best

#### **Key considerations**:
- Use `cv` parameter to generate out-of-fold predictions
- Prevents data leakage and overfitting
- Base models should be diverse
- More complex but often highest accuracy

#### **When to use**:
- Maximum accuracy needed
- Have computational resources
- Diverse algorithms available
- Competition or high-stakes applications


## 4. Ensemble comparison

### 4.1. Strengths and limitations

| **Technique** | **Strengths** | **Limitations** |
|---------------|---------------|-----------------|
| **Voting** | Simple, interpretable, fast | Limited improvement if models too similar |
| **Bagging** | Reduces variance, parallelizable, OOB validation | Limited on high-bias models, memory intensive |
| **Random Forest** | Out-of-the-box performance, handles high dimensions | Less interpretable, memory intensive |
| **Boosting** | High accuracy, reduces bias and variance | Prone to overfitting, sequential (slower), sensitive to noise |
| **Stacking** | Highest accuracy potential, leverages diversity | Complex, computationally expensive, harder to interpret |

### 4.2. When to use each

| **Scenario** | **Recommended Technique** | **Why** |
|-------------|---------------------------|---------|
| **High variance problem** | Bagging, Random Forest | Averages out fluctuations |
| **High bias problem** | Boosting | Sequential error correction |
| **Need speed** | Bagging, Random Forest | Parallelizable |
| **Maximum accuracy** | XGBoost, Stacking | State-of-the-art performance |
| **Interpretability important** | Voting, Bagging with shallow trees | Simpler structure |
| **Large dataset** | XGBoost, CatBoost | Optimized implementations |
| **Categorical features** | CatBoost | Native categorical handling |
| **Limited tuning time** | Random Forest, CatBoost | Good defaults |
| **Noisy data** | Bagging | More robust than boosting |
| **Imbalanced classes** | Boosting | Focuses on difficult instances |

## 5. Basic ensemble workflow

```
1. Start with Individual Models
   - Train several models
   - Evaluate baseline performance
   ↓
2. Choose Ensemble Strategy
   - Voting: Quick combination
   - Bagging: High variance
   - Boosting: Need accuracy
   - Stacking: Maximum performance
   ↓
3. Train Ensemble
   - Use cross-validation
   - Monitor OOB scores (bagging)
   - Track learning curves (boosting)
   ↓
4. Tune Hyperparameters
   - n_estimators (all)
   - learning_rate (boosting)
   - max_depth (trees)
   ↓
5. Evaluate and Compare
   - Compare to best individual model
   - Check training vs test performance
   - Consider computational cost
   ↓
6. Select Final Model
   - Balance accuracy, speed, interpretability
```

## Additional resources

### Python libraries

- **[scikit-learn](https://scikit-learn.org)**: Core ensemble modules
  - [`ensemble`](https://scikit-learn.org/stable/modules/ensemble.html): VotingClassifier, BaggingClassifier, RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, StackingClassifier
  - [`model_selection`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection): cross_val_score, GridSearchCV, RandomizedSearchCV
  - [`sklearn.pipeline`](https://scikit-learn.org/stable/modules/compose.html): Preprocessing+estimator pipelines
- **[xgboost](https://xgboost.readthedocs.io/)**: Optimized gradient boosting
- **[catboost](https://catboost.ai/)**: Gradient boosting for categorical features
- **[lightgbm](https://lightgbm.readthedocs.io/)**: Fast gradient boosting framework
- **[vecstack](https://github.com/vecxoz/vecstack)**: Stacking with cross-validation support

### Recommended reading

- <a href="https://scikit-learn.org/stable/modules/ensemble.html" target="_blank">**Scikit-learn Ensemble Guide**</a>: Comprehensive ensemble documentation
- <a href="https://xgboost.readthedocs.io/en/stable/tutorials/model.html" target="_blank">**XGBoost Tutorial**</a>: Introduction to XGBoost
- <a href="https://www.statlearning.com/" target="_blank">**"Introduction to Statistical Learning"**</a>: Chapter 8 on Tree-Based Methods
