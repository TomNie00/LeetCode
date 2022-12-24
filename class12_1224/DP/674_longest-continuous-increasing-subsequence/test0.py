class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1

        return max(dp)


if __name__ == '__main__':
    object = Solution()
    nums = [1, 3, 5, 4, 7]
    print(object.findLengthOfLCIS(nums))

    object1 = Solution()
    nums = [2, 2, 2, 2, 2]
    print(object1.findLengthOfLCIS(nums))