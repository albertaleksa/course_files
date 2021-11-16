from functools import wraps
from time import sleep


def hello ():
    return "Func hello"


test = hello
print(test())


def super_func(func):
    print("Func super_func")
    print(func())


super_func(hello)

print("----------------------")


def my_decorator(func):
    def func_wrapper():
        print("Code before")
        func()
        print("Code after")
    return func_wrapper


def func_test():
    print("Func func_test")


test2 = my_decorator(func_test)
test2()

print("----------------------")


# the same like previous but using @decorator
@my_decorator
def func_test2():
    print("Func func_test")


func_test2()

print("----------------------")


def make_title(fn):
    def wrapped():
        title = fn()
        title = title.capitalize()
        title = title.replace(',', '')
        return title
    return wrapped


@make_title
def hi():
    return "hello, world"


print(hi())

print("----------------------")


def my_decorator(fn):
    def wrapper(*args, **kwargs):
        # do some stuff with fn(*args, **kwargs)
        pass
    return wrapper


def shout(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    """Greeting function"""
    return f"Hi, I'm {name}"


@shout
def lol():
    return "lol"


print(greet("Jack"))
print(lol())

print(greet.__doc__)
print(greet.__name__)
help(greet)

print("----------------------")


def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines):
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}

print("----------------------")


def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return [fn(*args, **kwargs), fn(*args, **kwargs)]
    return wrapper


@double_return
def add(x, y):
    return x + y


print(add(1, 2)) # [3, 3]


@double_return
def greet(name):
    return "Hi, I'm " + name


print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"]

print("----------------------")


def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            return "Too many arguments!"
        return fn(*args, **kwargs)
    return wrapper


@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)


print(add_all()) # 0
print(add_all(1)) # 1
print(add_all(1,2)) # 3
print(add_all(1,2,3)) # "Too many arguments!"
print(add_all(1,2,3,4,5,6)) # "Too many arguments!"


print("----------------------")


def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) != int:
                return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return wrapper


@only_ints
def add(x, y):
    return x + y


print(add(1, 2))  # 3
print(add("1", "2"))  # "Please only invoke with integers."

print("----------------------")


def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

print(show_secrets(role="admin")) # "Shh! Don't tell anybody!"
print(show_secrets(role="nobody")) # "Unauthorized"
print(show_secrets(a="b")) # "Unauthorized"

print("----------------------")


def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg is not {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is("tako")
def fav_foods(*foods):
    return foods


@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2


print(fav_foods("tako", "burrito"))
print(fav_foods("ice cream", "tako"))
print(add_to_ten(10, 12))
print(add_to_ten(1, 2))

print("----------------------")


def delay(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"Waiting {val}s before running {fn.__name__}")
            sleep(val)
            return fn(*args, **kwargs)
        return wrapper
    return inner



@delay(3)
def say_hi():
    return "hi"

print(say_hi())
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"


