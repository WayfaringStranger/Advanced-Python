from itertools import count, cycle, repeat
# count(x): count from x: x, x+1, x+2, x+3...
for i in count(10):
    print(i)
    if  i >= 13:
        break

# cycle(iterable) : cycle infinitely through an iterable
print("")
sum = 0
for i in cycle([1, 2, 3]):
    print(i)
    sum += i
    if sum >= 12:
        break

# repeat(x): repeat x infinitely or n times
print("")
for i in repeat("A", 3):
    print(i)
