# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 1
        upper = n
        my_guess = int((lower + upper) / 2)
        resp = guess(my_guess)
        while resp != 0:
            if resp < 0:
                if upper == my_guess:
                    upper -= 1
                else:
                    upper = my_guess
            else:
                if lower == my_guess:
                    lower += 1
                else:
                    lower = my_guess
            my_guess = int((lower + upper) / 2)
            resp = guess(my_guess)
        return my_guess