def findWordsContaining(words, x):
    return [index for index in range(0, len(words)) if x in words[index]]


print(findWordsContaining(["leet","code"], "e")) # [0, 1]
print(findWordsContaining(["abc","bcd","aaaa","cbc"], "a")) # [0, 2]