import heapq


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        # submit accept

        dis = []
        res = []

        for i in arr:
            distance = abs(i - x)
            heapq.heappush(dis, (distance, i))

        for idx in range(k):
            res.append(heapq.heappop(dis)[1])

        return sorted(res)

if __name__ == '__main__':
    object = Solution()
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3

    print(object.findClosestElements(arr,k,x))