# Unsupervised learning

Unsupervised learning discovers hidden patterns and structures in unlabeled data without predefined target variables. This guide covers clustering, dimensionality reduction, association rules, and anomaly detection techniques essential for exploratory analysis and feature engineering.

## 1. Best practices

### 1.1. General guidelines

#### **Understand Your Goal**
   - Clustering: group similar data points
   - Dimensionality reduction: reduce features, visualize
   - Association rules: find item relationships
   - Anomaly detection: identify outliers

#### **Always Preprocess Data**
   - Standardize features for distance-based methods
   - Handle missing values appropriately
   - Remove or handle outliers (unless detecting them)
   - Scale features to similar ranges

#### **Determine Optimal Parameters**
   - Use elbow method for k-means
   - Check silhouette scores for cluster quality
   - Examine scree plots for PCA components
   - Validate with multiple metrics

#### **Visualize Results**
   - Plot clusters in 2D/3D space
   - Use dendrograms for hierarchical clustering
   - Show explained variance for PCA
   - Create t-SNE plots for high-dimensional data

#### **Validate Findings**
   - Check if clusters make domain sense
   - Verify dimensionality reduction preserves information
   - Confirm association rules are actionable
   - Test anomaly detection on known outliers

#### **Consider Scalability**
   - K-means: excellent for large datasets
   - DBSCAN: struggles with very large data
   - PCA: scales well
   - t-SNE: limited to moderate-sized datasets

#### **Interpret Results Carefully**
   - Clustering assignments are not absolute truth
   - PCA components lose interpretability
   - Association rules need minimum support/confidence
   - Anomalies require domain validation

#### **Combine Techniques**
   - Use PCA before clustering for high dimensions
   - Apply t-SNE for visualizing cluster results
   - Use clustering to identify segments, then association rules within segments

### 1.2. Common pitfalls

| **Pitfall** | **Problem** | **Solution** |
|-------------|-------------|--------------|
| **Not scaling features** | Distance-based methods fail | Always standardize for k-means, hierarchical, DBSCAN |
| **Wrong k in k-means** | Poor cluster quality | Use elbow method and silhouette scores |
| **Using k-means for non-spherical clusters** | Incorrect groupings | Try DBSCAN or hierarchical clustering |
| **Ignoring explained variance in PCA** | Information loss | Check cumulative variance, aim for 95%+ |
| **Using t-SNE distances as meaningful** | Misinterpretation | Only cluster shape matters, not inter-cluster distance |
| **Fitting PCA on entire dataset** | Data leakage | Fit on training data only, transform test data |
| **Setting arbitrary DBSCAN parameters** | Poor results | Use k-distance plots to determine eps |
| **Treating cluster assignments as labels** | Over-confidence | Remember clusters are exploratory |
| **Too many PCA components** | Defeats purpose | Select components explaining 90-95% variance |
| **Using accuracy to evaluate clustering** | Wrong metric | Use silhouette score, within-cluster SS |


## 2. Technique selection guide

| **Technique** | **Purpose** | **Data Type** | **Computational Cost** | **Key Advantage** |
|---------------|-------------|---------------|----------------------|-------------------|
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html" target="_blank">**K-Means**</a> | Clustering | Numerical | Low | Fast, scalable, simple |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html" target="_blank">**Hierarchical**</a> | Clustering | Numerical | Medium | No need to specify k, dendrogram visualization |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html" target="_blank">**DBSCAN**</a> | Clustering | Numerical | Medium | Arbitrary shapes, handles noise |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html" target="_blank">**PCA**</a> | Dimensionality reduction | Numerical | Low | Unsupervised, preserves global variance |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html" target="_blank">**LDA**</a> | Dimensionality reduction | Numerical (labeled) | Low | Supervised, maximizes class separation |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html" target="_blank">**t-SNE**</a> | Visualization | Numerical | High | Excellent for visualization, preserves local structure |
| **Apriori/Eclat** | Association rules | Transactional | Medium | Finds item relationships |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html" target="_blank">**Isolation Forest**</a> | Anomaly detection | Numerical | Low | Fast, unsupervised outlier detection |

## 3. Clustering algorithms

Clustering groups similar data points together without predefined labels.

### 3.1. Algorithm comparison

<table>
  <thead>
    <tr>
      <th><strong>Algorithm</strong></th>
      <th><strong>Cluster Shape</strong></th>
      <th><strong>Number of Clusters</strong></th>
      <th><strong>Handles Noise</strong></th>
      <th><strong>Key Parameters</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html" target="_blank"><strong>K-Means</strong></a></td>
      <td>Spherical</td>
      <td>Must specify k</td>
      <td>No</td>
      <td><code>n_clusters</code>, <code>init</code>, <code>random_state</code></td>
    </tr>
    <tr>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html" target="_blank"><strong>Hierarchical (Agglomerative)</strong></a></td>
      <td>Any</td>
      <td>Cut dendrogram at desired level</td>
      <td>Limited</td>
      <td><code>n_clusters</code>, <code>linkage</code> (ward, complete, average, single)</td>
    </tr>
    <tr>
      <td><strong>Hierarchical (Divisive)</strong></td>
      <td>Any</td>
      <td>Split from top down</td>
      <td>Limited</td>
      <td>Split criterion, stopping condition</td>
    </tr>
    <tr>
      <td><a href="https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html" target="_blank"><strong>DBSCAN</strong></a></td>
      <td>Arbitrary shapes</td>
      <td>Automatic</td>
      <td>Yes (marks as noise)</td>
      <td><code>eps</code> (neighborhood radius), <code>min_samples</code></td>
    </tr>
  </tbody>
</table>

#### **Algorithm details:**

##### **K-Means:**
- Iteratively assigns points to nearest centroid
- Updates centroids as cluster means
- Fast and scalable
- Use elbow method or silhouette score to find optimal k
- Best for: well-separated, spherical clusters

##### **Hierarchical Agglomerative:**
- Starts with each point as cluster
- Progressively merges closest clusters
- Creates dendrogram showing hierarchy
- Linkage methods: ward (minimize variance), complete (max distance), average, single (min distance)
- Best for: understanding data hierarchy, unknown cluster count

##### **Hierarchical Divisive:**
- Starts with all points in one cluster
- Recursively splits largest/most diverse cluster
- More computationally expensive
- Less common than agglomerative
- Best for: top-down decomposition needs

##### **DBSCAN:**
- Groups points based on density
- Core points: ≥ min_samples within eps radius
- Border points: within eps of core point
- Noise points: neither core nor border
- Best for: arbitrary shapes, noisy data, outlier detection

### 3.2. When to use each

| **Scenario** | **Recommended Algorithm** | **Why** |
|-------------|---------------------------|---------|
| **Spherical clusters** | K-Means | Fast, efficient, optimal for spherical shapes |
| **Unknown cluster count** | Hierarchical, DBSCAN | Don't require pre-specified k |
| **Non-spherical clusters** | DBSCAN | Handles arbitrary shapes |
| **Need hierarchy** | Hierarchical | Provides dendrogram for analysis |
| **Large dataset** | K-Means | Most scalable |
| **Noisy data with outliers** | DBSCAN | Explicitly identifies noise |
| **Well-separated clusters** | K-Means | Simple and effective |
| **Varying densities** | Hierarchical with appropriate linkage | More flexible than k-means |
| **Need reproducibility** | K-Means (with random_state) | Deterministic results |


## 4. Dimensionality reduction

Reduces feature count while preserving essential information.

### 4.1. Method comparison

| **Method** | **Type** | **Supervised** | **Linear** | **Components** | **Best For** |
|------------|----------|----------------|------------|----------------|--------------|
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html" target="_blank">**PCA**</a> | Feature extraction | No | Yes | Up to n features | General dimensionality reduction, preprocessing |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html" target="_blank">**LDA**</a> | Feature extraction | Yes | Yes | Up to k-1 classes | Classification preprocessing, class separation |
| <a href="https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html" target="_blank">**t-SNE**</a> | Feature extraction | No | No | Typically 2-3 | Visualization of high-dimensional data |

#### **Method details:**

##### **PCA (Principal Component Analysis):**
- Finds directions of maximum variance
- Creates orthogonal (uncorrelated) components
- First components capture most information
- Use scree plot or cumulative explained variance
- **Workflow**: standardize → compute covariance → find eigenvectors → transform data
- **Best practices**: standardize data, keep 90-95% variance, check component loadings

##### **LDA (Linear Discriminant Analysis):**
- Maximizes between-class variance, minimizes within-class variance
- Requires class labels
- Limited to k-1 components for k classes
- More effective than PCA when classes are well-defined
- **Workflow**: calculate class means → compute scatter matrices → solve eigenvalue problem → project data
- **Best practices**: verify Gaussian assumption, check equal covariances, use with sufficient samples

##### **t-SNE (t-Distributed Stochastic Neighbor Embedding):**
- Non-linear method preserving local structure
- Converts distances to probabilities
- Uses t-distribution in low-dimensional space
- Stochastic (different runs give different results)
- **Key parameters**: perplexity (5-50, balances local/global), learning_rate, n_iter
- **Best practices**: use subset for large data, run multiple times, don't interpret inter-cluster distances

### 4.2. Selection guidelines

#### **Use PCA when:**
- Unlabeled data
- General preprocessing needed
- Want interpretable linear combinations
- Need fast computation
- Working with any dataset size

#### **Use LDA when:**
- Have labeled data for classification
- Want to maximize class separation
- Preprocessing before classifier
- Classes are distinct
- Number of classes < number of features

#### **Use t-SNE when:**
- Need 2D/3D visualization
- Exploring cluster structure
- Presenting insights to stakeholders
- Local structure more important than global
- Dataset is moderate-sized (< 10,000 samples)


## 5. Association rules

Discovers relationships between items in transactional data (market basket analysis).

**Key metrics:**

| **Metric** | **Formula** | **Interpretation** |
|-----------|-------------|-------------------|
| **Support** | Frequency(X) / Total transactions | How often itemset appears |
| **Confidence** | Frequency(X,Y) / Frequency(X) | How often rule is true |
| **Lift** | Support(X,Y) / (Support(X) × Support(Y)) | Association strength vs. independence |

**Algorithms:**

<table>
  <thead>
    <tr>
      <th><strong>Algorithm</strong></th>
      <th><strong>Approach</strong></th>
      <th><strong>Best For</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Apriori</strong></td>
      <td>Breadth-first search, uses Apriori property (subsets of frequent itemsets are frequent)</td>
      <td>Sparse datasets, finding all frequent itemsets</td>
    </tr>
    <tr>
      <td><strong>Eclat</strong></td>
      <td>Depth-first search, vertical data format (TID lists)</td>
      <td>Dense datasets, faster than Apriori</td>
    </tr>
  </tbody>
</table>

#### **Best practices:**
- Set minimum support (e.g., 1%) to filter rare itemsets
- Set minimum confidence (e.g., 20%) for reliable rules
- Lift > 1 indicates positive association
- Validate rules with domain knowledge
- Consider computational cost for large datasets

#### **Common applications:**
- Retail: product recommendations, store layout
- Web: page navigation patterns, content suggestions
- Healthcare: symptom-treatment associations
- Finance: fraud pattern detection


## 6. Anomaly detection

Identifies rare observations that differ significantly from normal patterns.

#### **Isolation Forest:**
- Isolates anomalies using random partitioning
- Anomalies require fewer splits to isolate
- Fast and scalable
- No distance calculations needed

#### **How it works:**
1. Build isolation trees with random feature splits
2. Measure path length to isolate each point
3. Shorter paths indicate anomalies
4. Average across multiple trees

#### **Key parameters:**
- `contamination`: expected proportion of outliers (default: 0.1)
- `n_estimators`: number of trees (default: 100)
- `max_samples`: samples per tree

#### **Best practices:**
- Set contamination based on domain knowledge
- Use sufficient estimators (100-300)
- Validate detected anomalies with domain experts
- Standardize features first
- Works well with high-dimensional data

#### **Applications:**
- Fraud detection in transactions
- Network intrusion detection
- Manufacturing defect identification
- Health monitoring (abnormal vitals)


## 7. Evaluation metrics

### 7.1. Clustering metrics

| **Metric** | **Range** | **Best Value** | **Purpose** |
|-----------|-----------|----------------|-------------|
| **Silhouette Score** | [-1, 1] | +1 | Measures cluster cohesion and separation |
| **Within-Cluster Sum of Squares (WCSS)** | [0, ∞) | Lower | Used in elbow method to find optimal k |
| **Davies-Bouldin Index** | [0, ∞) | Lower | Ratio of within-cluster to between-cluster distances |
| **Calinski-Harabasz Index** | [0, ∞) | Higher | Ratio of between-cluster to within-cluster dispersion |

#### **Silhouette Score:**
- $s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$
- $a(i)$: average distance to points in same cluster
- $b(i)$: average distance to points in nearest cluster
- Score near +1: well-clustered
- Score near 0: on cluster boundary
- Score near -1: possibly wrong cluster

#### **Elbow Method (WCSS):**
- Plot WCSS vs. number of clusters
- Look for "elbow" where improvement diminishes
- Choose k at elbow point

### 7.2. Dimensionality reduction metrics

| **Metric** | **Application** | **Interpretation** |
|-----------|-----------------|-------------------|
| **Explained Variance Ratio** | PCA | Proportion of variance captured per component |
| **Cumulative Explained Variance** | PCA | Total variance captured by selected components |
| **Reconstruction Error** | PCA | How well reduced data reconstructs original |
| **Downstream Task Performance** | All | Performance on classification/regression after reduction |

#### **Best practices:**
- Retain components explaining 90-95% variance
- Use scree plots to visualize explained variance
- Validate with downstream task performance
- Check if reduction improves or hurts model accuracy


## 8. Unsupervised learning workflow

```
1. Define Objective
   - Clustering: segment data
   - Dimensionality reduction: simplify/visualize
   - Association rules: find patterns
   - Anomaly detection: identify outliers
   ↓
2. Data Preprocessing
   - Handle missing values
   - Standardize features (for distance-based methods)
   - Remove or flag known outliers (if not detecting)
   ↓
3. Exploratory Analysis
   - Visualize data distribution
   - Check correlations
   - Identify potential number of clusters
   ↓
4. Apply Technique
   Clustering:
     - Try multiple algorithms
     - Use elbow method for k
     - Calculate silhouette scores
   
   Dimensionality Reduction:
     - Check explained variance
     - Validate with downstream tasks
     - Visualize results
   
   Association Rules:
     - Set support/confidence thresholds
     - Generate rules
     - Filter by lift
   
   Anomaly Detection:
     - Set contamination parameter
     - Identify anomalies
     - Validate with domain knowledge
   ↓
5. Evaluate Results
   - Use appropriate metrics
   - Visualize clusters/components
   - Check domain validity
   ↓
6. Iterate and Refine
   - Adjust parameters
   - Try different algorithms
   - Combine techniques
   ↓
7. Interpret and Apply
   - Validate findings with stakeholders
   - Document insights
   - Use results for downstream tasks
```


## Additional resources

### Python libraries

- **[scikit-learn](https://scikit-learn.org)**: Core unsupervised learning modules
  - [`cluster`](https://scikit-learn.org/stable/modules/clustering.html): KMeans, AgglomerativeClustering, DBSCAN
  - [`decomposition`](https://scikit-learn.org/stable/modules/decomposition.html): PCA
  - [`discriminant_analysis`](https://scikit-learn.org/stable/modules/lda_qda.html): LinearDiscriminantAnalysis
  - [`manifold`](https://scikit-learn.org/stable/modules/manifold.html): TSNE
  - [`ensemble`](https://scikit-learn.org/stable/modules/ensemble.html): IsolationForest
- **[mlxtend](http://rasbt.github.io/mlxtend/)**: Association rule mining
  - `frequent_patterns.apriori`: Apriori algorithm
  - `frequent_patterns.association_rules`: Generate rules
- **[pyECLAT](https://github.com/jeffheaton/pyECLAT)**: Eclat algorithm implementation
- **[scipy.cluster.hierarchy](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html)**: Hierarchical clustering with dendrograms

### Recommended reading

- <a href="https://scikit-learn.org/stable/modules/clustering.html" target="_blank">**Scikit-learn Clustering Guide**</a>: Comprehensive clustering documentation
- <a href="https://scikit-learn.org/stable/modules/decomposition.html" target="_blank">**Scikit-learn Decomposition Guide**</a>: PCA and other decomposition methods
- <a href="https://distill.pub/2016/misread-tsne/" target="_blank">**"How to Use t-SNE Effectively"**</a>: Interactive guide to t-SNE
- <a href="https://www.statlearning.com/" target="_blank">**"Introduction to Statistical Learning"**</a>: Chapter 12 on Unsupervised Learning
