'''Task 1

Create your own implementation of a built-in function enumerate, named `with_index`, which
takes two parameters: `iterable` and `start`, default is 0. Tips: see the documentation for the
enumerate function'''

import itertools


def with_index_1(iterable, start=10):
    for element in iterable:
        yield start, element
        start += 1


def with_index_2(iterable, start=0):
    return zip(itertools.count(start=start), iterable)
#
# for i in with_index_1(range(5)):
#     print(i)


# for i in with_index_2(range(5)):
#     print(i)
