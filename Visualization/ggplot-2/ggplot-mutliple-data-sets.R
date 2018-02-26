#Data set 2
x.1 <- c(10,20)
y.1 <- c(10,20)
d.1 <- data.frame(x.1, y.1) 

#Data set 2
x.2 <- c(10,15)
y.2 <- c(12,20)
d.2 <- data.frame(x.2, y.2) 

#base plot
ggplot(data=d.1, aes(x=x.1, y=y.1)) +
  geom_line() +
  geom_line(data=d.2, aes(x=x.2, y=y.2))