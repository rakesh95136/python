#Write a program to swap two numbers without using third variable


'''
a = 10   b = 20

a = a + b
a = 30

b = (a - b)
a = (a - b)

'''

a = input("Enter first number : ")
b = input("Enter second number : ")

print ("a : ", a)
print ("b : ", b)



a = int(a) + int(b)
b = int(a) - int(b)
a = int(a) - int(b)

print(" ")


print ("a : ", a)
print ("b : ", b)






