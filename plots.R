#Some data for plots
data.1 <- c(1,1,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6)
data.2 <- c(12,14,10,16)
data.3 <- data.frame(group=c("A","B","C"), value=c(5,15,10))
data.4 <- matrix(c(1,2,3,4,5,6,7,8,9), nrow=3, byrow=TRUE)

#Show 2x2 plots
par(mfrow=c(2,3))

#Histograms
h <- hist(data.1, breaks=c(0,2,4,6))
abline(h=8)

#Density
d <- density(data.1)
plot(d)
polygon(d, col="forestgreen")
abline(v=3.5)

#Barplot
barplot(data.2, col=c("lightgray","lightgray","lightgray","forestgreen"))

#Dot chart
dotchart(data.3$value, labels=data.3$group)

#Image
image(data.4)

#Contour
x <- c(1:49,50,49:1)
values <- outer(sqrt(x), sqrt(x), FUN = '*')
axis <- 1:99
image(axis, axis, values)
contour(axis, axis, values, col = "pink", add=TRUE, method = "edge")