def pivotInteger(n, init = 0):
    if init > n:
        return -1
    if sum(range(0, init+1)) == sum(range(init, n+1)):
        return init
    return pivotInteger(n, init := init + 1)


"""
def pivotInteger(n):
    init = 0
    while init <= n:
        if sum(range(0, init+1)) == sum(range(init, n+1)):
            return init
        init += 1
    return -1
"""

print(pivotInteger(8)) # 6
print(pivotInteger(9)) # -1
print(pivotInteger(1)) # 1