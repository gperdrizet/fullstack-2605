# Statistics overview

This guide summarizes the core ideas from the statistics overview resource: descriptive statistics, common probability distributions, and how to choose a statistical test.

## 1. Common descriptive statistics

Descriptive statistics summarize the center, spread, and shape of a dataset.

### 1.1. Measures of central tendency, spread, and shape

| Category | Statistic | When to use |
|----------|-----------|-------------|
| Central tendency | Mean | Symmetric data without strong outliers |
| Central tendency | Median | Skewed data or data with outliers |
| Central tendency | Mode | Categorical data or multimodal distributions |
| Spread | Range | Quick estimate of spread |
| Spread | Variance and standard deviation | General variability measures |
| Spread | Interquartile range (IQR) | Robust spread measure for skewed data |
| Spread | Coefficient of variation | Compare variability across different scales |
| Shape | Skewness | Assess asymmetry |
| Shape | Kurtosis | Assess tail heaviness and outlier tendency |

### 1.2. Interpretation guidelines

- Mean, median, and mode are often close for symmetric distributions.
- A right-skewed distribution usually has mean greater than median.
- A left-skewed distribution usually has mean less than median.
- High variance or standard deviation means values are more spread out.
- IQR is useful when outliers would distort the mean and standard deviation.

### 1.3. Choosing the right statistic

1. Use mean and standard deviation for symmetric data without strong outliers.
2. Use median and IQR for skewed data or data with outliers.
3. Use coefficient of variation when comparing spread across different units or scales.
4. Use skewness and kurtosis when you need a more detailed view of distribution shape.

## 2. Common probability distributions

Probability distributions describe how likely different outcomes are in a random process.

### 2.1. Discrete distributions

| Distribution | Typical use |
|--------------|-------------|
| Bernoulli | A single yes/no outcome |
| Binomial | Number of successes in repeated independent trials |
| Poisson | Count of events in a fixed interval |
| Geometric | Number of trials until the first success |

### 2.2. Continuous distributions

| Distribution | Typical use |
|--------------|-------------|
| Uniform | Values are equally likely in an interval |
| Normal | Symmetric bell-shaped data |
| Exponential | Time between events in a Poisson process |
| Gamma | Generalized waiting-time model |
| Beta | Values constrained to the interval [0, 1] |
| Chi-square | Sum of squared standard normal variables |
| Student's t | Small-sample inference with heavier tails |
| F | Comparing variance ratios |
| Pareto | Heavy-tailed and power-law behavior |

## 3. Statistical test selection guide

Before selecting a test, check the data type, distribution shape, and whether the samples are independent.

### 3.1. Assumption checklist

- Verify normality when using parametric tests.
- Check whether observations are independent.
- Confirm that groups have similar variance when required.
- Use non-parametric tests when sample size is small, data are ordinal, or assumptions are not met.

### 3.2. Common test choices

| Scenario | Parametric test | Non-parametric alternative |
|----------|-----------------|----------------------------|
| One sample vs. known value | One-sample t-test | Wilcoxon signed-rank test |
| Two independent groups | Two-sample t-test | Mann-Whitney U test |
| Two paired groups | Paired t-test | Wilcoxon signed-rank test |
| Three or more independent groups | One-way ANOVA | Kruskal-Wallis test |
| Three or more paired groups | Repeated measures ANOVA | Friedman test |
| Relationship between two continuous variables | Pearson correlation | Spearman correlation |
| Independence of categorical variables | Chi-square test of independence | Fisher's exact test |

### 3.3. Multiple testing correction

When you run many tests, the chance of false positives increases.

- Bonferroni is the simplest and most conservative correction.
- Holm-Bonferroni is less conservative than Bonferroni.
- Benjamini-Hochberg controls the false discovery rate.
- Post-hoc tests are appropriate after ANOVA when comparing specific group pairs.

## Source

- [Statistics overview](https://gperdrizet.github.io/FSA_devops/resource_pages/statistics.html)