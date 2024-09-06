def scoreOfString(s):
    count = 0
    aux = [ord(c) for c in s]
    for index in range(0, len(aux) - 1):
        count += abs(aux[index] - aux[index + 1])
    return count

print(scoreOfString("hello")) # 13
