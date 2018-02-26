#Test data
d <- c("Alpha","Delta","Charlie","Bravo")
#Create an order vector
o <- order(d)
#Create data frame
df <- data.frame(d)
#Order data frame
df[o,]
