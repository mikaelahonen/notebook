library(reshape)

#Melt all
a.1 <- sample(1:5,5,replace=TRUE)
b.1 <- sample(1:5,5,replace=TRUE)
df.1 <- data.frame(a.1,b.1)
df.1

melt(df.1)

#When id is defined, it has been left out from melting
id <- 1:10
a.2 <- sample(1:5,10,replace=TRUE)
b.2 <- sample(1:5,10,replace=TRUE)
df.2 <- data.frame(id,a.2,b.2)
df.2

melt(df.2, id.vars="id")
