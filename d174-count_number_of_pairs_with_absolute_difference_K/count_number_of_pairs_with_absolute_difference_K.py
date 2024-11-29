def countKDifference(nums, k):
    count = 0 
    for i in range(len(nums)):
        count += len([n for n in nums[i+1::] if abs(n - nums[i]) == k])
    return count

print(countKDifference([1,2,2,1], 1))
print(countKDifference([3,2,1,5,4], 2))