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

    @property
    def get_to_work(self):
        return self.boss.workers

    @get_to_work.setter
    def get_to_work(self, worker):
        self.boss.workers.append(worker)




def main():
    user_1 = EMail("test.first@analytics.com")

    boss = Boss(1, 'Bill', 'Microsoft')
    # print(boss.get_to_work)
    boss.get_to_work = Worker(112, 'Kelvin', 'Microsoft', boss)
    print(boss.get_to_work)


if __name__ == '__main__':
    main()
