#Vector 1
x.1 <- c(100,500,400,300)
#Add 10%
x.2 <- c(110,550,440,330)
#Substract 10%
x.3 <- c(90,450,360,270)
#Combine vectors
x <- c(x.1, x.2, x.3)
#Get autocorrelations. The pattern will appear every 4 values.
acf(x)
