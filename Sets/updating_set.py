setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# update() : Update the set by adding elements from another set.
setA.update(setB)
print(setA)

# intersection_update() : Update the set by keeping only the elements found in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.intersection_update(setB)
print(setA)

# difference_update() : Update the set by removing elements found in another set.
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.difference_update(setB)
print(setA)

# symmetric_difference_update() : Update the set by only keeping the elements found in either set, but not in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.symmetric_difference_update(setB)
print(setA)

# Note: all update methods also work with other iterables as argument, e.g lists, tuples
# setA.update([1, 2, 3, 4, 5, 6])
