def defangIPaddr(address):
    return address.replace('.', '[.]')

print(defangIPaddr('127.0.0.1')) # '127[.]0[.]0[.]1'