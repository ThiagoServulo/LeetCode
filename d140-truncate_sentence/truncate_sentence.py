def truncateSentence(s, k):
    s = s.split(' ')
    return ' '.join(s[:k])

print(truncateSentence("Hello how are you Contestant", 4))