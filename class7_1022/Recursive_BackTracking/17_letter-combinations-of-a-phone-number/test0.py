class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # submit accept

        res = []
        letter_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def helper(idx, curr):
            # i will record the idx that we at and curr_digit will keep the output that we have right now
            if len(curr) == len(digits):
                res.append(curr)
                return
            # The base case of if the length are equal when the curr_digit equal to the digits. we add to our res

            for char in letter_dict[digits[idx]]:
                helper(idx + 1, curr + char)
                # move idx to the next and then curr will be added char

        if digits:
            # if digits is not None then we do the function
            # if it is None then we just return res which is []
            helper(0, "")
        return res
