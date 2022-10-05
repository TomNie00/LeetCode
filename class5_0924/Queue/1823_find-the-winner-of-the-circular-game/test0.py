from collections import deque
class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        q = deque()

        for i in range(1, n+1):
            q.append(i)

        while len(q) > 1:
            num = 1
            while num != k:
                q.append(q.popleft())
                num += 1
            if num == k:
                q.popleft()

        return q[0]

