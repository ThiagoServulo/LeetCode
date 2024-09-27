def restoreString(s, indices):
    z = zip(s, indices)
    z = sorted(z, key=lambda x: x[1])
    return ''.join([x[0] for x in z])

print(restoreString('abc', [2,1,0])) # 'cba'
