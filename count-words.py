# Write a program to count the number of words in a string

s = "My name was something when I was old"

s1 = ' '.join(s)

list1 = s1.split()

print(len(list1))

# OR BELOW PROGRAM

count = 0
for i in list1:
    count = count + 1

print(count)
