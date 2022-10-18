# take a list and print out all the elements that are less than 5. 

L1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
L2 = []
for i in L1:
    if i < 5: 
        L2.append(i)

print(L2)