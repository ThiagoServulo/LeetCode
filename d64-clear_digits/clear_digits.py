nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def clearDigits(s):
    if len([x for x in nums if x in s]) == 0:
        return s
    for index in range(0, len(s)):
        if s[index] in nums:
            s = s[0:index] + s[index + 1:]
            if index != 0:
                s = s[0:index - 1] + s[index:]
            return clearDigits(s)
    return s

print(clearDigits("ab2c")) # 'ac'
print(clearDigits("abc")) # 'abc'
