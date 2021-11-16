age = int(input("How old are you? "))

if age >= 18:
    print("Welcome!")
else:
    print(f"You are too young! You are {age} years old. Please, come in {18 - age} years!")
