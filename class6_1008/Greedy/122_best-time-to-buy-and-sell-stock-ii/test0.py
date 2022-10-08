class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # submit accept
        # res = 0
        # for i in range(len(prices) - 1):
        #     if prices[i + 1] > prices[i]:
        #         # if next day higher than today then buy and sell it next day
        #         res += prices[i + 1] - prices[i]
        #
        # return res

        # submit accept
        # faster
        res = 0
        pre = 0
        count = len(prices)

        for i in range(count):
            if i + 1 < count:
                if prices[i] > prices[i + 1]:
                    res += prices[i] - prices[pre]
                    pre = i + 1
            else:
                if prices[i] >= prices[i - 1]:
                    # consider the [1, 2, 9. 9] and [1, 2, 9]
                    res += prices[i] - prices[pre]

        return res


if __name__ == '__main__':
    object = Solution()
    # prices = [7,1,5,3,6,4]
    # prices = [1,2,3,4,5]
    # prices = [6,1,3,2,4,7]
    prices = [1, 9, 6, 9, 1, 7, 1, 1, 5, 9, 9, 9]

    res = object.maxProfit(prices)

    print(res)
