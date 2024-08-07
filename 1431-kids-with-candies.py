def kidsWithCandies(self, candies, extraCandies):
    my_max = max(candies)
    result = []
    for i in range(len(candies)):
        result.append(candies[i] + extraCandies >= my_max)
    return result