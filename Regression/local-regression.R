#Create data
set.seed(1)
x <- 1:20
y <- 5+rnorm(20)
df <- data.frame(x,y)

#Create plot
plot(x, y)

#Create data for spline. 
#n: Number of fitted values to calculate. Dedault is 3*length(x) 
#degree: Degree of polynoms
#span: Small number > line goes from dot to dot. Big number > almost straight line.
fit <- loess(y ~ x, df, span=0.5, degree=2)

#ggplot2 base plot
ggplot(data=df, mapping=aes(x=x, y=y)) +
  #observed dots
  geom_point(aes(y = y), color="red") +
  #loess line
  geom_line(aes(y = fit$fitted), color="black") +
  #scale coordination
  coord_cartesian(ylim=c(0:7))
  

