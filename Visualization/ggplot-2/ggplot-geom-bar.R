library(ggplot2)

group <- c("A","A","A","B","C","C") 
df <- data.frame(group)

#Simple barchart that counts occurences of each group
ggplot(df, aes(x=group)) + geom_bar()