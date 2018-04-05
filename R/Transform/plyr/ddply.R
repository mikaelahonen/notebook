library(plyr)

group <- c("A","A","B","A","B")
b <- c(2,4,6,8,10)
c <- c(2,4,8,16,32)
df <- data.frame(group,b,c)
df

#Count rows per group
ddply(df, .(df$group), "nrow")

#Get max of b column. The last row of function determines the returned value
#The argument x in function() declaration is the subset of data containing only values for the group being processed
ddply(df, .(df$group), .progress="text", .fun=function(x){
  max(x$b)
})
