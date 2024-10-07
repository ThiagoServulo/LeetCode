from collections import Counter

def repeatedCharacter(s):
    for end in range(1, len(s) + 1):
        if max(list(Counter(s[:end]).values())) == 2:
            return s[end - 1]

print(repeatedCharacter("abccbaacz")) # 'c'