def convertToBase(num, currentBase, newBase):
    if num == 0:
        return 0
    return (num % newBase) + currentBase * convertToBase(int(num / newBase), currentBase, newBase)

def convertToBase7(num):
    aux = ''
    if num < 0:
        aux += '-'
    aux += str(convertToBase(abs(num), 10, 7))
    return aux

print(convertToBase7(-7)) # -10
print(convertToBase7(100)) # 202