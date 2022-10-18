# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. 

# code: 

def histogram(inputList):
    for i in range(len(inputList)):
        print(inputList[i] * "*")

histogram([ 4, 7, 2, 5, 1])