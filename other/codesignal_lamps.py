def solution(lamps):
    res = {}
    for lamp in lamps:
        print(f"lamp = {lamp}")
        center = lamp[0]
        radius = lamp[1]
        for i in range(center-radius, center+radius+1):
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        print(f"res = {res}")
    print(res)
    max_lamps = max(res.values())
    print(f"max_lamps = {max_lamps}")

    for coord in sorted(res):
        print(f"coord = {coord}")
        if res[coord] == max_lamps:
            return coord


arr = [[-2, 3], [2, 3], [2, 1]]
print(solution(arr))

arr = [[-2, 3], [5, 1]]
print(solution(arr))