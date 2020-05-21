my_dict = {"name":"Max", "age":28, "city":"New York"}
# use if .. in ..
if "name" in my_dict:
    print(my_dict["name"])

# use try except
try:
    print(my_dict["firstname"])
except KeyError:
    print("No key found")
