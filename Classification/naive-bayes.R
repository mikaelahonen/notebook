library(e1071)

#Prepare data
#Take aggregated Titanic data to data frame
df <- data.frame(Titanic)
#Get number of rows
row.max.1 <- nrow(df)
#Get row numbers repeated by the times of frequency column
row.ids <- rep(1:row.max.1, df$Freq)
#Repeat the rows by row ids
data <- df[row.ids, 1:4]
data$all <- paste(data$Class,data$Sex,data$Age)

#Reorder data
ids <- sample(nrow(data))
data.sample <- data[ids,]

#Split to train and test data
data.train <- data.sample[1:1500, ]
data.test <- data.sample[1501:2201, ]

#Fit naive bayes model
fit <- naiveBayes(Survived~Age+Sex+Class, data=data.train)

#Predict probabilites
probs <- predict(fit, data.test, type = "raw")
probs <- data.frame(probs)

#Get more probable option
Prediction <- ifelse(probs$Yes>0.5,"Yes","No")

#Paste predicted probabilities to original data
data.test.new <- cbind(data.test, probs, Prediction)

#Prediction rate
sum(data.test.new$Survived == data.test.new$Prediction) / nrow(data.test.new)
