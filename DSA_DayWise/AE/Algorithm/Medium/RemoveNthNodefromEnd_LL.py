'''
#Mycode
# Time O(n) | Space O(1)

class Node:
    def __init__(self,value):
        self.value = value
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    def Insert(self,value):
        if self.head == None:
            self.head = Node(value)
            self.count +=1
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = Node(value)
            self.count +=1
    def printAll(self):
        if self.head == None:
            print("Empty LinkedList")
        else:
            n = self.head
            while n.ref is not None:
                print(f'{n.value} -->', end = ' ')
                n = n.ref
            print(n.value)
    def RemoveFromLast(self,N):
        First = self.head
        Second = self.head
        if N > self.count:
            print("Value Greater than LinkedList")
        elif N == self.count:
            self.head = self.head.ref
            self.count -=1
            return self.printAll()
        else:
            while (N!=0):
                Second = Second.ref
                N-=1
            while(Second.ref!=None):
                First = First.ref
                Second = Second.ref
            First.ref = First.ref.ref
            self.count -= 1
            return self.printAll()
'''


'''
#Mycode is Better Than ALgoexpert.

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next
'''


if __name__ == "__main__":
    LL = LinkedList()
    LL.Insert(10)
    LL.Insert(11)
    LL.Insert(12)
    LL.Insert(13)
    LL.Insert(14)
    LL.Insert(15)
    LL.printAll()
    LL.RemoveFromLast(6)
    LL.RemoveFromLast(5)
    LL.RemoveFromLast(4)
    LL.RemoveFromLast(3)
    LL.RemoveFromLast(2)
    LL.RemoveFromLast(1)