def thousandSeparator(n):
    ret = ''
    while n > 0:
        aux = str(n % 1000)
        aux = aux.zfill(3) if n > 1000 else aux
        ret = aux if ret == '' else (aux + '.') + ret
        n //= 1000
    return '0' if ret == '' else ret

print(thousandSeparator(51040)) # 51.040
print(thousandSeparator(0)) # 0