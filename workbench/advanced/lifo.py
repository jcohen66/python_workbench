# use lifo queue as a stack
from queue import LifoQueue

q = LifoQueue()
q.put('first')
q.put('second')
q.put('third')

print(q)
print(q.get_nowait())
print(q.get_nowait())
print(q.get_nowait())
print(q)
