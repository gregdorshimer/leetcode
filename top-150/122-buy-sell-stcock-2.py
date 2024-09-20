class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        holding = False
        bought_at = -1
        for i in range(len(prices) - 1):
            if not holding and prices[i] < prices[i + 1]:
                bought_at = i
                holding = True
            elif prices[i] > prices[i + 1] and holding:
                profit += (prices[i] - prices[bought_at])
                holding = False
        if holding:
            profit += (prices[-1] - prices[bought_at])
        return profit