from collections import Counter

def firstUniqChar(s):
    letters = dict(Counter(s))
    index_unique_letters = [s.index(x[0]) for x in letters.items() if x[1] == 1]
    return min(index_unique_letters) if len(index_unique_letters) > 0 else -1

print(firstUniqChar('leetcode')) # 0
print(firstUniqChar('leetcodel')) # 3
print(firstUniqChar('aaaaaaaaaaaaaaaa')) # -1