# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(left, right):
            if not left and not right:
                # if left and right are both null
                return True
            if not left or not right:
                # if left or right has one side is null then is not Symmetric Tree
                return False

            return left.val == right.val and helper(left.left, right. right) and helper(left.right, right.left)
        return helper(root.left, root.right)