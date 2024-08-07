def gcdOfStrings(self, str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    if len(str1) <= len(str2):
        x = str1
        y = str2
    else:
        x = str2
        y = str1
    if x + y != y + x:
        return ''
    for i in range(len(x), 0, -1):
        print('i = ', i)
        print('len(x) % i = ', len(x) % i)
        print('len(y) % i = ', len(y) % i)
        if ((len(x) % i) == 0) & ((len(y) % i) == 0) & (x[:i] == y[:i]):
            return x[:i]
    return ''
