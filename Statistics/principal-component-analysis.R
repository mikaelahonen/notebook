#Data
x <- c(1,2,2,4,5)
y <- c(1,5,2,4,3)
z <- c(1,3,5,2,4)
xyz <- data.frame(x,y,z)

#Principal component analysis
pca <- princomp(~x+y+z, xyz)

#Print results
summary(pca)
loadings(pca)

#Draw plots
plot(pca)
biplot(pca)

