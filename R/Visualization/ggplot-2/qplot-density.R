library(ggplot2)

d.norm <- data.frame(value=rnorm(1000))

#Quick plot density function
qplot(data=d.norm, x=value, geom="density")