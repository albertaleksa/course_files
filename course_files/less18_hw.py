import math

# print("Exercise 1")
# lst_1 = input("Input list separated by space: ").split()
# print([int(i) * 2 for i in lst_1])

# print("Exercise 2")
# lst_2 = input("Input list separated by space: ").split()
# print(sum(int(i) ** 2 for i in lst_2))


def litres_count(hours):
    print(f"time1 = {hours} --> litres = {int(hours * 0.5)}")


print("Exercise 3.1")
user_hours = float(input("Input count of hours: "))
litres_count(user_hours)


# print("Exercise 3.2")
# hours = float(input("Input count of hours: "))
# print(f"time1 = {hours} --> litres = {math.floor(hours * 0.5)}")

# print("Exercise 4")
# s = input("Input string: ")
# if s.count(" ") > 0:
#     s = s.upper()
# else:
#     s = s.lower()
#
# print(s)
