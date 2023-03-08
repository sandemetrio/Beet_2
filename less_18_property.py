"""Task 1

Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a
valid email string."""
import re


class EMail:
    def __init__(self, email):
        self.email = self.validate(email)

    @classmethod
    def validate(cls, mail):
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', mail):
            return mail
        else:
            raise ValueError('Not valid email')


"""Task 2

Implement 2 classes, the first one is the Boss and the second one is the Worker.

Worker has a property 'boss', and its value must be an instance of Boss.

You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers.
You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances of Boss
class to workers list directly via access to attribute, use getters and setters instead!"""


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def __str__(self):
        return f' ID: {self.id}\n NAME: {self.name}\n COMPANY: {self.company}\n'

    def __repr__(self):
        return f' ID: {self.id}\n NAME: {self.name}\n COMPANY: {self.company}\n'

    @property
    def get_to_work(self):
        return self.boss.workers

    @get_to_work.setter
    def get_to_work(self, worker):
        self.boss.workers.append(worker)


'''Task 3

Write a class TypeDecorators which has several methods for converting results of functions
to a specified type(if it's possible):
methods:

to_int
to_str
to_bool
to_float

Don't forget to use @wraps




'''


class TypeDecorators:
    @staticmethod
    def to_int(function):
        def wrapper(value):
            try:
                return int(value)
            except ValueError:
                print(f'Cant convert it to integer: "{value}"')

        return wrapper

    @staticmethod
    def to_str(function):
        def wrapper(value):
            try:
                return str(value)
            except ValueError:
                print(f'Cant convert it to string: "{value}"')

        return wrapper

    @staticmethod
    def to_bool(function):
        def wrapper(value):
            try:
                return bool(value)
            except ValueError:
                print(f'Cant convert it to bool: "{value}"')

        return wrapper

    @staticmethod
    def to_float(function):
        def wrapper(value):
            try:
                return float(value)
            except ValueError:
                print(f'Cant convert it to float: "{value}"')
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


def main():
    user_1 = EMail("test.first@analytics.com")
    #
    # boss = Boss(1, 'Bill', 'Microsoft')
    # worker = Worker(112, 'Kelvin', 'Microsoft', boss)
    # # boss.get_to_work = Worker(118, 'Gelvin', 'Microsoft', boss)
    # # print(boss.get_to_work)
    # worker.get_to_work = Worker(122, 'Melvin', 'Microsoft', boss)
    # worker.get_to_work = Worker(118, 'Gelvin', 'Microsoft', boss)
    # print((worker.get_to_work))
    assert do_nothing('25') == 25

    assert do_something('True') is True


if __name__ == '__main__':
    main()
