# Normally distributed statistical tests #
Use these test when it's excpected that data is normally distributed.

## ANOVA ##
Stands for <i>Analysis of variance</i>.
It is meant to compare means of more than two groups.
As it's investigating the mean - not the variance - the name is misleading.
Use either `aov()` or fit linear model first with `lm()`.
<br/>
<br/>
When ANOVA is used for one or two categories, it's equal to t-test.
<br/>
<br/>
ANOVA compares variation within and between groups.
If the difference is significant, then the difference of means will also be.
<br/>
<br/>
Assumptions
* Population of each group is normally distributed
* Variance in each group's population is the same
* Group samples are random
* Group samples independent of each other
<br/>
<br/>
Notes:
* Variance should be equal among the groups
* [Read more](http://cba.ualr.edu/smartstat/topics/anova/example.pdf)

## Correlation test ##
Calculate confidence interval for correlation with given probability.
Function `cor.test()` is used.

## F-test ##
Test if true ratio of variances is equal to 1.

## T-test - One sample ##
Compare mean of a distribution to the expected mean.


## T-test - Two sample ##
Compare means of two distributions.
<br/>
<br/>
For example
* Are two sets of tires from the same set?
* Is it co-incidence that people in one organizations are happier than in the other?

## T-test - Paired ##
Compare means of two distributions pairwise. 
Basically this is a special case of one sample t-test.
In this version you create a single vector calculating the differences of each pair.
Then you do the one sample t-test with the expectation that the actual mean is 0.
<br/>
<br/>
For example
* Stock indexes before and after
* Weight loss for test persons before and after