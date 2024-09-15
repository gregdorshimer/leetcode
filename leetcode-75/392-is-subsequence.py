def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    i = 0
    j = 0
    while (i < len(s)) & (j < len(t)):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i >= len(s)
