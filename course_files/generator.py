def week():
    days_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days_week:
        yield day


days = week()
print(next(days)) # 'Monday'
print(next(days)) # 'Tuesday'
print(next(days)) # 'Wednesday'
print(next(days)) # 'Thursday'
print(next(days)) # 'Friday'
print(next(days)) # 'Saturday'
print(next(days)) # 'Sunday'
# print(next(days)) # StopIteration


def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"


gen = yes_or_no()
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
print(next(gen)) # 'yes'
print(next(gen)) # 'no'


def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1


counter = current_beat()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))



'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''


def make_song(count=99, beverage="soda"):
    for i in range(count, -1, -1):
        if i == 1:
            yield "Only 1 bottle of " + beverage + " left!"
        elif i == 0:
            yield "No more " + beverage + "!"
        else:
            yield str(i) + " bottles of " + beverage + " on the wall."



kombucha_song = make_song(5, "kombucha")
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))

default_song = make_song()
print(next(default_song))


print("-------------------------")


def get_multiples(number=1, count=10):
    next_num = number
    while count > 0:
        yield next_num
        count -= 1
        next_num += number


evens = get_multiples(2, 3)
print(next(evens)) # 2
print(next(evens)) # 4
print(next(evens)) # 6
# print(next(evens)) # StopIteration

default_multiples = get_multiples()
print(list(default_multiples)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print("-------------------------")


def get_unlimited_multiples(number=1):
    next_number = number
    while True:
        yield next_number
        next_number += number


sevens = get_unlimited_multiples(7)
print([next(sevens) for i in range(15)])
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
print([next(ones) for i in range(20)])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def nums():
    for num in range(1, 10):
        yield num


g = nums()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

g1 = (num for num in range(1, 10))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))


