class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = [] # stack of tuples

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                top = stack.pop()
                result[top[0]] = i - top[0]
            stack.append((i, temp))

        return result