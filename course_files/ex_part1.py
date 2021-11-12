# Ex. 108
'''
Write a function called reverse_string which accepts a string
and returns a new string with all the characters reversed.

reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''


# add whatever parameters you deem necessary - good luck!
def reverse_string(string):
    # implement your function here
    return string[::-1]


print(reverse_string('awesome'))
print("----------------------------")
# Ex. 109
'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''


def list_check(lst):
    # return all(map(lambda x: isinstance(x, list), lst))
    return all(type(x) == list for x in lst)
    # for el in lst:
    #     print(f"el = {el} type(el) = {type(el)}")
    #     if type(el) != list:
    #     # if not isinstance(el, list):
    #         return False
    # return True


print(list_check([[],[1],[2,3]]))
print("----------------------------")

# Ex. 110
'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''


def remove_every_other(lst):
    return [lst[i] for i in range(len(lst)) if i % 2 == 0]
    # return [val for i, val in enumerate(lst) if i % 2 == 0]
    # lst_new = []
    # for i in range(len(lst)):
    #     if i % 2 == 0:
    #         lst_new.append(lst[i])
    # return lst_new


print(remove_every_other([1,2,3,4,5]))

print("----------------------------")

# Ex. 111

'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

def sum_pairs(lst, num):
    new_lst = [[lst[i],lst[i+1]] for i in range(len(lst) - 1) if lst[i] + lst[i+1] == num]
    return new_lst[0] if len(new_lst) > 0 else []

print(sum_pairs([4,2,10,5,1], 6))
print(sum_pairs([11,20,4,2,1,5], 100))

print("----------------------------")

# Ex. 112

'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''


def vowel_count(string):
    string = string.lower()
    return {key: string.count(key) for key in string if key in 'aeoiu'}


print(vowel_count('awesome'))
print(vowel_count('Elie'))
print(vowel_count('Colt'))

