# Statistics

## Factor Analysis ##
Simple use case for `factanal` function.
* Factor analysis is close friend of principal component analysis. 
* Factor analysis is used for situations where you want to test impact of latent factors. 
* Use different rotation if factors have correlation. [Read more](http://www.theanalysisfactor.com/rotations-factor-analysis/)
* [Difference to principal component analysis](https://stats.stackexchange.com/questions/1576/what-are-the-differences-between-factor-analysis-and-principal-component-analysi).

## Lasso
Least Absolute Selection Shrinkage Operator.
Useful, when model has many predictor variables.
Lambda is used to tune the penalty impact.

## Linear Discriminant Analysis ##
To do: Example of linear discriminant analysis.
* Reduces dimensions
* Tries to maximize separation between known categories
* [Youtube tutorial](https://www.youtube.com/watch?v=azXCzI57Yfc)

## Prinicpal Component Analysis ##
Example syntax of `princomp` function that performs a principal component analysis. 
* Prinicipal component analysis is used for dimensional reduction. 
* Does not assume a dependent variable ([source](ftp://statgen.ncsu.edu/pub/thorne/molevoclass/AtchleyOct19.pdf))
* Original variables are can not directly associated with specific principal components.
* [Difference to factor analysis](https://stats.stackexchange.com/questions/1576/what-are-the-differences-between-factor-analysis-and-principal-component-analysi).

## Stepwise variable selection
Minimize model complexity by AIC by
adding or removing a variable one at the time.

