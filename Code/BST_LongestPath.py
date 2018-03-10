class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, node):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root==None:
            return 0
        heightLeft=self.maxDepth(root.left)
        heightRight=self.maxDepth(root.right)
        return max(heightLeft, heightRight)+1

        # if node == None:
        #     return 0
        #
        # left_height = self.maxDepth(node.left)
        # right_height = self.maxDepth(node.right)
        #
        # return max(right_height + left_height) + 1

