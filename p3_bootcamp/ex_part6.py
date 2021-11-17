# Ex. 133


def letter_counter(string):
    my_str = string.lower()
    def inner(num):
        nonlocal my_str
        return my_str.count(num.lower())
    return inner


counter = letter_counter('Amazing')
print(counter('a')) # 2
print(counter('m')) # 1

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i')) # 2
print(counter2('t')) # 1

print("----------------------")

# Ex. 134


def once(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        if count > 0:
            return None
        else:
            count += 1
            return fn(*args, **kwargs)
    return inner


def add(a,b):
    return a+b


oneAddition = once(add)

print(oneAddition(2,2)) # 4
print(oneAddition(2,2)) # None
print(oneAddition(12,200)) # None

print("----------------------")

# Ex. 135


def next_prime():
    number = 2
    all_primes = set()
    while True:
        for prime in all_primes:
            if number % prime == 0:
                break
        else:
            all_primes.add(number)
            yield number
        number += number % 2 + 1


primes = next_prime()
print([next(primes) for i in range(25)])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


