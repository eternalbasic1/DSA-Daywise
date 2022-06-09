class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self,value):
        currentNode = self
        if currentNode.value == None:
            currentNode.value = value
            return self
        while True:
            if value < currentNode.value:
                if currentNode.left:
                    currentNode = currentNode.left
                else:
                    currentNode.left = BST(value)
                    break
            else:
                if currentNode.right:
                    currentNode = currentNode.right
                else:
                    currentNode.right = BST(value)
                    break
        return self
    def contains(self,value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False
    def remove(self,value , parentNode = None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getminvalue()
                    currentNode.right.remove(currentNode.value,currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.left = currentNode.left.left
                        currentNode.right = currentNode.left.right
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.right if currentNode.right is not None else currentNode.left
                break
        return self
    def getminvalue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
    def preorder(self):
        print(self.value,end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        
if __name__ == "__main__":
    BinarySearchTree = BST(None)
    arr = [10,11,12,13,14,15]
    for i in arr:
        BinarySearchTree.insert(i)
    BinarySearchTree.preorder()
    BinarySearchTree.remove(10)
    print()
    BinarySearchTree.preorder()
