'''
Using print statement do the following
    1) Output the concatenation of two tuples
    2) Using an example tuple in the print statement, print the word 'World' 3 times
'''

#1) Output the concatenation of two tuples
#Example 1
t = (1,2,3) + (11,22,33)
print(t)

#Example 2
t1 = ('a','b','c')
t2 = ('A','B','C')
t3 = t1 + t2
print(t3)


#2) Using an example tuple in the print statement, print the word 'World' 3 times
#Example 1
t = ('hello',)
print(t * 3)

#Example 2
t1 = (1,2,3)
print(t1 * 3)