#1
try:
	print(1/2)
except:
	print("Error 1: Invalid division!")
#2
try:
	print(1/0)
except:
	print("Error 2: Invalid division!")
#3
try:
	print(1/0)
except Exception as e:
	print('Uncaught exception: ' + str(e))	
#4
try:
	print(1/0)
except ZeroDivisionError:
	print("ZeroDivisionError happened")

