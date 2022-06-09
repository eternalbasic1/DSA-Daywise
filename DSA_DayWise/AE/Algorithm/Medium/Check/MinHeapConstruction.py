class MinHeap:
    def __init__(self,arr):
        self.arr = arr
        self.final = []
        self.BuildHeap()
    def BuildHeap(self):
        for i in self.arr:
            self.Scrutanize(i)
    def Scrutanize(self,value):
        if len(self.final) == 0:
            self.final.append(value)
        else:
            self.final.append(value)
            parentNode = (len(self.final) - 2) // 2
            currentNode = len(self.final)-1
            self.insert(parentNode,currentNode)
    def insert(self,parentNode,currentNode):
        if self.final[parentNode] < self.final[currentNode]:
            return
        else:
            self.shiftUp(parentNode,currentNode)
    def shiftUp(self,parentNode,currentNode):
        while(True):
            if parentNode == 0 and self.final[parentNode] < self.final[currentNode]:
                break
            else:
                self.swap(parentNode,currentNode)
                if parentNode == 0:
                    break
                else:
                    currentNode = parentNode
                    parentNode = (currentNode-1)//2
        return
    def swap(self,currentNode,parentNode):
        self.final[currentNode],self.final[parentNode] = self.final[parentNode],self.final[currentNode]
        return
    def print(self):
        for i in range(len(self.final)):
            print(self.final[i], end=' ')
    def remove(self):
        self.final[0],self.final[-1] = self.final[-1],self.final[0]
        valueToRemove = self.final.pop()
        currentNode = 0
        childNodeOne = 1
        childNodeTwo = 2
        self.shiftDown(currentNode,childNodeOne,childNodeTwo)
        return valueToRemove
    def shiftDown(self,currentNode,childNodeOne,childNodeTwo):
        while True:
            if childNodeOne>len(self.final)-1:
                break
            elif childNodeTwo > len(self.final)-1:
                if self.final[currentNode]>self.final[childNodeOne]:
                    self.swap(currentNode,childNodeOne)
                    break
                else:
                    break
            else:
                if self.final[currentNode]<self.final[childNodeOne] and self.final[currentNode] < self.final[childNodeTwo]:
                    return
                else:
                    if self.final[childNodeOne]<self.final[childNodeTwo]:
                        self.swap(currentNode,childNodeOne)
                        currentNode = childNodeOne
                        childNodeOne = (2*currentNode) + 1
                        childNodeTwo = (2*currentNode) + 2

                    else:
                        self.swap(currentNode,childNodeTwo)
                        currentNode = childNodeTwo
                        childNodeOne = (2 * currentNode) + 1
                        childNodeTwo = (2 * currentNode) + 2
if __name__ == "__main__":
    arr = [102,31,44,17,18,30,23,8,12]
    #arr = [40,50,100,40,15,30,10]
    #8 12 23 17 31 30 44 102 18
    #8 12 23 17 31 44 30 102 18
    result = MinHeap(arr)
    # result.Scrutanize(30)
    # result.Scrutanize(23)
    # result.Scrutanize(8)
    # result.Scrutanize(12)
    result.print()
    print()
    for i in range(9):
        remove_value = result.remove()
        print(remove_value,end=' ')
        # result.print()
        # print()
    result.print()

