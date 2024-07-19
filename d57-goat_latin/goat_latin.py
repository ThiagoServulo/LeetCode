def toGoatLatin(sentence):
    words = sentence.split(" ")
    aux = 2
    ret = []
    for word in words:
        if(word[0].lower() in ['a', 'e', 'i', 'o', 'u']):
            ret.append(word + "m" + (aux * "a"))
        else:
            ret.append(word[1:] + word[0] + "m" + (aux * "a"))
        aux += 1
    return ' '.join(ret)

print(toGoatLatin("The quick brown fox jumped over the lazy dog"))