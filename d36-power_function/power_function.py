def pow(x, n, d):
    def p1(x, n):
        return 1 if (n == 0) else x * p1(x, n := n-1)
    p = p1(x,n)
    return p - (int(p/d) * d)


print(pow(2,3,3))