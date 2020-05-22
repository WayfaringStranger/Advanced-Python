# Use curly braces or the built-in set function.
my_set = {"apple", "banana", "cherry"}
print(my_set)

# or use the set function and create from an iterable, e.g. list, tuple, string
my_set_2 = set(["one", "two", "three"])
my_set_2 = set(("one", "two", "three"))
print(my_set_2)

my_set_3 = set("aaabbbcccdddeeeeeffff")
print(my_set_3)

# careful: an empty set cannot be created with {}, as this is interpreted as dict
# use set() instead
a = {}
print(type(a))
a = set()
print(type(a))
