class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        str1 = min(strs)
        ans = ""

        if len(strs) == 1:
            return strs[0]

        for string in strs:
            for i in range(len(str1) - 1):
                if str1[i] != string[i]:
                    ans = str1[: i]
                    return ans


if __name__ == "__main__":
    obj = Solution()

    strs = ["flower", "flow", "flight"]
    # strs = ["dog", "racecar", "car"]
    result = obj.longestCommonPrefix(strs)
    print(result)