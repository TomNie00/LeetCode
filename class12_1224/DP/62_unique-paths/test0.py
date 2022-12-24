class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0] * n for i in range(m)]

        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row][col - 1] + dp[row - 1][col]

        return dp[m-1][n-1]


if __name__ == '__main__':
    object = Solution()
    m = 3
    n = 7
    print(object.uniquePaths(m,n))

    object1 = Solution()
    m = 3
    n = 2
    print(object1.uniquePaths(m, n))