def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    s = ''
    counter = 1
    for i in range(1, len(chars)):
        current = chars[i]
        prev = chars[i-1]
        if current == prev:
            counter += 1
        else:
            s += prev
            if counter > 1:
                s += str(counter)
                counter = 1
        if i == (len(chars) - 1):
            s += current
            if counter > 1:
                s += str(counter)

    chars = list(s)
    return len(chars)


compress(['a', 'a', 'a', 'b', 'b', 'b', 'c'])
compress(['a', 'b', 'c', 'c', 'c', 'c', 'c'])
compress(['a', 'a', 'b', 'b', 'c', 'c'])
compress(["a","a","b","b","c","c","c"])
compress(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'])
