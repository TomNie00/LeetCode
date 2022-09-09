class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        char = ''

        if s is None:
            return 0

        if len(s) == 1:
            return int(s)

        for char in s:
            if char == ' ':
                continue
            stack.append(char)

        a = int(stack.pop())
        res = a

        while len(stack) != 0:
            o = stack.pop()
            b = int(stack.pop())
            if o == '+':
                res += b
            elif o == '*':
                res *= b
            elif o == '-':
                res = b - res
            elif o == '/':
                res = b // res

        return res


if __name__ == '__main__':
    s = " 3+5 / 2 "
    obj = Solution()

    res = obj.calculate(s)
    print(res)
