def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    val_counts = dict()
    for num in arr:
        if num in val_counts:
            val_counts[num] += 1
        else:
            val_counts[num] = 1
    values = set()
    for val in val_counts.values():
        if val in values:
            return False
        else:
            values.add(val)
    return True
