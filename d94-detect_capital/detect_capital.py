def detectCapitalUse(word: str):
    filtered = [letter for letter in word if letter.islower()]
    if len(filtered) == 0 or len(filtered) == len(word) or \
        (len(filtered) == len(word) - 1 and word[0].isupper()):
        return True
    return False

print(detectCapitalUse('asc')) # True
print(detectCapitalUse('Google')) # True
print(detectCapitalUse('USA')) # True
print(detectCapitalUse('UaaSaaA')) # False