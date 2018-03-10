class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def chkBal(root):

            if not root:
                return 0

            left_height = chkBal(root.left)

            if left_height == -1:
                return -1

            right_height = chkBal(root.right)

            if right_height == -1:
                return -1

            if (abs(left_height - right_height) > 1):
                return -1

            return max(left_height, right_height) + 1

        return chkBal(root) != -1