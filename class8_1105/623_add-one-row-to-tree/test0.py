# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        # submit accept

        if depth == 1:
            return TreeNode(val, root)
        else:
            return self.workhorse(root, val, depth - 1, 1)

    def workhorse(self, root, val, depth, curr_level):

        if not root:
            return

        if curr_level == depth:
            root.left = TreeNode(val, root.left)
            root.right = TreeNode(val, root.right)

        self.workhorse(root.left, val, depth, curr_level + 1)
        self.workhorse(root.right, val, depth, curr_level + 1)

        return root
