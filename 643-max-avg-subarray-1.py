def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]
    max_sum = current_sum
    i = 0
    j = k
    while j < len(nums):
        current_sum -= nums[i]
        current_sum += nums[j]
        max_sum = max(current_sum, max_sum)
        i += 1
        j += 1
    return max_sum / float(k)

print(findMaxAverage([1,12,-5,-6,50,3], 1))
print(findMaxAverage([1,12,-5,-6,50,3], 4))

