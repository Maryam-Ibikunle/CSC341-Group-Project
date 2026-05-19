class BPlusNode:
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.children = []
        self.leaf = True
        self.next = None

    def split(self):
        mid = len(self.keys) // 2
        sibling = BPlusNode(self.order)
        sibling.leaf = self.leaf
        sibling.next = self.next
        self.next = sibling

        if self.leaf:
            sibling.keys = self.keys[mid:]
            sibling.children = self.children[mid:]
            self.keys = self.keys[:mid]
            self.children = self.children[:mid]
            return sibling.keys[0], sibling
        else:
            promote = self.keys[mid]
            sibling.keys = self.keys[mid + 1 :]
            sibling.children = self.children[mid + 1 :]
            self.keys = self.keys[:mid]
            self.children = self.children[: mid + 1]
            return promote, sibling


class BPlusTree:
    def __init__(self, order=4):
        self.order = order
        self.root = BPlusNode(order)

    def _find_leaf(self, key):
        node = self.root
        while not node.leaf:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            node = node.children[i]
        return node

    def search(self, key):
        leaf = self._find_leaf(key)
        return key in leaf.keys

    def insert(self, key, value=None):
        leaf = self._find_leaf(key)
        i = 0
        while i < len(leaf.keys) and key > leaf.keys[i]:
            i += 1
        leaf.keys.insert(i, key)
        leaf.children.insert(i, value)

        if len(leaf.keys) >= self.order:
            self._split_up(leaf)

    def _split_up(self, node):
        promote_key, sibling = node.split()

        if node == self.root:
            new_root = BPlusNode(self.order)
            new_root.leaf = False
            new_root.keys = [promote_key]
            new_root.children = [node, sibling]
            self.root = new_root
            return

        parent = self._find_parent(self.root, node)
        i = parent.children.index(node)
        parent.keys.insert(i, promote_key)
        parent.children.insert(i + 1, sibling)

        if len(parent.keys) >= self.order:
            self._split_up(parent)

    def _find_parent(self, current, target):
        if current.leaf or target in current.children:
            return current
        for child in current.children:
            if not child.leaf:
                result = self._find_parent(child, target)
                if result:
                    return result
        return None

    def range_query(self, start, end):
        leaf = self._find_leaf(start)
        result = []
        while leaf:
            for key in leaf.keys:
                if start <= key <= end:
                    result.append(key)
                elif key > end:
                    return result
            leaf = leaf.next
        return result


bpt = BPlusTree(order=4)
keys = [5, 15, 25, 35, 45, 10, 20, 30]
for k in keys:
    bpt.insert(k)

print("B+ Tree Demo")
print("Inserted:", keys)
print("Search 15:", bpt.search(15))
print("Search 99:", bpt.search(99))
print("Range query 10-30:", bpt.range_query(10, 30))
print("Range query 1-50:", bpt.range_query(1, 50))
