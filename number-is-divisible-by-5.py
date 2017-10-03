#Write a program to check whether a given number is divisible by 5 or not

a = input("Enter a number : ")

b = (int(a)%5)

if(b == 0):
    print("Yes")
else:
    print("No")

