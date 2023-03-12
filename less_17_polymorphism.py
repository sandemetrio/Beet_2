"""Task 1 Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, and make their
own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be
to print ‘meow’. Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and
performs talk method on input parameter.  """

from abc import ABC, abstractmethod
from pprint import pprint


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def talk(self):
        raise NotImplementedError('Must be implemented by subclass')


class Dog(Animal):
    def talk(self):
        print('Bark')


class Cat(Animal):
    def talk(self):
        print('Meow')


"""Task 2 Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

Library class

Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list
for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books

"""


class Author:
    def __init__(self,
                 name: str,
                 country: str,
                 birthday: int,
                 books: list
                 ):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f'class object {self.__class__.__name__}, name : {self.name},' \
               f' date of birth {self.birthday}, country : {self.country},' \
               f' list of books: {self.books} '

    def __repr__(self):
        return f'class object {self.__class__.__name__}, name : {self.name},' \
               f' date of birth {self.birthday}, country : {self.country},' \
               f' list of books: {self.books[:2]} and others'


class Book:
    counter = 0

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        cls.counter += 1
        return obj

    def __init__(self,
                 name: str,
                 year: int,
                 author: Author):
        self.name = name
        self.year = year
        self.author = author
        self.id = Book.counter

    def __str__(self):
        return f' class: {self.__class__.__name__}, name : {self.name},' \
               f' year of publishing {self.year}, author : {self.author.name}, id: {self.id}'

    def __repr__(self):
        return f' class: {self.__class__.__name__}, name: {self.name},' \
               f' year of publishing: {self.year}, author: {self.author.name}, id: {self.id}'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def add_new_book(self, book_name: str, year: int, author: Author):
        for book in self.books:
            if book_name == book.name:
                return 'This book is already added'

        new_book = Book(book_name, year, author)
        self.books.append(new_book)
        if author not in self.authors:
            self.authors.append(author)
        return new_book

    def group_by_author(self, author: Author):
        res = []
        for book in self.books:
            if book.author == author:
                res.append(book)
        return res

    def group_by_year(self, year: int):
        res = []
        for book in self.books:
            if book.year == year:
                res.append(book)
        return res


"""Task 3 Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною 
перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння між
об'єктами класу Fraction"""


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0:
            raise ZeroDivisionError

    def __add__(self, other):
        if self.denominator == other.denominator:
            return print(f'{self.numerator + other.numerator}\n'
                         f'{"_" * 3}\n'
                         f'{self.denominator}')

        return print(f'{self.numerator * other.denominator + other.numerator * self.denominator}\n'
                     f'{"_" * 3}\n'
                     f'{self.denominator * other.denominator}')

    def __sub__(self, other):
        if self.denominator == other.denominator:
            return print(f'{self.numerator - other.numerator}\n'
                         f'{"_" * 3}\n'
                         f'{self.denominator}')
        return print(f'{self.numerator * other.denominator - other.numerator * self.denominator}\n'
                     f'{"_" * 3}\n'
                     f'{self.denominator * other.denominator}')

    def __mul__(self, other):

        return print(f'{self.numerator * other.numerator}\n'
                     f'{"_" * 3}\n'
                     f'{self.denominator * other.denominator}')

    def __truediv__(self, other):
        return print(f'{self.numerator * other.denominator}\n'
                     f'{"_" * 3}\n'
                     f'{self.denominator * other.numerator}')

    def __le__(self, other):
        if self.denominator == other.denominator:
            if self.numerator <= other.numerator:
                return True
            else:
                return False
        else:
            if self.numerator * other.denominator <= other.numerator * self.denominator:
                return True
            else:
                return False

    def __lt__(self, other):
        if self.denominator == other.denominator:
            if self.numerator < other.numerator:
                return True
            else:
                return False
        else:
            if self.numerator * other.denominator < other.numerator * self.denominator:
                return True
            else:
                return False

    def __eq__(self, other):
        if self.denominator == other.denominator:
            if self.numerator == other.numerator:
                return True
            else:
                return False
        else:
            if self.numerator * other.denominator == other.numerator * self.denominator:
                return True
            else:
                return False

    def __ne__(self, other):
        if self.denominator == other.denominator:
            if self.numerator != other.numerator:
                return True
            else:
                return False
        else:
            if self.numerator * other.denominator != other.numerator * self.denominator:
                return True
            else:
                return False

    def __gt__(self, other):
        if self.denominator == other.denominator:
            if self.numerator > other.numerator:
                return True
            else:
                return False
        else:
            if self.numerator * other.denominator > other.numerator * self.denominator:
                return True
            else:
                return False

    def __ge__(self, other):
        if self.denominator == other.denominator:
            if self.numerator >= other.numerator:
                return True
            else:
                return False
        else:
            if self.numerator * other.denominator >= other.numerator * self.denominator:
                return True
            else:
                return False


def main():
    # rowling = Author("Rowling Joanne", 'United Kingdom', 1965, [
    #     "Harry Potter and the Philosopher's Stone",
    #     "Harry Potter and the Chamber of Secrets",
    #     "Harry Potter and the Prisoner of Azkaban",
    #     "Harry Potter and the Goblet of Fire",
    #     "Harry Potter and the Order of the Phoenix",
    #     "Harry Potter and the Half-Blood Prince",
    #     "Harry Potter and the Deathly Hallows",
    # ])
    # keyes = Author("Keyes Daniel", "USA", 1927, [
    #     "Flowers for Algernon",
    #     "The Touch",
    #     "The Minds of Billy Milligan"
    # ])
    #
    king = Author("King Stephen", "USA", 1947, [
        "Carrie",
        "It",
        "The Green Mile"
        "The Stand"
    ])
    # lib = Library('Vernadskogo')
    #
    # test = Book("Harry Potter and the Philosopher's Stone", 1997, rowling)
    # lib.books.append(test)
    #
    # lib.add_new_book("Harry Potter and the Chamber of Secrets", 1998, rowling)
    #
    # lib.add_new_book("Harry Potter and the Prisoner of Azkaban", 1999, rowling)
    # lib.add_new_book("Harry Potter and the Goblet of Fire", 2000, rowling)
    # lib.add_new_book("Flowers for Algernon", 1966, keyes)
    # lib.add_new_book("The Touch", 1968, keyes)
    # lib.add_new_book("The Minds of Billy Milligan", 2000, keyes)
    #
    # lib.add_new_book("Carrie", 1974, king)
    # lib.add_new_book("It", 1986, king)
    # lib.add_new_book("The Green Mile", 1996, king)
    # lib.add_new_book("The Stand", 2000, king)
    # # pprint(lib.books)
    # # pprint(lib.authors)
    # # pprint(lib.group_by_author(rowling))
    # pprint(lib.group_by_year(2000))

    # x = Fraction(5, 4)
    # y = Fraction(2, 6)
    # x * y


if __name__ == '__main__':
    main()
