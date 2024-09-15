def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    stack = []
    i = 0
    while i < len(asteroids):
        if len(stack) == 0:
            stack.append(asteroids[i])
            i += 1
        elif (stack[len(stack) - 1] < 0) | (asteroids[i] > 0):
            stack.append(asteroids[i])
            i += 1
        elif (stack[len(stack) - 1]) + asteroids[i] == 0:
            stack.pop()
            i += 1
        elif stack[len(stack) - 1] + asteroids[i] < 0:
            stack.pop()
        else:
            i += 1

    return stack
