def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    mystring = list(s)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    i = 0
    j = len(s) - 1
    while True:
        if i >= j:
            break
        if mystring[i] in vowels:
            if mystring[j] in vowels:
                mystring[i], mystring[j] = mystring[j], mystring[i]
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            if mystring[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1
    return ''.join(mystring)
