def maximum69Number (num):
    index = 0
    num_str = str(num)
    for n in num_str:
        if(n == '6'):
            return int(num_str[:index] + '9' + num_str[index+1:])
        index += 1
    return num

print(maximum69Number(99669)) # 99969