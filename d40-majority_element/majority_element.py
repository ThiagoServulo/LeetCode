from collections import Counter

def majorityElement(nums):
    dict_counter = Counter(nums)
    return dict_counter.most_common(1)[0][0]


print(majorityElement([6,5,5]))