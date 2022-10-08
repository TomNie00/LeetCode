class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # submit accept

        prefix = min(strs)
        # find the min length in the strs
        if not strs:
            return ''
        for idx, value in enumerate(prefix):
            for word in strs:
                if word[idx] != value:
                    # check this index of every words in the strs equals to this index of prefix
                    return prefix[:idx]

        return prefix
