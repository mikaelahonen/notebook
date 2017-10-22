# Machine Learning
Algorithms and methods that can handle variant and complex data.
I define machine algorithms to be able to solve
both categorical and numeric response variables.

## Bagging
A technique where other models, often trees, are used.
Also known as bootstrap aggregation.

## Boosting
Close friend with bagging.
In boosting better models have more impact in voting.

## CART
CART is a machine learning algorithm which stands for 
Classification And Regression Trees.
CART uses a greedy algorithm.

# K-nearest neighbors
One of the simplest classification methods.
Works for regression as well.

The algorithm:
Predict the class of a unseen observations.
By default all predictor variables should be numeric.

1. Define the training data set. 
2. For a new observation, 
look k number of observations that are closest.
in the training dataset.
3. The prediction is the class that has most "votes" 
from the neighbors.

You can use `knn()` function from `class` library.
The `knn()` doesn't create a model object like most
of the other machine learning functions does.

## MARS
Multivariate Adaptive Regression Splines.
Closely related to CART: Create a large model and
prunes the tree.
Use function `earth()` from package `earth`.

## Neural Network
In neural network each observation corresponds to
and input value. 

In classification there are as many output variables
as there are classification groups.
In regression (numeric prediction) only a single 
output is used.

There might be one or multiple hidden layers with
any number of nodes.
Each observation (input node) is connected to each
node of the first input layers. If there are multiple 
hidden layers, all of the nodes in the first input layers
are connected to all nodes of the second input layer and so on.
Finally the last hidden layer is connected to the output layer.

Bias unit is a constant input term.

Use `softmax` function for classification
and `sigmoid` for regression.

Use `nnet` package. 
The package only allows a single hidden layer.

## Random forest
Trees in random forest aren't pruned like in CART,
so they grow to deeper level.

## Support vector machines
Works for classification and regression, 
even though it's more often applied to classification problems.


[Read more](https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/)

Use `e1071` package and function `svm()`.


