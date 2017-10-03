#How to check if a string contains only characters

s = '12121rakesh211'

s1 = ' '.join(s)

list = s1.split();
list2 = []

for i in list:
    if i.isdigit():
        pass
    else:
        list2.append(i)

print(list2)
