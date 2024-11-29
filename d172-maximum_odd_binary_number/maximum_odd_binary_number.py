def maximumOddBinaryNumber(s):
    return ('1' * (s.count('1') - 1)) + ('0' * s.count('0')) + '1'


print(maximumOddBinaryNumber('100')) # '001'