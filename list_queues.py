from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
print(queue)
queue.append("Graham")          
queue.popleft()                 
'Eric'
queue.popleft()                 
'John'
queue                           
deque(['Michael', 'Terry', 'Graham'])
print(queue)
