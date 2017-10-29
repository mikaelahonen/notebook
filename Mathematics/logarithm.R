#x values
x.10 <- c(0.01,0.1,1,10,20,40)
#y values by log() functions
#base: define the logarithm base, e is default
y.10 <- log(x.10, base=10)

#Scatter plot
plot(x.10, y.10)
#Combine with lines
lines(x.10, y.10)
#Draw horizontal zero line
abline(h=0)