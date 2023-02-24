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


def main():

    student_1 = Student('Ivan', 'Ivanenko', 19, 11, 'Football')
    teacher_1 = Teacher('Petro', 'Petrenko', 48)

    print(student_1)
    print(teacher_1)


if __name__ == '__main__':
    main()
