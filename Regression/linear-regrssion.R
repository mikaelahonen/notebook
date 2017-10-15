#Predictor variable
x <- 1:20

#Response variable
set.seed(20)
y <- 1:20 + round(rnorm(20), 1)

#Fit linear model
df <- data.frame(x,y)
df
lm <- lm(y~x, df)

#Get intercept and coefficient
i <- lm$coefficients[[1]]
c <- lm$coefficients[[2]]

#Plot
plot(x,y)
abline(i,c,col="red")

#Test with new data
newdata = data.frame(x=c(21,22))
predict(lm, newdata)

