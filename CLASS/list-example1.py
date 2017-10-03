'''
Write a program to print a new list which contains all the first characters of strings in a list

list = ['Madhya Pradesh','Karnataka','Chennai','Goa','Delhi']

'''
list = ['Madhya Pradesh','Karnataka','Chennai','Goa','Delhi']

for i in list:
    print(i[0])


'''
Write a program to replace each string with an integer value in a given list of strings. 
The replacement integer value should be sum of ASCCI values of each character of corresponding string.

list_rivers = ['Ganges','Godavari','Brahmaputra','Narmada','Yamuna','Mahanadi','Kaveri','Tapti']

'''

list_rivers = ['Ganges','Godavari','Brahmaputra','Narmada','Yamuna','Mahanadi','Kaveri','Tapti']

new_list = []

for i in list_rivers:
    sum = 0
    for j in i:
        sum = sum + ord(j)
    new_list.append(sum)

print(new_list)


'''
Write a program which prints all duplicated values in a list
'''

list = [1,2,3,4,5,3,4,6,7,8,2]

new_list = []

for i in list:
    if i not in new_list:
        new_list.append(i)
    else:
        print(i)

OR

print(d)

new = []
for i in list:
    if i in new:
        print(i)
    else:
        new.append(i)





