import heapq
from audioop import reverse

import heapq

class Solution(object):
    def maxScore(nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        my_heap = []
        zipped = sorted(list(zip(nums2, nums1)), reverse=True)
        max_sum = 0
        for num2, num1 in zipped:
            if len(my_heap) == k:
                popped = heapq.heappop(my_heap)
                max_sum -= popped
            heapq.heappush(my_heap, num1)
            max_sum += num1
            if len(my_heap) == k:
                result = max(result, max_sum * num2)
        return result
