import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # submit accept

        q = collections.deque()
        q.append(root)
        sol = []

        while q:
            size = len(q)
            level_val = []
            while size:
                size -= 1
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                level_val.append(curr.val)

            sol.append(sum(level_val) / len(level_val))

        return sol
