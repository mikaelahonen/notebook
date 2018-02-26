import collections

#Node data
nodes = [
	('a', 'b'),
	('a', 'c'),
	('b', 'a'),
	('b', 'd'),
	('c', 'a'),
	('d', 'a'),
	('d', 'b'),
	('d', 'c'),
]

#Create a graph by using default dict
graph = collections.defaultdict(list)
