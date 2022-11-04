class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        all_sol = []
        sol_so_far = []
        self.workhorse(s, 0, [], all_sol)

        return all_sol


    def workhorse(self, orig, idx, sol_so_far, all_sol):
        if len(sol_so_far) == len(orig):
            all_sol.append("".join(sol_so_far))
            return

        if orig[idx].isdigit():
            sol_so_far.append(orig[idx])
            self.workhorse(orig,idx + 1, sol_so_far, all_sol)
            sol_so_far.pop()
        else:
            sol_so_far.append(orig[idx].upper())
            self.workhorse(orig, idx + 1, sol_so_far, all_sol)
            sol_so_far.pop()
            sol_so_far.append(orig[idx].lower())
            self.workhorse(orig, idx + 1, sol_so_far, all_sol)
            sol_so_far.pop()

if __name__ == '__main__':
    object = Solution()

    s = "a1b2"
    print(object.letterCasePermutation(s))
    s = "3z4"
    print(object.letterCasePermutation(s))