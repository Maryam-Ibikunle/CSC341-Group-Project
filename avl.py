class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def getHeight(self, node):
        return node.height if node else 0

    def getBalance(self):
        return self.getHeight(self.left) - self.getHeight(self.right)

    def updateHeight(self):
        self.height = 1 + max(self.getHeight(self.left), self.getHeight(self.right))

    def rightRotate(self):
        x = self.left
        t2 = x.right

        x.right = self
        self.left = t2

        self.updateHeight()
        x.updateHeight()

        return x

    def leftRotate(self):
        y = self.right
        t2 = y.left

        y.left = self
        self.right = t2

        self.updateHeight()
        y.updateHeight()

        return y

    def insert(self, key):
        if key < self.key:
            if self.left:
                self.left = self.left.insert(key)
            else:
                self.left = AVLNode(key)
        elif key > self.key:
            if self.right:
                self.right = self.right.insert(key)
            else:        
                self.right = AVLNode(key)
        else:
            return self

        self.updateHeight()
        balance = self.getBalance()

        if balance > 1 and key < self.left.key:
            return self.rightRotate()

        if balance < -1 and key > self.right.key:
            return self.leftRotate()

        if balance > 1 and key > self.left.key:
            self.left = self.left.leftRotate()
            return self.rightRotate()

        if balance < -1 and key < self.right.key:
            self.right = self.right.rightRotate()
            return self.leftRotate()

        return self

    def getMin(self):
        if self.left is None:
            return self
        return self.left.getMin()

    def inorder(self):
        result = []
        if self.left:
            result += self.left.inorder()
        result.append(self.key)
        if self.right:
            result += self.right.inorder()
        return result

    def preorder(self):
        result = [self.key]
        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result

    def postorder(self):
        result = []
        if self.left:
            result += self.left.postorder()
        if self.right:
            result += self.right.postorder()
        result.append(self.key)
        return result

if __name__ == "__main__":
    root = AVLNode(10)
    
    for num in [20, 30, 40, 50, 60, 70, 80, 90, 100]:
        root = root.insert(num)
        
    print(root.inorder())
    print(root.preorder())
    print(root.postorder())
    print(root.getMin().key)