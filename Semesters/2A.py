def find_vowel(s):
    list = [ 'a', 'e', 'i', 'o', 'u' ]
    for i in s:
        if i in list:
            print("True")
        else:
            print("False")

find_vowel("God is Great")