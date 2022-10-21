class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # submit accept

        res = []
        candidates.sort()

        def helper(start, curr, target):
            # set the index to start for easy understanding the new start position
            if target == 0:
                res.append(curr[:])
            if target <= 0:
                return

            prev = -1
            for i in range(start, len(candidates)):
                # since we do not want to contain the duplicate combinations so we set the start position as start
                # then we can avoid the same value
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                helper(i + 1, curr, target - candidates[i])
                curr.pop()
                prev = candidates[i]

        helper(0, [], target)
        return res