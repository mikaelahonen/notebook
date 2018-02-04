import math
import collections

#Initiate a counter class
counter = collections.Counter()

#Loop 1000 000 numbers
for i in range(0, 1000000):
	#Add count for the calculated integer
	counter[math.sqrt(i) // 25] += 1
	
#Print 5 most common integers
for key, count in counter.most_common(5):
	print('%s: %d' % (key, count))