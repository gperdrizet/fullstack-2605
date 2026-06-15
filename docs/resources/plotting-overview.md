# Plotting overview

Data visualization is essential for exploring, understanding, and communicating insights from data. This guide covers common plot types, their purposes, and when to use them.

## Table of contents
1. [Plot selection guide](#1-plot-selection-guide)
   - [By analysis goal](#11-by-analysis-goal)
   - [By data type combination](#12-by-data-type-combination)
2. [Best practices](#2-best-practices)
   - [General guidelines](#21-general-guidelines)
   - [Common mistakes to avoid](#22-common-mistakes-to-avoid)
3. [Common plot types by data type and purpose](#3-common-plot-types-by-data-type-and-purpose)
   - [Univariate plots (single variable)](#31-univariate-plots-single-variable)
   - [Bivariate plots (two variables)](#32-bivariate-plots-two-variables)
   - [Multivariate plots (three or more variables)](#33-multivariate-plots-three-or-more-variables)
   - [Specialized statistical plots](#34-specialized-statistical-plots)
   - [Time series plots](#35-time-series-plots)
4. [Additional resources](#4-additional-resources)
   - [Python visualization libraries](#41-python-visualization-libraries)
   - [Recommended reading](#42-recommended-reading)
   - [Python plotting resources](#43-python-plotting-resources)
   - [Color palettes](#44-color-palettes)

---

## 1. Plot selection guide

### 1.1. By analysis goal

| **Goal** | **Recommended plot types** |
|----------|---------------------------|
| **Understand distribution of single variable** | Histogram, Box plot, Violin plot, Density plot |
| **Compare groups** | Box plot, Violin plot, Bar chart, Strip plot |
| **Find relationships between variables** | Scatter plot, Line plot, Regression plot, Heatmap |
| **Show composition** | Pie chart, Stacked bar chart, Area plot |
| **Analyze time series** | Line plot, Area plot, Seasonal plot |
| **Detect outliers** | Box plot, Scatter plot, Strip plot |
| **Explore multivariate data** | Pair plot, Correlation heatmap, Facet grid |
| **Check statistical assumptions** | Q-Q plot, Residual plot, Histogram |
| **Show uncertainty** | Error bars, Confidence bands, Violin plots |

### 1.2. By data type combination

<table>
  <thead>
    <tr>
      <th><strong>X Variable</strong></th>
      <th><strong>Y Variable</strong></th>
      <th><strong>Z Variable (optional)</strong></th>
      <th><strong>Recommended Plots</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3"><strong>Categorical</strong></td>
      <td><strong>None</strong></td>
      <td>None</td>
      <td>Bar chart, Pie chart, Count plot</td>
    </tr>
    <tr>
      <td><strong>Continuous</strong></td>
      <td>None</td>
      <td>Box plot, Violin plot, Bar chart, Strip plot</td>
    </tr>
    <tr>
      <td><strong>Categorical</strong></td>
      <td>None</td>
      <td>Heatmap, Stacked bar chart, Grouped bar chart</td>
    </tr>
    <tr>
      <td rowspan="4"><strong>Continuous</strong></td>
      <td><strong>None</strong></td>
      <td>None</td>
      <td>Histogram, Box plot, Violin plot, Density plot</td>
    </tr>
    <tr>
      <td rowspan="3"><strong>Continuous</strong></td>
      <td>None</td>
      <td>Scatter plot, Line plot, Hexbin, 2D density</td>
    </tr>
    <tr>
      <td>Continuous</td>
      <td>3D scatter, Bubble chart, Contour plot</td>
    </tr>
    <tr>
      <td>Categorical</td>
      <td>Scatter with hue, Facet grid</td>
    </tr>
  </tbody>
</table>

---

## 2. Best practices

### 2.1. General guidelines

1. **Choose the right plot for your data type and message**
   - Match plot type to data structure (categorical vs continuous)
   - Consider what you want to communicate

2. **Keep it simple**
   - Avoid unnecessary 3D effects
   - Remove chart junk (excessive gridlines, decorations)
   - Use appropriate aspect ratios

3. **Use color effectively**
   - Use color to encode information, not just for decoration
   - Ensure accessibility (colorblind-friendly palettes)
   - Maintain consistency across related plots

4. **Label clearly**
   - Always include axis labels with units
   - Add informative titles
   - Include legends when needed
   - Annotate important points

5. **Consider your audience**
   - Technical vs general audience
   - Level of detail appropriate for context
   - Medium of presentation (paper, screen, presentation)

### 2.2. Common mistakes to avoid

| **Mistake** | **Problem** | **Solution** |
|-------------|-------------|--------------|
| **Starting y-axis at non-zero** | Exaggerates differences | Start at zero for bar charts; flexible for line plots |
| **Too many categories** | Cluttered, hard to read | Limit to 7-10 categories; consider grouping or filtering |
| **3D when 2D suffices** | Distorts perception, hard to read | Use 2D alternatives with color or size |
| **Pie charts with many slices** | Hard to compare angles | Use bar chart instead |
| **Dual y-axes** | Can be misleading | Use separate plots or normalize scales |
| **Missing error bars** | Unclear uncertainty | Add error bars or confidence intervals |
| **Poor color choices** | Not colorblind-safe, poor contrast | Use established palettes (ColorBrewer, Seaborn) |
| **Overplotting** | Too many overlapping points | Use transparency, jitter, hexbin, or sample data |

---

## 3. Common plot types by data type and purpose

### 3.1. Univariate plots (single variable)

| **Plot Type** | **Example** | **Data Type** | **Purpose** | **Key Features** | **Python Implementation** |
|---------------|-------------|---------------|-------------|------------------|---------------------------|
| **Histogram** | [![Histogram](../assets/plot_examples/histogram.png)](../assets/plot_examples/histogram.png) | Continuous | Show distribution and frequency of values | Bins group continuous data; bar heights show frequency | `plt.hist(data, bins=30)` or `sns.histplot(data)` |
| **Box Plot (Box-and-Whisker)** | [![Box Plot](../assets/plot_examples/boxplot.png)](../assets/plot_examples/boxplot.png) | Continuous | Display distribution summary (quartiles, median, outliers) | Shows Q1, median, Q3, whiskers (1.5×IQR), and outliers as points | `plt.boxplot(data)` or `sns.boxplot(data)` |
| **Violin Plot** | [![Violin Plot](../assets/plot_examples/violinplot.png)](../assets/plot_examples/violinplot.png) | Continuous | Combination of box plot and density plot | Wider sections indicate higher density; includes median marker | `sns.violinplot(x=data)` |
| **Density Plot (KDE)** | [![Density Plot](../assets/plot_examples/densityplot.png)](../assets/plot_examples/densityplot.png) | Continuous | Smooth estimate of probability density function | Smooth curve showing probability density | `sns.kdeplot(data)` or `data.plot(kind='kde')` |
| **Bar Chart** | [![Bar Chart](../assets/plot_examples/barchart.png)](../assets/plot_examples/barchart.png) | Categorical | Compare frequencies or values across categories | Each bar represents a category; height shows value/count | `plt.bar(categories, values)` or `sns.barplot(x, y)` |
| **Count Plot** | [![Count Plot](../assets/plot_examples/countplot.png)](../assets/plot_examples/countplot.png) | Categorical | Show frequency of categorical values | Specialized bar chart for counts | `sns.countplot(x=category)` |
| **Pie Chart** | [![Pie Chart](../assets/plot_examples/piechart.png)](../assets/plot_examples/piechart.png) | Categorical | Show proportions of a whole | Circular chart divided into slices; each slice represents proportion | `plt.pie(values, labels=labels)` |
| **Strip Plot** | [![Strip Plot](../assets/plot_examples/stripplot.png)](../assets/plot_examples/stripplot.png) | Continuous (grouped by category) | Show individual data points along one axis | Points plotted along axis; shows each individual value | `sns.stripplot(x=category, y=values)` |
| **Swarm Plot** | [![Swarm Plot](../assets/plot_examples/swarmplot.png)](../assets/plot_examples/swarmplot.png) | Continuous (grouped by category) | Like strip plot but points don't overlap | Non-overlapping points; good for seeing density | `sns.swarmplot(x=category, y=values)` |

### 3.2. Bivariate plots (two variables)

| **Plot Type** | **Example** | **X-axis Type** | **Y-axis Type** | **Purpose** | **Key Features** | **Python Implementation** |
|---------------|-------------|-----------------|-----------------|-------------|------------------|---------------------------|
| **Scatter Plot** | [![Scatter Plot](../assets/plot_examples/scatterplot.png)](../assets/plot_examples/scatterplot.png) | Continuous | Continuous | Show relationship between two continuous variables | Each point represents one observation | `plt.scatter(x, y)` or `sns.scatterplot(x, y)` |
| **Line Plot** | [![Line Plot](../assets/plot_examples/lineplot.png)](../assets/plot_examples/lineplot.png) | Continuous/Time | Continuous | Show trends over continuous variable (often time) | Points connected by lines | `plt.plot(x, y)` or `data.plot()` |
| **Bar Chart** | [![Bar Chart](../assets/plot_examples/barchart.png)](../assets/plot_examples/barchart.png) | Categorical | Continuous | Compare continuous values across categories | Bars represent values for each category | `plt.bar(categories, values)` or `sns.barplot(x, y)` |
| **Box Plot (Grouped)** | [![Grouped Box Plot](../assets/plot_examples/grouped_boxplot.png)](../assets/plot_examples/grouped_boxplot.png) | Categorical | Continuous | Compare distributions across categories | Multiple box plots side by side | `sns.boxplot(x=category, y=values)` |
| **Violin Plot (Grouped)** | [![Grouped Violin Plot](../assets/plot_examples/grouped_violinplot.png)](../assets/plot_examples/grouped_violinplot.png) | Categorical | Continuous | Compare distribution shapes across categories | Multiple violin plots side by side | `sns.violinplot(x=category, y=values)` |
| **Heatmap** | [![Heatmap](../assets/plot_examples/heatmap.png)](../assets/plot_examples/heatmap.png) | Categorical/Discrete | Categorical/Discrete | Show magnitude of values in two-dimensional space | Color intensity represents value magnitude | `sns.heatmap(data, annot=True)` |
| **Hexbin Plot** | [![Hexbin Plot](../assets/plot_examples/hexbinplot.png)](../assets/plot_examples/hexbinplot.png) | Continuous | Continuous | Show density of points in 2D space | Hexagonal bins; color shows point density | `plt.hexbin(x, y, gridsize=30)` |
| **2D Density Plot** | [![2D Density Plot](../assets/plot_examples/density2d.png)](../assets/plot_examples/density2d.png) | Continuous | Continuous | Show probability density in 2D space | Contour lines or color gradients show density | `sns.kdeplot(x=x, y=y)` |
| **Joint Plot** | [![Joint Plot](../assets/plot_examples/jointplot.png)](../assets/plot_examples/jointplot.png) | Continuous | Continuous | Combine scatter plot with marginal distributions | Central scatter with histograms/KDEs on margins | `sns.jointplot(x=x, y=y)` |

### 3.3. Multivariate plots (three or more variables)

| **Plot Type** | **Example** | **Purpose** | **Key Features** | **Python Implementation** |
|---------------|-------------|-------------|------------------|---------------------------|
| **Pair Plot (Scatter Matrix)** | [![Pair Plot](../assets/plot_examples/pairplot.png)](../assets/plot_examples/pairplot.png) | Show all pairwise relationships in dataset | Grid of scatter plots; diagonal shows distributions | `sns.pairplot(dataframe)` |
| **3D Scatter Plot** | [![3D Scatter Plot](../assets/plot_examples/scatter3d.png)](../assets/plot_examples/scatter3d.png) | Show relationship between three continuous variables | Points plotted in 3D space | `from mpl_toolkits.mplot3d import Axes3D` then `ax.scatter3D(x, y, z)` |
| **Bubble Chart** | [![Bubble Chart](../assets/plot_examples/bubblechart.png)](../assets/plot_examples/bubblechart.png) | Show three continuous variables (x, y, size) | Like scatter plot but point size represents third variable | `plt.scatter(x, y, s=sizes)` |
| **Facet Grid (Small Multiples)** | [![Facet Grid](../assets/plot_examples/facetgrid.png)](../assets/plot_examples/facetgrid.png) | Show subsets of data in separate subplots | Multiple plots arranged in grid | `sns.FacetGrid(data, col='category').map(plt.scatter, 'x', 'y')` |
| **Parallel Coordinates** | [![Parallel Coordinates](../assets/plot_examples/parallelcoordinates.png)](../assets/plot_examples/parallelcoordinates.png) | Compare multiple variables across observations | Lines connect values across parallel axes | `pd.plotting.parallel_coordinates(df, 'class_column')` |
| **Correlation Heatmap** | [![Correlation Heatmap](../assets/plot_examples/correlation_heatmap.png)](../assets/plot_examples/correlation_heatmap.png) | Show correlation between all variable pairs | Color-coded correlation matrix | `sns.heatmap(df.corr(), annot=True)` |

### 3.4. Specialized statistical plots

| **Plot Type** | **Example** | **Purpose** | **Key Features** | **Python Implementation** |
|---------------|-------------|-------------|------------------|---------------------------|
| **Q-Q Plot (Quantile-Quantile)** | [![Q-Q Plot](../assets/plot_examples/qqplot.png)](../assets/plot_examples/qqplot.png) | Test if data follows theoretical distribution | Points should follow diagonal line if normally distributed | `stats.probplot(data, dist="norm", plot=plt)` |
| **Residual Plot** | [![Residual Plot](../assets/plot_examples/residualplot.png)](../assets/plot_examples/residualplot.png) | Diagnose regression model fit | Plot residuals vs fitted values; should show random pattern | `sns.residplot(x=predictions, y=residuals)` |
| **ROC Curve** | [![ROC Curve](../assets/plot_examples/roc_curve.png)](../assets/plot_examples/roc_curve.png) | Evaluate binary classifier performance | Plots True Positive Rate vs False Positive Rate | `from sklearn.metrics import roc_curve` then `plt.plot(fpr, tpr)` |
| **Confusion Matrix** | [![Confusion Matrix](../assets/plot_examples/confusion_matrix.png)](../assets/plot_examples/confusion_matrix.png) | Show classification results | Matrix showing predicted vs actual classes | `sns.heatmap(confusion_matrix, annot=True, fmt='d')` |
| **Error Bars** | [![Error Bars](../assets/plot_examples/errorbars.png)](../assets/plot_examples/errorbars.png) | Show uncertainty or variability | Bars extend from points to show range | `plt.errorbar(x, y, yerr=errors)` |
| **Regression Plot** | [![Regression Plot](../assets/plot_examples/regressionplot.png)](../assets/plot_examples/regressionplot.png) | Show linear relationship and confidence interval | Scatter plot with fitted line and confidence band | `sns.regplot(x=x, y=y)` |

### 3.5. Time series plots

| **Plot Type** | **Example** | **Purpose** | **Key Features** | **Python Implementation** |
|---------------|-------------|-------------|------------------|---------------------------|
| **Line Plot** | [![Time Series Line Plot](../assets/plot_examples/timeseries_line.png)](../assets/plot_examples/timeseries_line.png) | Show values changing over time | X-axis is time; y-axis is value | `plt.plot(dates, values)` or `data.plot()` |
| **Area Plot** | [![Area Plot](../assets/plot_examples/areaplot.png)](../assets/plot_examples/areaplot.png) | Show cumulative totals over time | Filled area under line(s) | `data.plot.area()` or `plt.fill_between(x, y)` |
| **Stacked Area Plot** | [![Stacked Area Plot](../assets/plot_examples/stacked_area.png)](../assets/plot_examples/stacked_area.png) | Show multiple time series composition | Multiple series stacked on top of each other | `data.plot.area(stacked=True)` |
| **Seasonal Plot** | [![Seasonal Plot](../assets/plot_examples/seasonalplot.png)](../assets/plot_examples/seasonalplot.png) | Show patterns that repeat over time | Multiple lines for each season/cycle | Manually create with groupby and plot |
| **Autocorrelation Plot** | [![Autocorrelation Plot](../assets/plot_examples/autocorrelation.png)](../assets/plot_examples/autocorrelation.png) | Show correlation of series with lagged versions | Correlation at different lag values | `pd.plotting.autocorrelation_plot(data)` |
| **Lag Plot** | [![Lag Plot](../assets/plot_examples/lagplot.png)](../assets/plot_examples/lagplot.png) | Check for randomness in time series | Current value vs lagged value | `pd.plotting.lag_plot(data)` |


---

## 4. Additional resources

### 4.1. Python visualization libraries

| **Library** | **Strengths** | **Best For** | **Import Statement** |
|-------------|---------------|--------------|---------------------|
| **Matplotlib** | Highly customizable, fine control | Publication-quality plots, custom visualizations | `import matplotlib.pyplot as plt` |
| **Seaborn** | Beautiful defaults, statistical plots | Exploratory data analysis, statistical visualization | `import seaborn as sns` |
| **Pandas** | Integrated with DataFrames | Quick exploration, simple plots | Built-in: `df.plot()` |
| **Plotly** | Interactive plots, 3D support | Dashboards, web applications, interactive exploration | `import plotly.express as px` |
| **Bokeh** | Interactive web-ready plots | Interactive dashboards, streaming data | `from bokeh.plotting import figure` |

### 4.2. Recommended reading

- <a href="https://www.edwardtufte.com/tufte/books_vdqi" target="_blank">**"The Visual Display of Quantitative Information"**</a> by Edward Tufte
- <a href="https://clauswilke.com/dataviz/" target="_blank">**"Fundamentals of Data Visualization"**</a> by Claus O. Wilke
- <a href="https://www.storytellingwithdata.com/" target="_blank">**"Storytelling with Data"**</a> by Cole Nussbaumer Knaflic

### 4.3. Python plotting resources

- <a href="https://colorbrewer2.org/" target="_blank">**ColorBrewer**</a>: Color schemes for maps and data visualization
- <a href="https://seaborn.pydata.org/examples/index.html" target="_blank">**Seaborn Gallery**</a>: Examples of statistical plots
- <a href="https://matplotlib.org/stable/gallery/index.html" target="_blank">**Matplotlib Gallery**</a>: Comprehensive plot examples
- <a href="https://www.python-graph-gallery.com/" target="_blank">**Python Graph Gallery**</a>: Collection of plot types with code

### 4.4. Color palettes

```python
# Colorblind-friendly palettes
sns.color_palette("colorblind")
sns.color_palette("Set2")

# Diverging (for correlation matrices)
sns.color_palette("RdBu_r", as_cmap=True)
sns.color_palette("coolwarm", as_cmap=True)

# Sequential (for heatmaps)
sns.color_palette("YlOrRd", as_cmap=True)
sns.color_palette("viridis", as_cmap=True)
```