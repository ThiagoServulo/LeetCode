def twoSum(A, B):
    if len(A) == 1:
        return []

    ret = []
    for index1 in range(0, len(A)):
        for index2 in range(index1 + 1, len(A)):
            if(A[index1] + A[index2]) == B:
                if ret == [] or (ret[1] - 1) > index2:
                    ret = [index1 + 1, index2 + 1]
    return ret
    
print(twoSum([2, 4, 4, 5, 7, 11, 15], 9))