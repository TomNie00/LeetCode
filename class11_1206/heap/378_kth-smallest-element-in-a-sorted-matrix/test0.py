import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        # submit accept but too slow

        arr = []
        res = 0
        for i in matrix:
            arr.extend(i)

        heapq.heapify(arr)

        while k:
            k -= 1
            res = heapq.heappop(arr)

        return res

if __name__ == '__main__':
    object = Solution()

    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8

    print(object.kthSmallest(matrix,k))