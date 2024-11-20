def findCenter(edges):
    for i in range(1, len(edges)):
        if edges[0][0] not in edges[i]:
            return edges[0][1]
    return edges[0][0]


print(findCenter([[1,2],[2,3],[4,2]])) # 2