#Data
x <- c(1,2,3,4,10)
y <- c(1,2,6,4,5)
z <- c(1,2,3,4,5)
xyz <- data.frame(x,y,z)

#3d visualization from data points
attach(xyz)
plot3d(x, y, z, type="s", col=as.numeric(Species), size=1)

#Principal component analysis
pca <- princomp(~x+y+z, xyz)

#Print results
summary(pca)

#Sum of squares is 1 for each row
pca$loadings

#Show values for each observation
pca$scores

#Draw plots
plot(pca)
biplot(pca)

