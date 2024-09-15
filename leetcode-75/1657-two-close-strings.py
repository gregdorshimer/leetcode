def closeStrings(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: bool
    """
    if len(word1) != len(word2):
        return False
    if set(word1) != set(word2):
        return False
    dict1 = dict()
    dict2 = dict()
    for i in range(len(word1)):
        if word1[i] in dict1:
            dict1[word1[i]] += 1
        else:
            dict1[word1[i]] = 1
        if word2[i] in dict2:
            dict2[word2[i]] += 1
        else:
            dict2[word2[i]] = 1
    occ1 = sorted(list(dict1.values()))
    occ2 = sorted(list(dict2.values()))
    return occ1 == occ2


closeStrings('aaabbbbccddeeeeefffff', 'aaaaabbcccdddeeeeffff')
