library(ggplot2)

df <- data.frame(x=c(0:9), y=c(1:10))

#ggplot2 point plot
ggplot(data=df, mapping=aes(x=x, y=y)) + geom_point()