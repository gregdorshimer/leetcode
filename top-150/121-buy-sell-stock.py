class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_max = prices[-1]
        cur_profit = 0
        for i in range(len(prices) - 2, -1, -1):
            cur_max = max(cur_max, prices[i + 1])
            cur_profit = max(cur_profit, cur_max - prices[i])
        return cur_profit

print(Solution.maxProfit(Solution(), [7,1,5,3,6,4]))