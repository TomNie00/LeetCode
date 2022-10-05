from collections import deque
from queue import Queue
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

        # q1 = Queue()
        #
        # for char in s:
        #     q1.put(char)
        #
        # for char in s:
        #     if q.count(char) == 1:
        #         return q.index(char)

        count_dict = {}

        for c in s:
            if c in count_dict:
                count_dict[c] += 1
            else:
                count_dict[c] = 1

        for idx, value in enumerate(s):
            if count_dict[value] == 1:
                return idx

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