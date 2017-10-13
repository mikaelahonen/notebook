group <- rep(c("A","B","C"), 2)
value <- 1:6
df <- data.frame(group, value)
tapply(df$value, INDEX=list(df$group), FUN=mean)
