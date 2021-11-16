import random


def check_number_func(user_number, main_number):
    if user_number == main_number:
        return True
    else:
        if user_number > main_number:
            print("Your number more than guessed number")
        elif user_number < main_number:
            print("Your number less than guessed number")
        return False


print("This is the game 'Guess The Number'!")
unknown_number = random.randint(1, 100)
counts = 0

while True:
    check_number = int(input("Try to guess. Input your number from 1 to 100: "))
    counts += 1
    if check_number_func(check_number, unknown_number):
        print(f"Congratulations! You guess the number {unknown_number} with {counts} attempts")
        break
    else:
        print("Sorry! You didn't guess the number!")
        print("Try again!")
        print()
