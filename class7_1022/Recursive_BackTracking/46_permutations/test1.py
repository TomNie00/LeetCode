class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # error

        all_sol = []
        sol_so_far = []
        self.workhorse(sol_so_far, 0, all_sol, nums)
        return all_sol

    def workhorse(self, sol_so_far, idx, all_sol, nums):
        if len(nums) <= 0:
            # since we pass the new nums. if the length of new nums is 0 then we go over all the solution then append
            # sol_so_far into all_sol
            all_sol.append(sol_so_far[:])
            return

        if idx >= len(nums):
            # in case out of range
            return

        for i in range(len(nums)):
            # go over every i in the nums
            # two cases

            # one is we add this num into sol_so_far, then we should pop this num out of the nums and after recursive
            # we add it back and pop the num we just add it from sol_so_far

            # second is we do not add this
            num = nums.pop(i)
            sol_so_far.append(num)
            self.workhorse(sol_so_far, idx, all_sol, nums)
            sol_so_far.pop()
            nums.append(num)
            self.workhorse(sol_so_far, idx + 1, all_sol, nums)


if __name__ == '__main__':
    object = Solution()

    nums = [1, 2, 3]
    print(object.permute(nums))
    nums = [0, 1]
    print(object.permute(nums))
    nums = [1]
    print(object.permute(nums))
