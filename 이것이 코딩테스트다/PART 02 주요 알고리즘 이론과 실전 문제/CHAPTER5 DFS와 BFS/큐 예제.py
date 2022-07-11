# 큐 자료구조를 이용하기 위해 collections 모듈에서 deque를 사용
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# list() 메서드를 활용하여 큐를 리스트로 변환할 수 있음
list = list(queue)
print(list)