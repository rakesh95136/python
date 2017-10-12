#8) Write a program to count the number of occurrences of each character in a given string

s = 'rakeshthakurrr'

d = {}

for i in s:
	if i in d:
		d[i] = d[i] + 1
	else:
		d[i] = 1


print(d)