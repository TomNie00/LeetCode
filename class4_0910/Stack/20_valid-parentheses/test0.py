class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        dir = {'(':')','{':'}','[':']'}

        for char in s:
            if char in dir:
                stack.append(char)
            else:
                # right parentheses
                if len(stack) == 0:
                    return False
                if dir[stack.pop()] != char:
                    return False
        if len(stack) > 0:
            return False
        return True


if __name__ == '__main__':
    s = ")("
    obj = Solution()
    res = obj.isValid(s)
    print(res)



