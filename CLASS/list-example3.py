import collections
'''
Write a program to find the maximum number from the given list of numbers and replace all the numbers from the list with maximum
number


Given two list x and y, print new list as output which includes all the elements of x and y except
for the first and last elements

Write a program to print True if the given list contains multiple of 4 or 8

'''

#Write a program to find the maximum number from the given list of numbers and replace all the numbers from the list with maximum
#number

list = [1,2,9,8,44,5]

max = 0
for i in list:
    if i > max:
        max = i

index = 0
for j in list:
    list[index] = max
    index += 1

print(list)



#Given two list x and y, print new list as output which includes all the elements of x and y except
#for the first and last elements

listA = [1,2,3,4,5]
listB = [11,22,33,44,55]

listC = []

for i in listA:
    if ((i == listA[0]) or (i == listA[-1])):
        pass
    else:
        listC.append(i)

for i in listB:
     if ((i == listB[0]) or (i == listB[-1])):
         pass
     else:
         listC.append(i)

print(listC)

#OR

del listA[0]
del listA[-1]
del listB[0]
del listB[-1]
listC = listA + listB
print(listC)


#OR
print(listA[1:-1])
print(listB[1:-1])



#Write a program to print True if the given list contains multiple of 4 or 8

list1 = [1,2,17,26,24]

for i in list1:
    if ((i%4) == 0 or (i%8) == 0):
        print("true")
    else:
        pass

#OR

for i in list1:
    if not (i%4):
        print(i)



