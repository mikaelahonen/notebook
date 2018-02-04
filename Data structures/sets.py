#Set a
a = set('hello!')
b = set('howdy!')

print('a: "hello!". b: "howdy!"')

print('Set stores unque items in random order')
print(a)

print('Sorted set')
print(sorted(a))

print('Common items in a and b')
print(a & b)

print('All unique items in one or both')
print(a | b)

print('All items in one but not in both.')
print(a ^ b)

print('Every item in the first but not the latter.')
print(a-b)

print('True if every item in b is in a.')
print(a>b)