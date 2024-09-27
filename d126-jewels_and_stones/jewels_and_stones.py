def numJewelsInStones(jewels, stones):
    count = 0
    for j in jewels:
        count += stones.count(j)
    return count

print(numJewelsInStones("aA", "aAAbbbb")) # 3
