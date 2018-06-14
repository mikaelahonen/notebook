#In progress...

#Also known as Lorenz distribution
#X/Y = Cauchy(0,1)

x.1 <- rnorm(1000)
x.2 <- rnorm(1000)
cauchy <- x.1/x.2

par(mfrow=c(2,2))
hist(x.1)
hist(x.2)
hist(cauchy)
