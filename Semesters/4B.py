# Write a program to print a specific list after removing the 0th, 2nd, 4th and 5th element. 
# Code: 
#        0     1     2  3  4  5  6 
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Original List is ", l1)

l1.remove(l1[0])
print("After removing 0th element: ", l1)

l1.remove(l1[1])
print("After removing 2nd element: ", l1)

l1.remove(l1[2])
print("After removing 4th element: ", l1)

l1.remove(l1[2])
print("After removing 5th element: ", l1)