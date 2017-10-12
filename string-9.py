#9) Write a program to convert all the vowels to uppercase for the given input string.

a = 'rakeishthakuR'

for i in a:
	if i in 'aeiou':
		print(chr(ord(i) - 32))