library(ggplot2)

x <- 1:10
y <- 1:10
group <- rep(c("odd","even"),5)
df <- data.frame(x, y, group)

#Quick plot with two panels
qplot(data=df, x=x, y=y, facets=group~.)