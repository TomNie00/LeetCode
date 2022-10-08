class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # submit accept

        num = str(x)

        return num == num[::-1]


        # submit accept but slower
        # if x < 0:
        #     return False
        #
        # oldnum = x
        # num = 0
        # while x > 0:
        #     num = num * 10 + x % 10
        #     x = x // 10
        #
        # return oldnum == num
