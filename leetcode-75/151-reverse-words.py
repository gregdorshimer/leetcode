def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    mylist = s.split()
    mylist.reverse()
    return ' '.join(mylist)