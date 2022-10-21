# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # submit accept

        def helper(root):
            if not root:
                return [0,0]

            left_pair = helper(root.left)
            right_pair = helper(root.right)

            withroot = root.val + left_pair[1] + right_pair[1]
            withoutroot = max(left_pair) + max(right_pair)

            return [withroot, withoutroot]

        return max(helper(root))