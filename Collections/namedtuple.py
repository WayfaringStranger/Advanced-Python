''' namedtuples are easy to create, lightweight object types. They assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index. '''

from collections import namedtuple
# create a namedtuple with its class name as string and its fields as string
# fields have to be separated by comma or space in the given string
Point = namedtuple('Point','x, y')
pt = Point(1, -4)
print(pt)
print(pt._fields)
print(type(pt))
print(pt.x, pt.y)

Person = namedtuple('Person','name, age')
friend = Person(name='Tom', age=25)
print(friend.name, friend.age)
