class Class1:
    x = 10

    def func(self):
        print("Method func from Class1")


class Class2(Class1):
    def func(self):
        print("Method func from Class2")


class Class3(Class2):
    def func(self):
        print("Method func from Class3")


class Class4(Class3):
    pass


class Class5(Class2):
    def func(self):
        print("Method func from Class5")


class Class6(Class5):
    def func(self):
        print("Method func from Class6")


class Class7(Class4, Class6):
    pass


c = Class7()
print(c.x)
c.func()


class A:
    def hi(self):
        print("A")


class B(A):
    def hi(self):
        print("B")


class C(A):
    def hi(self):
        print("C")


class D(B, C):
    pass


d = D()
d.hi()

