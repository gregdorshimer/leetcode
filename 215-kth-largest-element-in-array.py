import heapq

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    heapq.heapify(nums)
    return heapq.nlargest(k, nums)[-1:][0]


test1 = [3,2,1,5,6,4]
print(findKthLargest(test1, 2))
