class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(1, n):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])

        return dp[-1]


if __name__ == '__main__':
    object = Solution()
    nums = [1, 2, 3, 1]
    print(object.rob(nums))
