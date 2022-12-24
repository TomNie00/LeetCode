class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        row = len(text1)
        col = len(text2)

        dp = [[0] * (col + 1) for i in range(row + 1)]

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[row][col]


if __name__ == '__main__':
    object = Solution()
    text1 = "abcde"
    text2 = "ace"
    print(object.longestCommonSubsequence(text2, text1))
