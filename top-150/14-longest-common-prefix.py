def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = ''
    char = ''
    i = 0
    while i < len(strs[0]):
        char = strs[0][i]
        for my_str in strs:
            if i < len(my_str):
                if my_str[i] != char:
                    return prefix
            else:
                return prefix
        prefix += char
        i += 1
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))