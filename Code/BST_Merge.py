def mergeTrees(self, t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """

    if t1 and t2:
        t3 = TreeNode(t1.val + t2.val)
        t3.left = self.mergeTrees(t1.left, t2.left)
        t3.right = self.mergeTrees(t1.right, t2.right)
    elif t1:
        t3 = TreeNode(t1.val)
        t3.left = self.mergeTrees(t1.left, None)
        t3.right = self.mergeTrees(t1.right, None)
    elif t2:
        t3 = TreeNode(t2.val)
        t3.left = self.mergeTrees(None, t2.left)
        t3.right = self.mergeTrees(None, t2.right)
    else:
        t3 = None

    return t3