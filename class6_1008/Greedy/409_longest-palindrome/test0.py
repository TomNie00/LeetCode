import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # submit accept

        counter = collections.Counter(s)
        res = 0
        odd = 0

        for c, value in counter.items():
            if value % 2 == 1:
                # this value is odd
                res += value - 1
                odd = 1
                # exist a character could be place in the middle at the end
            else:
                # this value is even
                res += value

        return res + odd
