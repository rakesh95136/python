

#Shallow and Deep Copy


#In Shallow copying address of the sublist or address of the element is copied
#Therefore if any changes is made in list2 is reflected in list1 also

# In Deep copying the value is copied
# Because of this any changes made in list1 will not refelect in list1 




#Shallow copy Example 1
k1 = [1,2,3,4,5]
k2 = k1
k2[1] = 99  #If I change k2 element it will be reflected in the k1 too
print('k1 :',k1)  # Result : [1, 99, 3, 4, 5]
print('k2 :',k2)  # Result : [1, 99, 3, 4, 5]
print('Address of the k1 : ', hex(id(k1)))  # Address will be same
print('Address of the k2 : ', hex(id(k2)))  # Address will be same

#Shallow copy Example 2
#I'm changing the memory address
m1 = [1,2,3,4]
m2 = m1  # At this point the address of m1 and m2 will be same
m2 = [11,22,33] # Now at this point me got new memory address
print(m1) # Result [1,2,3,4]
print(m2) # result [11,22,33]

#Copy with the Slice Operator
#Technically shallow work doesn't work here
n1 = [1,2,3,4]
n2 = n1[:]
print('Address of n1 :',hex(id(n1)))  # Address is different than n2
print('Address of n2 :', hex(id(n2))) # Address is differnt than n1
#Therefor if any changes are made in n2 it will not refelect to n1
n2[1] = 100
print('n1 :',n1) #[1, 2, 3, 4]
print('n2 :',n2) #[1, 100, 3, 4]

#Shallow copy with  list contains sublists
b1 = [1,2,3,[100,200,300],4]
b2 = b1[:]
#Still both the address are different
print('Address of b1 :', hex(id(b1)))
print('Address of b2 :',hex(id(b2)))
b2[3][2] = 0
b2[1] = 77
print('b1  :', b1)
print('b2  :', b2)

#deepcopy
from copy import deepcopy

#Example 1
z1 = [1,2,3,4,5]
z2 = deepcopy(z1)
#Both z1 and z2 will get differebt address
print('Address of z1 : ',hex(id(z1)))
print('Address of z2 : ', hex(id(z2)))
z2[4] = 200
print('z1 : ',z1)  # print [1, 2, 3, 4, 5]
print('z2 :', z2)  # [1, 2, 3, 4, 200]

#Example2

a1 = [1,2,3,[11,22,33,4]]
a2 = deepcopy(a1)

a2[3][0] = 77
a2[0] = 0

print('a1  : ', a1)  #print [1, 2, 3, [11, 22, 33, 4]]
print('a2  :', a2) # print [0, 2, 3, [77, 22, 33, 4]]















