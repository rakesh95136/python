import collections
'''
--STRING--

Write a program to reverse a string

Write a program to print a new string which contains 4 copies of the last three characters from the given string.

Write a program to print the output string which contains last half + first half of the given string. The given string is of even length.

Given a string, print the output string by removing the first and last character of the string.

Given two strings of different length and print output string as shortest string + largest string + shortest string

Given a string, write a program which rotates left 2 and prints the output below.
Ex input : Hello
output : lloHe

'''

#Write a program to reverse a string

str = "ABCDEF"

l = len(str) - 1

str1 = ''

i = 0
while (l >= 0):
    str1 = str1 + str[l]
    l -= 1

print(str1)


#Write a program to print a new string which contains 4 copies of the last three characters from the given string.
s = 'abcdef'
new_str = (4 * s[3:])
print(new_str)

#OR

a = ''
for i in range(0,4):
    a += s[3:]

print(a)

#Write a program to print the output string which contains last half + first half
#of the given string. The given string is of even length.
s = '12345678'
half_len = len(s)/2
j = int(half_len)
print(s[:j])
print(s[j:])

#Given a string, print the output string by removing the first and last character of the string.
s = '12345'
print(s[:1])  #Print first character
print(s[-1:]) #print last ccharacter

#Given a string, write a program which rotates left 2 and prints the output below.
#Ex input : Hello
#output : lloHe
s = 'Hello'
d = s[:2]
d1 = s[2:]
print(d1 + d)
