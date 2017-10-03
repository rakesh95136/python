#Given a string, find its first non-repeating character

s = 'GeeksforGeeks'  #This is should print f
d = {}

s1 = ' '.join(s)

list = s1.split()

for i in list:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1


for i in d:
    if (d.get(i) > 1):
       pass
    else:
        print(i)
        exit()







