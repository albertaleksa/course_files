# Ex. 123


def sum_up_diagonals(lst):
    # sum_up = 0
    # for i in range(len(lst)):
    #     sum_up += lst[i][i] + lst[i][len(lst)-i-1]
    # return sum_up
    return sum(lst[i][i] + lst[i][len(lst)-i-1] for i in range(len(lst)))


list1 = [
    [1, 2],
    [3, 4]
]

print(sum_up_diagonals(list1))  # 10

list2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sum_up_diagonals(list2))  # 30

list3 = [
    [4, 1, 0],
    [-1, -1, 0],
    [0, 0, 9]
]

print(sum_up_diagonals(list3))  # 11

list4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(sum_up_diagonals(list4))  # 68

print("-----------------------")

# Ex. 124


def min_max_key_in_dictionary(dict_val):
    return [min(dict_val.keys()), max(dict_val.keys())]


print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'})) # [1,10]
print(min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"})) # [1,4]

print("-----------------------")

# Ex. 125


def find_greater_numbers(lst):
    pass


find_greater_numbers([1,2,3]) # 3
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0


