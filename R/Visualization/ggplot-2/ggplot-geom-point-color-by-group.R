library(ggplot2)

#Daa frame with x, observed and predicted variables.
data <- data.frame(
  x=1:4,
  y=1:4,
  group=c("A","A","B","B")
)

#Point plot per variable with colors
ggplot(data=data, aes(x=x, y=y, color=group)) +
  geom_point(size=5) +
  scale_color_manual(values=c(A="#11dddd", B="#dddd11"))