class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # submit accept

        res = []

        def helper(idx, curr, sum):
            if sum == target:
                # The base case if we find the combination sum
                res.append(curr[:])
                # if just append curr then it will be empty
                # since python do not have the list.copy() in python3
                # we can use curr[:]
                return

            if idx > len(candidates) - 1 or sum > target:
                # The base case of if the index out of range or the sum is greater than the target
                return

            # since we want unique combinations we have two options every single time one is take the same element
            # since this element has been taken we can not take the element twice so another option is we do not
            # choose the element
            curr.append(candidates[idx])
            helper(idx, curr, sum + candidates[idx])
            # we take the element and change the total

            curr.pop()
            helper(idx + 1, curr, sum)
            # we pop the element that we add and make the idx + 1 to avoid choose this element

        helper(0, [], 0)
        return res
