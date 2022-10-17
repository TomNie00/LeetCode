# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        # left right root
        # root right left to do reverse
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # submit accept

        # ITERATIVE
        res = []
        stack = []
        stack.append(root)
        curr = None

        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res[::-1]

        # RECURSIVE
        # res = []
        # if not root:
        #     return []
        #
        # def helper(root):
        #     if not root:
        #         return
        #
        #     res.append(root.val)
        #     helper(root.right)
        #     helper(root.left)
        #
        #     return res[::-1]
        # return helper(root)
