class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        val = 0
        i = len(s) - 1
        while i > -1:
            val += vals[s[i]]
            if i > 0:
                if vals[s[i]] <= vals[s[i - 1]]:
                    i -= 1
                else:
                    val -= vals[s[i - 1]]
                    i -= 2
            else:
                break
        return val

print(Solution.romanToInt(Solution(), "III"))
print(Solution.romanToInt(Solution(), "LVIII"))
print(Solution.romanToInt(Solution(), "MCMXCIV"))


