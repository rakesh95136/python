import os

from os import walk


path = "./CLASS/newdir"
for(a,b,c) in walk(path):
	for i in c:
		if(i == 'mmm.txt'):
			p = path + "/"+i
			d = open(p,'r')
			vv = d.read()
			count = 0
			for k in vv:
				count += 1
				print(count)
			


