def convertToBin(n):
    if n == 0:
        return 0
    return (n % 2) + 10 * convertToBin(int(n / 2))

def minBitFlips(start, goal):
    start, goal = (start, goal) if start < goal else (goal, start)
    s = str(convertToBin(start))[::-1]
    g = str(convertToBin(goal))[::-1]
    count = 0
    for i in range(0, len(s)):
        if s[i] != g[i]:
            count += 1
    for i in range(len(s), len(g)):
        if g[i] == '1':
            count += 1
    return count

print(minBitFlips(10 , 7)) # 3
print(minBitFlips(82 , 10)) # 3



