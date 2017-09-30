library(ggplot2)

group <- rep(c("A","B","C"),2) 
value <- c(1,2,3,4,5,6)
df <- data.frame(group, value)

#barchart that sums by group
ggplot(df, aes(y=value, x=group)) + geom_col()