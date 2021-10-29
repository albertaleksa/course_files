def gen2(n):
    for e in range(1, n+1):
        yield e * 2


def gen(lst):
    for el in lst:
        # for e in range(1, el+1):
        #     yield e
        yield from gen2(el)


for i in gen([5, 10]):
    print(i, end=" ")

print()


lst = [1, '2', 3]


def f(l):
    return [i * 2 for i in l]


def f2(l):
    def multi(x):
        if isinstance(x, int):
            return int(x) * 2
    return [multi(i) for i in l if multi(i)]


print(f(lst))
print(f2(lst))
