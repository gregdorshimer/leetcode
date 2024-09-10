class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        result = spells
        for i in range(len(spells)):
            lower = 0
            upper = len(potions) - 1
            while True:
                if lower > upper:
                    result[i] = 0
                    break
                j = int((lower + upper) / 2)
                score = spells[i] * potions[j]
                if j > 0:
                    prev_score = spells[i] * potions[j - 1]
                    if prev_score < success <= score:
                        result[i] = len(potions) - j
                        break
                    elif score >= success and prev_score >= success:
                        if upper == j:
                            upper -= 1
                        else:
                            upper = j
                    else:
                        if lower == j:
                            lower += 1
                        else:
                            lower = j
                else:
                    if score >= success:
                        result[i] = len(potions)
                        break
                    else:
                        lower += 1
        return result
