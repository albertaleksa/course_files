class Person:

    def __init__(self, name):
        print("Constructor")
        self.name = name
        self.__age = 20

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

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 0 < value < 101:
            self.__age = value
        else:
            print("Wrong age")
