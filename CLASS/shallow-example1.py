'''

--SHALLOW COPYING--------

Given a list
colours1 = ['red','green'] with the help of a new list, modify the list colors1, such that
colours1 = ["red","blue"]


Given a list
list1 = ['a','b','c','d'] with the help of 'slice' construct and a new list, make changes in list1, such that
list1=['a','x','c','d']. Verify if the original list is modified.


Given a list, lst1 = ['a','b',['ab','ba']] with the help of 'slice' construct and a new list, modifylst1 such that
lst1 = ['a','b',['ab','d']]

'''

#Given a list
#colours1 = ['red','green'] with the help of a new list, modify the list colors1, such that
#colours1 = ["red","blue"]

colours1 = ['red','green']
colours2 = colours1

colours2[1] = 'blue'

print(colours1)
print(colours2)

#Given a list
#list1 = ['a','b','c','d'] with the help of 'slice' construct and a new list, make changes in list1, such that
#list1=['a','x','c','d']. Verify if the original list is modified.

list1 = ['a','b','c','d']
list2 = list1[:]
list2[1] = 'x'
#list1 and list2 will be different
print(list1) 
print(list2)


#Given a list, lst1 = ['a','b',['ab','ba']] with the help of 'slice' construct and a new list, modifylst1 such that
#lst1 = ['a','b',['ab','d']]

lst1 = ['a','b',['ab','ba']]
lst2 = lst1[:]
lst2[2][1] = 'd'
print(lst1)
print(lst2)


