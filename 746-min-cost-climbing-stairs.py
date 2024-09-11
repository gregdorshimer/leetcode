class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[1]
        full_cost = cost
        for i in range(len(full_cost) - 3, -1, -1):
            full_cost[i] = cost[i] + min(full_cost[i + 1], full_cost[i + 2])
        return min(full_cost[0], full_cost[1])