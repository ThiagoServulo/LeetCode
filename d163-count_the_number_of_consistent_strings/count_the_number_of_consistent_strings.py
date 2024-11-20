def countConsistentStrings(allowed, words):
    count = 0
    for word in words:
        word = set(word)
        if(len([letter for letter in word if letter not in allowed]) == 0):
            count += 1
    return count

print(countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"])) # 7