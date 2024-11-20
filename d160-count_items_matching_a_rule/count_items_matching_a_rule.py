def countMatches(items, ruleKey, ruleValue):
    key = ["type", "color", "name"].index(ruleKey)
    return len(list(filter(lambda item: item[key] == ruleValue, items)))

print(countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"))