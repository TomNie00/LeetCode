import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # submit accept

        res = []
        if not root:
            return res
        q = collections.deque()
        q.append(root)
        left = True


        while q:
            level = []
            size = len(q)
            while size > 0:
                size -= 1
                curr = q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if left:
                res.append(level)
                left = False
            else:
                level.reverse()
                res.append(level)
                left = True
        return res

