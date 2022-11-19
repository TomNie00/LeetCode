# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def workhorse(root, res):
            if not root:
                return

            workhorse(root.left, res + 1)
            workhorse(root.right, res + 1)

            return res

        return workhorse(root, 0)


