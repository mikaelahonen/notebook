library(nnet)

#Randomize the order of data
order <- sample(nrow(iris))
d.sample <- iris[order,]

#Train and test data
d.train <- d.sample[1:100,]
d.test <- d.sample[101:150,]

#Fit the neuwal netowrk model
#size: how many nodes in the hidden layer
#weights: emphasize some observations more
#maxit: maximum number of iteratiosn 
fit <- nnet(Species~., 
            data=d.train, 
            size=3,
            maxit=200)

#Predict
d.pred <- predict(fit, d.test)

#Get the most probable class name
i <- apply(d.pred,1,which.max)
class <- colnames(d.pred)[i]

#Factor levels must be same than original variable, else an error happens
class <- factor(class, levels=levels(iris$Species))

#Combine predictions to test data
d.results <- cbind(d.test, class)

#New column: correctly predicted or not? 
d.results$correct <- d.results$Species==d.results$class

#Count success ratio
mean(d.results$correct)
