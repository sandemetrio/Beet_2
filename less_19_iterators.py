'''Task 1

Create your own implementation of a built-in function enumerate, named `with_index`, which
takes two parameters: `iterable` and `start`, default is 0. Tips: see the documentation for the
enumerate function'''


def with_index(iterable, start=10):
    for element in iterable:
        yield start, element
        start += 1


for i in with_index(range(5)):
    print(i)