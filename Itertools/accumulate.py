''' Make an iterator that returns accumulated sums, or accumulated results of other binary functions. '''

from itertools import accumulate

# return accumulated sums
acc = accumulate([1,2,3,4])
print(list(acc))

# other possible functions are possible
import operator
acc = accumulate([1,2,3,4], func=operator.mul)
print(list(acc))

acc = accumulate([1,5,2,6,3,4], func=max)
print(list(acc))
