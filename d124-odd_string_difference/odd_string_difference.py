def oddString(words):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for word in words:
        w = []
        w.extend(list(zip(word, word[1:])))
        s = {abs(letters.index(x[0]) - letters.index(x[1])) for x in w if (abs(letters.index(x[0]) - letters.index(x[1]))) != 0}
        if len(s) == 1:
            return word
        

print(oddString(["adc","wzy","abc"])) # "abc"
print(oddString(["aaa","bob","ccc","ddd"])) # "bob"
