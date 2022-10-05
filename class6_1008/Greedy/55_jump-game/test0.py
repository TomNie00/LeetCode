class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # submit accept

        right = 0

        for idx, value in enumerate(nums):
            if idx > right:
                # means that we can not arrive this index
                return False
            else:
                right = max(right, idx + value)
        #         update the new right that we can arrival

        return True
