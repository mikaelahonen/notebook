#Fisher's test works using either
## two categorical vectors as x and y argument
## table(x,y) as x argument


x <- c(rep("A",3), rep("B",3), rep("C",3))
y <- x

#Replace couple of values from y
y[4] <- "A"
y[7] <- "A"

#Print vectors
x
y

fisher.test(x,y)