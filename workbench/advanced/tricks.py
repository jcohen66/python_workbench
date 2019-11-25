# checking if strings are anagrams
from collections import Counter
def new_anagram(word1, word2, word3):
    return Counter(word1) == Counter(word2) == Counter(word3)

print(new_anagram('Hi', 'Hi', 'Hi'))
print(new_anagram('Hi', 'New', 'Hi'))
print(new_anagram('New', 'New', 'New'))


# swapping numbers
a = 10
b = 20
print(a, b)
a, b = b, a 
print(a, b)

# reversing a string
s = 'HiString!'
print('Reversed string is: ', s[::-1])

# single string from a list
new_list = ['first', 'second', 'third']
print("|".join(new_list))

# comparison operator trick
i = 5
result = 1 < i < 10
print(result)
result = 1 > i <= 4
print(result)

# file path
import os 
import socket

# display the modules
print(os)
print(socket)

# enums
class NewName:
    Python, Is, Fun = range(3)
    
print(NewName.Python)
print(NewName.Is)
print(NewName.Fun)

# function for multi values
def floostec():
    return 1, 2, 3, 4, 5

u, v, w, x, y = floostec()
print(u, v, w, x, y)

# frequent values in a list
numbers = [1, 2, 2, 5, 4, 5, 3, 5, 6, 7, 7]
print(max(set(numbers), key = numbers.count))

# memory for object
import sys
a = 1
print(sys.getsizeof(a))

# string many times
x = 5
y = "HiThere! "
print(y * x)


# zip built-in
keys = ['x', 'y', 'z']
values = [1, 2, 10]
comp1 = dict(zip(keys, values))
print(comp1)

#uuid
import uuid
userid = uuid.uuid4()
print(userid)
