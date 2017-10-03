'''---DEEP COPYING------------------------

GIven a list
lst1 = ['a','b',['ab','ba']]
Use the function deepcopy and a new list to make changes in the lst2. Verify if the list is modified


Given a listlst1 = ['a','b',['ab','ba']]
Use the function 'copy' and a new list to make changes in the lst2. Verify if the list is modified
'''

from copy import deepcopy

#Given a list
#lst1 = ['a','b',['ab','ba']]
#Use the function deepcopy and a new list to make changes in the lst2. Verify if the list is modified

lst1 = ['a','b',['ab','ba']]
lst2 = deepcopy(lst1)
lst2[2][1] = 'z'
lst2[0] = 'z'
#Both lists will be different
print(lst1)
print(lst2)

#Given a list
# lst1 = ['a','b',['ab','ba']]
#Use the function 'copy' and a new list to make changes in the lst2. Verify if the list is modified
from copy import copy

lst1 = ['a','b',['ab','ba']]
lst2 = copy(lst1)
lst2[2][1] = 'x'
lst2[0] = 'x'
print(lst1)  # ['a', 'b', ['ab', 'x']]
print(lst2)  # ['x', 'b', ['ab', 'x']]

#BOTH ( UP and DOWN) program is same

lst1 = ['a','b',['ab','ba']]
lst2 = lst1[:]
lst2[2][1] = 'd'
lst2[0] = 'k'
print(lst1) # ['a', 'b', ['ab', 'd']]
print(lst2) #['k', 'b', ['ab', 'd']]