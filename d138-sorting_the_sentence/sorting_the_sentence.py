def sortSentence(s):
    s = s.split(' ')
    odict = {n[-1]:n[:-1] for n in s}
    odict = sorted(odict.items())
    return ' '.join([x[1] for x in odict])

print(sortSentence("is2 sentence4 This1 a3")) # This is a sentence
