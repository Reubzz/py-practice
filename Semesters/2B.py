# Find lenght of List or String.

def len_s(s):
    count = 0
    for i in s:
        if i != " ":
            count = count + 1
    print("the total length of String in : ", count)

len_s("God is Great")