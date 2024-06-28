def fizzBuzz(num):
    def divisibleByThree(num):
        return (num % 3) == 0
    def divisibleByFive(num):
        return (num % 5) == 0
    res = []
    for n in range(1, num + 1):
        aux = ''
        if divisibleByThree(n):
            aux += 'Fizz'
        if divisibleByFive(n):
            aux += 'Buzz'
        if aux == '':
            aux = str(n)
        res.append(aux)
    return res

print(fizzBuzz(15))