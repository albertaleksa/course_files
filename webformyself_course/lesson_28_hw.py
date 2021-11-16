def odd_ball(arr):
    if arr.count("odd") > 0:
        if arr.index("odd") in arr:
            return True
    return False


print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]))
print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]))
print(odd_ball(["even", 10, "odd", 2, "even"]))


def find_sum(n):
    return sum(i for i in range(n+1) if i % 3 == 0 or i % 5 == 0)


print(find_sum(5))
print(find_sum(10))


def get_names(l):
    return [el for el in l if len(el) == 4]


names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]
print(get_names(names))
