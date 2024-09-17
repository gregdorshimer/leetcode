def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    j = 1
    if len(nums) <= 1:
        return len(nums)
    while j < len(nums):
        if i == j:
            j += 1
        elif nums[i] == nums[j]:
            j += 1
        elif nums[i] != nums[j] and i + 1 < j:
            nums[i + 1] = nums[j]
            i += 1
            j += 1
        else:
            i += 1
            j += 1
    return i + 1

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
