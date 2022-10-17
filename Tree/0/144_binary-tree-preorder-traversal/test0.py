# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        stack.append(root)

        while stack:
            curr = stack.pop()
            while curr:
                res.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
                # append right then left
                # after that stack pop in a right sort
        return res


        # res = []
        # def helper(root):
        #     if not root:
        #         return
        #
        #     res.append(root.val)
        #     helper(root.left)
        #     helper(root.right)
        #
        #     return res
        #
        # return helper(root)