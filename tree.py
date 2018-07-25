class Node:
    left, right, value = None, None, 0

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def addNode(self, value):
        return Node(value)

    def insert(self, root, value):
        if root == None:
            return self.addNode(value)
        else:
            if value <= root.value:
                root.left = self.insert(root.left, value)
            else:
                root.right = self.insert(root.right, value)
            return root

    def search(self, value, node):
        print("searching: ", value, " in: ", node)
        if node == None:
            return None
        else:
            if value == node.value:
                return node.value
            else:
                if value < node.value:
                    return self.search(value, node.left)
                else:
                    return self.search(value, node.right)

tree = BinaryTree()
tree.insert(tree.root, 15)
tree.insert(tree.root, 10)
tree.insert(tree.root, 7)
tree.insert(tree.root, 4)
tree.insert(tree.root, 1)
tree.insert(tree.root, 18)
tree.insert(tree.root, 24)
tree.insert(tree.root, 35)
tree.insert(tree.root, 47)
tree.insert(tree.root, 89)
tree.insert(tree.root, 78)
tree.insert(tree.root, 68)


print("---------------- Busqueda ---------------------------------------------")
print(tree.search(68, tree.root))
