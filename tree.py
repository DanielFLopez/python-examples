class Node:
    left, right, value = None, None, 0

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self):
        self.raiz = None

    def addNode(self, value):
        return Node(value)

    def insert(sefl, root, value):
        if root == None:
            return self.addNode(value)
        else:
            if value <= root.value:
                root.left = self.insert(root.left, value)
            else:
                root.right = self.insert(root.right, value)
            return root
