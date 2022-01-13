'''

We can implement priority queue in 2ways
1) Lists
2) Priority Queue ->queue module

'''
'''
# Using Lists

q = []
q.append(10)
q.append(20)
q.append(30)
q.sort()
print(q)
q.pop(0)
print(q)
q.pop(0)
print(q)
q.pop(0)
'''

# Using Priority Queue
# from queue module initialize priority queue
import queue
q = queue.PriorityQueue()
q.put(10)
q.put(20)
q.put(30)
print(q)
q.get()
q.get()

