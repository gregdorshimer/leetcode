class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        return max(dict, key=dict.get)
        """
        # counter approach, O(1) space
        counter = 0
        cur = None
        for num in nums:
            if num == cur:
                counter += 1
            elif counter > 0:
                counter -= 1
            else:
                cur = num
                counter = 1
        return cur