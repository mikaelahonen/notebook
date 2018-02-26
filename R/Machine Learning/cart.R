library(rpart)

fit <- rpart(Species~., data=iris)

#Print complexity parameters
printcp(fit)
#Plot complexity parameters
plotcp(fit, main="plotcp")

# Plot the tree. 
#Uniform = TRUE > uniform vertical spacing of the nodes
plot(fit, uniform=TRUE, compress=TRUE, main="Decision Tree")

#Add labels to all classes
#xpd prevents label to go outside the plot area
text(fit, use.n=TRUE, all=TRUE, cex=0.7, xpd=TRUE)

#Simplify the tree with prune()
#cp (complexity parameter) defines how much to prune the tree