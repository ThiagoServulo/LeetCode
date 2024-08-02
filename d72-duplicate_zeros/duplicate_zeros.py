def duplicateZeros(arr):
    index = 0
    tam = len(arr)
    while index < tam:
        if arr[index] == 0:
            arr.insert(index + 1, 0)
            arr.pop()
            index += 2
        else:
            index += 1
    return


arr = [1,0,2,3,0,4,5,0]
duplicateZeros(arr) # [1, 0, 0, 2, 3, 0, 0, 4]
print(arr)
