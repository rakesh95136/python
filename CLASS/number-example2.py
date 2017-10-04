'''
Write a program to find if a given number is prime or not
Write a program to find the factorail of given number
Write a program to construct two dimensional array and print the same
Write a program to convert base 10 to base 2, base 8, base 16 number systems.

'''

#Write a program to find if a given number is prime or not
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
# 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
# 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199

# 1 2 3 4 5 6 7 8 9 10 11 12 13

'''
a = input('Enter the number : ')
a1 = int(a)

i = 1
while (i < (a1 - 1)):
    i += 1
    if (a1%i == 0):
        break
if (i == (a1-1)):
    print('Prime Number')
else:
    print('Not a Prime Number')


#OR

x = input('Enter The Number : ')
x1 = int(x)
i = 2
while (i < x1):
    if (x1%i) == 0:
        break
    i += 1

if(i == x1):
    print('PRIME')
else:
    print('NOT PRIME')

'''
# Write a program to find the factorail of given number
# 1 2 3 4

x = input('Enter the number : ')
x1 = int(x)

def fun(x1):
    if x1 == 1:
        return 1
    else:
        x1 = x1 * fun(x1 - 1)
        return x1


v = fun(x1)
print(v)

# OR

x = input('Enter the number :')
x1 = int(x)

p = x1
while (x1 > 1):
      x1 -= 1
      p = p * x1

print(p)


#Write a program to construct two dimensional array and print the same
