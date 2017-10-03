#Sum of squares of first N natural numbers using recursion

# 5 4 3 2 1

#25 + 16 + 9 + 4 + 1

def fun1(n):
    if (n == 1):
        return 1
    else:
        d = ((n*n) + fun1(n-1))
        return d

c = fun1(5)

print(c)
