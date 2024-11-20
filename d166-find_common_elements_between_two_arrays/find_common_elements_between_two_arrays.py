def findIntersectionValues(nums1, nums2):
    return [sum([nums1.count(n) for n in set(nums2)]), sum([nums2.count(n) for n in set(nums1)])]


print(findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6])) # [3, 4]