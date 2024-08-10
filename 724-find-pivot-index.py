def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left_sum = 0
    total_sum = sum(nums)
    for i in range(len(nums)):
        right_sum = total_sum - nums[i] - left_sum
        if right_sum == left_sum:
            return i
        left_sum += nums[i]
    return -1
