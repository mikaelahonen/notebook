#Create data frame
a <- 1:3
b <- 4:6
df <- data.frame(a,b)

#Get column from data frame
df$a

#Filter: column `a` greater or equal to `2`
df[df$a>=2, ]
