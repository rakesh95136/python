#How to check if a string contains only digit

s = 'adsdsd3sdsds2ee'

s1 = ' '.join(s)

list = s1.split()

list1 = []
for i in list:
    try:
      list1.append(int(i))
    except ValueError:
      pass

if (len(list1)) > 0:
    print('Yes the string contain numbers')
else:
    print('No the string doesnt have numbers')
