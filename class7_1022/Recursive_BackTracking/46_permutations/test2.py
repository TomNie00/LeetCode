class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        all_sol = []
        sol_so_far = []
        self.workhorse(sol_so_far, all_sol, nums)
        return all_sol

    def workhorse(self, sol_so_far, all_sol, nums):
        if len(nums) == 0:
            all_sol.append(sol_so_far[:])
            return

        for i in range(len(nums)):
            curr_num = nums.pop(i)
            sol_so_far.append(curr_num)
            self.workhorse(sol_so_far, all_sol, nums)
            sol_so_far.pop()
            nums.insert(i, curr_num)


if __name__ == '__main__':
    object = Solution()

    nums = [1, 2, 3]
    print(object.permute(nums))

