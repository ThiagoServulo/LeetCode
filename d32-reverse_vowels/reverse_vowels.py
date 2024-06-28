def reverseVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s_vowels = [n for n in s if n in vowels]
    s_vowels.reverse()
    index = 0
    res = []
    for n in s:
        if n in vowels:
            res.append(s_vowels[index])
            index += 1
        else:
            res.append(n)
    return ''.join(res)
    

print(reverseVowels("race car"))