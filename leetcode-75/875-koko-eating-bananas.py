import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        i = 1
        j = max(piles)
        while i < j:
            mid = int ((i + j) / 2)
            if i == mid:
                break
            if Solution.canEat(self, piles, mid, h):
                j = mid
            else:
                i = mid
        return j

    def canEat(self, piles, speed, hours):
        hoursNeeded = 0
        for pile in piles:
            hoursNeeded += math.ceil(pile / speed)
        return hoursNeeded <= hours

print(Solution.canEat(Solution(), [3,6,7,11], 4, 8))
print(Solution.canEat(Solution(), [3,6,7,11], 3, 8))
print(Solution.minEatingSpeed(Solution(), [3,6,7,11], 8))