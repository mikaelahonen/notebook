# Normally distributed statistical tests #
Use these test when it's excpected that data is normally distributed.

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