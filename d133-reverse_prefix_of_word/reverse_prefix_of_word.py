def reversePrefix(word, ch):
    try:
        pos = word.index(ch)
        return word[pos: 0: -1] + word[0] + word[pos + 1: len(word)]
    except ValueError:
        return word


print(reversePrefix('abcdef', 'd')) # 'dcbaef'