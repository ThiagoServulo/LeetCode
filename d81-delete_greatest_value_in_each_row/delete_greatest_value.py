def deleteGreatestValue(grid):
    n_min = min([len(row) for row in grid])
    grid = [sorted(row, reverse=True) for row in grid]
    count = 0 
    for index in range(0, n_min):
        count += max([row[index] for row in grid])
    return count

print(deleteGreatestValue([[1,2,4],[3,3,1]])) # 8

