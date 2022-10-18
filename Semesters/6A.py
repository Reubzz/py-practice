# Write a program to read a text file

def file_read(fname):
    txt = open(fname)
    print(txt.read())

file_read("E:/Coding/Python Practice/Semesters/text.txt")