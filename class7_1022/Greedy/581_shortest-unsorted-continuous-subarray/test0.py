class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # submit accept
        # since this question do not have a very big range so we can sort first then compare

        new_nums = sorted(nums)

        min = -1
        max = -1
        # set -1 since nums index begins at 0

        for i in range(len(nums)):
            if nums[i] != new_nums[i]:
                if min != -1:
                    # if min has set another value then we change the max value
                    max = i
                else:
                    min = i

        if min != -1 and max != -1:
            # since the subarray need two elements at least so min and max need to be assign a new value if exist
            return max - min + 1
        else:
            return 0


if __name__ == '__main__':
    object = Solution()

    nums = [2,6,4,8,10,9,15]

    print(object.findUnsortedSubarray(nums))
