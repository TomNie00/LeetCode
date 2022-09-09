class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        dir = {'(':')','{':'}','[':']'}
        n = 0

        if s is None or len(s) == 0:
            return False

        if len(s) % 2:
            return False

        for char in s:
            if char in dir:
                stack.append(char)
            elif dir[stack.pop()] != char:
                return False

        return True


if __name__ == '__main__':
    s = ""
    obj = Solution()
    res = False

    res = obj.isValid(s)
    print(res)



