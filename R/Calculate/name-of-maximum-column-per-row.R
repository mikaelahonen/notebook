a <- c(3,4,9)
b <- c(2,5,8)
c <- c(1,6,7)
df <- data.frame(a,b,c)
df

#Get column name of maximum column
index.list <- apply(df,1,which.max)

#Get column names by the list of indexes
colnames(df)[index.list]