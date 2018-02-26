#Example in progress

#Library for lasso
library(lars)

#predictors
x.1 <- c(1,3,5,4,10)
x.2 <- c(1,4,3,4,2)
x.3 <- c(6,2,3,4,15)
x <- matrix(c(x.1,x.2,x.3),ncol=3)

#repsonse
y <- c(1,2,3,4,5)

#Data frame
df <- data.frame(x.1,x.2,x.3,y)

#lasso
fit.lasso <- lars(x, y)
df.lasso <- predict.lars(fit.lasso, newx=x ,type="fit")

#linear
fit.lm <- lm(y~., df)

#Bind
compare <- cbind(df,fit.lasso$)

#RSS Residual Squared Sums
sum(fit.lasso$RSS)
sum((fit.lm$fitted.values-y)^2)
