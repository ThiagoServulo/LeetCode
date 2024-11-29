def findDifference(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    return [list(nums1.difference(nums2)), list(nums2.difference(nums1))]


print(findDifference([1,2,3,3], [1,1,2,2])) # [[3], []]