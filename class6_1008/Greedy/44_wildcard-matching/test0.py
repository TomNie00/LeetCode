class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        sidx = 0
        pidx = 0


        while sidx < len(s):
            if pidx < len(p) and s[sidx] == p[pidx] or p[pidx] == '?':
                # when the two char is equal or p[idx] is '?' move forward
                sidx += 1
                pidx += 1
            elif pidx < len(p) and p[pidx] == '*':

