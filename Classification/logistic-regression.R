#Create data
x <- c(0,2,5,10,15,21,27,33,39,51,49,65,72,78,83,85,89,93,98,100)
y <- c(rep(0,10), rep(1,10))
df <- data.frame(x,y)

#Plot values
plot(x,y)

#Fit logistic regression
fit <- glm(y~x, family = "binomial", data = df)

#newdata argument of predict() takes data frame 
#with same column name than original predictor variable(s)
newdata <- data.frame(x=1:100)

#Predict
pred <- predict(fit, newdata, type="response")

#Draw line from predicted values
lines(pred)
