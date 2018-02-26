#random vector length 10
set.seed(100)
rand <- runif(10, -2, 2)

#x values
x <- 1:10

#y values
y <- 1:10 + rand

#plot x and y vector
plot(x, y)

#test for correlation
cor.test(x, y)