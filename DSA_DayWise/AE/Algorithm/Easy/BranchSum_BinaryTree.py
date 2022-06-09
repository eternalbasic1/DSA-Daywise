class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
def BranchSums(root):
    sums = []
    CalculateBranchSum(root,0,sums)
    return sums
def CalculateBranchSum(node,runningSum,sums):
    if node is None:
        return
    newrunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newrunningSum)
        return
    CalculateBranchSum(node.left,newrunningSum,sums)
    CalculateBranchSum(node.right,newrunningSum,sums)


#todo: This also works but looks a little bit messy

# def CalculateBranchSum(root,runningsum,sums):
#     newrunnigsum = runningsum + root.value
#     if root.left == None  and root.right == None:
#         sums.append(newrunnigsum)
#         return
#     if root.left:
#         CalculateBranchSum(root.left,sum,sums)
#     if root.right:
#         CalculateBranchSum(root.right,sum,sums)

if __name__ == "__main__":
    binaryTree = Node(1)
    binaryTree.left = Node(2)
    binaryTree.left.left = Node(4)
    binaryTree.left.left.left = Node(8)
    binaryTree.left.left.right = Node(9)
    binaryTree.left.right = Node(5)
    binaryTree.left.right.left = Node(10)
    binaryTree.right = Node(3)
    binaryTree.right.left = Node(6)
    binaryTree.right.right = Node(7)
    print(BranchSums(binaryTree))