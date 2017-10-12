#pastecs library for stat.desc function
library(pastecs)

#Create two distributions
d.before <- c(100,100,100,100,100,100,100,100,100,100)
d.after <-  c(200,110,190,310,450,120,130,160,170,250)

#Two sample T-test
t.test(d.before, d.after, paired=TRUE)