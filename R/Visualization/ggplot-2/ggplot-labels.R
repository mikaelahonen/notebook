x <- 1:3
y <- 1:3
label <- c("A", "B", "C")

d <- data.frame(x,y,label) 

#plot and set labels
ggplot(data=d, mapping=aes(x=x, y=y)) +
  geom_point() +
  geom_text(aes(label=label),hjust=0, vjust=-1)