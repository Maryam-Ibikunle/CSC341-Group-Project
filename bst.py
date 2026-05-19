class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def search(self, value):
        if self.value == value:
            return True
        if value < self.value:
            if self.left:
                return self.left.search(value)
            return False
        if self.right:
            return self.right.search(value)
        return False

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            successor = self.right
            while successor.left:
                successor = successor.left
            self.value = successor.value
            self.right = self.right.delete(successor.value)
        return self


root = TreeNode(5)
root.insert(3)
root.insert(7)
root.insert(1)
root.insert(4)
root.insert(6)
root.insert(8)
root.insert(2)
root.insert(9)

root.inorder()
root.preorder()
root.postorder()
print(root.search(4))
print(root.search(10))
root.delete(3)
root.inorder()
