''' Make an iterator that returns consecutive keys and groups from the iterable. The key is a function computing a key value for each element. If not specified or is None, key defaults to an identity function and returns the element unchanged. Generally, the iterable needs to already be sorted on the same key function. '''

from itertools import groupby

# use a function as key
def smaller_than_3(x):
    return x < 3

group_obj = groupby([1, 2, 3, 4], key=smaller_than_3)
for key, group in group_obj:
    print(key, list(group))

# or use a lamda expression, e.g. words with an 'i':
group_obj = groupby(["hi", "nice", "hello", "cool"], key=lambda x: "i" in x)
for key, group in group_obj:
    print(key, list(group))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

for key, group in groupby(persons, key=lambda x: x['age']):
    print(key, list(group))
