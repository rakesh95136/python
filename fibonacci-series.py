
#Fibonacci Series

# Write a program to print first N terms of Fibonacci series.

# Example 0 1 1 2 3 5 8 13 21 34
list = {}

i = 0
a = -1
b = 1
while(i <= 8):
     c = a + b;
     a = b
     b = c
     i += 1
     print(c)


#using recurssion

def fun1(n):
    if (n <= 2):
        return 1
    else:
        g = (fun1(n-1) + fun1(n-2))
        return g

f = fun1(8)

print(f)


