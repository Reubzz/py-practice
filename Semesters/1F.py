# Recursive Function - Factorial of a number. 

def factorial(n):
    if n == 1: 
        return n
    else:
        return n * factorial(n-1)

num = int(input("Enter a Number : "))
if(num < 0):
    print("Factorial of Negative number is not possible.")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of ", num, " is ", factorial(num))