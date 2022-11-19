import collections


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        q = collections.deque()
        visited = []
        province = 0

        for i in range(len(isConnected)):
            if i not in visited:
                visited.append(i)
                q.append(i)

                while q:
                    curr = q.popleft()
                    for y in range(len(isConnected[curr])):
                        if y not in visited and isConnected[curr][y] == 1:
                            q.append(y)
                            visited.append(y)

                province += 1

        return province



if __name__ == '__main__':
    obj = Solution()

    isConnected = [[1,1,0],[1,1,0],[0,0,1]]

    print(obj.findCircleNum(isConnected))

    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    print(obj.findCircleNum(isConnected))