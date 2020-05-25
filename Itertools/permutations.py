''' This tool returns successive length permutations of elements in an iterable, with all possible orderings, and no repeated elements. '''

from itertools import permutations

perm = permutations([1, 2, 3])
print(list(perm))

# optional: the length of the permutation tuples
perm = permutations([1, 2, 3], 2)
print(list(perm))
