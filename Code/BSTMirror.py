class Node:
    # Utility function to create new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    " * depth) + str(self.key)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret

def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        if root1.key == root2.key:
            return (isMirror(root1.right, root2.left) and isMirror(root2.right, root1.left))

    return False

def isSymmetric(root):
    return isMirror(root, root)


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)



print(root)
print(isSymmetric(root))