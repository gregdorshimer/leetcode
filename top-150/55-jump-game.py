class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = len(nums) - 2
        while i > -1:
            j = i -1
            if nums[i] == 0:
                while j > -1:
                    if nums[j] > i - j:
                        i = j
                        break
                    j -= 1
                if j < 0:
                    return False
            i -= 1
        return True
