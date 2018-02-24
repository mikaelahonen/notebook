#Accumulate is similar to reduce() but it can track all iterations
import operator
import itertools

# Sales per day
days = [10, 8, 5, 7, 12, 10, 5]
#Accumulate
x_object = itertools.accumulate(days, operator.add)
#Itertools object to list
x_list = list(x_object)

#Print
print(x_list)