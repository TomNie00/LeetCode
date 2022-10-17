# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # submit accept

        def generateBSTrees(start, end):

            if start > end:
                return [None]

            res = []

            for i in range(start, end+1):
                # set i as root and generate left and right
                left_subtree = generateBSTrees(start, i - 1 )
                right_subtree = generateBSTrees(i + 1, end)

                for l in left_subtree:
                    for r in right_subtree:
                        # have to put the generate treenode into res
                        cur_subtree = TreeNode(i)
                        cur_subtree.left = l
                        cur_subtree.right = r
                        res.append(cur_subtree)
            return res

        return generateBSTrees(1,n) if n else [0]
