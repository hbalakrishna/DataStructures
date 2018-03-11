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

def minDepth(root):
    if root == None:
        return 0
    heightLeft = minDepth(root.left)
    heightRight = minDepth(root.right)
    if root.left == None or root.right == None:
        return minDepth(root.left) + minDepth(root.right) + 1
    return 1 + min(heightLeft, heightRight)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root = Node(0)
# root.left = Node(1)


print(root)
print(minDepth(root))