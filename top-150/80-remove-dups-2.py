def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    k = 0
    for num in nums:
        if k < 2 or num != nums[k - 2]:
            nums[k] = num
            k += 1
    return k


print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))