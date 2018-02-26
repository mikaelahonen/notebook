#Examle from https://web.stanford.edu/class/psych253/tutorials/FactorAnalysis.html
#install.packages('corrplot')
library(corrplot)
d = read.table("http://www.stanford.edu/class/psych253/data/personality0.txt")
corrplot(cor(d), order = "hclust", tl.col='black', tl.cex=.75) 