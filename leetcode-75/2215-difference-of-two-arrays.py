def findDifference(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    """
    answer = [[], []]
    nums1_set = set(nums1[:])
    nums2_set = set(nums2[:])
    answer[0] = list(nums1_set.difference(nums2_set))
    answer[1] = list(nums2_set.difference(nums1_set))
    return answer
