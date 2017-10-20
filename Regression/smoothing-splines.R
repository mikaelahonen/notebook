#Create data
x <- 1:9
y <- rnorm(9)

#Create plot
plot(x, y)

#Create spline variable
spline <- spline(x, y) 
lines(spline)
lines(spline(x, y, n = 201), col = 2)