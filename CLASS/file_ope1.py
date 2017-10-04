import os
'''
1) Create a directory with name "newdir" and create a file "templo" in the new dirctory "newdir"
2) Rename a file in a particular directory
3) List all the files from a given path and verify the file text.file exists or not? If the file does not exit create it.
4) Write a program to ccount each word from the given file.
5) Write a program to retrieve the words XYZ and ABC from a given file
6) Write a program to get some keywords from a file.
7) Get the current working directory and navigate to some other directory and verify navigation is successful or not.
8) Remove all the empty directories from a given path
9) Get file size, inode, owners of a each file in a given path
'''

#1) Create a directory with name "newdir" and create a file "tempo" in the new dirctory "newdir"

path = "./newdir"

if not os.path.exists(path):
	os.mkdir(path)

filename = ./tempo"

print(os.path.dirname(path))


