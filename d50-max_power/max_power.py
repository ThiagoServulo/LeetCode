def maxPower(s):
    current_letter = ''
    max_count = 0
    count = 1
    for letter in s:
        if current_letter != letter:
            current_letter = letter
            max_count = max(max_count, count)
            count = 1
        else:
            count += 1
    return max(max_count, count)

print(maxPower("abbcccddddeeeeedcba")) # 5
print(maxPower("leetcode")) # 2