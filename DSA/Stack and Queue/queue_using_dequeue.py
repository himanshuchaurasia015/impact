from collections import deque
queue = deque()
queue.append("Rohit")
queue.append(4+8j)
queue.append(5.6)
queue.append(2003)
print(queue)
queue.popleft()
print(queue)
queue.popleft()
queue.popleft()
print(queue)
queue.popleft()
print(queue)