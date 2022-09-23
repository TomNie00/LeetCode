class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        liststr = list(s)

        for i in range(len(liststr)):
            # do not care the character only focus on the '(' and ')'
            if liststr[i] == '(':
                stack.append(i)
            elif liststr[i] == ')':
                if len(stack) == 0:
                    liststr[i] = ''
                    # delete the ')' in i position because there is not one more '(' before it
                else:
                    stack.pop()
                    # match the '(' ')'


        for i in stack:
            liststr[i] = ''
            # delete the single '(' at the i position

        return ''.join(liststr)
        # using .join to create a string made of liststr


if __name__ == '__main__':
    s = "(()"
    obj = Solution()

    res = obj.minRemoveToMakeValid(s)
    print(res)
