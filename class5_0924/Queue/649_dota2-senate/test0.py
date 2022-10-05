from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """

        q = deque()
        r = 0
        d = 0

        for char in senate:
            if len(q) == 0:
                q.append(char)
                if char == 'R':
                    r += 1
                else:
                    d += 1
            elif char == 'R':
                if d == 0:
                    if q[-1] == 'D':
                        q.pop()
                        r -= 1
                    else:
                        q.append(char)
                        r += 1
                else:
                    d -= 1
            elif char == 'D':
                if r == 0:
                    if q[-1] == 'R':
                        q.pop()
                        d -= 1

                    else:
                        q.append(char)
                        d += 1
                else:
                    r -= 1

        if len(q) == 0:
            q.append(senate[-1])

        return 'Dire' if q[0] == 'D' else 'Radiant'


if __name__ == '__main__':
    obj = Solution()
    senate = 'DRDRDRD'
    res = obj.predictPartyVictory(senate)
    print(res)
