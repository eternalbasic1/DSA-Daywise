'''

Queues can be implemeted using
1) Lists
2) Modules {(dequeue,collections)
OPERATION - enqueue, dequeue
'''


'''
  
1) LISTS 
method - enqueue:- append
         dequeue :- pop(0)
'''
'''
queue = []
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)
# print(queue.pop(0))
# print(queue)
queue.insert(0,10)
queue.insert(0,20)
queue.insert(0,30)
print(queue)
print(queue.pop())
'''




'''
2) method 
collections ->deque

'''
'''
# import  collections
# q = collections.deque()
# # q.appendleft(10)
# # print(q)
# # q.appendleft(20)
# # print(q)
# # q.appendleft(30)
# # print(q)
# # q.pop()
# # print(q)
# # q.pop()
# # print(q)
#
# q.append(10)
# print(q)
# q.append(20)
# print(q)
# q.append(30)
# print(q)
# q.popleft()
# print(q)
# q.popleft()
# print(q)

'''

'''
2) 
queue -> Queue module

'''


import queue
q = queue.Queue()
q.put(10)
q.put(20)
q.put(30)


