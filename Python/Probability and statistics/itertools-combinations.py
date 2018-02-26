#Unique combinations of items
import itertools
r = range(3)
o = itertools.combinations(r, 2)
l = list(o)
print(l)