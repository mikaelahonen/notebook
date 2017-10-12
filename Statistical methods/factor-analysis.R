#Examle from https://web.stanford.edu/class/psych253/tutorials/FactorAnalysis.html
d = read.table("http://www.stanford.edu/class/psych253/data/personality0.txt")
#scale-function transforms the vector values to normally distributed
d_scale <- as.data.frame(scale(d))
d_factanal <- factanal(d_scale, factors=10, rotation="none", na.action = na.omit)
#Show loadings
#Rule of thumb: Eigenvalue (loading) greater than 1 is significant
d_factanal$loadings