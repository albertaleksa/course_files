
print("Before exception")

try:
    print("In try block")
    num = 100 / 0
except (ZeroDivisionError, TypeError) as err:
    print("In except block")
    print(err.__class__.__name__)
    print(err)
    num = 0
else:
    print("Else")
finally:
    print("Finally")

print(f"num = {num}")
print("After exception")


while True:
    try:
        num = int(input("Input number > 0: "))
        print(f"100 / {num} = {100 / num}")
        break
    except ZeroDivisionError:
        print("Number must be not equal 0")
    except ValueError:
        print('Must be a number')


