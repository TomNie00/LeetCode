# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def workhorse(self, node):
        """
        return the sum of cur subtree and the sum of subtree tilts.
        """
        if not node:
            return 0, 0

        curr_val = node.val
        left_sum, left_tilt = 0, 0

        if node.left:
            left_sum, left_tilt = self.workhorse(node.left)

        right_sum, right_tilt = 0, 0

        if node.right:
            right_sum, right_tilt = self.workhorse(node.right)

        curr_sum = left_sum + right_sum + curr_val
        curr_tile = abs(left_sum - right_sum)

        return curr_sum, left_tilt + right_tilt + curr_tile

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        all_sum, all_tilt_sum = self.workhorse(root)
        return all_tilt_sum
