def balancedStringSplit(s):
    count_r = count_l = count_total = 0
    for x in s:
        if x == 'R':
            count_r += 1
        else:
            count_l += 1
        if count_r == count_l:
            count_total += 1
            count_r = count_l = 0
    return count_total

print(balancedStringSplit('RLRRRLLRLL')) # 2
print(balancedStringSplit('LLLLRRRR')) # 1