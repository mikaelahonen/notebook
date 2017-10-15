# Non parametric tests #
<p>
Non parametric statistical tests are used, 
when you can't expect data to be normally distributed.
</p>

## Kruskal-Wallis Rank sum test ##
<p>
Non paramteric equivalent for ANOVA.
</p>

## Sign test ##
<p>
Investigate hypothesis that sample's
quantile is the expected value.
Mostly the quantile is 0.5 which is also known as median.
</p>
<p>
Compare sample values to the expected quantile value.
If the sample value is bigger than the epected it gets plus sign,
otherwise minus.
If the comparison is tie, the value is dropped and
the sample size decreased by one.
</p>
<p>
Use `BSDA` library and `SIGN.test()` function.
</p>


## Wilcoxon test - One sample ##
<p>
Compare an expected mean to mean of observed data.
Non parametric equivalent for one sample t-test.
</p>

## Wilcoxon test - Two sample ##
<p>
Wilcoxon rank sum test.
Compare means of expected and observed data.
Non parametric equivalent for one sample t-test.
Also known as Mann-Whitney test.
</p>

