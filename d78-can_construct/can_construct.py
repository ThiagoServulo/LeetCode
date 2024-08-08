from collections import Counter

def canConstruct(ransomNote, magazine):
    rn_counter = Counter(ransomNote)
    m_counter = Counter(magazine)
    for rn in rn_counter.items():
        if rn[0] in m_counter.keys():
            if m_counter[rn[0]] < rn[1]:
                return False
        else:
            return False
    return True

print(canConstruct("abbb", "aab")) # False
print(canConstruct("ab", "aab")) # True