# Ex. 113

'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''


def titleize(string):
    return " ".join((word[0].upper() + word[1:]) for word in string.split())


print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))

print("-------------------------")

# Ex. 114
'''
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
'''


def find_factors(num):
    return [el for el in range(1, num+1) if num % el == 0]


print(find_factors(10))
print(find_factors(412146))

print("-------------------------")

# Ex. 115

'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''

def includes(collection, val, index=0):
    if isinstance(collection, (str, list)):
        return val in collection[index:]
    elif isinstance(collection, dict):
        return val in collection.values()
    return False


print(includes([1, 2, 3], 1))
print(includes([1, 2, 3], 1, 2))
print(includes({ 'a': 1, 'b': 2 }, 1))
print(includes({ 'a': 1, 'b': 2 }, 'a'))
print(includes('abcd', 'b'))
print(includes('abcd', 'e'))

print("-------------------------")

# Ex. 116
'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''


def repeat(string, num):
    return "".join(string for i in range(num))


print(repeat('*', 3))
print(repeat('abc', 2))
print(repeat('abc', 0))

print("-------------------------")

# Ex. 116

'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''


def truncate(string, num):
    if num < 3:
        return "Truncation must be at least 3 characters."
    elif len(string) >= num:
        return string[:num-3] + "..."
    else:
        return string


print(truncate("Super cool", 2))
print(truncate("Super cool", 1))
print(truncate("Super cool", 0))
print(truncate("Hello World", 6))
print(truncate("Problem solving is the best!", 10))
print(truncate("Another test", 12))
print(truncate("Woah", 4))
print(truncate("Woah", 3))
print(truncate("Yo",100))
print(truncate("Holy guacamole!", 152))



