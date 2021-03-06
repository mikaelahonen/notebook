library(ggplot2)

#Daa frame with x, observed and predicted variables.
data <- data.frame(
  x=1:20,
  observed=1:20+rnorm(20)*2,
  predicted=1:20
)

#Point plot per variable with colors
ggplot(data=data, mapping=aes(x=x, y=y)) +
  geom_point(aes(y = observed), color="black") +
  geom_point(aes(y = predicted), color="red")