#Variables
x <- 0
mean <- 0
sd <- 1

#Distribution height at given x value
dnorm(x, mean, sd, log=FALSE)

#Distribution probability at given x value
pnorm(x, mean, sd, log=FALSE)

#x value at given distribution density
p <- 0.5
qnorm(p, mean, sd, lower.tail=TRUE, log.p=FALSE)

#Generate 10 000 random normally distributed values
values <- rnorm(10000, mean, sd)
values[1:10]

#Histogram from generated values
hist(values, breaks=50)