#APPLY
a <- c(1,2,3,4)
b <- c(5,6,7,8)
df.apply <- data.frame(a,b)

#Apply for rows
apply(df.apply,1,mean)

#Apply for columns
apply(df.apply,2,mean)

#Apply custom function: Percentage of column total
apply(df.apply,2,function(x) round(x/sum(x),2))


#LAPPLY
list.lapply = list(a=1:4,b=5:8)
list.lapply
lapply(list.lapply, mean)


#SAPPLY
list.sapply = list(a=1:4,b=5:8)
list.sapply
sapply(list.sapply, mean)


#TAPPLY
#Apply function per group in a variable
group <- rep(c("A","B","C"), 2)
value <- 1:6
df.tapply <- data.frame(group, value)
df.tapply
tapply(df.tapply$value, INDEX=list(df.tapply$group), FUN=mean)
