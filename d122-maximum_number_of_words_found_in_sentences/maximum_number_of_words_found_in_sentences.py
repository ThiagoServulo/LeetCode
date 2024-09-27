def mostWordsFound(sentences):
    return max([len(s.split(' ')) for s in sentences])

print(mostWordsFound(["please wait", "continue to fight", "continue to win"])) # 3