def findRelativeRanks(score):
    res = []
    score_sorted = sorted(score,reverse=True)
    for s in score:
        index = score_sorted.index(s)
        if index == 0:
            res.append("Gold Medal")
        elif index == 1:
            res.append("Silver Medal")
        elif index == 2:
            res.append("Bronze Medal")
        else:
            res.append(str(index + 1))
    return res

print(findRelativeRanks([5,4,3,2,1])) # ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
print(findRelativeRanks([10,3,8,9,4])) # ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
