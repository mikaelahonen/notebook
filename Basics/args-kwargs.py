def addAndMultiply(coeff, *args, **kwargs):
	#x should be given as keyword argument
	ans = (kwargs['x']+args[0])*coeff
	return ans

#Returns (2+1)*4=12
result = addAndMultiply(4,1,x=2)
#Print result
print(result)