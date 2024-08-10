def largestAltitude(gain):
    """
    :type gain: List[int]
    :rtype: int
    """
    current_max = 0
    current_alt = 0
    for i in gain:
        current_alt += i
        if current_alt > current_max:
            current_max = current_alt
    return current_max
