#Create categorical vectors
x <- c(rep("A",5), rep("B",5))
y <- c(rep("A",2), rep("B",4), rep("A",4))

#Print x and y
x
y

#Create contingency table
table(x,y)