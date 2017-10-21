# Regression
Regression is a term to for analysis where
a sginle response variable (dependent variable) changes
according to predictor variables (independent variables).
All variables in regression are numeric (continuous).

Regressions can be used either to explain the phenomen
or to predict the unseen values.

## Linear regression
Fit a linear function by minimizing the sum of squared residuals.

Use function `lm()`.

## Local regression
Perform a local fit for data.
Use `loess()` function for this. 

## Stepwise variable selection
AIC is used for selection.
AIC = [Akaike Information Criterion](https://en.wikipedia.org/wiki/Akaike_information_criterion).

## Survival analysis
Answers to the question: What time it takes for an event to occur?
The value is always greater than zero.
Incompletely observed responses are censored.

Right censoring means that a subject doesn't experience the event before the study ends.
There are three main reasons for censoring:
* The event doesn't occur before the end of the study
* A subject can not be reached for whatever reason
* A subject withdraws from the study

When the event has occured before the study begins it is called left censoring.

[Read more](http://www.stat.columbia.edu/~madigan/W2025/notes/survival.pdf).

Examples:
* Time until tumor recurrence
* Time to machine failure

In other fields:
* Social sciences: Event history analysis
* Engineering: Reliability analysis


