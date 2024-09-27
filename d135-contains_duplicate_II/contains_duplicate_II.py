from collections import Counter

def containsNearbyDuplicate(nums, k):
    n = Counter(nums)
    for init in range(len(nums)):
        if n.get(nums[init]) <= 1:
            continue
        for i in range(init + 1, len(nums)):
            if nums[init] == nums[i] and abs(i - init) <= k:
                return True
    return False

print(containsNearbyDuplicate([1,2,3,1], 3)) # True
print(containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False