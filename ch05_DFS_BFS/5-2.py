# 5-2.py 큐 예제

from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
a1 = queue.popleft()
queue.append(1)
queue.append(4)
a2 = queue.popleft()

print(queue)
print(a1, a2)
queue.reverse()
print(queue)