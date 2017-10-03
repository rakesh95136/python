#Write a java program to reverse a string

s = "MynameissomethingandsomedayI'llbehavename"

s1 = ' '.join(s)

list1 = s1.split()
list2 = []

count = len(list1)

while (count > 0):
     count = count - 1
     list2.append(list1[count])

s2 = ''.join(list2)

print(s2)

