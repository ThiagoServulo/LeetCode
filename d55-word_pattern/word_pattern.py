from functools import reduce


def wordPattern(pattern, s):
    s_list = s.split(' ')

    if(len(s_list) != len(pattern)):
        return False

    dict_pattern = {}
    for index in range(0, len(pattern)):
        if pattern[index] not in dict_pattern:
            dict_pattern[pattern[index]] = s_list[index]
        else:
            if dict_pattern[pattern[index]] != s_list[index]:
                return False
    return len({x for x in dict_pattern.values()}) == len(dict_pattern) 

print(wordPattern("abba", "dog cat cat dog"))  # True
print(wordPattern("abba", "dog cat cat fish")) # False
print(wordPattern("aaaa", "dog cat cat dog"))  # False
print(wordPattern("abba", "dog dog dog dog"))  # False