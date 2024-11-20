def findLucky(arr):
    for n in sorted(list(set(arr)),reverse=True):
        if n == arr.count(n):
            return n
    return -1

print(findLucky([1,2,2,3,3,3])) # 3