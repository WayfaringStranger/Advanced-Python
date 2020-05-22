set_org = {1, 2, 3, 4, 5}

# this just copies the reference to the set, so be careful
set_copy = set_org

# now modifying the copy also affects the original
set_copy.update([3, 4, 5, 6, 7])
print(set_copy)
print(set_org)

# use copy() to actually copy the set
set_org = {1, 2, 3, 4, 5}
set_copy = set_org.copy()

# now modifying the copy does not affect the original
set_copy.update([3, 4, 5, 6, 7])
print(set_copy)
print(set_org)
