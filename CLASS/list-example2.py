import collections

#Wirte a program to print True if the first element or last element is divisible by 4 in the given list

list = [4,4,2,3,4,4,6,24]

len = len(list)

i = 0

while(i < len):
    if (i == 0 or i == (len - 1)):
        g = (list[i]%4)
        if (g == 0):
            print("Positioned ",i,' element is divisible by 4')

    #print(len)
    i += 1


#OR

q = [4,5,6,7,1]
if (q[0]%4) == 0 or (q[-1]%4) == 0:
    print('True')
else:
    print('False')



#Write a program to print True if the first and last elements are equal and odd numbers in the given list
lst = [1,2,3,4,5,6,1]

if ((lst[-1] == lst[0]) and (lst[-1]%2 != 0) ):
    print('True')
else:
    print('False')


#Write a program to print True if the sum of the first and last element are equal from the given two lists

list1 = [3,2,3,4,5,4]
list2 = [7,2,3,4,5,1]

sum1 = list1[0] + list1[-1]
sum2 = list2[0] + list2[-1]

if (sum1 == sum2):
    print('True')
else:
    print('False')


#Write a program to print the sum of all the element in the given list.

list11 = [1,2,3,4,5]

s = 0
for i in list11:
    s = s + i
print(s)

#Write a program to sort a list of integer element








#Write a program to print a new list by doing a left rotate on the given list.
# Ex input: [4,5,6,7]  output: [5,6,7,4]

list = [4,5,6,7]

d = collections.deque(list)

d.

d.rotate(3)

print(d)
































































