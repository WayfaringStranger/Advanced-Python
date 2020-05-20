tuple_1 = ("Sakshi", 21, "India")
name, age, city = tuple_1
print(name)
print(age)
print(city)

# tip: unpack multiple elements to a list with *
my_tuple = (0, 1, 2, 3, 4, 5)
item_first, *items_between, item_last = my_tuple
print(item_first)
print(items_between)
print(item_last)
