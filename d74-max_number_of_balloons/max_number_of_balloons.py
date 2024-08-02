def maxNumberOfBalloons(text):
    balloon = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
    l_letters = []
    letters = set(text)
    for letter in letters:
        if letter in balloon.keys():
            l_letters.append(int(text.count(letter) / balloon[letter]))
    return 0 if len(l_letters) != len(balloon) else min(l_letters)

print(maxNumberOfBalloons("lloo"))