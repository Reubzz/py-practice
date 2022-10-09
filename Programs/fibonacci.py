def fib(n):
    a = 0
    b = 1
    c = 0
    if n == 1:
        print(a)
    else:
        # print(a)
        # print(b)
        for i in range(0,n):
            print(c)
            a = b
            b = c
            c = a + b
num = int(input("How many numbers do you want : "))
fib(num)