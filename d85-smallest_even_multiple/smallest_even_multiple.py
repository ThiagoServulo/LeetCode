def smallestEvenMultiple(n):
    count = 1
    n_max, n_min = max(n,2), min(n,2)
    while True:
        if(n_max * count) % n_min == 0:
            return n_max * count
        count += 1

print(smallestEvenMultiple(5)) # 10
print(smallestEvenMultiple(6)) # 6
print(smallestEvenMultiple(1)) # 2