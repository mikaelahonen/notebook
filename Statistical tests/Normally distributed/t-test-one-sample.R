#pastecs library for stat.desc function
library(pastecs)

#Create the value vector with 100 normally distributed values
set.seed(1)
d.observed <- rnorm(100)

#Set expected value
d.expected <- -0.1

#Show histogram from observed values
hist(d.observed)

#Show summary statistics
stat.desc(d.observed)

#One sample T-test
#Calculate probibility that the mean of observed data is less than 3
t.test(d.observed, alternative="greater", mu=d.expected, conf.level=0.95)
