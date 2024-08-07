def mergeAlternately(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    result = ''
    word1_chars = list(word1)
    word2_chars = list(word2)
    for i in range(min(len(word1), len(word2))):
        result = result + word1_chars[i]
        result = result + word2_chars[i]
    if (len(word1_chars) > len(word2_chars)):
        for c in word1_chars[len(word2_chars):]:
            result = result + c
    else:
        for c in word2_chars[len(word1_chars):]:
            result = result + c
    return result