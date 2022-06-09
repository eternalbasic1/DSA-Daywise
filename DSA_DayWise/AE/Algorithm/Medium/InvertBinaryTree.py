#Iterative
'''
# time O(n) | space O(n) or 2^d as dept => number of nodes in a depth will be max
class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def preOrder(self):
        print(self.value,end=" ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapleftandright(current)
        queue.append(current.left)
        queue.append(current.right)
def swapleftandright(tree):
    tree.right,tree.left = tree.left ,tree.right
if __name__ == "__main__":
    bst = BST(10)
    bst.left = BST(5)
    bst.right = BST(15)
    bst.left.left = BST(3)
    bst.left.right = BST(8)
    bst.right.left = BST(13)
    bst.right.right = BST(18)
    bst.preOrder()
    print()
    invertBinaryTree(bst)
    bst.preOrder()
'''

#Recursive Way
'''
# time O(n) | space O(d) depth
class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def preOrder(self):
        print(self.value,end=" ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

def InvertBinaryTree(tree):
    if tree is None:
        return
    swapleftandright(tree)
    InvertBinaryTree(tree.left)
    InvertBinaryTree(tree.right)

def swapleftandright(tree):
    tree.left,tree.right = tree.right,tree.left


if __name__ == "__main__":
    bst = BST(10)
    bst.left = BST(5)
    bst.right = BST(15)
    bst.left.left = BST(3)
    bst.left.right = BST(8)
    bst.right.left = BST(13)
    bst.right.right = BST(18)
    bst.preOrder()
    print()
    InvertBinaryTree(bst)
    bst.preOrder()
'''