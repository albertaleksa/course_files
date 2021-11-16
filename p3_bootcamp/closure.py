def running_average():
    """
    Using closure.
    Function returns a function.
    When the function returned is passed a value,
    the function returns the current average of all previous function calls
    """
    count = 0
    summ = 0

    def helper(num):
        nonlocal count
        nonlocal summ
        count += 1
        summ += num
        avg = summ / count
        return round(avg, 2)

    return helper


rAvg = running_average()
print(rAvg(10)) # 10.0
print(rAvg(11)) # 10.5
print(rAvg(12)) # 11

rAvg2 = running_average()
print(rAvg2(1)) # 1
print(rAvg2(3)) # 2
