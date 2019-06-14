from collections import deque

q = deque()

q.append('a')
q.append('b')
q.append('c')

print(q.popleft())
print(q.popleft())

q.appendleft('d')
q.appendleft('e')
q.appendleft('f')

print(q.pop())
print(q.pop())
