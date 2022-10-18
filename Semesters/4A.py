# Write a Program that takes two lists and returns true if they have atleast one common element.

L1 = [1, 2 , 3, 4, 5, 6]
L2 = [10, 11, 12, 13, 14, 6]

for i in L1:
    for j in L2:
        if i == j: 
            print(i, " in L1 ", " and ", j, " in L2 are common.")
