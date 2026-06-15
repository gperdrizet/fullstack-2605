# Statistics overview

This guide summarizes the core ideas from the statistics overview resource: descriptive statistics, common probability distributions, and how to choose a statistical test.

The statistical testing section below is adapted from the source repo's Jekyll templates and keeps the same high-level guidance: use the quick guide first, then refer to the complete table for edge cases and more specific scenarios.

## Table of contents

1. [Common descriptive statistics](#1-common-descriptive-statistics)
	- [Measures of central tendency, spread, and shape](#11-measures-of-central-tendency-spread-and-shape)
	- [Interpretation guidelines](#12-interpretation-guidelines)
	- [Choosing the right statistic](#13-choosing-the-right-statistic)
2. [Common probability distributions](#2-common-probability-distributions)
	- [Discrete distributions](#21-discrete-distributions)
	- [Continuous distributions](#22-continuous-distributions)
3. [Statistical test selection guide](#3-statistical-test-selection-guide)
	- [Most common/useful tests](#31-most-commonuseful-tests)
	  - [Student's t-test](#311-students-t-test)
	  - [ANOVA (also known as the F-test)](#312-anova-also-known-as-the-f-test)
	  - [Mann-Whitney U test](#313-mann-whitney-u-test)
	  - [Kruskal-Wallis test (also known as ANOVA on ranks)](#314-kruskal-wallis-test-also-known-as-anova-on-ranks)
	- [Assumption checklist](#35-assumption-checklist)
	- [Complete test table](#36-complete-test-table)
	- [Multiple testing correction](#37-multiple-testing-correction)

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

The tests listed below cannot be used with nominal data as the dependent variable. Choosing the correct statistical test and plotting data effectively depends on the data's statistical type. See the Wikipedia article [Statistical data type](https://en.wikipedia.org/wiki/Statistical_data_type) for more information.

The tests below come in two flavors that differ in assumptions. Parametric tests (t-test, F-test) make assumptions about the population's distribution and parameters, non-parametric tests (Mann-Whitney, Kruskal–Wallis) do not. Parametric vs non-parametric is a useful distinction when thinking about statistical tests and models. See [Parametric and Nonparametric: Demystifying the Terms](https://github.com/4GeeksAcademy/gperdrizet-ds9-materials/blob/main/resources/articles/Hoskin_parametric_and%20_nonparametric.pdf).

### 3.1. Most common/useful tests

#### 3.1.1. Student's t-test

- Use this test for comparing two groups.
- Wikipedia article: [Student's t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)
- SciPy.stats implementation: [ttest_ind()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)

**Notes:** Tests wether the difference between two groups is significant or not. Assumes that the data from which the samples were drawn is normally distributed and the samples have the same variance. If this is not true, see the Mann-Whitney U test, below.

#### 3.1.2. ANOVA (also known as the F-test)

- Use this test for comparing multiple groups.
- Wikipedia article: [F-test](https://en.wikipedia.org/wiki/F-test)
- SciPy.stats implementation: [f_oneway()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html)

**Notes:** Tests whether or not one or more of the group means are different from the others. Assumes the data was drawn from a normally distributed population. If this is not true, see the Kruskal–Wallis test, below. Determining which sample(s) is/are different requires further analysis (see [Tukey's range test](https://en.wikipedia.org/wiki/Tukey%27s_range_test)).

#### 3.1.3. Mann-Whitney U test

- Use this test for comparing two groups that are not normally distributed.
- Wikipedia article: [Mann–Whitney U test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test)
- SciPy.stats implementation: [mannwhitneyu()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html)

**Notes:** Uses the rank order of observations to test for difference between two groups. Data must be at least ordinal (larger or smaller has a clear meaning) and assumes that the shapes of the sample distributions are similar. If you decide not to use this test because the sample distributions look very different, you have your answer already. For completeness, maybe see the [Kolmogorov–Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test) anyway.

#### 3.1.4. Kruskal-Wallis test (also known as ANOVA on ranks)

- Use this test for comparing two or more groups that are not normally distributed.
- Wikipedia article: [Kruskal–Wallis test](https://en.wikipedia.org/wiki/Kruskal%E2%80%93Wallis_test)
- SciPy.stats implementation: [kruskal()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html)

**Notes:** Uses rank order of observations to test whether or not one or more groups is different from the others. Follows the similar assumptions to the Mann-Whitney U test, above.

### 3.5. Assumption checklist

- Verify normality when using parametric tests.
- Check whether observations are independent.
- Confirm that groups have similar variance when required.
- Use non-parametric tests when sample size is small, data are ordinal, or assumptions are not met.

### 3.6. Complete test table

| Independent variable type | Dependent variable type | Situation | Parametric test | Non-parametric test | P-value interpretation |
|---------------------------|-------------------------|-----------|------------------|---------------------|------------------------|
| None | Continuous | Comparing one sample to a known value | One-sample t-test / Z-test | Wilcoxon signed-rank test | Low p-value: Sample mean significantly differs from known value |
| None | Continuous | Testing normality of data | Shapiro-Wilk test | Kolmogorov-Smirnov test | Low p-value: Data significantly deviates from normal distribution |
| None | Continuous | Comparing sample distribution to theoretical distribution | N/A | Kolmogorov-Smirnov test | Low p-value: Sample distribution differs from theoretical distribution |
| Categorical | Categorical | Comparing distributions of categorical variables | Chi-square test | Fisher's exact test (for small samples) | Low p-value: Observed distribution differs from expected |
| Categorical | Continuous | Comparing two independent groups | Independent samples t-test / Two-sample Z-test | Mann-Whitney U test (Wilcoxon rank-sum test) | Low p-value: Significant difference between the two groups |
| Categorical | Continuous | Comparing two paired/dependent groups | Paired t-test | Wilcoxon signed-rank test | Low p-value: Significant change between paired observations |
| Categorical | Continuous | Comparing three or more independent groups | One-way ANOVA | Kruskal-Wallis H test | Low p-value: At least one group differs from the others |
| Categorical | Continuous | Comparing three or more paired/dependent groups | Repeated measures ANOVA | Friedman test | Low p-value: Significant differences across repeated measurements |
| Categorical | Continuous | Testing effects of two or more factors | Two-way ANOVA / Factorial ANOVA | Scheirer-Ray-Hare test | Low p-value: Significant main effects or interaction effects |
| Categorical | Continuous | Comparing variances between two groups | F-test (Levene's test) | Levene's test / Fligner-Killeen test | Low p-value: Variances significantly differ between groups |
| Categorical | Categorical | Testing independence of two categorical variables | Chi-square test of independence | Fisher's exact test | Low p-value: Variables are dependent (not independent) |
| Continuous | Continuous | Testing relationship between two continuous variables | Pearson correlation | Spearman rank correlation / Kendall's tau | Low p-value: Significant correlation exists between variables |

### 3.7. Multiple testing correction

When you run many tests, the chance of false positives increases.

- Bonferroni is the simplest and most conservative correction.
- Holm-Bonferroni is less conservative than Bonferroni.
- Benjamini-Hochberg controls the false discovery rate.
- Post-hoc tests are appropriate after ANOVA when comparing specific group pairs.

## Source

- [Statistics overview](https://gperdrizet.github.io/FSA_devops/resource_pages/statistics.html)