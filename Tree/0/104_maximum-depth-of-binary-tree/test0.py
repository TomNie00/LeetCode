import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # submit accept

        # RECURSIVE
        if not root:
            return 0

        return 1 + max((self.maxDepth(root.left), self.maxDepth(root.right)))

        # ITERATION
        # q = collections.deque()
        # q.append(root)
        # level = 0
        # if not root:
        #     return level
        #
        # while q:
        #     size = len(q)
        #     while size > 0:
        #         size -= 1
        #         curr = q.popleft()
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)
        #     level += 1
        # return level