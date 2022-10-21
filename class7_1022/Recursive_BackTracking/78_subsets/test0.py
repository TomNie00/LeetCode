class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # submit accept

        res = []

        def helper(nums, curr):
            res.append(curr[:])
            for i in range(len(nums)):
                helper(nums[i + 1:], curr + [nums[i]])

        helper(nums, [])
        return res