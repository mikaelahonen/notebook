#Create matrix
vector <- c(1,2,3,4,5,6)
matrix <- matrix(vector, nrow=3, ncol=2)
matrix

#Check if matrix
is.matrix(matrix)

#Transpose
matrix.t <- t(matrix)
matrix.t

#Multiply matrixs:
#(1*1)+(4*4)=17
#(1*2)+(4*5)=22
#(1*3)+(4*6)=27
matrix %*% matrix.t

#rbind

#cbind