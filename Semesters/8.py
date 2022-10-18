# Write a Program to implement exception handling 

import sys
randomList = ['a', 2, 0]

for entry in randomList:
    try:
        print("The entry is ", entry)
        r = 1 / int(entry)
        break
    except: 
        print("Oos!! ", sys.exc_info()[0], "Occured")
        print("next entity")
        print()

print('The reciprocal of ', entry, " is ", r)