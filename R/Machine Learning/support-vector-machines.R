library(e1071)

#Randomize the order of data
order <- sample(nrow(iris))
d.sample <- iris[order,]

#Train and test data
d.train <- d.sample[1:100,]
d.test <- d.sample[101:150,]

#Fit the model
fit <- svm(Species~., data=d.train)
summary(fit)

#Predict the class
class <- predict(fit, d.test)

#Combine predictions to test data
d.results <- cbind(d.test, class)

#New column: correctly predicted or not? 
d.results$correct <- d.results$Species==d.results$class

#Count success ratio
mean(d.results$correct)
