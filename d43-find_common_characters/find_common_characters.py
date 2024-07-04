from collections import Counter

def commonChars(words):
    words_counter = [Counter(word) for word in words]
    word_base = words_counter[0]
    for word in words_counter[1:]:
        if(word_base == {}):
            return {}
        aux_word = {}
        for letter, count in word_base.items():
            if(letter in word):
                aux_word[letter] = min(count, word[letter])
        word_base = aux_word.copy()
    ret = []
    for letter, count in word_base.items():
        for _ in range(0,count):
            ret.append(letter)
    return ret

print(commonChars(["bella","xabel","roller"]))
