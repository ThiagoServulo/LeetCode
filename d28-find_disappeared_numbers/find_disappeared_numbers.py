def findDisappearedNumbers(nums):
   return [num for num in range(1, len(nums) + 1) if num not in nums]

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))