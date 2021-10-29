from course_files.timeit import Timer

code1 = """\
def sumEvenAfterQueries(nums, queries):
    sum_nums = sum(el1 for el1 in nums if el1 % 2 == 0)
    answer = []
    for x, k in queries:
        if nums[k] % 2 == 0:
            if x % 2 == 0:
                sum_nums += x
            else:
                sum_nums -= nums[k]
        elif x % 2 != 0:
            sum_nums += x + nums[k]
        nums[k] += x
        answer.append(sum_nums)
    return answer


nums = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]

print(sumEvenAfterQueries(nums, queries))
print(sumEvenAfterQueries([1], [[4, 0]]))
"""

t1 = Timer(stmt=code1)
# print(t1.timeit(number=10000))
print(t1.repeat(repeat=3, number=10000))
