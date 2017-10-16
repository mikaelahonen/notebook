#Create matrice
vector <- c(1,2,3,4,5,6)
matrice <- matrix(vector, nrow=3, ncol=2)
matrice

#Transpose
matrice.t <- t(matrice)
matrice.t

#Multiply matrices:
#(1*1)+(4*4)=17
#(1*2)+(4*5)=22
#(1*3)+(4*6)=27
matrice %*% matrice.t

#rbind

#cbind