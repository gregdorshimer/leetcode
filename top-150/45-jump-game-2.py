
def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums[-1] = 0
    for i in range(len(nums) - 2, -1, -1):
        val = nums[i]
        if 0 < val:
            nums[i] = None
            if i + val >= len(nums) - 1:
                nums[i] = 1
            else:
                for j in range(i + val, i, -1):
                    if nums[j] == 0:
                        continue
                    elif nums[i]:
                        nums[i] = min(nums[i], nums[j])
                    else:
                        nums[i] = nums[j]
                if nums[i]:
                    nums[i] += 1
                else:
                    nums[i] = 0
        print(nums)
    return nums[0]

"""
print(jump([2,3,1,1,4]))
print(jump([2,3,0,1,4]))
print(jump([3,2,1]))
print(jump([1,1,1,1]))
print(jump([5,0,0,0,0,0]))
print(jump([1,2,1,1,1]))
"""
print(jump([2,0,2,0,1]))
