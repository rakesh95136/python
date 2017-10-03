# Write a java program to print duplicate characters from String

s = "My name was something when I was small"
d = {}
d1 = {}
s1 = ' '.join(s)
list1 = s1.split()

list2 = []


for i in list1:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1


for n in d:
    if (d.get(n) > 1):
       d1[n] = d[n]


print(d1)



