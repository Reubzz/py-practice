# Write a program to append text to a file and display. 

def main():
    f = open("E:/Coding/Python Practice/Semesters/text.txt", "a+")
    f.write("Hello World 2")
    f.close()
main()