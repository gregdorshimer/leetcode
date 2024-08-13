def removeStars(s):
    """
    :type s: str
    :rtype: str
    """
    stack = ''
    for i in range(len(s)):
        if s[i] == "*":
            stack = stack[:-1]
        else:
            stack += s[i]
    return stack
