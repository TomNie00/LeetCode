class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = []
        carry = 0
        digits.reverse()
        # print(digits)
        for i in range(len(digits)):
            if i == 0:
                current_digit = digits[i]+1
                if digits[i] == 9:
                    carry = 1
                ans.append(current_digit % 10)
            else:
                current_digit = digits[i] + carry
                if current_digit >= 10: #。
                    carry = 1
                else:
                    carry = 0
                ans.append(current_digit % 10)
        if carry == 1:
            ans.append(carry)
        ans.reverse()
        return ans

if __name__ == "__main__":
    obj = Solution()
    # import ipdb;ipdb.set_trace()

    # s = [9_palindrome-number, 9_palindrome-number,9_palindrome-number]
    # print(s)
    # ans = obj.plusOne(s)
    # print(ans)
    # print('\n---\n')
    #
    # s = [4,3,2,1]
    # print(s)
    # ans = obj.plusOne(s)
    # print(ans)
    # print('\n---\n')
    #
    # s = [9_palindrome-number]
    # print(s)
    # ans = obj.plusOne(s)
    # print(ans)
    # print('\n---\n')

    s = [9,8,7,6,5,4,3,2,1,0]
    print(s)
    ans = obj.plusOne(s)
    print(ans)
    print('\n---\n')