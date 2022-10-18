# Armstrong Number 

def armstrong(num):
    temp = num
    sum = 0
    while temp > 0:
        sum = sum + ((temp % 10) ** 3)
        temp = temp // 10
    
    if num == sum:
        print("It is a Armstrong Number")
    else:
        print("It is not a Armstrong Number")

def palindrome(num):
    temp = num
    sum = 0
    while temp > 0:
        sum = (sum * 10) + (temp % 10)
        temp = temp // 10
    
    if num == sum:
        print("It is a Palindrome number.")
    else:
        print("It is Not a Palindrome number.")

palindrome(512)
palindrome(515)
armstrong(530)
armstrong(153)