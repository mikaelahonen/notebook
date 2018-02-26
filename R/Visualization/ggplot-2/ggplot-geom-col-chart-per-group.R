library(ggplot2)

group.val <- rep(c("A","B","C"),2) 
group.col <- c(rep("X",3), rep("Y",3))
value <- c(1,2,3,4,5,6)
df <- data.frame(group.val, group.col, value)

ggplot(df, aes(x=group.val, y=value, fill=group.col)) + geom_col(position="dodge") + facet_wrap(~group.col, ncol=1)

#Use position="stack" to stack x and y on top of each other