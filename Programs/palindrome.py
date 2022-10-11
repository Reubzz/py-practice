num = int(input("Enter a value:")) # input
temp = num 
rev = 0

while(temp > 0): # Checking if num is greater than 0
    digit = temp % 10 # Using modulus to get only the last digit
    rev = rev * 10 + digit # Reversing 
    temp //= 10 # Dividing by 10 to remove last digit
if(num == rev):
    print("This value is a palindrome number!")
else:
    print("This value is not a palindrome number!")