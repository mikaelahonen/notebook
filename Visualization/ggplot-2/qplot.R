library(ggplot2)
d.norm <- data.frame(value=rnorm(1000))
#Quick plot histogram
qplot(data=d.norm, x=value)