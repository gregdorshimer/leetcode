class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        if j == -1:
            return 0
        if j == 0:
            if nums[0] == val:
                return 0
            else:
                return 1
        while j > i:
            while i < len(nums) and nums[i] != val:
                i += 1
            while j > -1 and nums[j] == val:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        return i

print(Solution.removeElement(Solution(), [3,2,2,3], 3))
print(Solution.removeElement(Solution(), [0,1,2,2,3,0,4,2], 2))
print(Solution.removeElement(Solution(), [3,3], 3))