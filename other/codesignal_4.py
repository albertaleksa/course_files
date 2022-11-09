def solution(a, m, k):
    count = 0
    for i in range(len(a)-m+1):
        new_arr = a[i: i+m]
        dict_el = {}
        inner_count = 0
        for el in new_arr:
            if (k - el) in dict_el:
                inner_count += 1
            else:
                dict_el[el] = 1

        if inner_count > 0:
            count += 1
    return count


if __name__ == "__main__":
    arr = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7]
    m = 4
    k = 10
    print(solution(arr, m, k))

    arr = [15, 8, 8, 2, 6, 4, 1, 7]
    m = 2
    k = 8
    print(solution(arr, m, k))
