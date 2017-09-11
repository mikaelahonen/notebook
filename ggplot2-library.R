library(ggplot2)

#Data
d.norm <- data.frame(value=rnorm(1000))
d.panels <- data.frame(a=c(0:9), b=c(1:10), c=c(rep(c("odd","even"), times=5)))

var.1 <- rep(c("A","B","C"),2) 
var.2 <- c(rep("X",3), rep("Y",3))
var.3 <- c(1,2,3,4,5,6)
d.groups <- data.frame(group.1=var.1, group.2=var.2, value=var.3)


#Quick plot histogram
qplot(data=d.norm, x=value)

#Quick plot density function
qplot(data=d.norm, x=value, geom="density")

#Quick plot with two panels
qplot(data=d.panels, x=a, y=b, facets=c~.)

#ggplot2 point plot
ggplot(data=d.panels, mapping=aes(x=a, y=b)) + geom_point()

#Simple barchart that counts occurences of each group
ggplot(d.groups, aes(x=group.1)) + geom_bar()

#barchart that sums by group
ggplot(d.groups, aes(y=value, x=group.1)) + geom_col()

#Barchart for multiple groups to stack, use position="stack"
ggplot(d.groups, aes(x=group.1, y=value, fill=group.2)) + geom_col(position="dodge")

#Barcharts grouped to different panels by a group and colored
ggplot(d.groups, aes(x=group.1, y=value, fill=group.2)) + geom_col(position="dodge") + facet_wrap(~group.2, ncol=1)

