"""Task 1 A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as
attributes. Make another method called talk() which makes prints a greeting from the person containing, for example like
 this: “Hello, my name is Carl Johnson and I’m 26 years old”."""


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        return f'Hello, my name is {self.firstname} {self.lastname} I"m {self.age} years old'


"""Task 2 Doggy age

Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age. 
Then create a method `human_age` which returns the dog’s age in human equivalent."""


class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return f' if this dog was a human, it would be {self.dog_age * self.age_factor} years old'


"""Task 3

TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' 
    exists in the list, or "No" - in the other case.
 

The default channel turned on before all commands is №1."""


class TVController:
    lIST_OF_CHANNELS = ['BBC', 'National geographic', 'TV1000', 'Discovery', 'FOX', 'Cartoon Network']
    INDEX = 0

    # CURRENT = lIST_OF_CHANNELS[INDEX]

    def current(self):
        result = self.lIST_OF_CHANNELS[self.INDEX]
        return result

    def first_channel(self):
        self.INDEX = 0
        return self.current()

    def last_channel(self):
        self.INDEX = len(self.lIST_OF_CHANNELS) - 1
        return self.current()

    def turn_channel(self, num: int):
        if num in range(1, len(self.lIST_OF_CHANNELS) + 1):
            self.INDEX = num - 1
            return self.current()
        else:
            return f'No such channel as: {num}'

    def next_channel(self):
        try:
            self.INDEX += 1
            return self.current()
        except IndexError:
            return self.first_channel()

    def previous_channel(self):
        try:
            self.INDEX -= 1
            return self.current()
        except IndexError:
            return self.last_channel()

    def is_exist(self, arg):
        if isinstance(arg, int):
            if arg in range(1, len(self.lIST_OF_CHANNELS) + 1):
                return "Yes"
            else:
                return "No"

        elif isinstance(arg, str):
            if arg in self.lIST_OF_CHANNELS:
                return "Yes"
            else:
                return "No"

        else:
            return "No"


def main():
    # guy = Person('Ivan', 'Ivanenko', 30)
    # print(guy.talk())
    #
    # flafy = Dog(7)
    # print(flafy.human_age())

    controller = TVController()
    # print(controller.first_channel())
    # print(controller.previous_channel())
    # print(controller.previous_channel())
    # print(controller.previous_channel())
    # print(controller.previous_channel())
    # print(controller.previous_channel())
    # print(controller.previous_channel())
    # print(controller.previous_channel())


if __name__ == '__main__':
    main()
