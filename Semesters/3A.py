# pangram - a sentence that contains all alphabets in english

import string
def isPangram(s):
    alphaset = set(string.ascii_lowercase)
    return alphaset <= set(s.lower())
print(isPangram(input("Sentence :")))