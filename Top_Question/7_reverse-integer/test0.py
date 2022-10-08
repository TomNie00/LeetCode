class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # submit accept
        # s = str(x)
        # stack = []
        # carry = 0
        # res = ''
        #
        # for i in range(len(s)):
        #     if s[i] == '-':
        #         carry = 1
        #     else:
        #         stack.append(s[i])
        #
        # while stack:
        #     res += stack.pop()
        #
        # if carry:
        #     res = int(res) * -1
        #
        # if -2**31 <= int(res) <= 2**31 -1:
        #     return int(res)
        # else:
        #     return 0

        # submit accept
        # faster
        s = str(x)
        limit = 2 ** 31

        if s[0] == '-':
            if int(s[1:][::-1]) > limit:
                # since s[0] is '-' so we need to reverse from s[1] to the end
                return 0
            else:
                return -int(s[1:][::-1])
        else:
            if int(s[::-1]) > limit - 1:
                return 0
            else:
                return int(s[::-1])
