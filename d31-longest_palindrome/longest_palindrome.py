def longestPalindrome(word):
    count_even_letters = 0
    count_odd_letters = 0
    letters = list(word)
    while len(letters) > 0:
        count = letters.count(letters[0])
        count_even_letters += int(count / 2)
        count_odd_letters += count % 2
        letters = [l for l in  letters if l != letters[0]]
    return (count_even_letters * 2) + 1 if count_odd_letters != 0 else (count_even_letters * 2)

print(longestPalindrome("acdd"))