
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left = [0] * len(height)
    right = [0] * len(height)
    max_left = 0
    for i in range(len(height)):
        left[i] = max_left
        if height[i] > max_left:
            max_left = height[i]
    max_right = 0
    for j in range(len(height) - 1, -1, -1):
        right[j] = max_right
        if height[j] > max_right:
            max_right = height[j]
    total = 0
    for k in range(len(height)):
        total += max(0, min(left[k], right[k]) - height[k])
    return total


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))