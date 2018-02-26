#Use yield to read big csv files for example
#If the body of the def contains 'yield',
#  the function automatically becomes a generator function

#Example 1
def simple_generator_1():
	yield 1
	yield 2
	yield 3

#Print all
print("Example 1.1")
for value in simple_generator_1():
	print(value)
	
#Print all
print("Example 1.2")
generator_var = simple_generator_1()
print(next(generator_var))
print(next(generator_var))
print(next(generator_var))


#Example 2: Same but with loop
def simple_generator_2():
	#Loop values from 0 to 2
	for i in range(3):
		yield i+1

print("Example 2.1")
for value in simple_generator_2():
	print(value)
