import re
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # submit accept

        s = s.strip()
        result = ''
        RE = '^[+-]?[0-9_palindrome-number]+'

        result = re.match(RE,s)
        res = result.group(0)

        if not result:
            return 0
        else:
            return max(-2**31,min(int(res), 2**31-1))
