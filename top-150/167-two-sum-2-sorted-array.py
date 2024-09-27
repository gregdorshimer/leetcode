class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            my_sum = numbers[i] + numbers[j]
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif my_sum > target:
                j -= 1
            else:
                i += 1