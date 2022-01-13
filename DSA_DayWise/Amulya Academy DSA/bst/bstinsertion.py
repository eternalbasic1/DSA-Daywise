class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
         if self.key is None:
             self.key = data
             return
         if self.key == data:
             return
         if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
         if self.key > data:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

root = BST(30)

root.insert(10)
root.insert(9)
root.insert(35)
