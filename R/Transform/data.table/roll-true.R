library(data.table)

#roll=TRUE finds smaller or equal

key.1 <- c(1, 2, 3)
val.1 <- c("a", "b", "c")
df.1 <- data.frame(key.1, val.1)
dt.1 <- data.table(df.1)
setkey(dt.1, c("key.1"))

key.2 <- c(0.8,0.9,1,1.2,1.3, 2.12, 3.83)
val.2 <- c("e", "f", "g", "h", "i", "j", "k")
df.2 <- data.frame(key.2, val.2)
dt.2 <- data.table(df.2)
setkey(dt.2, c("key.2"))

dt.1[dt.2, roll=TRUE, on=c(key.1="key.2")]