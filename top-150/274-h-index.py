
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        sorted_cit = sorted(citations, reverse=True)
        for i in range(len(citations)):
            if sorted_cit[i] > i:
                h += 1
            else:
                break
        return h

print(Solution.hIndex(Solution(), [3,0,6,1,5]))