def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    my_stack = []
    for char in s:
        if char != ']':
            my_stack.append(char)
        else:
            subsegment = ''
            count = ''
            while my_stack and my_stack[-1] != '[':
                subsegment = my_stack.pop() + subsegment
            my_stack.pop()
            while my_stack and my_stack[-1] in digits:
                count = my_stack.pop() + count
            segment = subsegment * int(count)
            for letter in segment:
                my_stack.append(letter)
    return ''.join(my_stack)


print(decodeString('3[a]2[bc]'))
