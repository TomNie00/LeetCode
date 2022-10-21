class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # submit accept

        res = []
        curr = []

        def helper(idx):
            if idx >= len(s):
                # after go over it one time we append what we have in the curr into res
                res.append(curr[:])
                return

            for j in range(idx, len(s)):
                if self.Palindrome(s, idx, j):
                    # if s[idx:j] is Palindrome then append it into curr
                    curr.append(s[idx:j + 1])
                    helper(j + 1)
                    # do j+1 to find next
                    curr.pop()

        helper(0)
        return res

    def Palindrome(self, s, left, right):
        # consider if this s[left:right] is Palindrome
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
