def finalString(s):
    ret = ""
    for letter in s:
        if letter == 'i':
            ret = ret[::-1]
        else:
            ret += letter
    return ret

print(finalString('print')) # 'rpnt'
print(finalString('priint')) # 'prnt'