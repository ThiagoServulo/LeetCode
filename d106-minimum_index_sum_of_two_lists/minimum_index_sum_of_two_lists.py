def findRestaurant(list1, list2):
    res = []
    min_index = len(list1) + len(list2)
    for l in list1:
        if l in list2:
            index = list1.index(l) + list2.index(l)
            if index <= min_index:
                if index < min_index:
                    res.clear()
                min_index = index
                res.append(l)
    return res


print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"])) # ['Shogun']

print(findRestaurant(["happy","sad","good"], ["sad","happy","good"])) # ['happy', 'sad']