#Iterative
def inOrder(root):
    stack = []
    res = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            new_node = stack.pop()
            res.append(new_node.val)
            root = new_node.right

#Recursive
def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root)
        inOrderTraversal(root.right)
