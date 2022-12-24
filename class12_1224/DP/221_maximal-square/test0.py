class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for i in range(rows)]

        for i in range(rows):
            dp[i][0] = int(matrix[i][0])
        for y in range(cols):
            dp[0][y] = int(matrix[0][y])

        for row in range(1, rows):
            for col in range(1, cols):
                if int(matrix[row][col]) == 1:
                    dp[row][col] = min(dp[row][col - 1], dp[row - 1][col],
                                       dp[row - 1][col - 1]) + 1

        return max(map(max, dp)) ** 2


if __name__ == '__main__':
    object = Solution()
    matrix = [["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["0", "0", "1", "1", "1"]]

    print(object.maximalSquare(matrix))

    # object1 = Solution()
    # matrix = [["0", "1"], ["1", "0"]]
    # print(object1.maximalSquare(matrix))
    #
    # object2 = Solution()
    # matrix = [["0"]]
    # print(object2.maximalSquare(matrix))
    #
    # object2 = Solution()
    # matrix = []
    # print(object2.maximalSquare(matrix))
