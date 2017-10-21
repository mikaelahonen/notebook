#Create data
x <- 1:20
y <- 5+rnorm(20)
df <- data.frame(x,y)

#Create plot
plot(x, y)

#Create data for spline. Default n = 3*length(x) .
fit <- loess(y ~ x, df)
pred <- predict(fit, df)

#Combine p
results <- cbind(df, pred)

#ggplot2 base plot
ggplot(data=results, mapping=aes(x=x, y=y)) +
  #observed dots
  geom_point(aes(y = y), color="red") +
  #loess line
  geom_line(aes(y = pred), color="black") +
  #scale coordination
  coord_cartesian(ylim=c(0:7))
  

