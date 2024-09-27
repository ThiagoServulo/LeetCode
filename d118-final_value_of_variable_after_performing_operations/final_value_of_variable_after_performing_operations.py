def finalValueAfterOperations(operations):
    num = 0
    for operation in operations:
        num = num + 1 if operation == "X++" or operation == "++X" else num - 1
    return num

print(finalValueAfterOperations(["--X","X++","X++"])) # 1