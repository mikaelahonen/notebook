#Alternatively use MASS stepAIC

#Predictor variable
value <- c(10,20,30)

#Response variable
set.seed(20)
x <- 1:3
y <- 1:3
z <- 1:3

#Fit linear model
df <- data.frame(value,x,y,z)
df
lm <- lm(value ~ x+y+z, df)

lars(lm)
