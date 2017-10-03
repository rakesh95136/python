#Write a program to reverse a number

def fun1(remains):
    f = ''
    while(int(remains) > 0 ):
        if remains < 10:
            f = f + str(remains)
            #print(remains)
            return f
        else:
            last = int(remains)%10 # It always return last number
            #print("last ", last)
            remains = int(remains/10) # It will return remaining value
            f = f + str(last)
            #print("f  " , f)



dd = input("Enter value : ")
ddd = fun1(int(dd))

print(ddd)



