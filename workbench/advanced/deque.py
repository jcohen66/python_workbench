# use deque as stack
from collections import deque
q = deque()
q.append('first')
q.append('second')
q.append('third')

print(q)
print(q.pop())
print(q.pop())
print(q.pop())
print(q)

