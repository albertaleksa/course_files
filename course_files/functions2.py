def func1(a):
    print(f"a = {a} in func1")
    x = a
    print(f"x = {x} in func1")

    def func2(b):
        print(f"b = {b} in func2")
        nonlocal x                  #for modification var value, created in parent-function
        print(f"x = {x} in func2")
        print(x)
        x = b
        print(f"x = {x} in func2 after x=b")

    return func2


f1 = func1(10)
f1(5)
print()
f1(12)

# a = 10 in func1
# x = 10 in func1
# b = 5 in func2
# x = 10 in func2
# 10
# x = 5 in func2 after x=b
#
# b = 12 in func2
# x = 5 in func2
# 5
# x = 12 in func2 after x=b
#
# Process finished with exit code 0