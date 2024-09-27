def minimumAverage(nums):
    aux = []
    while len(nums) > 0:
        aux.append(((maior := max(nums)) + (menor := min(nums))) / 2)
        nums.remove(maior)
        nums.remove(menor)
    return min(aux)

print(minimumAverage([1,2,3,7,8,9])) # 5.0