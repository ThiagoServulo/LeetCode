def minCostClimbingStairs(cost):
    if len(cost) <= 1:
        return 0
    index = 0 if cost[0] < cost[1] else 1
    return cost[index] + minCostClimbingStairs(cost[index + 1:])

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
