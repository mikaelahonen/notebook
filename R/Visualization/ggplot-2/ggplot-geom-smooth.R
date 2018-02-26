library(ggplot2)

x <- c(1,1,2,3,3,4,5,6, 7, 8, 8, 9, 10,10,10,11)
y <- c(1,2,3,3,4,4,5,10,7 ,4, 15,14, 3, 4,20,20)
d.smooth <- data.frame(x,y)

#Geom smooth
ggplot(d.smooth, aes(x=x, y=y)) + geom_point() + geom_smooth(method="lm", level=0.95)
