row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

def findWords(words):
    output = []
    for word in words:
        row = row1 if word[0].lower() in row1 else (row2 if word[0].lower() in row2 else row3)      
        if all(letter.lower() in row for letter in word[1:]):
            output.append(word)       
    return output

print(findWords(["Hello","Alaska","Dad","Peace"])) # ["Alaska","Dad"]
print(findWords(["omk"])) # []
print(findWords(["adsdf","sfd"])) # ["adsdf","sfd"]