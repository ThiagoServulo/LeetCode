sapo = 'a123 bscd1234 sapo123 a34s, def4123'

def isDelimiter(a):
    return a in [' ', ',', '\n']

def validPasswords(string):
    count = 0
    start_index = 0
    for index in range(0, len(string) + 1):
        if index == len(string) or isDelimiter(string[index]):
            sub_str = string[start_index: index]
            if 6 <= len(sub_str) <= 10 and \
            len([c for c in sub_str if c.isdigit()]) >= 3 and \
            len([c for c in sub_str if c.isalpha()]) >= 3:
                print(sub_str)
                count += 1
            start_index = index + 1
    return count

print(validPasswords(sapo))

            
