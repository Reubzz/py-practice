# write a program to display the Fibonacci Sequence up to n-th term where n is provided by the user

n = int(input("Hows many terms : "))

x = 0
y = 1 
sum = 0

if n <= 0:
    print("Please enter a non-zero positive number.")
elif n == 1:
    print("The fibonacci series of 1 is ", x)
else: 
    count = 0
    print("The fibonacci series upto", n, " is :")
    while count < n:
        print(sum)
        x = y
        y = sum
        sum = x + y
        count = count + 1
