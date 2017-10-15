# Non parametric tests #
Non parametric statistical tests are used, 
when you can't expect data to be normally distributed.

## Kruskal-Wallis Rank sum test ##
Non paramteric equivalent for ANOVA.

## Sign test ##
Investigate hypothesis that sample's
quantile is the expected value.
Mostly the quantile is 0.5 which is also known as median.
<br/>
<br/>
Compare sample values to the expected quantile value.
If the sample value is bigger than the epected it gets plus sign,
otherwise minus.
If the comparison is tie, the value is dropped and
the sample size decreased by one.
<br/>
<br/>
Use `BSDA` library and `SIGN.test()` function.


## Wilcoxon test - One sample ##
Compare an expected mean to mean of observed data.
Non parametric equivalent for one sample t-test.

## Wilcoxon test - Two sample ##
Wilcoxon rank sum test.
Compare means of expected and observed data.
Non parametric equivalent for one sample t-test.
Also known as Mann-Whitney test.

