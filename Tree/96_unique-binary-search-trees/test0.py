# class TreeNode(object):
#     def __init__(self,,val = 0, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        visit = {}

        def helper(start, end):
            if start < 1 or end > n or start > end:
                return 1

            total = 0
            if (start, end) in visit:
                return visit[(start, end)]
            else:
                for i in range(start, end+1):
                    total += helper(start, i - 1) * helper(i + 1, end)
                visit[(start, end)] = total
                return total

        helper(1, n)
