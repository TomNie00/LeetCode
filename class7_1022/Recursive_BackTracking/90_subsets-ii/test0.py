class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # submit accept

        nums.sort()
        res = []

        def helper(idx, curr):
            if idx == len(nums):
                res.append(curr[:])
                return

            curr.append(nums[idx])
            helper(idx + 1, curr)
            curr.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            helper(idx + 1, curr)

        helper(0, [])
        return res