def stableMountains(height, threshold):
    res = []
    for i in range(0, len(height) - 1):
        if(height[i] > threshold):
            res.append(i + 1)
    return res

print(stableMountains([1,2,3,4,5], 2)) # [3, 4]