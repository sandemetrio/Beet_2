from pprint import pprint

"""Task 1 School

Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
 and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes
 , and keep in mind which are common and which are not. For example, the name should be a Person attribute, while salary
  should only be available to the teacher. """


class Person:
    def __init__(self,
                 name: str,
                 lastname: str,
                 age: int,
                 occupation: str):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.occupation = occupation

    def __repr__(self):
        return f'Hello my  name is {self.name} {self.lastname}, I"am {self.age} years old, and ' \
               f'my occupation is {self.occupation}'

    def go_to_school(self):
        print('I go to school 5 day a week')

    def prepare_for_lessons(self):
        pass

    def activities_during_break(self):
        pass

    def getting_reward(self):
        pass


class Student(Person):
    def __init__(self, name, lastname, age, grade, hobby, occupation='study'):
        super().__init__(name, lastname, age, occupation)
        self.grade = grade
        self.hobby = hobby

    def get_nick_name(self, nick):
        return f'{self.name} {nick} {self.lastname}'

    def prepare_for_lessons(self):
        print(f'I do my homework and than go play {self.hobby}')

    def activities_during_break(self):
        print('*playing with friends')

    def getting_reward(self):
        print(f' If study hard i will get good marks')


class Teacher(Person):
    def __init__(self,
                 name,
                 lastname,
                 age,
                 salary=20000,
                 occupation='teach'):
        super().__init__(name, lastname, age, occupation)
        self.salary = salary

    def prepare_for_lessons(self):
        print('I must check oll this homework')

    def activities_during_break(self):
        print('*have a cup of coffee')

    def getting_reward(self):
        print(f'Give me my {self.salary}')


"""Task 2 Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'"""


class Mathematician:
    def square_nums(self, list_: list):
        return [i ** 2 for i in list_]

    def remove_positives(self, list_: list):
        return [i for i in list_ if i <= 0]

    def filter_leaps(self, list_: list):
        return [i for i in list_ if i % 4 == 0 and not i % 100 == 0 or i % 400 == 0]


"""Task 3 Product Store

Write a class Product that has three attributes:
type, name, price
Then create a class ProductStore, which will have some Products and will operate with all products in the store. All 
methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional

 classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your 
store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input
identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other 
case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of prods in the store."""


class Product:
    def __init__(self, type_: str, name: str, price):
        self.type = type_
        self.name = name
        self.price = price


class ProductStore:
    STORE = []
    INCOME = 0

    def __init__(self, store_name: str):
        self.store_name = store_name
        self.product = Product

    def set_product(self, product: Product, amount: int):
        prod = {
            "type": product.type,
            "name": product.name,
            "price": round(product.price * 1.3, 2),
            "amount": amount,
            "discount": 0
        }
        self.STORE.append(prod)

    def get_product(self, identifier: str, identifier_type='name'):
        for item in self.STORE:
            if item[identifier_type] == identifier:
                return item
        print(f'No products such as {identifier} yet')
        return False

    def add(self, product: Product, amount: int):
        if prod := self.get_product(product.name):
            prod['amount'] += amount
            print(f'{amount} {product.name} added, total amount: {prod["amount"]}')
        else:
            self.set_product(product, amount)
            print(f'New product {product.name} added, total amount: {amount}')

    def set_discount(self, identifier, percent, identifier_type='name'):
        if prod := self.get_product(identifier, identifier_type):
            prod['discount'] = percent
            print(f'{percent}% discount set to {prod["name"]}, now it"s only {prod["price"]}')

    def sell_products(self, product_name, amount):
        if prod := self.get_product(product_name):
            if prod['amount'] >= amount:
                prod['amount'] -= amount
                self.INCOME = round(prod['price'] * (100 - prod['discount']) / 100 * amount, 2)
                return True
            else:
                print(f'Only {prod["amount"]} {prod["name"]} left')
                return False

    def get_income(self):
        return self.INCOME

    def get_all_products(self):
        pprint(self.STORE)

"""Custom exception

Create your custom exception named `CustomException`, you can inherit from base Exception class,
but extend its functionality to log every error message to a file named `logs.txt`. Tips: Use __init__ 
method to extend functionality for saving messages to file

class CustomException(Exception):

:"""


class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open('logs.txt', "w") as file:
            file.write(msg)





def main():
    student_1 = Student('Ivan', 'Ivanenko', 19, 11, 'Football')
    teacher_1 = Teacher('Petro', 'Petrenko', 48)

    # print(student_1)
    # print(teacher_1)
    # m = Mathematician()
    #
    # assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
    #
    # assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    #
    # assert m.filter_leaps([2001, 1884, 1995, 2003, 2020, 1700, 1800, 1900, 2100, 2200, 2300, 400]) == [1884, 2020, 400]

    # silpo = ProductStore('Сільпо')
    #
    # # silpo.add(Product('Diary', 'Milk', 32.49), 20)
    # silpo.add(Product('Bread', 'Lavash', 20.34), 10)
    # silpo.add(Product('Bread', 'Toast', 15.59), 50)
    # silpo.add(Product('Diary', 'Yogurt', 34.54), 20)
    # silpo.add(Product('Diary', 'Yogurt', 34.54), 20)
    # silpo.add(Product('Diary', 'Ayran', 54.40), 5)
    # silpo.add(Product('Diary', 'Ayran', 54.40), 5)
    # # print(silpo.STORE)
    # silpo.set_discount('Lavash', 30)
    #
    # silpo.sell_products('Toast', 10)
    # silpo.sell_products('Toast', 40)
    # silpo.sell_products('Toast', 1)
    #
    # print(silpo.get_income())
    # silpo.get_all_products()
    # silpo.get_product_info('Yogurt')
    raise CustomException('do smth here')


if __name__ == '__main__':
    main()
