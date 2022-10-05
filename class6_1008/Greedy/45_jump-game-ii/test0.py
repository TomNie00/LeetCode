class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # submit accept

        right = 0
        cur = -1
        count = 0
        i = 0

        while right < len(nums) - 1:
            if i > cur:
                count += 1
                cur = right
            right = max(right, i + nums[i])
            i += 1

        return count



if __name__ == "__main__":
    obj = Solution()

    nums = [1,2,1,1,1]

    res = obj.jump(nums)

    print(res)
