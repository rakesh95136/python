#Can tuples be reassigned
#The answer is YES



my_tuple = ('a','b','c',[1,2,3,4,5,6],'d')

#In this case my_tuple address is copied to your_tuple, so if you make any changed in the your_tuple then it ia affected on my_tuple too
your_tuple = my_tuple

print('Address of my_tuple ',hex(id(my_tuple)))
print('Address of your_tuple ', hex(id(your_tuple)))


#Now if you make any canges in your_tuple then my_tupele also get affected

del your_tuple[3][1]
your_tuple[3].append(100)

print('your_tuple :', your_tuple)
print('my_tuple :', my_tuple)



#Now make any changes in the my_tuple

del my_tuple[3][2]

print('your_tuple :', your_tuple)
print('my_tuple :', my_tuple)





