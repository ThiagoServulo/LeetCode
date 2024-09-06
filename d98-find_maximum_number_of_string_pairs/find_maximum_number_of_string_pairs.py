from collections import Counter

def maximumNumberOfStringPairs(words):
    counter_list = []
    count = 0
    for word in words:
        c = Counter(word)
        if c in counter_list:
            count += 1
        counter_list.append(c)
    return count


print(maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))