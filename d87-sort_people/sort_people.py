def sortPeople(names, heights):
    people = {height: name for name, height in zip(names, heights)}
    people = sorted(people.items(), key=lambda item: item[0], reverse=True)
    return [x[1] for x in people]

print(sortPeople(["Mary","John","Emma"], [180,165,170])) # ['Mary', 'John', 'Emma']