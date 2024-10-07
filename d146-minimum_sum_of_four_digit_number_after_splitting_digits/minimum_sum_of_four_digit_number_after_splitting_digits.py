def minimumSum(num):
    l_num = [int(n) for n in str(num)]
    new1 = new2 = ''
    for i in range(0, len(l_num)):
        if i%2 == 0:
            if new1 == '':
                new1 = str(min(l_num))
                l_num.remove(min(l_num))
            else:
                new1 += str(max(l_num))
                l_num.remove(max(l_num))
        else:
            if new2 == '':
                new2 = str(min(l_num))
                l_num.remove(min(l_num))
            else:
                new2 += str(max(l_num))
                l_num.remove(max(l_num))
    return int(new1) + int(new2)


print(minimumSum(4009)) # 13
print(minimumSum(2932)) # 52