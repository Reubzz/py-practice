num = int(input("Enter a number: "))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10 # Using modulus to get only the last digit
    sum += digit ** 3 # Cubing the last digit 
    temp //= 10 # Dividing by 10 to remove last digit

# Res
if num == sum:
    print(num," is an Armstrong number.")
else:
    print(num," is not an Armstrong number.")