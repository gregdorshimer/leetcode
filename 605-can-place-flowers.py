def canPlaceFlowers(self, flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    bedsum = sum(flowerbed)
    if n == 0:
        return True
    if len(flowerbed) <= 2:
        return (n == 1) & (bedsum == 0)
    mylist = flowerbed[:]
    i = 0
    k = 2
    if (flowerbed[0] == 0) & (flowerbed[1] == 0):
        mylist[0] = 1
    if len(flowerbed) >= 3:
        for j in range(1, len(flowerbed) - 1):
            if mylist[i] == 0 & mylist[j] == 0:
                if mylist[k] == 0:
                    mylist[j] = 1
            i += 1
            k += 1
    if (mylist[len(mylist) - 1] == 0) & (mylist[len(mylist) - 2] == 0):
        mylist[len(mylist) - 1] = 1
    return sum(mylist) >= n + bedsum