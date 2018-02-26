import pprint

#Tuples are immutable lists
#Tuples can be used as a key in a dict 
# if they are hashable

a = 1, 2, 3
b = 4, 5, 6

data = dict()
data[a] = 'var a'
data[b] = 'var b'

print('Tuples as dict keys')
pprint.pprint(data)

# Assign multiple tuples
a, b, c = (1, 2), (2, 4), (4, 8)
print('Assigned multiple tuples, print a only')
print(a)

#Pack and unpack
pkg = 'value 1', 'value 2'
un_pkg_a, un_pkg_b = pkg
print('Pack a and b, print only unpacked a')
print(un_pkg_a)

#Variable number items
a, *b = 1, 2, 3, 4
print('Only the first of 4 items was assigned a')
print(a)
