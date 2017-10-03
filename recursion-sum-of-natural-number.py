#5 4 3 2 1
# 5 + 4 + 3 + 2 + 1

def fun1(n):
    if (n == 1):
        return 1
    else:
       n1 = (n + fun1(n-1))
       return n1


ss = fun1(10)

print(ss)