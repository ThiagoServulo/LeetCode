def commonFactors(a, b):
    n_min, n_max = min(a, b), max(a, b)
    count = 0
    for n in range(1, n_min + 1):
        if n_min % n == 0 and n_max % n == 0:
            count += 1
    return count

print(commonFactors(1000, 998))