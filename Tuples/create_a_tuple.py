tuple_1 = ("Max", 28, "New York")
tuple_2 = "Linda", 25, "Miami" # Parentheses are optional

# Special case: a tuple with only one element needs to have a comma at the end, 
# otherwise it is not recognized as tuple
tuple_3 = (25,)
print(tuple_1)
print(tuple_2)
print(tuple_3)

# Or convert an iterable (list, dict, string) with the built-in tuple function
tuple_4 = tuple([1,2,3])
print(tuple_4)
