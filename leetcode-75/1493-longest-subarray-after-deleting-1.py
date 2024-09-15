def longestSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_ones = nums[0]
    i = 0
    j = 0
    flips = 1
    while j < len(nums):
        while (flips == 0) & (nums[j] == 0):
            # increment i loop
            if nums[i] == 0:
                flips += 1
            i += 1
        while (flips > 0) | (nums[j] == 1):
            # increment j loop
            if nums[j] == 0:
                flips -= 1
                j += 1
            else:
                j += 1
            if j >= len(nums):
                break
        max_ones = max(max_ones, j - i)

    return max(0, max_ones - 1)
