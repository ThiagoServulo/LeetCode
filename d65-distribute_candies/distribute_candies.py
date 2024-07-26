def distributeCandies(candyType):
    count_type = int(len(candyType) / 2)
    candy_set_len = len(set(candyType))
    return candy_set_len if candy_set_len < count_type else count_type

print(distributeCandies([1,1,2,2,3,3])) # 3
print(distributeCandies([1,1,2,3])) # 2
print(distributeCandies([1,1,1,1])) # 2
