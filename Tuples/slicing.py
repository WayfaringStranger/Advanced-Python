# a[start:stop:step], default step is 1
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
b = a[::2] # start to end with every second item
print(b)
b = a[::-1] # reverse tuple
print(b)
