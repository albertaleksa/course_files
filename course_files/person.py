class Person:

    # constructor
    def __init__(self, name, age):
        print("Constructor")
        self.name = name
        self.__age = age

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.__age}")

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, value):
    #     if 0 < value < 101:
    #         self.__age = value
    #     else:
    #         print("Wrong age")

    # getter
    @property
    def age(self):
        return self.__age

    # setter
    @age.setter
    def age(self, value):
        if 0 < value < 101:
            self.__age = value
        else:
            print("Wrong age")


class Employee(Person):

    company = 'Google'

    def more_info(self):
        print(f"Name: {self.name} works in {self.company}")
