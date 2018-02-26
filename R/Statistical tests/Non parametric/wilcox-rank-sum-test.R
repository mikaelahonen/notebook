#pastecs library for stat.desc function
library(pastecs)

#Create the value vector with 100 normally distributed values
set.seed(1)
d.observed <- runif(20,0,10)
stat.desc(d.observed)

#Set expected value
set.seed(2)
d.expected <- runif(25,0,10)
stat.desc(d.expected)


wilcox.test(d.observed, d.expected)
