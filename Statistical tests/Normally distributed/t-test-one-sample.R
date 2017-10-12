#pastecs library for stat.desc function
library(pastecs)

#Create two distributions
d.observed <- c(0,0,1,2,2,2,5,7,10,10,10,10,10,20,20)
d.expected <- 3

#Show summary statistics
stat.desc(d.observed)

#One sample T-test
#Calculate probibility that the mean of observed data is less than 3
t.test(d.observed, alternative="greater", mu=d.expected, conf.level=0.95)
