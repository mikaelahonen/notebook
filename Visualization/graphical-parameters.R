#dev.off() resets par() to defaults 
dev.off()

#Label align. 0=left, 1=right
par(adj=0)

#Set plot view to 2x2
par(mfrow=c(2,1))

#Background color
par(bg="hotpink")


#Create plots
plot(rnorm(2),rnorm(2),xlab="X 1",ylab="Y 2",main="Plot 1")
plot(rnorm(2),rnorm(2),xlab="X 2",ylab="Y 2",main="Plot 2")