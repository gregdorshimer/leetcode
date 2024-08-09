def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    ops = 0
    numbers = sorted(nums)
    i = 0
    j = len(numbers) - 1
    while i < j:
        sum = numbers[i] + numbers[j]
        if sum < k:
            i += 1
        elif sum > k:
            j -= 1
        else:
            ops += 1
            i += 1
            j -= 1
    return ops
