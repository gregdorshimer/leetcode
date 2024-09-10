class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        nth = 0
        n1 = 0
        n2 = 0
        n3 = 1
        i = 0
        if n == 0:
            return 0
        while i < n:
            nth = n1
            n1 = n2
            n2 = n3
            n3 = nth + n1 + n2
            i += 1
        return n3