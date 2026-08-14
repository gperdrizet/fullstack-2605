# Data wrangling overview

Data wrangling is the process of cleaning, structuring, and transforming raw data into a format suitable for analysis. It is one of the most time-consuming step in data science projects, but is critical for obtaining reliable insights.

## 1. Best Practices

### 1.1. General Guidelines

1. **Always Inspect First**
   - Use `head()`, `info()`, `describe()` before any operations
   - Visualize data distributions and relationships
   - Understand data types and missing patterns

2. **Document Your Steps**
   - Keep track of all transformations applied
   - Use comments to explain non-obvious decisions
   - Maintain a data dictionary

3. **Preserve Original Data**
   - Work on copies for destructive operations: `df_clean = df.copy()`
   - Keep raw data intact for reproducibility
   - Version control your data processing scripts

4. **Validate Assumptions**
   - Check data distributions before transformations
   - Verify join results (check shapes, duplicate keys)
   - Test on sample data first

5. **Handle Missing Data Thoughtfully**
   - Understand why data is missing before choosing strategy
   - Document imputation methods used
   - Consider creating indicator variables for imputed values

6. **Be Consistent**
   - Apply same transformations across training and test sets
   - Use same encoding for categorical variables
   - Maintain consistent data types

7. **Watch for Data Leakage**
   - Don't use future information to transform past data
   - Fit imputers/scalers on training data only
   - Be careful with time series data

8. **Test Your Joins**
   - Verify join results match expectations
   - Check for unexpected duplicates
   - Ensure key columns don't have nulls

9. **Consider Memory**
   - Use appropriate data types (`int8` vs `int64`)
   - Drop unnecessary columns early
   - Process large datasets in chunks

10. **Automate When Possible**
    - Create reusable functions for repetitive tasks
    - Build data cleaning pipelines
    - Use configuration files for parameters

### 1.2. Common Pitfalls

| **Pitfall** | **Problem** | **Solution** |
|-------------|-------------|--------------|
| **Modifying original data** | Irreversible changes | Always work on copies: `df_new = df.copy()` |
| **Ignoring data types** | Incorrect operations | Check and convert types explicitly |
| **Not handling nulls before joins** | Unexpected missing matches | Handle nulls before merging |
| **Inconsistent handling across splits** | Data leakage, poor generalization | Fit on train, transform on train and test |
| **Dropping too much data** | Loss of information | Consider imputation before deletion |
| **Arbitrary imputation** | Artificial patterns | Choose imputation method based on data characteristics |
| **Not checking for duplicates** | Biased results | Always check and handle duplicates |
| **Ignoring outliers** | Skewed statistics | Investigate and handle appropriately |
| **Forgetting to reset index** | Index issues after filtering | Use `reset_index(drop=True)` |
| **Improper join keys** | Duplicate or missing matches | Validate key uniqueness before joining |
| **Not documenting transformations** | Irreproducible results | Document every step in code or notebook |
| **Assuming data is clean** | Propagating errors | Always inspect and validate data |


## 2. Data Wrangling Workflow

### 2.1. Standard Pipeline

```
1. Data Collection
   ↓
2. Data Inspection (understand structure, types, quality)
   ↓
3. Data Cleaning (standardize formats, fix errors)
   ↓
4. Data Integration (merge, join, concat)
   ↓
5. Data Aggregation (groupby, summarize)
   ↓
6. Data Reshaping (pivot, melt)
   ↓
7. Remove Duplicates (drop_duplicates)
   ↓
8. Handle Missing Values (fillna, dropna)
   ↓
9. Handle Outliers (winsorize, cap, remove)
   ↓
10. Ready for Analysis or Modeling!
```

### 2.2. Key Principles

1. **Understand Before Acting**: Always inspect data thoroughly before making changes
2. **Preserve Original Data**: Work on copies for destructive operations
3. **Document Everything**: Keep track of all transformations applied
4. **Be Consistent**: Apply same operations across training and test sets
5. **Validate Results**: Check data quality after each major operation
6. **Consider Context**: Let domain knowledge guide decisions
7. **Watch for Leakage**: Don't use future information to transform past data


## 3. Core Data Wrangling Operations

### 3.1. Data Inspection

Essential functions and methods for understanding your data:

| **Operation** | **Method** | **Purpose** | **Example** |
|---------------|------------|-------------|-------------|
| **View first/last rows** | `df.head()` / `df.tail()` | Quick data preview | `df.head(10)` |
| **Data types and memory** | `df.info()` | Column types, non-null counts, memory usage | `df.info()` |
| **Descriptive statistics** | `df.describe()` | Mean, std, min, max, quartiles | `df.describe()` |
| **Shape** | `df.shape` | Number of rows and columns | `rows, cols = df.shape` |
| **Column names** | `df.columns` | List all column names | `list(df.columns)` |
| **Data types** | `df.dtypes` | Type of each column | `df.dtypes` |
| **Missing values** | `df.isnull().sum()` | Count nulls per column | `df.isnull().sum()` |
| **Unique values** | `df['col'].unique()` | Get unique values | `df['category'].nunique()` |
| **Value counts** | `df['col'].value_counts()` | Frequency of each value | `df['category'].value_counts()` |
| **Correlation** | `df.corr()` | Correlation matrix | `df.corr()` |

**Access Methods:**
- **Row access**: `df.iloc[0]` (integer position), `df.loc['label']` (label-based)
- **Column access**: `df['col']` (single column), `df[['col1', 'col2']]` (multiple columns)
- **Boolean indexing**: `df[df['age'] > 30]` (filter rows)

**Quick Visualizations:**
- `df.hist()`: Histograms for all numeric columns
- `df.plot(kind='box')`: Box plots to identify outliers
- `df['col'].plot(kind='bar')`: Bar plot for categorical data
- `df.plot(x='col1', y='col2', kind='scatter')`: Scatter plot for relationships

### 3.2. Data Cleaning

Standardizing and correcting data formats:

| **Operation** | **Method** | **Purpose** | **Example** |
|---------------|------------|-------------|-------------|
| **Convert data types** | `astype()` | Change column types | `df['age'] = df['age'].astype(int)` |
| **Convert to datetime** | `pd.to_datetime()` | Standardize date formats | `df['date'] = pd.to_datetime(df['date'])` |
| **String operations** | `.str` accessor | Clean text data | `df['name'].str.lower()` |
| **Replace values** | `replace()` | Substitute specific values | `df.replace({'Yes': 1, 'No': 0})` |
| **Rename columns** | `rename()` | Standardize column names | `df.rename(columns={'old': 'new'})` |
| **Strip whitespace** | `.str.strip()` | Remove leading/trailing spaces | `df['col'].str.strip()` |
| **Standardize case** | `.str.lower()` / `.str.upper()` | Consistent text case | `df['name'].str.title()` |

### 3.3. Handling Missing Data

#### Missingness Types

- **MCAR (Missing Completely At Random)**: Missingness is random and unrelated to any values
- **MAR (Missing At Random)**: Missingness depends on observed data but not on missing values
- **MNAR (Missing Not At Random)**: Missingness depends on the missing values themselves

#### Detecting Missing data

| **Purpose** | **Method** | **Returns** | **Example** |
|-------------|------------|-------------|-------------|
| Check if values are null | `isnull()` / `isna()` | Boolean DataFrame | `df.isnull()` |
| Check if values are not null | `notnull()` / `notna()` | Boolean DataFrame | `df.notnull()` |
| Count missing values per column | `isnull().sum()` | Series with counts | `df.isnull().sum()` |
| Total missing values in DataFrame | `isnull().sum().sum()` | Integer | `df.isnull().sum().sum()` |
| Percentage missing per column | `isnull().mean() * 100` | Series with percentages | `df.isnull().mean() * 100` |
| Columns with any missing values | `isnull().any()` | Boolean Series | `df.isnull().any()` |
| Rows with any missing values | `isnull().any(axis=1)` | Boolean Series | `df.isnull().any(axis=1)` |
| Count rows with missing values | `isnull().any(axis=1).sum()` | Integer | `df.isnull().any(axis=1).sum()` |
| Visualize missing patterns | `missingno.matrix()` | Visualization | `msno.matrix(df)` |
| Missing data heatmap | `missingno.heatmap()` | Correlation heatmap | `msno.heatmap(df)` |

**Note on Hidden Missing Data:**
Missing data doesn't always appear as `NaN` or `None`. Look out for "missing data hiding in plain sight":
- **Placeholder values**: `-999`, `-1`, `0`, `999`, `9999`
- **String placeholders**: `'N/A'`, `'NA'`, `'null'`, `'NULL'`, `'missing'`, `'unknown'`, `'?'`, `' '` (empty strings or whitespace)
- **Special codes**: `99`, `-9`, or other domain-specific sentinel values
- **Impossible values**: Negative ages, future dates, values outside valid ranges

Always inspect `value_counts()` and `unique()` for each column to identify these hidden missing values, then replace them with proper `NaN` before analysis.

#### Handling Missing Data

**For Numerical Data:**

| **When to Use** | **Strategy** | **Method** | **Example** |
|-----------------|--------------|------------|-------------|
| Normally distributed data | **Mean imputation** | `fillna(df.mean())` | `df['age'].fillna(df['age'].mean())` |
| Skewed data, presence of outliers | **Median imputation** | `fillna(df.median())` | `df['income'].fillna(df['income'].median())` |
| Discrete numeric values | **Mode imputation** | `fillna(df.mode().iloc[0])` | `df['rating'].fillna(df['rating'].mode()[0])` |
| Time series data | **Forward fill** | `fillna(method='ffill')` | `df['price'].fillna(method='ffill')` |
| Time series data | **Backward fill** | `fillna(method='bfill')` | `df['price'].fillna(method='bfill')` |
| Time series, ordered data | **Interpolation** | `interpolate()` | `df['temperature'].interpolate()` |
| Complex patterns | **KNN Imputation** | `KNNImputer()` | `from sklearn.impute import KNNImputer` |
| Multiple imputation with random forests | **MICE (miceforest)** | `miceforest.ImputationKernel()` | `from miceforest import ImputationKernel` |
| Domain-specific defaults | **Constant value** | `fillna(0)` or `fillna(-999)` | `df['discount'].fillna(0)` |

**For Categorical Data:**

| **When to Use** | **Strategy** | **Method** | **Example** |
|-----------------|--------------|------------|-------------|
| Most common category | **Mode imputation** | `fillna(df.mode()[0])` | `df['city'].fillna(df['city'].mode()[0])` |
| Missingness is informative | **Missing category** | `fillna('Unknown')` | `df['category'].fillna('Missing')` |
| Preserve missingness info | **Indicator variable** | Create binary flag | `df['was_missing'] = df['col'].isnull()` |

**Deletion Strategies:**

| **When to Use** | **Strategy** | **Method** | **Example** |
|-----------------|--------------|------------|-------------|
| < 5% missing, MCAR | **Drop rows** | `dropna()` | `df.dropna()` |
| > 40-50% missing | **Drop columns** | `dropna(axis=1)` | `df.dropna(axis=1, thresh=0.5*len(df))` |
| **Specific columns critical** | **Drop specific** | `dropna(subset=['col'])` | `df.dropna(subset=['target'])` |


### 3.4. Dealing with Duplicates

| **Purpose** | **Operation** | **Method** | **Example** |
|-------------|---------------|------------|-------------|
| Identify duplicate rows | **Find duplicates** | `duplicated()` | `df.duplicated()` |
| Number of duplicate rows | **Count duplicates** | `duplicated().sum()` | `df.duplicated().sum()` |
| Remove duplicate rows | **Drop duplicates** | `drop_duplicates()` | `df.drop_duplicates()` |
| Retain first occurrence (default) | **Keep first** | `drop_duplicates(keep='first')` | `df.drop_duplicates(keep='first')` |
| Retain last occurrence | **Keep last** | `drop_duplicates(keep='last')` | `df.drop_duplicates(keep='last')` |
| Remove all duplicates | **Remove all** | `drop_duplicates(keep=False)` | `df.drop_duplicates(keep=False)` |
| **Check specific columns only** | **Subset columns** | `drop_duplicates(subset=['col'])` | `df.drop_duplicates(subset=['id'])` |

### 3.5. Handling Outliers

#### Detection Methods

| **Technique** | **Method** | **Threshold** | **Implementation** |
|---------------|------------|---------------|-------------------|
| Visual inspection | **Box plot** | Beyond whiskers (1.5×IQR) | `df.boxplot()` or `sns.boxplot(data=df)` |
| Statistical calculation | **IQR method** | Q1 - 1.5×IQR or Q3 + 1.5×IQR | `Q1, Q3 = df.quantile([0.25, 0.75])` |
| Standard deviations | **Z-score** | \|z-score\| > 3 (or 2.5) | `np.abs(stats.zscore(df)) > 3` |
| Visual pattern recognition | **Scatter plot** | Domain-specific | `plt.scatter(df['x'], df['y'])` |
| Density-based detection | **Local Outlier Factor (LOF)** | Anomaly score threshold | `from sklearn.neighbors import LocalOutlierFactor`<br>`lof = LocalOutlierFactor()`<br>`outliers = lof.fit_predict(X)` |
| Tree-based anomaly detection | **Isolation Forest** | Contamination parameter | `from sklearn.ensemble import IsolationForest`<br>`iso = IsolationForest(contamination=0.1)`<br>`outliers = iso.fit_predict(X)` |

#### Treatment Strategies

| **When to Use** | **Strategy** | **Method** | **Implementation** |
|-----------------|--------------|------------|-------------------|
| Retain all observations | **Winsorization** | Cap at percentiles | `from scipy.stats.mstats import winsorize`<br>`winsorize(data, limits=[0.05, 0.05])` |
| Known valid ranges | **Capping/Clipping** | Set min/max bounds | `df['col'].clip(lower=0, upper=100)` |
| Outliers are errors | **Trimming/Removal** | Delete outlier rows | `df = df[df['col'] < upper_bound]` |
| Skewed distributions | **Transformation** | Log, sqrt, Box-Cox | `np.log1p(df['col'])` |
| Reduce extreme value impact | **Binning** | Discretize into categories | `pd.cut(df['col'], bins=5)` |
| Legitimate extreme values | **Do Nothing** | Keep outliers | Keep as-is when appropriate |

#### When to Keep Outliers

- Outliers represent genuine extreme cases (e.g., CEO salaries, rare events)
- Using robust statistical methods (median, MAD) that aren't sensitive to outliers
- The outlier is the phenomenon of interest (fraud detection, anomaly detection)
- Domain expertise confirms the data is correct
- Analysis goal is to understand the full range of data


## 4. Data Integration Techniques

### 4.1. Joining Methods Comparison

| **Method** | **Use Case** | **Key Alignment** | **Syntax** |
|------------|--------------|-------------------|------------|
| **concat** | Simple stacking of DataFrames | No key (by position/index) | `pd.concat([df1, df2], axis=0)` |
| **merge** | Complex key-based joins | Column keys | `pd.merge(df1, df2, on='key', how='inner')` |
| **join** | Index-based alignment | Index values | `df1.join(df2, on='key')` |

### 4.2. Join Types

| **Join Type** | **Description** | **Result Size** | **Use Case** |
|---------------|-----------------|-----------------|--------------|
| **Inner** | Only matching keys from both | Smallest (intersection) | When you only want complete records |
| **Outer** | All keys from both | Largest (union) | When you need all data from both sources |
| **Left** | All from left, matching from right | All left rows preserved | When left DataFrame is primary |
| **Right** | All from right, matching from left | All right rows preserved | When right DataFrame is primary |
| **Cross** | Cartesian product | All possible combinations | When you need all combinations |


## 5. Data Transformation Operations

### 5.1. Aggregation

Summarizing data based on groups:

#### Common Aggregation Functions

| **Function** | **Description** | **Example** |
|--------------|-----------------|-------------|
| `mean()` | Average value | `df.groupby('category')['value'].mean()` |
| `median()` | Middle value | `df.groupby('category')['value'].median()` |
| `sum()` | Total sum | `df.groupby('category')['value'].sum()` |
| `count()` | Number of observations | `df.groupby('category').count()` |
| `min()` / `max()` | Minimum/Maximum | `df.groupby('category')['value'].max()` |
| `std()` | Standard deviation | `df.groupby('category')['value'].std()` |
| `var()` | Variance | `df.groupby('category')['value'].var()` |
| `size()` | Group size | `df.groupby('category').size()` |
| `nunique()` | Number of unique values | `df.groupby('category')['id'].nunique()` |

### 5.2. Reshaping

Reorganizing data structure:

#### Pivot Tables

Transform data from long to wide format. <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html" target="_blank">**`pivot()` documentation**</a> | <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html" target="_blank">**`pivot_table()` documentation**</a>

```python
# Basic pivot
df.pivot(index='date', columns='category', values='value')

# Pivot with aggregation
df.pivot_table(
    index='date',
    columns='category',
    values='value',
    aggfunc='mean'
)

# Multiple aggregation functions
df.pivot_table(
    index='date',
    columns='category',
    values='value',
    aggfunc=['mean', 'sum', 'count']
)

# Multiple value columns
df.pivot_table(
    index='date',
    columns='category',
    values=['sales', 'profit'],
    aggfunc='sum'
)
```

#### Melt

Transform data from wide to long format. <a href="https://pandas.pydata.org/docs/reference/api/pandas.melt.html" target="_blank">**`melt()` documentation**</a>

```python
# Basic melt
pd.melt(df, id_vars=['id'], value_vars=['col1', 'col2'])

# Custom column names
pd.melt(
    df,
    id_vars=['id'],
    value_vars=['col1', 'col2'],
    var_name='variable',
    value_name='value'
)
```

#### Stack/Unstack

Reshape with multi-level indices. <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html" target="_blank">**`stack()` documentation**</a> | <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html" target="_blank">**`unstack()` documentation**</a>

```python
# Stack (columns to rows)
df.stack()

# Unstack (rows to columns)
df.unstack()

# Specify level
df.unstack(level=0)
```

#### Crosstab

Create cross-tabulation (frequency table) of two or more categorical variables. <a href="https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html" target="_blank">**`crosstab()` documentation**</a>

```python
# Basic crosstab
pd.crosstab(df['row_var'], df['col_var'])

# With margins (totals)
pd.crosstab(df['row_var'], df['col_var'], margins=True)

# With values and aggregation function
pd.crosstab(
    df['row_var'],
    df['col_var'],
    values=df['numeric_col'],
    aggfunc='mean'
)

# Normalize (show percentages)
pd.crosstab(df['row_var'], df['col_var'], normalize='all')  # All cells
pd.crosstab(df['row_var'], df['col_var'], normalize='index')  # By rows
pd.crosstab(df['row_var'], df['col_var'], normalize='columns')  # By columns

# Multiple variables
pd.crosstab([df['var1'], df['var2']], df['var3'])
```


## Additional Resources

### Python Libraries for Data Wrangling

- **pandas**: Primary tool for data manipulation and analysis
- **numpy**: Numerical operations and array handling
- **scipy**: Advanced statistical functions (e.g., winsorize)
- **sklearn.impute**: Advanced imputation methods (KNN, Iterative)
- **miceforest**: Fast multiple imputation using random forests (MICE algorithm)
- **missingno**: Visualizing missing data patterns
- **re**: Regular expressions for string pattern matching

### Recommended Reading

- <a href="https://pandas.pydata.org/docs/" target="_blank">**Pandas Documentation**</a>: Comprehensive guide to pandas operations
- <a href="https://www.oreilly.com/library/view/python-for-data/9781491957653/" target="_blank">**"Python for Data Analysis"**</a> by Wes McKinney (pandas creator)
- <a href="https://scikit-learn.org/stable/modules/impute.html" target="_blank">**Scikit-learn Imputation**</a>: Guide to imputation strategies in scikit-learn
- <a href="https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html" target="_blank">**Scikit-learn Outlier Detection**</a>: Evaluation and comparison of outlier detection methods
- <a href="https://github.com/ResidentMario/missingno" target="_blank">**missingno**</a>: Missing data visualization toolkit
- <a href="https://github.com/AnotherSamWilson/miceforest" target="_blank">**miceforest**</a>: Fast, memory efficient multiple imputation using random forests
