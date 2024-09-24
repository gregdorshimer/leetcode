class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank = 0
        min_tank = 0
        min_index = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff
            if tank < min_tank:
                min_index = i + 1
                min_tank = tank
        if tank < 0:
            return -1
        else:
            return min_index


#print(canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))