# Classification
Classification algorithms and methods aim to
diagnose and predict categorical response variables.

## Logistic regression
Predicts probabilities for binary response variables.
Predictor variables are numeric.

`0` and `1` labels should be approxiamtely balanced
in the population.

## Naive bayes
Also all independent variables must be categorical.

Use cases:
* Spam filter

Bayes law: `p(s|p) = p(p|s)p(s)/p(p)`.

Example:
* p(s) = I'm sick
* p(p) = Test is positive
* p(s|p) = I'm sick given that test is positive
* p(p|s) = Test is positive given that I'm sick

Use `e1071` library and `naiveBayes()` function. 
A-priori probabilities are the simple total probabilities.

Naive Bayes assumes independency between variables.
That's why you don't just sum up the number of observations
in a specific category and calculate the ratio.
To calculate probabilities by multiple predictors, 
first calculate proportional probabilities.

Here's an example when predictors are `x`, `y` and `z` and `r` is the response.
`r` means that event occurs and !r that it doesn't.
`p(!r|x,y,z) = p(x|!r) * p(y|!r) * p(z|!r) * p(!r)`
`p(r|x,y,z) = p(x|r) * p(y|r) * p(z|r) * p(r)`

Then you can scale `p(r|x,y,z)` and `p(!r|x,y,z)` so that the total to `1`.

[Calculate multiple variables](https://rpubs.com/dvorakt/144238).

