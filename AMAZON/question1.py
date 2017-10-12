#1)	From a given list of array (Not sorted) find the second largest value


'''

A simple solution will be first sort the array in descending order and then return the second element from the sorted array. The time complexity of this solution is O(nlogn).

A Better Solution is to traverse the array twice. In the first traversal find the maximum element. In the second traversal find the greatest element less than the element obtained in first traversal. The time complexity of this solution is O(n).

A more Efficient Solution can be to find the second largest element in a single traversal.
Below is the complete algorithm for doing this:


'''

#simple soultion

list1 = [34,100,23,1,4,5,89]
list1.sort()
print(list1[len(list1) - 2])



#Better soultion


list = [4,5,2,7,8,1]

g = 0
g1 = 0
for i in list:
    if i > g:
        g = i
    
    else:
        pass

for i in list:
    if i != g:
        if i > g1:
            g1 = i
    
    

print(g)
print(g1)

