def reformat(s):
    l_num = [x for x in s if x.isdigit()]
    l_alpha = [x for x in s if x.isalpha()]
    if abs(len(l_num) - len(l_alpha)) > 1:
        return ""
    res = ""
    aux = 1 if len(l_num) > len(l_alpha) else 0
    for index in range(0, len(l_num) + len(l_alpha)):
        res += str(l_alpha.pop() if index % 2 == aux else l_num.pop())
    return res

print(reformat('123asc'))
print(reformat('123asc4'))