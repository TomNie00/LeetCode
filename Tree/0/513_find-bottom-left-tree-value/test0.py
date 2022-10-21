import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # submit accept

        # DFS
        res = []
        level = 0
        def helper(root, res, level):
            if not root:
                return None
            if level == len(res):
                res.append([])
            res[level].append(root.val)

            helper(root.left, res, level + 1)
            helper(root.right, res, level + 1)
            return res[-1][0]
        return helper(root,res,level)


        # BFS
        # q = collections.deque()
        # q.append(root)
        # level = []
        # while q:
        #     level = []
        #     size = len(q)
        #     while size > 0:
        #         size -= 1
        #         curr = q.popleft()
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)
        #         level.append(curr.val)
        #
        # return level[0]
