def countKeyChanges(s):
    aux = s[0].lower()
    count = 0
    for x in s[1:].lower():
        if x != aux:
            aux = x
            count += 1
    return count

print(countKeyChanges("AAAaBb"))