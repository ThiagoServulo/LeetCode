def countAsterisks(s):
    s = s.split('|')
    return sum([s[x].count('*') for x in range(0, len(s), 2)])


print(countAsterisks("yo|uar|e**|b|e***au|tifu|l")) # 5