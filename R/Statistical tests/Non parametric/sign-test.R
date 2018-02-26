library(BSDA)

#Vector A length 10
set.seed(1)
a <- rep(10,10) + runif(10,-1,1)
mean(a)

#Vector B length 10
set.seed(2)
b <- rep(9, 10) + runif(10,-1,1)
mean(b)

#Sign test for differences
SIGN.test(a-b)
