def equalPairs(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    counter = 0
    rows = {}
    for row in grid:
        my_row = tuple(row)
        if my_row in rows:
            rows[my_row] += 1
        else:
            rows[my_row] = 1
    for i in range(len(grid)):
        col = []
        for j in range(len(grid)):
            col.append(grid[j][i])
        col = tuple(col)
        if col in rows:
            counter += rows[col]
    return counter



print(equalPairs([[1,2,3],[4,5,6],[7,8,9]]))
print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
