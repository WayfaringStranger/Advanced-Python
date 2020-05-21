my_dict = {"name": "Supriya", "age": 19, "city": "Ghazipur", "email": "supriya@gmail.com"}

# delete a key-value pair
del my_dict["email"]

# this returns the value and removes the key-value pair
print("popped value:", my_dict.pop("age"))

# return and removes the last inserted key-value pair
# (in versions before Python 3.7 it removes an arbitrary pair)
print("popped item:", my_dict.popitem())

print(my_dict)

# clear() : remove all pairs
# my_dict.clear()
