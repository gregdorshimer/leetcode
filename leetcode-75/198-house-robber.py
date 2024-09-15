class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        totals = nums
        # totals[i] is the total value stealable if ith house is robbed
        totals[len(nums) - 3] = nums[len(nums) - 3] + nums[len(nums) - 1]
        for i in range(len(nums) - 4, -1, -1):
            totals[i] = max(totals[i + 1],
                            totals[i] + totals[i + 2],
                            totals[i] + totals[i + 3])
        return max(totals[0], totals[1])

