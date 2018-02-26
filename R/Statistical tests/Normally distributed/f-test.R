#pastecs library for stat.desc function
library(pastecs)

#Create two distributions
d.observed <- c(0,0,1,2,2,2,3,5,5,5,5,8,8,9)
d.expected <- c(1,1,1,2,2,2,2,4,4,4,5,5,5,5)

#Show summary statistics
df <- data.frame(d.expected, d.observed)
stat.desc(df)

#Two sample T-test
var.test(d.observed, d.expected)