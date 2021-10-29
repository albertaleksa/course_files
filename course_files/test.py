
t =[[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

for i in range(1):
    print('#')
else:
    print('#')

nums = [1, 2, 3]
vals = nums[-1:-2]

print(nums, vals)

x = 1
x = x == x
print(x)


var = 1
while var < 10:
    print('#')
    var = var << 1


i = 0
while i <= 3:
    i += 2
    print("*")

my_list = [3, 1, -2]
print(my_list[my_list[-1]])

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(vals)

my_list = [i for i in range(-1, 2)]
print(my_list)

my_list1 = [1, 2, 3]
for v in range(len(my_list1)):
    my_list1.insert(1, my_list1[v])
print(my_list1)

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print('#')

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)


def get_res(**kwargs):
    print(kwargs)


get_res(a=1, b=2, c=3)


tup = (1, ) + (1, )
tup = tup + tup
print(len(tup))

def fun(in1=2, out=3):
    return in1 * out

print(fun(3))

def fun(x):
    global yyy
    yyy = x ** x
    return yyy

fun(2)
print(yyy)
print("-------")

my_list1 = ["aa", "bb", "cc", "dd", "ee"]
print(my_list1)

def my_list(my_list):
    del my_list[3]
    my_list[3] = "ram"


print(my_list(my_list1))

print(my_list1)

def fun(inp=2, out=3):
    return inp * out

print(fun(out=2))

def f_1(a):
    return  None

def f_2(a):
    return None

print(f_2(2))

nums = [1, 2, 3]
vals = nums
del vals[:]

print(vals, nums)

