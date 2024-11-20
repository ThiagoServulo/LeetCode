def canMakeArithmeticProgression(arr):
    arr = sorted(arr)
    aux = None
    for index in range(len(arr) - 1):
        if(aux == None):
            aux = abs(arr[index] - arr[index + 1])
        else:
            if(aux != abs((arr[index] - arr[index + 1]))):
                return False
    return True

print(canMakeArithmeticProgression([3,5,1])) # True
print(canMakeArithmeticProgression([1,2,4])) # False