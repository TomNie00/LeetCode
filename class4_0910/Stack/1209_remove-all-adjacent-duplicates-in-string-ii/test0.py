class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        stack = []
        char = ''
        temp = ''
        comp = ''
        n = 0
        l = -1
        str = s

        if s is None or k > len(s):
            return s

        while True:
            for char in str:
                if char != comp:
                    temp = ''
                if len(stack) == 0:
                    comp = char
                    stack.append(char)
                else:
                    if comp != char:
                        comp = char
                        stack.append(char)
                    else:
                        if temp == '':
                            temp += char
                        temp += char
                        stack.append(char)
                        if len(temp) == k:
                            for i in range(len(temp)):
                                stack.pop()
                            temp = ''
            if l != len(stack):
                l = len(stack)
            else:
                break
            str = ''
            while len(stack) != 0:
                str += stack.pop()
            str = str[::-1]
            comp = ''

        return str


if __name__ == '__main__':
    s = "deeedbbcccbdaa"
    k = 3
    obj = Solution()

    res = obj.removeDuplicates(s, k)
    print(res)
