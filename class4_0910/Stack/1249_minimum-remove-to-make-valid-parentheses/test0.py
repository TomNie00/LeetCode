class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # time limited
        stack = []
        l = 0
        r = 0
        num = 0
        y = False

        for char in s:
            stack.append(char)
            if char == '(':
                l += 1
            if char == ')':
                if l == 0:
                    stack.pop()
                    y = True
                else:
                    r += 1
        num = l - r
        if num > 0:  # ( 多
            s = ''
            while len(stack) != 0:
                if stack[-1] == ')' and s is None:
                    stack.pop()
                    r -= 1
                if stack[-1] == '(' and l != r:
                    stack.pop()
                    l -= 1
                else:
                    s += stack.pop()
            return s[::-1]
        elif num < 0:
            s = ''
            while len(stack) != 0:
                if stack[-1] == ')' and num + 1 <= 0:
                    stack.pop()
                    num += 1
                else:
                    s += stack.pop()
            return s[::-1]
        elif num == 0:
            s = ''
            if y == True:
                while len(stack) != 0:
                    s += stack.pop()
                return s[::-1]
            else:
                while len(stack) != 0:
                    if stack[-1] == '(' and s is None:
                        stack.pop()
                        l -= 1
                    elif stack[-1] == ')' and l < r:
                        stack.pop()
                        r -= 1
                    else:
                        s += stack.pop()

                return s[::-1]


if __name__ == '__main__':
    s = ")))(("
    obj = Solution()

    res = obj.minRemoveToMakeValid(s)
    print(res)
