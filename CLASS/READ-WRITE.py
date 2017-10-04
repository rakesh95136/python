'''

f = open('C:/Users/admin/Documents/file1.txt', 'r')

e = f.read()

count = 0
for i in e:
	count += 1
print(count)

'''

f = open('C:/Users/admin/Documents/file10.txt', 'w')
f.write('hello')