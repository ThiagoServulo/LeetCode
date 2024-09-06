def vowelStrings(words, left, right):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
    count = 0
    for word in words[left: right + 1]:
        if(word[0] in vowels and word[-1] in vowels):
            count += 1
    return count

print(vowelStrings(["hey","aeo","mu","ooo","artro"], 1, 4)) # 3