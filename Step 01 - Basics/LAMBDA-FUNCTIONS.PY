from typing import List, Tuple, Optional, Callable
from collections import defaultdict, OrderedDict, deque

# lambda format
# lambda input : expression
x = lambda x: x ** 2
print(x(9))

x = lambda x, y: x + y
print(x(2, 3))

x = lambda x: "even" if x % 2 == 0 else "odd"
print(x(3))
print(x(2))

# higer order functions -> functions which need some parameters as well as another function as its parameter
# example -> print the sum of even, odd and elements div by 3 from the following List

list1 = [11, 14, 21, 23, 56, 78, 45, 29, 28]
xx = lambda x: x % 2 == 0  # even
xy = lambda x: x % 2 != 0  # odd
xz = lambda x: x % 3 == 0  # divisible by 3


def eg_of_hof(fun: Callable, vec: List):
    res = 0
    for item in vec:
        if fun(item):
            res += item
    return res


print(eg_of_hof(xx, list1))
print(eg_of_hof(xy, list1))
print(eg_of_hof(xz, list1))

# map reduce and filter

# map -> format = map(function, iterable)
list2 = [2, 4, 5, 1, 4]
list2 = list(map(lambda x: x * 2, list2))
print(list2)

# Example : suppose we have some data from database and we want to fetch only names from these data -> then we can do this using map
Student = [
    {
        'name': 'dhruv',
        'age': 20
    },
    {
        'name': 'atharva',
        'age': 21
    },
    {
        'name': 'chiku',
        'age': 34
    }
]
print(Student)

names = list(map(lambda studentData: studentData['name'], Student))
print(names)

# filter -> format  = filter (function, iterable)
list3 = [1, 2, 3, 4, 5, 6, 7]
temp = list(filter(lambda x: x > 4, list3))
print(temp)

# reduce -> format = functools.reduce(function, iterable)
import functools

list4 = [1, 2, 3, 4, 5]

# greatest element
print(functools.reduce(lambda x, y: x if x > y else y, list4))

# smallest element
print(functools.reduce(lambda x, y: x if x < y else y, list4))

# sum of all elements
print(functools.reduce(lambda x, y: x + y, list4))

# list comprehension
list5 = [1, 2, 3, 4, 5]
list6 = [i * 2 for i in list5]
print(list6)

list7 = [i for i in list5 if i % 2 == 0]
print(list7)

# similarly dictionary comprehension can be done
