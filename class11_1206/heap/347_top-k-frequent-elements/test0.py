import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # submit accept

        res = []
        counter = collections.Counter(nums)

        for val, count in counter.items():
            if len(res) < k:
                heapq.heappush(res, (count, val))
            else:
                heapq.heappush(res, (count,val))
                heapq.heappop(res)

        return [val for count, val in res]

if __name__ == '__main__':
    object = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(object.topKFrequent(nums, k))