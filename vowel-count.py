s = 'My name is something from california'

d = {}

list = s.split()

s1 = ''.join(list)

s2 = ' '.join(s1)

list1 = s2.split()
list2 = []
for n in list1:
    if (n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u'):
        list2.append(n)

for n1 in list2:
    if n1 in d:
        d[n1] = d[n1] + 1
    else:
        d[n1] = 1


print (d)



#----OR

x = input('Enter The test : ')

x1 = ' '.join(x)

list = x1.split()

d = {}

for i in list:
    if (i == 'a' or i =='e' or i == 'i' or i == 'o' or i == 'u'):
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1


print (d)
