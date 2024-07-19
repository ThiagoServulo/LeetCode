from collections import Counter

def mostCommonWord(paragraph, banned):
    symbols = ["!", "?", "'", ",", ";", "."]
    for symbol in symbols:
        paragraph = paragraph.replace(symbol, " ")
    paragraph = paragraph.lower()
    words = [word.strip() for word in paragraph.split(" ") if word != ""]
    counter1 = Counter(words)
    for index in range(1, len(counter1) + 1):
        if(counter1.most_common(index)[index - 1][0] not in banned):
            return counter1.most_common(index)[index - 1][0]
        index += 1
    return []

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit", "Bob"]))
print(mostCommonWord("a, a, a, a, b,b,b,c, c", []))
print(mostCommonWord("a.", []))