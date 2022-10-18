# write a program to reverse a number.

def rev_num(num):
    rev = 0
    while num > 0:
        rev = (rev * 10) + num % 10
        num = num // 10
    print("The Reverse is : ", rev)   
rev_num(5144)