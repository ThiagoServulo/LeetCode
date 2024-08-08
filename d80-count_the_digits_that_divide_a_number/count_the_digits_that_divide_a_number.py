def countDigits(num):
    count = 0
    for n in str(num):
        if num % int(n) == 0:
            count += 1
    return count

print(countDigits(1248)) # 4