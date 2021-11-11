import math

print(math.e)
print(math.pow(2, 4))

result = math.e != math.pow(2, 4)
print(int(result))

print('Mike' > "Mikey")

x = '\''
print(len(x))



cash = 19867324678987.99  # DON'T CHANGE THE CASH VARIABLE

# ADD YOUR CODE BELOW:
print(cash/5)
res = round(cash/5, 2)
print(cash, "  ", res)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# use the person variable in your answer
answer = {k: v for (k, v) in person}
print(answer)


def speak(animal="dog"):
    return {
        "pig": "oink",
        "duck": "quack",
        "cat": "meow",
        "dog": "woof"
    }.get(animal, "?")


print(speak())

'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''


# flesh out multiple_letter count:
def multiple_letter_count(string):
    return {k: string.count(k) for k in string}


print(multiple_letter_count("awesome"))


def intersection(lst1, lst2):
    return [el for el in lst1 if el in lst2]


print(intersection([1, 2, 3], [2, 3, 4]))

print("----------------")


def isEven(num):
    return num % 2 == 0


'''
partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''


def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]
        # list(filter(fn, lst)), list(map(fn, lst))


print(partition([1,2,3,4], isEven))


# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1, 4, 7)
print(result1)
result2 = count_sevens(*nums)
print(result2)


print("----------------")


'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''


def calculate(**kwargs):
    result = "The result is"
    res = 0
    make_float = kwargs.get('make_float')
    operation = kwargs.get('operation')
    message = kwargs.get('message')
    if message:
        result = message
    first = kwargs.get('first')
    second = kwargs.get('second')

    if operation == "add":
        res = float(first) + float(second)
    elif operation == "subtract":
        res = float(first) - float(second)
    elif operation == "multiply":
        res = float(first) * float(second)
    elif operation == "divide":
        res = float(first) / float(second)

    if not make_float:
        res = int(res)

    return result + " " + str(res)


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
