class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root or root.key == key:
            return root
        elif key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            min_larger_node = self._min_value_node(root.right)
            root.key = min_larger_node.key
            root.right = self._delete(root.right, min_larger_node.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)

class AVLNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        # left left
        if balance > 1 and key < root.left.key:
            return self._right_rotate(root)

        # right right
        if balance < -1 and key > root.right.key:
            return self._left_rotate(root)

        # left right
        if balance > 1 and key > root.left.key:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # left right
        if balance < -1 and key < root.right.key:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, root):
        return root.height if root else 0

    def _get_balance(self, root):
        return self._get_height(root.left) - self._get_height(root.right) if root else 0

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)

class RBTNode(Node):
    def __init__(self, key, color='red'):
        super().__init__(key)
        self.color = color
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = RBTNode(key, color='black')
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left:
                self._insert(root.left, key)
            else:
                root.left = RBTNode(key)
                root.left.parent = root
        else:
            if root.right:
                self._insert(root.right, key)
            else:
                root.right = RBTNode(key)
                root.right.parent = root

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append((root.key, root.color))
            self._inorder(root.right, result)

if __name__ == '__main__':
    print("\n BST Test")
    bst = BST()
    for key in [20, 10, 30, 5, 15, 25, 35]:
        bst.insert(key)
    print("BST Inorder Traversal:", bst.inorder())
    print("Search for 15:", bst.search(15) is not None)
    print("Search for 100:", bst.search(100) is not None)
    bst.delete(10)
    print("BST Inorder after deleting 10:", bst.inorder())

    print("\nAVL Tree Test")
    avl = AVLTree()
    for key in [20, 10, 30, 5, 15, 25, 35]:
        avl.insert(key)
    print("AVL Inorder Traversal:", avl.inorder())

    print("\nRed-Black Tree Test")
    rbt = RedBlackTree()
    for key in [20, 10, 30, 5, 15, 25, 35]:
        rbt.insert(key)
    print("RBT Inorder Traversal (with colors):", rbt.inorder())
