# remove(x): removes x, raises a KeyError if element is not present
my_set = {"apple", "banana", "cherry"}
my_set.remove("apple")
print(my_set)

# KeyError:
# my_set.remove("orange")

# discard(x): removes x, does nothing if element is not present
my_set.discard("cherry")
my_set.discard("blueberry")
print(my_set)

# clear() : remove all elements
my_set.clear()
print(my_set)

# pop() : return and remove a random element
a = {True, 2, False, "hi", "hello"}
print(a.pop())
print(a)
