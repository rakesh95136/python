
str = "123456789"

d = len(str) - 1

i = 0
s = ''
while (d >= 0):
	s = s + str[d]
	d -= 1

print(s)
