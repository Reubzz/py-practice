# Create a Program that ask the user to enter their name and their age. Print out a message that tells
# them the year that they will turn 100 years old.

# Code 

import datetime
name = str(input('Enter your Name : '))
print("Hello", name)
age = int(input("Enter your Age : "))
year_now = datetime.datetime.now()
print("You will turn 100 years old in the year " + str((100 - age) + year_now.year))