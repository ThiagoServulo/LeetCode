def prefixCount(words, pref):
    return len(list(filter(lambda x: x[0: len(pref)] == pref, words)))

print(prefixCount(["pay","attention","practice","attend"], "at")) # 2