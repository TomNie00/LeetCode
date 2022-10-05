class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # submit accept

        # two conditions
        # first is 'aba'
        # second is 'abba'

        result = ''
        first = ''
        second = ''

        for i in range(len(s)):
            first = self.check_longest_palindrome(s, i, i)
            # first condition start left and right position is itself then move left to left, right to right
            firstlen = len(first)

            if firstlen > len(result):
                # if the first length is bigger than the result then update the substring
                result = first

            second = self.check_longest_palindrome(s, i, i + 1)
            # second condition start left from itself, start right from next right
            secondlen = len(second)

            if secondlen > len(result):
                # if the second length is bigger than the result then update the substring
                result = second

        return result

    def check_longest_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # make sure the left and right not out of range and check left == right
            left -= 1
            right += 1
            # then move left to left and right to right

        return s[left + 1: right]

