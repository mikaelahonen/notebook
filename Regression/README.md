# Regression
Regression is a term to for analysis where
a sginle response variable (dependent variable) changes
according to predictor variables (independent variables).
All variables in regression are numeric (continuous).

Regressions can be used either to explain the phenomen
or to predict the unseen values.

## Anscombe
The `anscombe` dataset has four different x-y-pairs.
Each of them has almost similar descriptive statistics
but look very different when plotted.

Common summary statistics:
* Mean of x: 0
* Sample variance of x: 11
* Mean of y: 7.50
* Correlation bettweeb x and y: 0.816
* Linear refgression line: y=3.00+0.500x
* Coefficient of determination of the linear regression*: 0.67

<i>*the proportion of the variance in the dependent variable 
that is predictable from the independent variable(s).</i>

## Linear regression
Fit a linear function by minimizing the sum of squared residuals.

Use function `lm()`.

## Local regression
Perform a local fit for data.
Use `loess()` function for this. 

## Stepwise variable selection
AIC is used for selection.
AIC = [Akaike Information Criterion](https://en.wikipedia.org/wiki/Akaike_information_criterion).



