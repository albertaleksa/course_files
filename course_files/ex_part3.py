# Ex. 118


def two_list_dictionary(lst1, lst2):
    # return {k: v for (k, v) in zip(lst1, lst2)}
    return {lst1[i]: (lst2[i] if i < len(lst2) else None) for i in range(len(lst1))}


print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])) # {'a': 1, 'b': 2, 'c': 3}
print(two_list_dictionary(['x', 'y', 'z'], [1,2])) # {'x': 1, 'y': 2, 'z': None}

print("-----------------------")

# Ex. 119


def range_in_list(lst, start=0, end=None):
    end = end or lst[-1]
    # return sum(lst[i] for i in range(start, end+1))
    return sum(lst[start:end+1])


print(range_in_list([1,2,3,4],0,2)) #  6
print(range_in_list([1,2,3,4],0,3)) # 10
print(range_in_list([1,2,3,4],1)) #  9
print(range_in_list([1,2,3,4])) # 10
print(range_in_list([1,2,3,4],0,100)) # 10
print(range_in_list([],0,1)) # 0


print("-----------------------")

# Ex. 120


def same_frequency(num1, num2):
    if len(str(num1)) != len(str(num2)):
        return False
    d1 = {letter: str(num1).count(letter) for letter in str(num1)}
    d2 = {letter: str(num2).count(letter) for letter in str(num2)}
    for k, v in d1.items():
        if not k in d2.keys():
            return False
        elif d2[k] != d1[k]:
            return False
    return True




print(same_frequency(551122,221515)) # True
print(same_frequency(321142,3212215)) # False
print(same_frequency(1212, 2211)) # True
print(same_frequency(12123435, 22114336)) # False
print(same_frequency(12123435, 22114333)) # False


print("-----------------------")

# Ex. 121


def nth(lst, num):
    return lst[num]


print(nth(['a', 'b', 'c', 'd'], 1))  # 'b'
print(nth(['a', 'b', 'c', 'd'], -2)) #  'c'
print(nth(['a', 'b', 'c', 'd'], 0))  # 'a'
print(nth(['a', 'b', 'c', 'd'], -4)) #  'a'
print(nth(['a', 'b', 'c', 'd'], -1)) #  'd'
print(nth(['a', 'b', 'c', 'd'], 3))  # 'd'


print("-----------------------")

# Ex. 121


def find_the_duplicate(lst):
    for el in lst:
        if lst.count(el) > 1:
            return el
    return None


print(find_the_duplicate([1,2,1,4,3,12])) # 1
print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
print(find_the_duplicate([2,1,3,4])) # None


