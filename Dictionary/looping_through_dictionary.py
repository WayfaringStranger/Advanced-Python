my_dict = {"name":"Max", "age":28, "city":"New York"}

# loop over keys
for key in my_dict:
    print(key, my_dict[key])

# loop over keys
for key in my_dict.keys():
    print(key)

# loop over values
for value in my_dict.values():
    print(value)

# loop over keys and values
for key, value in my_dict.items():
    print(key, value)
