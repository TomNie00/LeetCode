class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        dp = [0] * n
        minprice = prices[0]

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]

        # n = len(prices)
        # dp = [0] * n
        #
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         dp[i] = max(dp[i], prices[j] - prices[i])
        #
        # return max(dp)


if __name__ == '__main__':
    object = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(object.maxProfit(prices))

    object = Solution()
    prices = [7, 6, 4, 3, 1]
    print(object.maxProfit(prices))
