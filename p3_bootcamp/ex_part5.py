# Ex. 128


def valid_parentheses(string):
    opened_par = 0
    closed_par = 0
    for el in string:
        if el == "(":
            opened_par += 1
        elif el == ")":
            closed_par += 1
        if opened_par < closed_par:
            return False
    if opened_par != closed_par:
        return False
    return True


print(valid_parentheses("()")) # True
print(valid_parentheses(")(()))")) # False
print(valid_parentheses("(")) # False
print(valid_parentheses("(())((()())())")) # True
print(valid_parentheses('))((')) # False
print(valid_parentheses('())(')) # False
print(valid_parentheses('()()()()())()(')) # False

print("-----------------------")

# Ex. 129


def reverse_vowels(string):
    vow_list = [el for el in string if el in "aeiouAEIOU"]
    return "".join(vow_list.pop() if el in "aeiouAEIOU" else el for el in string)
    # res = ""
    # for el in string:
    #     if el in "aeiouAEIOU":
    #         el = vow_list.pop()
    #     res += el
    # return res


print(reverse_vowels("Hello!")) # "Holle!"
print(reverse_vowels("Tomatoes")) # "Temotaos"
print(reverse_vowels("Reverse Vowels In A String")) # "RivArsI Vewols en e Streng"
print(reverse_vowels("aeiou")) # "uoiea"
print(reverse_vowels("why try, shy fly?")) # "why try, shy fly?"

print("-----------------------")

# Ex. 130


def three_odd_numbers(lst):
    for i in range(len(lst)):
        if i + 2 < len(lst) and sum(lst[i:i+3]) % 2 == 1:
            return True
    return False


print(three_odd_numbers([1,2,3,4,5])) # True
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False

print("-----------------------")

# Ex. 131


def mode(lst):
    mode_dict = {el: lst.count(el) for el in lst}
    return [k for k in mode_dict.keys() if mode_dict[k] == max(mode_dict.values())][0]


print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) # 4

print("-----------------------")

# Ex. 131


def running_average():
    count = 0
    summ = 0

    def helper(num):
        nonlocal count
        nonlocal summ
        count += 1
        summ += num
        avg = summ / count
        return round(avg, 2)
    return helper


rAvg = running_average()
print(rAvg(10)) # 10.0
print(rAvg(11)) # 10.5
print(rAvg(12)) # 11

rAvg2 = running_average()
print(rAvg2(1)) # 1
print(rAvg2(3)) # 2
