#In deque every item points to the next and the previous item
#Only items in beginning and end should be changed

import collections

#Create queue
queue = collections.deque()

#Append items to queue
queue.append(1)
queue.append(2)
queue.append(3)

print('Show deque content')
print(queue)

print('Pop left and right')
queue.popleft()
queue.pop()

print('Remaining deque')
print(queue)

print('Loop circular deques 5 times with maxlen=2')
circular = collections.deque(maxlen=2)
for i in range(5):
	circular.append(i)
	print(circular)