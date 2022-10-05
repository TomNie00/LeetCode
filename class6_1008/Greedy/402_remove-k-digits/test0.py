class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # submit accept
        stack = []

        for i in num:
            while stack and k and int(i) < int(stack[-1]):
                # when stack is not empty and k > 0 and i < stack[-1] then we pop to make the number smaller
                stack.pop()
                k -= 1
            stack.append(i)

        while k:
            # in case the k still > 0
            stack.pop()
            k -= 1

        if stack:
            return str(int("".join(stack)))
        else:
            return '0'


