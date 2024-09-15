def increasingTriplet(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    least = float('inf')
    mid = float('inf')
    for n in nums:
        if n <= least:
            least = n
        elif n <= mid:
            mid = n
        else:
            return True
    return False