from collections import deque
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # for char in s:
        #     if s.count(char) == 1:
        #         return s.index(char)
        # more faster than below but still run out of time

        q = deque()

        for char in s:
            q.append(char)

        for char in s:
            if q.count(char) == 1:
                return q.index(char)

        return -1

if __name__ == '__main__':
    with open('timeout.txt') as f:
        lines = f.readlines()
    timeout = lines[0]
    s = timeout
    # s = "leetcode"
    obj = Solution()
    res = obj.firstUniqChar(s)
    print(res)