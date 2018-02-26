#Create data
x <- c(10:15)
y <- c(10:15)
df <- data.frame(x,y)

#Use coord_cartesian to set the limits for x and y
ggplot(data=df) +
  geom_point(aes(x=x, y = y)) +
  coord_cartesian(xlim=c(0:15), ylim=c(0,15))

