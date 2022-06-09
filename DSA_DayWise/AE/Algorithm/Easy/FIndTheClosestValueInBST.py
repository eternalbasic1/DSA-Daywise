class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


# IT is very important to write return in line 17 return FindTheClosestValueHelper(node.left,closestValue,value) if not it will return None

# def findClosestValueInBst(root,value):
#     return FindTheClosestValueHelper(root,float('inf'),value)
# def FindTheClosestValueHelper(node,closestValue,value):
#     if node is None:
#         return closestValue
#     if abs(node.value-closestValue)>abs(node.value-value):
#         closestValue = node.value
#     if node.value>value:
#         return FindTheClosestValueHelper(node.left,closestValue,value)
#     elif node.value<value:
#         return FindTheClosestValueHelper(node.right,closestValue,value)
#     else:
#         return closestValue

#algoexpert code ❤💕 Recursive Way


# def findClosestValueInBst(tree,target):
#     return findClosestValueInBstHelper(tree,target,float("inf"))
# def findClosestValueInBstHelper(tree,target,closest):
#     if tree is None:
#         return closest
#     if abs(target-closest) > abs(target-tree.value):
#         closest = tree.value
#     if target  < tree.value:
#         return findClosestValueInBstHelper(tree.left,target,closest)
#     elif target > tree.value:
#         return findClosestValueInBstHelper(tree.right,target,closest)
#     else:
#         return closest

# algoexpert code ❤💕 Iterative way
def findClosestValueInBst(tree,target):
    return findClosestValueInBstHelper(tree,target,float("inf"))
def findClosestValueInBstHelper(tree,target,closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target-closest) > abs(target-currentNode.value):
            closest = currentNode.value
        if target  < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

if __name__ == "__main__":
    binaryTree = Node(10)
    binaryTree.left = Node(5)
    binaryTree.left.left = Node(2)
    binaryTree.left.left.left = Node(1)
    binaryTree.left.right = Node(5)
    binaryTree.right = Node(15)
    binaryTree.right.left = Node(13)
    binaryTree.right.right = Node(22)
    binaryTree.right.left.right = Node(14)
    print(findClosestValueInBst(binaryTree,12))