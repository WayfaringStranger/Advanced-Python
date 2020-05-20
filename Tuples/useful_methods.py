my_tuple = ('a','p','p','l','e',)

# len() : get the number of elements in a tuple
print(len(my_tuple))

# count(x) : Return the number of items that is equal to x
print(my_tuple.count('p'))

# index(x) : Return index of first item that is equal to x
print(my_tuple.index('l'))

# repetition
my_tuple = ('a', 'b') * 5
print(my_tuple)

# concatenation
my_tuple = (1,2,3) + (4,5,6)
print(my_tuple)

# convert list to a tuple and vice versa
my_list = ['a', 'b', 'c', 'd']
list_to_tuple = tuple(my_list)
print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)

# convert string to tuple
string_to_tuple = tuple('Hello')
print(string_to_tuple)
