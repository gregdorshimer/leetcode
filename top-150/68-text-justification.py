import math
from functools import total_ordering


def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    line = []
    line_len = 0
    res = []
    for i in range(len(words)):
        if line_len == 0:
            line.append(words[i])
            line_len += len(words[i])
        elif line_len + 1 + len(words[i]) <= maxWidth:
            line.append(words[i])
            line_len = line_len + 1 + len(words[i])
        else:
            # pad line with spaces
            # append line to res
            # add words[i] to line
            if len(line) == 1: # if 1 word in this line
                res.append(line[0] + (' ' * (maxWidth - len(line[0]))))
            else:
                total_spaces = maxWidth - (line_len - (len(line) - 1))
                remainder = total_spaces % (len(line) - 1)
                spaces = int(math.floor(total_spaces / (len(line) - 1)))
                my_line = ''
                for j in range(len(line)):
                    my_line += line[j]
                    if j < len(line) - 1:
                        if remainder > 0:
                            my_line += ' ' * (spaces + 1)
                            remainder -= 1
                        else:
                            my_line += ' ' * spaces
                res.append(my_line)
            line = [words[i]]
            line_len = len(words[i])

    # add last line to res
    my_line = ''
    for k in range(len(line)):
        my_line += line[k]
        if k < len(line) - 1:
            my_line += ' '
    my_line += ' ' * (maxWidth - len(my_line))
    res.append(my_line)

    return res

print(fullJustify(["What","must","be","acknowledgment","shall","be"], 16))