import heapq


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # submit accepted

        res = []

        for i in nums:
            heapq.heappush(res, i)

        return [heapq.heappop(res) for i in range(len(res))]

if __name__ == '__main__':
    object = Solution()

    nums = [5, 2, 3, 1]

    print(object.sortArray(nums))