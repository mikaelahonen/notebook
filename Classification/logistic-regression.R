#Create data
x <- c(0,2,5,10,15,21,27,36,45,49,55,61,55,63,72,81,89,93,98,100)
y <- c(rep(0,12), rep(1,8))
df <- data.frame(x,y)

#Plot values
plot(x,y)

#Fit logistic regression
fit <- glm(y~x, family = "binomial", data = df)

#newdata argument of predict() takes data frame 
#with same column name than original predictor variable(s)
newdata <- data.frame(x=1:100)

#Predict probabilites for values of x
pred <- predict(fit, newdata, type="response")

#Print predicted values
round(pred,2)

#Draw line from predicted values
lines(pred)


