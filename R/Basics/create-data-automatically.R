#Sequence by start, end and interval
seq(0, 1, 0.2)

#Sequence by start, interval and length
seq(10, by=10, length.out=5)

#Sequence of length 10 that sums to 1
seq(0.01, by=0.02, length.out=10)

#Repeat a value number of times
rep("x", 5)

#Integer range
1:5
-5:-1

#Random numbers
runif(5, 1, 10)

#Random integers
sample(1:10, 5, replace=T)

#Random categories
sample(c("A","B"), 5, replace=T)
