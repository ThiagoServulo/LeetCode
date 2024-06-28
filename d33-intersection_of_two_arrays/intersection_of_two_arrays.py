def intersection(list1, list2):
    list3 = []
    for l in list1:
        if l in list2 and l not in list3:
            list3.append(l)
    return list3

def intersection2(list1, list2):
    return list(set(list1).intersection(set(list2)))


print(intersection2([4,9,5], [9,4,9,8,4]))