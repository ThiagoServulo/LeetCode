def numberOfMatches(n):
    count = 0
    while n > 1:
        count += n - int((n / 2))
        n = int((n / 2))
    return count

print(numberOfMatches(7)) # 6
print(numberOfMatches(14)) # 13
print(numberOfMatches(55)) # 54