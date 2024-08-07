def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    s = ''
    current = chars[0]
    counter = 0
    for char in chars:
        if char == current:
            counter += 1
            print('incremented counter to', counter)
        else:
            print('s before changes:', s)
            s += current
            s += str(counter)
            print('s after changes:', s)
            current = char
            counter = 0
    print('s: ', s)
    chars = list(s)
    return len(chars)

compress(['a', 'b', 'c', 'c', 'c', 'c', 'c'])
