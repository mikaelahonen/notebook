#Fisher's test works using either
## two categorical vectors as x and y argument
## table(x,y) as x argument

#Chi square test works using either
## two categorical vectors as x and y argument
## table(x,y) as x argument

smoke <- matrix(c(51,43,22,92,28,21,68,22,9),ncol=3,byrow=TRUE)
colnames(smoke) <- c("High","Low","Middle")
rownames(smoke) <- c("current","former","never")
smoke <- as.table(smoke)

#Print table
smoke

#Do chi square test
#If needed, set probabilities as a vector p=c(...)
chisq.test(smoke)