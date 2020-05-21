"""
Any immutable type, like strings or numbers can be used as a key. Also, a tuple can be used if it contains only immutable elements.
"""

# use numbers as key, but be careful
my_dict = {3: 9, 6: 36, 9:81}
# do not mistake the keys as indices of a list, e.g my_dict[0] is not possible here
print(my_dict[3], my_dict[6], my_dict[9])

# use a tuple with immutable elements (e.g. number, string)
my_tuple = (8, 7)
my_dict = {my_tuple: 15}

print(my_dict[my_tuple])
# print(my_dict[8, 7])

# a list is not possible because it is not immutable
# this will raise an Error:
# my_list = [8, 7]
# my_dict = {my_list: 15}
