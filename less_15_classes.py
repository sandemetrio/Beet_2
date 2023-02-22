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


class TVcontroler:
    list_of_channels = ['BBC', 'National geographic', 'TV1000', 'Discovery', 'FOX', 'Cartoon Network']
    def __init__(self):
        self.cannel

    def first_chanel(self):



def main():
    # guy = Person('Ivan', 'Ivanenko', 30)
    # print(guy.talk())
    #
    # flafy = Dog(7)
    # print(flafy.human_age())


if __name__ == '__main__':
    main()
