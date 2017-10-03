#Write a program to calculate sum of the digits of a given number

def fun1(remainingNo):
    r = 0
    while (int(remainingNo) > 0):
        if (int(remainingNo) < 10):
             r = (remainingNo + r)
             return r
        else:
            lastNo = int(remainingNo) % 10
            print("lastno  ", lastNo)
            r = lastNo + r
            remainingNo = int(remainingNo/ 10)


dd1 = input("Put the input Here : ")
dd = fun1(int(dd1))

print(dd)


#other way using list(array)

s = "3456"

s1 = ' '.join(s)
d = 0
list = s1.split()

for i in list:
    d = int(i) + d


print(d)