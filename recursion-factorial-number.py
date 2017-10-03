# Python program to find the factorial of a number provided by the user.

# 5 4 3 2 1


def fun1(n):
    if (n == 1):
        return 1
    else:
        e = (n * fun1(n -1))
        return e


s = fun1(5)
print(s)
