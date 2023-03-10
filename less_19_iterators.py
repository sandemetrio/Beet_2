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

"""Task 2

Create your own implementation of a built-in function range, named in_range(), which takes
three parameters: `start`, `end`, and optional step. Tips: See the documentation for `range`
function"""


def in_range(start, end, step=1):
    if start <= end and step >= 0:
        while start < end:
            yield start
            start += step
    elif start > end and step <= 0:
        while start > end:
            yield start
            start += step
    else:
        return None


"""Task 3

Create your own implementation of an iterable, which could be used inside for-in loop. Also,
add logic for retrieving elements using square brackets syntax."""


class Itertest():
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        for el in self.data:
            return el

    def __getitem__(self, key):
        return self.data[key]


















class MyIternacci:
    def __init__(self, num, start_1=0, start_2=1):
        if num < 1:
            raise ValueError("the length of the sequence must be greater than 0")
        self.num = num
        self.start_1 = start_1
        self.start_2 = start_2
        self.counter = 0
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num == self.counter:
            raise StopIteration
        if self.num == 1:
            return 0
        elif self.num == 2:
            return 1

        self.counter += 1

        self.value = self.start_1 + self.start_2
        self.start_1 = self.start_2
        self.start_2 = self.value
        return self.value



fib = MyIternacci(5)

for i in fib:
    print(i)