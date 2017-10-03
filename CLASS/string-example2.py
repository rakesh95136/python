'''
Concatente two given strings by omitting the first character
Write a program to count the number of occurrences of each character in a given string
Write a program to convert all the vowels to uppercase for the given input string.
Write a program to reverse the given input list
Write a program to count number of occurrences of vowels in a given string
Write a program to convert lower case to upper case letter?
Write a program to print the longest length string from given input list of strings.
'''

#Concatente two given strings by omitting the first character
a = '1234'
b = '5678'
print(a[1:] + b[1:])

#Write a program to count the number of occurrences of each character in a given string
s = 'aabbccdeeff'
d = {}
for i in s:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)

#Write a program to reverse the given input list
list1 = [1,2,3,4,5]
len = len(list1) - 1
list2 = []

while(len >= 0):
    list2.append(list1[len])
    #print(len)
    len -= 1
print(list2)


#Write a program to count number of occurrences of vowels in a given string

s = input("Enter the String : ")
count = 0
for i in s:
    if i in ('aeiou'):
        count += 1
    else:
        pass
print("The Vowels occurance are : ",count)



#Write a program to print the longest length string from given input list of strings.
s = input("Enter the sentance : ")
list = s.split()
d = {}
for i in list:
    count = 0
    for j in i:
        count += 1
    d[i] = count

print(max(d))

#OR

str = input('Enter the any sentance :')
list = str.split()

def get_len(s):
    count = 0
    for i in s:
        count += 1
    return count


def longest_len(list):
    d = 0
    x1 = ''
    for x in list:
        len = get_len(x)
        if len > d:
            d = len
            x1 = x
        return x,len

l = longest_len(list)
print(l)


#Write a program to convert all the vowels to uppercase for the given input string.
'''
For ex : 
(ord('a') - 32 ) --> Given you ASCII value of Capital A
then
chr(ord('a' - 32) --> Give you the character back from the ASCII value 
'''
s = 'Hello what is your name'
new_str = ''
for i in s:
    if i in 'aeiou':
        new_str += chr(ord(i) - 32)
print(new_str)


#Write a program to convert lower case to upper case letter?
s = 'mynameisrakesh'
new_str = ''
for i in s:
    new_str += chr(ord(i) - 32)
print(new_str)



#Write a program to print the longest length string from given input list of strings.

list = ['abcdwwww','abc','nmbvxw','Rakeshthakur']
c1 = 0
for i in list:
    count = 0
    for j in i:
        count += 1
    if count > c1:
        c1 = count
        i1 = i
        #print(c1)
print(c1,i1)




























































