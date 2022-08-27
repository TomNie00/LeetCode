class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right + left) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return mid


if __name__ == "__main__":
    object = Solution()

    nums = [1, 2, 3, 1]
    # nums = [1, 2, 1, 3, 5, 6, 4]

    result = object.findPeakElement(nums)

    print(result)