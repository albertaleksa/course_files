import sys


# map
doubles = map(lambda x: x * 2, [1, 2, 3, 4, 5])
print(list(doubles))

def decrement_list(lst):
    return list(map(lambda x: x - 1, lst))

print(decrement_list([1, 2, 3]))


# filter
l = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)


# filter & map
names = ["Lassie", "Colt", "Rusty"]
res = map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value) < 5, names))

print(list(res))



# Implement your is_all_strings function below:
def is_all_strings(lst):
    return all(isinstance(el, str) for el in lst)

print(is_all_strings(['a', 'b', 'c', 'd']))


# min max with lambda
names = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]
print(max(names))   # Tim
print(min(names))   # Arya

print(max(names, key=lambda n: len(n))) # Ollivander
print(min(names, key=lambda n: len(n))) # Tim


# sorted with lambda
songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

print(sorted(songs, key=lambda s: s['playcount'], reverse=True))


'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

# define sum_even_values
def sum_even_values(*arg):
    return sum(el for el in arg if el % 2 == 0)

print(sum_even_values(1,2,3,4,5,6))


# zip
def interleave(str1, str2):
    return "".join("".join(el) for el in zip(str1, str2))


print(interleave('hi', 'ha'))

