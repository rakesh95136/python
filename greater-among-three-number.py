#Write a program to to find greater among three number

a = input("Enter a first number -- A : ")

b = input("Enter a second number -- B : " )

c = input("Enter a third number -- C : ")


if ( int(a) > int(b)):
    if (int(a) > int(c)):
        #print ("A  > B > C")
        if(int(c) > int(b)):
            print(" A > C > B")
        else:
            print("A > B > C")
    else:
        print ("C > A > B")
else:
    if(int(b) > int(c)):
        if(int(c) > int(a)):
          print("B  > C > A")
        else:
           print("B > A > C")
    else:
        print ("C > B > A")

