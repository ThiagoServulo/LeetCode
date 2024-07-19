def countSegments(s):
    return len([x for x in s.split(' ') if x != ''])

print(countSegments("Hello, my name is John")) # 5