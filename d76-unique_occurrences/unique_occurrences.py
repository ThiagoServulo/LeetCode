def uniqueOccurrences(arr):
    s_arr = set(arr)
    nums_count = []
    for s in s_arr:
        c = arr.count(s)
        if c in nums_count:
            return False
        nums_count.append(c)
    return True

print(uniqueOccurrences([1,2,2,1,1,3])) # True
print(uniqueOccurrences([1,2])) # False