class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        my_sum = 0
        candies = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i + 1]:
                candies[i + 1] = candies[i] + 1
        for j in range(len(ratings) - 1, 0, -1):
            if ratings[j] < ratings[j - 1] and candies[j] >= candies[j - 1]:
                candies[j - 1] = candies[j] + 1
            my_sum += candies[j]
        return my_sum + candies[0]

#print(candy([1,3,4,5,2]))