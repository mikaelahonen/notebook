library(reshape2)

#acast for vector or matrix output 
#dcast for data frame output

#Create data
variable <- sample(c("A","B"),10,replace=TRUE)
value <- sample(1:5,10,replace=TRUE)
df.1 <- data.frame(variable, value)
df.1

#Create columns from a categorical variable
dcast(df.1, value~variable)

