#Take aggregated Titanic data to data frame
df <- data.frame(Titanic)
#Get number of rows
row.max.1 <- nrow(df)
#Get row numbers repeated by the times of frequency column
row.ids <- rep(1:row.max.1, df$Freq)
#Repeat the rows by row ids
df.2 <- df[row.ids, ]
#Optional: Change row names
row.max.2 <- nrow(df.2)
rownames(df.2) <- 1:row.max.2
#Print
df.2
