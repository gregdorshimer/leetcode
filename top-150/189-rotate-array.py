def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    inc = k % len(nums)
    length = len(nums)
    reverse(nums, 0, length - inc - 1)
    reverse(nums, length - inc, length - 1)
    reverse(nums, 0, length - 1)
    return nums

def reverse(arr, i, j):
    """ Reverses the elements in arr[i:j+1]"""
    while i < j :
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1



a = [1,2,3,4,5,6,7,8]
reverse(a, 4,7)
print(a)

print(rotate([1,2,3,4,5,6,7], 3))
print(rotate([-1,-100,3,99], 2))


