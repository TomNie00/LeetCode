# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # submit accept

        def helper(root, left_sub, right_sub):
            # we need to keep left_sub < root.val < right_sub
            if not root:
                # if root is none also True
                return True

            if not (right_sub < root.val < left_sub):
                return False

            return helper(root.left, left_sub, root.val) and helper(root.right, root.val, right_sub)
            # for the left subtree we just upadte the right_sub since we have to keep root.left is less than root
            # for the right subtree we just upadte the left_sub since we have to keep root.right is greater than root

        return helper(root, float("-inf"), float("inf"))
