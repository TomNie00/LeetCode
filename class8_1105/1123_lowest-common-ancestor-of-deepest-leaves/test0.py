# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # submit accept

        return self.workhorse(root, 0)[0]

    def workhorse(self, root, depth):
        if not root:
            return root, 0
        if not root.left and not root.right:
            return root, depth

        left_node, left_depth = self.workhorse(root.left, depth + 1)
        right_node, right_depth = self.workhorse(root.right, depth + 1)

        if left_depth == right_depth:
            return root, left_depth
        elif left_depth > right_depth:
            return left_node, left_depth
        else:
            return right_node, right_depth
