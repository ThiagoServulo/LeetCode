def decodeMessage(key, message):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
               'u', 'v', 'w', 'x', 'y', 'z']
    aux = []
    for n in key:
        if n not in aux and n != " ":
            aux.append(n)
    res = ''
    for l in message:
        res += letters[aux.index(l)] if l != " " else ' '
    return res


print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv")) # "this is a secret"
