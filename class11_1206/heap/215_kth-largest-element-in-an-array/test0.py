import heapq as hq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # submit

        res = 0
        max_heap = []
        for i in nums:
            hq.heappush(max_heap, -1 * i)

        while k > 0:
            res = hq.heappop(max_heap)
            k -= 1

        return -res

if __name__ == '__main__':
    object = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    print(object.findKthLargest(nums,k))