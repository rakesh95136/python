#Program to calculate sum of first N odd natural numbers

#9 7 5 3 1

#Basically function fun(n) will check if the supplied number is even or odd number. If the number is odd then  just call 2nd function fun1(n2)
# if it is even number the make it odd by (n-1) and then supplied to fun1(n2)

def fun(n):
    v = (n%2)
    if (v != 0):
        s1 = fun1(n)
        return s1
    else:
        n3 = (n-1)
        s1 = fun1(n3)
        return s1





def fun1(n2):
    if ( n2 == 1):
        return 1
    else:
        s = (n2 + fun1(n2-2))
        return s


f = fun(11)

print(f)






