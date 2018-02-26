library(randomForest)

#Split to train and test data
set.seed(1)
data.iris <- data.frame(iris)
data.iris <- data.iris[sample(nrow(data.iris)),]

#Split to test and train data
data.train <- data.iris[1:75, ]
data.test <- data.iris[76:150, ]

#Fit the model
#sampsize: how many observations sampled per tree
#mtry: how many variables per tree
#nodesize: stop splitting when nodesizes is less than this
fit <- randomForest(Species~., 
                    data=data.train, 
                    importance=TRUE,
                    sampsize=50,
                    mtry=3,
                    nodesize=2)

#Show results
fit
importance(fit)

#Predict
prediction <- predict(fit, data.test)

#Bind to validation
data.results <- cbind(data.test, prediction)

#Calculate success rate
rate <- sum(data.results$Species == data.results$prediction)/nrow(data.results)
paste(round(rate,4)*100, "%")
