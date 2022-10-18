def lastNLines(fname, n):
    with open(fname) as file:
        for line in (file.readlines()[-n:]):
            print(line, end = " ")
lastNLines("E:/Coding/Python Practice/Semesters/text.txt", 1)