class Node:
    left, right, value = None, None, 0

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self):
        self.root = None

    def addNode(self, value):
        return Node(value)

    def insert(self, root, value):
        if root == None:
            print("was added to root")
            root = self.addNode(value)
        else:
            if value <= root.value:
                print("added to left")
                root.left = self.insert(root.left, value)
            else:
                print("added to right")
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

    def inorder(self, node):
        if node == None:
            return None
        else:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

    def preorder(self, node):
        if node == None:
            return None
        else:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node == None:
            return None
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)

    def height(self, node):
        height = 0
        if node == None:
            return height
        else:
            left = self.height(node.left)
            right = self.height(node.right)
            print("value left: ", left, "value right: ", right)
            if left > right:
                height = left + 1
            else:
                height = right + 1
        return height




tree = BinaryTree()
tree.root = tree.insert(tree.root, 15)
tree.root = tree.insert(tree.root, 7)
tree.root = tree.insert(tree.root, 5)
tree.root = tree.insert(tree.root, 10)
tree.root = tree.insert(tree.root, 4)
tree.root = tree.insert(tree.root, 6)
tree.root = tree.insert(tree.root, 18)
tree.root = tree.insert(tree.root, 35)
tree.root = tree.insert(tree.root, 16)
tree.root = tree.insert(tree.root, 47)
tree.root = tree.insert(tree.root, 29)
tree.root = tree.insert(tree.root, 20)
tree.root = tree.insert(tree.root, 68)
tree.root = tree.insert(tree.root, 19)

print("tree root: ", tree.root)

print("---------------- Search ---------------------------------------------")
print(tree.search(6, tree.root))

# left -> root -> right
print("---------------- Inorder search -------------------------------------")
print(tree.inorder(tree.root))

# root -> left -> right
print("---------------- Preorder search ------------------------------------")
print(tree.preorder(tree.root))

# left -> right -> root
print("---------------- Postorder search -----------------------------------")
print(tree.postorder(tree.root))

# height
print("---------------- height tree ----------------------------------------")
print(tree.height(tree.root))


tree2 = BinaryTree()
tree2.root = tree2.insert(tree2.root, 3)
tree2.root = tree2.insert(tree2.root, 1)
tree2.root = tree2.insert(tree2.root, 4)
tree2.root = tree2.insert(tree2.root, 2)

print("---------------- height tree2 ---------------------------------------")
print(tree2.height(tree2.root))
