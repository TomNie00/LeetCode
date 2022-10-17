class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # submit accept

        if len(nums) <= 1:
            # base case
            return [nums]

        res = []

        for idx, value in enumerate(nums):
            new_nums = nums[:idx] + nums[idx + 1:]
            # ignore the element that we currently be
            for x in self.permute(new_nums):
                res.append([value] + x)

        return res


if __name__ == '__main__':
    object = Solution()

    num = [1,2,3]
    print(object.permute(num))
