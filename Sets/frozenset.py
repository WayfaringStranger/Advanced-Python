'''
Frozen set is just an immutable version of normal set. While elements of a set can be modified at any time, elements of frozen set remains the same after creation. Creation with: my_frozenset = frozenset(iterable)
'''

a = frozenset([0, 1, 2, 3, 4])

# The following is not allowed:
# a.add(5)
# a.remove(1)
# a.discard(1)
# a.clear()

# Also no update methods are allowed:
# a.update([1,2,3])

# Other set operations work
odds = frozenset({1, 3, 5, 7, 9})
evens = frozenset({0, 2, 4, 6, 8})
print(odds.union(evens))
print(odds.intersection(evens))
print(odds.difference(evens))
