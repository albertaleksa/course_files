passw = input("Input password: ")


def check_passw(p):
    def deco(f):
        print("deco")
        if int(p) == 10:
            return f
        else:
            return lambda: "Closed"
    print("check")
    return deco


@check_passw(passw)
def func():
    return "Open"


print(func())
