# R Examples #
This repository is mainly for my personal learning but I'm glad if it's helpful to others' projects as well.

## Statistics ##

### Factor Analysis ##
Simple use case for `factanal` function.
* Factor analysis is close friend of principal component analysis. 
* Factor analysis is used for situations where you want to test impact of latent factors. 
* Use different rotation if factors have correlation. [Read more](http://www.theanalysisfactor.com/rotations-factor-analysis/)
* [Difference to principal component analysis](https://stats.stackexchange.com/questions/1576/what-are-the-differences-between-factor-analysis-and-principal-component-analysi).

### Linear Discriminant Analysis ###
To do: Example of linear discriminant analysis.
* Reduces dimensions
* Tries to maximize separation between known categories
* [Youtube tutorial](https://www.youtube.com/watch?v=azXCzI57Yfc)

### Prinicpal Component Analysis ###
Example syntax of `princomp` function that performs a principal component analysis. 
* Prinicipal component analysis is used for dimensional reduction. 
* Does not assume a dependent variable ([source](ftp://statgen.ncsu.edu/pub/thorne/molevoclass/AtchleyOct19.pdf))
* Original variables are can not directly associated with specific principal components.
* [Difference to factor analysis](https://stats.stackexchange.com/questions/1576/what-are-the-differences-between-factor-analysis-and-principal-component-analysi).

## Visualization ##
### Basic Graphics ###
Some simple R plots to get started quickly.

### corrplot library ###
Create a visual correlation matrix with corrplot library.

### ggplot2 library ###
Some simple R plots made with `ggplot2` graphics library to get started quickly.
* Great [cheatsheet](https://www.rstudio.com/resources/cheatsheets/) for ggplot2 in RStudio web page.
* Use `qplot()` for less detailed plots
* Use `ggplot()` together with additional definitions for more detailed plots
* Define dataset and variable mappings in `ggplot()` base function
* Use geom_ functions with `ggplot()` to actually draw plots. For example `ggplot() + geom_point()`

