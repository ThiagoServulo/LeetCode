def calPoints(operations):
    array = []
    for operation in operations:
        if operation == '+':
            array.append(array[-1] + array[-2])
        elif operation == 'D':
            array.append(array[-1] * 2)
        elif operation == 'C':
            array.pop()
        else:
            array.append(int(operation))
    return sum(array)

print(calPoints(["5","2","C","D","+"])) # 30
print(calPoints(["5","-2","4","C","D","9","+","+"])) # 27
print(calPoints(["5","C"])) # 0