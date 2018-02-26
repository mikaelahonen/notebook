#Alternatively use MASS stepAIC

#Predictor variable
value <- 1:20

#Response variable
set.seed(20)
x <- 1:20 + round(rnorm(20)*1.0, 1)
y <- 1:20 + round(rnorm(20)*2.0, 1)
z <- 1:20 + round(rnorm(20)*0.1, 1)

#Fit linear model
df <- data.frame(value,x,y,z)
df
lm <- lm(value ~ x+y+z, df)

#Do the forward stepwise variable selection
step(lm, direction="forward")
#Do the backward stepwise variable selection
step(lm, direction="backward")
