#Create data
x <- 1:10
y <- rnorm(10)

#Create plot
plot(x, y)

#Create data for spline. Default n = 3*length(x) .
s.default <- spline(x, y)
lines(s.default)

#Create more accurate data for spline
s.200 <- spline(x, y, n = 200)
lines(s.200, col = "red")