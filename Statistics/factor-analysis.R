#Examle from https://web.stanford.edu/class/psych253/tutorials/FactorAnalysis.html
d = read.table("http://www.stanford.edu/class/psych253/data/personality0.txt")
d_scale = as.data.frame(scale(d))
d_factanal <- factanal(d_scale, factors=10, rotation="none", na.action = na.omit)