''' r-length tuples, in sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order. combinations() does not allow repeated elements, but combinationswithreplacement() does. '''

from itertools import combinations, combinations_with_replacement

# the second argument is mandatory and specifies the length of the output tuples.
comb = combinations([1, 2, 3, 4], 2)
print(list(comb))

comb = combinations_with_replacement([1, 2, 3, 4], 2)
print(list(comb))
