def licenseKeyFormatting(s, k):
    a = ''
    aux = 0
    for x in s[::-1]:
        if x.isalpha() or x.isnumeric():
            a += x.upper()
            if ((len(a) - aux) % k) == 0:
                a += '-'
                aux += 1
    a = a[::-1]
    return a if a =='' or a[0] != '-' else a[1::]


print(licenseKeyFormatting("5F3Z-2e-9-w", 4)) # 5F3Z-2E9W
print(licenseKeyFormatting("2-5g-3-J", 2)) #2-5G-3J
