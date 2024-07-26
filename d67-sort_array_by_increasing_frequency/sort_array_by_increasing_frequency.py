from collections import Counter

def frequencySort(nums):
    c_nums = dict(Counter(nums))
    quantity = sorted(list(set(c_nums.values())))
    resp = []
    for i in quantity:
        aux = [x for x in c_nums if c_nums.get(x) == i]
        aux = sorted(aux, reverse=True)
        for a in aux:
            for _ in range(0, i):
                resp.append(a)
    return resp

print(frequencySort([2,3,1,3,2])) # [1,3,3,2,2]