'''
LIFO
stacks can be implemented using
1) lists
2)modulus

'''

'''
# Implementation using lists
stack = []
stack.append(30)
stack.append(40)
stack.append(50)
print(stack)
stack.pop()
stack.pop()

print(stack)
print(len(stack)!=0)
print(not stack == False)
print(stack[-1])
'''


# Implementation using modules
# 1) collections -> deque
# 2)queue -> lifoqueue
#1) collections.deque() {(push,put)(pop,get)}

'''
import collections
stack = collections.deque()
print(stack)
stack.append(30)
stack.append(40)
stack.append(50)
print(stack)
stack.pop()
stack.pop()
print(stack)
stack.pop()
print(not stack)
stack.append(40)
stack.append(50)
print(stack[-1])
'''

'''
import queue
# stack  = queue.LifoQueue()
# stack.put(10)
# stack.put(20)
# stack.put(30)
# while not stack.empty():
#     print(stack.get(), end=" ")
# print(stack.empty())
stack  = queue.LifoQueue(3)
stack.put(10)
stack.put(20)
stack.put(30)
#stack.put(40,timeout=1)
stack.get(timeout=1)
stack.get(timeout=1)
stack.get(timeout=1)
stack.get(timeout=1)
'''
import queue_s
stack  = queue_s.LifoQueue()