# Sort ascending or decending a dictionary by value. 

# Code :
from platform import release


released = {
    'Python 3.6': "2017",
    'Python 1.0': "2002",
    'Python 2.3': "2010"
}
print("Orginal dictionary is ", released)
print("Dictionary in ascending order by value : ")


for key, value in sorted(released.items()):
    print(key, value)

print("Dictionary in decending order by value: ")
for key, value in sorted(released.items(), reverse=True):
    print(key, value)
