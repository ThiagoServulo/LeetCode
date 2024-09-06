def findPermutationDifference(s, t):
    res = 0
    for i in range(len(s)):
        res += abs(i - t.index(s[i]))
    return res

print(findPermutationDifference("abc", "bac")) # 2
print(findPermutationDifference("abcde", "edbac")) # 12
