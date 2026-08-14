# Feature engineering overview

Feature engineering is the process of selecting, transforming, and creating features from raw data to improve machine learning model performance. It transforms data into formats that help models learn patterns more effectively.

## 1. Best practices

### 1.1. General guidelines

#### **Understand Your Data**
   - Visualize distributions before transformations
   - Check for missing values and outliers
   - Understand feature types and relationships

#### **Handle Missing Values First**
   - Impute before scaling or transforming
   - Consider creating indicator variables

#### **Document Everything**
   - Track all transformations for reproducibility
   - Maintain data dictionaries
   - Use version control

#### **Test Multiple Approaches**
   - Try different transformations
   - Compare model performance
   - Use cross-validation

#### **Use Pipelines**
   - <a href="https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html" target="_blank">**Sklearn pipelines**</a> ensure consistency
   - Prevent data leakage
   - Simplify deployment

#### **Check Feature Importance**
   - Remove low-importance features
   - Reduce dimensionality
   - Improve model interpretability

#### **Validate Assumptions**
   - Verify transformations achieve desired effect
   - Check for normality when needed
   - Ensure proper scaling

### 1.2. Common pitfalls

| **Pitfall** | **Problem** | **Solution** |
|-------------|-------------|--------------|
| **Log of zero/negative** | Mathematical error | Use <code>np.log1p()</code> or Yeo-Johnson |
| **High-cardinality one-hot** | Too many features | Use feature hashing or target encoding |
| **Ordinal for nominal** | Implies false ordering | Use one-hot encoding instead |
| **Outliers before scaling** | Compresses distribution | Handle outliers first or use robust scalers |
| **Keeping all dummy columns** | Multicollinearity | Use <code>drop_first=True</code> |
| **Not documenting steps** | Irreproducible | Document all transformations |
| **Feature leakage** | Overfitting | Use only past/available information |
| **Forgetting to transform test data** | Inconsistent preprocessing | Apply same transformations to test set |

---

## 2. Feature engineering workflow

### 2.1. Standard pipeline

```
1. Understand the Data
   ↓
2. Create New Features (mathematical combinations)
   ↓
3. Transform Features (log, sqrt, power, quantile)
   ↓
4. Scale Features (min-max or standard scaling)
   ↓
5. Encode Categories (ordinal, one-hot, or hashing)
   ↓
6. Group & Aggregate (create group-based features)
   ↓
7. Validate & Test (check feature importance, correlations)
   ↓
8. Ready for Model Training!
```

### 2.2. Key principles

1. **Visualize First**: Understand distributions before transforming
2. **Domain Knowledge**: Let subject matter expertise guide feature creation
3. **Iterative Process**: Test transformations and evaluate impact
4. **Document Everything**: Track all transformations for reproducibility
5. **Avoid Leakage**: Don't use future information in feature creation
6. **Test Impact**: Validate that engineered features improve model performance

---

## 3. Transformation selection guide

### 3.1. By data characteristics

| **Data Characteristic** | **Recommended Transformation** | **Reason** |
|------------------------|-------------------------------|------------|
| **Right-skewed** | Log or Power Transformation | Compresses large values, spreads small values |
| **Moderate skew** | Square root | Gentler compression than log |
| **Count data** | Square root or log(x+1) | Stabilizes variance |
| **Unknown distribution** | Power Transformation (Yeo-Johnson) | Automatically finds optimal transformation |
| **Negative values** | Power Transformation (Yeo-Johnson) | Handles negative values without constant |
| **Heavy outliers** | Quantile Transformation | Most robust to extreme values |
| **Need uniform distribution** | Quantile Transformation (uniform) | Maps to [0,1] with uniform spread |
| **Normally distributed** | No transformation needed | Already suitable for most algorithms |
| **Bounded range needed** | Min-Max scaling | Maps to [0,1] or custom range |
| **Unbounded, mixed scale** | Standard scaling | Centers and standardizes |

### 3.2. By transformation type

| **Transformation** | **When to Use** | **Advantages** | **Limitations** |
|-------------------|----------------|----------------|----------------|
| **Log** | Right-skewed, positive values | Simple, interpretable | Cannot handle zero/negative |
| **Square Root** | Moderate skew, count data | Gentler than log | Only non-negative values |
| **Power** | Unknown optimal transformation | Automated, handles negatives (Yeo-Johnson) | Standardizes output |
| **Quantile** | Heavy outliers, unknown distribution | Most robust, no assumptions | Distorts linear relationships |
| **Min-Max** | Neural networks, bounded data | Preserves shape, bounded output | Sensitive to outliers |
| **Standard** | Normal data, linear models | Less sensitive to outliers | Unbounded output |

---

## 4. Core feature engineering techniques

### 4.1. Feature transformations

Modify scale, distribution, or nature of features to improve model suitability.

#### Sklearn transformers API

All sklearn preprocessing transformers follow a consistent pattern:
- **`fit(X)`**: Learn parameters from data
- **`transform(X)`**: Apply learned transformation
- **`fit_transform(X)`**: Combine both steps

```python
import pandas as pd
from sklearn.preprocessing import PowerTransformer

# Apply a power transform to a dataframe
transformer = PowerTransformer()
df_transformed = transformer.fit_transform(df)

# Convert back to DataFrame with column names
df_transformed = pd.DataFrame(
    X_transformed,
    columns=transformer.get_feature_names_out(),
    index=df.index
)
```

#### Transformation methods

<table>
  <thead>
    <tr>
      <th><strong>Method</strong></th>
      <th><strong>Implementation</strong></th>
      <th><strong>Use Case</strong></th>
      <th><strong>Key Features</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Log</strong></td>
      <td><code>np.log()</code> or <code>np.log1p()</code></td>
      <td>Right-skewed data</td>
      <td>Simple, interpretable; use <code>log1p()</code> for zeros</td>
    </tr>
    <tr>
      <td><strong>Square Root</strong></td>
      <td><code>np.sqrt()</code></td>
      <td>Moderately skewed, count data</td>
      <td>Gentler than log</td>
    </tr>
    <tr>
      <td><strong>Power</strong></td>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html" target="_blank"><code>PowerTransformer()</code></a></td>
      <td>Unknown distribution, negative values</td>
      <td>Box-Cox (positive) or Yeo-Johnson (any values)</td>
    </tr>
    <tr>
      <td><strong>Quantile</strong></td>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html" target="_blank"><code>QuantileTransformer()</code></a></td>
      <td>Heavy outliers, non-parametric</td>
      <td>Maps to uniform or normal distribution</td>
    </tr>
  </tbody>
</table>

### 4.2. Feature scaling

Standardize feature ranges to ensure equal contribution to model training.

<table>
  <thead>
    <tr>
      <th><strong>Method</strong></th>
      <th><strong>Formula</strong></th>
      <th><strong>Output Range</strong></th>
      <th><strong>Outlier Sensitivity</strong></th>
      <th><strong>Distribution</strong></th>
      <th><strong>Best For</strong></th>
      <th><strong>Implementation</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Min-Max</strong></td>
      <td>(X - X_min) / (X_max - X_min)</td>
      <td>[0, 1] or custom</td>
      <td>High</td>
      <td>Preserves shape</td>
      <td>Neural networks, bounded data, known bounds, no extreme outliers</td>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html" target="_blank"><code>MinMaxScaler()</code></a></td>
    </tr>
    <tr>
      <td><strong>Standard</strong></td>
      <td>(X - μ) / σ</td>
      <td>Unbounded (typically -3 to +3)</td>
      <td>Moderate</td>
      <td>Centers around 0</td>
      <td>Normal data, linear models, PCA, unknown bounds, data with outliers</td>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html" target="_blank"><code>StandardScaler()</code></a></td>
    </tr>
  </tbody>
</table>

### 4.3. Feature encoding

Convert categorical variables into numeric format for machine learning algorithms.

<table>
  <thead>
    <tr>
      <th><strong>Method</strong></th>
      <th><strong>Output</strong></th>
      <th><strong>Dimensionality</strong></th>
      <th><strong>Ordinal Assumption</strong></th>
      <th><strong>Memory</strong></th>
      <th><strong>Reversible</strong></th>
      <th><strong>Best For</strong></th>
      <th><strong>Implementation</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Ordinal</strong></td>
      <td>Single integer column</td>
      <td>No increase</td>
      <td>Yes</td>
      <td>Efficient</td>
      <td>Yes</td>
      <td>Ordered categories, tree models, binary categories</td>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html" target="_blank"><code>OrdinalEncoder()</code></a></td>
    </tr>
    <tr>
      <td><strong>One-Hot</strong></td>
      <td>Multiple binary columns</td>
      <td>+n_categories</td>
      <td>No</td>
      <td>Can be large</td>
      <td>Yes</td>
      <td>Nominal data, linear models, few categories</td>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html" target="_blank"><code>OneHotEncoder()</code></a></td>
    </tr>
    <tr>
      <td><strong>Feature Hashing</strong></td>
      <td>Fixed-size sparse matrix</td>
      <td>Fixed size</td>
      <td>No</td>
      <td>Very efficient</td>
      <td>No</td>
      <td>High-cardinality features, many categories</td>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html" target="_blank"><code>FeatureHasher()</code></a></td>
    </tr>
  </tbody>
</table>

### 4.4. Grouping operations

Create aggregate features by splitting data into groups, applying functions, and combining results.

**Common Usage**: <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html" target="_blank"><code>df.groupby()</code></a>

```python
# Basic aggregation
df.groupby('city')['price'].mean()

# Multiple functions
df.groupby('category').agg(['mean', 'sum', 'count'])

# Convert to DataFrame
result = df.groupby('city')['price'].mean().reset_index()
```

**Common Functions**: `sum()`, `mean()`, `max()`, `min()`, `count()`, `std()`, `median()`

**Applications**:
- Aggregate features (customer total purchases)
- Group statistics (average price by city)
- Ratio features (value / group_mean)
- Deviation features (value - group_median)
- Target encoding (mean target by category)

---

## Additional resources

### Python libraries

- **[pandas](https://pandas.pydata.org/)**: Data manipulation, <code>get_dummies()</code>, <code>groupby()</code>
- **[numpy](https://numpy.org/)**: Mathematical transformations (<code>log</code>, <code>sqrt</code>)
- **[scikit-learn](https://scikit-learn.org/)**: Preprocessing, scaling, encoding, feature extraction
- **[scipy](https://scipy.org/)**: Advanced statistical transformations

### Key sklearn modules

- **[sklearn.preprocessing](https://scikit-learn.org/stable/api/sklearn.preprocessing.html)**: Transformers, scalers, encoders
- **[sklearn.feature_extraction](https://scikit-learn.org/stable/modules/feature_extraction.html)**: Feature hashing, text features
- **[sklearn.pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)**: Chaining transformations

### Recommended reading

- <a href="https://scikit-learn.org/stable/modules/preprocessing.html" target="_blank">**Scikit-learn Preprocessing Guide**</a>: Comprehensive guide to data preprocessing
- <a href="https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/" target="_blank">**"Feature Engineering for Machine Learning"**</a> by Alice Zheng & Amanda Casari
- <a href="https://www.kaggle.com/learn/feature-engineering" target="_blank">**Kaggle Feature Engineering Course**</a>: Hands-on tutorials and examples
