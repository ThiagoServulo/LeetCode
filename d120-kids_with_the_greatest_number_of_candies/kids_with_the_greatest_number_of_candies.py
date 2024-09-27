def kidsWithCandies(candies, extraCandies):
    m = max(candies)
    return [(i + extraCandies) >= m for i in candies]

print(kidsWithCandies([2,3,5,1,3], 3)) # [true,true,true,false,true]