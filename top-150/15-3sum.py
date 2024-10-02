class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triple = [nums[i], nums[l], nums[r]]
                    res.append(triple)
                    while l < r and nums[l] == triple[1]:
                        l += 1
                    while l < r and nums[r] == triple[2]:
                        r -= 1
        return res










        """
        brute force:
        """
        res = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if ((nums[i], nums[j], nums[k]) not in res) and \
                            ((nums[i], nums[k], nums[j]) not in res) and \
                            ((nums[j], nums[i], nums[k]) not in res) and \
                            ((nums[j], nums[k], nums[i]) not in res) and \
                            ((nums[k], nums[i], nums[j]) not in res) and \
                            ((nums[k], nums[j], nums[i]) not in res):
                            res.add((nums[i], nums[j], nums[k]))
        for item in res:
            list(item)
        return list(res)
