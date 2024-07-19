"""
s = "acg"
t_list = "ahbgdc"
letter = g
init = 5
index  = 5
"""

def isSubsequence(s, t):
    t_list = list(t)
    init = -1
    for letter in s:
        if letter in t_list:
            try:
                index = t_list.index(letter, init + 1)
                if(index < init):
                    return False
                init = index
            except ValueError:
                return False
        else:
            return False
    return True

print(isSubsequence("acd", "ahbgdc")) # False
print(isSubsequence("axd", "ahbgdc")) # False
print(isSubsequence("agc", "ahbgdc")) # True