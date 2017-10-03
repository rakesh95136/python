#Program to calculate sum of first N even natural numbers

#10 8 6 4 2


def fun2(n):
    v = (n%2)
    if (v == 0):
       d = fun1(n)
       return d
    else:
       d = fun1(n-1)
       return d

def fun1(n):
    if (n == 2):
        return 2
    else:
        f = (n + fun1(n-2))
        return f


g = fun2(13)

print(g)

