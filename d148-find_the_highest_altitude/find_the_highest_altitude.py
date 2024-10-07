def largestAltitude(gain):
    maxi = 0
    for i in range(1,len(gain) + 1):
        aux = sum([n for n in gain[0: i]])
        maxi = max(maxi, aux)
    return maxi

print(largestAltitude([-5,1,5,0,-7])) # 1