class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # submit accept 
        res = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                # if next day higher than today then buy and sell it next day
                res += prices[i + 1] - prices[i]

        return res
