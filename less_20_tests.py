'''Task 1

Pick your solution to one of the exercises in this module.
Design tests for this solution and write tests using unittest library. '''

import unittest

from less_17_polymorphism import Author, Book, Library


class BookClassTest(unittest.TestCase):
    def setUp(self):
        self.author = Author('name', 'country', 0, [])
        self.book = Book('name', 0, self.author)

    def test_class_counter(self):
        self.assertEqual(Book.counter, 1)
        book_2 = Book('name', 0, self.author)
        book_3 = Book('name', 0, self.author)
        self.assertEqual(Book.counter, 3)


class LibraryClassTest(unittest.TestCase):
    def setUp(self):
        self.author = Author('name', 'country', 0, ['author_book_1', 'author_book_2', 'author_book_3'])
        self.author_2 = Author('name', 'country', 0, ['author_2_book_1', 'author_2_book_2', 'author_2_book_3'])
        self.book = Book('name', 0, self.author)
        self.library = Library('name')

    def test_add_new_book(self):
        self.assertEqual(self.library.books, [])

        book = self.library.add_new_book('name', 0, self.author)
        self.assertEqual(self.library.books[0], book)

        book_2 = self.library.add_new_book('name', 0, self.author)
        self.assertEqual(book_2, 'This book is already added')

        self.assertEqual(self.library.authors[0], self.author)

        self.assertEqual(len(self.library.books), 1)

    def test_group_by_author(self):
        self.library.add_new_book('name', 0, self.author)
        self.library.add_new_book('name2', 0, self.author_2)
        res_1 = self.library.group_by_author(self.author)
        res_2 = self.library.group_by_author(self.author_2)
        self.assertEqual(res_1, [self.library.books[0]])
        self.assertEqual(res_2, [self.library.books[1]])

    def test_group_by_year(self):
        self.library.add_new_book('name', 1, self.author)
        self.library.add_new_book('name2', 2, self.author_2)
        res_1 = self.library.group_by_year(1)
        res_2 = self.library.group_by_year(2)
        self.assertEqual(res_1, [self.library.books[0]])
        self.assertEqual(res_2, [self.library.books[1]])


unittest.main()
