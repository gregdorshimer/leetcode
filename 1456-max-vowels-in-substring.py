def maxVowels(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    current_vowels = 0
    for i in range(k):
        if s[i] in vowels:
            current_vowels += 1
    max_vowels = current_vowels
    i = 0
    j = k
    while j < len(s):
        if s[i] in vowels:
            current_vowels -= 1
        if s[j] in vowels:
            current_vowels += 1
        max_vowels = max(max_vowels, current_vowels)
        i += 1
        j += 1
    return max_vowels
