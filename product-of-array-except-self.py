def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    answer = []
    left = [nums[0]]
    right = [nums[len(nums) - 1]]
    for i in range(1, len(nums)):
        left.append(left[i - 1] * nums[i])
    for i in range(len(nums) - 2, -1, -1):
        right.insert(0, right[0] * nums[i])
    for i in range(len(nums)):
        if i == 0:
            answer.append(right[1])
        elif i == (len(nums) - 1):
            answer.append(left[len(nums) - 2])
        else:
            answer.append(left[i - 1] * right[i + 1])
    return answer