def sortVowels(s):
    aux = sorted([n for n in s if n.lower() in ["a", "e", "i", "o", "u"]], reverse=True)
    res = ""
    for index in range(len(s)):
        if(s[index].lower() in ["a", "e", "i", "o", "u"]):
            res += aux.pop()
        else:
            res += s[index]
    return res


print(sortVowels("lEetcOde")) # "lEOtcede"