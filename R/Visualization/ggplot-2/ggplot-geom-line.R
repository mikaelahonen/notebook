#Create data
set.seed(1)
x <- 1:20
y <- 5+rnorm(20)
df <- data.frame(x,y)

#ggplot2 point plot
ggplot(data=df, mapping=aes(x=x, y=y)) +
  geom_line(color="gray")

