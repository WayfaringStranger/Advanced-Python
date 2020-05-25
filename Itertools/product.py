''' This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops. For example, product(A, B) returns the same as ((x,y) for x in A for y in B). '''

from itertools import product

prod = product([1, 2], [3, 4])
print(list(prod)) # note that we convert the iterator to a list for printing

# to allow the product of an iterable with itself, specify the number of repetitions
prod = product([1, 2], [3], repeat=2)
print(list(prod)) # note that we convert the iterator to a list for printing
