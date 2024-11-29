def sumOddLengthSubarrays(arr):
    size = 1
    res = 0
    while size <= len(arr):
        for init in range(len(arr) - size + 1):
            res += sum(arr[init:init + size])
        size += 2
    return res

print(sumOddLengthSubarrays([1, 2, 3])) # 1 + 2 + 3 + 1 + 2 + 3 = 12