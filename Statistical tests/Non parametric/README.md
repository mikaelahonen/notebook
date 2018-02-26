# Non parametric tests #

Non parametric statistical tests are used, 
when you can't expect data to be normally distributed.

## Kruskal-Wallis Rank sum test ##

Non paramteric equivalent for ANOVA.

## Sign test ##

Investigate hypothesis that sample's
quantile is the expected value.
Mostly the quantile is 0.5 which is also known as median.

Compare sample values to the expected quantile value.
If the sample value is bigger than the epected it gets plus sign,
otherwise minus.
If the comparison is tie, the value is dropped and
the sample size decreased by one.

Use `BSDA` library and `SIGN.test()` function.

Doesn't expect symmetric distribution.

## Wilcox test - One sample ##
Compare an expected mean to mean of observed data.
Non parametric equivalent for one sample t-test.

Wilcox rank sum test 
* Expects symmetric distribution
* Applies only for median
* `wilcox.test()`

Procedure
1. Decrease the expected median from each value in sample.
2. Take the absolute value from those.
3. Sort absolute values from big to small.
4. Give each value rank starting from 1. On tie, give average rank.
5. Sum ranks for positive and negative values.
6. See results from a lookup table or use R.



## Wilcox test - Two sample ##
Also known as Mann-Whitney test.


