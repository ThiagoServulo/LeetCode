def nextGreaterElement(nums1, nums2):
    answer = []
    for num in nums1:
        index = nums2.index(num)
        if index == (len(nums2) - 1):
            answer.append(-1)
        else:
            aux = -1
            for n in nums2[index:]:
                if(n > num):
                    aux = n
                    break
            answer.append(aux)
    return answer

print(nextGreaterElement([4,1,2], [1,3,4,2])) # [-1,3,-1]
print(nextGreaterElement([2,4], [1,2,3,4])) # [3,-1]
print(nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])) # [7,7,7,7,7]