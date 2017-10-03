#How to count number of vowels and consonants in a String

s = 'Hello how r u'

d = {}

list1 = ' '.join(s).split()
list2 = []
list3 = []
for i in list1:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        list2.append(i)
    else:
        list3.append(i)

print(len(list2))
print(len(list3))



