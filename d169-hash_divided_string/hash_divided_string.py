def stringHash(s, k):
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    res = ''
    i = 0
    while i < len(s):
        res += letter[sum(map(lambda x: letter.index(x), s[i: i + k])) % 26]
        i += k
    return res

print(stringHash("abcd", 2)) # 'bf'
print(stringHash("mxz", 3)) # 'i'