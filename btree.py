class BTreeNode:
    def __init__(self, t, leaf=True):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []

    def insert(self, key):
        if len(self.keys) == (2 * self.t) - 1:
            s = BTreeNode(self.t, False)
            s.children.append(self)
            s.split_child(0)
            s.insert_non_full(key)
            return s
        else:
            self.insert_non_full(key)
            return self

    def insert_non_full(self, key):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == (2 * self.t) - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t - 1)]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.children = y.children[t: 2 * t]
            y.children = y.children[0: t]

    def getMin(self):
        curr = self
        while not curr.leaf:
            curr = curr.children[0]
        return curr.keys[0] if curr.keys else None

    def inorder(self):
        result = []
        for i in range(len(self.keys)):
            if not self.leaf:
                result += self.children[i].inorder()
            result.append(self.keys[i])
        if not self.leaf:
            result += self.children[-1].inorder()
        return result

    def preorder(self):
        result = self.keys.copy()
        if not self.leaf:
            for child in self.children:
                result += child.preorder()
        return result

    def postorder(self):
        result = []
        if not self.leaf:
            for child in self.children:
                result += child.postorder()
        result += self.keys.copy()
        return result

if __name__ == "__main__":
    root = BTreeNode(2)
    
    for num in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        root = root.insert(num)
        
    print(root.inorder())
    print(root.preorder())
    print(root.postorder())
    print(root.getMin())
