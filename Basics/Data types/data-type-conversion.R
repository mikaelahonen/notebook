#Table to data frame
tbl <- table(sample(c("A","B","C"),10,replace=TRUE))
tbl.df.long <- as.data.frame(tbl) 
tbl.df.short <- as.data.frame.matrix(tbl.df.long)
tbl.df.short
