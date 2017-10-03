'''

1) Check whether the given element is present in a tuple or not
2) Write a program in 2 lines:
        --Using a for loop and a tuple to print the below: (Hello earth & hello mars

3) Can we convert tuples to lists and vice versa

'''

# 1) Check whether the given element is present in a tuple or not
t = (1,2,3,4)
print( 1 in t)  #returns true
print( 1 not in t) #returns false

#2) Write a program in 2 lines:
#      --Using a for loop and a tuple to print the below: (Hello earth & hello mars

for n in ('earth', 'mars'):
    print('Hello ', n)

#3) Can we convert tuples to lists and vice versa
t = (1,2,3,4)
list1 = list(t) # Converts list into tuples
print(list1)
print(tuple(list(t))) # Returns Tuples
print(list(tuple(list(t)))) #Returns List
