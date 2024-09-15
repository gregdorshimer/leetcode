class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = int((j + i) / 2)
            if nums[mid] < nums[mid + 1]:
                if i == mid:
                    i += 1
                else:
                    i = mid
            else:
                j = mid
        return j