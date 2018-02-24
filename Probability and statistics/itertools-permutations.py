#Permutations are combinations where order of items matter
import itertools
r = range(3)
o = itertools.permutations(r, 2)
l = list(o)
print(l)