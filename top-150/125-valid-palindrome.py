
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    i = 0
    j = len(s) - 1
    chars = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    }
    while i < j and i < len(s) and j > -1:
        if s[i].lower() not in chars:
            i += 1
        if s[j].lower() not in chars:
            j -= 1
        if s[i].lower() in chars and s[j].lower() in chars:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome('..........!'))