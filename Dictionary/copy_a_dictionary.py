dict_org = {"name":"Max", "age":28, "city":"New York"}

# this just copies the reference to the dict, so be careful
dict_copy = dict_org

# now modifying the copy also affects the original
dict_copy["name"] = "Lisa"
print(dict_copy)
print(dict_org)

# use copy(), or dict(x) to actually copy the dict
dict_org = {"name":"Max", "age":28, "city":"New York"}

dict_copy = dict_org.copy()
# dict_copy = dict(dict_org)

# now modifying the copy does not affect the original
dict_copy["name"] = "Lisa"
print(dict_copy)
print(dict_org)
