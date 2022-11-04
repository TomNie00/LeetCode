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
        if node is None:
            return 0, 0
        cur_val = node.val
        left_sum, left_tilt = 0, 0

        if node.left is None:
            left_sum, left_tilt = 0, 0
        else:
            left_sum, left_tilt = self.workhorse(node.left)

        right_sum, right_tilt = 0, 0

        if node.right is None:
            right_sum, right_tilt = 0, 0
        else:
            right_sum, right_tilt = self.workhorse(node.right)

        cur_sum = left_sum + right_sum + cur_val
        cur_tilt = left_sum - right_sum

        if cur_tilt < 0:
            cur_tilt = -cur_tilt

        return cur_sum, left_tilt + right_tilt + cur_tilt

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        all_sum, all_tilt_sum = self.workhorse(root)
        return all_tilt_sum
