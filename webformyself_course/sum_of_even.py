def sumEvenAfterQueries(nums, queries):
    """
    :type nums: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
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
