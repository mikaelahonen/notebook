import operator
import functools

ls = ['H', 'ell', 'o!']

#User operator library
x_1 = functools.reduce(operator.concat, ls)
print(x_1)

#Do the same with custom function
def r(a,b):
	return a+b

x_2 = functools.reduce(r, ls)
print(x_2)
