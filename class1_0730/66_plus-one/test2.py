class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = []
        carry = 0
        is_first = True
        digits.reverse()
        for c in digits:
            if is_first:
                is_first = False
                cur = c + 1
                new_digit = cur % 10
                carry = cur // 10
                ans.append(new_digit)
            else:
                cur = c + carry
                new_digit = cur % 10
                carry = cur // 10
                ans.append(new_digit)

        if carry > 0:
            ans.append(carry)
        ans.reverse()
        return ans