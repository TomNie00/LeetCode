class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # This is more like a 2d array.
        # first position has the character, second position has the number of the character
        stack = []
        str = ''


        for i in range(len(s)):
            if len(stack) == 0:
                stack.append([s[i], 1])
            elif s[i] == stack[-1][0]:
                stack[-1][1] = stack[-1][1] + 1
            else:
                stack.append([s[i], 1])

            if stack[-1][1] == k:
                stack.pop()

        for i in range(len(stack)):
            str += stack[i][0] * stack[i][1]

        return str


if __name__ == '__main__':
    s = "deeedbbcccbdaa"
    k = 3
    obj = Solution()

    res = obj.removeDuplicates(s, k)
    print(res)
