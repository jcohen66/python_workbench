# Use list as stack
s = []
s.append('first')
s.append('second')
s.append('third')

print(s)
print(s.pop())
print(s.pop())
print(s.pop())

# if you go beyond the bounds you raise an IndexError exception
try:
    print(s.pop())
except IndexError:
    print('Nothing more to pop.')