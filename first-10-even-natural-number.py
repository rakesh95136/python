#Write a program to print first 10 even natural numbers
'''

j = 2
i = 0
while True:
    m = j % 2
    if m == 0:
        i = i + 1
        print(j)
        if (i == 10):

            exit()
    j += 1

# OR 

i = 0
while (i <= 10):
    print(2*i)
    i += 1


'''

